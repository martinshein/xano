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
- Custom Functions
- Reusable Logic
- Business Logic
title: 'Custom Functions'
---

# Custom Functions

## 📋 **Quick Summary**
Custom functions are reusable business logic components that centralize common operations across your Xano backend. Build once, use everywhere - perfect for maintaining consistent functionality across APIs while keeping code DRY and maintainable. Essential for complex n8n, WeWeb, and automation workflows.

## 🎯 **Core Concepts**

### What Are Custom Functions?
Custom functions are reusable business logic components that work like internal APIs. They have inputs, function stacks, and responses, but unlike regular APIs, they cannot be called externally. Instead, they serve as building blocks that can be inserted into other function stacks.

### Key Benefits
- **DRY Principle**: Write once, use everywhere
- **Centralized Maintenance**: Update logic in one place, changes reflect everywhere
- **Modular Architecture**: Break complex workflows into manageable components
- **Consistent Behavior**: Ensure uniform business logic across your application
- **Easy Testing**: Test complex logic in isolation

### Custom Function Components
- **Inputs**: Parameters the function needs to execute
- **Function Stack**: Business logic and processing steps
- **Response**: Data returned to the calling function stack
- **Metadata**: Name, description, tags, and organization folders

## 🛠️ **Creating Custom Functions**

### Step-by-Step Creation Process

```javascript
// Custom Function Structure
{
  "function_name": "validate_user_email",
  "description": "Validates email format and checks if user exists",
  "inputs": [
    {
      "name": "email",
      "type": "text",
      "required": true,
      "description": "Email address to validate"
    }
  ],
  "function_stack": [
    {
      "function": "Text Manipulation",
      "operation": "lowercase",
      "input": "{{inputs.email}}",
      "output_variable": "normalized_email"
    },
    {
      "function": "Regular Expression",
      "pattern": "^[\\w\\.-]+@[\\w\\.-]+\\.[a-zA-Z]{2,}$",
      "input": "{{normalized_email}}",
      "output_variable": "is_valid_format"
    },
    {
      "function": "Conditional",
      "condition": "{{is_valid_format === false}}",
      "true_steps": [
        {
          "function": "Response",
          "body": {
            "valid": false,
            "error": "Invalid email format"
          }
        }
      ]
    },
    {
      "function": "Get Record",
      "table": "users",
      "filter": {
        "email": "{{normalized_email}}"
      },
      "output_variable": "existing_user"
    }
  ],
  "response": {
    "valid": "{{is_valid_format}}",
    "exists": "{{existing_user !== null}}",
    "normalized_email": "{{normalized_email}}"
  }
}
```

### Navigation and Setup

1. **Access Custom Functions**: Click "Custom Functions" in the left sidebar
2. **Create New Function**: Click "+ Add Function"
3. **Configure Settings**: Set name, description, tags, and folder organization
4. **Build Function Stack**: Add business logic using visual builder
5. **Test Function**: Use built-in testing interface
6. **Deploy**: Save and use in other function stacks

## 🔄 **Using Custom Functions**

### Inserting Custom Functions into APIs

```javascript
// API Endpoint using Custom Function
{
  "endpoint": "/auth/register",
  "method": "POST",
  "function_stack": [
    {
      "function": "Custom Function",
      "custom_function_name": "validate_user_email",
      "inputs": {
        "email": "{{inputs.email}}"
      },
      "output_variable": "email_validation"
    },
    {
      "function": "Conditional",
      "condition": "{{email_validation.valid === false}}",
      "true_steps": [
        {
          "function": "Response",
          "status_code": 400,
          "body": "{{email_validation}}"
        }
      ]
    },
    {
      "function": "Conditional",
      "condition": "{{email_validation.exists === true}}",
      "true_steps": [
        {
          "function": "Response",
          "status_code": 409,
          "body": {
            "error": "User already exists"
          }
        }
      ]
    },
    {
      "function": "Add Record",
      "table": "users",
      "data": {
        "email": "{{email_validation.normalized_email}}",
        "password": "{{inputs.password | hash}}",
        "created_at": "{{timestamp}}"
      }
    }
  ]
}
```

### Nested Custom Functions

