---
title: Working with Data - Complete Data Management and Transformation Guide
description: Comprehensive guide to working with data in Xano including variables, database operations, filters, transformations, and integration patterns for no-code platforms
category: custom-functions
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - functions.md
  - custom-functions.md
  - right_value.md
subcategory: 05-advanced-features/custom-functions
tags:
  - data-management
  - variables
  - database-operations
  - data-transformation
  - filters
  - no-code
---

## 📋 **Quick Summary**

Working with data in Xano involves understanding the flow of information through your function stacks, from database operations to variable manipulation and data transformation. Master these concepts to build powerful applications with n8n, WeWeb, and other no-code platforms that handle complex data processing efficiently.

## What You'll Learn

- Understanding database vs variables and their appropriate uses
- How data flows through function stacks and variable management
- Advanced data transformation techniques and filters
- Complex data manipulation patterns and best practices
- Integration strategies for no-code platforms
- Performance optimization for data-heavy operations

# Working with Data

## Overview

**Working with Data** in Xano encompasses all aspects of data handling in your workflows - from retrieving information from databases to manipulating variables, transforming data with filters, and passing information between functions. Understanding these concepts is crucial for building efficient, scalable applications.

### Data Flow Architecture

**Data Sources:**
- **Database**: Persistent storage for long-term data
- **API Inputs**: Data from external requests
- **Variables**: Temporary storage within function stacks
- **External APIs**: Data from third-party services
- **Computed Values**: Results from calculations and transformations

**Data Destinations:**
- **Database Records**: Stored for future retrieval
- **API Responses**: Returned to clients
- **Variables**: Passed to subsequent functions
- **External Systems**: Sent via webhooks or API calls

## 🗄️ **Database vs Variables**

### Database Storage

**Use database storage for persistent data that needs to be:**
- Accessed across multiple workflows
- Retrieved after the current session ends
- Shared between different users or processes
- Maintained for historical or analytical purposes

**Examples of Database Data:**
```javascript
// User account information
{
  "id": 123,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "created_at": "2024-01-15T10:30:00Z",
  "subscription_tier": "premium"
}

// Product catalog data
{
  "id": 456,
  "name": "Wireless Headphones",
  "price": 99.99,
  "category": "electronics",
  "stock_quantity": 50,
  "description": "High-quality wireless headphones"
}

// Order history
{
  "id": 789,
  "user_id": 123,
  "items": [{"product_id": 456, "quantity": 2}],
  "total_amount": 199.98,
  "status": "completed",
  "order_date": "2024-01-16T14:20:00Z"
}
```

### Variable Storage

**Use variables for temporary data needed only within the current workflow:**
- Intermediate calculations and processing results
- Transformed data before saving to database
- API response formatting
- Loop counters and conditional flags
- Temporary data aggregations

**Examples of Variable Data:**
```javascript
// Function stack with variable usage
[
  {
    "function": "create_variable",
    "name": "current_timestamp",
    "value": "{{ now }}"
  },
  {
    "function": "create_variable",
    "name": "user_full_name",
    "value": "{{ user.first_name }} {{ user.last_name }}"
  },
  {
    "function": "create_variable",
    "name": "discount_amount",
    "value": "{{ order.total * user.discount_rate }}"
  },
  {
    "function": "create_variable",
    "name": "final_total",
    "value": "{{ order.total - discount_amount }}"
  }
]
```

## 🔧 **Data in Function Stacks**

### Function Output Variables

**Every function can produce output stored in variables using `return_as`:**

```javascript
// Database query with variable storage
{
  "function": "query_single_record",
  "table": "users",
  "filter": {"id": "{{ request.body.user_id }}"},
  "return_as": "user_data" // Variable name for storing result
}

// Using the stored variable in subsequent functions
{
  "function": "conditional",
  "condition": "{{ user_data.subscription_tier == 'premium' }}",
  "true_branch": [
    {
      "function": "query_all_records",
      "table": "premium_features",
      "return_as": "available_features"
    }
  ]
}
```

### Variable Chaining Patterns

**Sequential Data Processing:**

