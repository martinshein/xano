---
title: "Delete Record - Remove Database Records Safely"
description: "Learn how to safely delete records from your Xano database with soft deletion, cascading operations, and data integrity protection"
category: data-operations
tags:
  - Delete Record
  - Soft Delete
  - Data Removal
  - Cascading Deletes
  - Data Integrity
  - Backup Strategies
difficulty: intermediate
reading_time: 10 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of databases
  - Knowledge of Xano tables and relationships
  - Familiarity with function stacks
  - Understanding of Get Record operations
---

# Delete Record - Remove Database Records Safely

## 📋 **Quick Summary**

**What it does:** Delete Record removes records from your Xano database tables with options for soft deletion, cascading operations, and data integrity protection to ensure safe data removal.

**Why it matters:** Delete Record enables you to:
- **Remove outdated data** while maintaining referential integrity
- **Implement soft deletion** for data recovery
- **Handle cascading deletes** across related tables
- **Maintain audit trails** of deletion activities
- **Build data retention policies** and cleanup processes

**Time to implement:** 3-5 minutes for basic deletion, 15-25 minutes with soft deletion and cascading operations

---

## What You'll Learn

- Safe record deletion strategies and best practices
- Implementing soft deletion for data recovery
- Handling cascading deletes and relationship cleanup
- Building comprehensive deletion audit trails
- Advanced deletion patterns for complex scenarios

## Basic Delete Operations

### Simple Record Deletion

```javascript
// Basic delete record example
const deletedRecord = await deleteRecord({
  table: 'users',
  id: 123
});

if (deletedRecord) {
  console.log('User deleted successfully');
} else {
  console.log('User not found or already deleted');
}
```

### Safe Delete with Validation

```javascript
// Comprehensive delete function with safety checks
function safeDeleteUser(userId, currentUserId, options = {}) {
  try {
    // 1. Validate permissions
    if (!userId || !currentUserId) {
      throw new Error('User ID and current user ID are required');
    }
    
    // 2. Get the record to check permissions and relationships
    const userToDelete = getRecord({
      table: 'users',
      id: userId
    });
    
    if (!userToDelete) {
      return {
        success: false,
        error: 'User not found',
        code: 'USER_NOT_FOUND'
      };
    }
    
    // 3. Check deletion permissions
    const canDelete = checkDeletePermissions(userToDelete, currentUserId);
    if (!canDelete) {
      throw new Error('Permission denied: Cannot delete this user');
    }
    
    // 4. Check for dependencies that would prevent deletion
    const dependencies = checkUserDependencies(userId);
    if (dependencies.hasBlockingDependencies && !options.force) {
      return {
        success: false,
        error: 'Cannot delete user with active dependencies',
        code: 'HAS_DEPENDENCIES',
        dependencies: dependencies.details
      };
    }
    
    // 5. Perform soft delete by default, hard delete if specified
    let result;
    if (options.hardDelete) {
      result = performHardDelete(userId, currentUserId, dependencies);
    } else {
      result = performSoftDelete(userId, currentUserId);
    }
    
    // 6. Log the deletion for audit trail
    logDeletion(userId, currentUserId, userToDelete, options);
    
    return {
      success: true,
      deleted_user: result,
      deletion_type: options.hardDelete ? 'hard' : 'soft',
      message: 'User deleted successfully'
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message,
      code: 'DELETE_FAILED'
    };
  }
}

function checkDeletePermissions(user, currentUserId) {
  // Users can delete their own account, admins can delete any account
  return user.id === currentUserId || isAdmin(currentUserId);
}

function checkUserDependencies(userId) {
  // Check for orders
  const activeOrders = queryAllRecords({
    table: 'orders',
    filters: {
      customer_id: userId,
      status: { $in: ['pending', 'processing', 'shipped'] }
    },
    limit: 1
  });
  
  // Check for active subscriptions
  const activeSubscriptions = queryAllRecords({
    table: 'subscriptions',
    filters: {
      user_id: userId,
      status: 'active'
    },
    limit: 1
  });
  
  const hasBlockingDependencies = activeOrders.length > 0 || activeSubscriptions.length > 0;
  
  return {
    hasBlockingDependencies,
    details: {
      active_orders: activeOrders.length,
      active_subscriptions: activeSubscriptions.length
    }
  };
}
```

## Soft Deletion Implementation

