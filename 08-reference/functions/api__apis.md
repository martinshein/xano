---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- CRUD
- REST
- HTTP
- Endpoints
- Integration
title: 'API Design & REST Endpoints'
---

# API Design & REST Endpoints

## 📋 **Quick Summary**
Xano's API system enables you to build robust REST endpoints with visual workflows. Create CRUD operations, authentication flows, file upload handlers, and custom business logic endpoints that integrate seamlessly with n8n, WeWeb, and any frontend framework or external system.

## 🎯 **Core Concepts**

### What is an API?
An API (Application Programming Interface) acts as a communication bridge between different software applications. Like a waiter taking your order to the kitchen and bringing back your meal, an API takes requests, processes them, and returns responses.

### RESTful Architecture
REST (Representational State Transfer) is an architectural pattern that uses HTTP methods to perform operations on resources, creating predictable and scalable API interfaces.

## 🔧 **HTTP Methods & Operations**

### Standard HTTP Methods

```javascript
// HTTP methods and their typical usage
{
  "http_methods": {
    "GET": {
      "purpose": "Retrieve data without modifying anything",
      "examples": ["Fetch user profile", "List products", "Get order details"],
      "characteristics": ["Safe", "Idempotent", "Cacheable"]
    },
    "POST": {
      "purpose": "Create new resources or trigger actions",
      "examples": ["Create user", "Submit order", "Send email"],
      "characteristics": ["Not safe", "Not idempotent", "May have side effects"]
    },
    "PUT": {
      "purpose": "Update or create entire resource",
      "examples": ["Update complete user profile", "Replace document"],
      "characteristics": ["Not safe", "Idempotent", "Full resource replacement"]
    },
    "PATCH": {
      "purpose": "Partial updates to existing resources",
      "examples": ["Update user email", "Change order status"],
      "characteristics": ["Not safe", "Not idempotent", "Partial updates"]
    },
    "DELETE": {
      "purpose": "Remove resources",
      "examples": ["Delete user account", "Remove product"],
      "characteristics": ["Not safe", "Idempotent", "Resource removal"]
    }
  }
}
```

## 🛠️ **CRUD Operations**

### Auto-Generated Database APIs

```javascript
// Standard CRUD endpoints for a 'products' table
{
  "crud_endpoints": {
    "create_product": {
      "method": "POST",
      "endpoint": "/products",
      "purpose": "Create new product",
      "request_body": {
        "name": "Product Name",
        "price": 29.99,
        "description": "Product description",
        "category_id": 5,
        "active": true
      },
      "response": {
        "id": 123,
        "name": "Product Name",
        "price": 29.99,
        "description": "Product description",
        "category_id": 5,
        "active": true,
        "created_at": "2025-01-23T10:00:00Z",
        "updated_at": "2025-01-23T10:00:00Z"
      }
    },
    "get_products": {
      "method": "GET",
      "endpoint": "/products",
      "purpose": "List all products with filtering and pagination",
      "query_parameters": {
        "page": 1,
        "per_page": 20,
        "category_id": 5,
        "active": true,
        "search": "keyword"
      },
      "response": {
        "data": ["...array of products..."],
        "meta": {
          "current_page": 1,
          "per_page": 20,
          "total": 150,
          "total_pages": 8
        }
      }
    },
    "get_product": {
      "method": "GET",
      "endpoint": "/products/{id}",
      "purpose": "Get specific product by ID",
      "response": {
        "id": 123,
        "name": "Product Name",
        "price": 29.99,
        "category": {
          "id": 5,
          "name": "Electronics"
        }
      }
    },
    "update_product": {
      "method": "PATCH",
      "endpoint": "/products/{id}",
      "purpose": "Update specific product fields",
      "request_body": {
        "price": 24.99,
        "active": false
      },
      "response": {
        "id": 123,
        "name": "Product Name",
        "price": 24.99,
        "active": false,
        "updated_at": "2025-01-23T11:00:00Z"
      }
    },
    "delete_product": {
      "method": "DELETE",
      "endpoint": "/products/{id}",
      "purpose": "Remove product",
      "response": {
        "message": "Product deleted successfully"
      }
    }
  }
}
```

