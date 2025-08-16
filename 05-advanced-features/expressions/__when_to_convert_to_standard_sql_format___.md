---
title: Database Table Formats - JSONB vs Standard SQL
description: Complete guide to converting database tables from JSONB to standard SQL format in Xano, including when to convert and best practices for no-code platforms
category: expressions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - allow_direct_query.md
  - configuring-expressions.md
  - advanced_back_end_features.md
subcategory: 05-advanced-features/expressions
tags:
  - database-format
  - sql-conversion
  - jsonb-format
  - direct-database-connector
  - performance-optimization
  - no-code
---

## 📋 **Quick Summary**

Xano supports two database table formats: JSONB (JSON-based storage) and Standard SQL (traditional column-based). Understanding when and how to convert between formats is crucial for optimizing performance, enabling third-party tool integration, and building scalable applications with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Understanding JSONB vs Standard SQL table formats in Xano
- When to convert from JSONB to Standard SQL format
- Step-by-step conversion process and best practices
- Performance implications and optimization strategies
- Integration with external tools and no-code platforms
- Custom SQL table naming conventions

# Database Table Formats

## Overview

**Database Table Formats** in Xano determine how your data is structured and stored in the underlying PostgreSQL database. The choice between JSONB and Standard SQL format affects performance, compatibility with external tools, and integration capabilities with no-code platforms.

### Format Comparison

**JSONB Format:**
- **Structure**: Two columns per table (`id` and `jsonb`)
- **Storage**: JSON representation of the entire record in JSONB column
- **Performance**: Optimized for indexed queries and complex data structures
- **Compatibility**: Limited with traditional SQL tools

**Standard SQL Format:**
- **Structure**: Separate column for each field
- **Storage**: Traditional relational database layout
- **Performance**: Faster for non-indexed queries and analytics
- **Compatibility**: Full compatibility with external SQL tools

## 🔄 **When to Convert to Standard SQL Format**

### Use Cases for Standard SQL Format

**Third-Party Tool Integration:**
- **Business Intelligence**: Tableau, PowerBI, Looker integration
- **Analytics Platforms**: Direct SQL access for reporting
- **Data Visualization**: Tools that require standard column structure
- **ETL Processes**: Data pipeline tools that work with SQL schemas

**Performance Optimization:**
- **Non-Indexed Queries**: Faster performance on unindexed data
- **Large Dataset Analysis**: Better performance for analytical workloads
- **Column Addition**: Faster schema modifications
- **Bulk Operations**: Improved performance for large data operations

**Development Requirements:**
- **SQL Analytics**: Direct SQL query capabilities
- **Database Tools**: Native support for database administration tools
- **Reporting**: Complex reporting requirements
- **Data Migration**: Easier migration to/from other systems

### n8n Integration Example

