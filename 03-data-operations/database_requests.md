---
title: "Database Requests - Complete CRUD Operations Guide"
description: "Master all database request operations in Xano including Create, Read, Update, Delete with advanced querying, filtering, and performance optimization"
category: data-operations
tags:
  - Database Requests
  - CRUD Operations
  - Query Operations
  - Database Functions
  - Data Management
  - Performance Optimization
difficulty: beginner
reading_time: 12 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of databases
  - Knowledge of Xano tables and relationships
  - Familiarity with function stacks
---

# Database Requests - Complete CRUD Operations Guide

## 📋 **Quick Summary**

**What it does:** Database requests are the core functions for interacting with your Xano database, providing Create, Read, Update, and Delete (CRUD) operations with advanced querying capabilities.

**Why it matters:** Database requests enable you to:
- **Manage all data operations** in your applications
- **Build scalable data workflows** with efficient queries
- **Implement complex business logic** with database transactions
- **Optimize performance** with proper indexing and filtering
- **Ensure data integrity** with validation and constraints

**Time to implement:** 10-15 minutes for basic operations, 1+ hour for complex multi-table workflows

---

## What You'll Learn

- Complete overview of all database request types
- Advanced querying and filtering techniques
- Performance optimization strategies
- Transaction and bulk operation patterns
- Integration with no-code platforms

## Core Database Operations

### 📝 **Create Operations**

Add new data to your database tables.

```javascript
// Add Record - Create single record
const newUser = await addRecord({
  table: 'users',
  data: {
    email: 'john@example.com',
    name: 'John Doe',
    status: 'active',
    created_at: new Date().toISOString()
  }
});

// Bulk Operations - Create multiple records
const newUsers = await bulkAdd({
  table: 'users',
  data: [
    { email: 'user1@example.com', name: 'User One' },
    { email: 'user2@example.com', name: 'User Two' },
    { email: 'user3@example.com', name: 'User Three' }
  ]
});

// Add or Edit Record - Upsert operation
const upsertUser = await addOrEditRecord({
  table: 'users',
  filters: { email: 'john@example.com' },
  data: {
    email: 'john@example.com',
    name: 'John Doe Updated',
    last_login: new Date().toISOString()
  }
});
```

### 🔍 **Read Operations**

Retrieve data from your database with various query methods.

```javascript
// Get Record - Retrieve single record by ID
const user = await getRecord({
  table: 'users',
  id: 123
});

// Query All Records - Retrieve multiple records with filters
const activeUsers = await queryAllRecords({
  table: 'users',
  filters: {
    status: 'active',
    created_at: { $gte: '2024-01-01' }
  },
  sort: [{ field: 'created_at', direction: 'desc' }],
  limit: 50,
  offset: 0
});

// Advanced filtering with relationships
const usersWithProfiles = await queryAllRecords({
  table: 'users',
  include: ['profile', 'orders'],
  filters: {
    'profile.subscription_status': 'premium',
    'orders.total': { $gte: 100 }
  }
});
```

### ✏️ **Update Operations**

Modify existing data in your database.

```javascript
// Edit Record - Update complete record
const updatedUser = await editRecord({
  table: 'users',
  id: 123,
  data: {
    name: 'John Smith',
    email: 'johnsmith@example.com',
    updated_at: new Date().toISOString()
  }
});

// Patch Record - Partial updates
const patchedUser = await patchRecord({
  table: 'users',
  id: 123,
  fields: {
    last_login: new Date().toISOString(),
    login_count: { increment: 1 }
  }
});

// Bulk update multiple records
const bulkUpdate = await bulkEdit({
  table: 'users',
  filters: { status: 'inactive' },
  data: {
    status: 'archived',
    archived_at: new Date().toISOString()
  }
});
```

### 🗑️ **Delete Operations**

Remove data from your database safely.

```javascript
// Delete Record - Remove single record
const deletedUser = await deleteRecord({
  table: 'users',
  id: 123
});

// Soft delete (recommended)
const softDeleteUser = await patchRecord({
  table: 'users',
  id: 123,
  fields: {
    deleted_at: new Date().toISOString(),
    status: 'deleted'
  }
});

// Bulk delete with filters
const bulkDelete = await bulkDelete({
  table: 'temp_users',
  filters: {
    created_at: { $lt: '2024-01-01' },
    status: 'unverified'
  }
});
```

