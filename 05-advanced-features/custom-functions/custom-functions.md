---
title: Custom Functions - Reusable Business Logic Components
description: Complete guide to creating, managing, and using custom functions in Xano for building modular, maintainable backend systems with reusable business logic components
category: custom-functions
difficulty: advanced
last_updated: '2025-01-16'
related_docs:
  - async-functions.md
  - building-with-visual-development.md
  - function-stack-performance.md
subcategory: 05-advanced-features/custom-functions
tags:
  - custom-functions
  - reusable-logic
  - modular-design
  - function-stacks
  - business-logic
  - no-code
---

## 📋 **Quick Summary**

Custom functions are reusable building blocks that allow you to create business logic once and use it throughout your application. They have inputs, function stacks, and responses like API endpoints but cannot be called externally. Perfect for creating modular, maintainable code that integrates seamlessly with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- How to create and configure custom functions effectively
- Best practices for modular function design
- Advanced patterns for reusable business logic
- Organization strategies with folders and tagging
- Performance optimization and caching techniques
- Integration patterns for no-code platforms

# Custom Functions

## Overview

**Custom Functions** are internal building blocks that encapsulate business logic for reuse across multiple function stacks. Unlike API endpoints, they cannot be called externally but serve as centralized components that promote code reusability, maintainability, and consistency throughout your application.

### Custom Functions vs API Endpoints

**Custom Functions:**
- Internal use only (not externally accessible)
- Reusable across multiple function stacks
- Centralized logic maintenance
- No direct HTTP access
- Performance optimized for internal calls

**API Endpoints:**
- Externally accessible via HTTP
- Individual function stacks
- Direct external integration
- HTTP methods and authentication
- Public or private access control

## 🚀 **Creating Custom Functions**

### Basic Custom Function Structure

**Function Components:**

```javascript
// Custom function structure
{
  "name": "calculate_order_total",
  "description": "Calculates order total with tax and discounts",
  "inputs": [
    {
      "name": "items",
      "type": "array",
      "required": true,
      "description": "Array of order items"
    },
    {
      "name": "tax_rate",
      "type": "decimal", 
      "required": false,
      "default": 0.08,
      "description": "Tax rate as decimal (0.08 = 8%)"
    },
    {
      "name": "discount_code",
      "type": "text",
      "required": false,
      "description": "Optional discount code"
    }
  ],
  "function_stack": [
    // Business logic implementation
  ],
  "response": {
    "subtotal": "{{ calculated_subtotal }}",
    "tax_amount": "{{ calculated_tax }}",
    "discount_amount": "{{ calculated_discount }}",
    "total": "{{ final_total }}"
  }
}
```

### Step-by-Step Function Creation

**1. Define Function Inputs:**

```javascript
// Input configuration for user validation function
{
  "inputs": [
    {
      "name": "email",
      "type": "email",
      "required": true,
      "description": "Email address to validate"
    },
    {
      "name": "validation_level",
      "type": "text",
      "required": false,
      "default": "standard",
      "description": "Validation level: basic, standard, strict"
    },
    {
      "name": "check_domain",
      "type": "boolean",
      "required": false,
      "default": true,
      "description": "Whether to verify domain existence"
    }
  ]
}
```

**2. Implement Function Stack:**

