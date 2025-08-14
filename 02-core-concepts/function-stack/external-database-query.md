---
title: "External Database Query - Connect to Other Databases"
description: "Query PostgreSQL, MySQL, MS SQL, and Oracle databases from your Xano backend"
category: function-stack
subcategory: database
difficulty: advanced
has_code_examples: true
last_updated: '2025-01-23'
tags:
- external
- database
- postgresql
- mysql
- mssql
- oracle
---

# External Database Query - Connect to Other Databases



## Quick Summary

> **What it is:** Functions to connect and query external databases like PostgreSQL, MySQL, MS SQL, and Oracle
> 
> **When to use:** Integrating with existing databases, legacy systems, or third-party data sources
> 
> **Key benefit:** Access data from multiple databases without migration or complex synchronization
> 
> **Perfect for:** Non-developers building apps that need data from existing business systems

## What You'll Learn

- Supported database types
- Connection setup
- Writing secure queries
- Data integration patterns
- Error handling
- Performance optimization

## Supported Databases

### Available Connections
- **PostgreSQL** - Popular open-source database
- **MySQL** - Widely used web database
- **MS SQL Server** - Microsoft enterprise database
- **Oracle** - Enterprise database system

## Basic Setup

### Step 1: Add External Database Function
1. Click + in function stack
2. Select "Database Operations"
3. Choose your database type:
   - PostgreSQL Query
   - MySQL Query
   - MS SQL Query
   - Oracle Query

### Step 2: Configure Connection
```javascript
// Connection string format varies by database
PostgreSQL: "postgresql://username:password@host:port/database"
MySQL: "mysql://username:password@host:port/database"
MS SQL: "mssql://username:password@host:port/database"
Oracle: "oracle://username:password@host:port/service"
```

## Integration Examples

### With n8n - Legacy System Integration
```javascript
// n8n workflow needs customer data from old CRM
customer_id = Input.customer_id

// Query legacy PostgreSQL database
legacy_customer = PostgreSQL_Query {
  connection_string: env.LEGACY_DB_CONNECTION,
  query: `
    SELECT 
      customer_id,
      first_name,
      last_name,
      email,
      total_purchases,
      last_order_date
    FROM customers 
    WHERE customer_id = ?
  `,
  params: [customer_id]
}

if (legacy_customer && legacy_customer.length > 0) {
  customer = legacy_customer[0]
  
  // Store in Xano for faster access
  Add_Record {
    table: "customer_cache",
    customer_id: customer.customer_id,
    name: customer.first_name ~ " " ~ customer.last_name,
    email: customer.email,
    total_purchases: customer.total_purchases,
    last_order: customer.last_order_date,
    synced_at: timestamp()
  }
  
  return customer
} else {
  return {
    error: "Customer not found in legacy system"
  }
}
```

### With WeWeb - Multi-Database Dashboard
```javascript
// WeWeb dashboard showing data from multiple sources
date_filter = Input.date_from

// Query sales from MySQL e-commerce DB
ecommerce_sales = MySQL_Query {
  connection_string: env.ECOMMERCE_DB,
  query: `
    SELECT 
      DATE(created_at) as date,
      COUNT(*) as orders,
      SUM(total_amount) as revenue
    FROM orders 
    WHERE created_at >= ? 
    GROUP BY DATE(created_at)
    ORDER BY date
  `,
  params: [date_filter]
}

// Query inventory from PostgreSQL warehouse system
warehouse_data = PostgreSQL_Query {
  connection_string: env.WAREHOUSE_DB,
  query: `
    SELECT 
      product_sku,
      product_name,
      current_stock,
      reserved_stock,
      available_stock
    FROM inventory 
    WHERE current_stock < reorder_point
  `
}

// Query customer support from MS SQL
support_metrics = MSSQL_Query {
  connection_string: env.SUPPORT_DB,
  query: `
    SELECT 
      COUNT(CASE WHEN status = 'open' THEN 1 END) as open_tickets,
      COUNT(CASE WHEN status = 'resolved' AND resolved_date >= ? THEN 1 END) as resolved_today,
      AVG(CASE WHEN status = 'resolved' THEN DATEDIFF(hour, created_date, resolved_date) END) as avg_resolution_hours
    FROM support_tickets
  `,
  params: [date_filter]
}

return {
  sales_data: ecommerce_sales,
  low_stock_items: warehouse_data,
  support_metrics: support_metrics[0],
  dashboard_updated: timestamp()
}
```

## Connection String Setup

### PostgreSQL Connection
```javascript
// Basic connection
connection = "postgresql://user:password@localhost:5432/mydb"

// With SSL
connection = "postgresql://user:password@host:5432/db?sslmode=require"

// Environment variables (recommended)
connection = "postgresql://" ~ env.PG_USER ~ ":" ~ env.PG_PASSWORD ~ 
            "@" ~ env.PG_HOST ~ ":" ~ env.PG_PORT ~ "/" ~ env.PG_DATABASE
```

