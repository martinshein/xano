---
title: Swagger/OpenAPI Documentation - Automated API Documentation
description: Complete guide to Xano's auto-generated Swagger/OpenAPI documentation including configuration, testing, authentication, and integration with external tools and AI platforms
category: custom-functions
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - api__apis.md
  - building-with-visual-development.md
  - authentication.md
subcategory: 05-advanced-features/custom-functions
tags:
  - swagger
  - openapi
  - api-documentation
  - testing
  - integration
  - no-code
---

## 📋 **Quick Summary**

Swagger/OpenAPI documentation provides a standardized, interactive way to describe and test your APIs. Xano automatically generates comprehensive documentation for all your endpoints, complete with authentication testing, example requests/responses, and cURL commands. Perfect for developer onboarding, API integration, and AI/LLM consumption in n8n, WeWeb, and other platforms.

## What You'll Learn

- How to access and navigate Xano's auto-generated API documentation
- Configuring documentation access levels and authentication
- Testing APIs directly from the documentation interface
- Creating custom examples and sample data
- Integrating with external tools and AI platforms
- Best practices for comprehensive API documentation

# Swagger/OpenAPI Documentation

## Overview

**Swagger/OpenAPI Documentation** is a standardized format for describing REST APIs. Xano automatically generates interactive documentation for all your API endpoints, making it easy for developers to understand, test, and integrate with your APIs without needing extensive technical documentation.

### Documentation Benefits

**For Developers:**
- Interactive API testing environment
- Clear request/response examples
- Authentication flow demonstration
- Automatic code generation (cURL, SDKs)

**For AI/LLM Integration:**
- Standardized schema for AI tool consumption
- Automated workflow generation in n8n
- Dynamic form creation in WeWeb
- Context for AI development assistants

## 🚀 **Accessing Your API Documentation**

### Documentation URL Structure

```javascript
// Xano documentation URLs
{
  "public_docs": "https://your-instance.xano.com/docs/api-group-name",
  "private_docs": "https://your-instance.xano.com/docs/api-group-name?token=PRIVATE_TOKEN",
  "json_spec": "https://your-instance.xano.com/docs/api-group-name/openapi.json"
}
```

### Access Levels Configuration

**API Group Settings:**

```javascript
// Documentation access configuration
{
  "swagger_settings": {
    "access_level": "public", // public, private, disabled
    "private_token": "auto-generated-secure-token",
    "description": "User Management API v1.0",
    "contact": {
      "name": "API Support",
      "email": "api@yourcompany.com",
      "url": "https://yourcompany.com/support"
    },
    "version": "1.0.0",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    }
  }
}
```

## 🔗 **No-Code Platform Integration**

### n8n API Discovery and Testing

**Automated API Discovery Workflow:**

```javascript
// n8n workflow for automatic API integration
{
  "nodes": [
    {
      "name": "Fetch OpenAPI Spec",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/docs/users/openapi.json",
        "method": "GET",
        "headers": {
          "Accept": "application/json"
        }
      }
    },
    {
      "name": "Parse API Endpoints",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const spec = $input.first().json;
          const endpoints = [];
          
          for (const [path, methods] of Object.entries(spec.paths)) {
            for (const [method, details] of Object.entries(methods)) {
              endpoints.push({
                path: path,
                method: method.toUpperCase(),
                summary: details.summary,
                description: details.description,
                operationId: details.operationId,
                parameters: details.parameters || [],
                requestBody: details.requestBody,
                responses: details.responses,
                security: details.security || []
              });
            }
          }
          
          return endpoints.map(endpoint => ({ json: endpoint }));
        `
      }
    },
    {
      "name": "Test Each Endpoint",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com{{ $json.path }}",
        "method": "{{ $json.method }}",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_AUTH_TOKEN }}",
          "Content-Type": "application/json"
        },
        "body": "{{ $json.requestBody ? $json.requestBody.content['application/json'].example : '' }}"
      }
    }
  ]
}
```

### WeWeb Dynamic API Integration

**OpenAPI-Driven Form Generation:**

```javascript
// WeWeb component for dynamic API integration
class SwaggerAPIIntegration {
  constructor(swaggerUrl, authToken = null) {
    this.swaggerUrl = swaggerUrl;
    this.authToken = authToken;
    this.apiSpec = null;
  }
  
