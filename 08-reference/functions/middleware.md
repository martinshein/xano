---
title: Middleware Functions Reference
description: Complete guide to implementing middleware in Xano - request processing, authentication, validation, and cross-cutting concerns for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- middleware
- request-processing
- authentication
- validation
- cross-cutting-concerns
- interceptors
- filters
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 02-core-concepts/function-stack/middleware.md
- 08-reference/functions/webhooks.md
- 08-reference/functions/triggers.md
---

## 📋 **Quick Summary**

Middleware in Xano provides a powerful way to execute cross-cutting functionality across multiple API endpoints. It enables authentication, validation, logging, rate limiting, and other concerns that apply to multiple routes without code duplication.

## What You'll Learn

- How to create and configure middleware functions
- Authentication and authorization middleware patterns
- Request validation and transformation middleware
- Logging, monitoring, and rate limiting implementations
- Error handling and response modification middleware
- Integration patterns for no-code platforms
- Best practices for middleware performance and security

## Understanding Middleware

### Middleware Execution Flow

Middleware functions execute in a specific order in the request-response cycle:

```javascript
// Request flow
Request → Middleware 1 → Middleware 2 → Main Function → Response
        ↓               ↓                ↓
    Pre-processing   Validation      Business Logic
```

### Middleware Types

**Pre-Request Middleware:**
- Execute before main function
- Handle authentication and authorization
- Validate and transform requests
- Rate limiting and throttling

**Post-Request Middleware:**
- Execute after main function
- Modify responses
- Log request/response data
- Handle error responses

**Error Handling Middleware:**
- Process errors from any stage
- Transform error responses
- Log error details
- Implement fallback logic

## Basic Middleware Implementation

### 1. Authentication Middleware

```javascript
// JWT Authentication Middleware
{
  "middleware_name": "jwt_auth",
  "execution_order": 1,
  "function_stack": [
    {
      "function": "create_variable",
      "name": "auth_header",
      "value": "{{request.headers.authorization}}"
    },
    {
      "function": "conditional",
      "condition": "{{!auth_header || !starts_with(auth_header, 'Bearer ')}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 401,
          "body": {
            "error": "Missing or invalid authorization header",
            "code": "AUTH_REQUIRED"
          }
        }
      ]
    },
    {
      "function": "create_variable",
      "name": "token",
      "value": "{{substring(auth_header, 7)}}"
    },
    {
      "function": "try_catch",
      "try_stack": [
        {
          "function": "jwt_verify",
          "token": "{{token}}",
          "secret": "{{env.JWT_SECRET}}"
        },
        {
          "function": "get_record",
          "table": "users",
          "record_id": "{{jwt_payload.user_id}}"
        },
        {
          "function": "conditional",
          "condition": "{{!users || users.status != 'active'}}",
          "true_stack": [
            {
              "function": "return_response",
              "status": 403,
              "body": {"error": "User account is not active"}
            }
          ]
        },
        {
          "function": "set_auth_user",
          "user": "{{users}}"
        }
      ],
      "catch_stack": [
        {
          "function": "return_response",
          "status": 401,
          "body": {
            "error": "Invalid or expired token",
            "code": "TOKEN_INVALID"
          }
        }
      ]
    }
  ]
}
```

### 2. Request Validation Middleware

```javascript
// Input validation middleware
{
  "middleware_name": "validate_request",
  "execution_order": 2,
  "function_stack": [
    {
      "function": "create_variable",
      "name": "validation_rules",
      "value": {
        "email": {"required": true, "type": "email"},
        "name": {"required": true, "min_length": 2, "max_length": 50},
        "age": {"required": false, "type": "integer", "min": 13, "max": 120}
      }
    },
    {
      "function": "create_variable",
      "name": "validation_errors",
      "value": []
    },
    {
      "function": "for_each_loop",
      "array": "{{object_keys(validation_rules)}}",
      "function_stack": [
        {
          "function": "create_variable",
          "name": "field_name",
          "value": "{{loop_item}}"
        },
        {
          "function": "create_variable",
          "name": "field_rules",
          "value": "{{validation_rules[field_name]}}"
        },
        {
          "function": "create_variable",
          "name": "field_value",
          "value": "{{request.body[field_name]}}"
        },
        {
          "function": "conditional",
          "condition": "{{field_rules.required && !field_value}}",
          "true_stack": [
            {
              "function": "update_variable",
              "variable": "validation_errors",
              "value": "{{append(validation_errors, field_name + ' is required')}}"
            }
          ]
        },
        {
          "function": "conditional",
          "condition": "{{field_value && field_rules.type == 'email' && !is_valid_email(field_value)}}",
          "true_stack": [
            {
              "function": "update_variable",
              "variable": "validation_errors",
              "value": "{{append(validation_errors, field_name + ' must be a valid email')}}"
            }
          ]
        }
      ]
    },
    {
      "function": "conditional",
      "condition": "{{length(validation_errors) > 0}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 400,
          "body": {
            "error": "Validation failed",
            "details": "{{validation_errors}}"
          }
        }
      ]
    }
  ]
}
```

