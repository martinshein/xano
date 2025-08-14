---
title: "Database Indexing - Speed Up Your Queries by 95%"
description: "Learn how to use database indexes to dramatically improve query performance. Understand when and how to apply indexes for optimal speed without sacrificing write performance."
category: database
subcategory: performance
tags:
  - Indexing
  - Performance
  - Query Optimization
  - Database Speed
  - B-tree
  - GIN Index
  - Vector Search
difficulty: intermediate
reading_time: 15 minutes
last_updated: '2025-01-23'
prerequisites:
  - Database with 10,000+ records
  - Understanding of queries
  - Basic SQL knowledge helpful
---

# Database Indexing - Speed Up Your Queries by 95%

## 📋 **Quick Summary**

**What it does:** Indexes create special lookup tables that help your database find records instantly, like using a book's index instead of reading every page to find information.

**Why it matters:** Proper indexing can:
- Reduce query time from seconds to milliseconds (95%+ improvement)
- Enable real-time search in large datasets
- Support instant filtering in n8n/WeWeb apps
- Scale your app to millions of records
- Reduce server load and costs

**Time to implement:** 5 minutes per index, immediate results

---

## What You'll Learn

- How indexes work and when to use them
- Single vs. multi-field index strategies
- Step-by-step index implementation
- GIN indexes for complex data types
- Vector indexes for AI applications
- Common indexing mistakes to avoid
- Performance monitoring and optimization

## Understanding Database Indexes

### 📚 **What is an Index?**

Think of a database index like a book's index:

**Without an index (Full Table Scan):**
```
Looking for "authentication" in a 500-page book:
Page 1... no
Page 2... no
Page 3... no
[...497 more pages]
Time: 10 minutes
```

**With an index (Index Lookup):**
```
Check index: "authentication" → pages 42, 156, 289
Jump directly to those pages
Time: 10 seconds
```

### 🔍 **How Indexes Work**

Indexes create a separate, sorted data structure:

```yaml
Original Table (unsorted):
ID | Country  | Profession
5  | Canada   | Designer
2  | USA      | Developer
8  | Canada   | Developer
3  | Mexico   | Designer
...

Country Index (sorted):
Canada → Records: 5, 8, 12, 45...
Mexico → Records: 3, 9, 23...
USA → Records: 2, 6, 10, 34...
```

When you search for "Canada", the database jumps straight to matching records!

## When to Use Indexes

### ✅ **Perfect for Indexing**

Index these scenarios for massive speed gains:

```yaml
High-Value Scenarios:
✅ Frequently filtered columns (status, category, user_id)
✅ JOIN conditions (foreign keys)
✅ ORDER BY columns (created_at, price)
✅ WHERE clause columns
✅ Tables with 10,000+ records
✅ Columns with high selectivity
```

### ❌ **Avoid Indexing These**

Don't index in these situations:

```yaml
Low-Value Scenarios:
❌ Tables with < 1,000 records
❌ Columns with mostly NULL values
❌ Boolean fields (only 2 values)
❌ Frequently updated columns
❌ Columns rarely used in queries
❌ Tables with heavy write operations
```

## Real-World Performance Example

### 📊 **Case Study: 515,195 Records**

Let's see actual performance improvements:

**Test Setup:**
```yaml
Table: users
Records: 515,195
Fields: id, name, region, country, profession, email
Query: Find all users in Canada who are Developers
```

**Without Index:**
```sql
SELECT * FROM users 
WHERE country = 'Canada' 
AND profession = 'Developer'

Execution time: 620ms (0.62 seconds)
```

**With Indexes:**
```sql
CREATE INDEX idx_country ON users(country);
CREATE INDEX idx_profession ON users(profession);

-- Same query now:
Execution time: 50ms (0.05 seconds)
Result: 95% faster! 🚀
```

## Index Strategy Guide

### 🎯 **Single-Field Indexes**

Use when fields are queried independently:

```yaml
Scenario: E-commerce product search
Queries:
- Find all products in "Electronics"
- Find all products under $100
- Find all products by "Apple"

Strategy: Create separate indexes
- category_idx on category
- price_idx on price
- brand_idx on brand

Why: Each field is searched independently
```

### 🔗 **Multi-Field Indexes**

