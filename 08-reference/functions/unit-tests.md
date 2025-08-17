---
title: Unit Tests Functions Reference
description: Complete guide to implementing unit testing in Xano - automated testing, test suites, mocking, and quality assurance for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- unit-tests
- testing
- quality-assurance
- test-automation
- mocking
- test-suites
- ci-cd
- debugging
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 02-core-concepts/function-stack/testing.md
- 08-reference/functions/background-tasks.md
- 08-reference/functions/middleware.md
---

## 📋 **Quick Summary**

Unit testing in Xano enables automated testing of function stacks, API endpoints, and business logic to ensure code quality and reliability. It includes test creation, execution, mocking, and integration with CI/CD workflows.

## What You'll Learn

- How to create and organize unit tests in Xano
- Test suite creation and management
- Mocking external dependencies and services
- Assertion patterns and validation techniques
- Integration testing for complex workflows
- CI/CD pipeline integration for automated testing
- Best practices for test coverage and maintainability

## Understanding Unit Testing in Xano

### Test Types and Scope

**Unit Tests:**
- Test individual functions in isolation
- Mock external dependencies
- Fast execution and focused scope
- Validate specific business logic

**Integration Tests:**
- Test multiple functions working together
- Include real database operations
- Validate end-to-end workflows
- Test API endpoint behavior

**System Tests:**
- Test complete user scenarios
- Include external service interactions
- Validate system behavior under load
- Test deployment configurations

### Test Execution Flow

```javascript
// Test execution lifecycle
Test Setup → Execute Function → Assert Results → Cleanup
    ↓              ↓               ↓           ↓
Mock Data    Run Function    Validate     Reset State
```

## Basic Unit Test Implementation

### 1. Simple Function Test

```javascript
// Basic unit test for a calculation function
{
  "test_name": "calculate_order_total",
  "description": "Test order total calculation with tax and discount",
  "test_setup": [
    {
      "function": "create_test_data",
      "data": {
        "order_items": [
          {"price": 10.00, "quantity": 2},
          {"price": 15.50, "quantity": 1}
        ],
        "tax_rate": 0.08,
        "discount_percent": 10
      }
    }
  ],
  "test_execution": [
    {
      "function": "calculate_order_total",
      "items": "{{test_data.order_items}}",
      "tax_rate": "{{test_data.tax_rate}}",
      "discount": "{{test_data.discount_percent}}"
    }
  ],
  "assertions": [
    {
      "assertion": "equals",
      "actual": "{{calculate_order_total.subtotal}}",
      "expected": 35.50,
      "message": "Subtotal should be 35.50"
    },
    {
      "assertion": "equals",
      "actual": "{{calculate_order_total.tax_amount}}",
      "expected": 2.56,
      "message": "Tax amount should be 2.56"
    },
    {
      "assertion": "equals",
      "actual": "{{calculate_order_total.final_total}}",
      "expected": 34.40,
      "message": "Final total should be 34.40"
    }
  ],
  "cleanup": [
    {
      "function": "clear_test_data"
    }
  ]
}
```

### 2. API Endpoint Test

```javascript
// Test API endpoint behavior
{
  "test_name": "user_registration_endpoint",
  "description": "Test user registration with validation",
  "test_setup": [
    {
      "function": "create_test_database",
      "table": "users"
    },
    {
      "function": "mock_email_service",
      "return_value": {"success": true, "message_id": "test_123"}
    }
  ],
  "test_cases": [
    {
      "name": "valid_registration",
      "request": {
        "method": "POST",
        "endpoint": "/api/register",
        "body": {
          "email": "test@example.com",
          "password": "SecurePass123!",
          "name": "Test User"
        }
      },
      "expected_response": {
        "status": 201,
        "body_contains": {
          "user_id": "{{any_integer}}",
          "email": "test@example.com",
          "status": "pending_verification"
        }
      },
      "assertions": [
        {
          "assertion": "database_record_exists",
          "table": "users",
          "filter": {"email": "test@example.com"},
          "message": "User should be created in database"
        },
        {
          "assertion": "mock_called",
          "mock": "email_service",
          "times": 1,
          "message": "Verification email should be sent"
        }
      ]
    },
    {
      "name": "duplicate_email",
      "pre_setup": [
        {
          "function": "add_record",
          "table": "users",
          "data": {"email": "existing@example.com", "status": "active"}
        }
      ],
      "request": {
        "method": "POST",
        "endpoint": "/api/register",
        "body": {
          "email": "existing@example.com",
          "password": "SecurePass123!",
          "name": "Test User"
        }
      },
      "expected_response": {
        "status": 409,
        "body_contains": {
          "error": "Email already exists"
        }
      }
    }
  ]
}
```

