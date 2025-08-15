---
title: "Data Manipulation Functions - Transform & Process Data"
description: "Master data manipulation in Xano function stacks - transform, filter, sort, and process data efficiently for dynamic applications"
category: function-stack
tags:
  - Data Manipulation
  - Data Processing
  - Transform
  - Filter
  - Sort
  - Array Operations
  - Data Transformation
difficulty: intermediate
reading_time: 12 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of data types (arrays, objects)
  - Basic function stack knowledge
  - Familiarity with JSON structure
---

# Data Manipulation Functions - Transform & Process Data

## 📋 **Quick Summary**

**What it does:** Data manipulation functions provide powerful tools to transform, filter, sort, and process data within your Xano function stacks.

**Why it matters:** This enables you to:
- Transform raw data into formats needed by your frontend
- Filter large datasets based on dynamic criteria
- Sort and organize data for optimal user experience
- Process complex data structures for business logic

**Time to implement:** 15-20 minutes for basic operations, 45+ minutes for complex transformations

---

## What You'll Learn

- Core data manipulation functions and their uses
- Transforming arrays and objects efficiently
- Filtering and sorting techniques
- Data validation and cleaning
- Integration patterns with n8n and WeWeb

## Core Data Manipulation Functions

### Array Operations

#### Filter Arrays
Remove unwanted items based on conditions:
```javascript
// Filter active users only
users.filter(user => user.is_active === true)

// Filter products by price range
products.filter(product => product.price >= 50 && product.price <= 200)
```

#### Map/Transform Arrays
Convert each item in an array:
```javascript
// Extract just names from user objects
users.map(user => user.name)

// Add calculated fields
products.map(product => ({
  ...product,
  discounted_price: product.price * 0.9
}))
```

#### Sort Arrays
Organize data in specific order:
```javascript
// Sort users by creation date (newest first)
users.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))

// Sort products by price (lowest first)
products.sort((a, b) => a.price - b.price)
```

### Object Manipulation

#### Add/Modify Properties
```javascript
// Add new properties to objects
const enrichedUser = {
  ...user,
  full_name: `${user.first_name} ${user.last_name}`,
  is_premium: user.subscription_type === 'premium'
}
```

#### Extract Specific Fields
```javascript
// Pick only needed fields
const publicUserData = {
  id: user.id,
  name: user.name,
  avatar: user.avatar_url
}
```

## Common Data Manipulation Patterns

### Pattern 1: E-commerce Product Processing
```javascript
// Process product data for frontend display
const processedProducts = rawProducts
  .filter(product => product.is_active && product.stock > 0)
  .map(product => ({
    id: product.id,
    name: product.name,
    display_price: `$${product.price.toFixed(2)}`,
    image_url: product.images[0]?.url || '/default-product.jpg',
    in_stock: product.stock > 0,
    is_sale: product.sale_price < product.regular_price
  }))
  .sort((a, b) => b.is_sale - a.is_sale); // Sale items first
```

### Pattern 2: User Data Aggregation
```javascript
// Aggregate user activity data
const userStats = users.map(user => {
  const recentOrders = orders.filter(order => 
    order.user_id === user.id && 
    order.created_at > thirtyDaysAgo
  );
  
  return {
    id: user.id,
    name: user.name,
    total_orders: recentOrders.length,
    total_spent: recentOrders.reduce((sum, order) => sum + order.total, 0),
    last_order_date: Math.max(...recentOrders.map(o => o.created_at))
  };
});
```

### Pattern 3: Content Organization
```javascript
// Organize blog posts by category with metadata
const organizedContent = posts
  .filter(post => post.is_published)
  .reduce((acc, post) => {
    const category = post.category || 'uncategorized';
    if (!acc[category]) {
      acc[category] = [];
    }
    acc[category].push({
      ...post,
      read_time: Math.ceil(post.word_count / 200) + ' min read'
    });
    return acc;
  }, {});
```

## No-Code Platform Integration

### 🌐 **WeWeb Data Processing**

Transform Xano data for WeWeb components:

```javascript
// WeWeb collection processing
async function processProductsForWeWeb(rawProducts) {
  return rawProducts
    .filter(product => product.is_active)
    .map(product => ({
      ...product,
      // WeWeb-friendly format
      display_price: `$${product.price}`,
      image_src: product.featured_image?.url || '/placeholder.jpg',
      category_name: product.category?.name || 'Uncategorized',
      // Add WeWeb-specific properties
      ww_id: product.id,
      ww_href: `/products/${product.slug}`
    }))
    .sort((a, b) => a.sort_order - b.sort_order);
}
```

### 🔗 **n8n Workflow Data Processing**

Process data within n8n workflows:

```yaml
n8n Workflow: Customer Data Enrichment
1. HTTP Request → Get customers from Xano
2. Function Node → Process and enrich data
   ```javascript
   // Enrich customer data
   const enrichedCustomers = items.map(customer => ({
     ...customer,
     full_name: `${customer.first_name} ${customer.last_name}`,
     segment: customer.total_orders > 10 ? 'vip' : 'regular',
     last_seen: new Date(customer.last_login).toLocaleDateString()
   }));
   ```
3. HTTP Request → Send enriched data to CRM
```

### 🔧 **Make Data Transformation**

Transform arrays in Make scenarios:

```yaml
Make Scenario: Order Processing
1. Xano API → Get order details
2. Array Aggregator → Combine order items
3. Iterator → Process each item
   - Text Parser → Extract product details
   - Math → Calculate totals
   - Date/Time → Format dates
4. HTTP Request → Send to fulfillment service
```