### Custom Business Logic Endpoints

```javascript
// Advanced product search endpoint
{
  "endpoint": "/products/search",
  "method": "POST",
  "purpose": "Advanced product search with multiple criteria",
  "function_stack": [
    {
      "function": "Create Variable",
      "variable_name": "search_conditions",
      "value": []
    },
    // Build dynamic search conditions
    {
      "function": "Conditional",
      "condition": "{{inputs.name !== null}}",
      "true_steps": [
        {
          "function": "Arrays",
          "operation": "push",
          "array": "{{search_conditions}}",
          "value": {
            "name": {"LIKE": "%{{inputs.name}}%"}
          },
          "output_variable": "search_conditions"
        }
      ]
    },
    {
      "function": "Conditional",
      "condition": "{{inputs.price_range !== null}}",
      "true_steps": [
        {
          "function": "Arrays",
          "operation": "push",
          "array": "{{search_conditions}}",
          "value": {
            "price": {
              ">=": "{{inputs.price_range.min}}",
              "<=": "{{inputs.price_range.max}}"
            }
          },
          "output_variable": "search_conditions"
        }
      ]
    },
    // Execute search with dynamic conditions
    {
      "function": "Query All Records",
      "table": "products",
      "filter": "{{search_conditions | combine_with_and}}",
      "limit": "{{inputs.limit || 20}}",
      "offset": "{{inputs.offset || 0}}",
      "output_variable": "products"
    },
    // Enrich with related data
    {
      "function": "Loop",
      "input_array": "{{products}}",
      "loop_item_variable": "product",
      "steps": [
        {
          "function": "Get Record",
          "table": "categories",
          "record_id": "{{product.category_id}}",
          "output_variable": "category"
        },
        {
          "function": "Query All Records",
          "table": "product_images",
          "filter": {
            "product_id": "{{product.id}}"
          },
          "limit": 3,
          "output_variable": "images"
        },
        {
          "function": "Objects",
          "operation": "merge",
          "object1": "{{product}}",
          "object2": {
            "category": "{{category}}",
            "images": "{{images}}"
          },
          "output_variable": "enriched_product"
        }
      ]
    },
    {
      "function": "Response",
      "body": {
        "products": "{{loop_results}}",
        "total_found": "{{products.length}}",
        "search_criteria": "{{inputs}}"
      }
    }
  ]
}
```

## 🔗 **Integration Examples**

### n8n API Integration

```javascript
// n8n workflow calling Xano API
{
  "workflow_name": "Product Management",
  "trigger": {
    "type": "Webhook",
    "path": "product-update"
  },
  "nodes": [
    {
      "name": "Validate Product Data",
      "type": "Code",
      "code": `
        const product = $input.first().json;
        if (!product.name || !product.price) {
          throw new Error('Missing required product fields');
        }
        return { product };
      `
    },
    {
      "name": "Update Product in Xano",
      "type": "HTTP Request",
      "parameters": {
        "method": "PATCH",
        "url": "https://your-xano.xano.io/api:v1/products/{{$json.product.id}}",
        "headers": {
          "Authorization": "Bearer {{$credentials.xanoApi.token}}",
          "Content-Type": "application/json"
        },
        "body": {
          "name": "={{$json.product.name}}",
          "price": "={{$json.product.price}}",
          "updated_by": "n8n_automation"
        }
      }
    },
    {
      "name": "Sync to External Systems",
      "type": "HTTP Request",
      "parameters": {
        "method": "POST",
        "url": "https://your-xano.xano.io/api:v1/products/sync-external",
        "body": {
          "product_id": "={{$json.id}}",
          "systems": ["shopify", "stripe", "mailchimp"]
        }
      }
    }
  ]
}

// Corresponding Xano sync endpoint
{
  "endpoint": "/products/sync-external",
  "method": "POST",
  "function_stack": [
    {
      "function": "Get Record",
      "table": "products",
      "record_id": "{{inputs.product_id}}",
      "output_variable": "product"
    },
    {
      "function": "Loop",
      "input_array": "{{inputs.systems}}",
      "loop_item_variable": "system",
      "parallel": true,
      "steps": [
        {
          "function": "Custom Function",
          "custom_function": "sync_to_{{system}}",
          "execution_mode": "async",
          "parameters": {
            "product": "{{product}}"
          }
        }
      ]
    },
    {
      "function": "Response",
      "body": {
        "message": "Sync initiated for {{inputs.systems.length}} systems",
        "product_id": "{{inputs.product_id}}"
      }
    }
  ]
}
```