```javascript
// n8n workflow for PostgreSQL direct connection
{
  "nodes": [
    {
      "name": "Connect to Xano Database",
      "type": "Postgres",
      "parameters": {
        "host": "{{ $env.XANO_DB_HOST }}",
        "database": "{{ $env.XANO_DB_NAME }}",
        "user": "{{ $env.XANO_DB_USER }}",
        "password": "{{ $env.XANO_DB_PASSWORD }}",
        "port": 5432,
        "ssl": true
      }
    },
    {
      "name": "Query User Analytics",
      "type": "Postgres",
      "parameters": {
        "query": `
          SELECT 
            u.id,
            u.email,
            u.first_name,
            u.last_name,
            u.created_at,
            COUNT(o.id) as total_orders,
            SUM(o.total_amount) as lifetime_value,
            AVG(o.total_amount) as avg_order_value,
            MAX(o.created_at) as last_order_date
          FROM users u
          LEFT JOIN orders o ON u.id = o.user_id
          WHERE u.created_at >= NOW() - INTERVAL '30 days'
          GROUP BY u.id, u.email, u.first_name, u.last_name, u.created_at
          ORDER BY lifetime_value DESC
          LIMIT 100
        `,
        "additionalFields": {}
      }
    },
    {
      "name": "Process Analytics Data",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const analytics = $input.all();
          
          // Calculate segmentation metrics
          const segmentedUsers = analytics.map(user => {
            const lifetimeValue = parseFloat(user.json.lifetime_value) || 0;
            const totalOrders = parseInt(user.json.total_orders) || 0;
            const avgOrderValue = parseFloat(user.json.avg_order_value) || 0;
            
            let segment = 'new';
            if (lifetimeValue > 1000 && totalOrders > 5) {
              segment = 'vip';
            } else if (lifetimeValue > 500 || totalOrders > 3) {
              segment = 'loyal';
            } else if (totalOrders > 0) {
              segment = 'returning';
            }
            
            return {
              json: {
                ...user.json,
                customer_segment: segment,
                days_since_signup: Math.floor((new Date() - new Date(user.json.created_at)) / (24 * 60 * 60 * 1000)),
                is_recent_customer: new Date(user.json.last_order_date) > new Date(Date.now() - 30 * 24 * 60 * 60 * 1000)
              }
            };
          });
          
          return segmentedUsers;
        `
      }
    },
    {
      "name": "Update Xano with Segments",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/bulk-update-segments",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "user_segments": "{{ $json }}"
        }
      }
    }
  ]
}
```

## ❌ **When to Keep JSONB Format**

### Optimal JSONB Use Cases

**Current Performance Satisfaction:**
- Existing queries perform well
- No performance bottlenecks identified
- Application requirements are met

**No External Tool Requirements:**
- All data access through Xano APIs
- No need for direct database connections
- No third-party analytics tools

**Dynamic Schema Requirements:**
- Frequently changing data structures
- Complex nested JSON data
- Flexible field requirements

**Xano-Centric Architecture:**
- All operations through Xano function stacks
- No external database operations
- Pure no-code approach

## 🔧 **Conversion Process**

### Step-by-Step Conversion

**Phase 1: Enable Standard SQL Format**

1. **Access Workspace Settings**
   - Navigate to workspace dashboard
   - Click settings icon (⚙️) in upper-right corner
   - Select "Settings" from menu

2. **Enable SQL Format**
   - Scroll to "Database Preferences" section
   - Check "Use standard SQL columns for new tables"
   - Save settings

**Phase 2: Convert Existing Tables**

3. **Select Tables for Conversion**
   - Access migration panel from workspace settings
   - Select tables to convert from JSONB to SQL format
   - Review conversion impact and dependencies

4. **Execute Migration**
   - Confirm table selection
   - Initiate migration process
   - Monitor conversion progress

### WeWeb Integration Example

```javascript
// WeWeb component for managing SQL table format
class XanoTableFormatManager {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async checkTableFormat(tableName) {
    try {
      const response = await fetch(`${this.baseUrl}/api/table-info/${tableName}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        }
      });
      
      const tableInfo = await response.json();
      return {
        format: tableInfo.format, // 'jsonb' or 'sql'
        column_count: tableInfo.columns.length,
        supports_direct_query: tableInfo.format === 'sql'
      };
    } catch (error) {
      console.error('Failed to check table format:', error);
      return null;
    }
  }
  
  async performDirectQuery(query) {
    try {
      const response = await fetch(`${this.baseUrl}/api/direct-query`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          query: query,
          format: 'standard_sql'
        })
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('query_results', result.data);
        wwLib.wwVariable.updateValue('query_execution_time', result.execution_time);
        return result.data;
      } else {
        throw new Error(result.error);
      }
    } catch (error) {
      console.error('Direct query failed:', error);
      wwLib.wwUtils.showErrorToast('Query execution failed');
      return null;
    }
  }
  
  async generateAnalyticsReport(tableName, dateRange) {
    const { startDate, endDate } = dateRange;
    
    const analyticsQuery = `
      SELECT 
        DATE_TRUNC('day', created_at) as date,
        COUNT(*) as daily_count,
        COUNT(DISTINCT user_id) as unique_users,
        AVG(CASE WHEN total_amount IS NOT NULL THEN total_amount END) as avg_value
      FROM ${tableName}
      WHERE created_at BETWEEN '${startDate}' AND '${endDate}'
      GROUP BY DATE_TRUNC('day', created_at)
      ORDER BY date DESC
    `;
    
    const results = await this.performDirectQuery(analyticsQuery);
    
    if (results) {
      // Process results for visualization
      const processedData = results.map(row => ({
        date: new Date(row.date).toLocaleDateString(),
        dailyCount: parseInt(row.daily_count),
        uniqueUsers: parseInt(row.unique_users),
        avgValue: parseFloat(row.avg_value) || 0,
        growthRate: 0 // Calculate in next step
      }));
      
      // Calculate growth rates
      for (let i = 1; i < processedData.length; i++) {
        const current = processedData[i].dailyCount;
        const previous = processedData[i - 1].dailyCount;
        processedData[i].growthRate = previous > 0 ? ((current - previous) / previous) * 100 : 0;
      }
      
      wwLib.wwVariable.updateValue('analytics_report', processedData);
      return processedData;
    }
    
    return null;
  }
}

// Initialize table format manager
const tableManager = new XanoTableFormatManager(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function checkCurrentTableFormat() {
  const tableName = wwLib.wwVariable.getValue('selected_table');
  const formatInfo = await tableManager.checkTableFormat(tableName);
  
  if (formatInfo) {
    wwLib.wwVariable.updateValue('table_format', formatInfo.format);
    wwLib.wwVariable.updateValue('can_use_direct_query', formatInfo.supports_direct_query);
  }
}

async function generateDashboardReport() {
  const tableName = wwLib.wwVariable.getValue('analytics_table');
  const dateRange = {
    startDate: wwLib.wwVariable.getValue('report_start_date'),
    endDate: wwLib.wwVariable.getValue('report_end_date')
  };
  
  await tableManager.generateAnalyticsReport(tableName, dateRange);
}
```

## 🔧 **Custom SQL Table Names**

### Naming Convention Management

**Default Naming:**
- Format: `mvpw<workspaceID>_<tableID>` (e.g., `mvpw1_3`)
- Automatic generation by Xano
- Globally unique across all workspaces

**Custom Naming Benefits:**
- **Readability**: Intuitive table names for direct queries
- **Tool Compatibility**: Better integration with external connectors
- **Documentation**: Self-documenting database schema
- **Team Collaboration**: Easier understanding for team members

### Custom Naming Configuration

**Enable Custom Names:**
1. Access Workspace Settings
2. Enable "Custom SQL Table Names"
3. Navigate to individual table settings
4. Click "Manage" next to SQL Table Name

**Naming Best Practices:**
```sql
-- Good examples
users
product_catalog
order_items
user_sessions
analytics_events

-- Use prefixes for workspace separation
proj_a_users
proj_a_orders
proj_b_users
proj_b_orders

-- Environment-specific suffixes (automatic)
users_test      -- Test datasource
users_staging   -- Staging datasource
users          -- Production datasource
```

## ⚡ **Performance Optimization**

### Format-Specific Optimizations

**JSONB Format Optimization:**
- **Indexing**: Create GIN indexes on JSONB fields
- **Queries**: Use JSONB operators for efficient filtering
- **Caching**: Implement Redis caching for frequently accessed data

**Standard SQL Optimization:**
- **Indexes**: Create B-tree indexes on frequently queried columns
- **Partitioning**: Use table partitioning for large datasets
- **Views**: Create materialized views for complex analytics

### Performance Monitoring

```javascript
// Performance comparison function stack
[
  {
    "function": "create_variable",
    "name": "performance_test_start",
    "value": "{{ now }}"
  },
  {
    "function": "conditional",
    "condition": "{{ table_format == 'sql' }}",
    "true_branch": [
      {
        "function": "direct_database_query",
        "query": "SELECT COUNT(*) FROM {{ table_name }} WHERE created_at > '{{ start_date }}'",
        "return_as": "sql_result"
      }
    ],
    "false_branch": [
      {
        "function": "query_all_records",
        "table": "{{ table_name }}",
        "filter": {
          "created_at": {"$gt": "{{ start_date }}"}
        },
        "return_as": "jsonb_result"
      }
    ]
  },
  {
    "function": "create_variable",
    "name": "execution_time",
    "value": "{{ now - performance_test_start }}"
  },
  {
    "function": "log_performance_metric",
    "metric_type": "query_performance",
    "data": {
      "table_format": "{{ table_format }}",
      "execution_time": "{{ execution_time }}",
      "query_type": "count_with_filter",
      "timestamp": "{{ now }}"
    }
  }
]
```

## 💡 **Pro Tips**

- **Test Before Converting**: Use test instances to validate performance impact
- **Backup Data**: Always backup before format conversion
- **Index Strategy**: Plan indexing strategy based on query patterns
- **Tool Testing**: Verify external tool compatibility after conversion
- **Monitor Performance**: Track query performance before and after conversion
- **Gradual Migration**: Convert tables in phases for large applications

## 🔧 **Troubleshooting**

### Common Conversion Issues

**Problem**: External tools can't connect after conversion  
**Solution**: Verify connection credentials and ensure tools support PostgreSQL standard format

**Problem**: Query performance degraded after conversion  
**Solution**: Create appropriate indexes on frequently queried columns

**Problem**: Custom table names not working  
**Solution**: Ensure names are globally unique and follow PostgreSQL naming conventions

**Problem**: Applications break after format conversion  
**Solution**: Update any hardcoded table references and test all API endpoints

---

**Next Steps**: Ready to optimize database performance? Explore [Allow Direct Query](allow_direct_query.md) for advanced query capabilities or check [Configuring Expressions](configuring-expressions.md) for dynamic data handling