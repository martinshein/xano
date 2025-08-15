---
title: "Get Record - Retrieve Single Database Records"
description: "Learn how to fetch individual records from your Xano database by ID with error handling, relationship loading, and performance optimization"
category: data-operations
tags:
  - Get Record
  - Database Retrieval
  - Single Record
  - By ID
  - Relationships
  - Error Handling
difficulty: beginner
reading_time: 10 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of databases
  - Knowledge of Xano tables and primary keys
  - Familiarity with function stacks
---

# Get Record - Retrieve Single Database Records

## 📋 **Quick Summary**

**What it does:** Get Record retrieves a single record from your Xano database table using its unique identifier (ID), providing fast and efficient access to specific data entries.

**Why it matters:** Get Record enables you to:
- **Fetch user profiles** and individual account data
- **Load specific orders** or transaction details
- **Retrieve product information** for display pages
- **Access individual content items** like posts or articles
- **Build detail pages** and record-specific interfaces

**Time to implement:** 2-5 minutes for basic retrieval, 10-15 minutes with relationships and error handling

---

## What You'll Learn

- How to retrieve records by ID efficiently
- Error handling for missing or invalid records
- Loading related data with relationships
- Caching strategies for frequently accessed records
- Integration patterns with no-code platforms

## Basic Get Record Usage

### Simple Record Retrieval

```javascript
// Basic get record by ID
const user = await getRecord({
  table: 'users',
  id: 123
});

// Check if record exists
if (user) {
  console.log('User found:', user.name);
  // Output: User found: John Doe
} else {
  console.log('User not found');
}
```

### Get Record with Error Handling

```javascript
// Robust get record function
function getUserById(userId) {
  try {
    // Validate input
    if (!userId || isNaN(userId)) {
      throw new Error('Valid user ID is required');
    }
    
    // Retrieve user record
    const user = getRecord({
      table: 'users',
      id: parseInt(userId)
    });
    
    if (!user) {
      return {
        success: false,
        error: 'User not found',
        code: 'USER_NOT_FOUND'
      };
    }
    
    // Remove sensitive data before returning
    const safeUser = {
      id: user.id,
      name: user.name,
      email: user.email,
      status: user.status,
      created_at: user.created_at,
      last_login: user.last_login
    };
    
    return {
      success: true,
      user: safeUser
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message,
      code: 'RETRIEVAL_ERROR'
    };
  }
}
```

## Advanced Get Record Patterns

### Loading Records with Relationships

```javascript
// Get user with related profile and subscription data
function getUserWithDetails(userId) {
  // Get main user record
  const user = getRecord({
    table: 'users',
    id: userId
  });
  
  if (!user) {
    throw new Error('User not found');
  }
  
  // Get related profile
  const profile = getRecord({
    table: 'user_profiles',
    filters: { user_id: userId }
  });
  
  // Get active subscription
  const subscription = queryAllRecords({
    table: 'subscriptions',
    filters: {
      user_id: userId,
      status: 'active'
    },
    limit: 1
  })[0] || null;
  
  // Get recent orders
  const recentOrders = queryAllRecords({
    table: 'orders',
    filters: {
      customer_id: userId,
      created_at: { $gte: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString() }
    },
    sort: [{ field: 'created_at', direction: 'desc' }],
    limit: 5
  });
  
  return {
    user: user,
    profile: profile,
    subscription: subscription,
    recent_orders: recentOrders,
    data_loaded_at: new Date().toISOString()
  };
}
```

### Conditional Record Access