### WeWeb Data Collection Integration

```javascript
// WeWeb collection configuration
{
  "collection_name": "Products",
  "data_source": {
    "type": "rest_api",
    "base_url": "https://your-xano.xano.io/api:v1",
    "endpoints": {
      "list": {
        "method": "GET",
        "path": "/products",
        "cache_duration": 300
      },
      "create": {
        "method": "POST",
        "path": "/products"
      },
      "update": {
        "method": "PATCH",
        "path": "/products/{id}"
      },
      "delete": {
        "method": "DELETE",
        "path": "/products/{id}"
      }
    }
  },
  "headers": {
    "Authorization": "Bearer {{globals.authToken}}",
    "Content-Type": "application/json"
  },
  "auto_pagination": true,
  "real_time_updates": true
}

// WeWeb component using the collection
{
  "component_name": "ProductList",
  "data_binding": {
    "products": "{{collections.Products.data}}",
    "loading": "{{collections.Products.loading}}",
    "error": "{{collections.Products.error}}"
  },
  "methods": {
    "createProduct": `
      const newProduct = {
        name: this.form.name,
        price: this.form.price,
        description: this.form.description
      };
      
      await this.$collections.Products.create(newProduct);
      this.showForm = false;
      this.$toast.success('Product created successfully');
    `,
    "updateProduct": `
      await this.$collections.Products.update(productId, updatedData);
      this.$toast.success('Product updated successfully');
    `
  }
}
```

## 🚀 **Advanced API Patterns**

### Authentication Endpoints