```javascript
// Custom Function calling another Custom Function
{
  "function_name": "process_user_registration",
  "inputs": [
    {
      "name": "email",
      "type": "text"
    },
    {
      "name": "password", 
      "type": "text"
    },
    {
      "name": "profile_data",
      "type": "object"
    }
  ],
  "function_stack": [
    // Step 1: Validate email
    {
      "function": "Custom Function",
      "custom_function_name": "validate_user_email",
      "inputs": {
        "email": "{{inputs.email}}"
      },
      "output_variable": "email_validation"
    },
    // Step 2: Validate password
    {
      "function": "Custom Function", 
      "custom_function_name": "validate_password_strength",
      "inputs": {
        "password": "{{inputs.password}}"
      },
      "output_variable": "password_validation"
    },
    // Step 3: Create user if validations pass
    {
      "function": "Conditional",
      "condition": "{{email_validation.valid && password_validation.valid}}",
      "true_steps": [
        {
          "function": "Custom Function",
          "custom_function_name": "create_user_account",
          "inputs": {
            "email": "{{email_validation.normalized_email}}",
            "password": "{{inputs.password}}",
            "profile": "{{inputs.profile_data}}"
          }
        }
      ]
    }
  ]
}
```

## 🔗 **Integration Examples**

### n8n Workflow with Custom Functions

```javascript
// n8n workflow calling Xano API that uses custom functions
{
  "workflow": "User Onboarding",
  "nodes": [
    {
      "node_type": "Webhook",
      "name": "Receive Registration",
      "settings": {
        "path": "register-user",
        "method": "POST"
      }
    },
    {
      "node_type": "HTTP Request",
      "name": "Create User in Xano",
      "settings": {
        "method": "POST",
        "url": "https://your-xano.xano.io/api:v1/auth/register",
        "headers": {
          "Content-Type": "application/json"
        },
        "body": {
          "email": "{{$json.email}}",
          "password": "{{$json.password}}",
          "profile_data": {
            "first_name": "{{$json.first_name}}",
            "last_name": "{{$json.last_name}}",
            "company": "{{$json.company}}"
          }
        }
      }
    },
    {
      "node_type": "Switch",
      "name": "Check Registration Result",
      "settings": {
        "rules": [
          {
            "condition": "{{$json.success === true}}",
            "output": "success"
          },
          {
            "condition": "{{$json.success === false}}",
            "output": "error"
          }
        ]
      }
    },
    {
      "node_type": "HTTP Request",
      "name": "Send Welcome Email",
      "output_from": "success",
      "settings": {
        "method": "POST",
        "url": "{{$json.webhook_url}}",
        "body": {
          "to": "{{$json.user.email}}",
          "template": "welcome",
          "data": {
            "name": "{{$json.user.profile.first_name}}"
          }
        }
      }
    }
  ]
}
```

### WeWeb Component Integration

```vue
<template>
  <div class="user-registration-form">
    <form @submit.prevent="registerUser">
      <div class="form-group">
        <input 
          v-model="formData.email" 
          type="email" 
          placeholder="Email Address"
          :class="{ 'error': validationErrors.email }"
        />
        <span v-if="validationErrors.email" class="error-message">
          {{ validationErrors.email }}
        </span>
      </div>
      
      <div class="form-group">
        <input 
          v-model="formData.password" 
          type="password" 
          placeholder="Password"
          :class="{ 'error': validationErrors.password }"
        />
        <span v-if="validationErrors.password" class="error-message">
          {{ validationErrors.password }}
        </span>
      </div>
      
      <div class="form-group">
        <input 
          v-model="formData.first_name" 
          type="text" 
          placeholder="First Name"
        />
      </div>
      
      <button 
        type="submit" 
        :disabled="isLoading"
        class="register-button"
      >
        {{ isLoading ? 'Creating Account...' : 'Register' }}
      </button>
    </form>
    
    <div v-if="registrationResult.success" class="success-message">
      Account created successfully! Check your email to verify.
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        email: '',
        password: '',
        first_name: '',
        last_name: ''
      },
      validationErrors: {},
      isLoading: false,
      registrationResult: {}
    }
  },
  methods: {
    async registerUser() {
      this.isLoading = true
      this.validationErrors = {}
      
      try {
        // Call Xano API endpoint that uses custom functions
        const response = await this.$xano.auth.post('/register', {
          email: this.formData.email,
          password: this.formData.password,
          profile_data: {
            first_name: this.formData.first_name,
            last_name: this.formData.last_name
          }
        })
        
        if (response.success) {
          this.registrationResult = response
          // Redirect or show success message
          this.$router.push('/login?registered=true')
        }
        
      } catch (error) {
        if (error.response?.data?.validation_errors) {
          // Handle validation errors from custom functions
          this.validationErrors = error.response.data.validation_errors
        } else if (error.response?.status === 409) {
          this.validationErrors.email = 'This email is already registered'
        } else {
          this.validationErrors.general = 'Registration failed. Please try again.'
        }
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>
```