## Advanced Database Patterns

### Complex Query Builder

```javascript
// Advanced multi-table query function
class DatabaseQueryBuilder {
  static async buildUserDashboardData(userId) {
    // Get user with related data
    const user = await getRecord({
      table: 'users',
      id: userId,
      include: ['profile', 'subscription']
    });
    
    if (!user) {
      throw new Error('User not found');
    }
    
    // Get recent orders
    const recentOrders = await queryAllRecords({
      table: 'orders',
      filters: {
        customer_id: userId,
        created_at: { $gte: this.getDateDaysAgo(30) }
      },
      sort: [{ field: 'created_at', direction: 'desc' }],
      limit: 10,
      include: ['items.product']
    });
    
    // Get analytics data
    const analytics = await this.getUserAnalytics(userId);
    
    // Get notifications
    const notifications = await queryAllRecords({
      table: 'notifications',
      filters: {
        user_id: userId,
        read_at: null
      },
      sort: [{ field: 'created_at', direction: 'desc' }],
      limit: 5
    });
    
    return {
      user: user,
      recent_orders: recentOrders,
      analytics: analytics,
      unread_notifications: notifications,
      dashboard_generated_at: new Date().toISOString()
    };
  }
  
  static async getUserAnalytics(userId) {
    // Aggregate user data
    const orderStats = await queryAllRecords({
      table: 'orders',
      filters: { customer_id: userId },
      aggregate: {
        total_spent: { $sum: 'total_amount' },
        order_count: { $count: '*' },
        avg_order_value: { $avg: 'total_amount' },
        last_order_date: { $max: 'created_at' }
      }
    });
    
    return {
      lifetime_value: orderStats.total_spent || 0,
      total_orders: orderStats.order_count || 0,
      average_order_value: orderStats.avg_order_value || 0,
      last_purchase: orderStats.last_order_date,
      customer_since: this.getCustomerStartDate(userId)
    };
  }
  
  static getDateDaysAgo(days) {
    const date = new Date();
    date.setDate(date.getDate() - days);
    return date.toISOString();
  }
}
```

### Database Transaction Patterns

```javascript
// Complex e-commerce transaction
async function processOrderTransaction(orderData) {
  // Start transaction
  const transaction = await startTransaction();
  
  try {
    // 1. Create order
    const order = await addRecord({
      table: 'orders',
      data: {
        customer_id: orderData.customer_id,
        total_amount: orderData.total,
        status: 'processing',
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 2. Create order items and update inventory
    for (const item of orderData.items) {
      // Add order item
      await addRecord({
        table: 'order_items',
        data: {
          order_id: order.id,
          product_id: item.product_id,
          quantity: item.quantity,
          unit_price: item.price,
          total_price: item.quantity * item.price
        },
        transaction: transaction
      });
      
      // Update inventory
      const inventoryUpdate = await patchRecord({
        table: 'inventory',
        filters: { product_id: item.product_id },
        fields: {
          quantity: { decrement: item.quantity },
          reserved_quantity: { decrement: item.quantity }
        },
        transaction: transaction
      });
      
      // Check if inventory went negative
      if (inventoryUpdate.quantity < 0) {
        throw new Error(`Insufficient inventory for product ${item.product_id}`);
      }
    }
    
    // 3. Update customer statistics
    await patchRecord({
      table: 'customers',
      id: orderData.customer_id,
      fields: {
        total_orders: { increment: 1 },
        total_spent: { increment: orderData.total },
        last_order_date: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 4. Create audit log
    await addRecord({
      table: 'audit_logs',
      data: {
        action: 'order_created',
        entity_type: 'order',
        entity_id: order.id,
        user_id: orderData.customer_id,
        details: { order_total: orderData.total, item_count: orderData.items.length },
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // Commit transaction
    await commitTransaction(transaction);
    
    return {
      success: true,
      order: order,
      message: 'Order processed successfully'
    };
    
  } catch (error) {
    // Rollback on error
    await rollbackTransaction(transaction);
    
    return {
      success: false,
      error: error.message,
      code: 'TRANSACTION_FAILED'
    };
  }
}
```