```javascript
// Complete authentication system
{
  "auth_endpoints": {
    "register": {
      "endpoint": "/auth/register",
      "method": "POST",
      "function_stack": [
        {
          "function": "Text",
          "operation": "lowercase",
          "text": "{{inputs.email}}",
          "output_variable": "email"
        },
        {
          "function": "Query All Records",
          "table": "users",
          "filter": {"email": "{{email}}"},
          "output_variable": "existing_users"
        },
        {
          "function": "Conditional",
          "condition": "{{existing_users.length > 0}}",
          "true_steps": [
            {
              "function": "Response",
              "status_code": 409,
              "body": {"error": "Email already registered"}
            }
          ]
        },
        {
          "function": "Add Record",
          "table": "users",
          "data": {
            "email": "{{email}}",
            "password": "{{inputs.password | hash}}",
            "first_name": "{{inputs.first_name}}",
            "last_name": "{{inputs.last_name}}",
            "role": "user",
            "status": "active"
          },
          "output_variable": "new_user"
        },
        {
          "function": "Custom Function",
          "custom_function": "generate_auth_token",
          "parameters": {"user_id": "{{new_user.id}}"},
          "output_variable": "auth_token"
        },
        {
          "function": "Response",
          "status_code": 201,
          "body": {
            "user": {
              "id": "{{new_user.id}}",
              "email": "{{new_user.email}}",
              "name": "{{new_user.first_name}} {{new_user.last_name}}"
            },
            "auth_token": "{{auth_token}}"
          }
        }
      ]
    },
    "login": {
      "endpoint": "/auth/login",
      "method": "POST",
      "function_stack": [
        {
          "function": "Query All Records",
          "table": "users",
          "filter": {
            "email": "{{inputs.email | lowercase}}",
            "status": "active"
          },
          "limit": 1,
          "output_variable": "users"
        },
        {
          "function": "Conditional",
          "condition": "{{users.length === 0}}",
          "true_steps": [
            {
              "function": "Response",
              "status_code": 401,
              "body": {"error": "Invalid credentials"}
            }
          ]
        },
        {
          "function": "Create Variable",
          "variable_name": "user",
          "value": "{{users[0]}}"
        },
        {
          "function": "Conditional",
          "condition": "{{!verify_password(inputs.password, user.password)}}",
          "true_steps": [
            {
              "function": "Response",
              "status_code": 401,
              "body": {"error": "Invalid credentials"}
            }
          ]
        },
        {
          "function": "Edit Record",
          "table": "users",
          "record_id": "{{user.id}}",
          "data": {"last_login_at": "{{timestamp}}"}
        },
        {
          "function": "Custom Function",
          "custom_function": "generate_auth_token",
          "parameters": {"user_id": "{{user.id}}"},
          "output_variable": "auth_token"
        },
        {
          "function": "Response",
          "body": {
            "user": {
              "id": "{{user.id}}",
              "email": "{{user.email}}",
              "name": "{{user.first_name}} {{user.last_name}}",
              "role": "{{user.role}}"
            },
            "auth_token": "{{auth_token}}"
          }
        }
      ]
    }
  }
}
```

### File Upload Endpoints

```javascript
// Multi-file upload with processing
{
  "endpoint": "/files/upload",
  "method": "POST",
  "function_stack": [
    {
      "function": "Create Variable",
      "variable_name": "uploaded_files",
      "value": []
    },
    {
      "function": "Loop",
      "input_array": "{{inputs.files}}",
      "loop_item_variable": "file",
      "steps": [
        // Validate file
        {
          "function": "Conditional",
          "condition": "{{file.size > 10485760}}", // 10MB
          "true_steps": [
            {
              "function": "Response",
              "status_code": 400,
              "body": {
                "error": "File too large",
                "filename": "{{file.name}}"
              }
            }
          ]
        },
        // Upload to file storage
        {
          "function": "File Storage",
          "operation": "upload",
          "file": "{{file}}",
          "folder": "{{inputs.folder || 'uploads'}}",
          "output_variable": "uploaded_file"
        },
        // Create database record
        {
          "function": "Add Record",
          "table": "files",
          "data": {
            "filename": "{{uploaded_file.filename}}",
            "original_name": "{{file.name}}",
            "size": "{{file.size}}",
            "mime_type": "{{file.type}}",
            "url": "{{uploaded_file.url}}",
            "folder": "{{inputs.folder || 'uploads'}}",
            "uploaded_by": "{{auth_user.id}}",
            "uploaded_at": "{{timestamp}}"
          },
          "output_variable": "file_record"
        },
        // Process image files
        {
          "function": "Conditional",
          "condition": "{{file.type | starts_with:'image/'}}",
          "true_steps": [
            {
              "function": "Custom Function",
              "custom_function": "generate_image_thumbnails",
              "execution_mode": "async",
              "parameters": {
                "file_id": "{{file_record.id}}",
                "source_url": "{{uploaded_file.url}}"
              }
            }
          ]
        },
        {
          "function": "Arrays",
          "operation": "push",
          "array": "{{uploaded_files}}",
          "value": "{{file_record}}",
          "output_variable": "uploaded_files"
        }
      ]
    },
    {
      "function": "Response",
      "body": {
        "message": "Files uploaded successfully",
        "files": "{{uploaded_files}}",
        "count": "{{uploaded_files.length}}"
      }
    }
  ]
}
```

