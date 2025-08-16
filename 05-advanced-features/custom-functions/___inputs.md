---
title: Function Stack Inputs - Data Flow and Parameter Management
description: Complete guide to configuring and managing inputs in Xano function stacks, including parameter types, validation, default values, and best practices for API endpoint design
category: custom-functions
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - custom-functions.md
  - building-with-visual-development.md
  - function-stack-performance.md
subcategory: 05-advanced-features/custom-functions
tags:
  - inputs
  - parameters
  - data-validation
  - function-stacks
  - api-design
  - no-code
---

## 📋 **Quick Summary**

Function stack inputs define the data your endpoints, custom functions, and workflows need to operate. Learn how to configure parameter types, implement validation, set default values, and design robust APIs that integrate seamlessly with n8n, WeWeb, and other no-code platforms. Essential for building maintainable and secure function stacks.

## What You'll Learn

- How to configure and manage function stack inputs
- Parameter types and validation strategies
- Input documentation and API design best practices
- Security considerations for input handling
- Integration patterns for no-code platforms
- Advanced input configuration techniques

# Function Stack Inputs

## Overview

**Inputs** are the data entry points for your function stacks. They define what information your APIs, custom functions, background tasks, and triggers need to execute successfully. Proper input configuration ensures data integrity, improves security, and creates better developer experience for your API consumers.

### Input Components

**Input Definition:**
- Parameter name and type specification
- Validation rules and constraints
- Default values and optional parameters
- Documentation and descriptions

**Input Sources:**
- HTTP request body, query parameters, and headers
- Path parameters for RESTful APIs
- Authentication tokens and user context
- Environment variables and constants

## 🚀 **Input Types and Configuration**

### Basic Input Types

**Text Input:**
```json
{
  "name": "username",
  "type": "text",
  "required": true,
  "description": "User's login username",
  "validation": {
    "min_length": 3,
    "max_length": 50,
    "pattern": "^[a-zA-Z0-9_]+$"
  }
}
```

**Integer Input:**
```json
{
  "name": "page",
  "type": "integer",
  "required": false,
  "default": 1,
  "description": "Page number for pagination",
  "validation": {
    "min": 1,
    "max": 1000
  }
}
```

**Boolean Input:**
```json
{
  "name": "include_metadata",
  "type": "boolean",
  "required": false,
  "default": false,
  "description": "Whether to include additional metadata in response"
}
```

**Array Input:**
```json
{
  "name": "tags",
  "type": "array",
  "required": false,
  "description": "List of tags to associate with the item",
  "validation": {
    "max_items": 10,
    "item_type": "text"
  }
}
```

**Object Input:**
```json
{
  "name": "user_profile",
  "type": "object",
  "required": true,
  "description": "User profile information",
  "properties": {
    "first_name": {"type": "text", "required": true},
    "last_name": {"type": "text", "required": true},
    "email": {"type": "email", "required": true}
  }
}
```

### Advanced Input Configuration

**File Upload Input:**
```json
{
  "name": "profile_image",
  "type": "file",
  "required": false,
  "description": "User profile image upload",
  "validation": {
    "max_size": "5MB",
    "allowed_types": ["image/jpeg", "image/png", "image/webp"],
    "max_dimensions": {"width": 2048, "height": 2048}
  }
}
```

**Date/Timestamp Input:**
```json
{
  "name": "start_date",
  "type": "timestamp",
  "required": true,
  "description": "Event start date and time",
  "validation": {
    "format": "ISO8601",
    "min_date": "today",
    "max_date": "+1 year"
  }
}
```

## 🔗 **No-Code Platform Integration**

### n8n HTTP Request Configuration

**Sending Structured Data to Xano:**

```javascript
// n8n HTTP Request node configuration
{
  "method": "POST",
  "url": "https://your-xano-instance.com/api/users",
  "headers": {
    "Authorization": "Bearer {{ $json.auth_token }}",
    "Content-Type": "application/json"
  },
  "body": {
    "user_profile": {
      "first_name": "{{ $json.first_name }}",
      "last_name": "{{ $json.last_name }}",
      "email": "{{ $json.email }}"
    },
    "preferences": {
      "newsletter": "{{ $json.newsletter_opt_in }}",
      "notifications": "{{ $json.enable_notifications }}"
    },
    "tags": "{{ $json.user_tags.split(',') }}",
    "referral_code": "{{ $json.referral_code || null }}"
  }
}
```