## Performance Optimization

### Efficient Query Patterns

```javascript
// Performance-optimized query strategies
class QueryOptimizer {
  static async getOptimizedUserList(filters = {}) {
    // Use pagination for large datasets
    const pageSize = filters.limit || 50;
    const offset = filters.offset || 0;
    
    // Select only needed fields
    const users = await queryAllRecords({
      table: 'users',
      fields: ['id', 'name', 'email', 'status', 'created_at'],
      filters: {
        status: filters.status || 'active',
        ...filters.additionalFilters
      },
      sort: [{ field: 'created_at', direction: 'desc' }],
      limit: pageSize,
      offset: offset
    });
    
    // Get total count separately if needed
    const totalCount = filters.includeCount ? 
      await this.getFilteredUserCount(filters) : null;
    
    return {
      users: users,
      pagination: {
        page: Math.floor(offset / pageSize) + 1,
        page_size: pageSize,
        total_count: totalCount,
        has_more: users.length === pageSize
      }
    };
  }
  
  static async getFilteredUserCount(filters) {
    const result = await queryAllRecords({
      table: 'users',
      filters: {
        status: filters.status || 'active',
        ...filters.additionalFilters
      },
      aggregate: {
        count: { $count: '*' }
      }
    });
    
    return result.count || 0;
  }
  
  // Batch loading for related data
  static async loadUsersWithRelatedData(userIds) {
    // Load users in batch
    const users = await queryAllRecords({
      table: 'users',
      filters: {
        id: { $in: userIds }
      }
    });
    
    // Load related profiles in batch
    const profiles = await queryAllRecords({
      table: 'user_profiles',
      filters: {
        user_id: { $in: userIds }
      }
    });
    
    // Load recent orders in batch
    const recentOrders = await queryAllRecords({
      table: 'orders',
      filters: {
        customer_id: { $in: userIds },
        created_at: { $gte: this.getDateDaysAgo(30) }
      },
      sort: [{ field: 'created_at', direction: 'desc' }]
    });
    
    // Combine data efficiently
    const profileMap = new Map(profiles.map(p => [p.user_id, p]));
    const orderMap = new Map();
    
    recentOrders.forEach(order => {
      if (!orderMap.has(order.customer_id)) {
        orderMap.set(order.customer_id, []);
      }
      orderMap.get(order.customer_id).push(order);
    });
    
    return users.map(user => ({
      ...user,
      profile: profileMap.get(user.id) || null,
      recent_orders: orderMap.get(user.id) || []
    }));
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Database Workflows**

```javascript
// n8n workflow for automated data processing
function processDataWorkflow($input) {
  const trigger = $input.trigger;
  
  switch (trigger.event) {
    case 'user_registered':
      return processNewUser($input.user);
    case 'order_completed':
      return processCompletedOrder($input.order);
    case 'subscription_changed':
      return processSubscriptionChange($input.subscription);
    default:
      return { error: 'Unknown event type' };
  }
}

