---
title: "Query All Records - Advanced Data Retrieval"
description: "Master retrieving multiple records from your Xano database with advanced filtering, sorting, pagination, and performance optimization techniques"
category: data-operations
tags:
  - Query All Records
  - Database Retrieval
  - Filtering
  - Sorting
  - Pagination
  - Performance
difficulty: intermediate
reading_time: 15 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of databases
  - Knowledge of Xano tables and fields
  - Familiarity with function stacks
  - Understanding of basic SQL concepts
---

# Query All Records - Advanced Data Retrieval

## 📋 **Quick Summary**

**What it does:** Query All Records retrieves multiple records from your Xano database tables with powerful filtering, sorting, and pagination capabilities for building dynamic data-driven applications.

**Why it matters:** Query All Records enables you to:
- **Build dynamic lists** and search functionality
- **Implement advanced filtering** with multiple conditions
- **Create paginated data displays** for performance
- **Sort and organize data** for user interfaces
- **Optimize query performance** with proper indexing

**Time to implement:** 10-15 minutes for basic queries, 30+ minutes for complex filtering and optimization

---

## What You'll Learn

- Advanced filtering techniques with multiple conditions
- Sorting and pagination strategies
- Performance optimization for large datasets
- Integration with search and filter interfaces
- Best practices for efficient data retrieval

## Basic Query Operations

### Simple Record Retrieval

```javascript
// Basic query all records example
const allUsers = await queryAllRecords({
  table: 'users',
  limit: 50
});

// Returns array of user records
console.log(allUsers);
// Output: [{ id: 1, name: 'John', email: 'john@example.com' }, ...]
```

### Query with Basic Filtering

```javascript
// Query active users only
const activeUsers = await queryAllRecords({
  table: 'users',
  filters: {
    status: 'active'
  },
  sort: [{ field: 'created_at', direction: 'desc' }],
  limit: 25
});

// Query users created in the last 30 days
const recentUsers = await queryAllRecords({
  table: 'users',
  filters: {
    created_at: { $gte: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString() }
  }
});
```

## Advanced Filtering Patterns

### Multiple Condition Filtering

```javascript
// Complex filtering with multiple conditions
function searchUsers(searchParams) {
  const filters = {};
  
  // Build dynamic filters based on search parameters
  if (searchParams.name) {
    filters.name = { $ilike: `%${searchParams.name}%` };
  }
  
  if (searchParams.email) {
    filters.email = { $ilike: `%${searchParams.email}%` };
  }
  
  if (searchParams.status) {
    filters.status = searchParams.status;
  }
  
  if (searchParams.dateFrom || searchParams.dateTo) {
    filters.created_at = {};
    if (searchParams.dateFrom) {
      filters.created_at.$gte = searchParams.dateFrom;
    }
    if (searchParams.dateTo) {
      filters.created_at.$lte = searchParams.dateTo;
    }
  }
  
  // Execute query with dynamic filters
  const results = queryAllRecords({
    table: 'users',
    filters: filters,
    sort: [
      { field: 'last_login', direction: 'desc' },
      { field: 'created_at', direction: 'desc' }
    ],
    limit: searchParams.limit || 50,
    offset: searchParams.offset || 0
  });
  
  return {
    users: results,
    filters_applied: Object.keys(filters),
    total_conditions: Object.keys(filters).length
  };
}
```

### Advanced Operator Usage

```javascript
// Using various query operators for complex filtering
class UserQueryBuilder {
  static async getFilteredUsers(criteria) {
    const filters = {};
    
    // Text search operators
    if (criteria.nameContains) {
      filters.name = { $includes: criteria.nameContains };
    }
    
    if (criteria.emailDomain) {
      filters.email = { $like: `%@${criteria.emailDomain}` };
    }
    
    // Numeric operators
    if (criteria.minAge) {
      filters.age = { $gte: criteria.minAge };
    }
    
    if (criteria.ageRange) {
      filters.age = { 
        $gte: criteria.ageRange.min, 
        $lte: criteria.ageRange.max 
      };
    }
    
    // Array operators
    if (criteria.statusList) {
      filters.status = { $in: criteria.statusList };
    }
    
    if (criteria.excludeRoles) {
      filters.role = { $notin: criteria.excludeRoles };
    }
    
    // Date operators
    if (criteria.lastActiveAfter) {
      filters.last_active = { $gt: criteria.lastActiveAfter };
    }
    
    // Boolean operators
    if (criteria.isVerified !== undefined) {
      filters.email_verified = criteria.isVerified;
    }
    
    return await queryAllRecords({
      table: 'users',
      filters: filters,
      include: ['profile', 'subscription'],
      sort: [{ field: 'created_at', direction: 'desc' }]
    });
  }
  
  // OR condition example
  static async getUsersByMultipleEmails(emails) {
    return await queryAllRecords({
      table: 'users',
      filters: {
        $or: emails.map(email => ({ email: email }))
      }
    });
  }
  
  // Complex nested conditions
  static async getVIPUsers() {
    return await queryAllRecords({
      table: 'users',
      filters: {
        $and: [
          {
            $or: [
              { subscription_type: 'premium' },
              { subscription_type: 'enterprise' }
            ]
          },
          {
            total_spent: { $gte: 1000 }
          },
          {
            status: 'active'
          }
        ]
      },
      sort: [{ field: 'total_spent', direction: 'desc' }]
    });
  }
}
```

