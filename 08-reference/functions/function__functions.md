---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
- Visual Builder
- Function Stack
- Business Logic
title: 'Function Stack & Visual Builder'
---

# Function Stack & Visual Builder

## 📋 **Quick Summary**
Xano's Function Stack is the visual workflow builder that powers all business logic in your backend. Create complex data processing, API endpoints, and automation workflows using drag-and-drop functions without writing code. Perfect for building scalable applications with n8n, WeWeb, and other no-code platforms.

## 🎯 **Core Concepts**

### Function Stack Architecture
Function stacks are visual workflows that define your business logic through connected function blocks. Each function performs a specific operation and passes data to the next function in the sequence.

### Visual Builder Components
- **Function Palette**: Categorized library of available functions
- **Canvas**: Visual workspace for building workflows
- **Data Flow**: Automatic connection between function inputs/outputs
- **Testing Interface**: Built-in testing and debugging tools
- **Variable Inspector**: Real-time data monitoring

## 🏗️ **Function Categories**

### Database Functions
```javascript
// Database Operations Available in Function Stack
{
  "crud_operations": {
    "get_record": "Retrieve single database record",
    "query_all_records": "Fetch multiple records with filtering",
    "add_record": "Create new database entry",
    "edit_record": "Update existing record",
    "delete_record": "Remove record from database",
    "bulk_operations": "Mass data operations"
  },
  "advanced_database": {
    "database_transaction": "ACID-compliant multi-table operations",
    "external_database_query": "Connect to external databases",
    "direct_database_query": "Raw SQL execution",
    "get_database_schema": "Retrieve table structure information"
  }
}
```

### Data Manipulation Functions
```javascript
// Data Processing and Logic Functions
{
  "variables": {
    "create_variable": "Initialize data containers",
    "update_variable": "Modify variable values"
  },
  "flow_control": {
    "conditional": "If/else logic branching",
    "switch": "Multi-condition routing",
    "loops": "Iterate over arrays and collections"
  },
  "data_processing": {
    "math": "Arithmetic and calculations",
    "arrays": "List manipulation and processing",
    "objects": "JSON object transformation",
    "text": "String processing and formatting"
  }
}
```

### Integration Functions
```javascript
// External System Integration
{
  "api_functions": {
    "external_api_request": "HTTP requests to third-party APIs",
    "realtime_functions": "WebSocket and live data",
    "lambda_functions": "Serverless function execution"
  },
  "storage_functions": {
    "file_storage": "File upload and management",
    "data_caching": "Redis-based performance optimization",
    "cloud_services": "AWS, Google Cloud, Azure integrations"
  }
}
```

## 🛠️ **Building Function Stacks**

### Basic Workflow Creation

```javascript
// Example: User Registration Function Stack
{
  "workflow_name": "User Registration",
  "trigger": "POST /api:v1/auth/register",
  "steps": [
    {
      "function": "Create Variable",
      "variable_name": "user_email",
      "value": "{{inputs.email}}",
      "purpose": "Store user email for processing"
    },
    {
      "function": "Text Manipulation",
      "operation": "lowercase",
      "input": "{{user_email}}",
      "output_variable": "normalized_email"
    },
    {
      "function": "Query All Records",
      "table": "users",
      "filter": {
        "email": "{{normalized_email}}"
      },
      "purpose": "Check if user already exists"
    },
    {
      "function": "Conditional",
      "condition": "{{query_result.length > 0}}",
      "true_steps": [
        {
          "function": "Response",
          "status_code": 409,
          "message": "User already exists"
        }
      ],
      "false_steps": [
        {
          "function": "Add Record",
          "table": "users",
          "data": {
            "email": "{{normalized_email}}",
            "password": "{{inputs.password | hash}}",
            "created_at": "{{timestamp}}"
          }
        }
      ]
    }
  ]
}
```

### Advanced Data Processing

```javascript
// Example: E-commerce Order Processing
{
  "workflow_name": "Process Order",
  "trigger": "POST /api:v1/orders",
  "steps": [
    // Step 1: Validate inventory
    {
      "function": "Loop",
      "input_array": "{{inputs.items}}",
      "loop_item_variable": "item",
      "steps": [
        {
          "function": "Get Record",
          "table": "products",
          "record_id": "{{item.product_id}}"
        },
        {
          "function": "Conditional",
          "condition": "{{product.stock < item.quantity}}",
          "true_steps": [
            {
              "function": "Response",
              "status_code": 400,
              "message": "Insufficient stock for {{product.name}}"
            }
          ]
        }
      ]
    },
    // Step 2: Calculate totals
    {
      "function": "Math",
      "operation": "sum",
      "values": "{{items.*.subtotal}}",
      "output_variable": "order_subtotal"
    },
    {
      "function": "Math",
      "operation": "multiply",
      "value1": "{{order_subtotal}}",
      "value2": "{{tax_rate}}",
      "output_variable": "tax_amount"
    },
    // Step 3: Create order record
    {
      "function": "Add Record",
      "table": "orders",
      "data": {
        "user_id": "{{auth_user.id}}",
        "subtotal": "{{order_subtotal}}",
        "tax": "{{tax_amount}}",
        "total": "{{order_subtotal + tax_amount}}",
        "status": "pending"
      },
      "output_variable": "new_order"
    },
    // Step 4: Update inventory
    {
      "function": "Loop",
      "input_array": "{{inputs.items}}",
      "steps": [
        {
          "function": "Edit Record",
          "table": "products",
          "record_id": "{{item.product_id}}",
          "data": {
            "stock": "{{product.stock - item.quantity}}"
          }
        }
      ]
    }
  ]
}
```