### WeWeb Form Integration

**Dynamic Form Generation with Xano Inputs:**

```javascript
// WeWeb component for dynamic form creation
class XanoFormBuilder {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async getEndpointInputs(apiGroup, endpoint) {
    try {
      const response = await fetch(`${this.baseUrl}/api/meta/endpoint-inputs`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          api_group: apiGroup,
          endpoint: endpoint
        })
      });
      
      const inputDefinitions = await response.json();
      return inputDefinitions;
    } catch (error) {
      console.error('Failed to fetch input definitions:', error);
      return [];
    }
  }
  
  generateFormFields(inputDefinitions) {
    const formFields = inputDefinitions.map(input => {
      const field = {
        name: input.name,
        type: this.mapInputTypeToFormField(input.type),
        required: input.required,
        label: input.description || input.name,
        validation: this.createValidationRules(input)
      };
      
      if (input.default !== undefined) {
        field.defaultValue = input.default;
      }
      
      return field;
    });
    
    // Update WeWeb form configuration
    wwLib.wwVariable.updateValue('form_fields', formFields);
    return formFields;
  }
  
  mapInputTypeToFormField(inputType) {
    const typeMapping = {
      'text': 'text',
      'integer': 'number',
      'decimal': 'number',
      'boolean': 'checkbox',
      'email': 'email',
      'timestamp': 'datetime-local',
      'file': 'file',
      'array': 'tags',
      'object': 'json'
    };
    
    return typeMapping[inputType] || 'text';
  }
  
  createValidationRules(input) {
    const rules = [];
    
    if (input.required) {
      rules.push({ type: 'required', message: `${input.name} is required` });
    }
    
    if (input.validation) {
      if (input.validation.min_length) {
        rules.push({
          type: 'minLength',
          value: input.validation.min_length,
          message: `Minimum length is ${input.validation.min_length}`
        });
      }
      
      if (input.validation.max_length) {
        rules.push({
          type: 'maxLength',
          value: input.validation.max_length,
          message: `Maximum length is ${input.validation.max_length}`
        });
      }
      
      if (input.validation.pattern) {
        rules.push({
          type: 'pattern',
          value: input.validation.pattern,
          message: 'Invalid format'
        });
      }
    }
    
    return rules;
  }
  
  async submitForm(formData, apiGroup, endpoint) {
    try {
      const response = await fetch(`${this.baseUrl}/api/${apiGroup}/${endpoint}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      
      const result = await response.json();
      
      if (response.ok) {
        wwLib.wwVariable.updateValue('form_submission_success', true);
        wwLib.wwVariable.updateValue('form_result', result);
        wwLib.wwUtils.showSuccessToast('Form submitted successfully');
      } else {
        wwLib.wwVariable.updateValue('form_errors', result.errors || {});
        wwLib.wwUtils.showErrorToast('Form submission failed');
      }
      
      return result;
    } catch (error) {
      console.error('Form submission error:', error);
      wwLib.wwUtils.showErrorToast('Network error occurred');
      return { error: 'Submission failed' };
    }
  }
}