### 3. Database Operation Test

```javascript
// Test database operations with transactions
{
  "test_name": "order_processing_transaction",
  "description": "Test order processing with inventory update",
  "test_setup": [
    {
      "function": "create_test_products",
      "products": [
        {"id": 1, "name": "Product A", "stock": 10, "price": 25.00},
        {"id": 2, "name": "Product B", "stock": 5, "price": 40.00}
      ]
    }
  ],
  "test_execution": [
    {
      "function": "database_transaction",
      "operations": [
        {
          "function": "add_record",
          "table": "orders",
          "data": {
            "customer_id": 123,
            "status": "pending",
            "total": 90.00
          }
        },
        {
          "function": "add_record",
          "table": "order_items",
          "data": [
            {"order_id": "{{orders.id}}", "product_id": 1, "quantity": 2},
            {"order_id": "{{orders.id}}", "product_id": 2, "quantity": 1}
          ]
        },
        {
          "function": "update_inventory",
          "updates": [
            {"product_id": 1, "quantity_change": -2},
            {"product_id": 2, "quantity_change": -1}
          ]
        }
      ]
    }
  ],
  "assertions": [
    {
      "assertion": "database_record_exists",
      "table": "orders",
      "filter": {"customer_id": 123, "status": "pending"}
    },
    {
      "assertion": "equals",
      "actual": "{{get_product_stock(1)}}",
      "expected": 8,
      "message": "Product A stock should be reduced to 8"
    },
    {
      "assertion": "equals",
      "actual": "{{get_product_stock(2)}}",
      "expected": 4,
      "message": "Product B stock should be reduced to 4"
    }
  ]
}
```

## Advanced Testing Patterns

### 1. Mocking External Services

```javascript
// Mock external API services
{
  "test_name": "payment_processing_with_mocks",
  "description": "Test payment processing with external service mocks",
  "mocks": [
    {
      "mock_name": "stripe_payment_api",
      "service_url": "https://api.stripe.com/v1/payment_intents",
      "responses": {
        "success": {
          "status": 200,
          "body": {
            "id": "pi_test_123",
            "status": "succeeded",
            "amount": 2000,
            "currency": "usd"
          }
        },
        "failure": {
          "status": 400,
          "body": {
            "error": {
              "code": "card_declined",
              "message": "Your card was declined."
            }
          }
        }
      }
    },
    {
      "mock_name": "email_service",
      "service_url": "https://api.sendgrid.com/v3/mail/send",
      "responses": {
        "success": {
          "status": 202,
          "body": {"message": "Email sent successfully"}
        }
      }
    }
  ],
  "test_cases": [
    {
      "name": "successful_payment",
      "mock_behavior": {
        "stripe_payment_api": "success",
        "email_service": "success"
      },
      "test_execution": [
        {
          "function": "process_payment",
          "amount": 20.00,
          "currency": "usd",
          "payment_method": "card_test_123"
        }
      ],
      "assertions": [
        {
          "assertion": "mock_called",
          "mock": "stripe_payment_api",
          "with_params": {
            "amount": 2000,
            "currency": "usd"
          }
        },
        {
          "assertion": "equals",
          "actual": "{{process_payment.status}}",
          "expected": "succeeded"
        }
      ]
    }
  ]
}
```

### 2. Test Data Factories

