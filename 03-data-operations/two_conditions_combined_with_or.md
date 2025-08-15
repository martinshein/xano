---
title: "OR Conditions - Complex Query Logic"
description: "Master complex database filtering with OR conditions in Xano. Learn to combine multiple criteria, build flexible search functionality, and optimize query performance"
category: data-operations
tags:
  - OR Conditions
  - Query Logic
  - Database Filtering
  - Complex Queries
  - Search Functionality
  - Query Optimization
difficulty: intermediate
reading_time: 10 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of database queries
  - Familiarity with Query All Records
  - Knowledge of filtering concepts
---

# OR Conditions - Complex Query Logic

## 📋 **Quick Summary**

**What it does:** OR conditions allow you to combine multiple filter criteria where records match if ANY of the conditions are true, enabling flexible and powerful search functionality.

**Why it matters:** OR logic enables you to:
- **Build flexible search features** with multiple criteria
- **Create inclusive filtering** that captures broader result sets
- **Handle user preferences** with optional filters
- **Implement complex business rules** with conditional logic
- **Optimize user experience** with smart search capabilities

**Time to implement:** 10-15 minutes for basic OR conditions, 30+ minutes for complex multi-field logic

---

## What You'll Learn

- How to structure OR conditions in database queries
- Complex filtering patterns with multiple criteria
- Performance optimization for OR queries
- Integration with search interfaces
- Best practices for maintainable query logic

## Basic OR Condition Syntax

### Simple Two-Condition OR

```javascript
// Find users who are either premium subscribers OR have made recent purchases
const activeUsers = await queryAllRecords({
  table: 'users',
  filters: {
    $or: [
      { subscription_type: 'premium' },
      { last_purchase_date: { $gte: '2024-01-01' } }
    ]
  }
});

// SQL equivalent: WHERE subscription_type = 'premium' OR last_purchase_date >= '2024-01-01'
```

### Multiple OR Conditions

```javascript
// Find products that match any of multiple categories or price ranges
const searchResults = await queryAllRecords({
  table: 'products',
  filters: {
    $or: [
      { category: 'electronics' },
      { category: 'computers' },
      { price: { $lte: 50 } },      // Under $50
      { sale_price: { $gte: 0 } }    // On sale
    ]
  },
  sort: [{ field: 'name', direction: 'asc' }]
});
```

## Advanced OR Patterns

### Combining AND and OR Logic

```javascript
// Complex search: Find active users who are either premium OR have recent activity
const complexSearch = await queryAllRecords({
  table: 'users',
  filters: {
    status: 'active',  // AND condition (all must have active status)
    $or: [
      { subscription_type: 'premium' },
      { 
        $and: [
          { last_login: { $gte: '2024-01-01' } },
          { total_orders: { $gte: 5 } }
        ]
      }
    ]
  }
});

// SQL equivalent: 
// WHERE status = 'active' 
// AND (subscription_type = 'premium' 
//      OR (last_login >= '2024-01-01' AND total_orders >= 5))
```

### Dynamic Search Builder

```javascript
// Flexible search function that builds OR conditions dynamically
class SearchBuilder {
  static buildFlexibleSearch(searchParams) {
    const filters = {};
    const orConditions = [];
    
    // Add text search across multiple fields
    if (searchParams.query) {
      orConditions.push(
        { name: { $ilike: `%${searchParams.query}%` } },
        { description: { $ilike: `%${searchParams.query}%` } },
        { tags: { $ilike: `%${searchParams.query}%` } }
      );
    }
    
    // Add category options
    if (searchParams.categories && searchParams.categories.length > 0) {
      const categoryConditions = searchParams.categories.map(cat => ({ category: cat }));
      orConditions.push(...categoryConditions);
    }
    
    // Add price ranges
    if (searchParams.priceRanges) {
      searchParams.priceRanges.forEach(range => {
        orConditions.push({
          price: { $gte: range.min, $lte: range.max }
        });
      });
    }
    
    // Add date ranges
    if (searchParams.dateOptions) {
      searchParams.dateOptions.forEach(option => {
        orConditions.push({
          created_at: { $gte: option.start, $lte: option.end }
        });
      });
    }
    
    // Only add OR conditions if we have any
    if (orConditions.length > 0) {
      filters.$or = orConditions;
    }
    
    // Add required filters (AND conditions)
    if (searchParams.requiredStatus) {
      filters.status = searchParams.requiredStatus;
    }
    
    return {
      table: searchParams.table || 'products',
      filters: filters,
      sort: searchParams.sort || [{ field: 'created_at', direction: 'desc' }],
      limit: searchParams.limit || 20,
      offset: searchParams.offset || 0
    };
  }
}

// Usage example
const searchResults = await queryAllRecords(
  SearchBuilder.buildFlexibleSearch({
    query: 'laptop',
    categories: ['electronics', 'computers'],
    priceRanges: [
      { min: 0, max: 500 },
      { min: 1000, max: 2000 }
    ],
    requiredStatus: 'active'
  })
);
```

