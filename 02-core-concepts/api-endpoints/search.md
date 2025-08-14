---
title: "Database Search with Metadata API - Complete Guide"
description: "Master powerful database search and filtering with Xano's Metadata API - perfect for building advanced queries, sorting, and pagination in n8n, WeWeb, and Make"
category: api-endpoints
tags:
  - Database Search
  - Metadata API
  - Filtering
  - Sorting
  - Pagination
  - Query Operations
difficulty: intermediate
reading_time: 12 minutes
last_updated: '2025-01-23'
prerequisites:
  - Metadata API access token
  - Understanding of database tables
  - Basic knowledge of filtering and sorting
---

# Database Search with Metadata API

## 📋 **Quick Summary**

**What it does:** The Metadata API's search functionality provides powerful database querying capabilities with advanced filtering, sorting, and pagination - all without writing custom API endpoints.

**Why it matters:** This enables you to:
- Build complex search interfaces without custom endpoints
- Create advanced filtering and sorting in no-code tools
- Implement powerful data discovery features
- Query database content programmatically from any platform

**Time to implement:** 5-10 minutes for basic searches, 30+ minutes for complex filtering

---

## What You'll Learn

- Browse vs Search: when to use each approach
- Advanced filtering with comparison operators
- Complex search queries with AND/OR logic
- Multi-field sorting techniques
- Pagination strategies for large datasets
- Integration patterns for no-code platforms

## Understanding Search vs Browse

Think of Browse as a simple "show me all records" request, while Search is like having a powerful SQL WHERE clause that you can build visually.

### 🎯 **Browse Content - Perfect For:**
- Simple table listings
- Paginated record displays
- Quick data previews
- Admin panel overviews

### 🎯 **Search Content - Perfect For:**
- Advanced filtering interfaces
- Dynamic search forms
- Data analytics queries
- Complex business logic

## Authentication Setup

All search operations require Metadata API authentication:

```javascript
headers: {
  'Authorization': 'Bearer YOUR_METADATA_TOKEN',
  'Content-Type': 'application/json'
}
```

## Simple Browse Operations

### Basic Table Browse

Get all records from a table with optional pagination:

```json
GET /api:metadata/content/browse
{
  "workspace_id": 12345,
  "table_id": 67890,
  "page": 1,
  "per_page": 50
}
```

### 📝 **Example Response**

```json
{
  "items": [
    {
      "id": 1,
      "created_at": 1681336868222,
      "name": "Basketball",
      "description": "Round ball to shoot hoops",
      "category_id": 1,
      "price": 25.99
    }
  ],
  "itemsReceived": 1,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 156,
  "pageTotal": 4
}
```

### 💡 **Browse Use Cases**

```yaml
Perfect for:
- Product catalogs
- User lists
- Content galleries
- Admin dashboards
- Data exports
```

## Advanced Search Operations

### Basic Equality Search

Find records where a field equals a specific value:

```json
POST /api:metadata/content/search
{
  "workspace_id": 12345,
  "table_id": 67890,
  "search": {
    "status": "active"
  }
}
```

### Range Searches

Find records within a value range:

```json
{
  "workspace_id": 12345,
  "table_id": 67890,
  "search": [
    {
      "price|>": 30
    },
    {
      "price|<": 100
    }
  ]
}
```

### OR Logic Searches

Find records matching any of multiple conditions:

```json
{
  "search": [
    {
      "category": "electronics"
    },
    {
      "category|or": "computers"
    },
    {
      "category|or": "phones"
    }
  ]
}
```

## Comparison Operators Reference