### 3. Rate Limiting Middleware

```javascript
// Rate limiting middleware
{
  "middleware_name": "rate_limit",
  "execution_order": 1,
  "function_stack": [
    {
      "function": "create_variable",
      "name": "client_ip",
      "value": "{{request.ip}}"
    },
    {
      "function": "create_variable",
      "name": "rate_limit_key",
      "value": "rate_limit:{{client_ip}}:{{format_date(now(), 'Y-m-d-H-i')}}"
    },
    {
      "function": "get_cache",
      "key": "{{rate_limit_key}}"
    },
    {
      "function": "create_variable",
      "name": "current_count",
      "value": "{{cache_value || 0}}"
    },
    {
      "function": "conditional",
      "condition": "{{current_count >= 100}}", // 100 requests per minute
      "true_stack": [
        {
          "function": "return_response",
          "status": 429,
          "headers": {
            "Retry-After": "60",
            "X-RateLimit-Limit": "100",
            "X-RateLimit-Remaining": "0"
          },
          "body": {
            "error": "Rate limit exceeded",
            "retry_after": 60
          }
        }
      ]
    },
    {
      "function": "set_cache",
      "key": "{{rate_limit_key}}",
      "value": "{{current_count + 1}}",
      "ttl": 60
    },
    {
      "function": "set_response_header",
      "name": "X-RateLimit-Limit",
      "value": "100"
    },
    {
      "function": "set_response_header",
      "name": "X-RateLimit-Remaining",
      "value": "{{99 - current_count}}"
    }
  ]
}
```

## Advanced Middleware Patterns

### 1. CORS Middleware

```javascript
// Cross-Origin Resource Sharing middleware
{
  "middleware_name": "cors",
  "execution_order": 0,
  "function_stack": [
    {
      "function": "create_variable",
      "name": "origin",
      "value": "{{request.headers.origin}}"
    },
    {
      "function": "create_variable",
      "name": "allowed_origins",
      "value": ["https://app.example.com", "https://staging.example.com", "http://localhost:3000"]
    },
    {
      "function": "conditional",
      "condition": "{{in_array(origin, allowed_origins)}}",
      "true_stack": [
        {
          "function": "set_response_header",
          "name": "Access-Control-Allow-Origin",
          "value": "{{origin}}"
        }
      ],
      "false_stack": [
        {
          "function": "set_response_header",
          "name": "Access-Control-Allow-Origin",
          "value": "null"
        }
      ]
    },
    {
      "function": "set_response_header",
      "name": "Access-Control-Allow-Methods",
      "value": "GET, POST, PUT, DELETE, OPTIONS"
    },
    {
      "function": "set_response_header",
      "name": "Access-Control-Allow-Headers",
      "value": "Content-Type, Authorization, X-Requested-With"
    },
    {
      "function": "set_response_header",
      "name": "Access-Control-Max-Age",
      "value": "86400"
    },
    {
      "function": "conditional",
      "condition": "{{request.method == 'OPTIONS'}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 200,
          "body": {}
        }
      ]
    }
  ]
}
```

### 2. Request Logging Middleware

```javascript
// Comprehensive request logging
{
  "middleware_name": "request_logger",
  "execution_order": 0,
  "function_stack": [
    {
      "function": "create_variable",
      "name": "request_id",
      "value": "{{generate_uuid()}}"
    },
    {
      "function": "set_request_context",
      "request_id": "{{request_id}}"
    },
    {
      "function": "create_variable",
      "name": "log_data",
      "value": {
        "request_id": "{{request_id}}",
        "method": "{{request.method}}",
        "url": "{{request.url}}",
        "ip": "{{request.ip}}",
        "user_agent": "{{request.headers['user-agent']}}",
        "content_length": "{{request.headers['content-length']}}",
        "timestamp": "{{now()}}",
        "user_id": "{{auth.user.id || null}}"
      }
    },
    {
      "function": "add_record",
      "table": "request_logs",
      "data": "{{log_data}}"
    },
    {
      "function": "set_response_header",
      "name": "X-Request-ID",
      "value": "{{request_id}}"
    }
  ]
}
```

### 3. Response Transformation Middleware

