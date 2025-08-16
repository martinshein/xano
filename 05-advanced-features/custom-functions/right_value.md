---
title: Right Value - Comparison Operations and Value Evaluation
description: Complete guide to comparison operators and value evaluation in Xano including equality checks, string matching, array operations, and integration patterns for no-code platforms
category: custom-functions
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - working-with-data.md
  - types_of_middleware.md
  - building-with-visual-development.md
subcategory: 05-advanced-features/custom-functions
tags:
  - comparison-operators
  - conditionals
  - value-evaluation
  - data-filtering
  - expressions
  - no-code
---

## 📋 **Quick Summary**

Right Value represents the comparison target in conditional operations and filters throughout Xano. Understanding comparison operators and value evaluation is essential for building dynamic logic, database queries, and conditional workflows in your no-code applications with n8n, WeWeb, and other platforms.

## What You'll Learn

- Understanding Right Value concept in comparison operations
- Complete reference of all comparison operators available
- Best practices for value evaluation and type matching
- Advanced filtering techniques and pattern matching
- Integration patterns for dynamic conditional logic
- Performance optimization for complex comparisons

# Right Value - Comparison Operations

## Overview

**Right Value** is the target value used in comparison operations throughout Xano's function stacks, database queries, and conditional logic. It represents the "what you're comparing against" in any conditional statement, filter, or validation operation.

### Left Value vs Right Value

**Left Value (Source):**
- The original value being evaluated
- Can be variables, database fields, or expressions
- The subject of the comparison

**Right Value (Target):**
- The value being compared against
- Can be hardcoded values, variables, or dynamic expressions
- The comparison target or criteria

## 🔍 **Equality Operators**

### Equals (==) - Basic Equality

**Loose equality comparison that performs type coercion:**

```javascript
// Basic equality examples
{
  "function": "conditional",
  "condition": "{{ user.status == 'active' }}", // String comparison
  "true_branch": [
    {
      "function": "query_all_records",
      "table": "user_sessions",
      "filter": {
        "user_id": "{{ user.id }}"
      }
    }
  ]
}

// Numeric equality with type coercion
{
  "function": "conditional",
  "condition": "{{ order.total == 100 }}", // 100 (number) == "100" (string) = true
  "true_branch": [
    {
      "function": "apply_discount",
      "discount_type": "free_shipping"
    }
  ]
}
```

### Not Equals (!=) - Basic Inequality

**Checks if values are not equal with type coercion:**

```javascript
// Exclude inactive users
{
  "function": "query_all_records",
  "table": "users",
  "filter": {
    "status": {"$ne": "inactive"}, // Not equals inactive
    "last_login": {"$ne": null}    // Not null
  },
  "return_as": "active_users"
}

// Conditional processing for non-zero values
{
  "function": "conditional",
  "condition": "{{ cart.item_count != 0 }}",
  "true_branch": [
    {
      "function": "calculate_shipping_cost",
      "items": "{{ cart.items }}"
    }
  ]
}
```

### Strict Equality (===) - Type-Safe Comparison

**Exact value and type matching without coercion:**

```javascript
// Type-safe comparison example
{
  "function": "conditional",
  "condition": "{{ user.age === 21 }}", // Number 21, not string "21"
  "true_branch": [
    {
      "function": "send_birthday_offer",
      "user_id": "{{ user.id }}"
    }
  ]
}

// Boolean type checking
{
  "function": "conditional",
  "condition": "{{ subscription.auto_renew === true }}", // Boolean true, not "true"
  "true_branch": [
    {
      "function": "schedule_renewal",
      "subscription_id": "{{ subscription.id }}"
    }
  ]
}
```

### Strict Inequality (!==) - Type-Safe Inequality

**Values or types do not match:**

```javascript
// Strict type checking for data validation
{
  "function": "conditional",
  "condition": "{{ request.body.user_id !== null }}",
  "true_branch": [
    {
      "function": "validate_user_permissions",
      "user_id": "{{ request.body.user_id }}"
    }
  ],
  "false_branch": [
    {
      "function": "return_response",
      "status": 400,
      "body": {"error": "User ID is required"}
    }
  ]
}
```

## 🔢 **Numeric Comparison Operators**

### Greater Than (>) and Greater Than or Equal (>=)

**Numeric and date comparisons:**

```javascript
// Age-based filtering
{
  "function": "query_all_records",
  "table": "users",
  "filter": {
    "age": {"$gt": 18}, // Greater than 18
    "account_balance": {"$gte": 100.00} // Greater than or equal to $100
  },
  "return_as": "eligible_users"
}

// Date-based queries
{
  "function": "query_all_records",
  "table": "orders",
  "filter": {
    "created_at": {"$gte": "{{ now - 86400 }}"}, // Last 24 hours
    "total_amount": {"$gt": 50}
  },
  "return_as": "recent_large_orders"
}
```