| Operator | Syntax | Description | Example |
|----------|--------|-------------|---------|
| **Equals** | `"field": value` | Exact match | `"status": "active"` |
| **Greater than** | `"field|>": value` | Numeric comparison | `"price|>": 50` |
| **Less than** | `"field|<": value` | Numeric comparison | `"age|<": 30` |
| **Greater or equal** | `"field|>=": value` | Inclusive comparison | `"rating|>=": 4` |
| **Less or equal** | `"field|<=": value` | Inclusive comparison | `"quantity|<=": 10` |
| **Not equal** | `"field|!=": value` | Exclusion | `"status|!=": "deleted"` |
| **In list** | `"field|in": [values]` | Multiple values | `"category|in": [1,2,3]` |
| **Not in list** | `"field|not in": [values]` | Exclusion list | `"id|not in": [5,10,15]` |
| **Contains** | `"field|~": "text"` | Text search | `"name|~": "phone"` |
| **Starts with** | `"field|^=": "text"` | Prefix search | `"email|^=": "admin"` |
| **OR condition** | `"field|or": value` | Alternative condition | `"type|or": "premium"` |

## Complex Search Examples

### Multi-Field Product Search

```json
{
  "workspace_id": 12345,
  "table_id": 67890,
  "search": [
    {
      "name|~": "phone"
    },
    {
      "price|>": 100
    },
    {
      "price|<": 800
    },
    {
      "category|in": ["electronics", "mobile"]
    },
    {
      "status": "available"
    }
  ],
  "sort": [
    {
      "price": "asc"
    },
    {
      "rating": "desc"
    }
  ],
  "page": 1,
  "per_page": 20
}
```

### User Search with Date Filtering

```json
{
  "search": [
    {
      "created_at|>": 1681305600000
    },
    {
      "email|^=": "admin"
    },
    {
      "status|or": "premium"
    },
    {
      "status|or": "vip"
    }
  ],
  "sort": {
    "created_at": "desc"
  }
}
```

### E-commerce Inventory Query

```json
{
  "search": [
    {
      "quantity|>": 0
    },
    {
      "category|not in": ["discontinued", "seasonal"]
    },
    {
      "price|>=": 10
    },
    {
      "featured": true
    }
  ]
}
```

## Sorting Strategies

### Single Field Sort

```json
{
  "sort": {
    "created_at": "desc"
  }
}
```

### Multi-Field Sort

```json
{
  "sort": [
    {
      "priority": "desc"
    },
    {
      "created_at": "asc"
    },
    {
      "name": "asc"
    }
  ]
}
```

### 🎯 **Common Sort Patterns**

```yaml
E-commerce Products:
- Price (low to high)
- Rating (high to low)
- Newest first

User Management:
- Last login (recent first)
- Registration date (oldest first)
- Alphabetical by name

Content Systems:
- Publication date (newest first)
- View count (popular first)
- Category, then title
```

## Pagination Best Practices

### Standard Pagination

```json
{
  "page": 1,
  "per_page": 25,
  "search": {...},
  "sort": {...}
}
```

### Large Dataset Handling

```javascript
// For tables with 10k+ records
const searchConfig = {
  per_page: 100, // Larger pages for efficiency
  page: 1,
  search: {
    // Always include indexed fields for performance
    "created_at|>": lastWeek,
    "status": "active"
  },
  sort: {
    "id": "asc" // Use indexed field for consistent ordering
  }
};
```

### Performance Optimization

```javascript
// ✅ Good - Use indexed fields
{
  "search": {
    "id|in": [1, 2, 3, 4, 5],
    "status": "published"
  }
}

// ❌ Avoid - Text search on non-indexed fields
{
  "search": {
    "description|~": "random text search"
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Advanced Search Workflow**

```yaml
1. HTTP Request (Trigger with search parameters)
2. Set Node (Build search query)
3. HTTP Request (Call Metadata API search)
4. Function Node (Process results)
5. IF Node (Check result count)
6. Respond to Webhook (Return formatted data)
```

**n8n Search Query Builder:**
```javascript
// Build dynamic search from form inputs
const searchFilters = [];

if ($input.priceMin) {
  searchFilters.push({ "price|>": $input.priceMin });
}

if ($input.priceMax) {
  searchFilters.push({ "price|<": $input.priceMax });
}

if ($input.category) {
  searchFilters.push({ "category": $input.category });
}

if ($input.searchTerm) {
  searchFilters.push({ "name|~": $input.searchTerm });
}