```javascript
// Reusable test data factories
{
  "test_data_factories": {
    "user_factory": {
      "default": {
        "email": "user{{random_number()}}@example.com",
        "name": "Test User {{random_number()}}",
        "password": "SecurePass123!",
        "status": "active",
        "created_at": "{{now()}}"
      },
      "admin": {
        "email": "admin{{random_number()}}@example.com",
        "name": "Admin User {{random_number()}}",
        "password": "AdminPass123!",
        "role": "admin",
        "status": "active"
      },
      "inactive": {
        "email": "inactive{{random_number()}}@example.com",
        "name": "Inactive User",
        "status": "inactive"
      }
    },
    "product_factory": {
      "default": {
        "name": "Test Product {{random_number()}}",
        "price": "{{random_decimal(10, 100)}}",
        "stock": "{{random_integer(1, 50)}}",
        "category": "electronics",
        "status": "active"
      },
      "out_of_stock": {
        "name": "Out of Stock Product",
        "price": 25.99,
        "stock": 0,
        "status": "active"
      }
    }
  },
  "factory_usage": [
    {
      "function": "create_test_user",
      "factory": "user_factory",
      "variant": "admin",
      "overrides": {
        "email": "specific@example.com"
      }
    }
  ]
}
```

### 3. Parameterized Tests

```javascript
// Data-driven parameterized tests
{
  "test_name": "email_validation_scenarios",
  "description": "Test email validation with multiple scenarios",
  "parameters": [
    {
      "email": "valid@example.com",
      "expected_valid": true,
      "description": "Valid email format"
    },
    {
      "email": "invalid.email",
      "expected_valid": false,
      "description": "Missing @ symbol"
    },
    {
      "email": "@example.com",
      "expected_valid": false,
      "description": "Missing local part"
    },
    {
      "email": "user@",
      "expected_valid": false,
      "description": "Missing domain"
    },
    {
      "email": "user@example",
      "expected_valid": false,
      "description": "Missing TLD"
    },
    {
      "email": "user+tag@example.com",
      "expected_valid": true,
      "description": "Email with plus addressing"
    }
  ],
  "test_template": {
    "test_execution": [
      {
        "function": "validate_email",
        "email": "{{parameter.email}}"
      }
    ],
    "assertions": [
      {
        "assertion": "equals",
        "actual": "{{validate_email.is_valid}}",
        "expected": "{{parameter.expected_valid}}",
        "message": "{{parameter.description}}: {{parameter.email}}"
      }
    ]
  }
}
```

## Test Suite Organization

### 1. Test Suite Structure

```javascript
// Comprehensive test suite organization
{
  "test_suite": {
    "name": "User Management API",
    "description": "Complete test suite for user management functionality",
    "setup": [
      {
        "function": "create_test_database",
        "tables": ["users", "user_sessions", "user_profiles"]
      },
      {
        "function": "load_test_fixtures",
        "fixtures": ["test_users.json", "test_roles.json"]
      }
    ],
    "teardown": [
      {
        "function": "cleanup_test_database"
      },
      {
        "function": "reset_mocks"
      }
    ],
    "test_groups": [
      {
        "group": "Authentication Tests",
        "tests": [
          "user_registration_test",
          "user_login_test",
          "password_reset_test",
          "token_validation_test"
        ]
      },
      {
        "group": "Profile Management Tests",
        "tests": [
          "profile_update_test",
          "profile_validation_test",
          "profile_image_upload_test"
        ]
      },
      {
        "group": "Security Tests",
        "tests": [
          "rate_limiting_test",
          "sql_injection_prevention_test",
          "xss_prevention_test"
        ]
      }
    ]
  }
}
```

### 2. Continuous Integration Tests

```javascript
// CI/CD pipeline test configuration
{
  "ci_test_configuration": {
    "pipeline_name": "xano_api_tests",
    "triggers": ["push", "pull_request", "scheduled"],
    "environments": {
      "test": {
        "database_url": "{{env.TEST_DATABASE_URL}}",
        "api_base_url": "{{env.TEST_API_URL}}",
        "external_services": "mocked"
      },
      "staging": {
        "database_url": "{{env.STAGING_DATABASE_URL}}",
        "api_base_url": "{{env.STAGING_API_URL}}",
        "external_services": "sandbox"
      }
    },
    "test_stages": [
      {
        "stage": "unit_tests",
        "parallel": true,
        "tests": ["unit/**/*.test.js"],
        "timeout": 300
      },
      {
        "stage": "integration_tests",
        "parallel": false,
        "tests": ["integration/**/*.test.js"],
        "timeout": 600,
        "depends_on": ["unit_tests"]
      },
      {
        "stage": "e2e_tests",
        "parallel": false,
        "tests": ["e2e/**/*.test.js"],
        "timeout": 900,
        "depends_on": ["integration_tests"],
        "run_condition": "branch == 'main'"
      }
    ],
    "reporting": {
      "formats": ["junit", "coverage", "html"],
      "coverage_threshold": 80,
      "notification_channels": ["slack", "email"]
    }
  }
}
```

