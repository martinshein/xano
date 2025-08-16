---
title: Functions Overview - Complete Guide to Xano Function Categories
description: Comprehensive overview of all function types in Xano including database requests, data manipulation, security, APIs & lambdas, and integration with no-code platforms
category: custom-functions
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - custom-functions.md
  - building-with-visual-development.md
  - working-with-data.md
subcategory: 05-advanced-features/custom-functions
tags:
  - functions
  - database-requests
  - data-manipulation
  - security
  - apis-lambdas
  - no-code
---

## 📋 **Quick Summary**

Functions are the building blocks of Xano's visual development environment. They enable you to create powerful backend logic without writing code, covering everything from database operations to API integrations. Perfect for building complex applications with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Overview of all function categories available in Xano
- When to use different types of functions
- Best practices for function composition and architecture
- Integration patterns for no-code platforms
- Performance optimization strategies for function stacks

# Functions Overview

## Introduction

**Functions** in Xano are pre-built components that perform specific operations within your backend logic. They are organized into categories based on their functionality, from basic database operations to advanced AI integrations. Functions can be combined into **Function Stacks** to create complex workflows and business logic.

### Function Stack Architecture

**Function Stacks:**
- Sequential execution of multiple functions
- Variable passing between functions
- Conditional logic and branching
- Error handling and retry mechanisms
- Integration with external systems

**Function Categories:**
- Database Requests (CRUD operations)
- Data Manipulation (variables, conditionals, loops)
- Security (authentication, authorization)
- APIs & Lambdas (external integrations)
- Custom Functions (reusable logic)
- Utility Functions (helper operations)

## 🗄️ **Database Requests**

### Core Database Operations

**Query Operations:**
- **Query All Records**: Retrieve multiple records with filtering and sorting
- **Get Record**: Fetch a single record by ID or criteria
- **Query Single Record**: Find one record matching specific conditions

**Modification Operations:**
- **Add Record**: Insert new data into tables
- **Edit Record**: Update existing records completely
- **Patch Record**: Update specific fields of existing records
- **Add or Edit Record**: Upsert operation (insert or update)
- **Delete Record**: Remove records from tables

**Advanced Operations:**
- **Bulk Operations**: Process multiple records efficiently
- **Database Transaction**: Ensure data consistency across operations
- **External Database Query**: Connect to external databases
- **Direct Database Query**: Execute raw SQL queries

### n8n Integration Example