return {
  workspace_id: 12345,
  table_id: 67890,
  search: searchFilters,
  sort: { [$input.sortBy || 'created_at']: $input.sortOrder || 'desc' },
  page: $input.page || 1,
  per_page: $input.limit || 20
};
```

### 🌐 **WeWeb Dynamic Search Component**

```javascript
// WeWeb search function with advanced filtering
async function searchProducts(filters) {
  const searchQuery = {
    workspace_id: wwLib.envVars.WORKSPACE_ID,
    table_id: wwLib.envVars.PRODUCTS_TABLE_ID,
    search: [],
    sort: []
  };
  
  // Add price range filter
  if (filters.minPrice) {
    searchQuery.search.push({ "price|>": filters.minPrice });
  }
  if (filters.maxPrice) {
    searchQuery.search.push({ "price|<": filters.maxPrice });
  }
  
  // Add category filter
  if (filters.categories && filters.categories.length > 0) {
    searchQuery.search.push({ "category_id|in": filters.categories });
  }
  
  // Add text search
  if (filters.searchText) {
    searchQuery.search.push({ "name|~": filters.searchText });
  }
  
  // Add sorting
  if (filters.sortBy) {
    searchQuery.sort.push({ [filters.sortBy]: filters.sortOrder || 'asc' });
  }
  
  const response = await wwLib.api.post({
    url: wwLib.envVars.XANO_METADATA_API + '/content/search',
    data: searchQuery,
    headers: {
      'Authorization': 'Bearer ' + wwLib.envVars.METADATA_TOKEN
    }
  });
  
  // Update WeWeb collections
  wwLib.collections.searchResults.update(response.data.items);
  wwLib.variables.pagination.setValue({
    currentPage: response.data.curPage,
    totalPages: response.data.pageTotal,
    totalItems: response.data.itemsTotal
  });
  
  return response.data;
}
```

### 🔧 **Make Search & Filter Scenario**

```yaml
Scenario: Dynamic Product Search
1. Webhook (Receive search parameters)
2. Set Variable (Build search array)
3. Iterator (Process each filter condition)
4. HTTP Request (Search Metadata API)
5. Array Aggregator (Combine results)
6. Webhook Response (Return formatted data)
```

**Make Filter Builder Module:**
```json
{
  "search": [
    {{if(1.minPrice != null; {"price|>": 1.minPrice}; null)}},
    {{if(1.maxPrice != null; {"price|<": 1.maxPrice}; null)}},
    {{if(1.category != null; {"category_id": 1.category}; null)}},
    {{if(1.inStock; {"quantity|>": 0}; null)}}
  ]
}
```

## Common Search Patterns

### Pattern 1: E-commerce Product Filter

```javascript
class ProductSearchBuilder {
  constructor() {
    this.filters = [];
    this.sorts = [];
  }
  
  priceRange(min, max) {
    if (min) this.filters.push({ "price|>": min });
    if (max) this.filters.push({ "price|<": max });
    return this;
  }
  
  categories(categoryIds) {
    if (categoryIds.length > 0) {
      this.filters.push({ "category_id|in": categoryIds });
    }
    return this;
  }
  
  inStock() {
    this.filters.push({ "quantity|>": 0 });
    return this;
  }
  
  searchText(query) {
    if (query) {
      this.filters.push({ "name|~": query });
    }
    return this;
  }
  
  sortByPrice(direction = 'asc') {
    this.sorts.push({ "price": direction });
    return this;
  }
  
  build() {
    return {
      search: this.filters,
      sort: this.sorts
    };
  }
}

// Usage
const searchQuery = new ProductSearchBuilder()
  .priceRange(50, 200)
  .categories([1, 2, 3])
  .inStock()
  .searchText("wireless")
  .sortByPrice('asc')
  .build();