async function processNewUser(userData) {
  // Create user profile
  const profile = await addRecord({
    table: 'user_profiles',
    data: {
      user_id: userData.id,
      display_name: userData.name,
      onboarding_step: 1,
      created_at: new Date().toISOString()
    }
  });
  
  // Create default preferences
  await addRecord({
    table: 'user_preferences',
    data: {
      user_id: userData.id,
      email_notifications: true,
      marketing_emails: true,
      theme: 'light',
      language: 'en'
    }
  });
  
  // Add to default segment
  await addRecord({
    table: 'user_segments',
    data: {
      user_id: userData.id,
      segment_name: 'new_users',
      added_at: new Date().toISOString()
    }
  });
  
  return {
    success: true,
    profile_created: true,
    preferences_set: true,
    segment_assigned: true
  };
}
```

### 🌐 **WeWeb Data Management**

```javascript
// WeWeb data management utilities
class WeWebDataManager {
  static async loadDashboardData() {
    try {
      // Show loading indicator
      wwLib.showLoading();
      
      // Load user data
      const userData = await wwLib.api.get({
        url: `${wwLib.envVars.XANO_API_URL}/users/me`,
        headers: { 'Authorization': 'Bearer ' + wwLib.auth.getAuthToken() }
      });
      
      // Load dashboard metrics
      const metricsData = await wwLib.api.get({
        url: `${wwLib.envVars.XANO_API_URL}/users/me/metrics`,
        headers: { 'Authorization': 'Bearer ' + wwLib.auth.getAuthToken() }
      });
      
      // Update WeWeb collections
      wwLib.collections.currentUser.update(userData.data);
      wwLib.collections.userMetrics.update(metricsData.data);
      
      // Update variables
      wwLib.variables.lastDataLoad = new Date().toISOString();
      wwLib.variables.dashboardReady = true;
      
      return true;
      
    } catch (error) {
      console.error('Dashboard data load failed:', error);
      wwLib.showAlert('Failed to load dashboard data', 'error');
      return false;
    } finally {
      wwLib.hideLoading();
    }
  }
  
  static async updateUserProfile(profileData) {
    try {
      const response = await wwLib.api.patch({
        url: `${wwLib.envVars.XANO_API_URL}/users/me`,
        data: profileData,
        headers: { 'Authorization': 'Bearer ' + wwLib.auth.getAuthToken() }
      });
      
      if (response.data.success) {
        // Update local data
        wwLib.collections.currentUser.update(response.data.user);
        wwLib.showAlert('Profile updated successfully', 'success');
        return true;
      }
      
    } catch (error) {
      console.error('Profile update failed:', error);
      wwLib.showAlert('Failed to update profile', 'error');
      return false;
    }
  }
  
  static async searchAndFilter(searchParams) {
    try {
      const queryParams = new URLSearchParams();
      
      if (searchParams.query) queryParams.append('search', searchParams.query);
      if (searchParams.category) queryParams.append('category', searchParams.category);
      if (searchParams.dateFrom) queryParams.append('date_from', searchParams.dateFrom);
      if (searchParams.dateTo) queryParams.append('date_to', searchParams.dateTo);
      
      queryParams.append('page', searchParams.page || 1);
      queryParams.append('limit', searchParams.limit || 20);
      
      const response = await wwLib.api.get({
        url: `${wwLib.envVars.XANO_API_URL}/search?${queryParams}`,
        headers: { 'Authorization': 'Bearer ' + wwLib.auth.getAuthToken() }
      });
      
      // Update results collection
      wwLib.collections.searchResults.set(response.data.results);
      wwLib.variables.searchMetadata = response.data.metadata;
      
      return response.data;
      
    } catch (error) {
      console.error('Search failed:', error);
      wwLib.showAlert('Search failed', 'error');
      return null;
    }
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Master basic CRUD operations:
1. Create a simple users table
2. Implement add, get, edit, and delete functions
3. Add basic filtering and sorting
4. Test with sample data

### Intermediate Challenge
Build a content management system:
1. Create posts, categories, and tags tables
2. Implement complex queries with relationships
3. Add search and filtering capabilities
4. Create bulk operations for content management

### Advanced Challenge
Design a scalable e-commerce system:
1. Create orders, products, inventory, and customers tables
2. Implement transaction-based order processing
3. Add performance optimization with indexing
4. Create comprehensive analytics queries

## Best Practices

1. **Use appropriate indexes** - Index frequently queried fields
2. **Implement pagination** - Limit large result sets
3. **Validate inputs** - Always sanitize and validate data
4. **Use transactions** - For multi-table operations
5. **Monitor performance** - Track slow queries and optimize
6. **Plan for scale** - Design efficient data structures

## Next Steps

- Master [Query All Records](query_all_records.md) for advanced filtering
- Learn [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for complex operations
- Explore [External Database Query](external_database_query.md) for integrations
- Understand [Get Database Schema](get_database_schema.md) for dynamic operations

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Database operation discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Complete database guides
- 📖 [Advanced Patterns](../best-practices/database-patterns.md) - Scalable database design
- 🔧 [Support](https://xano.com/support) - Complex database assistance