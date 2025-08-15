---
title: "Query All Records Function"
description: "Retrieve multiple database records with filtering, sorting, and pagination using Xano's Query All Records function"
category: function-stack
difficulty: beginner
tags:
  - database
  - query
  - filtering
  - pagination
  - sorting
  - crud
  - search
related_docs:
  - get-record
  - add-record
  - edit-record
  - external-filtering-examples
  - patch-record
last_updated: '2025-01-23'
---

# Query All Records Function

## Quick Summary
Query All Records retrieves multiple database records with powerful filtering, sorting, and pagination capabilities. Essential for building lists, feeds, search results, and data tables that display collections of data efficiently.

## What You'll Learn
- Retrieving multiple records with complex filters
- Implementing search and sorting functionality
- Adding pagination for large datasets
- Building dynamic query parameters for flexible APIs
- Integration patterns for n8n data processing and WeWeb displays

## Core Features

### Basic Operations
- **Retrieve All** - Get all records from a table
- **Apply Filters** - Use WHERE conditions to filter results
- **Sort Results** - Order by specific fields (ascending/descending)
- **Limit Records** - Control number of records returned
- **Offset/Pagination** - Navigate through large datasets efficiently

### Advanced Filtering
- **Multiple Conditions** - Combine AND/OR logic for complex queries
- **Range Filters** - Date ranges, numeric ranges, between operations
- **Text Search** - LIKE, CONTAINS, starts with, ends with
- **Relationship Filters** - Filter by related table data
- **Null Checks** - Include or exclude records with null values

## Basic Query Structure

### Simple Record Retrieval
```sql
-- Basic query for all active products
SELECT * FROM products 
WHERE status = 'active'
ORDER BY created_at DESC
LIMIT 20
```

### With Pagination
```sql
-- Paginated results (page 2, 10 records per page)
SELECT * FROM products 
WHERE status = 'active'
ORDER BY name ASC
LIMIT 10 OFFSET 10
```

## Filtering Techniques

### Single Field Filtering
```javascript
// Filter products by category
{
  "table": "products",
  "filter": {
    "category": "electronics"
  },
  "sort": "name",
  "limit": 20
}
```

### Multiple Field Filtering
```javascript
// Complex filtering with multiple conditions
{
  "table": "products",
  "filter": {
    "category": "electronics",
    "price": {"<=": 500},
    "status": "active",
    "created_at": {">": "2024-01-01"}
  },
  "sort": "price",
  "order": "asc"
}
```

### Range and Comparison Filters
```javascript
// Various comparison operators
{
  "filters": {
    "price": {
      ">=": 100,
      "<=": 1000
    },
    "rating": {">": 4.0},
    "stock": {"!=": 0},
    "name": {"like": "%wireless%"}
  }
}
```

## Search Implementation

### Text Search Across Multiple Fields
```javascript
// Search products by name or description
function searchProducts(searchTerm) {
  return {
    "table": "products",
    "filter": {
      "OR": [
        {"name": {"like": `%${searchTerm}%`}},
        {"description": {"like": `%${searchTerm}%`}},
        {"tags": {"like": `%${searchTerm}%`}}
      ]
    },
    "sort": "relevance_score",
    "order": "desc"
  };
}
```

### Advanced Search with Weighting
```javascript
// Weighted search results
function advancedProductSearch(query) {
  return {
    "table": "products",
    "filter": {
      "OR": [
        {"name": {"like": `%${query}%`}},        // Higher weight
        {"description": {"like": `%${query}%`}}, // Medium weight
        {"category": {"like": `%${query}%`}}     // Lower weight
      ],
      "status": "active"
    },
    "sort": "CASE WHEN name LIKE '%${query}%' THEN 1 ELSE 2 END, popularity",
    "limit": 50
  };
}
```

## Sorting and Ordering

### Multiple Sort Criteria
```javascript
// Sort by multiple fields with priority
{
  "table": "products",
  "sort": [
    {"field": "featured", "order": "desc"},    // Featured first
    {"field": "rating", "order": "desc"},      // Then by rating
    {"field": "price", "order": "asc"}         // Then by price
  ]
}
```

