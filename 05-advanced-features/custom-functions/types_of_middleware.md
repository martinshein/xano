---
title: Types of Middleware - Pre and Post Processing Architecture
description: Complete guide to middleware types in Xano including pre-middleware, post-middleware, configuration options, and integration patterns for no-code platforms
category: custom-functions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - custom-functions.md
  - building-with-visual-development.md
  - working-with-data.md
subcategory: 05-advanced-features/custom-functions
tags:
  - middleware
  - pre-processing
  - post-processing
  - validation
  - authentication
  - no-code
---

## 📋 **Quick Summary**

Middleware are separate function stacks that execute before or after your main API logic, providing powerful pre and post-processing capabilities. Perfect for input validation, authentication, logging, data transformation, and output customization across your entire application or specific endpoints. Essential for building robust applications with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Understanding pre-middleware and post-middleware execution flow
- Configuration options and exception handling patterns
- Advanced middleware patterns for authentication and validation
- Integration strategies for no-code platforms
- Performance optimization and best practices
- Real-world implementation examples

# Types of Middleware

## Overview

**Middleware** are function stacks that execute at specific points in your API request/response lifecycle. They provide a powerful way to implement cross-cutting concerns like authentication, validation, logging, and data transformation without duplicating code across multiple endpoints.

### Middleware Execution Flow

**Request Processing Order:**
1. **Pre-Middleware** → Input validation → **Main Function Stack** → **Post-Middleware** → Response

**Key Benefits:**
- **Code Reusability**: Apply logic across multiple endpoints
- **Separation of Concerns**: Keep authentication, validation, and business logic separate
- **Flexibility**: Apply at workspace, API group, or individual API levels
- **Consistency**: Ensure uniform behavior across your application

## 🔄 **Pre-Middleware**

### Execution Context

**Pre-middleware executes before any input validation and main function stack processing:**

**Timing:**
- Runs immediately after request received
- Executes before input validation
- Has access to raw request data
- Can modify or validate inputs before main processing

**Use Cases:**
- Authentication and authorization
- Input validation and sanitization
- Request logging and monitoring
- Data transformation and enrichment
- Rate limiting and throttling

### Basic Pre-Middleware Example

**Authentication Pre-Middleware:**

```javascript
// Pre-middleware for JWT authentication
[
  {
    "function": "create_variable",
    "name": "auth_result",
    "value": {
      "authenticated": false,
      "user": null,
      "error": null
    }
  },
  {
    "function": "conditional",
    "condition": "{{ !vars.authorization }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "auth_result",
        "operation": "merge",
        "value": {
          "error": "Authorization header missing",
          "authenticated": false
        }
      },
      {
        "function": "return_response",
        "status": 401,
        "body": {
          "error": "Authorization required",
          "code": "MISSING_AUTH_HEADER"
        }
      }
    ]
  },
  {
    "function": "create_variable",
    "name": "token",
    "value": "{{ vars.authorization|replace('Bearer ', '') }}"
  },
  {
    "function": "validate_jwt_token",
    "token": "{{ token }}",
    "return_as": "token_validation"
  },
  {
    "function": "conditional",
    "condition": "{{ !token_validation.valid }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 401,
        "body": {
          "error": "Invalid or expired token",
          "code": "INVALID_TOKEN"
        }
      }
    ]
  },
  {
    "function": "query_single_record",
    "table": "users",
    "filter": {"id": "{{ token_validation.user_id }}"},
    "return_as": "user"
  },
  {
    "function": "conditional",
    "condition": "{{ user.status != 'active' }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 403,
        "body": {
          "error": "Account is not active",
          "code": "ACCOUNT_INACTIVE"
        }
      }
    ]
  },
  {
    "function": "update_variable",
    "name": "auth_result",
    "operation": "merge",
    "value": {
      "authenticated": true,
      "user": "{{ user }}",
      "user_id": "{{ user.id }}"
    }
  },
  {
    "function": "return_response",
    "body": {
      "user_id": "{{ user.id }}",
      "user_role": "{{ user.role }}",
      "authenticated": true
    }
  }
]
```