## No-Code Platform Testing Integration

### n8n Workflow Testing
```javascript
// Test n8n workflow integration
{
  "test_name": "n8n_webhook_processing",
  "description": "Test n8n webhook data processing",
  "test_setup": [
    {
      "function": "mock_n8n_webhook",
      "webhook_url": "https://hooks.n8n.cloud/webhook/test",
      "expected_payload": {
        "trigger": "order_created",
        "order_id": "{{test_order.id}}",
        "customer_email": "test@example.com"
      }
    }
  ],
  "test_execution": [
    {
      "function": "trigger_order_created_event",
      "order_data": "{{test_order}}"
    }
  ],
  "assertions": [
    {
      "assertion": "webhook_called",
      "webhook": "n8n_webhook",
      "within_seconds": 5,
      "with_payload": {
        "trigger": "order_created",
        "order_id": "{{test_order.id}}"
      }
    }
  ]
}
```

### WeWeb Component Testing
```javascript
// Test WeWeb component data flow
{
  "test_name": "weweb_component_data_binding",
  "description": "Test data binding for WeWeb components",
  "test_setup": [
    {
      "function": "create_test_component_data",
      "component": "user_dashboard",
      "data": {
        "user_stats": {
          "orders_count": 5,
          "total_spent": 150.00,
          "loyalty_points": 75
        }
      }
    }
  ],
  "test_execution": [
    {
      "function": "get_dashboard_data",
      "user_id": "{{test_user.id}}"
    }
  ],
  "assertions": [
    {
      "assertion": "has_properties",
      "actual": "{{get_dashboard_data.response}}",
      "expected_properties": [
        "orders_count",
        "total_spent", 
        "loyalty_points",
        "recent_orders"
      ]
    },
    {
      "assertion": "equals",
      "actual": "{{get_dashboard_data.response.orders_count}}",
      "expected": 5
    }
  ]
}
```

### Make.com Scenario Testing
```javascript
// Test Make.com scenario triggers
{
  "test_name": "make_scenario_execution",
  "description": "Test Make.com scenario triggering",
  "test_setup": [
    {
      "function": "mock_make_webhook",
      "scenario_id": "123456",
      "webhook_url": "https://hook.us1.make.com/test-webhook"
    }
  ],
  "test_execution": [
    {
      "function": "process_customer_signup",
      "customer_data": {
        "email": "newcustomer@example.com",
        "source": "website_form"
      }
    }
  ],
  "assertions": [
    {
      "assertion": "webhook_received",
      "webhook": "make_webhook",
      "payload_contains": {
        "event": "customer_signup",
        "customer_email": "newcustomer@example.com"
      }
    }
  ]
}
```

## Performance and Load Testing

### 1. Performance Benchmarks

```javascript
// Performance testing configuration
{
  "performance_tests": [
    {
      "test_name": "api_response_time",
      "description": "Test API response time under normal load",
      "endpoint": "/api/users",
      "method": "GET",
      "concurrent_users": 10,
      "duration_seconds": 60,
      "assertions": [
        {
          "metric": "average_response_time",
          "threshold": 200,
          "unit": "milliseconds"
        },
        {
          "metric": "95th_percentile_response_time",
          "threshold": 500,
          "unit": "milliseconds"
        },
        {
          "metric": "error_rate",
          "threshold": 1,
          "unit": "percentage"
        }
      ]
    },
    {
      "test_name": "database_query_performance",
      "description": "Test database query performance",
      "queries": [
        {
          "name": "user_lookup",
          "query": "SELECT * FROM users WHERE email = ?",
          "parameters": ["test@example.com"],
          "max_execution_time": 50
        },
        {
          "name": "order_history",
          "query": "SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC LIMIT 10",
          "parameters": [123],
          "max_execution_time": 100
        }
      ]
    }
  ]
}
```

