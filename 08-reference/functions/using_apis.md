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
- REST
- HTTP
- Integration
- Consumption
- External APIs
title: 'Using APIs & External Service Integration'
---

# Using APIs & External Service Integration

## 📋 **Quick Summary**
Learn how to effectively use and consume APIs in Xano, whether integrating with third-party services like Stripe, Shopify, or HubSpot, or building robust API consumption patterns for n8n, WeWeb, and other no-code platforms. Master authentication, error handling, and data transformation for reliable API integrations.

## 🎯 **Core Concepts**

### What is API Consumption?
API consumption is the process of making requests to external services to retrieve data, trigger actions, or synchronize information between systems. Xano provides powerful tools for consuming both REST and GraphQL APIs with comprehensive error handling and response processing.

### Types of API Integration
- **Data Synchronization**: Keep data in sync between systems
- **Service Integration**: Leverage external services (payments, email, CRM)
- **Workflow Automation**: Trigger external actions based on internal events
- **Real-time Communication**: WebSockets and live data streams

## 🛠️ **Basic API Consumption**

### Simple GET Request

```javascript
// Basic external API request pattern
{
  "function": "External API Request",
  "url": "https://api.example.com/users",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{env.API_TOKEN}}",
    "Content-Type": "application/json",
    "User-Agent": "Xano-Integration/1.0"
  },
  "query_parameters": {
    "page": 1,
    "limit": 100,
    "status": "active"
  },
  "timeout": 30000,
  "output_variable": "api_response"
}
```

### POST Request with Data

```javascript
// Creating records via external API
{
  "function": "External API Request",
  "url": "https://api.crm.com/contacts",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{env.CRM_API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "first_name": "{{inputs.first_name}}",
    "last_name": "{{inputs.last_name}}",
    "email": "{{inputs.email}}",
    "company": "{{inputs.company}}",
    "tags": ["lead", "website"],
    "custom_fields": {
      "lead_source": "xano_integration",
      "priority": "high"
    }
  },
  "output_variable": "crm_response"
}
```

## 🔐 **Authentication Patterns**

### Bearer Token Authentication

```javascript
// Most common API authentication method
{
  "authentication_setup": {
    "function": "Create Variable",
    "variable_name": "auth_headers",
    "value": {
      "Authorization": "Bearer {{env.API_ACCESS_TOKEN}}",
      "Content-Type": "application/json"
    }
  },
  "api_request": {
    "function": "External API Request",
    "url": "https://api.service.com/data",
    "headers": "{{auth_headers}}",
    "method": "GET"
  }
}
```

### API Key Authentication

```javascript
// API key in header or query parameter
{
  "header_based": {
    "function": "External API Request",
    "url": "https://api.service.com/endpoint",
    "headers": {
      "X-API-Key": "{{env.SERVICE_API_KEY}}",
      "Content-Type": "application/json"
    }
  },
  "query_parameter_based": {
    "function": "External API Request",
    "url": "https://api.service.com/endpoint",
    "query_parameters": {
      "api_key": "{{env.SERVICE_API_KEY}}",
      "format": "json"
    }
  }
}
```

### OAuth 2.0 Token Exchange

```javascript
// OAuth token refresh pattern
{
  "token_refresh_workflow": [
    {
      "function": "External API Request",
      "url": "https://oauth.provider.com/token",
      "method": "POST",
      "headers": {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      "body": "grant_type=refresh_token&refresh_token={{env.OAUTH_REFRESH_TOKEN}}&client_id={{env.OAUTH_CLIENT_ID}}&client_secret={{env.OAUTH_CLIENT_SECRET}}",
      "output_variable": "token_response"
    },
    {
      "function": "Conditional",
      "condition": "{{token_response.access_token !== null}}",
      "true_steps": [
        {
          "function": "External API Request",
          "url": "https://api.service.com/data",
          "headers": {
            "Authorization": "Bearer {{token_response.access_token}}"
          },
          "output_variable": "api_data"
        }
      ]
    }
  ]
}
```