```javascript
// Response transformation middleware (post-processing)
{
  "middleware_name": "response_transformer",
  "execution_type": "post_response",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{response.status >= 200 && response.status < 300}}",
      "true_stack": [
        {
          "function": "create_variable",
          "name": "transformed_response",
          "value": {
            "success": true,
            "data": "{{response.body}}",
            "timestamp": "{{now()}}",
            "request_id": "{{request.context.request_id}}"
          }
        },
        {
          "function": "update_response",
          "body": "{{transformed_response}}"
        }
      ],
      "false_stack": [
        {
          "function": "create_variable",
          "name": "error_response",
          "value": {
            "success": false,
            "error": "{{response.body.error || 'An error occurred'}}",
            "code": "{{response.body.code || 'UNKNOWN_ERROR'}}",
            "timestamp": "{{now()}}",
            "request_id": "{{request.context.request_id}}"
          }
        },
        {
          "function": "update_response",
          "body": "{{error_response}}"
        }
      ]
    }
  ]
}
```

## No-Code Platform Integration

### n8n Middleware Integration
```javascript
// Middleware for n8n webhook processing
{
  "middleware_name": "n8n_webhook_processor",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{request.headers['x-n8n-webhook'] == 'true'}}",
      "true_stack": [
        {
          "function": "create_variable",
          "name": "webhook_signature",
          "value": "{{request.headers['x-n8n-signature']}}"
        },
        {
          "function": "verify_webhook_signature",
          "payload": "{{request.body}}",
          "signature": "{{webhook_signature}}",
          "secret": "{{env.N8N_WEBHOOK_SECRET}}"
        },
        {
          "function": "set_request_context",
          "webhook_source": "n8n",
          "workflow_id": "{{request.headers['x-n8n-workflow-id']}}"
        }
      ]
    }
  ]
}
```

### WeWeb Authentication Middleware
```javascript
// WeWeb-specific authentication middleware
{
  "middleware_name": "weweb_auth",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{request.headers['x-weweb-app-id']}}",
      "true_stack": [
        {
          "function": "get_record",
          "table": "weweb_apps",
          "filter": {"app_id": "{{request.headers['x-weweb-app-id']}}"}
        },
        {
          "function": "conditional",
          "condition": "{{!weweb_apps || weweb_apps.status != 'active'}}",
          "true_stack": [
            {
              "function": "return_response",
              "status": 403,
              "body": {"error": "Invalid or inactive WeWeb app"}
            }
          ]
        },
        {
          "function": "set_request_context",
          "weweb_app": "{{weweb_apps}}",
          "source": "weweb"
        }
      ]
    }
  ]
}
```

### Make.com Data Processing Middleware
```javascript
// Make.com scenario data middleware
{
  "middleware_name": "make_data_processor",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{request.headers['x-make-scenario-id']}}",
      "true_stack": [
        {
          "function": "create_variable",
          "name": "make_metadata",
          "value": {
            "scenario_id": "{{request.headers['x-make-scenario-id']}}",
            "execution_id": "{{request.headers['x-make-execution-id']}}",
            "bundle_position": "{{request.headers['x-make-bundle-position']}}"
          }
        },
        {
          "function": "add_record",
          "table": "make_executions",
          "data": "{{make_metadata}}"
        },
        {
          "function": "set_request_context",
          "make_metadata": "{{make_metadata}}"
        }
      ]
    }
  ]
}
```

## Error Handling Middleware

### 1. Global Error Handler

```javascript
// Global error handling middleware
{
  "middleware_name": "error_handler",
  "execution_type": "error_handler",
  "function_stack": [
    {
      "function": "create_variable",
      "name": "error_details",
      "value": {
        "message": "{{error.message}}",
        "code": "{{error.code}}",
        "stack": "{{error.stack}}",
        "request_id": "{{request.context.request_id}}",
        "user_id": "{{auth.user.id || null}}",
        "timestamp": "{{now()}}"
      }
    },
    {
      "function": "add_record",
      "table": "error_logs",
      "data": "{{error_details}}"
    },
    {
      "function": "conditional",
      "condition": "{{env.ENVIRONMENT == 'production'}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 500,
          "body": {
            "error": "Internal server error",
            "request_id": "{{request.context.request_id}}"
          }
        }
      ],
      "false_stack": [
        {
          "function": "return_response",
          "status": 500,
          "body": {
            "error": "{{error.message}}",
            "code": "{{error.code}}",
            "request_id": "{{request.context.request_id}}",
            "stack": "{{error.stack}}"
          }
        }
      ]
    }
  ]
}
```

### 2. Validation Error Handler

