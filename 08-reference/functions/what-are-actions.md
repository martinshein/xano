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
- Actions
- Zero-dependency
- Marketplace
- Integrations
- Community
title: 'Xano Actions & Zero-Dependency Functions'
---

# Xano Actions & Zero-Dependency Functions

## 📋 **Quick Summary**
Xano Actions are powerful, zero-dependency functions that can be created, shared, forked, and installed by anyone. They provide reusable business logic and integrations without requiring database dependencies, making them perfect for community sharing and seamless integration across different Xano workspaces.

## 🎯 **Core Concepts**

### What are Actions?
Actions are lightweight, self-contained functions designed for specific processes like external API integrations or business logic execution. Unlike custom functions, Actions have zero dependencies, making them universally shareable and easy to integrate.

### Zero-Dependency Architecture
Actions are designed to be completely self-contained, requiring no external dependencies from your workspace, which enables seamless sharing and integration across different Xano instances.

## 🚀 **Key Features**

### Action Capabilities

```javascript
// What Actions can do
{
  "action_capabilities": {
    "external_integrations": {
      "description": "Connect to third-party APIs and services",
      "examples": [
        "Stripe payment processing",
        "SendGrid email sending",
        "Slack notifications",
        "Google Sheets integration"
      ]
    },
    "data_processing": {
      "description": "Transform and manipulate data",
      "examples": [
        "JSON transformation",
        "String manipulation",
        "Mathematical calculations",
        "Date/time processing"
      ]
    },
    "business_logic": {
      "description": "Reusable business logic components",
      "examples": [
        "Validation functions",
        "Formatting utilities",
        "Complex calculations",
        "Decision algorithms"
      ]
    },
    "utility_functions": {
      "description": "Common utility operations",
      "examples": [
        "Data encryption/decryption",
        "File format conversion",
        "Text parsing",
        "URL manipulation"
      ]
    }
  }
}
```

### Zero-Dependency Restrictions

```javascript
// What Actions cannot contain
{
  "restrictions": {
    "database_operations": {
      "not_allowed": [
        "Database request functions",
        "Direct table access",
        "Custom database tables"
      ],
      "reason": "Maintains zero-dependency architecture"
    },
    "workspace_dependencies": {
      "not_allowed": [
        "Environment variables (except Settings Registry)",
        "Middleware functions",
        "Lambda functions",
        "Redis caching operations"
      ],
      "reason": "Ensures portability across workspaces"
    },
    "complex_dependencies": {
      "not_allowed": [
        "Multiple Xano objects",
        "Docker microservices",
        "External file dependencies"
      ],
      "reason": "Maintains simplicity and shareability"
    }
  }
}
```

## 🛠️ **Creating Actions**

### Basic Action Structure

```javascript
// Example: Email Validation Action
{
  "action_name": "Email Validator",
  "description": "Validates email addresses with comprehensive checks",
  "category": "Utilities",
  "inputs": [
    {
      "name": "email",
      "type": "text",
      "required": true,
      "description": "Email address to validate"
    },
    {
      "name": "strict_mode",
      "type": "boolean",
      "default": false,
      "description": "Enable strict validation rules"
    }
  ],
  "function_stack": [
    {
      "function": "Create Variable",
      "variable_name": "email_pattern",
      "value": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    },
    {
      "function": "Text",
      "operation": "lowercase",
      "text": "{{inputs.email}}",
      "output_variable": "normalized_email"
    },
    {
      "function": "Text",
      "operation": "regex_match",
      "text": "{{normalized_email}}",
      "pattern": "{{email_pattern}}",
      "output_variable": "basic_valid"
    },
    {
      "function": "Conditional",
      "condition": "{{inputs.strict_mode === true}}",
      "true_steps": [
        {
          "function": "External API Request",
          "url": "https://api.email-validator.net/api/verify",
          "method": "GET",
          "query_parameters": {
            "EmailAddress": "{{normalized_email}}"
          },
          "output_variable": "advanced_validation"
        },
        {
          "function": "Response",
          "body": {
            "email": "{{normalized_email}}",
            "is_valid": "{{basic_valid && advanced_validation.status === 'valid'}}",
            "validation_type": "strict",
            "details": {
              "format_valid": "{{basic_valid}}",
              "domain_valid": "{{advanced_validation.status === 'valid'}}",
              "disposable": "{{advanced_validation.disposable || false}}"
            }
          }
        }
      ],
      "false_steps": [
        {
          "function": "Response",
          "body": {
            "email": "{{normalized_email}}",
            "is_valid": "{{basic_valid}}",
            "validation_type": "basic",
            "details": {
              "format_valid": "{{basic_valid}}"
            }
          }
        }
      ]
    }
  ]
}
```