## Sorting and Pagination

### Advanced Sorting Strategies

```javascript
// Multi-field sorting with priority
function getUsersSorted(sortOptions = {}) {
  const defaultSort = [
    { field: 'status', direction: 'asc' }, // Active users first
    { field: 'subscription_tier', direction: 'desc' }, // Premium users first
    { field: 'last_login', direction: 'desc' }, // Recent activity first
    { field: 'created_at', direction: 'desc' } // Newest users first
  ];
  
  const sort = sortOptions.customSort || defaultSort;
  
  return queryAllRecords({
    table: 'users',
    filters: { status: { $in: ['active', 'pending'] } },
    sort: sort,
    limit: sortOptions.limit || 50
  });
}

// Dynamic sorting based on user preferences
function getCustomSortedUsers(userPreferences) {
  const sortMap = {
    'name_asc': [{ field: 'name', direction: 'asc' }],
    'name_desc': [{ field: 'name', direction: 'desc' }],
    'date_newest': [{ field: 'created_at', direction: 'desc' }],
    'date_oldest': [{ field: 'created_at', direction: 'asc' }],
    'activity_recent': [{ field: 'last_login', direction: 'desc' }],
    'spending_high': [{ field: 'total_spent', direction: 'desc' }]
  };
  
  const sort = sortMap[userPreferences.sort_preference] || sortMap['date_newest'];
  
  return queryAllRecords({
    table: 'users',
    sort: sort,
    limit: userPreferences.results_per_page || 25
  });
}
```

### Efficient Pagination Implementation

```javascript
// Comprehensive pagination with metadata
class PaginationManager {
  static async getPaginatedResults(table, options = {}) {
    const page = Math.max(1, options.page || 1);
    const limit = Math.min(100, Math.max(1, options.limit || 25));
    const offset = (page - 1) * limit;
    
    // Get the actual records
    const records = await queryAllRecords({
      table: table,
      filters: options.filters || {},
      sort: options.sort || [{ field: 'id', direction: 'desc' }],
      limit: limit,
      offset: offset,
      include: options.include || []
    });
    
    // Get total count for pagination metadata
    const totalCount = await this.getTotalCount(table, options.filters);
    
    const totalPages = Math.ceil(totalCount / limit);
    const hasNextPage = page < totalPages;
    const hasPreviousPage = page > 1;
    
    return {
      data: records,
      pagination: {
        current_page: page,
        per_page: limit,
        total_records: totalCount,
        total_pages: totalPages,
        has_next_page: hasNextPage,
        has_previous_page: hasPreviousPage,
        next_page: hasNextPage ? page + 1 : null,
        previous_page: hasPreviousPage ? page - 1 : null,
        offset: offset
      }
    };
  }
  
  static async getTotalCount(table, filters = {}) {
    const result = await queryAllRecords({
      table: table,
      filters: filters,
      return_type: 'count'
    });
    
    return result || 0;
  }
  
  // Cursor-based pagination for large datasets
  static async getCursorPaginatedResults(table, options = {}) {
    const limit = Math.min(100, options.limit || 25);
    const cursor = options.cursor; // ID of last item from previous page
    
    const filters = { ...options.filters };
    
    // Add cursor condition if provided
    if (cursor) {
      filters.id = { $gt: cursor };
    }
    
    const records = await queryAllRecords({
      table: table,
      filters: filters,
      sort: [{ field: 'id', direction: 'asc' }],
      limit: limit + 1 // Get one extra to check if there's a next page
    });
    
    const hasNextPage = records.length > limit;
    const data = hasNextPage ? records.slice(0, limit) : records;
    const nextCursor = data.length > 0 ? data[data.length - 1].id : null;
    
    return {
      data: data,
      pagination: {
        has_next_page: hasNextPage,
        next_cursor: hasNextPage ? nextCursor : null,
        per_page: limit
      }
    };
  }
}
```