### Dynamic Sorting
```javascript
// Allow frontend to specify sort options
function getProducts(sortBy = 'created_at', sortOrder = 'desc') {
  const allowedSorts = ['name', 'price', 'rating', 'created_at', 'popularity'];
  const allowedOrders = ['asc', 'desc'];
  
  return {
    "table": "products",
    "sort": allowedSorts.includes(sortBy) ? sortBy : 'created_at',
    "order": allowedOrders.includes(sortOrder) ? sortOrder : 'desc',
    "limit": 20
  };
}
```

## Pagination Implementation

### Offset-Based Pagination
```javascript
// Traditional pagination with page numbers
function getPaginatedProducts(page = 1, perPage = 20) {
  const offset = (page - 1) * perPage;
  
  return {
    "table": "products",
    "filter": {"status": "active"},
    "sort": "created_at",
    "order": "desc",
    "limit": perPage,
    "offset": offset
  };
}
```

### Cursor-Based Pagination
```javascript
// More efficient for large datasets
function getProductsCursor(lastId = null, limit = 20) {
  let filter = {"status": "active"};
  
  if (lastId) {
    filter.id = {">": lastId};
  }
  
  return {
    "table": "products",
    "filter": filter,
    "sort": "id",
    "order": "asc",
    "limit": limit
  };
}
```

## Integration with n8n

### Data Collection for Processing
```javascript
// n8n workflow to process all user orders
const getAllOrders = {
  "table": "orders",
  "filter": {
    "status": "completed",
    "created_at": {
      ">=": "2024-01-01",
      "<=": "2024-12-31"
    }
  },
  "sort": "created_at",
  "order": "desc"
};

// Process in n8n Function Node
const orders = $json.orders;

// Group by month for reporting
const monthlyStats = orders.reduce((acc, order) => {
  const month = new Date(order.created_at).getMonth();
  acc[month] = (acc[month] || 0) + order.total;
  return acc;
}, {});

return { monthlyRevenue: monthlyStats };
```

### Batch Processing Pattern
```javascript
// n8n workflow for bulk email sending
function getBatchUsers(batchSize = 100, offset = 0) {
  return {
    "table": "users",
    "filter": {
      "email_verified": true,
      "marketing_consent": true,
      "status": "active"
    },
    "sort": "id",
    "limit": batchSize,
    "offset": offset
  };
}

// Process in batches to avoid timeouts
// n8n can loop through batches automatically
```

## Integration with WeWeb

### Dynamic Product Listing
```javascript
// WeWeb component for product catalog
export default {
  data() {
    return {
      products: [],
      filters: {
        category: '',
        minPrice: 0,
        maxPrice: 1000,
        searchTerm: ''
      },
      pagination: {
        currentPage: 1,
        perPage: 12,
        totalPages: 1
      },
      loading: false
    };
  },
  
  async mounted() {
    await this.loadProducts();
  },
  
  methods: {
    async loadProducts() {
      this.loading = true;
      
      try {
        const queryParams = this.buildQueryParams();
        const response = await this.$xano.get('/products', queryParams);
        
        this.products = response.data.products;
        this.pagination.totalPages = Math.ceil(response.data.total / this.pagination.perPage);
      } catch (error) {
        console.error('Failed to load products:', error);
      } finally {
        this.loading = false;
      }
    },
    
    buildQueryParams() {
      const params = {
        page: this.pagination.currentPage,
        per_page: this.pagination.perPage
      };
      
      // Add filters if they have values
      if (this.filters.category) {
        params.category = this.filters.category;
      }
      
      if (this.filters.searchTerm) {
        params.search = this.filters.searchTerm;
      }
      
      if (this.filters.minPrice > 0) {
        params.min_price = this.filters.minPrice;
      }
      
      if (this.filters.maxPrice < 1000) {
        params.max_price = this.filters.maxPrice;
      }
      
      return params;
    },
    
    async applyFilters() {
      this.pagination.currentPage = 1; // Reset to first page
      await this.loadProducts();
    },
    
    async changePage(page) {
      this.pagination.currentPage = page;
      await this.loadProducts();
    }
  },
  
  watch: {
    // Reactive filtering
    'filters.searchTerm': {
      handler: 'applyFilters',
      immediate: false
    }
  }
};
```