### Less Than (<) and Less Than or Equal (<=)

**Range and limit comparisons:**

```javascript
// Inventory management
{
  "function": "query_all_records",
  "table": "products",
  "filter": {
    "stock_quantity": {"$lt": 10}, // Less than 10 items
    "price": {"$lte": 99.99} // $99.99 or less
  },
  "return_as": "low_stock_affordable_items"
}

// User segmentation by activity
{
  "function": "conditional",
  "condition": "{{ user.login_count < 5 }}",
  "true_branch": [
    {
      "function": "send_onboarding_email",
      "user_id": "{{ user.id }}",
      "email_type": "new_user_guide"
    }
  ]
}
```

## 📝 **Text Comparison Operators**

### LIKE - Case-Insensitive Text Matching

**Flexible text comparison without case sensitivity:**

```javascript
// Case-insensitive name search
{
  "function": "query_all_records",
  "table": "users",
  "filter": {
    "first_name": {"$like": "john"} // Matches "John", "JOHN", "john"
  },
  "return_as": "users_named_john"
}

// Product search
{
  "function": "query_all_records",
  "table": "products",
  "filter": {
    "name": {"$like": "{{ request.body.search_term }}"}
  },
  "return_as": "matching_products"
}
```

### NOT LIKE - Case-Insensitive Exclusion

**Exclude text patterns:**

```javascript
// Exclude test accounts
{
  "function": "query_all_records",
  "table": "users",
  "filter": {
    "email": {"$not_like": "test%"}, // Exclude emails starting with "test"
    "username": {"$not_like": "%demo%"} // Exclude usernames containing "demo"
  },
  "return_as": "real_users"
}
```

### INCLUDES - Partial Text Matching

**Find substring matches within text:**

```javascript
// Comment moderation
{
  "function": "query_all_records",
  "table": "comments",
  "filter": {
    "content": {"$includes": "spam"} // Find comments containing "spam"
  },
  "return_as": "potential_spam_comments"
}

// Address filtering
{
  "function": "conditional",
  "condition": "{{ shipping_address.state|includes('CA') }}",
  "true_branch": [
    {
      "function": "apply_california_tax",
      "order_id": "{{ order.id }}"
    }
  ]
}
```

### DOES NOT INCLUDE - Exclusion by Substring

**Exclude records containing specific text:**

```javascript
// Filter out promotional emails
{
  "function": "query_all_records",
  "table": "emails",
  "filter": {
    "subject": {"$not_includes": "promo"},
    "body": {"$not_includes": "unsubscribe"}
  },
  "return_as": "non_promotional_emails"
}
```

## 🔗 **No-Code Platform Integration**

### n8n Dynamic Filtering Workflows

**Advanced filtering with dynamic right values:**