```javascript
// n8n workflow for database operations
{
  "nodes": [
    {
      "name": "Xano Query Records",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/users",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}"
        },
        "qs": {
          "filter": JSON.stringify({
            "status": "active",
            "created_at": {"$gte": "{{ $now.minus({days: 7}).toISO() }}"}
          }),
          "sort": "created_at desc",
          "limit": 100
        }
      }
    },
    {
      "name": "Process User Data",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const users = $input.first().json;
          
          // Transform data for external system
          const processedUsers = users.map(user => ({
            id: user.id,
            email: user.email,
            fullName: \`\${user.first_name} \${user.last_name}\`,
            signupDate: user.created_at,
            isActive: user.status === 'active'
          }));
          
          return processedUsers.map(user => ({json: user}));
        `
      }
    }
  ]
}
```

## 🔧 **Data Manipulation**

### Variable Management

**Variable Operations:**
- **Create Variable**: Initialize variables for data storage
- **Update Variable**: Modify existing variable values
- **Variable Scoping**: Manage variable accessibility across functions

**Control Flow:**
- **Conditional**: Execute functions based on logical conditions
- **Switch**: Multi-branch decision making
- **Loops**: Iterate over arrays and perform repeated operations

**Data Processing:**
- **Math**: Perform calculations and number operations
- **Arrays**: Manipulate lists and collections
- **Objects**: Work with structured data
- **Text**: String manipulation and formatting

### WeWeb Integration Example

```javascript
// WeWeb component for data manipulation
class XanoDataProcessor {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async processOrderData(orderData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/process-order`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          order_items: orderData.items,
          customer_id: orderData.customerId,
          processing_options: {
            calculate_tax: true,
            apply_discounts: true,
            validate_inventory: true
          }
        })
      });
      
      const processedOrder = await response.json();
      
      // Update WeWeb variables with processed data
      wwLib.wwVariable.updateValue('processed_order', processedOrder);
      wwLib.wwVariable.updateValue('order_total', processedOrder.calculated_total);
      wwLib.wwVariable.updateValue('tax_amount', processedOrder.tax_amount);
      
      return processedOrder;
    } catch (error) {
      console.error('Order processing failed:', error);
      wwLib.wwUtils.showErrorToast('Failed to process order');
      return null;
    }
  }
  
  async calculateDynamicPricing(productId, quantity, customerTier) {
    // Function stack processes pricing logic with multiple data manipulation functions
    const pricingData = {
      product_id: productId,
      quantity: quantity,
      customer_tier: customerTier,
      calculation_date: new Date().toISOString()
    };
    
    const response = await fetch(`${this.baseUrl}/api/calculate-pricing`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.authToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(pricingData)
    });
    
    const pricing = await response.json();
    
    // Update pricing display in WeWeb
    wwLib.wwVariable.updateValue('dynamic_price', pricing.final_price);
    wwLib.wwVariable.updateValue('discount_applied', pricing.discount_percentage);
    wwLib.wwVariable.updateValue('price_breakdown', pricing.breakdown);
    
    return pricing;
  }
}

// Initialize data processor
const dataProcessor = new XanoDataProcessor(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function processCurrentOrder() {
  const orderData = wwLib.wwVariable.getValue('current_order');
  await dataProcessor.processOrderData(orderData);
}

async function updateProductPricing() {
  const productId = wwLib.wwVariable.getValue('selected_product_id');
  const quantity = wwLib.wwVariable.getValue('order_quantity');
  const customerTier = wwLib.wwVariable.getValue('customer_tier');
  
  await dataProcessor.calculateDynamicPricing(productId, quantity, customerTier);
}
```

## 🔐 **Security Functions**

### Authentication & Authorization

**Authentication Functions:**
- User registration and login
- Password hashing and validation
- JWT token generation and verification
- Session management
- Multi-factor authentication

**Authorization Functions:**
- Role-based access control (RBAC)
- Permission checking
- Resource-level security
- API key validation
- OAuth integration

### Security Implementation Example

```javascript
// Comprehensive security function stack
[
  {
    "function": "validate_jwt_token",
    "token": "{{ request.headers.authorization|replace('Bearer ', '') }}",
    "return_as": "auth_result"
  },
  {
    "function": "conditional",
    "condition": "{{ !auth_result.valid }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 401,
        "body": {
          "error": "Invalid or expired token",
          "code": "UNAUTHORIZED"
        }
      }
    ]
  },
  {
    "function": "query_single_record",
    "table": "users",
    "filter": {"id": "{{ auth_result.user_id }}"},
    "return_as": "current_user"
  },
  {
    "function": "conditional",
    "condition": "{{ current_user.status != 'active' }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 403,
        "body": {
          "error": "User account is not active",
          "code": "ACCOUNT_INACTIVE"
        }
      }
    ]
  },
  {
    "function": "check_user_permissions",
    "user_id": "{{ current_user.id }}",
    "required_permissions": ["{{ request.body.action }}"],
    "resource_type": "{{ request.body.resource_type }}",
    "resource_id": "{{ request.body.resource_id }}",
    "return_as": "permission_check"
  },
  {
    "function": "conditional",
    "condition": "{{ !permission_check.authorized }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 403,
        "body": {
          "error": "Insufficient permissions",
          "required_permissions": "{{ permission_check.required }}",
          "code": "FORBIDDEN"
        }
      }
    ]
  }
]
```

## 🌐 **APIs & Lambdas**

### External Integrations

**API Functions:**
- **External API Request**: Call external services and APIs
- **Webhook Handling**: Process incoming webhook data
- **Rate Limiting**: Control API request frequency
- **Response Transformation**: Convert API responses

**Lambda Functions:**
- **Serverless Computing**: Execute custom code logic
- **Event Processing**: Handle asynchronous events
- **Data Transformation**: Complex data processing
- **Integration Logic**: Connect multiple systems

### Multi-Platform Integration Example

```javascript
// Cross-platform integration function stack
[
  {
    "function": "external_api_request",
    "url": "{{ env.STRIPE_API_URL }}/charges",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.STRIPE_SECRET_KEY }}",
      "Content-Type": "application/json"
    },
    "body": {
      "amount": "{{ request.body.amount * 100 }}",
      "currency": "usd",
      "customer": "{{ request.body.customer_id }}",
      "description": "{{ request.body.description }}"
    },
    "return_as": "stripe_charge"
  },
  {
    "function": "conditional",
    "condition": "{{ stripe_charge.status == 'succeeded' }}",
    "true_branch": [
      {
        "function": "add_record",
        "table": "payments",
        "data": {
          "stripe_charge_id": "{{ stripe_charge.id }}",
          "amount": "{{ stripe_charge.amount / 100 }}",
          "customer_id": "{{ request.body.customer_id }}",
          "status": "completed",
          "created_at": "{{ now }}"
        },
        "return_as": "payment_record"
      },
      {
        "function": "external_api_request",
        "url": "{{ env.MAILCHIMP_API_URL }}/lists/{{ env.MAILCHIMP_LIST_ID }}/members",
        "method": "PUT",
        "headers": {
          "Authorization": "Bearer {{ env.MAILCHIMP_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "email_address": "{{ request.body.customer_email }}",
          "status": "subscribed",
          "merge_fields": {
            "FNAME": "{{ request.body.customer_name }}",
            "LTYPE": "paid_customer",
            "AMOUNT": "{{ stripe_charge.amount / 100 }}"
          }
        },
        "execution_mode": "async"
      },
      {
        "function": "external_api_request",
        "url": "{{ env.N8N_WEBHOOK_URL }}/payment-success",
        "method": "POST",
        "body": {
          "payment_id": "{{ payment_record.id }}",
          "stripe_charge": "{{ stripe_charge }}",
          "customer_data": "{{ request.body }}",
          "timestamp": "{{ now }}"
        },
        "execution_mode": "async"
      }
    ]
  }
]
```

## 🔧 **Custom Functions**

### Reusable Business Logic

**Custom Function Benefits:**
- **Code Reusability**: Write once, use everywhere
- **Maintainability**: Centralized logic updates
- **Consistency**: Standardized business rules
- **Testing**: Isolated function testing

**Custom Function Types:**
- Business rule enforcement
- Data validation and sanitization
- Complex calculations
- External service integrations
- Report generation
- Notification systems

### Custom Function Architecture Example

```javascript
// Reusable user validation custom function
{
  "function_name": "validate_user_registration",
  "description": "Comprehensive user registration validation with business rules",
  "inputs": [
    {
      "name": "email",
      "type": "text",
      "required": true,
      "description": "User email address"
    },
    {
      "name": "password",
      "type": "text",
      "required": true,
      "description": "User password"
    },
    {
      "name": "profile_data",
      "type": "object",
      "required": false,
      "description": "Additional profile information"
    }
  ],
  "function_stack": [
    {
      "function": "create_variable",
      "name": "validation_errors",
      "value": []
    },
    {
      "function": "conditional",
      "condition": "{{ !email|regex_match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$') }}",
      "true_branch": [
        {
          "function": "update_variable",
          "name": "validation_errors",
          "operation": "append",
          "value": "Invalid email format"
        }
      ]
    },
    {
      "function": "conditional",
      "condition": "{{ password|length < 8 }}",
      "true_branch": [
        {
          "function": "update_variable",
          "name": "validation_errors",
          "operation": "append",
          "value": "Password must be at least 8 characters"
        }
      ]
    },
    {
      "function": "query_single_record",
      "table": "users",
      "filter": {"email": "{{ email }}"},
      "return_as": "existing_user"
    },
    {
      "function": "conditional",
      "condition": "{{ existing_user }}",
      "true_branch": [
        {
          "function": "update_variable",
          "name": "validation_errors",
          "operation": "append",
          "value": "Email address already registered"
        }
      ]
    },
    {
      "function": "conditional",
      "condition": "{{ validation_errors|length > 0 }}",
      "true_branch": [
        {
          "function": "return_value",
          "value": {
            "valid": false,
            "errors": "{{ validation_errors }}"
          }
        }
      ]
    },
    {
      "function": "hash_password",
      "password": "{{ password }}",
      "return_as": "hashed_password"
    },
    {
      "function": "return_value",
      "value": {
        "valid": true,
        "processed_data": {
          "email": "{{ email|lower }}",
          "password_hash": "{{ hashed_password }}",
          "profile": "{{ profile_data || {} }}",
          "validated_at": "{{ now }}"
        }
      }
    }
  ]
}
```

## 🛠️ **Utility Functions**

### Helper Operations

**Common Utilities:**
- **Date & Time**: Timestamp manipulation and formatting
- **File Operations**: File upload, download, and processing
- **Caching**: Redis-based data caching
- **Logging**: Request and error logging
- **Notifications**: Email, SMS, and push notifications

**Cloud Services:**
- **AWS Integration**: S3, Lambda, SES services
- **Google Cloud**: Storage, AI/ML services
- **Azure Services**: Various cloud integrations
- **Third-party APIs**: Payment, analytics, communication

### Utility Function Integration

```javascript
// Comprehensive utility function usage
[
  {
    "function": "upload_file",
    "file": "{{ request.files.document }}",
    "storage": "s3",
    "folder": "user-documents/{{ auth.user.id }}",
    "allowed_types": ["pdf", "doc", "docx"],
    "max_size": 10485760,
    "return_as": "uploaded_file"
  },
  {
    "function": "cache_set",
    "key": "user_document_{{ auth.user.id }}_{{ uploaded_file.id }}",
    "value": {
      "file_url": "{{ uploaded_file.url }}",
      "filename": "{{ uploaded_file.filename }}",
      "size": "{{ uploaded_file.size }}",
      "uploaded_at": "{{ now }}"
    },
    "ttl": 3600
  },
  {
    "function": "send_email",
    "template": "document_uploaded",
    "recipient": "{{ auth.user.email }}",
    "data": {
      "user_name": "{{ auth.user.first_name }}",
      "file_name": "{{ uploaded_file.filename }}",
      "file_size": "{{ uploaded_file.size|filesize }}",
      "download_url": "{{ uploaded_file.url }}"
    },
    "execution_mode": "async"
  },
  {
    "function": "log_event",
    "event_type": "file_upload",
    "data": {
      "user_id": "{{ auth.user.id }}",
      "file_id": "{{ uploaded_file.id }}",
      "file_type": "{{ uploaded_file.type }}",
      "timestamp": "{{ now }}"
    }
  }
]
```

## ⚡ **Performance Best Practices**

### Function Stack Optimization

**Efficient Design Patterns:**
- **Minimize Database Queries**: Batch operations and use joins
- **Implement Caching**: Cache frequently accessed data
- **Use Async Operations**: Non-blocking external API calls
- **Optimize Loops**: Avoid nested loops with large datasets
- **Conditional Logic**: Early returns to avoid unnecessary processing

**Resource Management:**
- **Memory Usage**: Monitor variable storage and cleanup
- **Execution Time**: Optimize slow function stacks
- **API Rate Limits**: Implement proper rate limiting
- **Error Handling**: Graceful failure management

### Performance Monitoring Example

```javascript
// Performance monitoring function stack
[
  {
    "function": "create_variable",
    "name": "performance_start",
    "value": "{{ now }}"
  },
  {
    "function": "create_variable",
    "name": "operation_metrics",
    "value": {
      "function_calls": 0,
      "database_queries": 0,
      "external_api_calls": 0,
      "cache_hits": 0,
      "errors": 0
    }
  },
  // Main business logic with performance tracking
  {
    "function": "increment_metric",
    "metric": "database_queries",
    "count": 1
  },
  {
    "function": "query_all_records",
    "table": "products",
    "filter": {"status": "active"},
    "return_as": "products"
  },
  // Performance logging
  {
    "function": "create_variable",
    "name": "execution_time",
    "value": "{{ now - performance_start }}"
  },
  {
    "function": "conditional",
    "condition": "{{ execution_time > 5000 }}",
    "true_branch": [
      {
        "function": "log_performance_warning",
        "execution_time": "{{ execution_time }}",
        "metrics": "{{ operation_metrics }}",
        "endpoint": "{{ request.path }}"
      }
    ]
  }
]
```

## 💡 **Pro Tips**

- **Start Simple**: Begin with basic functions and gradually add complexity
- **Reuse Logic**: Create custom functions for repeated operations
- **Handle Errors**: Implement comprehensive error handling in function stacks
- **Monitor Performance**: Track execution times and optimize slow operations
- **Document Functions**: Maintain clear descriptions and examples
- **Test Thoroughly**: Use Xano's testing tools to validate function behavior

## 🔧 **Troubleshooting**

### Common Function Issues

**Problem**: Function stack execution timeout  
**Solution**: Optimize database queries, implement pagination, and use async operations for external calls

**Problem**: Variables not passing between functions  
**Solution**: Check variable naming consistency and ensure proper return_as assignments

**Problem**: External API calls failing  
**Solution**: Verify API credentials, check rate limits, and implement retry logic

**Problem**: Database operations slow performance  
**Solution**: Add database indexes, optimize queries, and implement caching strategies

---

**Next Steps**: Ready to dive deeper? Explore [Custom Functions](custom-functions.md) for reusable logic or check [Working with Data](working-with-data.md) for advanced data manipulation techniques