### MySQL Connection
```javascript
// Basic connection
connection = "mysql://user:password@localhost:3306/mydb"

// With charset
connection = "mysql://user:password@host:3306/db?charset=utf8mb4"

// Environment variables
connection = "mysql://" ~ env.MYSQL_USER ~ ":" ~ env.MYSQL_PASSWORD ~ 
            "@" ~ env.MYSQL_HOST ~ ":" ~ env.MYSQL_PORT ~ "/" ~ env.MYSQL_DATABASE
```

### MS SQL Server
```javascript
// Basic connection
connection = "mssql://user:password@localhost:1433/mydb"

// With instance
connection = "mssql://user:password@host\\SQLEXPRESS:1433/db"

// Environment variables
connection = "mssql://" ~ env.MSSQL_USER ~ ":" ~ env.MSSQL_PASSWORD ~ 
            "@" ~ env.MSSQL_HOST ~ ":" ~ env.MSSQL_PORT ~ "/" ~ env.MSSQL_DATABASE
```

### Oracle Connection
```javascript
// Service name connection
connection = "oracle://user:password@host:1521/service"

// SID connection
connection = "oracle://user:password@host:1521:SID"

// Environment variables
connection = "oracle://" ~ env.ORACLE_USER ~ ":" ~ env.ORACLE_PASSWORD ~ 
            "@" ~ env.ORACLE_HOST ~ ":" ~ env.ORACLE_PORT ~ "/" ~ env.ORACLE_SERVICE
```

## Secure Query Patterns

### Always Use Parameters
```javascript
// ❌ DANGEROUS - SQL injection risk
dangerous_query = "SELECT * FROM users WHERE email = '" ~ Input.email ~ "'"

// ✅ SAFE - Parameterized query
safe_query = MySQL_Query {
  connection_string: env.DB_CONNECTION,
  query: "SELECT * FROM users WHERE email = ?",
  params: [Input.email]
}
```

### Multiple Parameters
```javascript
// Safe parameterized query with multiple values
user_orders = PostgreSQL_Query {
  connection_string: env.DB_CONNECTION,
  query: `
    SELECT 
      order_id,
      total_amount,
      status,
      created_at
    FROM orders 
    WHERE user_id = ? 
    AND created_at BETWEEN ? AND ?
    ORDER BY created_at DESC
  `,
  params: [Input.user_id, Input.start_date, Input.end_date]
}
```

## Common Query Patterns

### Data Synchronization
```javascript
// Sync recent orders from external system
sync_cutoff = Variable("last_sync_time") ?? "1970-01-01"

external_orders = MySQL_Query {
  connection_string: env.EXTERNAL_DB,
  query: `
    SELECT 
      order_id,
      customer_email,
      total_amount,
      status,
      created_at,
      updated_at
    FROM orders 
    WHERE updated_at > ?
    ORDER BY updated_at ASC
  `,
  params: [sync_cutoff]
}

// Process each new/updated order
For Each order in external_orders {
  // Check if order exists in Xano
  existing = Query_All_Records {
    table: "orders",
    filter: {external_order_id: order.order_id}
  }
  
  if (existing && existing.length > 0) {
    // Update existing order
    Edit_Record {
      id: existing[0].id,
      status: order.status,
      total_amount: order.total_amount,
      updated_at: order.updated_at
    }
  } else {
    // Create new order
    Add_Record {
      table: "orders",
      external_order_id: order.order_id,
      customer_email: order.customer_email,
      total_amount: order.total_amount,
      status: order.status,
      created_at: order.created_at
    }
  }
}

// Update sync timestamp
Update_Variable("last_sync_time", timestamp())
```

### Aggregation Reports
```javascript
// Generate sales report from external database
report_data = PostgreSQL_Query {
  connection_string: env.SALES_DB,
  query: `
    WITH monthly_sales AS (
      SELECT 
        DATE_TRUNC('month', order_date) as month,
        COUNT(*) as order_count,
        SUM(order_total) as revenue,
        COUNT(DISTINCT customer_id) as unique_customers
      FROM sales_orders
      WHERE order_date >= ?
      GROUP BY DATE_TRUNC('month', order_date)
    ),
    growth_calc AS (
      SELECT 
        month,
        order_count,
        revenue,
        unique_customers,
        LAG(revenue) OVER (ORDER BY month) as prev_revenue
      FROM monthly_sales
    )
    SELECT 
      month,
      order_count,
      revenue,
      unique_customers,
      CASE 
        WHEN prev_revenue > 0 
        THEN ROUND(((revenue - prev_revenue) / prev_revenue * 100), 2)
        ELSE NULL
      END as growth_percent
    FROM growth_calc
    ORDER BY month DESC
  `,
  params: [Input.start_date]
}

return {
  report: report_data,
  generated_at: timestamp()
}
```