```javascript
// Get record with permission checking
function getRecordSecure(table, recordId, currentUserId, userRole) {
  // Get the record
  const record = getRecord({
    table: table,
    id: recordId
  });
  
  if (!record) {
    return {
      success: false,
      error: 'Record not found',
      code: 'NOT_FOUND'
    };
  }
  
  // Check permissions based on table and user role
  const hasAccess = checkRecordAccess(record, currentUserId, userRole, table);
  
  if (!hasAccess) {
    return {
      success: false,
      error: 'Access denied',
      code: 'ACCESS_DENIED'
    };
  }
  
  // Filter sensitive fields based on role
  const filteredRecord = filterRecordByRole(record, userRole);
  
  return {
    success: true,
    record: filteredRecord,
    access_level: userRole
  };
}

function checkRecordAccess(record, userId, role, table) {
  // Admin can access everything
  if (role === 'admin') return true;
  
  // Table-specific access rules
  switch (table) {
    case 'users':
      // Users can access their own record
      return record.id === userId || role === 'moderator';
    
    case 'orders':
      // Users can access their own orders
      return record.customer_id === userId || role === 'staff';
    
    case 'posts':
      // Public posts or own posts
      return record.status === 'published' || record.author_id === userId;
    
    default:
      // Default: only owner or admin
      return record.user_id === userId;
  }
}

function filterRecordByRole(record, role) {
  const sensitiveFields = ['password', 'api_key', 'private_notes', 'internal_status'];
  
  if (role === 'admin') {
    return record; // Admin sees everything
  }
  
  // Remove sensitive fields for non-admin users
  const filtered = { ...record };
  sensitiveFields.forEach(field => {
    delete filtered[field];
  });
  
  return filtered;
}
```

### Batch Record Retrieval

```javascript
// Efficiently get multiple records by IDs
class RecordBatchLoader {
  static async getMultipleRecords(table, ids) {
    if (!ids || ids.length === 0) return [];
    
    // Use Query All Records with IN filter for efficiency
    const records = await queryAllRecords({
      table: table,
      filters: {
        id: { $in: ids }
      }
    });
    
    // Create a map for quick lookup
    const recordMap = new Map(records.map(r => [r.id, r]));
    
    // Return records in the same order as requested IDs
    return ids.map(id => recordMap.get(id) || null);
  }
  
  static async getUsersWithProfiles(userIds) {
    // Get users and profiles in parallel
    const [users, profiles] = await Promise.all([
      this.getMultipleRecords('users', userIds),
      queryAllRecords({
        table: 'user_profiles',
        filters: { user_id: { $in: userIds } }
      })
    ]);
    
    // Create profile lookup map
    const profileMap = new Map(profiles.map(p => [p.user_id, p]));
    
    // Combine users with their profiles
    return users.map(user => ({
      ...user,
      profile: user ? profileMap.get(user.id) || null : null
    }));
  }
  
  // Cache-aware batch loading
  static async getCachedRecords(table, ids, cacheMinutes = 5) {
    const cached = [];
    const uncachedIds = [];
    
    // Check cache for each ID
    ids.forEach(id => {
      const cacheKey = `${table}_${id}`;
      const cachedRecord = getFromCache(cacheKey);
      
      if (cachedRecord && !this.isCacheExpired(cachedRecord, cacheMinutes)) {
        cached.push(cachedRecord.data);
      } else {
        uncachedIds.push(id);
      }
    });
    
    // Load uncached records
    let freshRecords = [];
    if (uncachedIds.length > 0) {
      freshRecords = await this.getMultipleRecords(table, uncachedIds);
      
      // Cache fresh records
      freshRecords.forEach(record => {
        if (record) {
          const cacheKey = `${table}_${record.id}`;
          setCache(cacheKey, {
            data: record,
            cached_at: new Date().toISOString()
          });
        }
      });
    }
    
    // Combine cached and fresh records
    return [...cached, ...freshRecords].filter(Boolean);
  }
  
  static isCacheExpired(cachedItem, maxMinutes) {
    const cachedTime = new Date(cachedItem.cached_at);
    const expireTime = new Date(cachedTime.getTime() + maxMinutes * 60 * 1000);
    return new Date() > expireTime;
  }
}
```

## Performance Optimization

### Optimized Record Retrieval