## 🔄 **Advanced Integration Patterns**

### Pagination Handling

```javascript
// Automatic pagination processing
{
  "pagination_workflow": {
    "function_name": "fetch_all_pages",
    "steps": [
      {
        "function": "Create Variable",
        "variable_name": "all_results",
        "value": []
      },
      {
        "function": "Create Variable",
        "variable_name": "current_page",
        "value": 1
      },
      {
        "function": "Create Variable",
        "variable_name": "has_more_pages",
        "value": true
      },
      {
        "function": "Loop",
        "condition": "{{has_more_pages === true}}",
        "steps": [
          {
            "function": "External API Request",
            "url": "https://api.service.com/data",
            "query_parameters": {
              "page": "{{current_page}}",
              "per_page": 100
            },
            "output_variable": "page_response"
          },
          {
            "function": "Arrays",
            "operation": "concat",
            "array1": "{{all_results}}",
            "array2": "{{page_response.data}}",
            "output_variable": "all_results"
          },
          {
            "function": "Math",
            "operation": "add",
            "value1": "{{current_page}}",
            "value2": 1,
            "output_variable": "current_page"
          },
          {
            "function": "Update Variable",
            "variable_name": "has_more_pages",
            "value": "{{page_response.has_next_page}}"
          }
        ]
      }
    ]
  }
}
```

### Rate Limit Handling

```javascript
// Intelligent rate limit management
{
  "rate_limited_request": {
    "function_name": "safe_api_request",
    "parameters": {
      "url": "string",
      "method": "string",
      "data": "object"
    },
    "steps": [
      {
        "function": "Try-Catch",
        "try_steps": [
          {
            "function": "External API Request",
            "url": "{{inputs.url}}",
            "method": "{{inputs.method}}",
            "body": "{{inputs.data}}",
            "output_variable": "api_response"
          }
        ],
        "catch_steps": [
          {
            "function": "Conditional",
            "condition": "{{error.status_code === 429}}",
            "true_steps": [
              {
                "function": "Create Variable",
                "variable_name": "retry_after",
                "value": "{{error.headers['Retry-After'] || 60}}"
              },
              {
                "function": "Wait",
                "duration_seconds": "{{retry_after}}"
              },
              {
                "function": "External API Request",
                "url": "{{inputs.url}}",
                "method": "{{inputs.method}}",
                "body": "{{inputs.data}}",
                "output_variable": "api_response"
              }
            ],
            "false_steps": [
              {
                "function": "Response",
                "status_code": "{{error.status_code}}",
                "body": {
                  "error": "API request failed",
                  "details": "{{error.message}}"
                }
              }
            ]
          }
        ]
      }
    ]
  }
}
```

## 🔗 **Integration Examples**

### Stripe Payment Integration

```javascript
// Complete Stripe payment processing
{
  "stripe_payment_flow": [
    {
      "step": "Create Customer",
      "function": "External API Request",
      "url": "https://api.stripe.com/v1/customers",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{env.STRIPE_SECRET_KEY}}",
        "Content-Type": "application/x-www-form-urlencoded"
      },
      "body": "email={{inputs.email}}&name={{inputs.name}}&metadata[user_id]={{inputs.user_id}}",
      "output_variable": "stripe_customer"
    },
    {
      "step": "Create Payment Intent",
      "function": "External API Request",
      "url": "https://api.stripe.com/v1/payment_intents",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{env.STRIPE_SECRET_KEY}}",
        "Content-Type": "application/x-www-form-urlencoded"
      },
      "body": "amount={{inputs.amount}}&currency=usd&customer={{stripe_customer.id}}&metadata[order_id]={{inputs.order_id}}",
      "output_variable": "payment_intent"
    },
    {
      "step": "Store Payment Record",
      "function": "Add Record",
      "table": "payments",
      "data": {
        "user_id": "{{inputs.user_id}}",
        "stripe_customer_id": "{{stripe_customer.id}}",
        "stripe_payment_intent_id": "{{payment_intent.id}}",
        "amount": "{{inputs.amount}}",
        "currency": "usd",
        "status": "{{payment_intent.status}}"
      }
    }
  ]
}
```