### Advanced Action with Settings Registry

```javascript
// Example: Stripe Payment Processing Action
{
  "action_name": "Stripe Payment Processor",
  "description": "Process payments through Stripe with comprehensive error handling",
  "category": "Payments",
  "inputs": [
    {
      "name": "stripe_secret_key",
      "type": "text",
      "required": true,
      "settings_registry": true,
      "description": "Stripe Secret Key (from Settings Registry)"
    },
    {
      "name": "amount",
      "type": "number",
      "required": true,
      "description": "Payment amount in cents"
    },
    {
      "name": "currency",
      "type": "text",
      "default": "usd",
      "description": "Payment currency"
    },
    {
      "name": "customer_email",
      "type": "text",
      "required": true,
      "description": "Customer email address"
    },
    {
      "name": "description",
      "type": "text",
      "description": "Payment description"
    }
  ],
  "function_stack": [
    // Validate amount
    {
      "function": "Conditional",
      "condition": "{{inputs.amount < 50}}",
      "true_steps": [
        {
          "function": "Response",
          "status_code": 400,
          "body": {
            "error": "Amount must be at least $0.50",
            "code": "AMOUNT_TOO_LOW"
          }
        }
      ]
    },
    // Create Payment Intent
    {
      "function": "External API Request",
      "url": "https://api.stripe.com/v1/payment_intents",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{inputs.stripe_secret_key}}",
        "Content-Type": "application/x-www-form-urlencoded"
      },
      "body": "amount={{inputs.amount}}&currency={{inputs.currency}}&receipt_email={{inputs.customer_email}}&description={{inputs.description || 'Payment via Xano Action'}}",
      "output_variable": "payment_intent"
    },
    // Handle Stripe response
    {
      "function": "Conditional",
      "condition": "{{payment_intent.error !== null}}",
      "true_steps": [
        {
          "function": "Response",
          "status_code": 400,
          "body": {
            "error": "Payment failed",
            "details": "{{payment_intent.error.message}}",
            "code": "{{payment_intent.error.code}}"
          }
        }
      ],
      "false_steps": [
        {
          "function": "Response",
          "body": {
            "success": true,
            "payment_intent_id": "{{payment_intent.id}}",
            "client_secret": "{{payment_intent.client_secret}}",
            "amount": "{{payment_intent.amount}}",
            "currency": "{{payment_intent.currency}}",
            "status": "{{payment_intent.status}}"
          }
        }
      ]
    }
  ]
}
```

## 🔗 **Integration Examples**

### Using Actions in Function Stacks

```javascript
// Main API endpoint using Actions
{
  "endpoint": "/process-user-registration",
  "method": "POST",
  "function_stack": [
    // Use Email Validation Action
    {
      "function": "Action",
      "action_name": "Email Validator",
      "inputs": {
        "email": "{{inputs.email}}",
        "strict_mode": true
      },
      "output_variable": "email_validation"
    },
    // Check validation result
    {
      "function": "Conditional",
      "condition": "{{email_validation.is_valid === false}}",
      "true_steps": [
        {
          "function": "Response",
          "status_code": 400,
          "body": {
            "error": "Invalid email address",
            "details": "{{email_validation.details}}"
          }
        }
      ]
    },
    // Create user in database
    {
      "function": "Add Record",
      "table": "users",
      "data": {
        "email": "{{email_validation.email}}",
        "first_name": "{{inputs.first_name}}",
        "last_name": "{{inputs.last_name}}",
        "status": "pending"
      },
      "output_variable": "new_user"
    },
    // Use another Action for welcome email
    {
      "function": "Action",
      "action_name": "SendGrid Email Sender",
      "inputs": {
        "api_key": "{{env.SENDGRID_API_KEY}}",
        "to_email": "{{new_user.email}}",
        "template_id": "welcome_template",
        "dynamic_data": {
          "user_name": "{{new_user.first_name}}",
          "activation_link": "{{base_url}}/activate/{{new_user.id}}"
        }
      },
      "output_variable": "email_result"
    },
    {
      "function": "Response",
      "status_code": 201,
      "body": {
        "user": "{{new_user}}",
        "email_sent": "{{email_result.success}}",
        "message": "User registered successfully"
      }
    }
  ]
}
```