## Performance Optimization

### Query Optimization Strategies

```javascript
// Performance-optimized queries
class QueryOptimizer {
  static async getOptimizedUserList(criteria) {
    // Only select necessary fields to reduce data transfer
    const fields = [
      'id', 'name', 'email', 'status', 'created_at', 'last_login'
    ];
    
    // Use indexed fields for filtering when possible
    const indexedFilters = {};
    if (criteria.status) indexedFilters.status = criteria.status;
    if (criteria.email) indexedFilters.email = criteria.email;
    if (criteria.userId) indexedFilters.id = criteria.userId;
    
    return await queryAllRecords({
      table: 'users',
      fields: fields,
      filters: indexedFilters,
      sort: [{ field: 'id', direction: 'desc' }], // Use primary key for sorting
      limit: Math.min(50, criteria.limit || 25) // Limit result size
    });
  }
  
  // Batch loading with efficient queries
  static async getBatchUserData(userIds) {
    if (!userIds || userIds.length === 0) return [];
    
    // Use IN operator for batch loading
    const users = await queryAllRecords({
      table: 'users',
      filters: {
        id: { $in: userIds }
      },
      fields: ['id', 'name', 'email', 'status']
    });
    
    return users;
  }
  
  // Efficient search with pre-built indexes
  static async searchUsersOptimized(searchTerm) {
    if (!searchTerm || searchTerm.length < 2) {
      return { users: [], message: 'Search term too short' };
    }
    
    // Use full-text search if available, otherwise use LIKE
    const searchConditions = {
      $or: [
        { name: { $ilike: `%${searchTerm}%` } },
        { email: { $ilike: `%${searchTerm}%` } }
      ]
    };
    
    const users = await queryAllRecords({
      table: 'users',
      filters: searchConditions,
      fields: ['id', 'name', 'email', 'status'],
      sort: [{ field: 'last_login', direction: 'desc' }],
      limit: 20
    });
    
    return {
      users: users,
      search_term: searchTerm,
      result_count: users.length
    };
  }
}
```

### Relationship Loading Strategies

```javascript
// Efficient relationship loading
async function loadUsersWithRelationships(options = {}) {
  // Load users first
  const users = await queryAllRecords({
    table: 'users',
    filters: options.filters || {},
    limit: options.limit || 50,
    sort: [{ field: 'created_at', direction: 'desc' }]
  });
  
  if (users.length === 0) return [];
  
  const userIds = users.map(user => user.id);
  
  // Load related data in parallel for better performance
  const [profiles, subscriptions, recentOrders] = await Promise.all([
    // Load user profiles
    queryAllRecords({
      table: 'user_profiles',
      filters: { user_id: { $in: userIds } }
    }),
    
    // Load subscriptions
    queryAllRecords({
      table: 'subscriptions',
      filters: { 
        user_id: { $in: userIds },
        status: 'active'
      }
    }),
    
    // Load recent orders
    queryAllRecords({
      table: 'orders',
      filters: {
        customer_id: { $in: userIds },
        created_at: { $gte: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString() }
      },
      sort: [{ field: 'created_at', direction: 'desc' }],
      limit: 5
    })
  ]);
  
  // Create lookup maps for efficient joining
  const profileMap = new Map(profiles.map(p => [p.user_id, p]));
  const subscriptionMap = new Map(subscriptions.map(s => [s.user_id, s]));
  const orderMap = new Map();
  
  recentOrders.forEach(order => {
    if (!orderMap.has(order.customer_id)) {
      orderMap.set(order.customer_id, []);
    }
    orderMap.get(order.customer_id).push(order);
  });
  
  // Combine data efficiently
  return users.map(user => ({
    ...user,
    profile: profileMap.get(user.id) || null,
    subscription: subscriptionMap.get(user.id) || null,
    recent_orders: orderMap.get(user.id) || []
  }));
}
```

## No-Code Platform Integration

### 🔗 **n8n Integration**