## 🔗 **Integration Examples**

### n8n Workflow Integration

```javascript
// n8n Node calling Xano Function Stack
{
  "node_type": "HTTP Request",
  "method": "POST",
  "url": "https://your-xano.xano.io/api:v1/process-payment",
  "headers": {
    "Authorization": "Bearer {{$json.auth_token}}",
    "Content-Type": "application/json"
  },
  "body": {
    "order_id": "{{$json.order_id}}",
    "payment_method": "{{$json.payment_method}}",
    "amount": "{{$json.total_amount}}"
  }
}

// Corresponding Xano Function Stack
{
  "endpoint": "/process-payment",
  "method": "POST",
  "functions": [
    {
      "function": "Get Record",
      "table": "orders",
      "record_id": "{{inputs.order_id}}"
    },
    {
      "function": "External API Request",
      "url": "https://api.stripe.com/v1/payment_intents",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{env.STRIPE_SECRET_KEY}}"
      },
      "body": {
        "amount": "{{order.total * 100}}",
        "currency": "usd",
        "metadata": {
          "order_id": "{{order.id}}"
        }
      }
    },
    {
      "function": "Edit Record",
      "table": "orders",
      "record_id": "{{order.id}}",
      "data": {
        "payment_intent_id": "{{stripe_response.id}}",
        "status": "processing"
      }
    }
  ]
}
```

### WeWeb Data Binding

```javascript
// WeWeb Collection binding to Xano Function Stack
{
  "collection_name": "user_dashboard",
  "api_endpoint": "https://your-xano.xano.io/api:v1/dashboard-data",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{user.authToken}}"
  },
  "auto_fetch": true,
  "refresh_interval": 30000
}

// Xano Function Stack for Dashboard Data
{
  "endpoint": "/dashboard-data",
  "method": "GET",
  "functions": [
    {
      "function": "Query All Records",
      "table": "orders",
      "filter": {
        "user_id": "{{auth_user.id}}",
        "created_at": {
          ">=": "{{start_of_month}}"
        }
      },
      "output_variable": "monthly_orders"
    },
    {
      "function": "Math",
      "operation": "sum",
      "values": "{{monthly_orders.*.total}}",
      "output_variable": "monthly_spending"
    },
    {
      "function": "Query All Records",
      "table": "products",
      "filter": {
        "category": "{{user.preferences.favorite_category}}"
      },
      "limit": 5,
      "output_variable": "recommended_products"
    },
    {
      "function": "Response",
      "body": {
        "monthly_orders_count": "{{monthly_orders.length}}",
        "monthly_spending": "{{monthly_spending}}",
        "recent_orders": "{{monthly_orders | limit:3}}",
        "recommended_products": "{{recommended_products}}"
      }
    }
  ]
}
```

## 🚀 **Advanced Patterns**

### Error Handling and Validation

```javascript
// Comprehensive Error Handling Pattern
{
  "function_stack": [
    {
      "function": "Try-Catch",
      "try_steps": [
        {
          "function": "External API Request",
          "url": "https://api.third-party.com/data",
          "timeout": 5000
        }
      ],
      "catch_steps": [
        {
          "function": "Conditional",
          "condition": "{{error.status === 'timeout'}}",
          "true_steps": [
            {
              "function": "Add Record",
              "table": "error_logs",
              "data": {
                "error_type": "api_timeout",
                "endpoint": "third-party-api",
                "occurred_at": "{{timestamp}}"
              }
            },
            {
              "function": "Response",
              "status_code": 503,
              "message": "Service temporarily unavailable"
            }
          ],
          "false_steps": [
            {
              "function": "Response",
              "status_code": 500,
              "message": "Internal server error"
            }
          ]
        }
      ]
    }
  ]
}
```

### Performance Optimization with Caching

```javascript
// Redis Caching Implementation
{
  "function_stack": [
    {
      "function": "Create Variable",
      "variable_name": "cache_key",
      "value": "product_list_{{inputs.category}}_{{inputs.page}}"
    },
    {
      "function": "Data Caching (Redis)",
      "operation": "get",
      "key": "{{cache_key}}",
      "output_variable": "cached_data"
    },
    {
      "function": "Conditional",
      "condition": "{{cached_data !== null}}",
      "true_steps": [
        {
          "function": "Response",
          "body": "{{cached_data}}",
          "headers": {
            "X-Cache": "HIT"
          }
        }
      ],
      "false_steps": [
        {
          "function": "Query All Records",
          "table": "products",
          "filter": {
            "category": "{{inputs.category}}",
            "active": true
          },
          "limit": 20,
          "offset": "{{(inputs.page - 1) * 20}}"
        },
        {
          "function": "Data Caching (Redis)",
          "operation": "set",
          "key": "{{cache_key}}",
          "value": "{{products}}",
          "ttl": 300
        },
        {
          "function": "Response",
          "body": "{{products}}",
          "headers": {
            "X-Cache": "MISS"
          }
        }
      ]
    }
  ]
}
```

