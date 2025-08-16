---
title: "Xano Metadata API: Search and Browse"
description: "Master Xano's powerful Metadata API search capabilities for filtering, sorting, and retrieving database content with advanced query patterns"
category: expressions
has_code_examples: true
last_updated: '2025-01-16'
tags:
  - metadata-api
  - search
  - filtering
  - database-queries
  - api-integration
---

# Xano Metadata API: Search and Browse

## 📋 **Quick Summary**

Xano's Metadata API provides powerful search and browse capabilities for querying database content programmatically. Unlike regular APIs, the Metadata API bypasses access settings and enables complex filtering, sorting, and pagination operations essential for admin interfaces and data management tools.

## What You'll Learn

- Difference between Browse and Search operations
- Complex filtering with multiple conditions
- Search patterns using operators (equals, greater than, IN, NOT IN)
- Sorting strategies for single and multiple fields
- Pagination implementation and best practices
- Integration patterns for admin dashboards and reporting tools

## Understanding Browse vs Search

### Browse Content (Simple)

Browse is the straightforward method for retrieving table content with basic pagination:

**Use Cases:**
- Simple data listing
- Basic pagination needs
- Quick content retrieval
- Admin dashboard overviews

**Limitations:**
- No filtering capabilities
- No sorting options
- Basic pagination only

### Search (Advanced)

Search provides powerful filtering, sorting, and pagination with complex query capabilities:

**Use Cases:**
- Complex data filtering
- Multi-condition searches
- Sorted result sets
- Advanced admin interfaces
- Reporting and analytics

**Capabilities:**
- Multiple search conditions
- Various comparison operators
- Multi-field sorting
- Advanced pagination control

## Browse Content API

### Basic Browse Request

```javascript
// Simple browse request
const response = await fetch('/api:meta/content/{workspace_id}/{table_id}', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
  }
});

const data = await response.json();
```

### Browse Response Structure

```javascript
{
  "items": [
    {/* record 1 */},
    {/* record 2 */},
    {/* record 3 */},
    {/* record 4 */}
  ],
  "itemsReceived": 4,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 4,
  "pageTotal": 1
}
```

**Response Fields:**
- `items`: Array of database records
- `itemsReceived`: Number of items in current response
- `curPage`: Current page number
- `nextPage`/`prevPage`: Navigation information
- `itemsTotal`: Total records matching query
- `pageTotal`: Total number of pages

## Search API Fundamentals

### Search Endpoint

```http
POST /api:meta/content/{workspace_id}/{table_id}/search
```

### Request Structure Flexibility

Search accepts multiple request formats for different scenarios:

**Full Request with All Options:**
```javascript
{
  "page": 1,
  "per_page": 50,
  "sort": [/* sorting criteria */],
  "search": [/* search conditions */]
}
```

**Search-Only Request:**
```javascript
{
  "search": {/* single condition */}
}
```

**Array vs Object Search:**
- **Single Condition**: Use object format
- **Multiple Conditions**: Use array format

## Simple Search Patterns

### Search Where ID = 10

Find a specific record by ID:

```javascript
// Single condition as object
const searchRequest = {
  "search": {
    "field": "id",
    "operator": "=",
    "value": 10
  }
};

// Alternative array format
const searchRequestArray = {
  "search": [
    {
      "field": "id", 
      "operator": "=",
      "value": 10
    }
  ]
};
```

### Response for Single Record

```javascript
{
  "items": [
    {
      "id": 10,
      "name": "Product Name",
      "price": 45.99,
      "category": "Electronics"
    }
  ],
  "itemsReceived": 1,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 1,
  "pageTotal": 1
}
```

## Complex Search Patterns

### Range Queries (AND Logic)

Search for records where price is between 30 and 70:

```javascript
const rangeSearch = {
  "search": [
    {
      "field": "price",
      "operator": ">",
      "value": 30
    },
    {
      "field": "price", 
      "operator": "<",
      "value": 70
    }
  ]
};
```

**Result:** Returns records where price > 30 AND price < 70

### OR Logic Queries

Search for records where price < 30 OR price > 70:

```javascript
const orSearch = {
  "search": [
    {
      "field": "price",
      "operator": "<", 
      "value": 30
    },
    {
      "field": "price",
      "operator": ">",
      "value": 70,
      "or": true  // This makes it an OR condition
    }
  ]
};
```