### Complex Joins
```javascript
// Join data from multiple tables with conditions
customer_analysis = MySQL_Query {
  connection_string: env.CRM_DB,
  query: `
    SELECT 
      c.customer_id,
      c.first_name,
      c.last_name,
      c.email,
      COUNT(DISTINCT o.order_id) as total_orders,
      SUM(o.order_total) as lifetime_value,
      MAX(o.order_date) as last_order_date,
      AVG(o.order_total) as avg_order_value,
      COUNT(DISTINCT p.product_category) as categories_purchased
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    LEFT JOIN order_items oi ON o.order_id = oi.order_id
    LEFT JOIN products p ON oi.product_id = p.product_id
    WHERE c.registration_date >= ?
    GROUP BY c.customer_id, c.first_name, c.last_name, c.email
    HAVING COUNT(DISTINCT o.order_id) >= ?
    ORDER BY lifetime_value DESC
  `,
  params: [Input.registration_cutoff, Input.min_orders]
}
```

## Error Handling

### Connection Error Handling
```javascript
Try {
  results = PostgreSQL_Query {
    connection_string: env.DB_CONNECTION,
    query: "SELECT * FROM products WHERE category = ?",
    params: [Input.category]
  }
  
  return {
    success: true,
    data: results
  }
} Catch (error) {
  // Log error for debugging
  Add_Log({
    type: "database_error",
    database_type: "postgresql",
    error_message: error.message,
    query_attempted: "product category query"
  })
  
  // Return user-friendly error
  return {
    success: false,
    error: "Unable to fetch products at this time",
    retry_after: 30
  }
}
```

### Timeout Handling
```javascript
// Set reasonable timeout for slow queries
Try {
  large_report = MySQL_Query {
    connection_string: env.REPORTING_DB,
    query: `
      SELECT /* COMPLEX REPORTING QUERY */
      FROM large_table lt
      JOIN other_table ot ON lt.id = ot.foreign_id
      WHERE lt.date_column >= ?
    `,
    params: [Input.start_date],
    timeout: 30000  // 30 second timeout
  }
  
  return large_report
} Catch (timeout_error) {
  // Offer alternative or suggest filtering
  return {
    error: "Query timeout - please try with a shorter date range",
    suggested_max_days: 30
  }
}
```

## Performance Optimization

### Indexing Considerations
```javascript
// Query with proper index usage
optimized_query = PostgreSQL_Query {
  connection_string: env.DB_CONNECTION,
  query: `
    -- Ensure indexes exist on:
    -- users(email)
    -- orders(user_id, created_at)
    -- order_items(order_id)
    
    SELECT 
      u.user_id,
      u.email,
      COUNT(o.order_id) as order_count,
      SUM(oi.quantity * oi.price) as total_spent
    FROM users u
    INNER JOIN orders o ON u.user_id = o.user_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    WHERE u.email = ? 
    AND o.created_at >= ?
    GROUP BY u.user_id, u.email
  `,
  params: [Input.email, Input.date_from]
}
```

### Pagination for Large Results
```javascript
// Paginated query for large datasets
page_size = 100
offset = (Input.page - 1) * page_size

paginated_results = MySQL_Query {
  connection_string: env.DB_CONNECTION,
  query: `
    SELECT 
      customer_id,
      first_name,
      last_name,
      email,
      registration_date
    FROM customers
    WHERE status = 'active'
    ORDER BY registration_date DESC
    LIMIT ? OFFSET ?
  `,
  params: [page_size, offset]
}

// Get total count for pagination
total_count = MySQL_Query {
  connection_string: env.DB_CONNECTION,
  query: "SELECT COUNT(*) as total FROM customers WHERE status = 'active'"
}

return {
  data: paginated_results,
  pagination: {
    current_page: Input.page,
    page_size: page_size,
    total_records: total_count[0].total,
    total_pages: Math.ceil(total_count[0].total / page_size)
  }
}
```

## Try This

Connect to an external database:
1. Set up connection string
2. Write a simple SELECT query
3. Add parameterization for safety
4. Handle errors gracefully
5. Test with real data

## Pro Tips

💡 **Use Environment Variables:** Never hardcode connection strings

💡 **Always Parameterize:** Prevent SQL injection with parameters

💡 **Set Timeouts:** Avoid hanging on slow queries

💡 **Index Wisely:** Ensure external database has proper indexes

💡 **Cache Results:** Store frequently accessed data in Xano

## Common Gotchas

### Connection String Format
```javascript
// Problem: Wrong format
connection = "postgres://user:pass@host/db"  // Missing port!

// Solution: Complete format
connection = "postgresql://user:pass@host:5432/db"
```

### Parameter Types
```javascript
// Problem: Wrong parameter type
MySQL_Query {
  query: "SELECT * FROM users WHERE age > ?",
  params: ["25"]  // String instead of number
}

// Solution: Correct type
MySQL_Query {
  query: "SELECT * FROM users WHERE age > ?",
  params: [25]  // Proper integer
}
```

### Special Characters in Passwords
```javascript
// Problem: Special characters in connection string
connection = "mysql://user:p@ssw0rd!@host:3306/db"  // @ in password breaks parsing

// Solution: URL encode special characters
encoded_password = url_encode("p@ssw0rd!")
connection = "mysql://user:" ~ encoded_password ~ "@host:3306/db"
```

## Next Steps

1. Set up secure connections
2. Practice parameterized queries
3. Implement error handling
4. Optimize query performance
5. Build data sync workflows

Remember: External databases expand your data access - use them wisely and securely!