---
title: Types of Middleware in Xano - Complete Implementation Guide
description: Master Xano middleware patterns including pre-middleware validation, post-middleware processing, authentication middleware, logging systems, and cross-cutting concerns with comprehensive examples and integration strategies
category: functions
difficulty: intermediate
last_updated: '2025-08-17'
related_docs: []
subcategory: 08-reference/functions
tags:
- middleware
- pre-middleware
- post-middleware
- authentication-middleware
- validation-middleware
- logging-middleware
- cross-cutting-concerns
- middleware-patterns
- request-processing
- response-processing
---

# Types of Middleware in Xano - Complete Implementation Guide

## 📋 **Quick Summary**

Middleware in Xano provides powerful cross-cutting functionality that executes before or after your main function stacks. Learn to implement authentication, validation, logging, and response transformation middleware to create more maintainable and secure applications with consistent behavior across all endpoints.

## What You'll Learn

- **Middleware Fundamentals**: Understanding pre-middleware and post-middleware execution
- **Authentication Middleware**: Implement consistent authentication across endpoints
- **Validation Middleware**: Create reusable input validation patterns
- **Logging Middleware**: Track and monitor API usage and performance
- **Response Middleware**: Transform and standardize API responses
- **Integration Patterns**: Use middleware with n8n, WeWeb, and Make.com workflows

## Understanding Middleware in Xano

### What is Middleware?

```javascript
// Middleware concept and execution flow
const middlewareConcept = {
  // Definition and purpose
  definition: {
    what: "Reusable logic that executes before or after main function stacks",
    purpose: "Handle cross-cutting concerns across multiple API endpoints",
    benefits: "Reduces code duplication, ensures consistency, centralizes common logic",
    scope: "Can be applied to individual APIs, API groups, or entire workspace"
  },
  
  // Execution flow
  executionFlow: {
    request: "Client sends HTTP request to API endpoint",
    preMiddleware: "Pre-middleware executes first (before input validation)",
    inputValidation: "Xano validates required inputs and data types",
    mainFunction: "Your main API function stack executes",
    postMiddleware: "Post-middleware executes after function stack",
    response: "Final response sent back to client"
  },
  
  // Types of concerns middleware addresses
  crossCuttingConcerns: {
    authentication: "Verify user tokens and permissions",
    authorization: "Check user access to specific resources",
    validation: "Custom input validation beyond basic type checking",
    logging: "Track API usage, performance, and errors",
    caching: "Implement custom caching strategies",
    rateLimit: "Custom rate limiting and throttling",
    responseTransform: "Standardize response formats and add metadata",
    security: "Add security headers and sanitize inputs",
    monitoring: "Collect metrics and performance data"
  },
  
  // Middleware vs other approaches
  comparisonWithAlternatives: {
    customFunctions: {
      middleware: "Automatically applies to multiple endpoints",
      customFunction: "Must be manually added to each function stack"
    },
    
    duplicatedLogic: {
      middleware: "Write once, apply everywhere",
      duplication: "Copy same logic across multiple function stacks"
    },
    
    maintenance: {
      middleware: "Update logic in one place",
      manual: "Update each function stack individually"
    }
  }
};
```

### Middleware Architecture

```javascript
// Detailed middleware architecture in Xano
const middlewareArchitecture = {
  // Middleware types
  middlewareTypes: {
    preMiddleware: {
      timing: "Executes before input validation",
      access: "Has access to raw request data",
      purpose: "Authentication, request transformation, early validation",
      
      capabilities: [
        "Access to all defined API inputs",
        "Modify request data before main function",
        "Halt execution if conditions not met",
        "Add additional context to request"
      ],
      
      limitations: [
        "Runs before Xano's built-in input validation",
        "Cannot access main function stack results",
        "Must handle raw, unvalidated input data"
      ]
    },
    
    postMiddleware: {
      timing: "Executes after main function stack completes",
      access: "Has access to function stack response",
      purpose: "Response transformation, logging, cleanup",
      
      capabilities: [
        "Access to main function stack response",
        "Transform or replace response data",
        "Add metadata to responses",
        "Implement custom error handling"
      ],
      
      limitations: [
        "Cannot modify original request",
        "Cannot prevent main function execution",
        "Executes even if main function fails"
      ]
    }
  },
  
  // Application scope
  applicationScope: {
    workspaceLevel: {
      scope: "Applies to all APIs in the workspace",
      useCase: "Universal authentication, logging, security headers",
      management: "Configured in workspace settings",
      inheritance: "Inherited by all API groups and individual APIs"
    },
    
    apiGroupLevel: {
      scope: "Applies to all APIs within specific API group",
      useCase: "Group-specific validation, specialized logging",
      management: "Configured in API group settings", 
      customization: "Can override workspace-level middleware"
    },
    
    individualAPILevel: {
      scope: "Applies only to specific API endpoint",
      useCase: "Endpoint-specific processing, specialized validation",
      management: "Configured in individual API settings",
      flexibility: "Most granular control over middleware application"
    }
  },
  
  // Execution context
  executionContext: {
    inputData: {
      preMiddleware: "Raw request data in {{vars}} object",
      postMiddleware: "Main function response in {{vars}} object",
      access: "All defined API inputs available"
    },
    
    responseHandling: {
      merge: {
        behavior: "Middleware response merged with parent response",
        useCase: "Add additional fields to existing response",
        conflict: "Middleware fields override parent fields with same name"
      },
      
      replace: {
        behavior: "Middleware response completely replaces parent response",
        useCase: "Transform response format or handle errors",
        caution: "Original response data lost unless explicitly preserved"
      }
    },
    
    errorHandling: {
      silent: "Ignore middleware errors, continue normal execution",
      rethrow: "Allow post-middleware to run for error logging",
      critical: "Halt all execution if middleware error occurs"
    }
  }
};
```