// Usage in WeWeb
const formBuilder = new XanoFormBuilder(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

async function initializeForm() {
  const apiGroup = wwLib.wwVariable.getValue('target_api_group');
  const endpoint = wwLib.wwVariable.getValue('target_endpoint');
  
  const inputs = await formBuilder.getEndpointInputs(apiGroup, endpoint);
  const formFields = formBuilder.generateFormFields(inputs);
  
  wwLib.wwVariable.updateValue('form_initialized', true);
}

async function handleFormSubmit() {
  const formData = wwLib.wwVariable.getValue('form_data');
  const apiGroup = wwLib.wwVariable.getValue('target_api_group');
  const endpoint = wwLib.wwVariable.getValue('target_endpoint');
  
  const result = await formBuilder.submitForm(formData, apiGroup, endpoint);
  
  if (!result.error) {
    // Handle successful submission
    wwLib.wwUtils.navigateTo('/success');
  }
}
```

## 🛠️ **Function Stack Input Implementation**

### API Endpoint Input Configuration

**User Registration Endpoint:**

```javascript
// Function stack inputs for user registration
{
  "inputs": [
    {
      "name": "email",
      "type": "email",
      "required": true,
      "description": "User's email address for account creation",
      "validation": {
        "format": "email",
        "max_length": 255
      }
    },
    {
      "name": "password",
      "type": "text",
      "required": true,
      "description": "Account password (will be hashed)",
      "validation": {
        "min_length": 8,
        "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]"
      }
    },
    {
      "name": "profile",
      "type": "object",
      "required": true,
      "description": "User profile information",
      "properties": {
        "first_name": {"type": "text", "required": true, "max_length": 50},
        "last_name": {"type": "text", "required": true, "max_length": 50},
        "date_of_birth": {"type": "date", "required": false}
      }
    },
    {
      "name": "preferences",
      "type": "object",
      "required": false,
      "description": "User preferences and settings",
      "default": {"notifications": true, "newsletter": false},
      "properties": {
        "notifications": {"type": "boolean", "default": true},
        "newsletter": {"type": "boolean", "default": false},
        "language": {"type": "text", "default": "en"}
      }
    }
  ]
}
```

### Custom Function Input Design

**Email Template Generator Function:**

```javascript
// Custom function inputs for email template generation
{
  "function_name": "generate_email_template",
  "inputs": [
    {
      "name": "template_type",
      "type": "text",
      "required": true,
      "description": "Type of email template to generate",
      "validation": {
        "enum": ["welcome", "password_reset", "order_confirmation", "newsletter"]
      }
    },
    {
      "name": "recipient_data",
      "type": "object",
      "required": true,
      "description": "Information about the email recipient",
      "properties": {
        "name": {"type": "text", "required": true},
        "email": {"type": "email", "required": true},
        "language": {"type": "text", "default": "en"}
      }
    },
    {
      "name": "template_variables",
      "type": "object",
      "required": false,
      "description": "Variables to substitute in the template",
      "default": {}
    },
    {
      "name": "options",
      "type": "object",
      "required": false,
      "description": "Template generation options",
      "default": {"format": "html", "include_text_version": true},
      "properties": {
        "format": {"type": "text", "default": "html", "enum": ["html", "text", "both"]},
        "include_text_version": {"type": "boolean", "default": true},
        "priority": {"type": "text", "default": "normal", "enum": ["low", "normal", "high"]}
      }
    }
  ]
}
```

### Background Task Input Configuration

**Data Sync Task:**

```javascript
// Background task inputs for automated data synchronization
{
  "task_name": "sync_external_data",
  "schedule": "0 */6 * * *", // Every 6 hours
  "inputs": [
    {
      "name": "source_systems",
      "type": "array",
      "required": true,
      "description": "List of external systems to sync from",
      "validation": {
        "min_items": 1,
        "item_type": "text",
        "allowed_values": ["crm", "inventory", "analytics", "support"]
      }
    },
    {
      "name": "sync_options",
      "type": "object",
      "required": false,
      "description": "Synchronization configuration options",
      "default": {
        "incremental": true,
        "batch_size": 100,
        "retry_failed": true
      },
      "properties": {
        "incremental": {"type": "boolean", "default": true},
        "batch_size": {"type": "integer", "default": 100, "min": 10, "max": 1000},
        "retry_failed": {"type": "boolean", "default": true},
        "timeout_seconds": {"type": "integer", "default": 300, "min": 60, "max": 3600}
      }
    }
  ]
}
```

## 🔐 **Input Validation and Security**

### Server-Side Validation

**Comprehensive Input Validation Function Stack:**

```javascript
// Input validation function stack pattern
[
  {
    "function": "create_variable",
    "name": "validation_errors",
    "value": []
  },
  {
    "function": "conditional",
    "condition": "{{ !request.body.email || request.body.email|length == 0 }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_errors",
        "operation": "append",
        "value": {"field": "email", "message": "Email is required"}
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ request.body.email && !request.body.email|matches('/^[^@]+@[^@]+\\.[^@]+$/') }}",
    "true_branch": [
      {
        "function": "update_variable", 
        "name": "validation_errors",
        "operation": "append",
        "value": {"field": "email", "message": "Invalid email format"}
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ request.body.password && request.body.password|length < 8 }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "validation_errors",
        "operation": "append", 
        "value": {"field": "password", "message": "Password must be at least 8 characters"}
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
  }
]
```

### Input Sanitization

**Security-Focused Input Processing:**

```javascript
// Input sanitization and security measures
[
  {
    "function": "create_variable",
    "name": "sanitized_input",
    "value": {
      "email": "{{ request.body.email|trim|lower|sanitize }}",
      "name": "{{ request.body.name|trim|escape_html }}",
      "description": "{{ request.body.description|trim|escape_html|truncate(500) }}",
      "tags": "{{ request.body.tags|array_filter|array_unique|slice(0,10) }}"
    }
  },
  {
    "function": "conditional",
    "condition": "{{ sanitized_input.email|length == 0 }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {"error": "Email cannot be empty after sanitization"}
      }
    ]
  }
]
```

## 📝 **Input Documentation Best Practices**

### OpenAPI/Swagger Documentation

**Comprehensive API Documentation:**

```yaml
# OpenAPI specification for Xano endpoint inputs
openapi: 3.0.0
info:
  title: User Management API
  version: 1.0.0