```javascript
// Email validation function stack
[
  {
    "function": "create_variable",
    "name": "validation_result",
    "value": {
      "email": "{{ input.email }}",
      "is_valid": false,
      "errors": [],
      "warnings": []
    }
  },
  {
    "function": "conditional",
    "condition": "{{ !input.email || input.email|length == 0 }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_result",
        "operation": "merge",
        "value": {
          "errors": ["Email is required"]
        }
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ input.email && !input.email|is_email }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_result",
        "operation": "merge",
        "value": {
          "errors": "{{ validation_result.errors|append('Invalid email format') }}"
        }
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ input.validation_level == 'strict' }}",
    "true_branch": [
      {
        "function": "external_api_request",
        "url": "https://api.emailvalidation.io/v1/info",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ env.EMAIL_VALIDATION_API_KEY }}"
        },
        "query": {
          "email": "{{ input.email }}"
        },
        "return_as": "email_check_result"
      },
      {
        "function": "conditional",
        "condition": "{{ !email_check_result.deliverable }}",
        "true_branch": [
          {
            "function": "update_variable",
            "name": "validation_result",
            "operation": "merge",
            "value": {
              "warnings": "{{ validation_result.warnings|append('Email may not be deliverable') }}"
            }
          }
        ]
      }
    ]
  },
  {
    "function": "query_single_record",
    "table": "blocked_domains",
    "filter": {
      "domain": "{{ input.email|split('@')|last }}"
    },
    "return_as": "blocked_domain"
  },
  {
    "function": "conditional",
    "condition": "{{ blocked_domain }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_result",
        "operation": "merge",
        "value": {
          "errors": "{{ validation_result.errors|append('Domain is blocked') }}"
        }
      }
    ]
  },
  {
    "function": "update_variable",
    "name": "validation_result",
    "operation": "merge",
    "value": {
      "is_valid": "{{ validation_result.errors|length == 0 }}",
      "validation_level": "{{ input.validation_level }}",
      "checked_at": "{{ now }}"
    }
  }
]
```

**3. Configure Response:**

```javascript
// Function response configuration
{
  "response": {
    "is_valid": "{{ validation_result.is_valid }}",
    "email": "{{ validation_result.email }}",
    "errors": "{{ validation_result.errors }}",
    "warnings": "{{ validation_result.warnings }}",
    "validation_level": "{{ validation_result.validation_level }}",
    "checked_at": "{{ validation_result.checked_at }}"
  }
}
```

## 🔗 **No-Code Platform Integration**

### n8n Custom Function Utilization

**Workflow Using Custom Functions:**

```javascript
// n8n workflow leveraging Xano custom functions
{
  "nodes": [
    {
      "name": "Process User Registration",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/register-user",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $json.auth_token }}",
          "Content-Type": "application/json"
        },
        "body": {
          "email": "{{ $json.user_email }}",
          "password": "{{ $json.user_password }}",
          "profile": {
            "first_name": "{{ $json.first_name }}",
            "last_name": "{{ $json.last_name }}"
          }
        }
      }
    },
    {
      "name": "Send Welcome Email",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/send-welcome-email",
        "method": "POST",
        "body": {
          "user_id": "{{ $json.user_id }}",
          "email": "{{ $json.email }}",
          "template_variables": {
            "first_name": "{{ $json.first_name }}"
          }
        }
      }
    },
    {
      "name": "Add to Marketing List",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/add-to-marketing",
        "method": "POST",
        "body": {
          "user_id": "{{ $json.user_id }}",
          "list_name": "new_users",
          "tags": ["registered", "{{ $json.source }}"]
        }
      }
    }
  ]
}
```

### WeWeb Custom Function Integration

**Dynamic Business Logic Component:**