### Real-time Search Component
```javascript
// WeWeb search component with debouncing
export default {
  data() {
    return {
      searchQuery: '',
      searchResults: [],
      isSearching: false,
      searchTimeout: null
    };
  },
  
  methods: {
    async performSearch() {
      if (!this.searchQuery.trim()) {
        this.searchResults = [];
        return;
      }
      
      this.isSearching = true;
      
      try {
        const response = await this.$xano.get('/search/products', {
          q: this.searchQuery,
          limit: 10
        });
        
        this.searchResults = response.data;
      } catch (error) {
        console.error('Search failed:', error);
        this.searchResults = [];
      } finally {
        this.isSearching = false;
      }
    },
    
    onSearchInput() {
      // Debounce search to avoid too many requests
      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(() => {
        this.performSearch();
      }, 300);
    }
  }
};
```

## Advanced Query Patterns

### Relationship Filtering
```javascript
// Query products with category information
{
  "table": "products",
  "joins": [
    {
      "table": "categories",
      "on": "products.category_id = categories.id"
    }
  ],
  "filter": {
    "categories.name": "Electronics",
    "products.status": "active"
  },
  "select": [
    "products.*",
    "categories.name as category_name"
  ]
}
```

### Aggregation Queries
```javascript
// Get product counts by category
{
  "table": "products",
  "groupBy": "category_id",
  "select": [
    "category_id",
    "COUNT(*) as product_count",
    "AVG(price) as avg_price"
  ],
  "filter": {
    "status": "active"
  },
  "sort": "product_count",
  "order": "desc"
}
```

### Conditional Filtering
```javascript
// Dynamic filters based on user role
function getProductsForUser(userId, userRole) {
  let filter = {"status": "active"};
  
  if (userRole !== 'admin') {
    // Regular users only see published products
    filter.published = true;
  }
  
  if (userRole === 'vendor') {
    // Vendors only see their own products
    filter.vendor_id = userId;
  }
  
  return {
    "table": "products",
    "filter": filter,
    "sort": "created_at",
    "order": "desc"
  };
}
```

## Try This: Build a Complete Product Search API

1. **Create Search Endpoint**
   ```
   1. Accept search term, filters, sort, and pagination parameters
   2. Build dynamic query with Query All Records
   3. Apply text search across multiple fields
   4. Include category and price range filters
   5. Return paginated results with metadata
   ```

2. **Add Advanced Features**
   ```
   1. Implement search suggestions/autocomplete
   2. Add faceted search (category counts)
   3. Include related products
   4. Log search analytics
   5. Cache popular search results
   ```

3. **Frontend Integration**
   ```
   1. Build WeWeb search interface
   2. Add real-time search with debouncing
   3. Implement infinite scroll pagination
   4. Add filter chips and clear options
   5. Show search result counts and timing
   ```

## Performance Optimization

### Database Indexing
```sql
-- Create indexes for commonly filtered fields
CREATE INDEX idx_products_status ON products(status);
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_products_search ON products(name, description);
```

### Query Optimization
```javascript
// Optimize queries for large datasets
function getOptimizedProducts() {
  return {
    "table": "products",
    "select": [
      "id", "name", "price", "image_url", "category_id"
      // Only select needed fields
    ],
    "filter": {"status": "active"},
    "sort": "id", // Use indexed field for sorting
    "limit": 20
  };
}
```

### Caching Strategy
```javascript
// Cache frequently accessed queries
function getCachedProducts(cacheKey, filters) {
  // 1. Check cache for existing results
  // 2. If cache miss, execute query
  // 3. Store results in cache with TTL
  // 4. Return cached or fresh results
}
```

## Common Mistakes to Avoid

❌ **Not implementing pagination** - Large result sets can timeout
❌ **Missing database indexes** - Queries become slow on large tables
❌ **Over-fetching data** - Only select needed columns
❌ **Ignoring SQL injection** - Always use parameterized queries
❌ **Not caching results** - Repeated queries waste resources
❌ **Poor error handling** - Always handle query failures gracefully

## Pro Tips

💡 **Use database indexes** for all frequently filtered and sorted fields
💡 **Implement cursor-based pagination** for better performance on large datasets
💡 **Cache common queries** with appropriate TTL values
💡 **Validate all inputs** before building queries
💡 **Use LIMIT clauses** to prevent accidentally large result sets
💡 **Monitor query performance** and optimize slow queries
💡 **Implement search analytics** to understand user behavior
💡 **Use full-text search** for complex text searching needs

Query All Records is the foundation for building dynamic, searchable, and user-friendly data displays in your Xano applications.