## Pre-Middleware Patterns

### Authentication Middleware

```javascript
// Authentication middleware implementations
const authenticationMiddleware = {
  // JWT token validation
  jwtValidation: {
    purpose: "Validate JWT tokens before API execution",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Extract authorization header from request"
        },
        {
          function: "Conditional",
          condition: "{{vars.authorization}} exists",
          ifFalse: {
            function: "Response",
            status: 401,
            data: {
              error: true,
              message: "Authorization token required",
              code: "MISSING_TOKEN"
            }
          }
        },
        {
          function: "Text Functions",
          operation: "Extract token from 'Bearer {token}' format",
          input: "{{vars.authorization}}",
          output: "{{token}}"
        },
        {
          function: "External API Request",
          description: "Validate token with authentication service",
          url: "{{auth_service_url}}/validate",
          method: "POST",
          headers: {
            "Authorization": "Bearer {{token}}"
          }
        },
        {
          function: "Conditional",
          condition: "{{auth_response.valid}} === true",
          ifFalse: {
            function: "Response",
            status: 401,
            data: {
              error: true,
              message: "Invalid or expired token",
              code: "INVALID_TOKEN"
            }
          }
        },
        {
          function: "Create Variable",
          name: "authenticated_user",
          value: "{{auth_response.user}}"
        }
      ]
    },
    
    benefits: [
      "Consistent authentication across all endpoints",
      "Centralized token validation logic",
      "Easy to update authentication requirements",
      "Automatic user context injection"
    ]
  },
  
  // API key validation
  apiKeyValidation: {
    purpose: "Validate API keys for service-to-service communication",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Extract API key from request headers or query parameters"
        },
        {
          function: "Conditional",
          condition: "{{vars.x_api_key}} exists OR {{vars.api_key}} exists",
          ifFalse: {
            function: "Response",
            status: 401,
            data: {
              error: true,
              message: "API key required",
              code: "MISSING_API_KEY"
            }
          }
        },
        {
          function: "Create Variable",
          name: "api_key",
          value: "{{vars.x_api_key || vars.api_key}}"
        },
        {
          function: "Get Record",
          table: "api_keys",
          filter: {
            key: "{{api_key}}",
            active: true
          }
        },
        {
          function: "Conditional",
          condition: "{{api_key_record}} exists",
          ifFalse: {
            function: "Response", 
            status: 401,
            data: {
              error: true,
              message: "Invalid API key",
              code: "INVALID_API_KEY"
            }
          }
        },
        {
          function: "Edit Record",
          table: "api_keys",
          id: "{{api_key_record.id}}",
          data: {
            last_used: "{{now}}",
            usage_count: "{{api_key_record.usage_count + 1}}"
          }
        },
        {
          function: "Create Variable",
          name: "api_client",
          value: "{{api_key_record}}"
        }
      ]
    },
    
    features: [
      "API key validation and tracking",
      "Usage statistics and monitoring",
      "Client identification and context",
      "Automated usage logging"
    ]
  },
  
  // Role-based access control
  rbacMiddleware: {
    purpose: "Check user permissions and roles",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get authenticated user from previous middleware"
        },
        {
          function: "Conditional",
          condition: "{{vars.authenticated_user}} exists",
          ifFalse: {
            function: "Response",
            status: 401,
            data: {
              error: true,
              message: "Authentication required",
              code: "NOT_AUTHENTICATED"
            }
          }
        },
        {
          function: "Query All Records",
          table: "user_roles",
          filter: {
            user_id: "{{vars.authenticated_user.id}}"
          },
          with: ["role"]
        },
        {
          function: "Create Variable",
          name: "user_roles",
          value: "{{user_roles_result}}"
        },
        {
          function: "Create Variable",
          name: "user_permissions",
          value: "Array of permissions from user roles"
        },
        {
          function: "Conditional", 
          condition: "Required permissions check",
          description: "Check if user has required permissions for this endpoint",
          ifFalse: {
            function: "Response",
            status: 403,
            data: {
              error: true,
              message: "Insufficient permissions",
              code: "INSUFFICIENT_PERMISSIONS"
            }
          }
        }
      ]
    },
    
    advantages: [
      "Consistent permission checking",
      "Centralized access control logic",
      "Easy role and permission management",
      "Detailed access logging"
    ]
  }
};
```

### Input Validation Middleware