```javascript
// Specific validation error handler
{
  "middleware_name": "validation_error_handler",
  "execution_type": "error_handler",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{error.code == 'VALIDATION_ERROR'}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 400,
          "body": {
            "error": "Validation failed",
            "details": "{{error.validation_errors}}",
            "code": "VALIDATION_ERROR"
          }
        }
      ]
    }
  ]
}
```

## Try This: Complete Middleware Stack

Create a comprehensive middleware stack for an API:

```javascript
// Complete middleware stack configuration
{
  "api_group": "user_management",
  "middleware_stack": [
    {
      "name": "cors",
      "order": 1,
      "enabled": true
    },
    {
      "name": "request_logger",
      "order": 2,
      "enabled": true
    },
    {
      "name": "rate_limit",
      "order": 3,
      "enabled": true,
      "config": {
        "requests_per_minute": 60,
        "burst_limit": 10
      }
    },
    {
      "name": "jwt_auth",
      "order": 4,
      "enabled": true,
      "exclude_endpoints": ["/login", "/register", "/health"]
    },
    {
      "name": "validate_request",
      "order": 5,
      "enabled": true,
      "config": {
        "strict_mode": true
      }
    },
    {
      "name": "response_transformer",
      "order": 6,
      "enabled": true,
      "execution_type": "post_response"
    },
    {
      "name": "error_handler",
      "order": 7,
      "enabled": true,
      "execution_type": "error_handler"
    }
  ],
  "endpoint_specific_middleware": {
    "/upload": ["file_upload_validator", "virus_scanner"],
    "/admin/*": ["admin_auth", "admin_audit_logger"],
    "/webhook/*": ["webhook_signature_validator"]
  }
}
```

## Performance Optimization

### 1. Conditional Middleware Execution

```javascript
// Smart middleware execution
{
  "middleware_name": "smart_auth",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{starts_with(request.path, '/public/') || request.path == '/health'}}",
      "true_stack": [
        {
          "function": "skip_middleware",
          "continue": true
        }
      ]
    },
    {
      "function": "execute_auth_middleware"
    }
  ]
}
```

### 2. Caching Middleware

```javascript
// Response caching middleware
{
  "middleware_name": "response_cache",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{request.method == 'GET'}}",
      "true_stack": [
        {
          "function": "create_variable",
          "name": "cache_key",
          "value": "response:{{md5(request.url + request.query_string)}}"
        },
        {
          "function": "get_cache",
          "key": "{{cache_key}}"
        },
        {
          "function": "conditional",
          "condition": "{{cache_value}}",
          "true_stack": [
            {
              "function": "return_response",
              "status": 200,
              "headers": {"X-Cache": "HIT"},
              "body": "{{cache_value}}"
            }
          ]
        },
        {
          "function": "set_middleware_context",
          "cache_key": "{{cache_key}}"
        }
      ]
    }
  ]
}

// Post-response cache storage
{
  "middleware_name": "cache_response",
  "execution_type": "post_response",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{response.status == 200 && middleware.context.cache_key}}",
      "true_stack": [
        {
          "function": "set_cache",
          "key": "{{middleware.context.cache_key}}",
          "value": "{{response.body}}",
          "ttl": 300
        }
      ]
    }
  ]
}
```

## Common Middleware Mistakes to Avoid

### ❌ Poor Practices
- Not handling middleware errors properly
- Executing heavy operations in middleware
- Missing proper order configuration
- Not implementing proper skip conditions
- Ignoring performance implications

### ✅ Best Practices
- Keep middleware functions lightweight
- Implement proper error handling
- Use conditional execution for optimization
- Configure middleware order correctly
- Cache frequently accessed data

## Pro Tips

### 💡 **Performance Optimization**
- Use early returns to skip unnecessary processing
- Cache authentication results when possible
- Implement circuit breakers for external services
- Use conditional middleware execution

### 🔒 **Security Best Practices**
- Always validate and sanitize inputs
- Implement proper rate limiting
- Use secure headers middleware
- Log security-relevant events

### 📊 **Monitoring and Debugging**
- Add request correlation IDs
- Log middleware execution times
- Monitor middleware success/failure rates
- Implement health check endpoints

### 🔄 **Integration Patterns**
- Design middleware for reusability
- Use configuration for different environments
- Implement proper error propagation
- Create middleware composition patterns

## Troubleshooting Middleware Issues

### Common Problems
1. **Middleware not executing**: Check order and configuration
2. **Performance degradation**: Review middleware complexity
3. **Authentication failures**: Verify token validation logic
4. **CORS issues**: Check origin and header configurations

Middleware in Xano provides powerful cross-cutting functionality that enhances API security, performance, and maintainability. Proper implementation ensures consistent behavior across all endpoints while maintaining flexibility and performance.