```javascript
// Complex data processing workflow
[
  {
    "function": "query_all_records",
    "table": "orders",
    "filter": {
      "user_id": "{{ auth.user.id }}",
      "status": "completed",
      "created_at": {"$gte": "{{ now - 2592000 }}"} // Last 30 days
    },
    "return_as": "recent_orders"
  },
  {
    "function": "create_variable",
    "name": "order_totals",
    "value": "{{ recent_orders|map(attribute='total_amount') }}"
  },
  {
    "function": "create_variable",
    "name": "total_spent",
    "value": "{{ order_totals|sum }}"
  },
  {
    "function": "create_variable",
    "name": "average_order_value",
    "value": "{{ total_spent / recent_orders|length }}"
  },
  {
    "function": "create_variable",
    "name": "user_analytics",
    "value": {
      "total_orders": "{{ recent_orders|length }}",
      "total_spent": "{{ total_spent }}",
      "average_order_value": "{{ average_order_value }}",
      "period": "last_30_days",
      "calculated_at": "{{ now }}"
    }
  }
]
```

## 🔍 **Data Transformation with Filters**

### Text Transformation Filters

**String manipulation and formatting:**

```javascript
// Text transformation examples
{
  "function": "create_variable",
  "name": "processed_text_data",
  "value": {
    "original_name": "{{ user.first_name }}",
    "uppercase_name": "{{ user.first_name|upper }}",
    "lowercase_email": "{{ user.email|lower }}",
    "capitalized_name": "{{ user.first_name|capitalize }}",
    "trimmed_bio": "{{ user.bio|trim }}",
    "truncated_description": "{{ product.description|truncate(100) }}",
    "slug_from_title": "{{ article.title|slugify }}",
    "word_count": "{{ article.content|word_count }}"
  }
}
```

### Numeric and Math Filters

**Mathematical operations and calculations:**

```javascript
// Numeric transformations
{
  "function": "create_variable",
  "name": "pricing_calculations",
  "value": {
    "base_price": "{{ product.price }}",
    "tax_amount": "{{ product.price * 0.08 }}",
    "discount_amount": "{{ product.price * user.discount_rate }}",
    "final_price": "{{ (product.price * 1.08) - (product.price * user.discount_rate) }}",
    "rounded_price": "{{ final_price|round(2) }}",
    "formatted_price": "${{ final_price|number_format(2) }}",
    "percentage_saved": "{{ (user.discount_rate * 100)|round(1) }}%"
  }
}
```

### Date and Time Filters

**Temporal data manipulation:**

```javascript
// Date and time transformations
{
  "function": "create_variable",
  "name": "temporal_data",
  "value": {
    "current_timestamp": "{{ now }}",
    "formatted_date": "{{ now|date('Y-m-d H:i:s') }}",
    "user_friendly_date": "{{ user.created_at|date('F j, Y') }}",
    "days_since_signup": "{{ (now - user.created_at) / 86400 }}",
    "is_recent_user": "{{ (now - user.created_at) < 604800 }}", // 7 days
    "subscription_expires": "{{ user.subscription_start|add_days(365) }}",
    "time_until_expiry": "{{ user.subscription_expires - now }}",
    "is_expired": "{{ user.subscription_expires < now }}"
  }
}
```

### Array and Object Filters

**Collection manipulation and transformation:**

```javascript
// Array and object transformations
[
  {
    "function": "query_all_records",
    "table": "products",
    "filter": {"category": "electronics"},
    "return_as": "products"
  },
  {
    "function": "create_variable",
    "name": "product_analysis",
    "value": {
      "total_products": "{{ products|length }}",
      "product_names": "{{ products|map(attribute='name') }}",
      "price_range": {
        "min": "{{ products|map(attribute='price')|min }}",
        "max": "{{ products|map(attribute='price')|max }}",
        "average": "{{ products|map(attribute='price')|average }}"
      },
      "in_stock_products": "{{ products|select(attribute='stock_quantity', operator='>', value=0) }}",
      "out_of_stock_count": "{{ products|select(attribute='stock_quantity', operator='==', value=0)|length }}",
      "premium_products": "{{ products|select(attribute='price', operator='>', value=100) }}",
      "sorted_by_price": "{{ products|sort(attribute='price') }}",
      "grouped_by_brand": "{{ products|group_by('brand') }}"
    }
  }
]
```

## 🔗 **No-Code Platform Integration**

### n8n Data Processing Workflows

**Advanced data transformation workflows:**