## 🚀 **Advanced Patterns**

### Error Handling in Custom Functions

```javascript
// Error Handling Custom Function
{
  "function_name": "safe_external_api_call",
  "description": "Makes external API calls with comprehensive error handling",
  "inputs": [
    {
      "name": "api_url",
      "type": "text"
    },
    {
      "name": "method",
      "type": "text",
      "default": "GET"
    },
    {
      "name": "payload",
      "type": "object",
      "required": false
    },
    {
      "name": "timeout",
      "type": "integer",
      "default": 5000
    }
  ],
  "function_stack": [
    {
      "function": "Try-Catch",
      "try_steps": [
        {
          "function": "External API Request",
          "url": "{{inputs.api_url}}",
          "method": "{{inputs.method}}",
          "body": "{{inputs.payload}}",
          "timeout": "{{inputs.timeout}}",
          "output_variable": "api_response"
        }
      ],
      "catch_steps": [
        {
          "function": "Switch",
          "input": "{{error.type}}",
          "cases": [
            {
              "value": "timeout",
              "steps": [
                {
                  "function": "Add Record",
                  "table": "api_logs",
                  "data": {
                    "url": "{{inputs.api_url}}",
                    "status": "timeout",
                    "error": "Request timeout",
                    "timestamp": "{{timestamp}}"
                  }
                }
              ]
            },
            {
              "value": "network_error",
              "steps": [
                {
                  "function": "Add Record",
                  "table": "api_logs",
                  "data": {
                    "url": "{{inputs.api_url}}",
                    "status": "network_error",
                    "error": "{{error.message}}",
                    "timestamp": "{{timestamp}}"
                  }
                }
              ]
            }
          ],
          "default_steps": [
            {
              "function": "Add Record",
              "table": "api_logs", 
              "data": {
                "url": "{{inputs.api_url}}",
                "status": "unknown_error",
                "error": "{{error.message}}",
                "timestamp": "{{timestamp}}"
              }
            }
          ]
        }
      ]
    }
  ],
  "response": {
    "success": "{{api_response !== null}}",
    "data": "{{api_response}}",
    "error": "{{error.message || null}}"
  }
}
```

### Data Transformation Custom Functions

```javascript
// Data Processing Custom Function
{
  "function_name": "transform_user_data",
  "description": "Standardizes and enriches user data from various sources",
  "inputs": [
    {
      "name": "raw_user_data",
      "type": "object"
    },
    {
      "name": "source",
      "type": "text"
    }
  ],
  "function_stack": [
    {
      "function": "Switch",
      "input": "{{inputs.source}}",
      "cases": [
        {
          "value": "google_oauth",
          "steps": [
            {
              "function": "Create Variable",
              "variable": "standardized_data",
              "value": {
                "email": "{{inputs.raw_user_data.email}}",
                "first_name": "{{inputs.raw_user_data.given_name}}",
                "last_name": "{{inputs.raw_user_data.family_name}}",
                "avatar_url": "{{inputs.raw_user_data.picture}}",
                "provider": "google",
                "provider_id": "{{inputs.raw_user_data.sub}}"
              }
            }
          ]
        },
        {
          "value": "facebook_oauth",
          "steps": [
            {
              "function": "Create Variable",
              "variable": "standardized_data",
              "value": {
                "email": "{{inputs.raw_user_data.email}}",
                "first_name": "{{inputs.raw_user_data.first_name}}",
                "last_name": "{{inputs.raw_user_data.last_name}}",
                "avatar_url": "{{inputs.raw_user_data.picture.data.url}}",
                "provider": "facebook",
                "provider_id": "{{inputs.raw_user_data.id}}"
              }
            }
          ]
        },
        {
          "value": "manual_registration",
          "steps": [
            {
              "function": "Create Variable",
              "variable": "standardized_data",
              "value": {
                "email": "{{inputs.raw_user_data.email}}",
                "first_name": "{{inputs.raw_user_data.first_name}}",
                "last_name": "{{inputs.raw_user_data.last_name}}",
                "provider": "manual",
                "provider_id": null
              }
            }
          ]
        }
      ]
    },
    // Add computed fields
    {
      "function": "Update Variable",
      "variable": "standardized_data",
      "operation": "merge",
      "value": {
        "full_name": "{{standardized_data.first_name}} {{standardized_data.last_name}}",
        "username": "{{standardized_data.email | split('@') | first}}",
        "created_at": "{{timestamp}}",
        "updated_at": "{{timestamp}}"
      }
    },
    // Generate user slug
    {
      "function": "Text Manipulation",
      "operation": "slug",
      "input": "{{standardized_data.full_name}}",
      "output_variable": "user_slug"
    },
    {
      "function": "Update Variable",
      "variable": "standardized_data",
      "operation": "set_key",
      "key": "slug",
      "value": "{{user_slug}}"
    }
  ],
  "response": "{{standardized_data}}"
}
```

