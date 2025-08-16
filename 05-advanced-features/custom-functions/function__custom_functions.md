---
title: Custom Functions Function Reference
description: Quick reference for using custom functions in Xano function stacks, including function calls, input mapping, and return handling
category: custom-functions
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - custom-functions.md
  - building-with-visual-development.md
  - async-functions.md
subcategory: 05-advanced-features/custom-functions
tags:
  - custom-functions
  - function-reference
  - reusable-logic
  - function-calls
  - no-code
---

## 📋 **Quick Summary**

The Custom Functions function allows you to call reusable custom functions within your function stacks. Custom functions encapsulate business logic that can be used across multiple endpoints, background tasks, and triggers while maintaining centralized code in one location.

## What You'll Learn

- How to call custom functions in function stacks
- Input mapping and parameter passing
- Return value handling and variable assignment
- Synchronous vs asynchronous execution modes
- Best practices for custom function integration

# Custom Functions Function Reference

## Overview

The **Custom Functions** function enables you to execute your reusable custom functions within any function stack. This promotes code reusability, maintainability, and consistency across your application by centralizing business logic in modular components.

### Key Benefits

**Code Reusability:**
- Write once, use everywhere
- Centralized maintenance
- Consistent business logic
- Reduced code duplication

**Modularity:**
- Encapsulated functionality
- Clear input/output interfaces
- Easy testing and debugging
- Improved organization

## 🚀 **Basic Function Call**

### Simple Custom Function Usage

**Calling a User Validation Function:**
```javascript
{
  "function": "custom_function",
  "name": "validate_user_data",
  "inputs": {
    "email": "{{ request.body.email }}",
    "password": "{{ request.body.password }}",
    "validation_level": "strict"
  },
  "return_as": "validation_result"
}
```

### Using Function Results

**Processing Validation Response:**
```javascript
[
  {
    "function": "custom_function",
    "name": "validate_user_data",
    "inputs": {
      "email": "{{ request.body.email }}",
      "password": "{{ request.body.password }}"
    },
    "return_as": "validation"
  },
  {
    "function": "conditional",
    "condition": "{{ validation.is_valid }}",
    "true_branch": [
      {
        "function": "add_record",
        "table": "users",
        "data": {
          "email": "{{ validation.cleaned_email }}",
          "password": "{{ validation.hashed_password }}"
        }
      }
    ],
    "false_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {
          "error": "Validation failed",
          "details": "{{ validation.errors }}"
        }
      }
    ]
  }
]
```

## 🛠️ **Common Usage Patterns**

### Sequential Function Calls

**Multi-Step Data Processing:**
```javascript
[
  {
    "function": "custom_function",
    "name": "fetch_user_data",
    "inputs": {
      "user_id": "{{ auth.user.id }}"
    },
    "return_as": "user_data"
  },
  {
    "function": "custom_function",
    "name": "calculate_user_metrics",
    "inputs": {
      "user": "{{ user_data }}",
      "date_range": "last_30_days"
    },
    "return_as": "metrics"
  },
  {
    "function": "custom_function",
    "name": "generate_user_report",
    "inputs": {
      "user": "{{ user_data }}",
      "metrics": "{{ metrics }}",
      "format": "pdf"
    },
    "return_as": "report"
  }
]
```

### Parallel Function Execution

**Independent Operations:**
```javascript
[
  {
    "function": "custom_function",
    "name": "send_welcome_email",
    "inputs": {
      "user_id": "{{ new_user.id }}",
      "email": "{{ new_user.email }}"
    },
    "execution_mode": "async",
    "return_as": "email_job_id"
  },
  {
    "function": "custom_function",
    "name": "create_user_profile",
    "inputs": {
      "user_id": "{{ new_user.id }}",
      "profile_data": "{{ request.body.profile }}"
    },
    "return_as": "profile"
  },
  {
    "function": "custom_function",
    "name": "setup_user_preferences",
    "inputs": {
      "user_id": "{{ new_user.id }}",
      "defaults": true
    },
    "execution_mode": "async"
  }
]
```

### Conditional Function Calls

**Dynamic Logic Execution:**
```javascript
[
  {
    "function": "conditional",
    "condition": "{{ request.body.payment_method == 'credit_card' }}",
    "true_branch": [
      {
        "function": "custom_function",
        "name": "process_credit_card_payment",
        "inputs": {
          "amount": "{{ order_total }}",
          "card_data": "{{ request.body.card_info }}"
        },
        "return_as": "payment_result"
      }
    ],
    "false_branch": [
      {
        "function": "custom_function",
        "name": "process_paypal_payment",
        "inputs": {
          "amount": "{{ order_total }}",
          "paypal_token": "{{ request.body.paypal_token }}"
        },
        "return_as": "payment_result"
      }
    ]
  }
]
```

### Loop-Based Function Calls