### Soft Delete Strategy

```javascript
// Implement soft deletion to allow data recovery
function performSoftDelete(userId, deletedBy) {
  const deletionTimestamp = new Date().toISOString();
  
  // Mark user as deleted instead of removing
  const softDeletedUser = editRecord({
    table: 'users',
    id: userId,
    data: {
      deleted_at: deletionTimestamp,
      deleted_by: deletedBy,
      status: 'deleted',
      // Preserve original email but make it unique for future registrations
      original_email: null, // Will be set below
      email: `deleted_${userId}_${Date.now()}@deleted.local`
    }
  });
  
  // Store original email for potential recovery
  if (softDeletedUser) {
    editRecord({
      table: 'users',
      id: userId,
      data: {
        original_email: softDeletedUser.email
      }
    });
  }
  
  return softDeletedUser;
}

// Soft delete with cascading to related records
class SoftDeleteManager {
  static async softDeleteWithCascade(table, recordId, deletedBy, options = {}) {
    const deletionTimestamp = new Date().toISOString();
    
    // Get the main record
    const mainRecord = getRecord({ table, id: recordId });
    if (!mainRecord) {
      throw new Error('Record not found');
    }
    
    // Soft delete the main record
    const deletedRecord = editRecord({
      table: table,
      id: recordId,
      data: {
        deleted_at: deletionTimestamp,
        deleted_by: deletedBy,
        status: 'deleted'
      }
    });
    
    // Handle cascading soft deletes based on table
    const cascadeResults = await this.handleCascadingSoftDeletes(
      table, 
      recordId, 
      deletedBy, 
      deletionTimestamp,
      options
    );
    
    return {
      main_record: deletedRecord,
      cascade_results: cascadeResults,
      deleted_at: deletionTimestamp
    };
  }
  
  static async handleCascadingSoftDeletes(table, recordId, deletedBy, timestamp, options) {
    const results = {};
    
    switch (table) {
      case 'users':
        // Soft delete user's posts
        results.posts = await this.softDeleteRelated('posts', {
          author_id: recordId,
          deleted_at: null
        }, deletedBy, timestamp);
        
        // Soft delete user's comments
        results.comments = await this.softDeleteRelated('comments', {
          user_id: recordId,
          deleted_at: null
        }, deletedBy, timestamp);
        
        // Cancel active subscriptions instead of deleting
        results.subscriptions = await this.cancelUserSubscriptions(recordId, deletedBy);
        break;
      
      case 'posts':
        // Soft delete associated comments
        results.comments = await this.softDeleteRelated('comments', {
          post_id: recordId,
          deleted_at: null
        }, deletedBy, timestamp);
        break;
      
      case 'categories':
        // Move posts to "uncategorized" instead of deleting
        results.posts = await this.movePostsToUncategorized(recordId);
        break;
    }
    
    return results;
  }
  
  static async softDeleteRelated(table, filters, deletedBy, timestamp) {
    const relatedRecords = queryAllRecords({ table, filters });
    
    const results = [];
    for (const record of relatedRecords) {
      try {
        const updated = editRecord({
          table: table,
          id: record.id,
          data: {
            deleted_at: timestamp,
            deleted_by: deletedBy,
            status: 'deleted'
          }
        });
        results.push({ success: true, id: record.id, record: updated });
      } catch (error) {
        results.push({ success: false, id: record.id, error: error.message });
      }
    }
    
    return results;
  }
  
  static async cancelUserSubscriptions(userId, canceledBy) {
    const activeSubscriptions = queryAllRecords({
      table: 'subscriptions',
      filters: {
        user_id: userId,
        status: 'active'
      }
    });
    
    const results = [];
    for (const subscription of activeSubscriptions) {
      try {
        const canceled = editRecord({
          table: 'subscriptions',
          id: subscription.id,
          data: {
            status: 'canceled',
            canceled_at: new Date().toISOString(),
            canceled_by: canceledBy,
            cancel_reason: 'user_account_deleted'
          }
        });
        results.push({ success: true, id: subscription.id, record: canceled });
      } catch (error) {
        results.push({ success: false, id: subscription.id, error: error.message });
      }
    }
    
    return results;
  }
}
```

### Data Recovery from Soft Deletion