### HubSpot CRM Synchronization

```javascript
// Bidirectional CRM sync
{
  "hubspot_sync": {
    "create_contact": {
      "function": "External API Request",
      "url": "https://api.hubapi.com/crm/v3/objects/contacts",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{env.HUBSPOT_ACCESS_TOKEN}}",
        "Content-Type": "application/json"
      },
      "body": {
        "properties": {
          "firstname": "{{inputs.first_name}}",
          "lastname": "{{inputs.last_name}}",
          "email": "{{inputs.email}}",
          "phone": "{{inputs.phone}}",
          "company": "{{inputs.company}}",
          "lifecyclestage": "lead",
          "lead_source": "website_form"
        }
      },
      "output_variable": "hubspot_contact"
    },
    "update_xano_record": {
      "function": "Edit Record",
      "table": "leads",
      "record_id": "{{inputs.lead_id}}",
      "data": {
        "hubspot_contact_id": "{{hubspot_contact.id}}",
        "synced_at": "{{timestamp}}",
        "sync_status": "success"
      }
    }
  }
}
```

### Shopify Product Integration

```javascript
// E-commerce product synchronization
{
  "shopify_product_sync": {
    "fetch_products": {
      "function": "External API Request",
      "url": "https://{{env.SHOPIFY_STORE}}.myshopify.com/admin/api/2023-10/products.json",
      "headers": {
        "X-Shopify-Access-Token": "{{env.SHOPIFY_ACCESS_TOKEN}}"
      },
      "query_parameters": {
        "limit": 250,
        "updated_at_min": "{{inputs.last_sync_time}}"
      },
      "output_variable": "shopify_products"
    },
    "process_products": {
      "function": "Loop",
      "input_array": "{{shopify_products.products}}",
      "loop_item_variable": "product",
      "steps": [
        {
          "function": "Query All Records",
          "table": "products",
          "filter": {
            "shopify_id": "{{product.id}}"
          },
          "output_variable": "existing_product"
        },
        {
          "function": "Conditional",
          "condition": "{{existing_product.length > 0}}",
          "true_steps": [
            {
              "function": "Edit Record",
              "table": "products",
              "record_id": "{{existing_product[0].id}}",
              "data": {
                "title": "{{product.title}}",
                "price": "{{product.variants[0].price}}",
                "inventory": "{{product.variants[0].inventory_quantity}}",
                "updated_at": "{{product.updated_at}}"
              }
            }
          ],
          "false_steps": [
            {
              "function": "Add Record",
              "table": "products",
              "data": {
                "shopify_id": "{{product.id}}",
                "title": "{{product.title}}",
                "description": "{{product.body_html}}",
                "price": "{{product.variants[0].price}}",
                "inventory": "{{product.variants[0].inventory_quantity}}",
                "created_at": "{{product.created_at}}"
              }
            }
          ]
        }
      ]
    }
  }
}
```

## 📊 **Error Handling & Monitoring**

### Comprehensive Error Management