```javascript
// Advanced input validation patterns
const validationMiddleware = {
  // Comprehensive input sanitization
  inputSanitization: {
    purpose: "Sanitize and validate all user inputs",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get all request inputs for processing"
        },
        {
          function: "For Each",
          input: "{{vars}}",
          description: "Iterate through all input fields",
          
          innerFunctions: [
            {
              function: "Conditional",
              condition: "{{item}} is string type",
              ifTrue: [
                {
                  function: "Text Functions",
                  operation: "Trim whitespace",
                  input: "{{item}}",
                  output: "{{sanitized_value}}"
                },
                {
                  function: "Text Functions",
                  operation: "Remove HTML tags",
                  input: "{{sanitized_value}}",
                  output: "{{clean_value}}"
                },
                {
                  function: "Text Functions",
                  operation: "Escape special characters",
                  input: "{{clean_value}}",
                  output: "{{final_value}}"
                }
              ]
            },
            {
              function: "Update Variable",
              name: "{{loop_key}}",
              value: "{{final_value || item}}"
            }
          ]
        },
        {
          function: "Create Variable",
          name: "sanitized_inputs",
          value: "{{processed input object}}"
        }
      ]
    },
    
    sanitizationRules: {
      textFields: [
        "Trim leading and trailing whitespace",
        "Remove or escape HTML/XML tags",
        "Escape special characters for security",
        "Normalize unicode characters"
      ],
      
      emailFields: [
        "Convert to lowercase",
        "Validate email format with regex",
        "Check for common typos in domains",
        "Verify domain exists (optional)"
      ],
      
      numericFields: [
        "Validate numeric range limits",
        "Remove non-numeric characters",
        "Convert to appropriate numeric type",
        "Check for overflow/underflow"
      ]
    }
  },
  
  // Business rule validation
  businessRuleValidation: {
    purpose: "Validate complex business rules across inputs",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get sanitized inputs from previous processing"
        },
        {
          function: "Create Variable",
          name: "validation_errors",
          value: "[]"
        },
        {
          function: "Conditional",
          condition: "Age validation: {{vars.birth_date}} results in age >= 18",
          ifFalse: {
            function: "Arrays",
            operation: "Add to array",
            array: "{{validation_errors}}",
            item: {
              field: "birth_date",
              message: "Must be at least 18 years old",
              code: "AGE_REQUIREMENT"
            }
          }
        },
        {
          function: "Conditional",
          condition: "Password strength validation",
          ifFalse: {
            function: "Arrays", 
            operation: "Add to array",
            array: "{{validation_errors}}",
            item: {
              field: "password",
              message: "Password must contain uppercase, lowercase, number, and special character",
              code: "WEAK_PASSWORD"
            }
          }
        },
        {
          function: "External API Request",
          description: "Validate email address doesn't already exist",
          conditional: "Only if registering new user"
        },
        {
          function: "Conditional",
          condition: "{{validation_errors.length}} > 0",
          ifTrue: {
            function: "Response",
            status: 400,
            data: {
              error: true,
              message: "Validation failed",
              code: "VALIDATION_ERROR",
              details: {
                field_errors: "{{validation_errors}}"
              }
            }
          }
        }
      ]
    },
    
    businessRuleTypes: {
      crossFieldValidation: "Validate relationships between multiple fields",
      externalValidation: "Check against external systems or databases",
      contextualValidation: "Validate based on user context or permissions",
      temporalValidation: "Validate time-based constraints and business hours"
    }
  },
  
  // Rate limiting middleware
  rateLimitingMiddleware: {
    purpose: "Implement custom rate limiting logic",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get client IP and user context"
        },
        {
          function: "Create Variable",
          name: "rate_limit_key",
          value: "{{vars.authenticated_user.id || vars.client_ip}}"
        },
        {
          function: "External API Request",
          description: "Check Redis for current rate limit status",
          url: "{{redis_url}}/get/rate_limit_{{rate_limit_key}}",
          method: "GET"
        },
        {
          function: "Create Variable",
          name: "current_count",
          value: "{{redis_response.value || 0}}"
        },
        {
          function: "Conditional",
          condition: "{{current_count}} >= {{rate_limit_threshold}}",
          ifTrue: {
            function: "Response",
            status: 429,
            data: {
              error: true,
              message: "Rate limit exceeded. Try again later.",
              code: "RATE_LIMIT_EXCEEDED",
              retry_after: "{{rate_limit_window}}"
            }
          }
        },
        {
          function: "External API Request",
          description: "Increment rate limit counter",
          url: "{{redis_url}}/incr/rate_limit_{{rate_limit_key}}",
          method: "POST",
          data: {
            ttl: "{{rate_limit_window}}"
          }
        }
      ]
    },
    
    rateLimitStrategies: {
      perUser: "Separate limits for each authenticated user",
      perIP: "Limits based on client IP address", 
      perEndpoint: "Different limits for different API endpoints",
      sliding: "Sliding window rate limiting",
      tiered: "Different limits based on user subscription level"
    }
  }
};
```

## Post-Middleware Patterns

### Response Transformation Middleware