```javascript
// n8n workflow for dynamic data retrieval
function processDataQuery($input) {
  const params = $input.body || $input.query;
  
  // Build dynamic query from n8n parameters
  const queryConfig = {
    table: params.table || 'users',
    filters: {},
    sort: [],
    limit: Math.min(100, params.limit || 25),
    offset: params.offset || 0
  };
  
  // Process filters from n8n
  if (params.filters) {
    try {
      queryConfig.filters = typeof params.filters === 'string' 
        ? JSON.parse(params.filters) 
        : params.filters;
    } catch (error) {
      return { error: 'Invalid filters format' };
    }
  }
  
  // Process sorting from n8n
  if (params.sort_field && params.sort_direction) {
    queryConfig.sort = [{
      field: params.sort_field,
      direction: params.sort_direction
    }];
  }
  
  // Execute query
  const results = queryAllRecords(queryConfig);
  
  return {
    success: true,
    data: results,
    query_info: {
      table: queryConfig.table,
      filters_applied: Object.keys(queryConfig.filters).length,
      sort_applied: queryConfig.sort.length > 0,
      result_count: results.length
    }
  };
}

// n8n search functionality
function processSearchRequest($input) {
  const searchParams = $input.body;
  
  if (!searchParams.query || searchParams.query.length < 2) {
    return {
      success: false,
      error: 'Search query must be at least 2 characters'
    };
  }
  
  const searchResults = queryAllRecords({
    table: searchParams.table || 'content',
    filters: {
      $or: [
        { title: { $ilike: `%${searchParams.query}%` } },
        { description: { $ilike: `%${searchParams.query}%` } },
        { content: { $ilike: `%${searchParams.query}%` } }
      ]
    },
    sort: [{ field: 'updated_at', direction: 'desc' }],
    limit: searchParams.limit || 20
  });
  
  return {
    success: true,
    results: searchResults,
    search_query: searchParams.query,
    result_count: searchResults.length
  };
}
```

### 🌐 **WeWeb Integration**

```javascript
// WeWeb data loading utilities
class WeWebQueryManager {
  static async loadPageData(pageConfig) {
    try {
      // Show loading state
      wwLib.showLoading();
      
      // Prepare query parameters
      const queryParams = {
        page: wwLib.variables.currentPage || 1,
        limit: pageConfig.itemsPerPage || 20,
        filters: this.buildFiltersFromForm(),
        sort: this.buildSortFromState()
      };
      
      // Execute query
      const response = await wwLib.api.post({
        url: `${wwLib.envVars.XANO_API_URL}/query/${pageConfig.table}`,
        data: queryParams,
        headers: { 'Authorization': 'Bearer ' + wwLib.auth.getAuthToken() }
      });
      
      if (response.data.success) {
        // Update WeWeb collections
        wwLib.collections[pageConfig.collectionName].set(response.data.data);
        
        // Update pagination info
        wwLib.variables.pagination = response.data.pagination;
        wwLib.variables.lastDataLoad = new Date().toISOString();
        
        return true;
      }
      
      return false;
      
    } catch (error) {
      console.error('Data loading failed:', error);
      wwLib.showAlert('Failed to load data', 'error');
      return false;
    } finally {
      wwLib.hideLoading();
    }
  }
  
  static buildFiltersFromForm() {
    const filters = {};
    
    // Get filter values from WeWeb form elements
    const searchTerm = wwLib.variables.searchInput;
    if (searchTerm) {
      filters.name = { $ilike: `%${searchTerm}%` };
    }
    
    const statusFilter = wwLib.variables.statusFilter;
    if (statusFilter && statusFilter !== 'all') {
      filters.status = statusFilter;
    }
    
    const dateFrom = wwLib.variables.dateFromFilter;
    const dateTo = wwLib.variables.dateToFilter;
    if (dateFrom || dateTo) {
      filters.created_at = {};
      if (dateFrom) filters.created_at.$gte = dateFrom;
      if (dateTo) filters.created_at.$lte = dateTo;
    }
    
    return filters;
  }
  
  static buildSortFromState() {
    const sortField = wwLib.variables.sortField || 'created_at';
    const sortDirection = wwLib.variables.sortDirection || 'desc';
    
    return [{ field: sortField, direction: sortDirection }];
  }
  
  // Infinite scroll implementation
  static async loadMoreItems() {
    if (wwLib.variables.isLoadingMore) return;
    
    wwLib.variables.isLoadingMore = true;
    const currentPage = wwLib.variables.currentPage || 1;
    
    try {
      const response = await wwLib.api.post({
        url: `${wwLib.envVars.XANO_API_URL}/query/items`,
        data: {
          page: currentPage + 1,
          limit: 20,
          filters: this.buildFiltersFromForm()
        },
        headers: { 'Authorization': 'Bearer ' + wwLib.auth.getAuthToken() }
      });
      
      if (response.data.success && response.data.data.length > 0) {
        // Append new items to existing collection
        const currentItems = wwLib.collections.items.get() || [];
        wwLib.collections.items.set([...currentItems, ...response.data.data]);
        
        wwLib.variables.currentPage = currentPage + 1;
        wwLib.variables.hasMoreItems = response.data.pagination.has_next_page;
      } else {
        wwLib.variables.hasMoreItems = false;
      }
      
    } catch (error) {
      console.error('Load more failed:', error);
      wwLib.showAlert('Failed to load more items', 'error');
    } finally {
      wwLib.variables.isLoadingMore = false;
    }
  }
}
```