```javascript
// n8n workflow for dynamic user segmentation
{
  "nodes": [
    {
      "name": "Get Filter Criteria",
      "type": "Code",
      "parameters": {
        "jsCode": `
          // Dynamic filter criteria based on current date
          const now = new Date();
          const thirtyDaysAgo = new Date(now.getTime() - (30 * 24 * 60 * 60 * 1000));
          const oneYearAgo = new Date(now.getTime() - (365 * 24 * 60 * 60 * 1000));
          
          // Build dynamic filters
          const filters = {
            recent_users: {
              created_at: { '$gte': thirtyDaysAgo.toISOString() },
              status: { '$eq': 'active' }
            },
            loyal_customers: {
              created_at: { '$lte': oneYearAgo.toISOString() },
              total_orders: { '$gte': 10 },
              lifetime_value: { '$gte': 1000 }
            },
            at_risk_users: {
              last_login: { '$lte': thirtyDaysAgo.toISOString() },
              status: { '$ne': 'churned' }
            }
          };
          
          return [{ json: { filters: filters, timestamp: now.toISOString() } }];
        `
      }
    },
    {
      "name": "Query Recent Users",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/users",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}"
        },
        "qs": {
          "filter": "{{ JSON.stringify($json.filters.recent_users) }}"
        }
      }
    },
    {
      "name": "Query Loyal Customers",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/users",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}"
        },
        "qs": {
          "filter": "{{ JSON.stringify($json.filters.loyal_customers) }}"
        }
      }
    },
    {
      "name": "Process User Segments",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const recentUsers = $('Query Recent Users').first().json;
          const loyalCustomers = $('Query Loyal Customers').first().json;
          
          // Create segment analysis
          const analysis = {
            recent_users_count: recentUsers.length,
            loyal_customers_count: loyalCustomers.length,
            growth_rate: ((recentUsers.length / loyalCustomers.length) * 100).toFixed(2),
            segments: {
              recent: recentUsers.map(user => ({
                id: user.id,
                email: user.email,
                segment: 'recent',
                days_since_signup: Math.floor((new Date() - new Date(user.created_at)) / (24 * 60 * 60 * 1000))
              })),
              loyal: loyalCustomers.map(user => ({
                id: user.id,
                email: user.email,
                segment: 'loyal',
                lifetime_value: user.lifetime_value
              }))
            }
          };
          
          return [{ json: analysis }];
        `
      }
    }
  ]
}
```

### WeWeb Conditional Rendering

**Dynamic UI based on comparison operations:**

```javascript
// WeWeb component for conditional content display
class XanoConditionalRenderer {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async evaluateDisplayConditions(userId, contentType) {
    try {
      const response = await fetch(`${this.baseUrl}/api/evaluate-conditions`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          user_id: userId,
          content_type: contentType,
          evaluation_rules: [
            {
              condition: 'user.subscription_tier',
              operator: 'IN',
              right_value: ['premium', 'enterprise']
            },
            {
              condition: 'user.account_status',
              operator: '==',
              right_value: 'active'
            },
            {
              condition: 'user.last_login',
              operator: '>=',
              right_value: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString()
            }
          ]
        })
      });
      
      const evaluation = await response.json();
      
      // Update WeWeb conditional variables
      wwLib.wwVariable.updateValue('show_premium_content', evaluation.show_premium);
      wwLib.wwVariable.updateValue('show_onboarding', evaluation.show_onboarding);
      wwLib.wwVariable.updateValue('show_reactivation', evaluation.show_reactivation);
      
      return evaluation;
    } catch (error) {
      console.error('Condition evaluation failed:', error);
      return { show_premium: false, show_onboarding: false, show_reactivation: false };
    }
  }
  
  async buildDynamicQuery(filters) {
    // Build complex queries with multiple right values
    const queryConditions = {};
    
    // Process each filter condition
    Object.keys(filters).forEach(field => {
      const filter = filters[field];
      
      switch (filter.operator) {
        case 'BETWEEN':
          queryConditions[field] = {
            '$gte': filter.right_value.min,
            '$lte': filter.right_value.max
          };
          break;
          
        case 'IN':
          queryConditions[field] = {
            '$in': filter.right_value
          };
          break;
          
        case 'INCLUDES':
          queryConditions[field] = {
            '$includes': filter.right_value
          };
          break;
          
        case 'REGEX_MATCHES':
          queryConditions[field] = {
            '$regex': filter.right_value,
            '$options': 'i'
          };
          break;
          
        default:
          queryConditions[field] = {
            [`$${filter.operator.toLowerCase()}`]: filter.right_value
          };
      }
    });
    
    const response = await fetch(`${this.baseUrl}/api/query-dynamic`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.authToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        table: filters.table,
        conditions: queryConditions,
        limit: filters.limit || 100
      })
    });
    
    return await response.json();
  }
}