```javascript
// Response transformation and standardization
const responseMiddleware = {
  // Response standardization
  responseStandardization: {
    purpose: "Ensure consistent response format across all APIs",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get original API response"
        },
        {
          function: "Create Variable",
          name: "original_response",
          value: "{{vars}}"
        },
        {
          function: "Create Variable",
          name: "standardized_response",
          value: {
            success: true,
            data: "{{original_response}}",
            metadata: {
              timestamp: "{{now}}",
              request_id: "{{generate_uuid}}",
              api_version: "{{api_version}}",
              response_time_ms: "{{execution_time}}"
            },
            links: {
              self: "{{request_url}}",
              documentation: "{{docs_url}}"
            }
          }
        },
        {
          function: "Conditional",
          condition: "Response contains pagination data",
          ifTrue: {
            function: "Update Variable",
            name: "standardized_response.metadata.pagination",
            value: {
              page: "{{original_response.page}}",
              per_page: "{{original_response.per_page}}",
              total: "{{original_response.total}}",
              pages: "{{original_response.pages}}"
            }
          }
        }
      ],
      
      responseFormat: "Replace original response with standardized format"
    },
    
    standardizedStructure: {
      success: "Boolean indicating operation success",
      data: "The actual response data",
      metadata: {
        timestamp: "Response generation timestamp",
        requestId: "Unique request identifier",
        apiVersion: "API version used",
        responseTime: "Processing time in milliseconds",
        pagination: "Pagination info for collections (when applicable)"
      },
      links: {
        self: "URL of current request",
        next: "Next page URL (for paginated responses)",
        prev: "Previous page URL (for paginated responses)",
        documentation: "Link to API documentation"
      },
      errors: "Error details (for error responses)"
    }
  },
  
  // Data enrichment middleware
  dataEnrichment: {
    purpose: "Add additional context and computed fields to responses",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get original response data"
        },
        {
          function: "Conditional",
          condition: "Response contains user data",
          ifTrue: [
            {
              function: "Query All Records",
              table: "user_preferences",
              filter: {
                user_id: "{{vars.data.id}}"
              }
            },
            {
              function: "Update Variable",
              name: "vars.data.preferences",
              value: "{{user_preferences}}"
            },
            {
              function: "Create Variable",
              name: "vars.data.display_name",
              value: "{{vars.data.first_name}} {{vars.data.last_name}}"
            }
          ]
        },
        {
          function: "Conditional",
          condition: "Response contains product data",
          ifTrue: [
            {
              function: "External API Request",
              description: "Get current inventory levels",
              url: "{{inventory_api}}/stock/{{vars.data.product_id}}"
            },
            {
              function: "Update Variable",
              name: "vars.data.in_stock",
              value: "{{inventory_response.quantity > 0}}"
            },
            {
              function: "Update Variable",
              name: "vars.data.price_with_tax",
              value: "{{vars.data.price * (1 + tax_rate)}}"
            }
          ]
        }
      ],
      
      responseFormat: "Merge enriched data with original response"
    },
    
    enrichmentTypes: {
      computedFields: "Calculate derived values from existing data",
      relatedData: "Fetch and include related information",
      userContext: "Add user-specific contextual information",
      businessLogic: "Apply business rules to determine additional fields",
      externalData: "Integrate data from external services"
    }
  },
  
  // Security headers middleware
  securityHeadersMiddleware: {
    purpose: "Add security headers to all API responses",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get original response"
        },
        {
          function: "Create Variable",
          name: "security_headers",
          value: {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY", 
            "X-XSS-Protection": "1; mode=block",
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
            "Content-Security-Policy": "default-src 'self'",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Permissions-Policy": "geolocation=(), microphone=(), camera=()"
          }
        },
        {
          function: "Update Variable",
          name: "vars.headers",
          value: "{{merge existing headers with security_headers}}"
        }
      ],
      
      responseFormat: "Merge security headers into response"
    },
    
    securityHeaders: {
      contentSecurity: "Prevent XSS and injection attacks",
      frameOptions: "Prevent clickjacking attacks",
      transportSecurity: "Enforce HTTPS connections",
      contentTypeOptions: "Prevent MIME-type sniffing",
      permissionsPolicy: "Control browser feature access"
    }
  }
};
```

### Logging and Monitoring Middleware