```javascript
// WeWeb component leveraging Xano custom functions
class XanoBusinessLogic {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async validateUserInput(userData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/validate-user-data`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: userData.email,
          phone: userData.phone,
          validation_level: 'strict'
        })
      });
      
      const validation = await response.json();
      
      // Update UI validation state
      wwLib.wwVariable.updateValue('validation_errors', validation.errors || []);
      wwLib.wwVariable.updateValue('validation_warnings', validation.warnings || []);
      wwLib.wwVariable.updateValue('is_form_valid', validation.is_valid);
      
      return validation;
    } catch (error) {
      console.error('Validation failed:', error);
      return { is_valid: false, errors: ['Validation service unavailable'] };
    }
  }
  
  async calculateOrderTotal(orderItems, customerData = {}) {
    try {
      const response = await fetch(`${this.baseUrl}/api/calculate-order-total`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          items: orderItems,
          customer_id: customerData.id,
          discount_code: customerData.discount_code,
          shipping_address: customerData.shipping_address
        })
      });
      
      const totals = await response.json();
      
      // Update order summary in UI
      wwLib.wwVariable.updateValue('order_subtotal', totals.subtotal);
      wwLib.wwVariable.updateValue('order_tax', totals.tax_amount);
      wwLib.wwVariable.updateValue('order_shipping', totals.shipping_amount);
      wwLib.wwVariable.updateValue('order_discount', totals.discount_amount);
      wwLib.wwVariable.updateValue('order_total', totals.total);
      
      return totals;
    } catch (error) {
      console.error('Order calculation failed:', error);
      return { error: 'Unable to calculate order total' };
    }
  }
  
  async processPayment(paymentData, orderTotal) {
    try {
      const response = await fetch(`${this.baseUrl}/api/process-payment`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          payment_method: paymentData.method,
          payment_details: paymentData.details,
          amount: orderTotal,
          currency: 'USD',
          metadata: {
            order_id: wwLib.wwVariable.getValue('current_order_id'),
            customer_id: wwLib.wwVariable.getValue('current_customer_id')
          }
        })
      });
      
      const payment = await response.json();
      
      if (payment.success) {
        wwLib.wwVariable.updateValue('payment_status', 'completed');
        wwLib.wwVariable.updateValue('transaction_id', payment.transaction_id);
        wwLib.wwUtils.showSuccessToast('Payment processed successfully!');
        wwLib.wwUtils.navigateTo('/order-confirmation');
      } else {
        wwLib.wwVariable.updateValue('payment_status', 'failed');
        wwLib.wwVariable.updateValue('payment_error', payment.error);
        wwLib.wwUtils.showErrorToast(`Payment failed: ${payment.error}`);
      }
      
      return payment;
    } catch (error) {
      console.error('Payment processing failed:', error);
      wwLib.wwUtils.showErrorToast('Payment processing unavailable');
      return { success: false, error: 'Service unavailable' };
    }
  }
  
  async generateReport(reportType, parameters = {}) {
    try {
      const response = await fetch(`${this.baseUrl}/api/generate-report`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          report_type: reportType,
          parameters: parameters,
          format: 'json',
          async: true
        })
      });
      
      const report = await response.json();
      
      if (report.async_execution_id) {
        // Start polling for completion
        this.pollReportStatus(report.async_execution_id);
        wwLib.wwUtils.showInfoToast('Report generation started...');
      }
      
      return report;
    } catch (error) {
      console.error('Report generation failed:', error);
      return { error: 'Unable to generate report' };
    }
  }
  
  async pollReportStatus(executionId) {
    const checkStatus = async () => {
      try {
        const response = await fetch(`${this.baseUrl}/api/async-status`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${this.authToken}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            execution_ids: [executionId]
          })
        });
        
        const [status] = await response.json();
        
        if (status.status === 'completed') {
          wwLib.wwVariable.updateValue('generated_report', status.output);
          wwLib.wwUtils.showSuccessToast('Report generated successfully!');
          wwLib.wwModal.open('report-viewer-modal');
        } else if (status.status === 'error') {
          wwLib.wwUtils.showErrorToast(`Report generation failed: ${status.error}`);
        } else {
          // Still processing, check again in 3 seconds
          setTimeout(checkStatus, 3000);
        }
      } catch (error) {
        console.error('Status check failed:', error);
      }
    };
    
    // Initial delay before first check
    setTimeout(checkStatus, 3000);
  }
}

