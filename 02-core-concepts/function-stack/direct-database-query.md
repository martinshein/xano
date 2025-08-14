---
title: "Direct Database Query - Advanced SQL Control"
description: "Execute custom SQL queries for complex database operations"
category: function-stack
subcategory: database
difficulty: advanced
has_code_examples: true
last_updated: '2025-01-23'
tags:
- sql
- database
- advanced
- queries
- custom
---

# Direct Database Query - Advanced SQL Control



## Quick Summary

> **What it is:** Execute raw SQL queries directly on your database for complex operations
> 
> **When to use:** Complex joins, aggregations, or operations not available in visual builder
> 
> **Key benefit:** Full SQL power when visual functions aren't enough
> 
> **Perfect for:** Advanced users needing complex queries, reports, or database operations

## What You'll Learn

- Writing safe SQL queries
- Using parameters securely
- Complex joins and aggregations
- Performance optimization
- Common SQL patterns

## ⚠️ Requirements

Direct Database Query requires:
- Launch or Scale plan (upgraded, non-Legacy)
- SQL knowledge
- Understanding of database structure

## Basic Setup

### Step 1: Add Function
1. Click + in function stack
2. Select "Database Operations"
3. Choose "Direct Database Query"

### Step 2: Write Query
```sql
-- Basic SELECT
SELECT * FROM mvpw1_3 
WHERE xdo->>'status' = 'active'
LIMIT 10
```

### Step 3: Configure
- **Response Type:** Single item or List
- **Output Variable:** Name for results

## Understanding Table Identifiers

### Format: mvpw{workspace_id}_{table_id}

```sql
-- If workspace ID = 1, table ID = 3
SELECT * FROM mvpw1_3

-- If workspace ID = 500, table ID = 3913
SELECT * FROM mvpw500_3913
```

### Column Access
```sql
-- Using mvpw (returns id and xdo columns)
SELECT id, xdo FROM mvpw1_3

-- Access JSON fields in xdo
SELECT 
  id,
  xdo->>'name' as name,
  xdo->>'email' as email
FROM mvpw1_3
```

### Using x Identifier (Readable View)
```sql
-- More readable format
SELECT * FROM x1_3
-- Note: Limited functionality for inserts
```

## Parameter Safety

### ❌ NEVER Do This (SQL Injection Risk)
```sql
-- DANGEROUS! Never concatenate values
"SELECT * FROM users WHERE email = '" + Input.email + "'"
```

### ✅ Always Use Parameters
```sql
-- Safe parameterized query
SELECT * FROM mvpw1_3 
WHERE xdo->>'email' = ?

-- Statement Args: [Input.email]
```

## Integration Examples

### With n8n - Complex Report
```sql
-- n8n requests sales report
SELECT 
  DATE(xdo->>'created_at') as date,
  COUNT(*) as total_orders,
  SUM((xdo->>'amount')::decimal) as revenue
FROM mvpw1_orders
WHERE xdo->>'created_at' >= ?
GROUP BY DATE(xdo->>'created_at')
ORDER BY date DESC

-- Args: [Input.start_date]
```

### With WeWeb - Search Query
```sql
-- Advanced search with multiple conditions
SELECT 
  id,
  xdo->>'title' as title,
  xdo->>'description' as description
FROM mvpw1_products
WHERE 
  (xdo->>'title' ILIKE ? OR xdo->>'description' ILIKE ?)
  AND (xdo->>'price')::decimal BETWEEN ? AND ?
  AND xdo->>'category' = ?
LIMIT 20

-- Args: ['%search%', '%search%', min_price, max_price, category]
```

## Common Query Patterns

### Joins Between Tables
```sql
-- Join users and orders
SELECT 
  u.xdo->>'name' as customer,
  COUNT(o.id) as order_count,
  SUM((o.xdo->>'total')::decimal) as total_spent
FROM mvpw1_users u
LEFT JOIN mvpw1_orders o ON o.xdo->>'user_id' = u.id::text
GROUP BY u.id, u.xdo->>'name'
```

### Aggregations
```sql
-- Sales by category
SELECT 
  xdo->>'category' as category,
  COUNT(*) as count,
  AVG((xdo->>'price')::decimal) as avg_price,
  MIN((xdo->>'price')::decimal) as min_price,
  MAX((xdo->>'price')::decimal) as max_price
FROM mvpw1_products
GROUP BY xdo->>'category'
```