```javascript
// Performance-optimized get record patterns
class OptimizedRecordRetrieval {
  static async getRecordOptimized(table, id, options = {}) {
    // Validate input
    if (!id || !table) {
      throw new Error('Table and ID are required');
    }
    
    // Check cache first if enabled
    if (options.useCache) {
      const cacheKey = `${table}_${id}`;
      const cached = getFromCache(cacheKey);
      
      if (cached && !this.isCacheExpired(cached, options.cacheMinutes || 5)) {
        return {
          ...cached.data,
          _source: 'cache',
          _cached_at: cached.cached_at
        };
      }
    }
    
    // Specify fields to retrieve if provided
    const record = await getRecord({
      table: table,
      id: id,
      fields: options.fields || undefined
    });
    
    if (!record) {
      return null;
    }
    
    // Cache the result if caching is enabled
    if (options.useCache && record) {
      const cacheKey = `${table}_${id}`;
      setCache(cacheKey, {
        data: record,
        cached_at: new Date().toISOString()
      });
    }
    
    return {
      ...record,
      _source: 'database',
      _retrieved_at: new Date().toISOString()
    };
  }
  
  // Lightweight record existence check
  static async recordExists(table, id) {
    const record = await getRecord({
      table: table,
      id: id,
      fields: ['id'] // Only retrieve ID field for efficiency
    });
    
    return !!record;
  }
  
  // Get record with minimal data transfer
  static async getRecordSummary(table, id, summaryFields) {
    return await getRecord({
      table: table,
      id: id,
      fields: summaryFields
    });
  }
}
```

### Smart Relationship Loading

```javascript
// Intelligent relationship loading based on need
class SmartRelationshipLoader {
  static async getRecordWithSmartLoading(table, id, options = {}) {
    const record = await getRecord({ table, id });
    
    if (!record) return null;
    
    const result = { ...record };
    
    // Load relationships based on options
    if (options.includeProfile && table === 'users') {
      result.profile = await this.loadProfile(id);
    }
    
    if (options.includeRecentActivity) {
      result.recent_activity = await this.loadRecentActivity(table, id);
    }
    
    if (options.includeRelatedItems) {
      result.related_items = await this.loadRelatedItems(table, id, options.relatedLimit || 5);
    }
    
    if (options.includeStats) {
      result.stats = await this.loadRecordStats(table, id);
    }
    
    return result;
  }
  
  static async loadProfile(userId) {
    return await getRecord({
      table: 'user_profiles',
      filters: { user_id: userId }
    });
  }
  
  static async loadRecentActivity(table, recordId) {
    const activityMap = {
      'users': () => this.getUserActivity(recordId),
      'orders': () => this.getOrderActivity(recordId),
      'posts': () => this.getPostActivity(recordId)
    };
    
    const activityLoader = activityMap[table];
    return activityLoader ? await activityLoader() : null;
  }
  
  static async getUserActivity(userId) {
    return await queryAllRecords({
      table: 'user_activities',
      filters: { user_id: userId },
      sort: [{ field: 'created_at', direction: 'desc' }],
      limit: 10
    });
  }
  
  static async loadRecordStats(table, recordId) {
    const statsMap = {
      'users': () => this.getUserStats(recordId),
      'posts': () => this.getPostStats(recordId),
      'products': () => this.getProductStats(recordId)
    };
    
    const statsLoader = statsMap[table];
    return statsLoader ? await statsLoader() : null;
  }
  
  static async getUserStats(userId) {
    const [orderCount, totalSpent, lastLogin] = await Promise.all([
      queryAllRecords({
        table: 'orders',
        filters: { customer_id: userId },
        return_type: 'count'
      }),
      
      queryAllRecords({
        table: 'orders',
        filters: { customer_id: userId },
        aggregate: { total: { $sum: 'total_amount' } }
      }),
      
      queryAllRecords({
        table: 'user_sessions',
        filters: { user_id: userId },
        sort: [{ field: 'created_at', direction: 'desc' }],
        limit: 1
      })
    ]);
    
    return {
      order_count: orderCount || 0,
      lifetime_value: totalSpent.total || 0,
      last_login: lastLogin[0]?.created_at || null
    };
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Integration**

```javascript
// n8n workflow for record retrieval
function getRecordWorkflow($input) {
  const params = $input.body || $input.query;
  
  try {
    // Validate inputs
    if (!params.table || !params.id) {
      return {
        success: false,
        error: 'Table name and record ID are required'
      };
    }
    
    // Get the record
    const record = getRecord({
      table: params.table,
      id: params.id
    });
    
    if (!record) {
      return {
        success: false,
        error: 'Record not found',
        code: 'NOT_FOUND'
      };
    }
    
    // Apply field filtering if requested
    let filteredRecord = record;
    if (params.fields && Array.isArray(params.fields)) {
      filteredRecord = {};
      params.fields.forEach(field => {
        if (record[field] !== undefined) {
          filteredRecord[field] = record[field];
        }
      });
    }
    
    // Load relationships if requested
    if (params.include_relationships) {
      try {
        const relationships = JSON.parse(params.include_relationships);
        filteredRecord = await loadRelationships(filteredRecord, relationships, params.table);
      } catch (error) {
        console.warn('Failed to load relationships:', error.message);
      }
    }
    
    return {
      success: true,
      record: filteredRecord,
      metadata: {
        table: params.table,
        id: params.id,
        retrieved_at: new Date().toISOString()
      }
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message,
      code: 'PROCESSING_ERROR'
    };
  }
}