### n8n Integration with Actions

```javascript
// n8n workflow leveraging Xano Actions
{
  "workflow_name": "E-commerce Order Processing",
  "trigger": {
    "type": "Webhook",
    "path": "new-order"
  },
  "nodes": [
    {
      "name": "Validate Order Data",
      "type": "Code",
      "code": `
        const order = $input.first().json;
        if (!order.items || !order.customer_email) {
          throw new Error('Missing required order data');
        }
        return { order };
      `
    },
    {
      "name": "Process Payment (Xano Action)",
      "type": "HTTP Request",
      "parameters": {
        "method": "POST",
        "url": "https://your-xano.xano.io/api:v1/action/stripe-payment-processor",
        "headers": {
          "Authorization": "Bearer {{$credentials.xanoApi.token}}",
          "Content-Type": "application/json"
        },
        "body": {
          "amount": "={{Math.round($json.order.total * 100)}}",
          "currency": "usd",
          "customer_email": "={{$json.order.customer_email}}",
          "description": "Order #{{$json.order.id}}"
        }
      }
    },
    {
      "name": "Send Confirmation Email",
      "type": "HTTP Request",
      "parameters": {
        "method": "POST",
        "url": "https://your-xano.xano.io/api:v1/action/sendgrid-email-sender",
        "body": {
          "to_email": "={{$json.order.customer_email}}",
          "template_id": "order_confirmation",
          "dynamic_data": {
            "order_id": "={{$json.order.id}}",
            "payment_intent_id": "={{$node['Process Payment (Xano Action)'].json.payment_intent_id}}"
          }
        }
      }
    }
  ]
}
```

### WeWeb Action Integration