```javascript
// Comprehensive logging and monitoring patterns
const loggingMiddleware = {
  // Request/Response logging
  requestResponseLogging: {
    purpose: "Log all API requests and responses for monitoring and debugging",
    implementation: {
      preMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Capture incoming request data"
          },
          {
            function: "Create Variable",
            name: "request_log",
            value: {
              request_id: "{{generate_uuid}}",
              timestamp: "{{now}}",
              method: "{{request_method}}",
              url: "{{request_url}}",
              user_agent: "{{request_headers.user_agent}}",
              ip_address: "{{client_ip}}",
              authenticated_user: "{{vars.authenticated_user.id || null}}",
              inputs: "{{sanitize_sensitive_data(vars)}}"
            }
          },
          {
            function: "Add Record",
            table: "api_request_logs",
            data: "{{request_log}}"
          }
        ]
      },
      
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs", 
            description: "Get response data and request context"
          },
          {
            function: "Create Variable",
            name: "response_log",
            value: {
              request_id: "{{vars.request_id}}",
              response_timestamp: "{{now}}",
              status_code: "{{response_status}}",
              response_size: "{{response_body_size}}",
              execution_time_ms: "{{execution_duration}}",
              success: "{{response_status < 400}}",
              response_data: "{{sanitize_response_data(vars)}}"
            }
          },
          {
            function: "Edit Record",
            table: "api_request_logs",
            filter: {
              request_id: "{{vars.request_id}}"
            },
            data: "{{response_log}}"
          }
        ]
      }
    },
    
    logDataTypes: {
      requestData: "Method, URL, headers, parameters, user context",
      responseData: "Status code, response size, execution time",
      userContext: "Authentication status, user ID, permissions",
      performanceMetrics: "Execution time, database queries, external API calls"
    }
  },
  
  // Error logging and alerting
  errorLoggingMiddleware: {
    purpose: "Capture and analyze API errors for monitoring and debugging",
    implementation: {
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Check for errors in response"
          },
          {
            function: "Conditional",
            condition: "{{response_status}} >= 400 OR {{vars.error}} exists",
            ifTrue: [
              {
                function: "Create Variable",
                name: "error_log",
                value: {
                  error_id: "{{generate_uuid}}",
                  timestamp: "{{now}}",
                  request_id: "{{vars.request_id}}",
                  error_type: "{{classify_error(response_status)}}",
                  status_code: "{{response_status}}",
                  error_message: "{{vars.error.message}}",
                  stack_trace: "{{vars.error.stack}}",
                  user_id: "{{vars.authenticated_user.id}}",
                  endpoint: "{{request_url}}",
                  inputs: "{{sanitize_inputs(vars)}}",
                  user_agent: "{{request_headers.user_agent}}",
                  ip_address: "{{client_ip}}"
                }
              },
              {
                function: "Add Record",
                table: "error_logs",
                data: "{{error_log}}"
              },
              {
                function: "Conditional",
                condition: "{{error_log.error_type}} === 'critical'",
                ifTrue: {
                  function: "External API Request",
                  description: "Send alert to monitoring system",
                  url: "{{alerting_webhook_url}}",
                  method: "POST",
                  data: {
                    alert: "Critical API Error",
                    severity: "high",
                    details: "{{error_log}}"
                  }
                }
              }
            ]
          }
        ]
      }
    },
    
    errorClassification: {
      validation: "400-level errors from invalid input",
      authentication: "401/403 errors from auth failures",
      notFound: "404 errors from missing resources",
      server: "500-level errors from system failures",
      external: "Errors from external service dependencies"
    }
  },
  
  // Performance monitoring
  performanceMonitoring: {
    purpose: "Track API performance metrics for optimization",
    implementation: {
      preMiddleware: {
        functionStack: [
          {
            function: "Create Variable",
            name: "performance_start",
            value: "{{current_timestamp_ms}}"
          },
          {
            function: "Create Variable",
            name: "db_query_count_start",
            value: "{{current_db_query_count}}"
          }
        ]
      },
      
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Calculate performance metrics"
          },
          {
            function: "Create Variable",
            name: "performance_metrics",
            value: {
              request_id: "{{vars.request_id}}",
              endpoint: "{{request_url}}",
              method: "{{request_method}}",
              execution_time_ms: "{{current_timestamp_ms - vars.performance_start}}",
              db_queries_executed: "{{current_db_query_count - vars.db_query_count_start}}",
              response_size_bytes: "{{response_body_size}}",
              memory_usage_mb: "{{current_memory_usage}}",
              timestamp: "{{now}}"
            }
          },
          {
            function: "Add Record",
            table: "performance_metrics",
            data: "{{performance_metrics}}"
          },
          {
            function: "Conditional",
            condition: "{{performance_metrics.execution_time_ms}} > {{slow_query_threshold}}",
            ifTrue: {
              function: "Add Record",
              table: "slow_query_alerts",
              data: {
                endpoint: "{{request_url}}",
                execution_time: "{{performance_metrics.execution_time_ms}}",
                threshold: "{{slow_query_threshold}}",
                timestamp: "{{now}}"
              }
            }
          }
        ]
      }
    },
    
    performanceMetrics: {
      responseTime: "Total request processing time",
      databaseQueries: "Number of database queries executed",
      memoryUsage: "Peak memory consumption during request",
      responseSize: "Size of response payload",
      externalAPICalls: "Number and duration of external API calls"
    }
  }
};
```

## Advanced Middleware Patterns

### Conditional Middleware