// Helper function for loading relationships in n8n
async function loadRelationships(record, relationships, tableName) {
  const enriched = { ...record };
  
  for (const rel of relationships) {
    try {
      if (rel.type === 'hasOne') {
        enriched[rel.name] = await getRecord({
          table: rel.table,
          id: record[rel.foreign_key]
        });
      } else if (rel.type === 'hasMany') {
        enriched[rel.name] = await queryAllRecords({
          table: rel.table,
          filters: { [rel.foreign_key]: record.id },
          limit: rel.limit || 10
        });
      }
    } catch (error) {
      console.warn(`Failed to load relationship ${rel.name}:`, error.message);
      enriched[rel.name] = null;
    }
  }
  
  return enriched;
}
```

### 🌐 **WeWeb Integration**

```javascript
// WeWeb record loading utilities
class WeWebRecordLoader {
  static async loadRecord(table, id, options = {}) {
    try {
      // Show loading indicator
      if (options.showLoading !== false) {
        wwLib.showLoading();
      }
      
      // Make API request to get record
      const response = await wwLib.api.get({
        url: `${wwLib.envVars.XANO_API_URL}/${table}/${id}`,
        headers: { 
          'Authorization': 'Bearer ' + wwLib.auth.getAuthToken() 
        }
      });
      
      if (response.data && response.data.success) {
        const record = response.data.record;
        
        // Update WeWeb variable with the record
        const variableName = options.variableName || `current_${table}`;
        wwLib.variables[variableName] = record;
        
        // Update collection if specified
        if (options.updateCollection) {
          const collection = wwLib.collections[options.updateCollection];
          if (collection) {
            collection.updateItem(record.id, record);
          }
        }
        
        // Trigger refresh of page elements
        if (options.refreshElements) {
          wwLib.refreshElement(options.refreshElements);
        }
        
        return record;
      } else {
        throw new Error('Record not found');
      }
      
    } catch (error) {
      console.error('Failed to load record:', error);
      
      // Show user-friendly error
      const errorMessage = error.response?.status === 404 
        ? 'Record not found' 
        : 'Failed to load data';
      
      wwLib.showAlert(errorMessage, 'error');
      
      // Set error state
      wwLib.variables.lastError = {
        message: errorMessage,
        timestamp: new Date().toISOString()
      };
      
      return null;
    } finally {
      if (options.showLoading !== false) {
        wwLib.hideLoading();
      }
    }
  }
  
  // Load record with real-time updates
  static async loadRecordWithUpdates(table, id, updateInterval = 30000) {
    // Initial load
    await this.loadRecord(table, id);
    
    // Set up periodic updates
    const updateTimer = setInterval(async () => {
      try {
        await this.loadRecord(table, id, { showLoading: false });
      } catch (error) {
        console.warn('Background update failed:', error);
      }
    }, updateInterval);
    
    // Store timer ID for cleanup
    wwLib.variables[`${table}_${id}_updateTimer`] = updateTimer;
    
    return updateTimer;
  }
  
  // Stop real-time updates
  static stopRecordUpdates(table, id) {
    const timerKey = `${table}_${id}_updateTimer`;
    const timer = wwLib.variables[timerKey];
    
    if (timer) {
      clearInterval(timer);
      delete wwLib.variables[timerKey];
    }
  }
  