### Input Validation Pre-Middleware

**Comprehensive Input Sanitization:**

```javascript
// Pre-middleware for input validation and sanitization
[
  {
    "function": "create_variable",
    "name": "validation_errors",
    "value": []
  },
  {
    "function": "create_variable",
    "name": "sanitized_inputs",
    "value": {}
  },
  // Email validation
  {
    "function": "conditional",
    "condition": "{{ vars.email && !vars.email|regex_matches('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$') }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_errors",
        "operation": "append",
        "value": "Invalid email format"
      }
    ]
  },
  // Text sanitization
  {
    "function": "conditional",
    "condition": "{{ vars.message }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "sanitized_inputs",
        "operation": "merge",
        "value": {
          "message": "{{ vars.message|strip_tags|trim }}"
        }
      }
    ]
  },
  // Password strength validation
  {
    "function": "conditional",
    "condition": "{{ vars.password && vars.password|length < 8 }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_errors",
        "operation": "append",
        "value": "Password must be at least 8 characters long"
      }
    ]
  },
  // Return validation errors if any
  {
    "function": "conditional",
    "condition": "{{ validation_errors|length > 0 }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {
          "error": "Validation failed",
          "errors": "{{ validation_errors }}",
          "code": "VALIDATION_ERROR"
        }
      }
    ]
  },
  // Return sanitized inputs
  {
    "function": "return_response",
    "body": "{{ sanitized_inputs|merge(vars) }}"
  }
]
```

## 🔄 **Post-Middleware**

### Execution Context

**Post-middleware executes after the main function stack but before the response is delivered:**

**Timing:**
- Runs after main function stack completion
- Executes before response sent to client
- Has access to API response data
- Can modify, enhance, or replace response

**Use Cases:**
- Response transformation and formatting
- Data filtering and security
- Logging and analytics
- Performance monitoring
- Error handling and reporting

### Basic Post-Middleware Example

**Response Enhancement Post-Middleware:**

```javascript
// Post-middleware for response enhancement and logging
[
  {
    "function": "create_variable",
    "name": "enhanced_response",
    "value": {
      "data": "{{ vars }}",
      "meta": {
        "timestamp": "{{ now }}",
        "api_version": "v1.0",
        "request_id": "{{ uuid }}"
      }
    }
  },
  {
    "function": "conditional",
    "condition": "{{ vars.error }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "enhanced_response",
        "operation": "merge",
        "value": {
          "success": false,
          "error_logged": true
        }
      },
      {
        "function": "external_api_request",
        "url": "{{ env.ERROR_LOGGING_WEBHOOK }}",
        "method": "POST",
        "body": {
          "error": "{{ vars.error }}",
          "timestamp": "{{ now }}",
          "api_endpoint": "{{ request.path }}",
          "user_id": "{{ auth.user.id }}"
        },
        "execution_mode": "async"
      }
    ],
    "false_branch": [
      {
        "function": "update_variable",
        "name": "enhanced_response",
        "operation": "merge",
        "value": {
          "success": true,
          "processing_time": "{{ now - request.timestamp }}"
        }
      }
    ]
  },
  {
    "function": "add_record",
    "table": "api_usage_logs",
    "data": {
      "endpoint": "{{ request.path }}",
      "method": "{{ request.method }}",
      "user_id": "{{ auth.user.id }}",
      "response_status": "{{ enhanced_response.success ? 'success' : 'error' }}",
      "processing_time": "{{ now - request.timestamp }}",
      "timestamp": "{{ now }}"
    },
    "execution_mode": "async"
  },
  {
    "function": "return_response",
    "body": "{{ enhanced_response }}"
  }
]
```

## 🔗 **No-Code Platform Integration**

### n8n Middleware Coordination

**Webhook Integration with Pre-Middleware:**