// Initialize conditional renderer
const conditionalRenderer = new XanoConditionalRenderer(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function updateContentVisibility() {
  const userId = wwLib.wwVariable.getValue('current_user_id');
  await conditionalRenderer.evaluateDisplayConditions(userId, 'dashboard');
}

async function performAdvancedSearch() {
  const searchFilters = {
    table: 'products',
    name: {
      operator: 'INCLUDES',
      right_value: wwLib.wwVariable.getValue('search_term')
    },
    price: {
      operator: 'BETWEEN',
      right_value: {
        min: wwLib.wwVariable.getValue('min_price'),
        max: wwLib.wwVariable.getValue('max_price')
      }
    },
    category: {
      operator: 'IN',
      right_value: wwLib.wwVariable.getValue('selected_categories')
    },
    limit: 50
  };
  
  const results = await conditionalRenderer.buildDynamicQuery(searchFilters);
  wwLib.wwVariable.updateValue('search_results', results);
}
```

## 🔍 **Array Comparison Operators**

### IN - Value in Array

**Check if a single value exists in a list:**

```javascript
// User role checking
{
  "function": "conditional",
  "condition": "{{ user.role|in(['admin', 'moderator', 'manager']) }}",
  "true_branch": [
    {
      "function": "grant_admin_access",
      "user_id": "{{ user.id }}"
    }
  ]
}

// Status filtering
{
  "function": "query_all_records",
  "table": "orders",
  "filter": {
    "status": {"$in": ["confirmed", "processing", "shipped"]}
  },
  "return_as": "active_orders"
}
```

### NOT IN - Value not in Array

**Exclude values from a list:**

```javascript
// Exclude specific user types
{
  "function": "query_all_records",
  "table": "users",
  "filter": {
    "account_type": {"$nin": ["test", "demo", "suspended"]}
  },
  "return_as": "production_users"
}
```

### OVERLAPS - Array Intersection

**Check if two arrays share any common values:**

```javascript
// Permission overlap checking
{
  "function": "conditional",
  "condition": "{{ user.permissions|overlaps(required_permissions) }}",
  "true_branch": [
    {
      "function": "allow_access",
      "resource": "{{ request.resource }}"
    }
  ]
}
```

### CONTAINS - Exact Schema Match

**JSON and array structure matching:**

```javascript
// Complex object validation
{
  "function": "conditional",
  "condition": "{{ user.preferences|contains({'notifications': {'email': true}}) }}",
  "true_branch": [
    {
      "function": "send_email_notification",
      "user_id": "{{ user.id }}"
    }
  ]
}
```

## 🎯 **Regular Expression Operators**

### REGEX MATCHES - Pattern Matching

**Advanced text pattern validation:**

```javascript
// Email validation
{
  "function": "conditional",
  "condition": "{{ user.email|regex_matches('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$') }}",
  "true_branch": [
    {
      "function": "validate_email_format",
      "email": "{{ user.email }}"
    }
  ]
}

// Phone number validation
{
  "function": "conditional",
  "condition": "{{ customer.phone|regex_matches('^\\+?[1-9]\\d{1,14}$') }}",
  "true_branch": [
    {
      "function": "send_sms_verification",
      "phone": "{{ customer.phone }}"
    }
  ]
}
```

### REGEX DOES NOT MATCH - Pattern Exclusion

**Exclude patterns from processing:**

```javascript
// Filter out invalid formats
{
  "function": "query_all_records",
  "table": "user_submissions",
  "filter": {
    "content": {"$not_regex": "^\\s*$"} // Exclude empty or whitespace-only content
  },
  "return_as": "valid_submissions"
}
```

## ⚡ **Advanced Right Value Patterns**

### Dynamic Right Values with Expressions

**Using variables and calculations as right values:**

```javascript
// Dynamic pricing thresholds
{
  "function": "conditional",
  "condition": "{{ order.total >= (user.tier_discount_threshold * 1.2) }}",
  "true_branch": [
    {
      "function": "apply_tier_discount",
      "order_id": "{{ order.id }}",
      "discount_rate": "{{ user.tier_discount_rate }}"
    }
  ]
}

// Time-based comparisons
{
  "function": "query_all_records",
  "table": "events",
  "filter": {
    "start_time": {
      "$gte": "{{ now }}",
      "$lte": "{{ now + (24 * 3600) }}" // Next 24 hours
    }
  },
  "return_as": "upcoming_events"
}
```

### Conditional Right Values

**Different right values based on conditions:**

```javascript
// Conditional validation logic
[
  {
    "function": "create_variable",
    "name": "validation_threshold",
    "value": "{{ user.account_type == 'premium' ? 1000 : 100 }}"
  },
  {
    "function": "conditional",
    "condition": "{{ transaction.amount > validation_threshold }}",
    "true_branch": [
      {
        "function": "require_additional_verification",
        "transaction_id": "{{ transaction.id }}"
      }
    ]
  }
]
```

### Nested Right Value Evaluations

**Complex nested comparison logic:**

```javascript
// Multi-level conditional processing
{
  "function": "conditional",
  "condition": "{{ user.subscription.tier == 'enterprise' && user.usage.api_calls > (user.subscription.limits.api_calls * 0.8) }}",
  "true_branch": [
    {
      "function": "send_usage_warning",
      "user_id": "{{ user.id }}",
      "usage_percentage": "{{ (user.usage.api_calls / user.subscription.limits.api_calls) * 100 }}"
    }
  ]
}
```

## 💡 **Pro Tips**

- **Type Awareness**: Use strict equality (===) when type matters to avoid unexpected coercion
- **Performance**: Index database fields that are frequently used in comparisons
- **Case Sensitivity**: Use LIKE for case-insensitive text comparisons
- **Null Handling**: Always consider null values in your comparison logic
- **Array Operations**: Use IN for single-value-to-array comparisons, OVERLAPS for array-to-array
- **Regex Efficiency**: Use regex sparingly for performance-critical operations

## 🔧 **Troubleshooting**

### Common Right Value Issues

**Problem**: Comparison not working as expected with numbers  
**Solution**: Check if values are strings vs numbers; use strict equality (===) for type-safe comparisons

**Problem**: Text comparisons failing due to case sensitivity  
**Solution**: Use LIKE operator for case-insensitive comparisons or convert values to lowercase

**Problem**: Array IN operations not matching  
**Solution**: Ensure the right value is an array and left value is a single item, not vice versa

**Problem**: Date comparisons producing unexpected results  
**Solution**: Ensure dates are in consistent formats (ISO strings or timestamps)

---

**Next Steps**: Ready to build complex conditional logic? Explore [Working with Data](working-with-data.md) for advanced data manipulation or check [Types of Middleware](types_of_middleware.md) for processing patterns