paths:
  /api/users:
    post:
      summary: Create new user account
      description: Creates a new user account with profile information and preferences
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
                  description: User's email address for account creation
                  example: "user@example.com"
                  maxLength: 255
                password:
                  type: string
                  description: Account password (must meet security requirements)
                  minLength: 8
                  pattern: "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]"
                profile:
                  type: object
                  required:
                    - first_name
                    - last_name
                  properties:
                    first_name:
                      type: string
                      maxLength: 50
                      example: "John"
                    last_name:
                      type: string
                      maxLength: 50
                      example: "Doe"
                    date_of_birth:
                      type: string
                      format: date
                      example: "1990-01-15"
                preferences:
                  type: object
                  description: User preferences and settings
                  properties:
                    notifications:
                      type: boolean
                      default: true
                      description: Enable email notifications
                    newsletter:
                      type: boolean
                      default: false
                      description: Subscribe to newsletter
                    language:
                      type: string
                      default: "en"
                      enum: ["en", "es", "fr", "de"]
                      description: Preferred language
```

### Interactive Documentation

**Self-Documenting API Inputs:**

```javascript
// Generate dynamic input documentation
[
  {
    "function": "create_variable",
    "name": "endpoint_documentation",
    "value": {
      "endpoint": "/api/users",
      "method": "POST",
      "description": "Create new user account with comprehensive validation",
      "inputs": [
        {
          "name": "email",
          "type": "email",
          "required": true,
          "description": "User's email address for account creation",
          "validation": "Must be valid email format, max 255 characters",
          "example": "user@example.com"
        },
        {
          "name": "password", 
          "type": "text",
          "required": true,
          "description": "Secure password for account access",
          "validation": "Minimum 8 characters, must include uppercase, lowercase, number, and special character",
          "example": "SecurePass123!"
        }
      ],
      "examples": {
        "basic_registration": {
          "email": "john.doe@example.com",
          "password": "SecurePass123!",
          "profile": {
            "first_name": "John",
            "last_name": "Doe"
          }
        }
      }
    }
  }
]
```

## 💡 **Pro Tips**

- **Start Simple**: Begin with required inputs, add optional parameters later
- **Validate Early**: Implement input validation at the beginning of function stacks
- **Document Everything**: Clear input descriptions improve developer experience
- **Use Defaults Wisely**: Provide sensible defaults for optional parameters
- **Security First**: Always sanitize and validate user inputs
- **Test Edge Cases**: Verify behavior with empty, null, and invalid inputs

## 🔧 **Troubleshooting**

### Common Input Issues

**Problem**: Required inputs not being validated  
**Solution**: Ensure validation functions are placed before any data processing

**Problem**: Default values not applying  
**Solution**: Check input configuration and verify default value syntax

**Problem**: File uploads failing  
**Solution**: Verify file size limits, content types, and storage configuration

**Problem**: Complex object inputs not parsing correctly  
**Solution**: Validate JSON structure and use proper object notation

---

**Next Steps**: Ready to implement robust inputs? Check out [Custom Functions](custom-functions.md) for function creation or explore [Building with Visual Development](building-with-visual-development.md) for complete workflow design