  async loadAPISpec() {
    try {
      const response = await fetch(this.swaggerUrl);
      this.apiSpec = await response.json();
      
      wwLib.wwVariable.updateValue('api_spec', this.apiSpec);
      wwLib.wwVariable.updateValue('api_endpoints', this.parseEndpoints());
      
      return this.apiSpec;
    } catch (error) {
      console.error('Failed to load API spec:', error);
      return null;
    }
  }
  
  parseEndpoints() {
    if (!this.apiSpec) return [];
    
    const endpoints = [];
    
    for (const [path, methods] of Object.entries(this.apiSpec.paths)) {
      for (const [method, details] of Object.entries(methods)) {
        endpoints.push({
          id: `${method}_${path}`.replace(/[^a-zA-Z0-9]/g, '_'),
          path: path,
          method: method.toUpperCase(),
          summary: details.summary || `${method.toUpperCase()} ${path}`,
          description: details.description || '',
          parameters: this.parseParameters(details.parameters || []),
          requestBody: this.parseRequestBody(details.requestBody),
          responses: details.responses || {},
          requiresAuth: (details.security && details.security.length > 0),
          tags: details.tags || []
        });
      }
    }
    
    return endpoints;
  }
  
  parseParameters(parameters) {
    return parameters.map(param => ({
      name: param.name,
      in: param.in, // query, header, path, cookie
      required: param.required || false,
      type: param.schema?.type || 'string',
      description: param.description || '',
      example: param.example || param.schema?.example
    }));
  }
  
  parseRequestBody(requestBody) {
    if (!requestBody) return null;
    
    const jsonContent = requestBody.content?.['application/json'];
    if (!jsonContent) return null;
    
    return {
      required: requestBody.required || false,
      schema: jsonContent.schema,
      example: jsonContent.example
    };
  }
  
  generateFormFields(endpointId) {
    const endpoint = this.getEndpoint(endpointId);
    if (!endpoint) return [];
    
    const fields = [];
    
    // Add parameter fields
    endpoint.parameters.forEach(param => {
      if (param.in === 'query' || param.in === 'path') {
        fields.push({
          name: param.name,
          type: this.mapTypeToFormField(param.type),
          required: param.required,
          label: param.description || param.name,
          placeholder: param.example || `Enter ${param.name}`,
          validation: this.createValidationRules(param)
        });
      }
    });
    
    // Add request body fields
    if (endpoint.requestBody) {
      const schema = endpoint.requestBody.schema;
      if (schema.type === 'object' && schema.properties) {
        Object.entries(schema.properties).forEach(([propName, propSchema]) => {
          fields.push({
            name: propName,
            type: this.mapTypeToFormField(propSchema.type),
            required: schema.required?.includes(propName) || false,
            label: propSchema.description || propName,
            placeholder: propSchema.example || `Enter ${propName}`,
            validation: this.createValidationRules(propSchema)
          });
        });
      }
    }
    
    return fields;
  }
  
  mapTypeToFormField(type) {
    const typeMapping = {
      'string': 'text',
      'integer': 'number',
      'number': 'number',
      'boolean': 'checkbox',
      'array': 'tags',
      'object': 'json'
    };
    
    return typeMapping[type] || 'text';
  }
  
  createValidationRules(schema) {
    const rules = [];
    
    if (schema.minLength) {
      rules.push({
        type: 'minLength',
        value: schema.minLength,
        message: `Minimum length is ${schema.minLength}`
      });
    }
    
    if (schema.maxLength) {
      rules.push({
        type: 'maxLength',
        value: schema.maxLength,
        message: `Maximum length is ${schema.maxLength}`
      });
    }
    
    if (schema.pattern) {
      rules.push({
        type: 'pattern',
        value: schema.pattern,
        message: 'Invalid format'
      });
    }
    
    return rules;
  }
  