```javascript
// WeWeb workflow using Xano Actions
{
  "component_name": "ContactForm",
  "data": {
    "form": {
      "name": "",
      "email": "",
      "message": "",
      "phone": ""
    },
    "submitting": false,
    "errors": {}
  },
  "methods": {
    "validateForm": `
      // Use Xano Action for email validation
      const emailValidation = await this.$xano.callAction('email-validator', {
        email: this.form.email,
        strict_mode: true
      });
      
      if (!emailValidation.is_valid) {
        this.errors.email = 'Please enter a valid email address';
        return false;
      }
      
      // Use Xano Action for phone validation
      if (this.form.phone) {
        const phoneValidation = await this.$xano.callAction('phone-validator', {
          phone: this.form.phone,
          country_code: 'US'
        });
        
        if (!phoneValidation.is_valid) {
          this.errors.phone = 'Please enter a valid phone number';
          return false;
        }
      }
      
      return true;
    `,
    "submitForm": `
      this.submitting = true;
      this.errors = {};
      
      try {
        // Validate form using Actions
        if (!(await this.validateForm())) {
          this.submitting = false;
          return;
        }
        
        // Submit form data
        const response = await this.$xano.post('/contact-submissions', this.form);
        
        // Send notification using Action
        await this.$xano.callAction('slack-notifier', {
          channel: '#leads',
          message: \`New contact form submission from \${this.form.name} (\${this.form.email})\`
        });
        
        this.$toast.success('Thank you for your message!');
        this.form = { name: '', email: '', message: '', phone: '' };
        
      } catch (error) {
        this.errors.general = 'Something went wrong. Please try again.';
      } finally {
        this.submitting = false;
      }
    `
  }
}
```

## 📦 **Action Packages**

### Creating Action Packages

```javascript
// Example: E-commerce Action Package
{
  "package_name": "E-commerce Essentials",
  "description": "Complete set of actions for e-commerce functionality",
  "category": "E-commerce",
  "version": "1.2.0",
  "actions": [
    {
      "name": "Product Validator",
      "description": "Validate product data before creating/updating"
    },
    {
      "name": "Inventory Manager",
      "description": "Check and update inventory levels"
    },
    {
      "name": "Price Calculator",
      "description": "Calculate pricing with taxes and discounts"
    },
    {
      "name": "Order Processor",
      "description": "Process and validate orders"
    },
    {
      "name": "Shipping Calculator",
      "description": "Calculate shipping costs and delivery times"
    }
  ],
  "installation_guide": `
    # E-commerce Essentials Package

    ## Quick Start
    1. Install the package in your Xano workspace
    2. Configure your settings registry values:
       - STRIPE_SECRET_KEY
       - SHIPSTATION_API_KEY
       - TAX_SERVICE_API_KEY
    3. Use actions in your function stacks

    ## Example Usage
    Use the Product Validator action before creating products:
    
    \`\`\`javascript
    {
      "function": "Action",
      "action_name": "Product Validator",
      "inputs": {
        "product_data": "{{inputs.product}}"
      }
    }
    \`\`\`
  `
}
```

## 🚀 **Advanced Action Patterns**

### Conditional Logic Action

```javascript
// Complex business logic action
{
  "action_name": "Subscription Tier Calculator",
  "description": "Calculate appropriate subscription tier based on usage",
  "inputs": [
    {
      "name": "monthly_api_calls",
      "type": "number",
      "required": true
    },
    {
      "name": "storage_gb",
      "type": "number",
      "required": true
    },
    {
      "name": "team_members",
      "type": "number",
      "default": 1
    },
    {
      "name": "features_required",
      "type": "array",
      "description": "List of required features"
    }
  ],
  "function_stack": [
    {
      "function": "Create Variable",
      "variable_name": "tier_rules",
      "value": {
        "starter": {
          "max_api_calls": 10000,
          "max_storage": 5,
          "max_team_members": 1,
          "features": ["basic_analytics"]
        },
        "professional": {
          "max_api_calls": 100000,
          "max_storage": 50,
          "max_team_members": 5,
          "features": ["basic_analytics", "advanced_reporting", "webhooks"]
        },
        "enterprise": {
          "max_api_calls": 1000000,
          "max_storage": 500,
          "max_team_members": 50,
          "features": ["basic_analytics", "advanced_reporting", "webhooks", "custom_integrations", "priority_support"]
        }
      }
    },
    {
      "function": "Create Variable",
      "variable_name": "recommended_tier",
      "value": "starter"
    },
    // Check Professional tier requirements
    {
      "function": "Conditional",
      "condition": "{{inputs.monthly_api_calls > tier_rules.starter.max_api_calls || inputs.storage_gb > tier_rules.starter.max_storage || inputs.team_members > tier_rules.starter.max_team_members}}",
      "true_steps": [
        {
          "function": "Update Variable",
          "variable_name": "recommended_tier",
          "value": "professional"
        }
      ]
    },
    // Check Enterprise tier requirements
    {
      "function": "Conditional",
      "condition": "{{inputs.monthly_api_calls > tier_rules.professional.max_api_calls || inputs.storage_gb > tier_rules.professional.max_storage || inputs.team_members > tier_rules.professional.max_team_members}}",
      "true_steps": [
        {
          "function": "Update Variable",
          "variable_name": "recommended_tier",
          "value": "enterprise"
        }
      ]
    },
    // Check feature requirements
    {
      "function": "Loop",
      "input_array": "{{inputs.features_required || []}}",
      "loop_item_variable": "required_feature",
      "steps": [
        {
          "function": "Conditional",
          "condition": "{{!tier_rules[recommended_tier].features.includes(required_feature)}}",
          "true_steps": [
            {
              "function": "Conditional",
              "condition": "{{tier_rules.professional.features.includes(required_feature) && recommended_tier === 'starter'}}",
              "true_steps": [
                {
                  "function": "Update Variable",
                  "variable_name": "recommended_tier",
                  "value": "professional"
                }
              ]
            },
            {
              "function": "Conditional",
              "condition": "{{tier_rules.enterprise.features.includes(required_feature) && recommended_tier !== 'enterprise'}}",
              "true_steps": [
                {
                  "function": "Update Variable",
                  "variable_name": "recommended_tier",
                  "value": "enterprise"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "function": "Response",
      "body": {
        "recommended_tier": "{{recommended_tier}}",
        "usage_analysis": {
          "api_calls": "{{inputs.monthly_api_calls}}",
          "storage_gb": "{{inputs.storage_gb}}",
          "team_members": "{{inputs.team_members}}"
        },
        "tier_details": "{{tier_rules[recommended_tier]}}",
        "upgrade_reasons": "{{recommended_tier !== 'starter' ? 'Usage exceeds starter limits' : 'Current usage fits starter plan'}}"
      }
    }
  ]
}
```

## 🛠️ **Action Development Best Practices**

### Error Handling

```javascript
// Robust error handling in Actions
{
  "error_handling_pattern": {
    "input_validation": [
      {
        "function": "Conditional",
        "condition": "{{inputs.required_field === null || inputs.required_field === ''}}",
        "true_steps": [
          {
            "function": "Response",
            "status_code": 400,
            "body": {
              "error": "Missing required field",
              "field": "required_field",
              "code": "VALIDATION_ERROR"
            }
          }
        ]
      }
    ],
    "external_api_handling": [
      {
        "function": "Try-Catch",
        "try_steps": [
          {
            "function": "External API Request",
            "url": "https://api.example.com/endpoint",
            "timeout": 10000
          }
        ],
        "catch_steps": [
          {
            "function": "Switch",
            "variable": "{{error.status_code}}",
            "cases": {
              "404": [
                {
                  "function": "Response",
                  "status_code": 404,
                  "body": {
                    "error": "Resource not found",
                    "code": "NOT_FOUND"
                  }
                }
              ],
              "429": [
                {
                  "function": "Response",
                  "status_code": 429,
                  "body": {
                    "error": "Rate limit exceeded",
                    "code": "RATE_LIMIT_EXCEEDED",
                    "retry_after": "{{error.headers['Retry-After'] || 60}}"
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
                  "code": "SERVICE_ERROR"
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

### Testing and Documentation

```javascript
// Action testing and documentation approach
{
  "testing_strategy": {
    "unit_tests": [
      {
        "test_name": "Valid email validation",
        "inputs": {
          "email": "user@example.com",
          "strict_mode": false
        },
        "expected_output": {
          "is_valid": true,
          "validation_type": "basic"
        }
      },
      {
        "test_name": "Invalid email validation",
        "inputs": {
          "email": "invalid-email",
          "strict_mode": false
        },
        "expected_output": {
          "is_valid": false,
          "validation_type": "basic"
        }
      }
    ],
    "integration_tests": [
      {
        "test_name": "Full workflow with external API",
        "setup": "Mock external API responses",
        "inputs": "Real-world data scenarios",
        "validation": "End-to-end functionality"
      }
    ]
  },
  "documentation_format": `
    # Action Name
    
    ## Description
    Brief description of what the action does.
    
    ## Inputs
    - **field_name** (type, required): Description
    
    ## Outputs
    - **result_field** (type): Description
    
    ## Settings Registry
    - **API_KEY**: Required API key for external service
    
    ## Usage Examples
    \`\`\`javascript
    {
      "function": "Action",
      "action_name": "Your Action",
      "inputs": {
        "field": "value"
      }
    }
    \`\`\`
    
    ## Error Handling
    List of possible error codes and their meanings.
  `
}
```

## 📈 **Action Marketplace & Community**

### Publishing Guidelines

```javascript
// Action publishing checklist
{
  "publishing_requirements": {
    "code_quality": [
      "Comprehensive error handling",
      "Input validation",
      "Proper response formatting",
      "Performance optimization"
    ],
    "documentation": [
      "Clear description",
      "Complete input/output documentation",
      "Usage examples",
      "Error code reference"
    ],
    "testing": [
      "Unit tests for all scenarios",
      "Edge case validation",
      "Performance testing",
      "Security validation"
    ],
    "metadata": [
      "Appropriate category",
      "Relevant tags",
      "Version number",
      "License information"
    ]
  },
  "visibility_options": {
    "public": "Available to all users in marketplace",
    "private": "Internal use only",
    "unlisted": "Accessible via direct URL only"
  }
}
```

---

*Actions provide a powerful way to create and share reusable functionality across the Xano ecosystem, enabling developers to build more efficiently by leveraging community-created components and contributing their own solutions back to the platform.*