### Pagination & Filtering

```javascript
// Advanced pagination and filtering endpoint
{
  "endpoint": "/orders",
  "method": "GET",
  "function_stack": [
    // Set up pagination defaults
    {
      "function": "Create Variable",
      "variable_name": "page",
      "value": "{{inputs.page || 1}}"
    },
    {
      "function": "Create Variable",
      "variable_name": "per_page",
      "value": "{{inputs.per_page || 20}}"
    },
    {
      "function": "Math",
      "operation": "multiply",
      "value1": "{{page - 1}}",
      "value2": "{{per_page}}",
      "output_variable": "offset"
    },
    // Build dynamic filters
    {
      "function": "Create Variable",
      "variable_name": "filters",
      "value": {}
    },
    {
      "function": "Conditional",
      "condition": "{{inputs.status !== null}}",
      "true_steps": [
        {
          "function": "Objects",
          "operation": "set",
          "object": "{{filters}}",
          "key": "status",
          "value": "{{inputs.status}}",
          "output_variable": "filters"
        }
      ]
    },
    {
      "function": "Conditional",
      "condition": "{{inputs.date_range !== null}}",
      "true_steps": [
        {
          "function": "Objects",
          "operation": "set",
          "object": "{{filters}}",
          "key": "created_at",
          "value": {
            ">=": "{{inputs.date_range.start}}",
            "<=": "{{inputs.date_range.end}}"
          },
          "output_variable": "filters"
        }
      ]
    },
    // Get total count for pagination
    {
      "function": "Query All Records",
      "table": "orders",
      "filter": "{{filters}}",
      "count_only": true,
      "output_variable": "total_count"
    },
    // Get paginated results
    {
      "function": "Query All Records",
      "table": "orders",
      "filter": "{{filters}}",
      "limit": "{{per_page}}",
      "offset": "{{offset}}",
      "sort": [{"created_at": "desc"}],
      "output_variable": "orders"
    },
    // Calculate pagination metadata
    {
      "function": "Math",
      "operation": "ceiling",
      "value1": "{{total_count}}",
      "value2": "{{per_page}}",
      "output_variable": "total_pages"
    },
    {
      "function": "Response",
      "body": {
        "data": "{{orders}}",
        "pagination": {
          "current_page": "{{page}}",
          "per_page": "{{per_page}}",
          "total_items": "{{total_count}}",
          "total_pages": "{{total_pages}}",
          "has_next": "{{page < total_pages}}",
          "has_prev": "{{page > 1}}"
        },
        "filters_applied": "{{filters}}"
      }
    }
  ]
}
```

## 📊 **API Design Best Practices**

### RESTful URL Design

```javascript
// URL design patterns
{
  "url_patterns": {
    "resource_collections": {
      "pattern": "/resources",
      "examples": ["/users", "/products", "/orders"],
      "methods": ["GET (list)", "POST (create)"]
    },
    "specific_resources": {
      "pattern": "/resources/{id}",
      "examples": ["/users/123", "/products/456"],
      "methods": ["GET (read)", "PATCH/PUT (update)", "DELETE (remove)"]
    },
    "nested_resources": {
      "pattern": "/resources/{id}/subresources",
      "examples": ["/users/123/orders", "/products/456/reviews"],
      "methods": ["GET (list)", "POST (create)"]
    },
    "actions_on_resources": {
      "pattern": "/resources/{id}/action",
      "examples": ["/orders/123/cancel", "/users/456/activate"],
      "methods": ["POST (perform action)"]
    },
    "search_and_filtering": {
      "pattern": "/resources/search",
      "examples": ["/products/search", "/users/search"],
      "methods": ["GET", "POST (complex queries)"]
    }
  }
}
```

### Response Formatting