### 2. Load Testing Scenarios

```javascript
// Load testing configuration
{
  "load_tests": [
    {
      "scenario": "user_registration_load",
      "description": "Test user registration under heavy load",
      "load_pattern": "ramp_up",
      "users": {
        "start": 1,
        "end": 100,
        "ramp_duration": 300
      },
      "test_duration": 600,
      "user_behavior": [
        {
          "action": "register_user",
          "weight": 70,
          "think_time": 2
        },
        {
          "action": "login_user", 
          "weight": 30,
          "think_time": 1
        }
      ],
      "success_criteria": [
        {
          "metric": "error_rate",
          "threshold": 2,
          "unit": "percentage"
        },
        {
          "metric": "throughput",
          "threshold": 50,
          "unit": "requests_per_second"
        }
      ]
    }
  ]
}
```

## Try This: Complete Test Implementation

Create a comprehensive test for a user authentication system:

```javascript
// Complete authentication test suite
{
  "test_suite": "user_authentication_complete",
  "description": "Complete test suite for user authentication",
  "global_setup": [
    {
      "function": "create_test_environment",
      "database": "test_auth_db",
      "tables": ["users", "sessions", "password_resets"]
    },
    {
      "function": "setup_mocks",
      "services": ["email_service", "sms_service"]
    }
  ],
  "tests": [
    {
      "name": "complete_user_registration_flow",
      "steps": [
        {
          "description": "Register new user",
          "action": "POST /api/register",
          "data": {
            "email": "test@example.com",
            "password": "SecurePass123!",
            "name": "Test User"
          },
          "assertions": [
            {"status": 201},
            {"body_contains": {"user_id": "{{any_integer}}"}}
          ]
        },
        {
          "description": "Verify email was sent",
          "assertions": [
            {
              "assertion": "mock_called",
              "mock": "email_service",
              "with_template": "email_verification"
            }
          ]
        },
        {
          "description": "Activate user account",
          "action": "GET /api/verify/{{verification_token}}",
          "assertions": [
            {"status": 200},
            {"body_contains": {"message": "Account verified"}}
          ]
        },
        {
          "description": "Login with activated account",
          "action": "POST /api/login",
          "data": {
            "email": "test@example.com",
            "password": "SecurePass123!"
          },
          "assertions": [
            {"status": 200},
            {"body_contains": {"access_token": "{{any_string}}"}}
          ]
        }
      ]
    }
  ],
  "global_teardown": [
    {
      "function": "cleanup_test_environment"
    }
  ]
}
```

## Common Testing Mistakes to Avoid

### ❌ Poor Practices
- Testing implementation details instead of behavior
- Not using proper test isolation
- Creating flaky tests with timing dependencies
- Missing edge case coverage
- Not maintaining test data properly

### ✅ Best Practices
- Focus on testing behavior, not implementation
- Use proper setup/teardown for test isolation
- Mock external dependencies consistently
- Test both happy path and error scenarios
- Maintain clear and descriptive test names

## Pro Tips

### 💡 **Test Organization**
- Group related tests in test suites
- Use descriptive test names and descriptions
- Implement proper test data management
- Create reusable test utilities and factories

### 🔒 **Quality Assurance**
- Aim for high test coverage of critical paths
- Include security testing scenarios
- Test error handling and edge cases
- Validate performance under load

### 📊 **Monitoring and Reporting**
- Track test execution metrics
- Monitor test suite performance
- Generate comprehensive test reports
- Set up alerts for test failures

### 🔄 **CI/CD Integration**
- Run tests on every code change
- Use different test environments appropriately
- Implement proper test result reporting
- Set up automated deployment based on test results

## Troubleshooting Test Issues

### Common Problems
1. **Flaky tests**: Improve test isolation and remove timing dependencies
2. **Slow test execution**: Optimize database operations and use mocking
3. **Test data conflicts**: Implement proper cleanup and unique test data
4. **Mock configuration issues**: Verify mock setup and reset procedures

Unit testing in Xano provides comprehensive quality assurance capabilities for function stacks, APIs, and business logic. Proper implementation ensures reliable, maintainable code and confident deployments.