**Batch Processing:**
```javascript
[
  {
    "function": "loop",
    "array": "{{ order_items }}",
    "operations": [
      {
        "function": "custom_function",
        "name": "update_inventory",
        "inputs": {
          "product_id": "{{ item.product_id }}",
          "quantity_sold": "{{ item.quantity }}",
          "warehouse_location": "{{ item.warehouse }}"
        },
        "return_as": "inventory_update"
      },
      {
        "function": "custom_function",
        "name": "log_inventory_change",
        "inputs": {
          "product_id": "{{ item.product_id }}",
          "change_type": "sale",
          "quantity": "{{ item.quantity }}",
          "order_id": "{{ order.id }}"
        },
        "execution_mode": "async"
      }
    ]
  }
]
```

## ⚡ **Execution Modes**

### Synchronous Execution (Default)

**Blocking Execution:**
```javascript
{
  "function": "custom_function",
  "name": "validate_and_process_data",
  "inputs": {
    "data": "{{ input_data }}"
  },
  "execution_mode": "sync",  // Optional - this is default
  "return_as": "processed_data"
}
// Next function waits for completion
```

### Asynchronous Execution

**Non-Blocking Execution:**
```javascript
{
  "function": "custom_function",
  "name": "send_notification_email",
  "inputs": {
    "user_id": "{{ user.id }}",
    "template": "order_confirmation"
  },
  "execution_mode": "async",
  "return_as": "email_execution_id"
}
// Function stack continues immediately
```

## 🔄 **Input Mapping Patterns**

### Static Input Values

**Hard-coded Parameters:**
```javascript
{
  "function": "custom_function",
  "name": "generate_api_key",
  "inputs": {
    "key_type": "access_token",
    "expires_in": 3600,
    "permissions": ["read", "write"]
  }
}
```

### Dynamic Input Mapping

**Request and Context Data:**
```javascript
{
  "function": "custom_function",
  "name": "create_audit_entry",
  "inputs": {
    "user_id": "{{ auth.user.id }}",
    "action": "{{ request.method }} {{ request.path }}",
    "ip_address": "{{ request.ip }}",
    "timestamp": "{{ now }}",
    "request_data": "{{ request.body }}",
    "user_agent": "{{ request.headers['user-agent'] }}"
  }
}
```

### Computed Input Values

**Derived Parameters:**
```javascript
{
  "function": "custom_function",
  "name": "calculate_shipping_cost",
  "inputs": {
    "total_weight": "{{ cart_items|sum(attribute='weight') }}",
    "destination_zip": "{{ shipping_address.zip_code }}",
    "shipping_method": "{{ request.body.shipping_option }}",
    "order_value": "{{ cart_items|sum(attribute='price') }}",
    "is_expedited": "{{ request.body.shipping_option == 'express' }}"
  }
}
```

## 💡 **Best Practices**

### Input Validation

**Validate Before Function Call:**
```javascript
[
  {
    "function": "conditional",
    "condition": "{{ !request.body.email || !request.body.password }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {"error": "Email and password required"}
      }
    ]
  },
  {
    "function": "custom_function",
    "name": "authenticate_user",
    "inputs": {
      "email": "{{ request.body.email }}",
      "password": "{{ request.body.password }}"
    },
    "return_as": "auth_result"
  }
]
```

### Error Handling

**Graceful Function Failure Management:**
```javascript
[
  {
    "function": "try_catch",
    "try_block": [
      {
        "function": "custom_function",
        "name": "external_api_integration",
        "inputs": {
          "api_endpoint": "{{ third_party_url }}",
          "data": "{{ request.body }}"
        },
        "return_as": "api_response"
      }
    ],
    "catch_block": [
      {
        "function": "create_variable",
        "name": "api_response",
        "value": {
          "success": false,
          "error": "External service unavailable",
          "fallback_used": true
        }
      }
    ]
  }
]
```

### Performance Optimization

**Efficient Function Usage:**
```javascript
// Cache results to avoid repeated calls
[
  {
    "function": "cache_get",
    "key": "user_permissions_{{ auth.user.id }}",
    "return_as": "cached_permissions"
  },
  {
    "function": "conditional",
    "condition": "{{ !cached_permissions }}",
    "true_branch": [
      {
        "function": "custom_function",
        "name": "calculate_user_permissions",
        "inputs": {
          "user_id": "{{ auth.user.id }}"
        },
        "return_as": "permissions"
      },
      {
        "function": "cache_set",
        "key": "user_permissions_{{ auth.user.id }}",
        "value": "{{ permissions }}",
        "ttl": 300
      }
    ],
    "false_branch": [
      {
        "function": "create_variable",
        "name": "permissions",
        "value": "{{ cached_permissions }}"
      }
    ]
  }
]
```

## 🔧 **Common Issues**

**Problem**: Custom function not found  
**Solution**: Verify function name spelling and ensure function is published

**Problem**: Input mapping errors  
**Solution**: Check input parameter names match function definition exactly

**Problem**: Async function results not available  
**Solution**: Use `async_function_await` to retrieve results from async executions

**Problem**: Function timeout errors  
**Solution**: Optimize function logic or increase timeout settings

---

**Next Steps**: For comprehensive custom function creation and management, see [Custom Functions](custom-functions.md). For async patterns, check [Async Functions](async-functions.md).