```javascript
// Restore soft-deleted records
class DataRecoveryManager {
  static async restoreSoftDeletedRecord(table, recordId, restoredBy) {
    // Get the soft-deleted record
    const deletedRecord = getRecord({ table, id: recordId });
    
    if (!deletedRecord || !deletedRecord.deleted_at) {
      throw new Error('Record not found or not soft-deleted');
    }
    
    // Prepare restoration data
    const restorationData = {
      deleted_at: null,
      deleted_by: null,
      status: 'active',
      restored_at: new Date().toISOString(),
      restored_by: restoredBy
    };
    
    // For users, restore original email if available
    if (table === 'users' && deletedRecord.original_email) {
      // Check if original email is now available
      const emailConflict = queryAllRecords({
        table: 'users',
        filters: {
          email: deletedRecord.original_email,
          deleted_at: null
        },
        limit: 1
      })[0];
      
      if (!emailConflict) {
        restorationData.email = deletedRecord.original_email;
        restorationData.original_email = null;
      } else {
        throw new Error('Cannot restore: original email is now taken by another user');
      }
    }
    
    // Restore the record
    const restoredRecord = editRecord({
      table: table,
      id: recordId,
      data: restorationData
    });
    
    // Log restoration
    addRecord({
      table: 'restoration_logs',
      data: {
        table_name: table,
        record_id: recordId,
        restored_by: restoredBy,
        original_deletion_date: deletedRecord.deleted_at,
        restored_at: restorationData.restored_at
      }
    });
    
    return restoredRecord;
  }
  
  static async bulkRestoreRecords(table, recordIds, restoredBy) {
    const results = {
      successful: [],
      failed: []
    };
    
    for (const recordId of recordIds) {
      try {
        const restored = await this.restoreSoftDeletedRecord(table, recordId, restoredBy);
        results.successful.push({ id: recordId, record: restored });
      } catch (error) {
        results.failed.push({ id: recordId, error: error.message });
      }
    }
    
    return results;
  }
  
  // List soft-deleted records for recovery interface
  static getSoftDeletedRecords(table, options = {}) {
    const filters = { deleted_at: { $ne: null } };
    
    // Add date range filter if specified
    if (options.deletedAfter) {
      filters.deleted_at = { ...filters.deleted_at, $gte: options.deletedAfter };
    }
    
    if (options.deletedBefore) {
      filters.deleted_at = { ...filters.deleted_at, $lte: options.deletedBefore };
    }
    
    return queryAllRecords({
      table: table,
      filters: filters,
      sort: [{ field: 'deleted_at', direction: 'desc' }],
      limit: options.limit || 50
    });
  }
}
```

## Hard Deletion with Safety

### Protected Hard Delete