### Conditional Logic Custom Functions

```javascript
// Business Rules Custom Function
{
  "function_name": "calculate_pricing_tier",
  "description": "Determines user pricing tier based on usage and profile",
  "inputs": [
    {
      "name": "user_id",
      "type": "integer"
    },
    {
      "name": "usage_data",
      "type": "object"
    }
  ],
  "function_stack": [
    {
      "function": "Get Record",
      "table": "users",
      "record_id": "{{inputs.user_id}}",
      "output_variable": "user"
    },
    {
      "function": "Query All Records",
      "table": "subscriptions",
      "filter": {
        "user_id": "{{inputs.user_id}}",
        "status": "active"
      },
      "output_variable": "active_subscriptions"
    },
    {
      "function": "Conditional",
      "condition": "{{active_subscriptions.length > 0}}",
      "true_steps": [
        {
          "function": "Response",
          "body": {
            "tier": "{{active_subscriptions[0].tier}}",
            "reason": "active_subscription"
          }
        }
      ],
      "false_steps": [
        {
          "function": "Math",
          "operation": "add",
          "values": [
            "{{inputs.usage_data.api_calls || 0}}",
            "{{inputs.usage_data.storage_gb || 0}}",
            "{{inputs.usage_data.bandwidth_gb || 0}}"
          ],
          "output_variable": "usage_score"
        },
        {
          "function": "Conditional",
          "condition": "{{usage_score > 1000}}",
          "true_steps": [
            {
              "function": "Response",
              "body": {
                "tier": "enterprise",
                "reason": "high_usage",
                "usage_score": "{{usage_score}}"
              }
            }
          ],
          "false_steps": [
            {
              "function": "Conditional",
              "condition": "{{usage_score > 100}}",
              "true_steps": [
                {
                  "function": "Response",
                  "body": {
                    "tier": "professional",
                    "reason": "moderate_usage",
                    "usage_score": "{{usage_score}}"
                  }
                }
              ],
              "false_steps": [
                {
                  "function": "Response",
                  "body": {
                    "tier": "starter",
                    "reason": "low_usage",
                    "usage_score": "{{usage_score}}"
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## 📁 **Organization and Management**

### Function Folders and Organization

```javascript
// Folder Structure Best Practices
{
  "folder_organization": {
    "authentication": [
      "validate_user_email",
      "hash_password",
      "generate_jwt_token",
      "verify_jwt_token"
    ],
    "data_processing": [
      "transform_user_data",
      "sanitize_input",
      "validate_schema",
      "format_response"
    ],
    "external_integrations": [
      "safe_external_api_call",
      "send_email_notification",
      "upload_to_s3",
      "process_payment"
    ],
    "business_logic": [
      "calculate_pricing_tier",
      "apply_discount_rules",
      "check_inventory_availability",
      "generate_order_summary"
    ]
  }
}
```

### Function Documentation Standards

```javascript
// Documentation Best Practices
{
  "function_name": "descriptive_action_name",
  "description": "Clear, concise explanation of what the function does and when to use it",
  "tags": ["category", "feature", "integration"],
  "inputs": [
    {
      "name": "parameter_name",
      "type": "data_type",
      "required": true,
      "description": "Detailed explanation of this parameter",
      "example": "sample_value"
    }
  ],
  "response_format": {
    "success": "boolean",
    "data": "object",
    "error": "string or null"
  },
  "use_cases": [
    "User registration validation",
    "Data import processing",
    "API response transformation"
  ]
}
```

## 🎯 **Best Practices**

### 1. Function Design Principles

```javascript
// Single Responsibility Principle
{
  "good_example": {
    "function_name": "validate_email_format",
    "purpose": "Only validates email format - one clear responsibility"
  },
  "bad_example": {
    "function_name": "process_user_registration_and_send_email_and_log_activity",
    "purpose": "Too many responsibilities - should be split into multiple functions"
  }
}
```

### 2. Input Validation

```javascript
// Always validate inputs in custom functions
{
  "function_stack": [
    {
      "function": "Conditional",
      "condition": "{{inputs.email === null || inputs.email === ''}}",
      "true_steps": [
        {
          "function": "Response",
          "status_code": 400,
          "body": {
            "error": "Email is required",
            "field": "email"
          }
        }
      ]
    },
    // Continue with main logic only after validation
    {
      "function": "Text Manipulation",
      "operation": "lowercase",
      "input": "{{inputs.email}}"
    }
  ]
}
```

### 3. Error Handling

```javascript
// Consistent error response format
{
  "error_response_standard": {
    "success": false,
    "error": {
      "message": "Human-readable error message",
      "code": "ERROR_CODE",
      "field": "field_that_caused_error",
      "details": "Additional technical details"
    }
  }
}
```

### 4. Performance Optimization

```javascript
// Optimize database queries in custom functions
{
  "performance_tips": {
    "database_queries": "Only fetch fields you need",
    "external_apis": "Implement timeout and retry logic",
    "caching": "Cache expensive computations",
    "parallel_processing": "Use parallel loops for independent operations"
  }
}
```

## 🔧 **Converting Existing Logic**

### From API Endpoint to Custom Function

```javascript
// Original API endpoint
{
  "endpoint": "/validate-user",
  "method": "POST",
  "function_stack": [
    {
      "function": "Get Record",
      "table": "users",
      "filter": {"email": "{{inputs.email}}"}
    },
    {
      "function": "Conditional",
      "condition": "{{user !== null}}",
      "true_steps": [
        {"function": "Response", "body": {"exists": true}}
      ],
      "false_steps": [
        {"function": "Response", "body": {"exists": false}}
      ]
    }
  ]
}