```javascript
// n8n workflow triggered by Xano pre-middleware
{
  "nodes": [
    {
      "name": "Xano Pre-Middleware Webhook",
      "type": "Webhook",
      "parameters": {
        "path": "xano-pre-validation",
        "httpMethod": "POST",
        "authentication": "headerAuth",
        "options": {}
      }
    },
    {
      "name": "External Validation Service",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.VALIDATION_SERVICE_URL }}/validate",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.VALIDATION_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "email": "{{ $json.email }}",
          "validation_type": "comprehensive",
          "check_disposable": true,
          "check_mx_record": true
        }
      }
    },
    {
      "name": "Process Validation Result",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const validationResult = $input.first().json;
          const originalData = $('Xano Pre-Middleware Webhook').first().json;
          
          // Determine if validation passed
          const isValid = validationResult.valid && validationResult.deliverable;
          
          // Create response for Xano
          const response = {
            validation_passed: isValid,
            email: originalData.email,
            validation_details: {
              is_disposable: validationResult.is_disposable,
              mx_found: validationResult.mx_found,
              syntax_valid: validationResult.syntax.valid,
              risk_score: validationResult.risk_score
            }
          };
          
          if (!isValid) {
            response.error = 'Email validation failed';
            response.error_details = validationResult.errors || [];
          }
          
          return [{ json: response }];
        `
      }
    },
    {
      "name": "Return to Xano",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.XANO_CALLBACK_URL }}/validation-result",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": "{{ $json }}"
      }
    }
  ]
}
```

### WeWeb Middleware Integration

**Frontend Integration with Middleware Responses:**

```javascript
// WeWeb component for handling middleware-enhanced responses
class XanoMiddlewareHandler {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.requestIdTracker = new Map();
  }
  
  async makeApiRequest(endpoint, data, options = {}) {
    try {
      const requestId = this.generateRequestId();
      
      // Store request metadata for tracking
      this.requestIdTracker.set(requestId, {
        endpoint: endpoint,
        timestamp: new Date().toISOString(),
        data: data
      });
      
      const response = await fetch(`${this.baseUrl}/api/${endpoint}`, {
        method: options.method || 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json',
          'X-Request-ID': requestId
        },
        body: JSON.stringify(data)
      });
      
      const responseData = await response.json();
      
      // Handle middleware-enhanced response
      if (responseData.meta) {
        this.handleResponseMetadata(responseData.meta, requestId);
      }
      
      // Handle validation errors from pre-middleware
      if (!response.ok && responseData.code === 'VALIDATION_ERROR') {
        this.handleValidationErrors(responseData.errors);
        return { success: false, errors: responseData.errors };
      }
      
      // Handle authentication errors from pre-middleware
      if (!response.ok && responseData.code === 'INVALID_TOKEN') {
        this.handleAuthenticationError();
        return { success: false, error: 'Authentication required' };
      }
      
      // Update WeWeb variables with response data
      if (responseData.success !== false) {
        wwLib.wwVariable.updateValue(`${endpoint}_response`, responseData.data);
        wwLib.wwVariable.updateValue(`${endpoint}_meta`, responseData.meta);
      }
      
      return { success: true, data: responseData.data, meta: responseData.meta };
      
    } catch (error) {
      console.error('API request failed:', error);
      wwLib.wwUtils.showErrorToast('Network error occurred');
      return { success: false, error: 'Network error' };
    }
  }
  
  handleResponseMetadata(meta, requestId) {
    // Update request tracking
    const requestInfo = this.requestIdTracker.get(requestId);
    if (requestInfo) {
      const responseTime = new Date() - new Date(requestInfo.timestamp);
      
      // Update performance metrics in WeWeb
      wwLib.wwVariable.updateValue('api_response_time', responseTime);
      wwLib.wwVariable.updateValue('last_request_id', meta.request_id);
      wwLib.wwVariable.updateValue('api_version', meta.api_version);
      
      // Clean up tracking
      this.requestIdTracker.delete(requestId);
    }
  }
  
  handleValidationErrors(errors) {
    // Display validation errors in UI
    const errorMessages = errors.map(error => ({
      type: 'validation',
      message: error,
      timestamp: new Date().toISOString()
    }));
    
    wwLib.wwVariable.updateValue('form_errors', errorMessages);
    
    // Show user-friendly error messages
    errors.forEach(error => {
      wwLib.wwUtils.showErrorToast(error);
    });
  }
  
  handleAuthenticationError() {
    // Clear authentication state
    wwLib.wwVariable.updateValue('auth_token', null);
    wwLib.wwVariable.updateValue('current_user', null);
    wwLib.wwVariable.updateValue('is_authenticated', false);
    
    // Redirect to login page
    wwLib.wwPageActions.navigate('/login');
    wwLib.wwUtils.showErrorToast('Please log in to continue');
  }
  
  generateRequestId() {
    return `req_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
  
  async uploadFileWithMiddleware(file, uploadOptions = {}) {
    const formData = new FormData();
    formData.append('file', file);
    
    // Add metadata for middleware processing
    formData.append('upload_context', JSON.stringify({
      type: uploadOptions.type || 'general',
      max_size: uploadOptions.maxSize || 10485760, // 10MB default
      allowed_types: uploadOptions.allowedTypes || ['jpg', 'png', 'pdf']
    }));
    
    try {
      const response = await fetch(`${this.baseUrl}/api/upload`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'X-Request-ID': this.generateRequestId()
        },
        body: formData
      });
      
      const result = await response.json();
      
      // Handle middleware validation for file uploads
      if (!response.ok && result.code === 'FILE_VALIDATION_ERROR') {
        wwLib.wwUtils.showErrorToast(`File validation failed: ${result.error}`);
        return { success: false, error: result.error };
      }
      
      if (result.success) {
        wwLib.wwVariable.updateValue('uploaded_file', result.data);
        wwLib.wwUtils.showSuccessToast('File uploaded successfully');
      }
      
      return result;
      
    } catch (error) {
      console.error('File upload failed:', error);
      wwLib.wwUtils.showErrorToast('Upload failed');
      return { success: false, error: 'Upload failed' };
    }
  }
}

// Initialize middleware handler
const middlewareHandler = new XanoMiddlewareHandler(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function submitUserData() {
  const userData = {
    email: wwLib.wwVariable.getValue('user_email'),
    password: wwLib.wwVariable.getValue('user_password'),
    first_name: wwLib.wwVariable.getValue('user_first_name'),
    last_name: wwLib.wwVariable.getValue('user_last_name')
  };
  
  const result = await middlewareHandler.makeApiRequest('register', userData);
  
  if (result.success) {
    wwLib.wwUtils.showSuccessToast('Registration successful');
    wwLib.wwPageActions.navigate('/dashboard');
  }
}

async function updateProfile() {
  const profileData = {
    first_name: wwLib.wwVariable.getValue('profile_first_name'),
    last_name: wwLib.wwVariable.getValue('profile_last_name'),
    bio: wwLib.wwVariable.getValue('profile_bio')
  };
  
  const result = await middlewareHandler.makeApiRequest('profile/update', profileData, {
    method: 'PATCH'
  });
  
  if (result.success) {
    wwLib.wwUtils.showSuccessToast('Profile updated successfully');
  }
}
```

## ⚙️ **Middleware Configuration**

### Response Types

**Merge Response:**
- Combines middleware output with original response
- Middleware variables are added to the original data
- Duplicate keys are overwritten by middleware values
- Useful for enhancing existing responses

**Replace Response:**
- Middleware output completely replaces original response
- Original data is not passed through unless explicitly included
- Provides complete control over response structure
- Useful for transformation and security filtering

### Exception Handling Options

**Silent Mode:**
```javascript
{
  "exception_preference": "silent",
  "description": "Ignores middleware errors and continues with original response"
}
```

**Rethrow Mode:**
```javascript
{
  "exception_preference": "rethrow",
  "description": "Allows post-middleware to execute for error logging, then rethrows error"
}
```

**Critical Mode:**
```javascript
{
  "exception_preference": "critical",
  "description": "Halts all execution if middleware error occurs"
}
```

### Advanced Middleware Patterns

**Rate Limiting Pre-Middleware:**

```javascript
// Rate limiting with Redis caching
[
  {
    "function": "create_variable",
    "name": "rate_limit_key",
    "value": "rate_limit_{{ auth.user.id || request.ip }}_{{ now|date('Y-m-d-H-i') }}"
  },
  {
    "function": "cache_get",
    "key": "{{ rate_limit_key }}",
    "return_as": "current_requests"
  },
  {
    "function": "create_variable",
    "name": "request_count",
    "value": "{{ current_requests.value || 0 }}"
  },
  {
    "function": "conditional",
    "condition": "{{ request_count >= 100 }}", // 100 requests per minute
    "true_branch": [
      {
        "function": "return_response",
        "status": 429,
        "body": {
          "error": "Rate limit exceeded",
          "retry_after": 60,
          "limit": 100,
          "current": "{{ request_count }}",
          "code": "RATE_LIMIT_EXCEEDED"
        }
      }
    ]
  },
  {
    "function": "cache_set",
    "key": "{{ rate_limit_key }}",
    "value": "{{ request_count + 1 }}",
    "ttl": 60
  },
  {
    "function": "return_response",
    "body": {
      "rate_limit_remaining": "{{ 100 - (request_count + 1) }}",
      "rate_limit_reset": "{{ now + 60 }}"
    }
  }
]
```

**Security Headers Post-Middleware:**

```javascript
// Security headers and response sanitization
[
  {
    "function": "create_variable",
    "name": "secure_response",
    "value": "{{ vars }}"
  },
  {
    "function": "conditional",
    "condition": "{{ vars.user }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "secure_response",
        "operation": "merge",
        "value": {
          "user": {
            "id": "{{ vars.user.id }}",
            "email": "{{ vars.user.email }}",
            "first_name": "{{ vars.user.first_name }}",
            "last_name": "{{ vars.user.last_name }}",
            "role": "{{ vars.user.role }}"
            // Exclude sensitive fields like password_hash, reset_tokens, etc.
          }
        }
      }
    ]
  },
  {
    "function": "set_response_headers",
    "headers": {
      "X-Content-Type-Options": "nosniff",
      "X-Frame-Options": "DENY",
      "X-XSS-Protection": "1; mode=block",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "Content-Security-Policy": "default-src 'self'",
      "X-API-Version": "v1.0",
      "X-Response-Time": "{{ now - request.timestamp }}ms"
    }
  },
  {
    "function": "return_response",
    "body": "{{ secure_response }}"
  }
]
```

## 💡 **Pro Tips**

- **Keep Middleware Lightweight**: Avoid heavy operations that could impact performance
- **Use Appropriate Exception Handling**: Choose silent for non-critical operations, critical for security
- **Cache Validation Results**: Store validation outcomes to avoid repeated processing
- **Monitor Middleware Performance**: Track execution times and optimize slow middleware
- **Implement Fallbacks**: Always have graceful degradation for middleware failures
- **Version Your Middleware**: Maintain backwards compatibility when updating middleware logic

## 🔧 **Troubleshooting**

### Common Middleware Issues

**Problem**: Pre-middleware not receiving expected inputs  
**Solution**: Ensure all inputs are defined in the API endpoint; pre-middleware only sees defined inputs

**Problem**: Post-middleware replacing original response unintentionally  
**Solution**: Check response type setting; use "merge" instead of "replace" to preserve original data

**Problem**: Middleware causing performance issues  
**Solution**: Optimize database queries, use async execution for non-critical operations, implement caching

**Problem**: Middleware errors breaking API functionality  
**Solution**: Review exception preference settings; use "silent" for non-critical middleware or implement proper error handling

---

**Next Steps**: Ready to implement robust middleware? Check out [Custom Functions](custom-functions.md) for reusable logic or explore [Working with Data](working-with-data.md) for advanced data processing techniques