```javascript
// n8n workflow for complex data processing
{
  "nodes": [
    {
      "name": "Fetch Xano Data",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/analytics/raw-data",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}"
        },
        "qs": {
          "start_date": "{{ $now.minus({days: 30}).toISO() }}",
          "end_date": "{{ $now.toISO() }}"
        }
      }
    },
    {
      "name": "Transform User Data",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const rawData = $input.first().json;
          
          // Group users by signup date
          const usersByDate = {};
          rawData.users.forEach(user => {
            const signupDate = new Date(user.created_at).toISOString().split('T')[0];
            if (!usersByDate[signupDate]) {
              usersByDate[signupDate] = [];
            }
            usersByDate[signupDate].push(user);
          });
          
          // Calculate daily metrics
          const dailyMetrics = Object.keys(usersByDate).map(date => {
            const users = usersByDate[date];
            const totalRevenue = users.reduce((sum, user) => sum + (user.lifetime_value || 0), 0);
            
            return {
              date: date,
              new_users: users.length,
              total_revenue: totalRevenue,
              average_ltv: totalRevenue / users.length,
              premium_users: users.filter(u => u.subscription_tier === 'premium').length
            };
          });
          
          // Calculate growth metrics
          const sortedMetrics = dailyMetrics.sort((a, b) => new Date(a.date) - new Date(b.date));
          const growthData = sortedMetrics.map((metric, index) => {
            if (index === 0) return { ...metric, growth_rate: 0 };
            
            const previousMetric = sortedMetrics[index - 1];
            const growthRate = ((metric.new_users - previousMetric.new_users) / previousMetric.new_users) * 100;
            
            return {
              ...metric,
              growth_rate: Math.round(growthRate * 100) / 100
            };
          });
          
          return [{
            json: {
              daily_metrics: growthData,
              summary: {
                total_new_users: rawData.users.length,
                total_revenue: dailyMetrics.reduce((sum, m) => sum + m.total_revenue, 0),
                average_daily_signups: dailyMetrics.reduce((sum, m) => sum + m.new_users, 0) / dailyMetrics.length,
                period_start: sortedMetrics[0]?.date,
                period_end: sortedMetrics[sortedMetrics.length - 1]?.date
              }
            }
          }];
        `
      }
    },
    {
      "name": "Send to Analytics Dashboard",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/analytics/processed-data",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": "{{ $json }}"
      }
    },
    {
      "name": "Generate Report",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const data = $input.first().json;
          
          // Generate HTML report
          const reportHtml = \`
            <h2>Monthly Growth Report</h2>
            <p><strong>Period:</strong> \${data.summary.period_start} to \${data.summary.period_end}</p>
            <p><strong>Total New Users:</strong> \${data.summary.total_new_users}</p>
            <p><strong>Total Revenue:</strong> $\${data.summary.total_revenue.toFixed(2)}</p>
            <p><strong>Average Daily Signups:</strong> \${data.summary.average_daily_signups.toFixed(1)}</p>
            
            <h3>Daily Breakdown</h3>
            <table border="1">
              <tr>
                <th>Date</th>
                <th>New Users</th>
                <th>Revenue</th>
                <th>Growth Rate</th>
              </tr>
              \${data.daily_metrics.map(metric => \`
                <tr>
                  <td>\${metric.date}</td>
                  <td>\${metric.new_users}</td>
                  <td>$\${metric.total_revenue.toFixed(2)}</td>
                  <td>\${metric.growth_rate}%</td>
                </tr>
              \`).join('')}
            </table>
          \`;
          
          return [{ json: { report_html: reportHtml, data: data } }];
        `
      }
    }
  ]
}
```

### WeWeb Data Management

**Real-time data manipulation in WeWeb:**

```javascript
// WeWeb component for advanced data handling
class XanoDataManager {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.dataCache = new Map();
    this.transformationPipeline = [];
  }
  
  async fetchAndTransformData(endpoint, transformations = []) {
    try {
      // Check cache first
      const cacheKey = `${endpoint}_${JSON.stringify(transformations)}`;
      if (this.dataCache.has(cacheKey)) {
        const cached = this.dataCache.get(cacheKey);
        if (Date.now() - cached.timestamp < 300000) { // 5 minutes
          return cached.data;
        }
      }
      
      // Fetch data from Xano
      const response = await fetch(`${this.baseUrl}/api/${endpoint}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        }
      });
      
      let data = await response.json();
      
      // Apply transformations
      data = this.applyTransformations(data, transformations);
      
      // Cache result
      this.dataCache.set(cacheKey, {
        data: data,
        timestamp: Date.now()
      });
      
      // Update WeWeb variables
      wwLib.wwVariable.updateValue(`${endpoint}_data`, data);
      wwLib.wwVariable.updateValue(`${endpoint}_last_updated`, new Date().toISOString());
      
      return data;
      
    } catch (error) {
      console.error('Data fetch and transform failed:', error);
      wwLib.wwUtils.showErrorToast('Failed to load data');
      return null;
    }
  }
  
  applyTransformations(data, transformations) {
    return transformations.reduce((result, transform) => {
      switch (transform.type) {
        case 'filter':
          return result.filter(item => this.evaluateCondition(item, transform.condition));
          
        case 'map':
          return result.map(item => this.transformItem(item, transform.mapping));
          
        case 'sort':
          return [...result].sort((a, b) => {
            const aVal = this.getNestedValue(a, transform.field);
            const bVal = this.getNestedValue(b, transform.field);
            return transform.order === 'desc' ? bVal - aVal : aVal - bVal;
          });
          
        case 'group':
          return this.groupBy(result, transform.field);
          
        case 'aggregate':
          return this.aggregateData(result, transform.operations);
          
        case 'join':
          return this.joinData(result, transform.joinData, transform.joinField);
          
        default:
          return result;
      }
    }, data);
  }
  
  evaluateCondition(item, condition) {
    const value = this.getNestedValue(item, condition.field);
    
    switch (condition.operator) {
      case 'equals': return value === condition.value;
      case 'not_equals': return value !== condition.value;
      case 'greater_than': return value > condition.value;
      case 'less_than': return value < condition.value;
      case 'contains': return String(value).toLowerCase().includes(String(condition.value).toLowerCase());
      case 'in': return condition.value.includes(value);
      default: return true;
    }
  }
  
  transformItem(item, mapping) {
    const transformed = {};
    
    Object.keys(mapping).forEach(newKey => {
      const config = mapping[newKey];
      
      if (typeof config === 'string') {
        // Simple field mapping
        transformed[newKey] = this.getNestedValue(item, config);
      } else if (typeof config === 'object') {
        // Complex transformation
        if (config.source) {
          let value = this.getNestedValue(item, config.source);
          
          // Apply filters
          if (config.filters) {
            value = this.applyFilters(value, config.filters);
          }
          
          transformed[newKey] = value;
        } else if (config.computed) {
          // Computed field
          transformed[newKey] = this.computeValue(item, config.computed);
        }
      }
    });
    
    return { ...item, ...transformed };
  }
  
  applyFilters(value, filters) {
    return filters.reduce((result, filter) => {
      switch (filter.type) {
        case 'uppercase': return String(result).toUpperCase();
        case 'lowercase': return String(result).toLowerCase();
        case 'capitalize': return String(result).charAt(0).toUpperCase() + String(result).slice(1).toLowerCase();
        case 'truncate': return String(result).substring(0, filter.length) + (result.length > filter.length ? '...' : '');
        case 'round': return Math.round(Number(result) * Math.pow(10, filter.decimals || 0)) / Math.pow(10, filter.decimals || 0);
        case 'format_currency': return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(result);
        case 'format_date': return new Date(result).toLocaleDateString();
        default: return result;
      }
    }, value);
  }
  
  computeValue(item, computation) {
    switch (computation.type) {
      case 'concat':
        return computation.fields.map(field => this.getNestedValue(item, field)).join(computation.separator || ' ');
        
      case 'calculate':
        const values = computation.fields.map(field => Number(this.getNestedValue(item, field)) || 0);
        switch (computation.operation) {
          case 'sum': return values.reduce((a, b) => a + b, 0);
          case 'subtract': return values.reduce((a, b) => a - b);
          case 'multiply': return values.reduce((a, b) => a * b, 1);
          case 'divide': return values.reduce((a, b) => a / b);
          case 'average': return values.reduce((a, b) => a + b, 0) / values.length;
          default: return 0;
        }
        
      case 'conditional':
        const condition = this.evaluateCondition(item, computation.condition);
        return condition ? computation.true_value : computation.false_value;
        
      default:
        return null;
    }
  }
  
  groupBy(data, field) {
    const grouped = {};
    
    data.forEach(item => {
      const key = this.getNestedValue(item, field);
      if (!grouped[key]) {
        grouped[key] = [];
      }
      grouped[key].push(item);
    });
    
    return grouped;
  }
  
  aggregateData(data, operations) {
    const result = {};
    
    operations.forEach(op => {
      const values = data.map(item => Number(this.getNestedValue(item, op.field)) || 0);
      
      switch (op.type) {
        case 'sum':
          result[op.name] = values.reduce((a, b) => a + b, 0);
          break;
        case 'average':
          result[op.name] = values.reduce((a, b) => a + b, 0) / values.length;
          break;
        case 'min':
          result[op.name] = Math.min(...values);
          break;
        case 'max':
          result[op.name] = Math.max(...values);
          break;
        case 'count':
          result[op.name] = data.length;
          break;
      }
    });
    
    return result;
  }
  
  getNestedValue(obj, path) {
    return path.split('.').reduce((current, key) => current && current[key], obj);
  }
  
  async saveTransformedData(data, endpoint) {
    try {
      const response = await fetch(`${this.baseUrl}/api/${endpoint}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      
      if (response.ok) {
        wwLib.wwUtils.showSuccessToast('Data saved successfully');
        return await response.json();
      } else {
        throw new Error('Failed to save data');
      }
      
    } catch (error) {
      console.error('Save failed:', error);
      wwLib.wwUtils.showErrorToast('Failed to save data');
      return null;
    }
  }
}