```javascript
// Hard delete with comprehensive safety checks
function performHardDelete(userId, deletedBy, dependencies) {
  // 1. Create backup before deletion
  const backup = createDeletionBackup(userId);
  
  try {
    // 2. Clean up related data in order
    const cleanupResults = performCascadingCleanup(userId, deletedBy);
    
    // 3. Delete the main record
    const deletedUser = deleteRecord({
      table: 'users',
      id: userId
    });
    
    // 4. Log successful deletion
    addRecord({
      table: 'hard_deletion_logs',
      data: {
        table_name: 'users',
        record_id: userId,
        deleted_by: deletedBy,
        backup_id: backup.id,
        cleanup_results: cleanupResults,
        deleted_at: new Date().toISOString()
      }
    });
    
    return deletedUser;
    
  } catch (error) {
    // 5. If deletion fails, restore from backup
    restoreFromBackup(backup);
    throw error;
  }
}

function createDeletionBackup(userId) {
  const timestamp = new Date().toISOString();
  
  // Get main user record
  const user = getRecord({ table: 'users', id: userId });
  
  // Get related data
  const userPosts = queryAllRecords({
    table: 'posts',
    filters: { author_id: userId }
  });
  
  const userComments = queryAllRecords({
    table: 'comments',
    filters: { user_id: userId }
  });
  
  const userOrders = queryAllRecords({
    table: 'orders',
    filters: { customer_id: userId }
  });
  
  // Create backup record
  const backup = addRecord({
    table: 'deletion_backups',
    data: {
      user_id: userId,
      backup_data: {
        user: user,
        posts: userPosts,
        comments: userComments,
        orders: userOrders
      },
      created_at: timestamp,
      backup_type: 'pre_hard_delete'
    }
  });
  
  return backup;
}

function performCascadingCleanup(userId, deletedBy) {
  const results = {};
  
  try {
    // Delete comments first (no dependencies)
    results.comments = deleteRecordsByFilter('comments', {
      user_id: userId
    });
    
    // Delete posts (after comments are handled)
    results.posts = deleteRecordsByFilter('posts', {
      author_id: userId
    });
    
    // Handle orders (convert to anonymous)
    results.orders = anonymizeUserOrders(userId);
    
    // Delete user sessions
    results.sessions = deleteRecordsByFilter('user_sessions', {
      user_id: userId
    });
    
    // Delete user preferences
    results.preferences = deleteRecordsByFilter('user_preferences', {
      user_id: userId
    });
    
    return results;
    
  } catch (error) {
    throw new Error(`Cascading cleanup failed: ${error.message}`);
  }
}

function deleteRecordsByFilter(table, filters) {
  const records = queryAllRecords({ table, filters });
  const deleted = [];
  
  for (const record of records) {
    try {
      deleteRecord({ table, id: record.id });
      deleted.push(record.id);
    } catch (error) {
      console.warn(`Failed to delete ${table} record ${record.id}:`, error.message);
    }
  }
  
  return { count: deleted.length, ids: deleted };
}

function anonymizeUserOrders(userId) {
  const userOrders = queryAllRecords({
    table: 'orders',
    filters: { customer_id: userId }
  });
  
  const anonymized = [];
  
  for (const order of userOrders) {
    try {
      const updated = editRecord({
        table: 'orders',
        id: order.id,
        data: {
          customer_id: null,
          customer_name: 'Anonymous User',
          customer_email: 'deleted@anonymous.local',
          anonymized_at: new Date().toISOString(),
          original_customer_id: userId
        }
      });
      anonymized.push(order.id);
    } catch (error) {
      console.warn(`Failed to anonymize order ${order.id}:`, error.message);
    }
  }
  
  return { count: anonymized.length, ids: anonymized };
}
```

## No-Code Platform Integration

### 🔗 **n8n Integration**

```javascript
// n8n workflow for safe record deletion
function deleteRecordWorkflow($input) {
  const params = $input.body || $input.query;
  
  try {
    // Validate required parameters
    if (!params.table || !params.id) {
      return {
        success: false,
        error: 'Table and record ID are required'
      };
    }
    
    // Get current record to check if it exists
    const currentRecord = getRecord({
      table: params.table,
      id: params.id
    });
    
    if (!currentRecord) {
      return {
        success: false,
        error: 'Record not found',
        code: 'NOT_FOUND'
      };
    }
    
    // Check deletion permissions
    if (params.check_permissions && params.user_id) {
      const canDelete = checkDeletionPermissions(params.table, currentRecord, params.user_id);
      if (!canDelete) {
        return {
          success: false,
          error: 'Permission denied',
          code: 'ACCESS_DENIED'
        };
      }
    }
    
    // Check for dependencies if specified
    if (params.check_dependencies) {
      const dependencies = checkRecordDependencies(params.table, params.id);
      if (dependencies.hasBlockingDependencies && !params.force_delete) {
        return {
          success: false,
          error: 'Record has dependencies that prevent deletion',
          code: 'HAS_DEPENDENCIES',
          dependencies: dependencies.details
        };
      }
    }
    
    // Perform deletion based on type
    let result;
    if (params.soft_delete) {
      result = performSoftDeletion(params.table, params.id, params.user_id);
    } else {
      result = performHardDeletion(params.table, params.id, params.user_id, params);
    }
    
    // Log deletion activity
    if (params.log_activity) {
      logDeletionActivity(params.table, params.id, currentRecord, params.user_id, params);
    }
    
    return {
      success: true,
      deleted_record: result,
      deletion_type: params.soft_delete ? 'soft' : 'hard',
      metadata: {
        table: params.table,
        id: params.id,
        deleted_at: new Date().toISOString()
      }
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message,
      code: 'DELETE_ERROR'
    };
  }
}
```

### 🌐 **WeWeb Integration**