Use when fields are always queried together:

```yaml
Scenario: User location search
Query: Find users in specific city AND state

Strategy: Create compound index
- location_idx on (state, city)

Why: Fields always used together
Order matters: Less unique → More unique
```

### 📐 **Index Order Rules**

For multi-field indexes, order is crucial:

```yaml
Good Order (Less → More Unique):
1. country (195 possible values)
2. state (50 possible values)
3. city (10,000+ possible values)
4. street (millions of values)

Bad Order (More → Less Unique):
1. timestamp (almost all unique)
2. user_id (all unique)
3. status (3 values)
Result: Index barely helps!
```

## Creating Indexes in Xano

### 🛠️ **Step-by-Step Process**

1. **Navigate to Database:**
   ```
   Database → Select Table → Indexes Tab
   ```

2. **Click "Create Index"**

3. **Configure Index:**
   ```yaml
   Name: idx_user_location
   Type: Index (standard)
   Fields: 
     1. country (ASC)
     2. profession (ASC)
   ```

4. **Save and Wait:**
   - Small tables: Instant
   - Large tables: Several minutes
   - Monitor progress in UI

### ⚡ **Quick Index Examples**

**User Authentication:**
```yaml
Index: idx_email
Field: email
Type: Unique
Use: Login queries, prevent duplicates
```

**Order Management:**
```yaml
Index: idx_order_status_date
Fields: status, created_at
Use: Find pending orders by date
```

**Product Search:**
```yaml
Index: idx_category_price
Fields: category, price
Use: Category browsing with price filters
```

## Advanced Index Types

### 🔍 **GIN Index (Complex Data)**

For JSON, arrays, and full-text search:

```javascript
// Searching arrays with GIN index
// Table has field: tags = ['electronics', 'sale', 'featured']

// Create search variable:
const searchVar = {
  tags: ['sale']  // Find records containing 'sale'
};

// Query using 'contains' operator
// GIN index makes this instant!
```

**Setup in Xano:**
```yaml
Type: GIN
Field: tags (array/JSON field)
Automatic: Yes (pre-configured)
Performance: 0.23s → 0.02s (91% faster)
```

### 🤖 **Vector Index (AI/ML)**

For similarity search and AI embeddings:

```yaml
Use Cases:
- Semantic search
- Recommendation systems
- Image similarity
- Content matching

Index Types:
- L2 Distance: Euclidean distance
- Inner Product: OpenAI embeddings (recommended)
- Cosine Distance: Direction similarity
```

**Always index vector columns - even with few records!**

### 🗺️ **Spatial Index**

For geographic data:

```yaml
Field Type: Geography/Geometry
Use Cases:
- Find nearby locations
- Radius searches
- Polygon contains point
- Distance calculations
```

## Index Best Practices

### 📋 **Planning Checklist**

Before creating indexes:

```yaml
✅ Analyze slow queries first
✅ Check current query execution time
✅ Identify WHERE/JOIN/ORDER BY columns
✅ Consider write vs. read frequency
✅ Plan for data growth
✅ Test in development first
```

### 🎯 **Optimization Strategy**

1. **Start with Problem Queries:**
   ```sql
   -- Identify slow queries
   -- Check Request History
   -- Look for patterns
   ```

2. **Measure Before/After:**
   ```yaml
   Before Index: 1.44 seconds
   After Index: 0.02 seconds
   Improvement: 98% faster
   ```

3. **Monitor Storage:**
   ```yaml
   Index Storage Impact:
   - Each index: 10-30% table size
   - Keep total storage < 50% capacity
   - Remove unused indexes
   ```

## Integration Optimization

### 🔧 **n8n Performance**

Optimize API calls with proper indexing:

```javascript
// n8n HTTP Request node
{
  "url": "https://api.xano.io/users",
  "qs": {
    "country": "Canada",      // Indexed
    "profession": "Developer", // Indexed
    "limit": 100
  }
}

// Without indexes: 2-3 second timeout risk
// With indexes: 50ms response ✓
```

### 🌐 **WeWeb Collections**

Enable real-time filtering:

```yaml
WeWeb Collection Setup:
- Filter by category (indexed)
- Sort by price (indexed)
- Search by name (indexed)

Result: Instant UI updates
No loading spinners needed!
```