// Initialize data manager
const dataManager = new XanoDataManager(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function loadAndTransformUsers() {
  const transformations = [
    {
      type: 'filter',
      condition: { field: 'status', operator: 'equals', value: 'active' }
    },
    {
      type: 'map',
      mapping: {
        full_name: {
          computed: {
            type: 'concat',
            fields: ['first_name', 'last_name'],
            separator: ' '
          }
        },
        formatted_signup_date: {
          source: 'created_at',
          filters: [{ type: 'format_date' }]
        },
        lifetime_value_formatted: {
          source: 'lifetime_value',
          filters: [{ type: 'format_currency' }]
        }
      }
    },
    {
      type: 'sort',
      field: 'created_at',
      order: 'desc'
    }
  ];
  
  const users = await dataManager.fetchAndTransformData('users', transformations);
  wwLib.wwVariable.updateValue('transformed_users', users);
}

async function generateUserAnalytics() {
  const users = wwLib.wwVariable.getValue('users_data') || [];
  
  const analytics = dataManager.applyTransformations(users, [
    {
      type: 'aggregate',
      operations: [
        { type: 'count', name: 'total_users' },
        { type: 'average', field: 'lifetime_value', name: 'avg_ltv' },
        { type: 'sum', field: 'lifetime_value', name: 'total_revenue' }
      ]
    }
  ]);
  
  wwLib.wwVariable.updateValue('user_analytics', analytics);
}
```

## ⚡ **Advanced Data Patterns**

### Data Validation and Sanitization

**Comprehensive data cleaning workflow:**

```javascript
// Data validation and sanitization function stack
[
  {
    "function": "create_variable",
    "name": "raw_input",
    "value": "{{ request.body }}"
  },
  {
    "function": "create_variable",
    "name": "validation_errors",
    "value": []
  },
  {
    "function": "create_variable",
    "name": "sanitized_data",
    "value": {}
  },
  
  // Email validation and sanitization
  {
    "function": "conditional",
    "condition": "{{ raw_input.email }}",
    "true_branch": [
      {
        "function": "conditional",
        "condition": "{{ raw_input.email|regex_matches('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$') }}",
        "true_branch": [
          {
            "function": "update_variable",
            "name": "sanitized_data",
            "operation": "merge",
            "value": {
              "email": "{{ raw_input.email|lower|trim }}"
            }
          }
        ],
        "false_branch": [
          {
            "function": "update_variable",
            "name": "validation_errors",
            "operation": "append",
            "value": "Invalid email format"
          }
        ]
      }
    ]
  },
  
  // Text field sanitization
  {
    "function": "conditional",
    "condition": "{{ raw_input.first_name }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "sanitized_data",
        "operation": "merge",
        "value": {
          "first_name": "{{ raw_input.first_name|strip_tags|trim|capitalize }}"
        }
      }
    ]
  },
  
  // Numeric validation
  {
    "function": "conditional",
    "condition": "{{ raw_input.age }}",
    "true_branch": [
      {
        "function": "conditional",
        "condition": "{{ raw_input.age|is_numeric && raw_input.age >= 13 && raw_input.age <= 120 }}",
        "true_branch": [
          {
            "function": "update_variable",
            "name": "sanitized_data",
            "operation": "merge",
            "value": {
              "age": "{{ raw_input.age|int }}"
            }
          }
        ],
        "false_branch": [
          {
            "function": "update_variable",
            "name": "validation_errors",
            "operation": "append",
            "value": "Age must be between 13 and 120"
          }
        ]
      }
    ]
  },
  
  // Return validation results
  {
    "function": "conditional",
    "condition": "{{ validation_errors|length > 0 }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {
          "error": "Validation failed",
          "errors": "{{ validation_errors }}",
          "received_data": "{{ raw_input }}"
        }
      }
    ],
    "false_branch": [
      {
        "function": "return_response",
        "body": {
          "success": true,
          "sanitized_data": "{{ sanitized_data }}"
        }
      }
    ]
  }
]
```

### Complex Data Aggregation

**Multi-table data aggregation and analysis:**

```javascript
// Advanced data aggregation workflow
[
  {
    "function": "query_all_records",
    "table": "orders",
    "filter": {
      "created_at": {"$gte": "{{ now - 2592000 }}"}, // Last 30 days
      "status": "completed"
    },
    "join": [
      {
        "table": "users",
        "on": "orders.user_id = users.id"
      },
      {
        "table": "order_items",
        "on": "orders.id = order_items.order_id"
      },
      {
        "table": "products",
        "on": "order_items.product_id = products.id"
      }
    ],
    "return_as": "order_data"
  },
  
  // Calculate user metrics
  {
    "function": "create_variable",
    "name": "user_metrics",
    "value": "{{ order_data|group_by('user_id')|transform_groups }}"
  },
  
  // Calculate product metrics
  {
    "function": "create_variable",
    "name": "product_metrics",
    "value": {
      "top_products": "{{ order_data|group_by('product_id')|sort_by_revenue|limit(10) }}",
      "category_performance": "{{ order_data|group_by('product_category')|calculate_totals }}",
      "average_order_value": "{{ order_data|map(attribute='total_amount')|average }}",
      "total_revenue": "{{ order_data|map(attribute='total_amount')|sum }}"
    }
  },
  
  // Time-based analysis
  {
    "function": "create_variable",
    "name": "time_analysis",
    "value": {
      "daily_sales": "{{ order_data|group_by('created_at|date(\"Y-m-d\")')|daily_totals }}",
      "weekly_trends": "{{ order_data|group_by('created_at|date(\"Y-W\")')|weekly_analysis }}",
      "peak_hours": "{{ order_data|group_by('created_at|date(\"H\")')|hourly_distribution }}"
    }
  },
  
  // Compile comprehensive report
  {
    "function": "create_variable",
    "name": "analytics_report",
    "value": {
      "period": "last_30_days",
      "generated_at": "{{ now }}",
      "summary": {
        "total_orders": "{{ order_data|length }}",
        "total_revenue": "{{ product_metrics.total_revenue }}",
        "average_order_value": "{{ product_metrics.average_order_value }}",
        "unique_customers": "{{ order_data|map(attribute='user_id')|unique|length }}"
      },
      "user_insights": "{{ user_metrics }}",
      "product_insights": "{{ product_metrics }}",
      "temporal_insights": "{{ time_analysis }}"
    }
  }
]
```

## 💡 **Pro Tips**

- **Variable Naming**: Use descriptive names that clearly indicate the data content and type
- **Data Validation**: Always validate and sanitize input data before processing
- **Performance**: Cache frequently accessed data and avoid repeated database queries
- **Memory Management**: Clean up large variables when no longer needed
- **Error Handling**: Implement fallbacks for missing or invalid data
- **Documentation**: Comment complex data transformations for maintainability

## 🔧 **Troubleshooting**

### Common Data Handling Issues

**Problem**: Variables not updating correctly between functions  
**Solution**: Check variable names for typos and ensure proper `return_as` assignments

**Problem**: Filters not working as expected  
**Solution**: Verify data types and filter syntax; use debug outputs to inspect intermediate values

**Problem**: Performance issues with large datasets  
**Solution**: Implement pagination, use database joins instead of multiple queries, cache results

**Problem**: Data transformation errors with null values  
**Solution**: Add null checks and default values in expressions and filters

---

**Next Steps**: Ready to master data management? Explore [Functions](functions.md) for comprehensive function usage or check [Custom Functions](custom-functions.md) for building reusable data processing logic