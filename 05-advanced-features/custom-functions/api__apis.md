---
title: API Design and Implementation - Building RESTful Endpoints in Xano
description: Complete guide to designing, building, and managing APIs in Xano including CRUD operations, authentication, CORS configuration, and best practices for scalable API architecture
category: custom-functions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - custom-functions.md
  - building-with-visual-development.md
  - authentication.md
subcategory: 05-advanced-features/custom-functions
tags:
  - api-design
  - crud-operations
  - rest-api
  - endpoints
  - api-groups
  - cors
  - no-code
---

## 📋 **Quick Summary**

APIs are the backbone of modern applications, enabling communication between different systems and services. Learn how to design and build robust, scalable APIs in Xano including CRUD operations, authentication, file uploads, and custom endpoints. Perfect for creating backends that integrate seamlessly with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- API fundamentals and RESTful design principles
- Creating and organizing API groups and endpoints
- Implementing CRUD operations with auto-generation
- Configuring authentication and security
- CORS management and external access control
- Advanced API patterns and best practices

# API Design and Implementation

## Overview

**APIs (Application Programming Interfaces)** act as intermediaries that allow different software applications to communicate with each other. In Xano, APIs are organized into groups and can be automatically generated for common operations or custom-built for specific business logic.

### API Analogy

Think of an API like a waiter in a restaurant:
- **You (the client)** place an order with specific requirements
- **The waiter (the API)** takes your order to the kitchen
- **The kitchen (the backend)** prepares what you requested
- **The waiter returns** with exactly what you ordered

This seamless communication enables applications to work together without knowing each other's internal workings.

## 🚀 **API Components and Structure**

### Essential API Components

**1. HTTP Methods (Verbs):**
```javascript
// RESTful API method conventions
{
  "GET": "Retrieve data - safe and idempotent",
  "POST": "Create new resources - not idempotent", 
  "PUT": "Update/replace entire resource - idempotent",
  "PATCH": "Partial update - idempotent",
  "DELETE": "Remove resource - idempotent"
}
```

**2. Headers:**
```javascript
// Common API headers
{
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "Accept": "application/json",
  "User-Agent": "MyApp/1.0",
  "X-API-Version": "v1"
}
```

**3. Request Body/Query Parameters:**
```javascript
// Query parameters (typically for GET requests)
GET /api/users?page=2&limit=10&sort=created_at&filter=active

// Request body (typically for POST/PUT/PATCH)
POST /api/users
{
  "email": "user@example.com",
  "profile": {
    "first_name": "John",
    "last_name": "Doe"
  },
  "preferences": {
    "notifications": true
  }
}
```

**4. Response Structure:**
```javascript
// Successful response
{
  "status": 200,
  "data": {
    "id": 123,
    "email": "user@example.com",
    "created_at": "2024-01-15T10:30:00Z"
  },
  "meta": {
    "total": 1,
    "page": 1
  }
}

// Error response
{
  "status": 400,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      {
        "field": "email",
        "message": "This field is required"
      }
    ]
  }
}
```

## 🔗 **No-Code Platform Integration**

### n8n API Workflow Integration

**Complete CRUD Operations with n8n:**

```javascript
// n8n workflow for user management
{
  "nodes": [
    {
      "name": "Create User",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/users",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $json.auth_token }}",
          "Content-Type": "application/json"
        },
        "body": {
          "email": "{{ $json.user_email }}",
          "profile": {
            "first_name": "{{ $json.first_name }}",
            "last_name": "{{ $json.last_name }}"
          }
        }
      }
    },
    {
      "name": "Get User",
      "type": "HTTP Request", 
      "parameters": {
        "url": "https://your-xano-instance.com/api/users/{{ $json.user_id }}",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $json.auth_token }}"
        }
      }
    },
    {
      "name": "Update User",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/users/{{ $json.user_id }}",
        "method": "PATCH",
        "headers": {
          "Authorization": "Bearer {{ $json.auth_token }}",
          "Content-Type": "application/json"
        },
        "body": {
          "profile": {
            "phone": "{{ $json.phone_number }}"
          }
        }
      }
    },
    {
      "name": "Delete User",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/users/{{ $json.user_id }}",
        "method": "DELETE",
        "headers": {
          "Authorization": "Bearer {{ $json.auth_token }}"
        }
      }
    }
  ]
}
```