### Window Functions
```sql
-- Ranking with row numbers
SELECT 
  xdo->>'name' as name,
  (xdo->>'score')::integer as score,
  ROW_NUMBER() OVER (ORDER BY (xdo->>'score')::integer DESC) as rank
FROM mvpw1_players
LIMIT 10
```

### Subqueries
```sql
-- Find above-average orders
SELECT * FROM mvpw1_orders
WHERE (xdo->>'total')::decimal > (
  SELECT AVG((xdo->>'total')::decimal)
  FROM mvpw1_orders
)
```

## Update Operations

### Bulk Updates
```sql
-- Update multiple records
UPDATE mvpw1_products
SET xdo = jsonb_set(xdo, '{on_sale}', 'true')
WHERE (xdo->>'price')::decimal > 100

-- Return affected count
RETURNING COUNT(*)
```

### Conditional Updates
```sql
-- Complex update logic
UPDATE mvpw1_users
SET xdo = CASE
  WHEN (xdo->>'purchases')::int >= 10 
    THEN jsonb_set(xdo, '{tier}', '"gold"')
  WHEN (xdo->>'purchases')::int >= 5
    THEN jsonb_set(xdo, '{tier}', '"silver"')
  ELSE xdo
END
WHERE xdo->>'active' = 'true'
```

## Insert Operations

### Batch Insert
```sql
-- Insert multiple records
INSERT INTO mvpw1_logs (xdo)
VALUES 
  ('{"action": "login", "user_id": 1, "timestamp": "2024-01-15T10:00:00Z"}'::jsonb),
  ('{"action": "view", "user_id": 1, "timestamp": "2024-01-15T10:05:00Z"}'::jsonb),
  ('{"action": "purchase", "user_id": 1, "timestamp": "2024-01-15T10:10:00Z"}'::jsonb)
```

## Performance Optimization

### Use Indexes
```sql
-- Check if field is indexed
EXPLAIN SELECT * FROM mvpw1_users
WHERE xdo->>'email' = 'test@example.com'

-- Create index (via Xano interface)
-- Then queries on that field are faster
```

### Limit Results
```sql
-- Always limit when possible
SELECT * FROM mvpw1_logs
ORDER BY xdo->>'timestamp' DESC
LIMIT 100  -- Don't fetch entire table!
```

### Optimize Joins
```sql
-- Filter before joining
WITH active_users AS (
  SELECT id, xdo FROM mvpw1_users
  WHERE xdo->>'status' = 'active'
)
SELECT * FROM active_users u
JOIN mvpw1_orders o ON o.xdo->>'user_id' = u.id::text
```

## Try This

Create a dashboard query:
1. Add Direct Database Query
2. Write aggregation query
3. Add date parameters
4. Test with sample data
5. Use results in response

## Pro Tips

💡 **Always Parameterize:** Never concatenate user input into queries

💡 **Test in Small Batches:** Use LIMIT during development

💡 **Monitor Performance:** Use EXPLAIN to check query plans

💡 **Index Key Fields:** Add indexes for WHERE clause fields

💡 **Backup Before Updates:** Test UPDATE/DELETE queries carefully

## Common Gotchas

### JSON Type Casting
```sql
-- Problem: JSON values are text
WHERE xdo->>'price' > 100  -- String comparison!

-- Solution: Cast to proper type
WHERE (xdo->>'price')::decimal > 100
```

### NULL Handling
```sql
-- Problem: NULL in JSON
WHERE xdo->>'field' = NULL  -- Doesn't work!

-- Solution: Use IS NULL
WHERE xdo->>'field' IS NULL
```

### Case Sensitivity
```sql
-- Case-sensitive
WHERE xdo->>'name' = 'John'  -- Won't match 'john'

-- Case-insensitive
WHERE xdo->>'name' ILIKE 'john'  -- Matches any case
```

## Next Steps

1. Learn basic SQL syntax
2. Understand your table structure
3. Practice with SELECT queries
4. Test UPDATE/DELETE carefully
5. Optimize with indexes

Remember: With great SQL power comes great responsibility - always validate and parameterize!