```javascript
// Conditional and dynamic middleware patterns
const conditionalMiddleware = {
  // Environment-based middleware
  environmentBasedMiddleware: {
    purpose: "Apply different middleware based on environment",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get current environment context"
        },
        {
          function: "Switch",
          input: "{{environment}}",
          cases: {
            development: [
              {
                function: "Create Variable",
                name: "debug_mode",
                value: true
              },
              {
                function: "Add Record",
                table: "debug_logs",
                data: {
                  request: "{{vars}}",
                  timestamp: "{{now}}"
                }
              }
            ],
            
            staging: [
              {
                function: "Create Variable",
                name: "test_user_context",
                value: "{{test_user_info}}"
              },
              {
                function: "External API Request",
                description: "Log to staging monitoring system",
                url: "{{staging_monitoring_url}}/log"
              }
            ],
            
            production: [
              {
                function: "Create Variable",
                name: "production_mode",
                value: true
              },
              {
                function: "Conditional",
                condition: "{{response_status}} >= 400",
                ifTrue: {
                  function: "External API Request",
                  url: "{{production_alerting_url}}/alert"
                }
              }
            ]
          }
        }
      ]
    },
    
    environmentTypes: {
      development: "Debug logging, relaxed validation, test data injection",
      staging: "Performance testing, integration validation, mock services",
      production: "Error alerting, performance monitoring, security logging"
    }
  },
  
  // Feature flag middleware
  featureFlagMiddleware: {
    purpose: "Control feature availability through feature flags",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get user context and endpoint info"
        },
        {
          function: "External API Request",
          description: "Check feature flag service",
          url: "{{feature_flag_service}}/check",
          data: {
            feature: "{{endpoint_feature_flag}}",
            user_id: "{{vars.authenticated_user.id}}",
            context: {
              ip: "{{client_ip}}",
              user_agent: "{{request_headers.user_agent}}"
            }
          }
        },
        {
          function: "Conditional",
          condition: "{{feature_flag_response.enabled}} === false",
          ifTrue: {
            function: "Response",
            status: 501,
            data: {
              error: true,
              message: "This feature is currently unavailable",
              code: "FEATURE_DISABLED"
            }
          }
        },
        {
          function: "Create Variable",
          name: "feature_config",
          value: "{{feature_flag_response.config}}"
        }
      ]
    },
    
    featureFlagTypes: {
      killSwitch: "Completely disable features in emergency",
      rollout: "Gradual rollout to percentage of users",
      userBased: "Enable features for specific user groups",
      geographic: "Enable features based on user location",
      timeWindow: "Enable features during specific time periods"
    }
  },
  
  // A/B testing middleware
  abTestingMiddleware: {
    purpose: "Route users to different test variations",
    implementation: {
      functionStack: [
        {
          function: "Get All Inputs",
          description: "Get user context for test assignment"
        },
        {
          function: "Create Variable",
          name: "user_hash",
          value: "{{hash(vars.authenticated_user.id + test_salt)}}"
        },
        {
          function: "Create Variable",
          name: "test_group",
          value: "{{user_hash % 100 < 50 ? 'A' : 'B'}}"
        },
        {
          function: "Add Record",
          table: "ab_test_assignments",
          data: {
            user_id: "{{vars.authenticated_user.id}}",
            test_name: "{{current_ab_test}}",
            variant: "{{test_group}}",
            timestamp: "{{now}}"
          }
        },
        {
          function: "Create Variable",
          name: "test_config",
          value: "{{get_test_config(test_group)}}"
        },
        {
          function: "Switch",
          input: "{{test_group}}",
          cases: {
            A: {
              function: "Create Variable",
              name: "ui_variant",
              value: "control"
            },
            B: {
              function: "Create Variable", 
              name: "ui_variant",
              value: "experimental"
            }
          }
        }
      ]
    },
    
    testingScenarios: {
      uiExperiments: "Test different user interface variations",
      algorithmTesting: "Test different recommendation algorithms",
      pricingExperiments: "Test different pricing strategies",
      contentVariations: "Test different content and messaging",
      featureComparison: "Compare different feature implementations"
    }
  }
};
```

### Middleware Chaining and Composition