**Important:** The `"or": true` is applied to the condition where it appears, creating OR logic with the previous condition.

## Advanced Operators

### IN and NOT IN Operators

**IN Operator** - Match any value in a list:

```javascript
const inSearch = {
  "search": {
    "field": "id",
    "operator": "IN",
    "value": [2, 3, 7]
  }
};
```

**NOT IN Operator** - Exclude values in a list:

```javascript
const notInSearch = {
  "search": {
    "field": "id", 
    "operator": "NOT IN",
    "value": [1, 2, 3, 4, 6, 7, 8, 9]
  }
};
```

### Text Search Operators

```javascript
// Exact match
{
  "field": "name",
  "operator": "=",
  "value": "Exact Product Name"
}

// Contains (case-insensitive)
{
  "field": "description",
  "operator": "LIKE",
  "value": "%keyword%"
}

// Starts with
{
  "field": "name",
  "operator": "LIKE", 
  "value": "Product%"
}

// Ends with
{
  "field": "name",
  "operator": "LIKE",
  "value": "%Name"
}
```

## Sorting Implementation

### Single Field Sorting

Sort by one field in ascending order:

```javascript
const singleSort = {
  "sort": {
    "field": "name",
    "direction": "asc"
  }
};

// Alternative array format (also valid)
const singleSortArray = {
  "sort": [
    {
      "field": "name",
      "direction": "asc"
    }
  ]
};
```

### Multi-Field Sorting

Sort by multiple fields with priority order:

```javascript
const multiSort = {
  "sort": [
    {
      "field": "rating",
      "direction": "desc"  // Primary sort: highest rating first
    },
    {
      "field": "name", 
      "direction": "asc"   // Secondary sort: alphabetical by name
    }
  ]
};
```

**Sort Priority:** First sort condition has highest priority, subsequent sorts break ties.

## Pagination Strategies

### Basic Pagination

```javascript
const paginatedSearch = {
  "page": 1,
  "per_page": 25,
  "search": {/* your search conditions */}
};
```

### Pagination Best Practices

```javascript
// Efficient pagination for large datasets
const efficientPagination = {
  "page": 1,
  "per_page": 100,  // Larger page size for fewer requests
  "sort": [
    {
      "field": "id",
      "direction": "asc"  // Consistent sorting for stable pagination
    }
  ],
  "search": {/* filtering conditions */}
};
```

## Try This: Admin Dashboard Search

Build a comprehensive product search for an admin dashboard:

```javascript
async function searchProducts(filters) {
  const searchConditions = [];
  
  // Name filter (if provided)
  if (filters.name) {
    searchConditions.push({
      "field": "name",
      "operator": "LIKE",
      "value": `%${filters.name}%`
    });
  }
  
  // Price range filter
  if (filters.minPrice) {
    searchConditions.push({
      "field": "price", 
      "operator": ">=",
      "value": filters.minPrice
    });
  }
  
  if (filters.maxPrice) {
    searchConditions.push({
      "field": "price",
      "operator": "<=", 
      "value": filters.maxPrice
    });
  }
  
  // Category filter
  if (filters.categories && filters.categories.length > 0) {
    searchConditions.push({
      "field": "category",
      "operator": "IN",
      "value": filters.categories
    });
  }
  
  const request = {
    "page": filters.page || 1,
    "per_page": filters.pageSize || 50,
    "sort": [
      {
        "field": filters.sortField || "created_at",
        "direction": filters.sortDirection || "desc"
      }
    ],
    "search": searchConditions
  };
  
  const response = await fetch('/api:meta/content/workspace/table/search', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + jwtToken,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(request)
  });
  
  return await response.json();
}

// Usage example
const results = await searchProducts({
  name: "laptop",
  minPrice: 500,
  maxPrice: 2000,
  categories: ["Electronics", "Computers"],
  page: 1,
  pageSize: 20,
  sortField: "price",
  sortDirection: "asc"
});
```

## Integration with No-Code Platforms

### WeWeb Integration

Use search API to power WeWeb data tables:

```javascript
// WeWeb custom function for dynamic search
async function fetchTableData(searchParams) {
  const searchRequest = {
    "page": searchParams.page || 1,
    "per_page": 50,
    "search": searchParams.filters || [],
    "sort": searchParams.sort || []
  };
  
  const response = await wwLib.executeWebflow({
    url: '/api:meta/content/workspace/table/search',
    method: 'POST',
    body: searchRequest
  });
  
  return response.data;
}
```

### Make.com Scenarios

Create automation scenarios using search data:

```javascript
// Make.com HTTP module configuration
{
  "url": "{{xano_base_url}}/api:meta/content/{{workspace_id}}/{{table_id}}/search",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{xano_jwt}}",
    "Content-Type": "application/json"
  },
  "body": {
    "search": [
      {
        "field": "status",
        "operator": "=", 
        "value": "pending"
      },
      {
        "field": "created_at",
        "operator": ">",
        "value": "{{yesterday_date}}"
      }
    ]
  }
}
```

### n8n Workflow Integration

Build monitoring workflows with search data:

```javascript
// n8n HTTP Request node for monitoring
{
  "method": "POST",
  "url": "=/api:meta/content/{{$json.workspace}}/{{$json.table}}/search",
  "authentication": "predefinedCredentialType",
  "credentialType": "xanoApi",
  "body": {
    "search": [
      {
        "field": "error_count",
        "operator": ">",
        "value": 10
      },
      {
        "field": "last_check",
        "operator": "<",
        "value": "={{DateTime.now().minus({hours: 1}).toISO()}}"
      }
    ]
  }
}
```

## Performance Optimization

### Indexing Considerations

**Fields to Index:**
- Frequently searched fields
- Sort fields
- Foreign key relationships
- Date/timestamp fields for range queries

### Efficient Query Patterns

```javascript
// Good: Specific conditions first
const efficientSearch = {
  "search": [
    {
      "field": "status",        // Indexed enum field
      "operator": "=",
      "value": "active"
    },
    {
      "field": "created_at",    // Indexed date field  
      "operator": ">",
      "value": "2024-01-01"
    },
    {
      "field": "description",   // Text search last
      "operator": "LIKE",
      "value": "%keyword%"
    }
  ]
};
```

### Large Dataset Strategies

```javascript
// For large datasets, use consistent sorting and smaller pages
const largeDatasetSearch = {
  "page": 1,
  "per_page": 25,           // Smaller page size
  "sort": [
    {
      "field": "id",          // Indexed unique field
      "direction": "asc"      // Consistent direction
    }
  ],
  "search": [/* specific filters */]
};
```

## Common Mistakes to Avoid

1. **OR Logic Confusion**: Remember `"or": true` applies to the condition where it's placed
2. **Over-Pagination**: Avoid very large page sizes that impact performance
3. **Missing Indexes**: Not indexing frequently searched fields
4. **Inconsistent Sorting**: Changing sort order between pagination requests
5. **Complex Text Searches**: Using LIKE patterns on non-indexed text fields for large datasets

## Pro Tips

1. **Field Selection**: Only request fields you actually need
2. **Consistent Sorting**: Always include a unique field in sort for stable pagination
3. **Filter Ordering**: Put most selective filters first for better performance
4. **Caching Strategy**: Cache search results for frequently accessed data
5. **Batch Processing**: Use larger page sizes for data export scenarios
6. **Error Handling**: Implement proper error handling for malformed queries

## API Scope Requirements

**Required Scope**: Workspace Database: Read

**Security Note**: The Metadata API bypasses normal API access settings and returns all fields regardless of field-level access configurations. Ensure proper authentication and authorization in your applications.

## Response Format Consistency

All search operations return the same response structure for consistent handling:

```javascript
{
  "items": [/* array of matching records */],
  "itemsReceived": Number,    // Items in current page
  "curPage": Number,          // Current page number  
  "nextPage": Number|null,    // Next page (null if last)
  "prevPage": Number|null,    // Previous page (null if first)
  "offset": Number,           // Record offset
  "itemsTotal": Number,       // Total matching records
  "pageTotal": Number         // Total pages available
}
```

The Xano Metadata API Search functionality provides enterprise-grade querying capabilities essential for building sophisticated admin interfaces, reporting tools, and data management systems. By mastering these search patterns and optimization techniques, you can create efficient, scalable applications that handle complex data requirements with ease.