```

### Pattern 2: User Management Search

```javascript
function buildUserSearchQuery(criteria) {
  const search = [];
  
  // Role-based filtering
  if (criteria.roles && criteria.roles.length > 0) {
    search.push({ "role|in": criteria.roles });
  }
  
  // Registration date range
  if (criteria.registeredAfter) {
    search.push({ "created_at|>": criteria.registeredAfter });
  }
  
  // Activity status
  if (criteria.activeOnly) {
    search.push({ "last_login|>": Date.now() - (30 * 24 * 60 * 60 * 1000) });
  }
  
  // Email domain filtering
  if (criteria.emailDomain) {
    search.push({ "email|~": `@${criteria.emailDomain}` });
  }
  
  return {
    search,
    sort: [
      { "last_login": "desc" },
      { "created_at": "desc" }
    ]
  };
}
```

### Pattern 3: Content Management Search

```javascript
function searchContent(params) {
  const searchFilters = [];
  
  // Publication status
  if (params.published !== undefined) {
    searchFilters.push({ "status": params.published ? "published" : "draft" });
  }
  
  // Author filtering
  if (params.authorId) {
    searchFilters.push({ "author_id": params.authorId });
  }
  
  // Date range
  if (params.dateFrom) {
    searchFilters.push({ "published_at|>": params.dateFrom });
  }
  if (params.dateTo) {
    searchFilters.push({ "published_at|<": params.dateTo });
  }
  
  // Tag filtering
  if (params.tags && params.tags.length > 0) {
    params.tags.forEach((tag, index) => {
      if (index === 0) {
        searchFilters.push({ "tags|~": tag });
      } else {
        searchFilters.push({ "tags|~|or": tag });
      }
    });
  }
  
  return {
    search: searchFilters,
    sort: [
      { "featured": "desc" },
      { "published_at": "desc" }
    ]
  };
}
```

## Error Handling & Performance

### Common Search Errors

| Error Code | Issue | Solution |
|------------|-------|----------|
| 400 | Invalid search syntax | Check field names and operators |
| 401 | Authentication failed | Verify Metadata API token |
| 413 | Query too complex | Reduce search conditions |
| 429 | Rate limited | Implement retry logic |
| 500 | Database timeout | Optimize query or add indexes |

### Performance Optimization

```javascript
// ✅ Optimized search patterns
const optimizedSearch = {
  // Use indexed fields first
  search: [
    { "status": "active" },        // Indexed field
    { "category_id": 5 },          // Foreign key (indexed)
    { "created_at|>": lastWeek },  // Date field (indexed)
    { "name|~": searchTerm }       // Text search last
  ],
  // Limit results
  per_page: 50,
  // Sort by indexed fields
  sort: { "created_at": "desc" }
};

// ❌ Avoid inefficient patterns
const slowSearch = {
  search: [
    { "description|~": "long text search" }, // Slow text search
    { "complex_calculation|>": 100 }         // Computed field
  ],
  per_page: 1000, // Too many results
  sort: { "description": "asc" } // Sorting by text field
};
```

## 💡 **Try This**

### Beginner Challenge
Build a basic product search that:
1. Filters by price range
2. Searches product names
3. Sorts by price or name
4. Shows 20 results per page

### Intermediate Challenge
Create an advanced user finder that:
1. Combines multiple search criteria
2. Uses OR logic for role filtering
3. Implements date range filtering
4. Provides multi-field sorting

### Advanced Challenge
Design a complex analytics query that:
1. Filters across multiple related tables
2. Implements advanced date filtering
3. Uses statistical aggregation
4. Optimizes for performance

## Common Mistakes to Avoid

1. **Too many OR conditions** - Can slow down queries significantly
2. **Text search on large fields** - Use indexed fields when possible
3. **Missing pagination** - Always limit results for performance
4. **Complex sorts on unindexed fields** - Can cause timeouts
5. **No error handling** - Search queries can fail for various reasons

## Next Steps

- Learn about [Content Management](content.md) for creating and updating
- Explore [Request History](request-history.md) for monitoring searches
- Master [File Operations](file.md) for media-rich content
- Understand [Token Security](token-scopes-reference.md) for access control

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Search and filtering discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step examples
- 📖 [Metadata API Docs](master-metadata-api.md) - Complete reference
- 🔧 [Support](https://xano.com/support) - Technical assistance