```javascript
// Advanced middleware composition patterns
const middlewareComposition = {
  // Middleware pipelines
  middlewarePipelines: {
    authenticationPipeline: {
      description: "Complete authentication and authorization pipeline",
      middlewareChain: [
        "Rate Limiting Middleware",
        "API Key Validation Middleware", 
        "JWT Token Validation Middleware",
        "User Context Enrichment Middleware",
        "RBAC Permission Check Middleware"
      ],
      
      execution: "Sequential execution with early termination on failure",
      benefits: "Modular, testable, and reusable authentication flow"
    },
    
    dataPipeline: {
      description: "Data validation and transformation pipeline",
      middlewareChain: [
        "Input Sanitization Middleware",
        "Business Rule Validation Middleware",
        "Data Enrichment Middleware", 
        "Format Standardization Middleware"
      ],
      
      execution: "Each middleware transforms data for next middleware",
      benefits: "Clean separation of data processing concerns"
    },
    
    monitoringPipeline: {
      description: "Comprehensive monitoring and logging pipeline",
      middlewareChain: [
        "Request Logging Middleware",
        "Performance Monitoring Middleware",
        "Error Detection Middleware",
        "Alerting Middleware"
      ],
      
      execution: "Parallel execution where possible for performance",
      benefits: "Complete observability across all endpoints"
    }
  },
  
  // Conditional middleware execution
  conditionalExecution: {
    userTypeBasedMiddleware: {
      concept: "Different middleware for different user types",
      implementation: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Determine user type"
          },
          {
            function: "Switch",
            input: "{{vars.authenticated_user.type}}",
            cases: {
              admin: "Execute admin-specific middleware",
              customer: "Execute customer-specific middleware", 
              api_client: "Execute API client middleware",
              guest: "Execute guest user middleware"
            }
          }
        ]
      }
    },
    
    endpointSpecificMiddleware: {
      concept: "Apply middleware based on endpoint characteristics",
      implementation: {
        rules: [
          "Public endpoints: Rate limiting + input validation only",
          "Protected endpoints: Full authentication + authorization",
          "Admin endpoints: Enhanced logging + audit trail",
          "External API endpoints: API key validation + usage tracking"
        ]
      }
    }
  },
  
  // Middleware error handling
  errorHandlingStrategies: {
    gracefulDegradation: {
      concept: "Continue execution with reduced functionality on non-critical middleware errors",
      implementation: {
        silentMode: "Log errors but don't halt execution",
        fallbackMode: "Use default behavior when middleware fails",
        circuitBreaker: "Disable problematic middleware temporarily"
      }
    },
    
    failFast: {
      concept: "Immediately halt execution on any middleware error",
      implementation: {
        criticalMode: "All middleware errors are critical",
        validationRequired: "Must pass all validation middleware",
        securityEnforced: "Any security middleware failure stops execution"
      }
    },
    
    partialExecution: {
      concept: "Allow some middleware to fail while others continue",
      implementation: {
        priorityLevels: "Critical, important, optional middleware categories",
        dependencyChains: "Some middleware depends on others completing",
        rollback: "Undo changes from failed middleware pipeline"
      }
    }
  }
};
```

## Integration with No-Code Platforms

### n8n Middleware Integration

```javascript
// n8n integration with Xano middleware
const n8nMiddlewareIntegration = {
  // Webhook-based middleware triggers
  webhookMiddlewareTriggers: {
    concept: "Use n8n workflows as external middleware processors",
    implementation: {
      preMiddleware: {
        functionStack: [
          {
            function: "External API Request",
            description: "Call n8n webhook for external processing",
            url: "{{n8n_webhook_url}}/pre-process",
            method: "POST",
            data: {
              request_data: "{{vars}}",
              endpoint: "{{request_url}}",
              user_context: "{{authenticated_user}}"
            }
          },
          {
            function: "Conditional",
            condition: "{{n8n_response.allow}} === true",
            ifFalse: {
              function: "Response",
              status: "{{n8n_response.status || 403}}",
              data: "{{n8n_response.error_message}}"
            }
          },
          {
            function: "Create Variable",
            name: "n8n_enriched_data",
            value: "{{n8n_response.enriched_data}}"
          }
        ]
      }
    },
    
    useCases: [
      "External fraud detection systems",
      "Third-party validation services",
      "Complex business rule engines",
      "Multi-system data enrichment"
    ]
  },
  
  // Event-driven middleware
  eventDrivenMiddleware: {
    concept: "Trigger n8n workflows based on middleware events",
    implementation: {
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Get response data for event processing"
          },
          {
            function: "Conditional",
            condition: "Trigger condition met (error, success, threshold)",
            ifTrue: {
              function: "External API Request",
              description: "Trigger n8n workflow",
              url: "{{n8n_webhook_url}}/event-handler",
              method: "POST",
              async: true,
              data: {
                event_type: "{{determine_event_type}}",
                timestamp: "{{now}}",
                context: "{{vars}}",
                metadata: "{{request_metadata}}"
              }
            }
          }
        ]
      }
    },
    
    eventTypes: {
      errorEvents: "API errors trigger incident response workflows",
      performanceEvents: "Slow responses trigger optimization workflows", 
      businessEvents: "Successful transactions trigger fulfillment workflows",
      securityEvents: "Suspicious activity triggers security workflows"
    }
  },
  
  // Data synchronization middleware
  dataSynchronizationMiddleware: {
    concept: "Keep external systems synchronized via n8n workflows",
    implementation: {
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Check for data changes"
          },
          {
            function: "Conditional",
            condition: "Data was modified in main function",
            ifTrue: [
              {
                function: "Create Variable",
                name: "sync_payload",
                value: {
                  operation: "{{determine_operation}}",
                  table: "{{affected_table}}",
                  data: "{{changed_data}}",
                  user_id: "{{authenticated_user.id}}"
                }
              },
              {
                function: "External API Request",
                description: "Trigger data sync workflow",
                url: "{{n8n_webhook_url}}/data-sync",
                method: "POST",
                async: true,
                data: "{{sync_payload}}"
              }
            ]
          }
        ]
      }
    },
    
    synchronizationScenarios: {
      crmSync: "Sync customer data to external CRM systems",
      inventorySync: "Update inventory levels across platforms",
      analyticsSync: "Send usage data to analytics platforms", 
      backupSync: "Replicate critical data to backup systems"
    }
  }
};
```

### WeWeb Middleware Integration