## Common Indexing Patterns

### 🛒 **E-Commerce**

```yaml
Products Table:
- idx_category_price: (category, price)
- idx_brand: brand
- idx_sku: sku (unique)
- idx_status_stock: (status, stock_quantity)

Orders Table:
- idx_user_date: (user_id, created_at)
- idx_status: status
- idx_tracking: tracking_number (unique)
```

### 👥 **User Management**

```yaml
Users Table:
- idx_email: email (unique)
- idx_username: username (unique)
- idx_status_created: (status, created_at)
- idx_role: role

Sessions Table:
- idx_token: token (unique)
- idx_user_expires: (user_id, expires_at)
```

### 📝 **Content Management**

```yaml
Posts Table:
- idx_status_published: (status, published_at)
- idx_author: author_id
- idx_category_tags: (category, tags) [GIN]
- idx_search: title, content [Full-text]
```

## Troubleshooting Slow Queries

### 🔍 **Diagnosis Steps**

1. **Check if index exists:**
   ```sql
   -- In Database → Table → Indexes
   -- Verify field is indexed
   ```

2. **Verify index is used:**
   ```yaml
   Common issues:
   - Wrong field order in multi-field index
   - Query doesn't match index exactly
   - NULL values preventing index use
   ```

3. **Index not helping?**
   ```yaml
   Possible causes:
   - Too many records match (low selectivity)
   - Table too small for index benefit
   - Complex query needing different index
   ```

## Monitoring & Maintenance

### 📊 **Performance Tracking**

```yaml
Weekly Review:
1. Check Request History for slow queries
2. Identify patterns in slow requests
3. Review index usage statistics
4. Remove unused indexes
5. Add indexes for new query patterns
```

### 🧹 **Index Cleanup**

```yaml
Signs to Remove Index:
- Query pattern changed
- Feature deprecated
- Index never used (check logs)
- Duplicate indexes exist
- Write performance suffering
```

## Try This: Speed Up Your App

### 📝 **Exercise: Optimize User Search**

Your app has 50,000 users and this query is slow:

```sql
SELECT * FROM users 
WHERE status = 'active' 
AND country = 'USA' 
AND created_at > '2024-01-01'
ORDER BY last_login DESC
```

**Your mission:**
1. Time the current query
2. Create appropriate indexes
3. Re-test query speed
4. Document improvement

**Solution:**
```yaml
Indexes to create:
1. idx_status_country: (status, country)
2. idx_created: created_at
3. idx_last_login: last_login DESC

Expected improvement: 90-95% faster
```

## Common Questions

### "How many indexes are too many?"

```yaml
Guidelines:
- 3-5 indexes per table typical
- Max 10 for complex tables
- Each index adds storage overhead
- Monitor write performance
```

### "Should I index foreign keys?"

```yaml
Almost always YES:
- Speeds up JOINs dramatically
- Improves relationship queries
- Essential for good performance
```

### "When do indexes update?"

```yaml
Automatically on:
- INSERT: New entry added to index
- UPDATE: Index entry moved if needed
- DELETE: Entry removed from index

No manual refresh needed!
```

## Best Practices Summary

### ✅ **Do's**

1. **Index foreign keys** always
2. **Test in development** first
3. **Monitor query performance** regularly
4. **Use compound indexes** for related fields
5. **Index before going live** with data
6. **Document your indexes** and their purpose

### ❌ **Don'ts**

1. **Don't over-index** small tables
2. **Don't index** high-write tables heavily
3. **Don't ignore** storage limits
4. **Don't index** low-selectivity columns
5. **Don't forget** index maintenance
6. **Don't index** frequently changing columns

## Next Steps

After understanding indexing:

1. **Audit your slowest queries** using Request History
2. **Create strategic indexes** based on patterns
3. **Measure improvements** and document
4. **Set up monitoring** for new slow queries
5. **Plan index review** schedule (monthly)
6. **Share knowledge** with your team

## Related Documentation

- [Database Basics](./database-basics.md)
- [Query Optimization](../function-stack/query-all-records.md)
- [Database Maintenance](./database-maintenance.md)
- [Direct Database Connector](./direct-database-connector.md)
- [Performance Troubleshooting](../../troubleshooting/performance.md)