  getEndpoint(endpointId) {
    const endpoints = wwLib.wwVariable.getValue('api_endpoints') || [];
    return endpoints.find(ep => ep.id === endpointId);
  }
  
  async testEndpoint(endpointId, formData) {
    const endpoint = this.getEndpoint(endpointId);
    if (!endpoint) {
      throw new Error('Endpoint not found');
    }
    
    try {
      // Build URL with path parameters
      let url = `${this.apiSpec.servers[0].url}${endpoint.path}`;
      const queryParams = {};
      
      // Process parameters
      endpoint.parameters.forEach(param => {
        const value = formData[param.name];
        if (value !== undefined) {
          if (param.in === 'path') {
            url = url.replace(`{${param.name}}`, encodeURIComponent(value));
          } else if (param.in === 'query') {
            queryParams[param.name] = value;
          }
        }
      });
      
      // Add query parameters
      if (Object.keys(queryParams).length > 0) {
        url += '?' + new URLSearchParams(queryParams).toString();
      }
      
      // Prepare request options
      const options = {
        method: endpoint.method,
        headers: {
          'Content-Type': 'application/json'
        }
      };
      
      // Add authentication
      if (endpoint.requiresAuth && this.authToken) {
        options.headers['Authorization'] = `Bearer ${this.authToken}`;
      }
      
      // Add request body
      if (endpoint.requestBody && ['POST', 'PUT', 'PATCH'].includes(endpoint.method)) {
        const bodyData = {};
        if (endpoint.requestBody.schema?.properties) {
          Object.keys(endpoint.requestBody.schema.properties).forEach(key => {
            if (formData[key] !== undefined) {
              bodyData[key] = formData[key];
            }
          });
        }
        options.body = JSON.stringify(bodyData);
      }
      
      const response = await fetch(url, options);
      const result = await response.json();
      
      const testResult = {
        url: url,
        method: endpoint.method,
        status: response.status,
        statusText: response.statusText,
        headers: Object.fromEntries(response.headers.entries()),
        body: result,
        success: response.ok
      };
      
      wwLib.wwVariable.updateValue('last_api_test_result', testResult);
      
      return testResult;
    } catch (error) {
      console.error('API test failed:', error);
      throw error;
    }
  }
}