## No-Code Platform Integration

### 🔗 **n8n OR Condition Workflows**

```javascript
// n8n function for building dynamic OR conditions
function buildDynamicQuery($input) {
  const searchParams = $input.body;
  const orConditions = [];
  
  // Handle multiple search criteria
  if (searchParams.name) {
    orConditions.push({ name: { $ilike: `%${searchParams.name}%` } });
  }
  
  if (searchParams.email) {
    orConditions.push({ email: { $ilike: `%${searchParams.email}%` } });
  }
  
  if (searchParams.phone) {
    orConditions.push({ phone: { $ilike: `%${searchParams.phone}%` } });
  }
  
  if (searchParams.tags && searchParams.tags.length > 0) {
    searchParams.tags.forEach(tag => {
      orConditions.push({ tags: { $ilike: `%${tag}%` } });
    });
  }
  
  // Build final query
  const query = {
    table: 'contacts',
    filters: {
      status: 'active'
    }
  };
  
  if (orConditions.length > 0) {
    query.filters.$or = orConditions;
  }
  
  return {
    query: query,
    conditions_count: orConditions.length,
    search_type: 'flexible_or_search'
  };
}
```

### 🌐 **WeWeb Search Interface**

```javascript
// WeWeb search component with OR conditions
class WeWebSearchHandler {
  static async performFlexibleSearch() {
    const searchForm = wwLib.form.getFormData('searchForm');
    
    try {
      // Show loading
      wwLib.showLoading();
      
      // Build OR conditions from form
      const orConditions = [];
      
      if (searchForm.productName) {
        orConditions.push({ name: { $ilike: `%${searchForm.productName}%` } });
      }
      
      if (searchForm.category && searchForm.category !== 'all') {
        orConditions.push({ category: searchForm.category });
      }
      
      if (searchForm.priceRange) {
        const [min, max] = searchForm.priceRange.split('-').map(Number);
        orConditions.push({ price: { $gte: min, $lte: max } });
      }
      
      if (searchForm.onSale) {
        orConditions.push({ sale_price: { $gt: 0 } });
      }
      
      // Build query
      const queryData = {
        table: 'products',
        filters: {
          status: 'active'
        },
        limit: 20,
        offset: (wwLib.variables.currentPage - 1) * 20
      };
      
      if (orConditions.length > 0) {
        queryData.filters.$or = orConditions;
      }
      
      // Execute search
      const response = await wwLib.api.post({
        url: `${wwLib.envVars.XANO_API_URL}/search/products`,
        data: queryData,
        headers: {
          'Authorization': 'Bearer ' + wwLib.auth.getAuthToken()
        }
      });
      
      // Update results
      wwLib.collections.searchResults.set(response.data);
      wwLib.variables.totalResults = response.data.length;
      wwLib.variables.hasMoreResults = response.data.length === 20;
      
      // Update UI
      if (response.data.length === 0) {
        wwLib.showAlert('No products found matching your criteria', 'info');
      }
      
    } catch (error) {
      console.error('Search failed:', error);
      wwLib.showAlert('Search failed. Please try again.', 'error');
    } finally {
      wwLib.hideLoading();
    }
  }
  
  static clearSearch() {
    wwLib.form.reset('searchForm');
    wwLib.collections.searchResults.clear();
    wwLib.variables.totalResults = 0;
    wwLib.variables.currentPage = 1;
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Create basic OR search:
1. Build a simple product search with name OR category matching
2. Add price range as an additional OR condition
3. Test with various combinations
4. Add basic result sorting

### Intermediate Challenge
Build flexible user search:
1. Create search across name, email, and phone fields
2. Add date range options (created this week OR this month)
3. Include status conditions (active OR pending)
4. Implement pagination for results

### Advanced Challenge
Design comprehensive search system:
1. Build dynamic query builder with unlimited OR conditions
2. Add performance monitoring for complex queries
3. Implement search result caching
4. Create search analytics and optimization

## Best Practices

1. **Index strategically** - Ensure all OR condition fields are indexed
2. **Limit OR conditions** - Too many can impact performance
3. **Use specific conditions** - Avoid overly broad OR logic
4. **Test performance** - Monitor query execution times
5. **Consider alternatives** - Full-text search for complex text matching
6. **Cache results** - Store frequently used OR query results

## Next Steps

- Master [Query All Records](query_all_records.md) for advanced filtering
- Learn [Using the Expression Builder](using_the_expression_builder.md) for dynamic conditions
- Explore [External Filtering Examples](external_filtering_examples.md) for complex patterns
- Understand [Database Requests](database_requests.md) for comprehensive operations

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Query logic discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Advanced filtering guides
- 📖 [Query Examples](../examples/complex-queries.md) - Real-world patterns
- 🔧 [Support](https://xano.com/support) - Complex query assistance