  // Load record for form editing
  static async loadRecordForEdit(table, id, formId) {
    const record = await this.loadRecord(table, id);
    
    if (record && formId) {
      // Populate form fields with record data
      wwLib.form.populateForm(formId, record);
      
      // Set form to edit mode
      wwLib.variables.formMode = 'edit';
      wwLib.variables.editingRecordId = id;
    }
    
    return record;
  }
}
```

### 🔧 **Make.com Integration**

```javascript
// Make.com scenario for record retrieval and processing
function processMakeRecordRetrieval(inputData) {
  const config = inputData.configuration;
  
  try {
    // Get the record
    const record = getRecord({
      table: config.table_name,
      id: config.record_id
    });
    
    if (!record) {
      return {
        success: false,
        error: 'Record not found',
        record_id: config.record_id,
        table: config.table_name
      };
    }
    
    // Transform data based on Make.com mapping
    const transformedRecord = transformRecordForMake(record, config.field_mapping);
    
    // Add Make.com specific metadata
    const result = {
      success: true,
      record: transformedRecord,
      metadata: {
        source_table: config.table_name,
        record_id: config.record_id,
        retrieved_at: new Date().toISOString(),
        scenario_id: config.scenario_id
      }
    };
    
    // Add conditional processing based on record data
    if (config.conditional_processing) {
      result.processing_flags = evaluateConditions(record, config.conditions);
    }
    
    return result;
    
  } catch (error) {
    return {
      success: false,
      error: error.message,
      record_id: config.record_id,
      table: config.table_name,
      scenario_id: config.scenario_id
    };
  }
}

function transformRecordForMake(record, fieldMapping) {
  if (!fieldMapping) return record;
  
  const transformed = {};
  
  Object.entries(fieldMapping).forEach(([makeField, xanoField]) => {
    if (record[xanoField] !== undefined) {
      transformed[makeField] = record[xanoField];
    }
  });
  
  return transformed;
}

function evaluateConditions(record, conditions) {
  const flags = {};
  
  conditions.forEach(condition => {
    const fieldValue = record[condition.field];
    let result = false;
    
    switch (condition.operator) {
      case 'equals':
        result = fieldValue === condition.value;
        break;
      case 'greater_than':
        result = fieldValue > condition.value;
        break;
      case 'contains':
        result = String(fieldValue).includes(condition.value);
        break;
      case 'is_null':
        result = fieldValue === null || fieldValue === undefined;
        break;
    }
    
    flags[condition.flag_name] = result;
  });
  
  return flags;
}
```

## 💡 **Try This**

### Beginner Challenge
Build a simple record viewer:
1. Create a function to get a user by ID
2. Add error handling for non-existent users
3. Display user information safely (no sensitive data)
4. Test with valid and invalid IDs

### Intermediate Challenge
Create a detailed record loader:
1. Get a record with related profile data
2. Add caching for frequently accessed records
3. Implement permission-based field filtering
4. Build a record existence checker

### Advanced Challenge
Design a high-performance record system:
1. Implement batch record loading with relationships
2. Add smart caching with automatic invalidation
3. Create role-based access control
4. Build real-time record synchronization

## Common Mistakes to Avoid

1. **No existence checking** - Always verify records exist before processing
2. **Missing error handling** - Handle database errors and invalid IDs
3. **Exposing sensitive data** - Filter out private fields before returning
4. **Inefficient relationship loading** - Use batch queries for multiple relationships
5. **No input validation** - Validate and sanitize ID parameters
6. **Ignoring performance** - Consider caching for frequently accessed records

## Best Practices

1. **Validate inputs** - Check ID format and table name before querying
2. **Handle missing records** - Provide clear error messages for not found cases
3. **Filter sensitive data** - Remove private fields based on user permissions
4. **Use caching wisely** - Cache frequently accessed records with appropriate TTL
5. **Load relationships efficiently** - Batch related data queries when possible
6. **Monitor performance** - Track retrieval times and optimize slow queries

## Next Steps

- Learn [Query All Records](query_all_records.md) for retrieving multiple records
- Master [Edit Record](edit_record.md) for updating record data
- Explore [Add Record](add_record.md) for creating new records
- Understand [Database Relationships](../advanced/relationships.md) for complex data loading

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Record retrieval discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Get Record implementation guides
- 📖 [Performance Tips](../best-practices/record-optimization.md) - Optimization strategies
- 🔧 [Support](https://xano.com/support) - Database operation assistance