### 🔧 **Make.com Integration**

```javascript
// Make.com scenario for automated data retrieval
function processMakeQuery(inputData) {
  const scenario = inputData.scenario_config;
  
  try {
    // Build query based on Make.com scenario configuration
    const queryConfig = {
      table: scenario.table_name,
      filters: {},
      limit: scenario.max_results || 100
    };
    
    // Process dynamic filters from Make.com
    if (scenario.filter_conditions) {
      scenario.filter_conditions.forEach(condition => {
        if (condition.field && condition.operator && condition.value !== undefined) {
          switch (condition.operator) {
            case 'equals':
              queryConfig.filters[condition.field] = condition.value;
              break;
            case 'contains':
              queryConfig.filters[condition.field] = { $ilike: `%${condition.value}%` };
              break;
            case 'greater_than':
              queryConfig.filters[condition.field] = { $gt: condition.value };
              break;
            case 'less_than':
              queryConfig.filters[condition.field] = { $lt: condition.value };
              break;
            case 'in_list':
              queryConfig.filters[condition.field] = { $in: condition.value.split(',') };
              break;
          }
        }
      });
    }
    
    // Add date range filters if specified
    if (scenario.date_range) {
      const dateField = scenario.date_field || 'created_at';
      queryConfig.filters[dateField] = {};
      
      if (scenario.date_range.from) {
        queryConfig.filters[dateField].$gte = scenario.date_range.from;
      }
      
      if (scenario.date_range.to) {
        queryConfig.filters[dateField].$lte = scenario.date_range.to;
      }
    }
    
    // Execute query
    const results = queryAllRecords(queryConfig);
    
    // Format results for Make.com
    return {
      success: true,
      data: results.map(record => ({
        ...record,
        _scenario_id: scenario.id,
        _processed_at: new Date().toISOString()
      })),
      metadata: {
        total_records: results.length,
        query_executed_at: new Date().toISOString(),
        filters_applied: Object.keys(queryConfig.filters)
      }
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message,
      scenario_id: scenario.id
    };
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Build a basic search interface:
1. Create a simple query with filtering by status
2. Add basic sorting by creation date
3. Implement pagination with 10 results per page
4. Test with different filter combinations

### Intermediate Challenge
Create an advanced search system:
1. Build multi-field search with text matching
2. Add date range filtering
3. Implement dynamic sorting options
4. Create efficient pagination with metadata

### Advanced Challenge
Design a high-performance data dashboard:
1. Build complex queries with multiple relationships
2. Implement cursor-based pagination for large datasets
3. Add real-time search with debouncing
4. Optimize queries for sub-second response times

## Common Mistakes to Avoid

1. **Querying without limits** - Always use pagination for large datasets
2. **Inefficient filtering** - Use indexed fields for better performance
3. **Loading unnecessary data** - Select only required fields
4. **No error handling** - Handle empty results and query failures
5. **Ignoring performance** - Monitor and optimize slow queries
6. **Poor sorting strategy** - Use appropriate fields for sorting

## Best Practices

1. **Use indexes wisely** - Index frequently queried and sorted fields
2. **Implement pagination** - Always limit result sets for better performance
3. **Cache when appropriate** - Cache frequently accessed data
4. **Validate inputs** - Sanitize and validate all query parameters
5. **Monitor performance** - Track query execution times
6. **Plan for scale** - Design queries that work with growing datasets

## Next Steps

- Learn [Get Record](get_record.md) for single record retrieval
- Master [Add Record](add_record.md) for creating new data
- Explore [Edit Record](edit_record.md) for updating existing records
- Understand [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for complex operations

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Query optimization discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Advanced querying techniques
- 📖 [Performance Guide](../best-practices/query-optimization.md) - Query optimization strategies
- 🔧 [Support](https://xano.com/support) - Complex query assistance