```javascript
// Consistent response formats
{
  "response_formats": {
    "success_response": {
      "status_code": 200,
      "body": {
        "success": true,
        "data": "{{actual_data}}",
        "message": "Operation completed successfully"
      }
    },
    "error_response": {
      "status_code": 400,
      "body": {
        "success": false,
        "error": {
          "code": "VALIDATION_ERROR",
          "message": "Invalid input provided",
          "details": [
            "Email is required",
            "Password must be at least 8 characters"
          ]
        }
      }
    },
    "paginated_response": {
      "status_code": 200,
      "body": {
        "success": true,
        "data": ["...array of items..."],
        "meta": {
          "pagination": {
            "current_page": 1,
            "per_page": 20,
            "total": 100,
            "total_pages": 5
          }
        }
      }
    }
  }
}
```

### Error Handling

```javascript
// Comprehensive error handling
{
  "error_handling_pattern": [
    {
      "function": "Try-Catch",
      "try_steps": [
        "...main API logic..."
      ],
      "catch_steps": [
        {
          "function": "Switch",
          "variable": "{{error.type}}",
          "cases": {
            "validation_error": [
              {
                "function": "Response",
                "status_code": 400,
                "body": {
                  "error": "Invalid input",
                  "details": "{{error.details}}"
                }
              }
            ],
            "not_found": [
              {
                "function": "Response",
                "status_code": 404,
                "body": {
                  "error": "Resource not found"
                }
              }
            ],
            "permission_denied": [
              {
                "function": "Response",
                "status_code": 403,
                "body": {
                  "error": "Insufficient permissions"
                }
              }
            ]
          },
          "default": [
            {
              "function": "Add Record",
              "table": "error_logs",
              "data": {
                "endpoint": "{{request.endpoint}}",
                "error": "{{error}}",
                "timestamp": "{{timestamp}}"
              }
            },
            {
              "function": "Response",
              "status_code": 500,
              "body": {
                "error": "Internal server error"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## 🔒 **Security & CORS**

### CORS Configuration

```javascript
// CORS settings for different environments
{
  "cors_configurations": {
    "development": {
      "allow_origins": ["http://localhost:3000", "http://localhost:8080"],
      "allow_methods": ["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
      "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
      "allow_credentials": true,
      "max_age": 3600
    },
    "production": {
      "allow_origins": [
        "https://your-frontend.com",
        "https://admin.your-frontend.com"
      ],
      "allow_methods": ["GET", "POST", "PATCH", "DELETE"],
      "allow_headers": ["Content-Type", "Authorization"],
      "allow_credentials": true,
      "max_age": 86400
    }
  }
}
```

### API Security Implementation

```javascript
// Security middleware patterns
{
  "security_middleware": {
    "authentication_check": [
      {
        "function": "Conditional",
        "condition": "{{request.headers.authorization === null}}",
        "true_steps": [
          {
            "function": "Response",
            "status_code": 401,
            "body": {"error": "Authentication required"}
          }
        ]
      },
      {
        "function": "Custom Function",
        "custom_function": "verify_auth_token",
        "parameters": {
          "token": "{{request.headers.authorization | remove:'Bearer '}}"
        },
        "output_variable": "auth_user"
      }
    ],
    "rate_limiting": [
      {
        "function": "Custom Function",
        "custom_function": "check_rate_limit",
        "parameters": {
          "ip": "{{request.ip}}",
          "endpoint": "{{request.endpoint}}"
        },
        "output_variable": "rate_limit_status"
      },
      {
        "function": "Conditional",
        "condition": "{{rate_limit_status.exceeded}}",
        "true_steps": [
          {
            "function": "Response",
            "status_code": 429,
            "headers": {
              "X-RateLimit-Reset": "{{rate_limit_status.reset_time}}"
            },
            "body": {"error": "Rate limit exceeded"}
          }
        ]
      }
    ]
  }
}
```

---

*Well-designed APIs serve as the backbone of modern applications, enabling seamless integration between different systems and providing the foundation for scalable, maintainable software architecture.*