## Advanced Data Manipulation Techniques

### Nested Array Processing
```javascript
// Process orders with line items
const processedOrders = orders.map(order => ({
  ...order,
  line_items: order.items.map(item => ({
    ...item,
    total: item.quantity * item.price,
    product_name: products.find(p => p.id === item.product_id)?.name
  })),
  order_total: order.items.reduce((sum, item) => 
    sum + (item.quantity * item.price), 0
  )
}));
```

### Dynamic Grouping
```javascript
// Group data by dynamic field
function groupBy(array, key) {
  return array.reduce((groups, item) => {
    const group = item[key];
    if (!groups[group]) {
      groups[group] = [];
    }
    groups[group].push(item);
    return groups;
  }, {});
}

// Usage: Group users by subscription type
const usersBySubscription = groupBy(users, 'subscription_type');
```

### Data Validation and Cleaning
```javascript
// Clean and validate user input
function cleanUserData(rawUserData) {
  return {
    name: rawUserData.name?.trim() || '',
    email: rawUserData.email?.toLowerCase().trim() || '',
    age: Math.max(0, parseInt(rawUserData.age) || 0),
    preferences: Array.isArray(rawUserData.preferences) 
      ? rawUserData.preferences 
      : [],
    created_at: new Date().toISOString()
  };
}
```

## Performance Optimization

### Efficient Array Processing
```javascript
// ✅ Good: Chain operations efficiently
const result = data
  .filter(item => item.active)  // Reduce dataset first
  .map(item => transformItem(item))
  .slice(0, 100);  // Limit results

// ❌ Avoid: Processing large arrays multiple times
const filtered = data.filter(item => item.active);
const mapped = filtered.map(item => transformItem(item));
const limited = mapped.slice(0, 100);
```

### Memory-Efficient Processing
```javascript
// For large datasets, process in chunks
function processInChunks(array, chunkSize, processor) {
  const results = [];
  for (let i = 0; i < array.length; i += chunkSize) {
    const chunk = array.slice(i, i + chunkSize);
    results.push(...processor(chunk));
  }
  return results;
}
```

## 💡 **Try This: Build a Product Search System**

Create a comprehensive product search with multiple filters:

### Step 1: Define Search Parameters
```javascript
const searchParams = {
  query: "laptop",
  category: "electronics",
  min_price: 500,
  max_price: 2000,
  in_stock: true,
  sort_by: "price",
  sort_order: "asc"
};
```

### Step 2: Apply Filters
```javascript
function searchProducts(products, params) {
  return products
    .filter(product => {
      // Text search
      const matchesQuery = !params.query || 
        product.name.toLowerCase().includes(params.query.toLowerCase()) ||
        product.description.toLowerCase().includes(params.query.toLowerCase());
      
      // Category filter
      const matchesCategory = !params.category || 
        product.category === params.category;
      
      // Price range
      const inPriceRange = 
        (!params.min_price || product.price >= params.min_price) &&
        (!params.max_price || product.price <= params.max_price);
      
      // Stock filter
      const stockFilter = !params.in_stock || product.stock > 0;
      
      return matchesQuery && matchesCategory && inPriceRange && stockFilter;
    })
    .sort((a, b) => {
      const field = params.sort_by || 'name';
      const order = params.sort_order === 'desc' ? -1 : 1;
      
      if (a[field] < b[field]) return -1 * order;
      if (a[field] > b[field]) return 1 * order;
      return 0;
    });
}
```

### Step 3: Add Metadata
```javascript
function enrichSearchResults(results, params) {
  return {
    results: results.map(product => ({
      ...product,
      relevance_score: calculateRelevance(product, params.query),
      is_featured: product.featured || false,
      discount_percentage: product.sale_price 
        ? Math.round((1 - product.sale_price / product.price) * 100) 
        : 0
    })),
    total_count: results.length,
    filters_applied: Object.keys(params).filter(key => params[key]),
    search_metadata: {
      query: params.query,
      category: params.category,
      price_range: `${params.min_price || 0} - ${params.max_price || '∞'}`
    }
  };
}
```

## Common Mistakes to Avoid

❌ **Modifying original arrays/objects**
- Use spread operator `...` or `Array.from()` for copies
- Avoid mutating methods like `push()`, `splice()` on original data

❌ **Inefficient nested loops**
- Use `Map` objects for lookups instead of nested `find()` calls
- Pre-index related data when possible

❌ **Not handling edge cases**
- Check for null/undefined values before processing
- Handle empty arrays and objects gracefully

❌ **Complex operations in single chain**
- Break complex transformations into readable steps
- Use intermediate variables for clarity

## Pro Tips

💡 **Use Lodash for Complex Operations**
Xano supports Lodash for advanced data manipulation:
```javascript
// Group by multiple fields
const grouped = _.groupBy(data, item => `${item.category}-${item.status}`);

// Deep merge objects
const merged = _.merge({}, defaultConfig, userConfig);
```

💡 **Cache Expensive Transformations**
Store processed data to avoid repeated calculations:
```javascript
// Cache lookup tables
const categoryLookup = new Map(
  categories.map(cat => [cat.id, cat.name])
);
```

💡 **Validate Data Structure**
Always check data types before manipulation:
```javascript
if (Array.isArray(data) && data.length > 0) {
  // Safe to process array
}
```

---

**Next Steps:** Ready to filter data? Learn about [Filter Functions](filters.md) for advanced filtering or explore [Array Functions](arrays.md) for array-specific operations.