// Converted to Custom Function
{
  "function_name": "check_user_exists",
  "inputs": [{"name": "email", "type": "text"}],
  "function_stack": [
    {
      "function": "Get Record",
      "table": "users", 
      "filter": {"email": "{{inputs.email}}"}
    }
  ],
  "response": {
    "exists": "{{user !== null}}",
    "user_id": "{{user.id || null}}"
  }
}
```

### Extracting Logic from Complex Workflows

```javascript
// Select specific steps in function stack editor:
// 1. Highlight the steps you want to extract
// 2. Click "Convert to Function" button
// 3. Configure inputs/outputs
// 4. Replace original steps with custom function call

{
  "extraction_workflow": [
    "Select steps in visual editor",
    "Click 'Convert to Function' button", 
    "Configure function name and description",
    "Map inputs from selected steps",
    "Define response structure",
    "Test extracted function",
    "Replace original steps with function call"
  ]
}
```

## 🔍 **Testing and Debugging**

### Built-in Testing Interface

```javascript
// Test Custom Function with sample data
{
  "test_configuration": {
    "function_name": "validate_user_email",
    "test_inputs": {
      "email": "test@example.com"
    },
    "expected_output": {
      "valid": true,
      "exists": false,
      "normalized_email": "test@example.com"
    }
  }
}
```

### Debug Mode

```javascript
// Enable debug mode to inspect variable values
{
  "debug_features": {
    "step_by_step_execution": "Watch each function execute",
    "variable_inspection": "See variable values at each step",
    "performance_metrics": "Monitor execution time",
    "error_details": "Detailed error messages and stack traces"
  }
}
```

---

*Custom functions are the key to building maintainable, scalable Xano backends. They promote code reuse, consistency, and make complex applications much easier to manage and debug.*