```javascript
// Robust API error handling framework
{
  "error_handling_framework": {
    "function": "Try-Catch",
    "try_steps": [
      {
        "function": "External API Request",
        "url": "{{inputs.api_endpoint}}",
        "method": "{{inputs.method}}",
        "headers": "{{inputs.headers}}",
        "body": "{{inputs.body}}",
        "timeout": 30000,
        "output_variable": "api_response"
      }
    ],
    "catch_steps": [
      {
        "function": "Switch",
        "variable": "{{error.status_code}}",
        "cases": {
          "400": [
            {
              "function": "Add Record",
              "table": "api_error_logs",
              "data": {
                "error_type": "bad_request",
                "endpoint": "{{inputs.api_endpoint}}",
                "request_data": "{{inputs.body}}",
                "error_details": "{{error.response}}",
                "timestamp": "{{timestamp}}"
              }
            },
            {
              "function": "Response",
              "status_code": 400,
              "body": {
                "error": "Invalid request data",
                "details": "{{error.response.message}}"
              }
            }
          ],
          "401": [
            {
              "function": "Custom Function",
              "custom_function": "refresh_api_token",
              "parameters": {
                "service": "{{inputs.service_name}}"
              }
            }
          ],
          "429": [
            {
              "function": "Custom Function",
              "custom_function": "handle_rate_limit",
              "parameters": {
                "retry_after": "{{error.headers['Retry-After']}}",
                "endpoint": "{{inputs.api_endpoint}}"
              }
            }
          ],
          "500": [
            {
              "function": "Custom Function",
              "custom_function": "notify_admin",
              "parameters": {
                "alert_type": "external_api_failure",
                "service": "{{inputs.service_name}}",
                "error": "{{error}}"
              }
            }
          ]
        },
        "default": [
          {
            "function": "Response",
            "status_code": 500,
            "body": {
              "error": "External service unavailable",
              "retry_suggested": true
            }
          }
        ]
      }
    ]
  }
}
```

## 🚀 **Performance Optimization**

### Request Caching Strategy

```javascript
// Intelligent API response caching
{
  "cached_api_request": {
    "function_name": "cached_external_request",
    "parameters": {
      "cache_key": "string",
      "api_url": "string",
      "cache_ttl": "number"
    },
    "steps": [
      {
        "function": "Data Caching (Redis)",
        "operation": "get",
        "key": "{{inputs.cache_key}}",
        "output_variable": "cached_response"
      },
      {
        "function": "Conditional",
        "condition": "{{cached_response !== null}}",
        "true_steps": [
          {
            "function": "Response",
            "body": "{{cached_response}}",
            "headers": {
              "X-Cache": "HIT",
              "X-Cache-Age": "{{cached_response.age}}"
            }
          }
        ],
        "false_steps": [
          {
            "function": "External API Request",
            "url": "{{inputs.api_url}}",
            "output_variable": "fresh_response"
          },
          {
            "function": "Data Caching (Redis)",
            "operation": "set",
            "key": "{{inputs.cache_key}}",
            "value": "{{fresh_response}}",
            "ttl": "{{inputs.cache_ttl}}"
          },
          {
            "function": "Response",
            "body": "{{fresh_response}}",
            "headers": {
              "X-Cache": "MISS"
            }
          }
        ]
      }
    ]
  }
}
```

## 🎯 **Best Practices**

### API Integration Guidelines

```javascript
// Best practices for reliable API integration
{
  "integration_principles": {
    "reliability": {
      "timeout_management": "Set appropriate timeouts (30-60 seconds)",
      "retry_logic": "Implement exponential backoff for transient failures",
      "circuit_breaker": "Prevent cascade failures with circuit breaker pattern"
    },
    "security": {
      "credential_management": "Store API keys in environment variables",
      "request_signing": "Use HMAC signatures when available",
      "data_validation": "Validate all incoming API responses"
    },
    "performance": {
      "response_caching": "Cache stable data with appropriate TTL",
      "request_batching": "Batch multiple operations when supported",
      "connection_pooling": "Reuse HTTP connections for efficiency"
    },
    "monitoring": {
      "error_tracking": "Log all API errors with context",
      "performance_monitoring": "Track response times and success rates",
      "alerting": "Set up alerts for API failures and degradation"
    }
  }
}
```

---

*Effective API usage enables powerful integrations that extend Xano's capabilities, allowing seamless communication with external services while maintaining reliability, security, and performance.*