```javascript
// WeWeb deletion handling with user confirmation
class WeWebDeleteHandler {
  static async confirmAndDelete(table, recordId, options = {}) {
    try {
      // Get record for confirmation display
      const record = wwLib.variables[`current_${table}`] || 
                    await this.loadRecord(table, recordId);
      
      if (!record) {
        wwLib.showAlert('Record not found', 'error');
        return false;
      }
      
      // Show confirmation dialog
      const confirmed = await this.showDeleteConfirmation(record, options);
      if (!confirmed) return false;
      
      // Show loading state
      wwLib.showLoading();
      
      // Prepare deletion request
      const deletePayload = {
        soft_delete: options.softDelete !== false, // Default to soft delete
        user_id: wwLib.auth.getUserId(),
        check_dependencies: true,
        log_activity: true
      };
      
      // Submit deletion request
      const response = await wwLib.api.delete({
        url: `${wwLib.envVars.XANO_API_URL}/${table}/${recordId}`,
        data: deletePayload,
        headers: {
          'Authorization': 'Bearer ' + wwLib.auth.getAuthToken(),
          'Content-Type': 'application/json'
        }
      });
      
      if (response.data.success) {
        // Update local data
        this.handleSuccessfulDeletion(table, recordId, response.data);
        
        // Show success message
        const message = response.data.deletion_type === 'soft' 
          ? 'Record moved to trash successfully'
          : 'Record deleted permanently';
        
        wwLib.showAlert(message, 'success');
        return true;
        
      } else if (response.data.code === 'HAS_DEPENDENCIES') {
        // Handle dependency conflicts
        this.handleDependencyConflict(response.data, table, recordId, options);
        return false;
        
      } else {
        wwLib.showAlert(response.data.error || 'Deletion failed', 'error');
        return false;
      }
      
    } catch (error) {
      console.error('Deletion error:', error);
      wwLib.showAlert('An error occurred during deletion', 'error');
      return false;
    } finally {
      wwLib.hideLoading();
    }
  }
  
  static async showDeleteConfirmation(record, options) {
    const recordType = options.recordType || 'record';
    const recordName = record.name || record.title || `ID ${record.id}`;
    
    return new Promise((resolve) => {
      wwLib.showDialog({
        title: `Delete ${recordType}`,
        message: `Are you sure you want to delete "${recordName}"? ${
          options.softDelete !== false 
            ? 'This will move it to the trash where it can be recovered.'
            : 'This action cannot be undone!'
        }`,
        buttons: [
          {
            text: 'Cancel',
            action: () => resolve(false)
          },
          {
            text: options.softDelete !== false ? 'Move to Trash' : 'Delete Permanently',
            action: () => resolve(true),
            style: 'danger'
          }
        ]
      });
    });
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Build a basic record deletion system:
1. Create a function to safely delete a user record
2. Implement basic permission checking
3. Add simple soft deletion functionality
4. Test with valid and invalid scenarios

### Intermediate Challenge
Create an advanced deletion system:
1. Implement cascading soft deletes for related records
2. Add data recovery functionality
3. Build dependency checking before deletion
4. Create comprehensive deletion audit trails

### Advanced Challenge
Design a complete data lifecycle management system:
1. Implement automated data retention policies
2. Add bulk deletion with rollback capabilities
3. Create real-time dependency tracking
4. Build advanced recovery and restoration tools

## Common Mistakes to Avoid

1. **No permission checks** - Always verify user can delete the record
2. **Ignoring dependencies** - Check for related data before deletion
3. **No backup strategy** - Create backups before hard deletes
4. **Missing audit trails** - Log all deletion activities
5. **Hard delete by default** - Use soft deletion for recoverable data
6. **No cascade handling** - Handle related record cleanup properly

## Best Practices

1. **Prefer soft deletion** - Use hard deletion only when necessary
2. **Check permissions first** - Verify user authorization before deletion
3. **Handle dependencies** - Check and manage related data properly
4. **Create audit trails** - Log all deletion activities with details
5. **Implement recovery** - Provide ways to restore soft-deleted data
6. **Use transactions** - Ensure atomic deletion operations

## Next Steps

- Learn [Patch Record](patch_record.md) for partial updates
- Master [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for complex operations
- Explore [Data Validation](../best-practices/validation.md) for integrity checking
- Understand [Backup Strategies](../best-practices/backup-recovery.md) for data protection

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Record deletion discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Deletion implementation guides
- 📖 [Data Safety Guide](../best-practices/data-safety.md) - Safe deletion strategies
- 🔧 [Support](https://xano.com/support) - Database operation assistance