// Initialize business logic helper
const businessLogic = new XanoBusinessLogic(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage examples in WeWeb
async function handleFormSubmission() {
  const userData = {
    email: wwLib.wwVariable.getValue('user_email'),
    phone: wwLib.wwVariable.getValue('user_phone')
  };
  
  const validation = await businessLogic.validateUserInput(userData);
  
  if (validation.is_valid) {
    // Proceed with registration
    wwLib.wwUtils.navigateTo('/registration-step-2');
  } else {
    // Show validation errors
    wwLib.wwVariable.updateValue('show_validation_errors', true);
  }
}

async function calculateCartTotal() {
  const cartItems = wwLib.wwVariable.getValue('cart_items');
  const customer = wwLib.wwVariable.getValue('current_customer');
  
  const totals = await businessLogic.calculateOrderTotal(cartItems, customer);
  
  if (!totals.error) {
    wwLib.wwVariable.updateValue('cart_updated', true);
  }
}
```

## 🛠️ **Advanced Custom Function Patterns**

### Modular Function Composition

**Composable User Management Functions:**

```javascript
// Base user validation function
{
  "name": "validate_user_data",
  "inputs": ["user_data", "validation_rules"],
  "function_stack": [
    // Email validation logic
    // Phone validation logic  
    // Password strength validation
  ]
}

// User creation function using validation
{
  "name": "create_user_account",
  "inputs": ["user_data", "send_welcome_email"],
  "function_stack": [
    {
      "function": "custom_function",
      "name": "validate_user_data",
      "inputs": {
        "user_data": "{{ input.user_data }}",
        "validation_rules": "standard"
      },
      "return_as": "validation_result"
    },
    {
      "function": "conditional",
      "condition": "{{ !validation_result.is_valid }}",
      "true_branch": [
        {
          "function": "return_response",
          "status": 400,
          "body": {
            "error": "Validation failed",
            "details": "{{ validation_result.errors }}"
          }
        }
      ]
    },
    {
      "function": "hash_password",
      "password": "{{ input.user_data.password }}",
      "return_as": "hashed_password"
    },
    {
      "function": "add_record",
      "table": "users",
      "data": {
        "email": "{{ input.user_data.email }}",
        "password": "{{ hashed_password }}",
        "status": "active"
      },
      "return_as": "new_user"
    },
    {
      "function": "conditional",
      "condition": "{{ input.send_welcome_email }}",
      "true_branch": [
        {
          "function": "custom_function",
          "name": "send_welcome_email",
          "inputs": {
            "user_id": "{{ new_user.id }}",
            "email": "{{ new_user.email }}"
          },
          "execution_mode": "async"
        }
      ]
    }
  ]
}
```

### Error Handling and Logging Functions

**Centralized Error Management:**

```javascript
// Error logging custom function
{
  "name": "log_error",
  "inputs": ["error_data", "context", "severity"],
  "function_stack": [
    {
      "function": "add_record",
      "table": "error_logs",
      "data": {
        "error_message": "{{ input.error_data.message }}",
        "error_code": "{{ input.error_data.code }}",
        "stack_trace": "{{ input.error_data.stack }}",
        "context": "{{ input.context }}",
        "severity": "{{ input.severity || 'medium' }}",
        "user_id": "{{ auth.user.id }}",
        "ip_address": "{{ request.ip }}",
        "user_agent": "{{ request.headers['user-agent'] }}",
        "timestamp": "{{ now }}"
      }
    },
    {
      "function": "conditional",
      "condition": "{{ input.severity == 'high' || input.severity == 'critical' }}",
      "true_branch": [
        {
          "function": "external_api_request",
          "url": "{{ env.ALERT_WEBHOOK_URL }}",
          "method": "POST",
          "body": {
            "alert_type": "error",
            "severity": "{{ input.severity }}",
            "message": "{{ input.error_data.message }}",
            "context": "{{ input.context }}",
            "timestamp": "{{ now }}"
          }
        }
      ]
    }
  ]
}

// Protected function execution with error handling
{
  "name": "safe_execute_function",
  "inputs": ["function_name", "function_inputs", "fallback_response"],
  "function_stack": [
    {
      "function": "try_catch",
      "try_block": [
        {
          "function": "custom_function",
          "name": "{{ input.function_name }}",
          "inputs": "{{ input.function_inputs }}",
          "return_as": "function_result"
        }
      ],
      "catch_block": [
        {
          "function": "custom_function",
          "name": "log_error",
          "inputs": {
            "error_data": "{{ error }}",
            "context": {
              "function_name": "{{ input.function_name }}",
              "inputs": "{{ input.function_inputs }}"
            },
            "severity": "medium"
          }
        },
        {
          "function": "create_variable",
          "name": "function_result",
          "value": "{{ input.fallback_response || {'success': false, 'error': 'Function execution failed'} }}"
        }
      ]
    }
  ]
}
```

## 📁 **Organization and Management**

### Folder Structure Strategy

**Recommended Organization:**

```javascript
// Custom function folder structure
{
  "folders": {
    "authentication": [
      "validate_user_credentials",
      "create_auth_token", 
      "refresh_token",
      "logout_user"
    ],
    "user_management": [
      "create_user_account",
      "update_user_profile",
      "deactivate_user",
      "get_user_preferences"
    ],
    "order_processing": [
      "calculate_order_total",
      "apply_discount_code",
      "process_payment",
      "generate_invoice"
    ],
    "notifications": [
      "send_welcome_email",
      "send_order_confirmation",
      "send_password_reset",
      "send_notification"
    ],
    "utilities": [
      "validate_email",
      "format_phone_number",
      "generate_unique_id",
      "log_error"
    ],
    "reporting": [
      "generate_sales_report",
      "calculate_metrics",
      "export_data",
      "create_dashboard_data"
    ]
  }
}
```

### Function Naming Conventions

**Best Practices:**

```javascript
// Naming convention examples
{
  "action_patterns": {
    "create_": "create_user_account, create_order, create_invoice",
    "update_": "update_user_profile, update_order_status",
    "delete_": "delete_user_account, delete_order",
    "get_": "get_user_data, get_order_details",
    "validate_": "validate_email, validate_payment_data",
    "calculate_": "calculate_tax, calculate_shipping",
    "send_": "send_email, send_notification",
    "process_": "process_payment, process_order"
  },
  "domain_grouping": {
    "user_": "user_create, user_update, user_validate",
    "order_": "order_create, order_calculate, order_process",
    "payment_": "payment_validate, payment_process, payment_refund"
  }
}
```

## ⚡ **Performance Optimization**

### Response Caching

**Cache Configuration:**

```javascript
// Custom function with response caching
{
  "name": "get_user_preferences",
  "caching": {
    "enabled": true,
    "ttl": 300, // 5 minutes
    "key_pattern": "user_prefs_{{ input.user_id }}",
    "invalidation_triggers": [
      "user_profile_updated",
      "preferences_changed"
    ]
  },
  "function_stack": [
    {
      "function": "query_single_record",
      "table": "user_preferences", 
      "filter": {"user_id": "{{ input.user_id }}"},
      "return_as": "preferences"
    },
    {
      "function": "conditional",
      "condition": "{{ !preferences }}",
      "true_branch": [
        {
          "function": "create_variable",
          "name": "preferences",
          "value": {
            "theme": "light",
            "notifications": true,
            "language": "en"
          }
        }
      ]
    }
  ]
}
```

### Async Function Optimization

**Background Processing:**

```javascript
// Heavy computation as async function
{
  "name": "generate_analytics_report",
  "execution_mode": "async", // Can be called asynchronously
  "function_stack": [
    {
      "function": "query_all_records",
      "table": "orders",
      "filter": {
        "created_at": {
          "$gte": "{{ input.start_date }}",
          "$lte": "{{ input.end_date }}"
        }
      },
      "return_as": "orders"
    },
    {
      "function": "custom_function",
      "name": "calculate_revenue_metrics",
      "inputs": {"orders": "{{ orders }}"},
      "return_as": "revenue_metrics"
    },
    {
      "function": "custom_function",
      "name": "calculate_customer_metrics", 
      "inputs": {"orders": "{{ orders }}"},
      "return_as": "customer_metrics"
    },
    {
      "function": "create_variable",
      "name": "report_data",
      "value": {
        "revenue": "{{ revenue_metrics }}",
        "customers": "{{ customer_metrics }}",
        "generated_at": "{{ now }}"
      }
    }
  ]
}
```

## 💡 **Pro Tips**

- **Keep Functions Focused**: Each custom function should have a single, well-defined responsibility
- **Use Descriptive Names**: Function names should clearly indicate their purpose and functionality
- **Implement Error Handling**: Always include proper error handling and fallback mechanisms
- **Leverage Async Execution**: Use async mode for time-consuming operations to improve performance
- **Cache Frequently Used Data**: Implement response caching for functions with stable outputs
- **Version Your Functions**: Use tags and descriptions to track function versions and changes

## 🔧 **Troubleshooting**

### Common Custom Function Issues

**Problem**: Custom function not appearing in function selection  
**Solution**: Verify function is published and check folder organization

**Problem**: Input validation errors when calling custom functions  
**Solution**: Ensure input types match function definitions and required fields are provided

**Problem**: Performance issues with custom functions  
**Solution**: Enable response caching, use async execution for heavy operations, and optimize database queries

**Problem**: Circular dependencies between custom functions  
**Solution**: Refactor functions to remove circular calls or create intermediate functions

---

**Next Steps**: Ready to build modular custom functions? Check out [Async Functions](async-functions.md) for background processing or explore [Building with Visual Development](building-with-visual-development.md) for complete application architecture