### Bulk Data Processing

```javascript
// Batch Processing Pattern
{
  "function_stack": [
    {
      "function": "Query All Records",
      "table": "users",
      "filter": {
        "email_verified": false,
        "created_at": {
          "<": "{{timestamp - (7 * 24 * 60 * 60 * 1000)}}" // 7 days ago
        }
      },
      "limit": 100,
      "output_variable": "unverified_users"
    },
    {
      "function": "Loop",
      "input_array": "{{unverified_users}}",
      "loop_item_variable": "user",
      "parallel": true,
      "max_concurrency": 10,
      "steps": [
        {
          "function": "External API Request",
          "url": "https://api.sendgrid.com/v3/mail/send",
          "method": "POST",
          "headers": {
            "Authorization": "Bearer {{env.SENDGRID_API_KEY}}"
          },
          "body": {
            "personalizations": [{
              "to": [{"email": "{{user.email}}"}],
              "subject": "Verify Your Account"
            }],
            "content": [{
              "type": "text/html",
              "value": "Please verify your account: {{verification_link}}"
            }]
          }
        },
        {
          "function": "Edit Record",
          "table": "users",
          "record_id": "{{user.id}}",
          "data": {
            "reminder_sent_at": "{{timestamp}}"
          }
        }
      ]
    }
  ]
}
```

## 🎯 **Best Practices**

### 1. Function Stack Organization

```javascript
// Organize complex workflows with clear naming
{
  "best_practices": {
    "naming_convention": {
      "variables": "descriptive_snake_case",
      "functions": "Clear action descriptions",
      "endpoints": "RESTful naming (GET /users, POST /orders)"
    },
    "modularity": {
      "custom_functions": "Extract reusable logic",
      "error_handling": "Consistent error responses",
      "validation": "Input validation at entry points"
    },
    "performance": {
      "database_queries": "Use appropriate indexes",
      "caching": "Cache expensive operations",
      "parallel_processing": "Use parallel loops for independent operations"
    }
  }
}
```

### 2. Testing and Debugging

```javascript
// Built-in Testing Approach
{
  "testing_workflow": {
    "unit_testing": "Test individual functions in isolation",
    "integration_testing": "Test complete function stacks",
    "mock_data": "Use test data for development",
    "debug_variables": "Monitor variable values during execution",
    "request_history": "Review execution logs and performance"
  },
  "debugging_tools": {
    "variable_inspector": "Real-time data monitoring",
    "step_by_step_execution": "Trace function execution",
    "error_logging": "Capture and analyze errors",
    "performance_metrics": "Monitor execution time and resource usage"
  }
}
```

### 3. Security Implementation

```javascript
// Security Best Practices in Function Stacks
{
  "security_patterns": {
    "authentication": {
      "jwt_validation": "Verify tokens in protected endpoints",
      "role_based_access": "Check user permissions before operations",
      "api_key_management": "Secure external API credentials"
    },
    "data_validation": {
      "input_sanitization": "Clean user inputs before processing",
      "sql_injection_prevention": "Use parameterized queries",
      "xss_protection": "Encode output data"
    },
    "secure_communications": {
      "https_only": "Enforce SSL for all API calls",
      "cors_configuration": "Properly configure cross-origin requests",
      "rate_limiting": "Implement request throttling"
    }
  }
}
```

## 🔧 **Common Use Cases**

### User Authentication Workflow
```javascript
// Complete authentication system
{
  "login_endpoint": "/auth/login",
  "registration_endpoint": "/auth/register",
  "password_reset_endpoint": "/auth/reset-password",
  "profile_update_endpoint": "/auth/profile"
}
```

### E-commerce Operations
```javascript
// Product catalog and order management
{
  "product_endpoints": ["/products", "/products/{id}", "/categories"],
  "order_endpoints": ["/orders", "/orders/{id}/status", "/checkout"],
  "inventory_endpoints": ["/inventory/update", "/inventory/check"]
}
```

### Content Management
```javascript
// CMS functionality
{
  "content_endpoints": ["/posts", "/pages", "/media"],
  "admin_endpoints": ["/admin/users", "/admin/settings", "/admin/analytics"]
}
```

### Real-time Features
```javascript
// Live data and notifications
{
  "realtime_endpoints": ["/notifications", "/chat", "/presence"],
  "webhook_endpoints": ["/webhooks/stripe", "/webhooks/sendgrid"]
}
```

---

*The Function Stack and Visual Builder provide the foundation for building sophisticated backend applications without code, enabling rapid development and seamless integration with modern no-code platforms.*