// Initialize Swagger integration
const swaggerApi = new SwaggerAPIIntegration(
  wwLib.wwVariable.getValue('swagger_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function initializeAPIExplorer() {
  await swaggerApi.loadAPISpec();
  const endpoints = wwLib.wwVariable.getValue('api_endpoints');
  wwLib.wwVariable.updateValue('available_endpoints', endpoints);
}

async function loadEndpointForm() {
  const selectedEndpoint = wwLib.wwVariable.getValue('selected_endpoint_id');
  const formFields = swaggerApi.generateFormFields(selectedEndpoint);
  wwLib.wwVariable.updateValue('endpoint_form_fields', formFields);
}

async function testSelectedEndpoint() {
  const endpointId = wwLib.wwVariable.getValue('selected_endpoint_id');
  const formData = wwLib.wwVariable.getValue('endpoint_form_data');
  
  try {
    const result = await swaggerApi.testEndpoint(endpointId, formData);
    
    if (result.success) {
      wwLib.wwUtils.showSuccessToast('API call successful');
    } else {
      wwLib.wwUtils.showErrorToast(`API call failed: ${result.status}`);
    }
  } catch (error) {
    wwLib.wwUtils.showErrorToast(`Test failed: ${error.message}`);
  }
}
```

## 🛠️ **Documentation Customization**

### Custom Examples and Sample Data

**Setting Sample Inputs and Responses:**

```javascript
// Function stack with custom examples for documentation
[
  {
    "function": "create_variable",
    "name": "sample_user_data",
    "value": {
      "email": "john.doe@example.com",
      "profile": {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "location": "San Francisco, CA"
      },
      "preferences": {
        "notifications": true,
        "newsletter": false,
        "language": "en"
      }
    }
  },
  {
    "function": "add_record",
    "table": "users",
    "data": "{{ sample_user_data }}",
    "return_as": "created_user"
  },
  {
    "function": "return_response",
    "status": 201,
    "body": {
      "id": "{{ created_user.id }}",
      "email": "{{ created_user.email }}",
      "profile": "{{ created_user.profile }}",
      "created_at": "{{ created_user.created_at }}",
      "success": true,
      "message": "User created successfully"
    }
  }
]
```

### Enhanced API Descriptions

**Comprehensive Endpoint Documentation:**

```yaml
# OpenAPI specification enhancement
openapi: 3.0.0
info:
  title: User Management API
  description: |
    Complete user lifecycle management API for modern applications.
    
    ## Authentication
    This API uses Bearer token authentication. Include your token in the Authorization header:
    ```
    Authorization: Bearer YOUR_TOKEN_HERE
    ```
    
    ## Rate Limiting
    - 100 requests per minute for authenticated users
    - 20 requests per minute for unauthenticated users
    
    ## Error Handling
    All errors follow RFC 7807 problem details format.
  version: 1.0.0
  contact:
    name: API Support Team
    email: api-support@yourcompany.com
    url: https://docs.yourcompany.com
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

servers:
  - url: https://your-xano-instance.com/api
    description: Production server
  - url: https://staging-instance.xano.com/api
    description: Staging server

paths:
  /users:
    post:
      summary: Create new user account
      description: |
        Creates a new user account with comprehensive validation and automatic welcome email.
        
        ### Features
        - Email uniqueness validation
        - Password strength requirements
        - Automatic profile creation
        - Welcome email trigger
        - Audit log entry
        
        ### Business Rules
        - Email must be unique across all users
        - Password must contain at least 8 characters
        - Profile information is required for account activation
      operationId: createUser
      tags:
        - User Management
      security:
        - BearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - email
                - password
                - profile
              properties:
                email:
                  type: string
                  format: email
                  description: Unique email address for the account
                  example: "john.doe@example.com"
                  maxLength: 255
                password:
                  type: string
                  description: Secure password meeting complexity requirements
                  minLength: 8
                  example: "SecurePass123!"
                profile:
                  type: object
                  required:
                    - first_name
                    - last_name
                  properties:
                    first_name:
                      type: string
                      description: User's first name
                      maxLength: 50
                      example: "John"
                    last_name:
                      type: string
                      description: User's last name
                      maxLength: 50
                      example: "Doe"
                    phone:
                      type: string
                      description: Optional phone number
                      pattern: "^\\+?[1-9]\\d{1,14}$"
                      example: "+1-555-123-4567"
                preferences:
                  type: object
                  description: User preference settings
                  properties:
                    notifications:
                      type: boolean
                      description: Enable email notifications
                      default: true
                    newsletter:
                      type: boolean
                      description: Subscribe to newsletter
                      default: false
                    language:
                      type: string
                      description: Preferred language code
                      enum: ["en", "es", "fr", "de"]
                      default: "en"
            examples:
              complete_user:
                summary: Complete user registration
                value:
                  email: "john.doe@example.com"
                  password: "SecurePass123!"
                  profile:
                    first_name: "John"
                    last_name: "Doe"
                    phone: "+1-555-123-4567"
                  preferences:
                    notifications: true
                    newsletter: false
                    language: "en"
              minimal_user:
                summary: Minimal required fields
                value:
                  email: "jane.smith@example.com"
                  password: "AnotherSecure456!"
                  profile:
                    first_name: "Jane"
                    last_name: "Smith"
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    description: Unique user identifier
                    example: 12345
                  email:
                    type: string
                    format: email
                    example: "john.doe@example.com"
                  profile:
                    type: object
                    properties:
                      first_name:
                        type: string
                        example: "John"
                      last_name:
                        type: string
                        example: "Doe"
                      phone:
                        type: string
                        example: "+1-555-123-4567"
                  created_at:
                    type: string
                    format: date-time
                    example: "2024-01-15T10:30:00Z"
                  status:
                    type: string
                    enum: ["active", "pending", "inactive"]
                    example: "active"
              examples:
                success_response:
                  summary: Successful user creation
                  value:
                    id: 12345
                    email: "john.doe@example.com"
                    profile:
                      first_name: "John"
                      last_name: "Doe"
                      phone: "+1-555-123-4567"
                    created_at: "2024-01-15T10:30:00Z"
                    status: "active"
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: "Validation failed"
                  details:
                    type: array
                    items:
                      type: object
                      properties:
                        field:
                          type: string
                          example: "email"
                        message:
                          type: string
                          example: "Email already exists"
        '401':
          description: Authentication required
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |
        JWT authentication token. Obtain by calling the /auth/login endpoint.
        
        Example:
        ```
        Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
        ```
```

## 🧪 **Interactive Testing**

### Authentication Testing

**Setting Up Test Authentication:**

```javascript
// Test authentication configuration
{
  "test_auth": {
    "token_type": "Bearer",
    "token_value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user_context": {
      "id": 123,
      "email": "test@example.com",
      "roles": ["user"]
    }
  },
  "test_scenarios": [
    {
      "name": "Authenticated User",
      "description": "Test with valid authentication token",
      "auth_token": "valid_user_token"
    },
    {
      "name": "Admin User",
      "description": "Test with admin privileges",
      "auth_token": "admin_user_token"
    },
    {
      "name": "Unauthenticated",
      "description": "Test without authentication",
      "auth_token": null
    }
  ]
}
```

### Test Data Management

**Dynamic Test Data Generation:**

```javascript
// Test data factory for documentation examples
[
  {
    "function": "create_variable",
    "name": "test_data_factory",
    "value": {
      "users": {
        "john_doe": {
          "email": "john.doe@example.com",
          "password": "TestPass123!",
          "profile": {
            "first_name": "John",
            "last_name": "Doe",
            "age": 30
          }
        },
        "jane_admin": {
          "email": "jane.admin@example.com",
          "password": "AdminPass456!",
          "profile": {
            "first_name": "Jane",
            "last_name": "Admin",
            "role": "administrator"
          }
        }
      },
      "products": {
        "sample_product": {
          "name": "Premium Widget",
          "description": "High-quality widget for testing",
          "price": 29.99,
          "category": "widgets"
        }
      }
    }
  }
]
```

## 🔧 **Integration Tools**

### cURL Command Generation

**Automatic cURL Generation:**

```bash
# Generated cURL commands from Swagger docs
curl -X POST "https://your-xano-instance.com/api/users" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "SecurePass123!",
    "profile": {
      "first_name": "John",
      "last_name": "Doe"
    }
  }'