### WeWeb API Service Integration

**Comprehensive API Service Layer:**

```javascript
// WeWeb API service for Xano integration
class XanoAPIService {
  constructor(baseUrl, authToken = null) {
    this.baseUrl = baseUrl;
    this.authToken = authToken;
  }
  
  // Authentication methods
  async login(email, password) {
    try {
      const response = await fetch(`${this.baseUrl}/api/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: email,
          password: password
        })
      });
      
      const result = await response.json();
      
      if (response.ok) {
        this.authToken = result.authToken;
        wwLib.wwVariable.updateValue('auth_token', result.authToken);
        wwLib.wwVariable.updateValue('current_user', result.user);
        return result;
      } else {
        throw new Error(result.message || 'Login failed');
      }
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  }
  
  // Generic CRUD operations
  async create(endpoint, data) {
    return this.makeRequest(endpoint, 'POST', data);
  }
  
  async read(endpoint, params = {}) {
    const queryString = new URLSearchParams(params).toString();
    const url = queryString ? `${endpoint}?${queryString}` : endpoint;
    return this.makeRequest(url, 'GET');
  }
  
  async update(endpoint, data) {
    return this.makeRequest(endpoint, 'PATCH', data);
  }
  
  async delete(endpoint) {
    return this.makeRequest(endpoint, 'DELETE');
  }
  
  // Generic request method
  async makeRequest(endpoint, method, data = null) {
    try {
      const url = `${this.baseUrl}/api/${endpoint.replace(/^\//, '')}`;
      
      const options = {
        method: method,
        headers: {
          'Content-Type': 'application/json'
        }
      };
      
      if (this.authToken) {
        options.headers['Authorization'] = `Bearer ${this.authToken}`;
      }
      
      if (data && ['POST', 'PUT', 'PATCH'].includes(method)) {
        options.body = JSON.stringify(data);
      }
      
      const response = await fetch(url, options);
      const result = await response.json();
      
      if (!response.ok) {
        throw new Error(result.message || `HTTP ${response.status}`);
      }
      
      return result;
    } catch (error) {
      console.error(`API ${method} ${endpoint} error:`, error);
      throw error;
    }
  }
  
  // Specialized methods
  async getUsers(page = 1, limit = 10, filters = {}) {
    const params = {
      page: page,
      limit: limit,
      ...filters
    };
    
    return this.read('users', params);
  }
  
  async createUser(userData) {
    const user = await this.create('users', userData);
    wwLib.wwVariable.updateValue('latest_created_user', user);
    return user;
  }
  
  async updateUser(userId, updates) {
    const user = await this.update(`users/${userId}`, updates);
    
    // Update current user if it's the same user
    const currentUser = wwLib.wwVariable.getValue('current_user');
    if (currentUser && currentUser.id === userId) {
      wwLib.wwVariable.updateValue('current_user', { ...currentUser, ...user });
    }
    
    return user;
  }
  
  async uploadFile(file, metadata = {}) {
    try {
      const formData = new FormData();
      formData.append('file', file);
      
      Object.keys(metadata).forEach(key => {
        formData.append(key, metadata[key]);
      });
      
      const response = await fetch(`${this.baseUrl}/api/upload`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`
        },
        body: formData
      });
      
      const result = await response.json();
      
      if (!response.ok) {
        throw new Error(result.message || 'Upload failed');
      }
      
      return result;
    } catch (error) {
      console.error('File upload error:', error);
      throw error;
    }
  }
}

// Initialize API service
const api = new XanoAPIService(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage examples in WeWeb
async function handleUserRegistration() {
  try {
    const userData = {
      email: wwLib.wwVariable.getValue('registration_email'),
      password: wwLib.wwVariable.getValue('registration_password'),
      profile: {
        first_name: wwLib.wwVariable.getValue('first_name'),
        last_name: wwLib.wwVariable.getValue('last_name')
      }
    };
    
    const newUser = await api.createUser(userData);
    
    wwLib.wwUtils.showSuccessToast('Account created successfully!');
    wwLib.wwUtils.navigateTo('/welcome');
  } catch (error) {
    wwLib.wwUtils.showErrorToast(`Registration failed: ${error.message}`);
  }
}

async function loadUserList() {
  try {
    const page = wwLib.wwVariable.getValue('current_page') || 1;
    const searchTerm = wwLib.wwVariable.getValue('search_term') || '';
    
    const result = await api.getUsers(page, 10, {
      search: searchTerm,
      status: 'active'
    });
    
    wwLib.wwVariable.updateValue('users_list', result.data);
    wwLib.wwVariable.updateValue('total_users', result.meta.total);
    wwLib.wwVariable.updateValue('current_page', result.meta.page);
  } catch (error) {
    wwLib.wwUtils.showErrorToast(`Failed to load users: ${error.message}`);
  }
}
```

## 🛠️ **API Groups and Organization**

### API Group Configuration

**Production-Ready API Group Setup:**

```javascript
// API Group configuration
{
  "name": "User Management",
  "description": "Complete user lifecycle management APIs",
  "canonical_id": "users",
  "tags": ["authentication", "user-management", "core"],
  "settings": {
    "swagger": {
      "access": "private",
      "token_required": true,
      "version": "v1"
    },
    "cors": {
      "mode": "custom",
      "allow_credentials": true,
      "allow_methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
      "allow_origins": [
        "https://yourdomain.com",
        "https://app.yourdomain.com",
        "https://admin.yourdomain.com"
      ],
      "allow_headers": [
        "Authorization",
        "Content-Type",
        "Accept",
        "X-Requested-With",
        "X-API-Version"
      ],
      "max_age": 3600
    },
    "request_history": {
      "enabled": true,
      "retention_days": 30,
      "log_level": "info"
    },
    "external_access": true
  }
}
```

### Multi-Environment API Management

**Development, Staging, and Production Setup:**

```javascript
// Environment-specific API configurations
{
  "development": {
    "base_url": "https://dev-instance.xano.com",
    "cors": {
      "mode": "default", // Allow all for development
      "allow_origins": ["*"]
    },
    "rate_limiting": {
      "enabled": false
    },
    "debug_mode": true
  },
  "staging": {
    "base_url": "https://staging-instance.xano.com", 
    "cors": {
      "mode": "custom",
      "allow_origins": [
        "https://staging.yourdomain.com",
        "https://test.yourdomain.com"
      ]
    },
    "rate_limiting": {
      "enabled": true,
      "requests_per_minute": 1000
    },
    "debug_mode": false
  },
  "production": {
    "base_url": "https://prod-instance.xano.com",
    "cors": {
      "mode": "custom",
      "allow_origins": [
        "https://yourdomain.com",
        "https://app.yourdomain.com"
      ]
    },
    "rate_limiting": {
      "enabled": true,
      "requests_per_minute": 500
    },
    "debug_mode": false,
    "monitoring": {
      "error_tracking": true,
      "performance_monitoring": true
    }
  }
}
```

## 📋 **CRUD Operations and Auto-Generation**

### Automated CRUD Endpoint Generation

**Complete User Management CRUD:**

```javascript
// Auto-generated CRUD endpoints for users table
{
  "endpoints": [
    {
      "name": "Get All Users",
      "method": "GET",
      "path": "/users",
      "description": "Retrieve paginated list of users with filtering",
      "query_parameters": {
        "page": {"type": "integer", "default": 1},
        "limit": {"type": "integer", "default": 10, "max": 100},
        "search": {"type": "text", "description": "Search in name and email"},
        "status": {"type": "text", "enum": ["active", "inactive", "pending"]},
        "sort": {"type": "text", "default": "created_at", "enum": ["name", "email", "created_at"]}
      }
    },
    {
      "name": "Get User by ID", 
      "method": "GET",
      "path": "/users/{id}",
      "description": "Retrieve specific user by ID",
      "path_parameters": {
        "id": {"type": "integer", "required": true}
      }
    },
    {
      "name": "Create User",
      "method": "POST", 
      "path": "/users",
      "description": "Create new user account",
      "request_body": {
        "email": {"type": "email", "required": true},
        "password": {"type": "text", "required": true, "min_length": 8},
        "profile": {
          "type": "object",
          "properties": {
            "first_name": {"type": "text", "required": true},
            "last_name": {"type": "text", "required": true},
            "phone": {"type": "text", "required": false}
          }
        }
      }
    },
    {
      "name": "Update User",
      "method": "PATCH",
      "path": "/users/{id}",
      "description": "Partial update of user information",
      "path_parameters": {
        "id": {"type": "integer", "required": true}
      },
      "request_body": {
        "profile": {
          "type": "object",
          "properties": {
            "first_name": {"type": "text"},
            "last_name": {"type": "text"},
            "phone": {"type": "text"}
          }
        },
        "preferences": {
          "type": "object",
          "properties": {
            "notifications": {"type": "boolean"},
            "newsletter": {"type": "boolean"}
          }
        }
      }
    },
    {
      "name": "Delete User",
      "method": "DELETE",
      "path": "/users/{id}",
      "description": "Soft delete user account",
      "path_parameters": {
        "id": {"type": "integer", "required": true}
      }
    }
  ]
}
```

### Custom Function Stack Implementation

**Advanced User Creation with Validation:**

```javascript
// Custom user creation function stack
[
  {
    "function": "create_variable",
    "name": "validation_errors",
    "value": []
  },
  {
    "function": "conditional",
    "condition": "{{ !request.body.email || !request.body.email|is_email }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_errors",
        "operation": "append",
        "value": {"field": "email", "message": "Valid email is required"}
      }
    ]
  },
  {
    "function": "query_single_record",
    "table": "users",
    "filter": {"email": "{{ request.body.email }}"},
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
        "value": {"field": "email", "message": "Email already exists"}
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ validation_errors|length > 0 }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {
          "error": "Validation failed",
          "details": "{{ validation_errors }}"
        }
      }
    ]
  },
  {
    "function": "hash_password",
    "password": "{{ request.body.password }}",
    "return_as": "hashed_password"
  },
  {
    "function": "add_record",
    "table": "users",
    "data": {
      "email": "{{ request.body.email|trim|lower }}",
      "password": "{{ hashed_password }}",
      "status": "active",
      "email_verified": false
    },
    "return_as": "new_user"
  },
  {
    "function": "add_record",
    "table": "user_profiles",
    "data": {
      "user_id": "{{ new_user.id }}",
      "first_name": "{{ request.body.profile.first_name|trim }}",
      "last_name": "{{ request.body.profile.last_name|trim }}",
      "phone": "{{ request.body.profile.phone|trim }}"
    },
    "return_as": "user_profile"
  },
  {
    "function": "run_task",
    "task": "send_welcome_email",
    "context": {
      "user_id": "{{ new_user.id }}",
      "email": "{{ new_user.email }}",
      "name": "{{ user_profile.first_name }}"
    }
  },
  {
    "function": "return_response",
    "status": 201,
    "body": {
      "id": "{{ new_user.id }}",
      "email": "{{ new_user.email }}",
      "profile": "{{ user_profile }}",
      "created_at": "{{ new_user.created_at }}"
    }
  }
]
```

## 🔐 **Authentication and Security**

### JWT Authentication Implementation

**Complete Authentication Flow:**

```javascript
// Login endpoint function stack
[
  {
    "function": "create_variable",
    "name": "login_attempt",
    "value": {
      "email": "{{ request.body.email|trim|lower }}",
      "timestamp": "{{ now }}",
      "ip_address": "{{ request.headers['x-forwarded-for'] || request.ip }}"
    }
  },
  {
    "function": "query_single_record",
    "table": "users",
    "filter": {
      "email": "{{ login_attempt.email }}",
      "status": "active"
    },
    "return_as": "user"
  },
  {
    "function": "conditional",
    "condition": "{{ !user }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 401,
        "body": {"error": "Invalid credentials"}
      }
    ]
  },
  {
    "function": "verify_password",
    "password": "{{ request.body.password }}",
    "hash": "{{ user.password }}",
    "return_as": "password_valid"
  },
  {
    "function": "conditional",
    "condition": "{{ !password_valid }}",
    "true_branch": [
      {
        "function": "add_record",
        "table": "login_attempts",
        "data": {
          "user_id": "{{ user.id }}",
          "success": false,
          "ip_address": "{{ login_attempt.ip_address }}",
          "attempted_at": "{{ login_attempt.timestamp }}"
        }
      },
      {
        "function": "return_response",
        "status": 401,
        "body": {"error": "Invalid credentials"}
      }
    ]
  },
  {
    "function": "create_auth_token",
    "user_id": "{{ user.id }}",
    "expires_in": 86400,
    "return_as": "auth_token"
  },
  {
    "function": "add_record",
    "table": "login_attempts",
    "data": {
      "user_id": "{{ user.id }}",
      "success": true,
      "ip_address": "{{ login_attempt.ip_address }}",
      "attempted_at": "{{ login_attempt.timestamp }}"
    }
  },
  {
    "function": "edit_record",
    "table": "users",
    "id": "{{ user.id }}",
    "data": {
      "last_login": "{{ now }}",
      "login_count": "{{ user.login_count + 1 }}"
    }
  },
  {
    "function": "return_response",
    "status": 200,
    "body": {
      "authToken": "{{ auth_token }}",
      "user": {
        "id": "{{ user.id }}",
        "email": "{{ user.email }}",
        "last_login": "{{ now }}"
      },
      "expires_in": 86400
    }
  }
]
```

### API Key Authentication

**API Key Management System:**

```javascript
// API key validation middleware
[
  {
    "function": "create_variable",
    "name": "api_key",
    "value": "{{ request.headers['x-api-key'] || request.query.api_key }}"
  },
  {
    "function": "conditional",
    "condition": "{{ !api_key }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 401,
        "body": {"error": "API key required"}
      }
    ]
  },
  {
    "function": "query_single_record",
    "table": "api_keys",
    "filter": {
      "key": "{{ api_key }}",
      "status": "active",
      "expires_at": {"$gt": "{{ now }}"}
    },
    "return_as": "valid_key"
  },
  {
    "function": "conditional",
    "condition": "{{ !valid_key }}",
    "true_branch": [
      {
        "function": "return_response", 
        "status": 401,
        "body": {"error": "Invalid or expired API key"}
      }
    ]
  },
  {
    "function": "edit_record",
    "table": "api_keys",
    "id": "{{ valid_key.id }}",
    "data": {
      "last_used": "{{ now }}",
      "usage_count": "{{ valid_key.usage_count + 1 }}"
    }
  },
  {
    "function": "create_variable",
    "name": "authenticated_client",
    "value": "{{ valid_key.client_info }}"
  }
]
```

## 💡 **Pro Tips**

- **Follow RESTful Conventions**: Use standard HTTP methods and status codes consistently
- **Implement Pagination**: Always paginate list endpoints to prevent performance issues
- **Version Your APIs**: Include version numbers in URLs or headers for backward compatibility
- **Document Everything**: Maintain comprehensive API documentation with examples
- **Monitor Usage**: Track API usage patterns to optimize performance and detect issues
- **Implement Rate Limiting**: Protect your APIs from abuse with appropriate rate limiting

## 🔧 **Troubleshooting**

### Common API Issues

**Problem**: CORS errors when calling APIs from frontend  
**Solution**: Configure CORS settings in API group to allow your frontend domain

**Problem**: Authentication tokens not working  
**Solution**: Verify token format, expiration, and proper header format (`Bearer <token>`)

**Problem**: 404 errors on valid endpoints  
**Solution**: Check API group canonical ID and endpoint path configuration

**Problem**: Slow API response times  
**Solution**: Optimize database queries, implement caching, and review function stack complexity

---

**Next Steps**: Ready to build robust APIs? Check out [Custom Functions](custom-functions.md) for reusable logic or explore [Building with Visual Development](building-with-visual-development.md) for complete application architecture