```javascript
// WeWeb integration with Xano middleware
const wewebMiddlewareIntegration = {
  // Frontend context middleware
  frontendContextMiddleware: {
    concept: "Enrich API responses with frontend-specific data",
    implementation: {
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Get response data and user context"
          },
          {
            function: "Create Variable",
            name: "frontend_context",
            value: {
              user_preferences: "{{get_user_ui_preferences}}",
              feature_flags: "{{get_user_feature_flags}}",
              localization: "{{get_user_locale_settings}}",
              theme: "{{get_user_theme_preferences}}"
            }
          },
          {
            function: "Update Variable",
            name: "vars.ui_context",
            value: "{{frontend_context}}"
          }
        ]
      }
    },
    
    contextTypes: {
      userPreferences: "UI settings, layout preferences, accessibility options",
      featureFlags: "Available features for current user",
      localization: "Language, currency, date format settings",
      navigation: "Menu items, page permissions, workflow states"
    }
  },
  
  // Real-time data middleware
  realTimeDataMiddleware: {
    concept: "Prepare data for real-time updates in WeWeb",
    implementation: {
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Check if data should trigger real-time updates"
          },
          {
            function: "Conditional",
            condition: "Data change affects other users",
            ifTrue: [
              {
                function: "Create Variable",
                name: "realtime_update",
                value: {
                  channel: "{{determine_channel}}",
                  event: "{{determine_event_type}}",
                  data: "{{format_for_realtime}}",
                  affected_users: "{{get_affected_users}}"
                }
              },
              {
                function: "External API Request",
                description: "Send to WebSocket service",
                url: "{{websocket_service_url}}/broadcast",
                method: "POST",
                data: "{{realtime_update}}"
              }
            ]
          }
        ]
      }
    },
    
    realtimeScenarios: {
      chatMessages: "Broadcast new messages to chat participants",
      notifications: "Send notifications to affected users",
      dataUpdates: "Update shared data across user sessions",
      statusChanges: "Broadcast status changes to relevant users"
    }
  },
  
  // Progressive loading middleware
  progressiveLoadingMiddleware: {
    concept: "Optimize data loading for WeWeb applications",
    implementation: {
      postMiddleware: {
        functionStack: [
          {
            function: "Get All Inputs",
            description: "Analyze response data size and complexity"
          },
          {
            function: "Conditional",
            condition: "Response contains large dataset",
            ifTrue: [
              {
                function: "Create Variable",
                name: "chunked_response",
                value: {
                  immediate_data: "{{extract_critical_data}}",
                  lazy_load_urls: "{{generate_lazy_load_endpoints}}",
                  total_chunks: "{{calculate_chunk_count}}",
                  load_strategy: "progressive"
                }
              },
              {
                function: "Response",
                data: "{{chunked_response}}",
                responseType: "replace"
              }
            ]
          }
        ]
      }
    },
    
    loadingStrategies: {
      critical: "Load essential data immediately",
      deferred: "Load secondary data after initial render",
      onDemand: "Load data when user requests it",
      predictive: "Preload data based on user behavior patterns"
    }
  }
};
```

## 💡 **Pro Tips**

1. **Start Simple**: Begin with basic authentication middleware before building complex logic

2. **Plan Your Pipeline**: Design middleware execution order carefully to avoid conflicts

3. **Handle Errors Gracefully**: Always plan for middleware failures and provide fallbacks

4. **Monitor Performance**: Track middleware execution time to avoid performance bottlenecks

5. **Keep It Modular**: Build focused middleware that does one thing well

## Try This: Complete Middleware Implementation

Build a comprehensive middleware system:

```javascript
// Complete middleware implementation example
const completeMiddlewareSystem = {
  // 1. Authentication pipeline
  authenticationPipeline: {
    preMiddleware: [
      "Rate limiting based on IP and user",
      "API key validation for service accounts",
      "JWT token validation for users",
      "User context enrichment with roles",
      "Permission checking for endpoint access"
    ]
  },
  
  // 2. Data processing pipeline
  dataProcessingPipeline: {
    preMiddleware: [
      "Input sanitization and cleaning",
      "Business rule validation",
      "Data transformation and enrichment"
    ]
  },
  
  // 3. Monitoring pipeline
  monitoringPipeline: {
    postMiddleware: [
      "Request/response logging",
      "Performance metrics collection",
      "Error detection and alerting",
      "Usage analytics tracking"
    ]
  },
  
  // 4. Response standardization
  responseStandardization: {
    postMiddleware: [
      "Standard response format application",
      "Security headers addition",
      "Data enrichment for frontend",
      "Real-time update triggers"
    ]
  }
};
```

## Common Mistakes to Avoid

❌ **Adding too much logic to middleware**
✅ Keep middleware focused on specific cross-cutting concerns

❌ **Not handling middleware errors properly**
✅ Plan for failures and implement appropriate error handling

❌ **Creating performance bottlenecks**
✅ Monitor middleware execution time and optimize slow operations

❌ **Ignoring middleware execution order**
✅ Carefully plan the sequence of middleware execution

❌ **Not testing middleware in isolation**
✅ Test each middleware independently before chaining them

Middleware is a powerful pattern for implementing cross-cutting concerns in Xano applications. Use these patterns to create more maintainable, secure, and consistent APIs across your entire application.