```

### Postman Collection Export

**Postman Integration Pattern:**

```json
{
  "info": {
    "name": "Xano API Collection",
    "description": "Auto-generated from Swagger documentation",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "auth": {
    "type": "bearer",
    "bearer": [
      {
        "key": "token",
        "value": "{{auth_token}}",
        "type": "string"
      }
    ]
  },
  "variable": [
    {
      "key": "base_url",
      "value": "https://your-xano-instance.com/api",
      "type": "string"
    },
    {
      "key": "auth_token",
      "value": "",
      "type": "string"
    }
  ]
}
```

## 💡 **Pro Tips**

- **Keep Examples Current**: Regularly update sample data to reflect real use cases
- **Document Edge Cases**: Include examples of error scenarios and validation failures
- **Use Descriptive Names**: Make endpoint names and descriptions self-explanatory
- **Version Your APIs**: Include version information in documentation
- **Security First**: Never include real credentials or sensitive data in examples
- **Test Regularly**: Use the interactive testing features to verify documentation accuracy

## 🔧 **Troubleshooting**

### Common Documentation Issues

**Problem**: Documentation not updating after API changes  
**Solution**: Republish the API endpoint and refresh the documentation page

**Problem**: Authentication testing not working  
**Solution**: Verify token format and expiration, ensure proper Bearer token format

**Problem**: Examples not showing in documentation  
**Solution**: Set examples using the "Set As Example" feature in Run & Debug panel

**Problem**: Private documentation not accessible  
**Solution**: Check API group settings and ensure private token is included in URL

---

**Next Steps**: Ready to enhance your API documentation? Check out [API Design](api__apis.md) for comprehensive API development or explore [Building with Visual Development](building-with-visual-development.md) for complete application architecture