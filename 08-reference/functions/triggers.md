---
title: Database Triggers Functions Reference
description: Complete guide to implementing database triggers in Xano - automatic execution of functions based on database events for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- triggers
- database-events
- automation
- before-after-hooks
- data-validation
- audit-logging
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 02-core-concepts/function-stack/database-requests.md
- 08-reference/functions/webhooks.md
- 08-reference/functions/background-tasks.md
---

## 📋 **Quick Summary**

Database triggers in Xano automatically execute function stacks when specific database events occur. They enable data validation, audit logging, real-time notifications, and complex business logic automation without manual intervention.

## What You'll Learn

- How to create and configure database triggers
- Before and after trigger implementations
- Common trigger patterns for data validation and logging
- Trigger integration with no-code platforms
- Best practices for trigger performance and reliability
- Advanced trigger scenarios and error handling

## Understanding Database Triggers

### Trigger Types and Events

**Insert Triggers:**
- Execute when new records are created
- Useful for data validation and initialization
- Can modify data before saving

**Update Triggers:**
- Execute when existing records are modified
- Track changes and maintain audit trails
- Implement business rule validation

**Delete Triggers:**
- Execute when records are removed
- Handle cascading deletions and cleanup
- Archive data before deletion

### Before vs After Triggers

```javascript
// Before triggers - modify data before database operation
{
  "trigger_type": "before_insert",
  "table": "users",
  "function_stack": [
    {
      "function": "create_variable",
      "name": "hashed_password",
      "value": "{{hash_password(input.password)}}"
    },
    {
      "function": "update_variable",
      "variable": "input.password",
      "value": "{{hashed_password}}"
    }
  ]
}

// After triggers - react to completed database operations
{
  "trigger_type": "after_insert",
  "table": "orders",
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "{{env.EMAIL_SERVICE_URL}}",
      "data": {
        "template": "order_confirmation",
        "to": "{{new_record.customer_email}}",
        "order_id": "{{new_record.id}}"
      }
    }
  ]
}
```

## Common Trigger Implementations

### 1. Data Validation and Transformation

```javascript
// Email validation and normalization
{
  "trigger": "before_insert",
  "table": "users",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{!is_valid_email(input.email)}}",
      "true_stack": [
        {
          "function": "throw_error",
          "message": "Invalid email format",
          "code": "VALIDATION_ERROR"
        }
      ]
    },
    {
      "function": "update_variable",
      "variable": "input.email",
      "value": "{{lowercase(trim(input.email))}}"
    },
    {
      "function": "update_variable",
      "variable": "input.created_at",
      "value": "{{now()}}"
    }
  ]
}

// Price calculation trigger
{
  "trigger": "before_insert",
  "table": "order_items",
  "function_stack": [
    {
      "function": "get_record",
      "table": "products",
      "filter": {"id": "{{input.product_id}}"}
    },
    {
      "function": "update_variable",
      "variable": "input.unit_price",
      "value": "{{products.price}}"
    },
    {
      "function": "update_variable",
      "variable": "input.total_price",
      "value": "{{input.quantity * products.price}}"
    }
  ]
}
```

### 2. Audit Logging and Change Tracking

```javascript
// Comprehensive audit trail
{
  "trigger": "after_update",
  "table": "users",
  "function_stack": [
    {
      "function": "create_variable",
      "name": "changes",
      "value": "{{diff(old_record, new_record)}}"
    },
    {
      "function": "add_record",
      "table": "audit_log",
      "data": {
        "table_name": "users",
        "record_id": "{{new_record.id}}",
        "action": "update",
        "changes": "{{changes}}",
        "user_id": "{{auth.user.id}}",
        "timestamp": "{{now()}}",
        "ip_address": "{{request.ip}}"
      }
    }
  ]
}

// Status change logging
{
  "trigger": "after_update",
  "table": "orders",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{old_record.status}} != {{new_record.status}}",
      "true_stack": [
        {
          "function": "add_record",
          "table": "status_history",
          "data": {
            "order_id": "{{new_record.id}}",
            "old_status": "{{old_record.status}}",
            "new_status": "{{new_record.status}}",
            "changed_by": "{{auth.user.id}}",
            "changed_at": "{{now()}}"
          }
        }
      ]
    }
  ]
}
```

### 3. Real-time Notifications

```javascript
// User signup notification
{
  "trigger": "after_insert",
  "table": "users",
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "{{env.SLACK_WEBHOOK_URL}}",
      "data": {
        "text": "New user registered: {{new_record.email}}",
        "channel": "#notifications"
      }
    },
    {
      "function": "realtime_publish",
      "channel": "admin_dashboard",
      "event": "new_user",
      "data": {
        "user_id": "{{new_record.id}}",
        "email": "{{new_record.email}}",
        "registered_at": "{{new_record.created_at}}"
      }
    }
  ]
}

// Order status update notification
{
  "trigger": "after_update",
  "table": "orders",
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{new_record.status}} == 'shipped'",
      "true_stack": [
        {
          "function": "external_api_request",
          "url": "{{env.EMAIL_SERVICE_URL}}",
          "data": {
            "template": "order_shipped",
            "to": "{{new_record.customer_email}}",
            "tracking_number": "{{new_record.tracking_number}}"
          }
        }
      ]
    }
  ]
}
```

## No-Code Platform Integration

### n8n Workflow Triggers
```javascript
// Trigger n8n workflow from database changes
{
  "trigger": "after_insert",
  "table": "leads",
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "https://hooks.n8n.cloud/webhook/lead-processor",
      "method": "POST",
      "data": {
        "lead_id": "{{new_record.id}}",
        "email": "{{new_record.email}}",
        "source": "{{new_record.source}}",
        "score": "{{new_record.lead_score}}"
      }
    }
  ]
}
```

### WeWeb Component Updates
```javascript
// Update WeWeb interface in real-time
{
  "trigger": "after_update",
  "table": "tasks",
  "function_stack": [
    {
      "function": "realtime_publish",
      "channel": "project_{{new_record.project_id}}",
      "event": "task_updated",
      "data": {
        "task_id": "{{new_record.id}}",
        "status": "{{new_record.status}}",
        "assigned_to": "{{new_record.assigned_user_id}}",
        "updated_at": "{{now()}}"
      }
    }
  ]
}
```

### Make.com Scenario Triggers
```javascript
// Trigger Make.com scenario
{
  "trigger": "after_insert",
  "table": "support_tickets",
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "https://hook.us1.make.com/ticket-handler",
      "data": {
        "ticket_id": "{{new_record.id}}",
        "priority": "{{new_record.priority}}",
        "customer_id": "{{new_record.customer_id}}",
        "subject": "{{new_record.subject}}"
      }
    }
  ]
}
```

## Advanced Trigger Patterns

### 1. Cascading Operations
```javascript
// Cascade delete with cleanup
{
  "trigger": "before_delete",
  "table": "users",
  "function_stack": [
    {
      "function": "query_all_records",
      "table": "orders",
      "filter": {"user_id": "{{old_record.id}}"}
    },
    {
      "function": "for_each_loop",
      "array": "{{orders}}",
      "function_stack": [
        {
          "function": "edit_record",
          "table": "orders",
          "record_id": "{{loop_item.id}}",
          "data": {"user_id": null, "status": "orphaned"}
        }
      ]
    },
    {
      "function": "add_record",
      "table": "deleted_users_archive",
      "data": "{{old_record}}"
    }
  ]
}
```

### 2. Complex Business Logic
```javascript
// Inventory management trigger
{
  "trigger": "after_insert",
  "table": "order_items",
  "function_stack": [
    {
      "function": "get_record",
      "table": "products",
      "record_id": "{{new_record.product_id}}"
    },
    {
      "function": "create_variable",
      "name": "new_stock",
      "value": "{{products.stock_quantity - new_record.quantity}}"
    },
    {
      "function": "conditional",
      "condition": "{{new_stock < 0}}",
      "true_stack": [
        {
          "function": "throw_error",
          "message": "Insufficient stock",
          "code": "STOCK_ERROR"
        }
      ]
    },
    {
      "function": "edit_record",
      "table": "products",
      "record_id": "{{new_record.product_id}}",
      "data": {"stock_quantity": "{{new_stock}}"}
    },
    {
      "function": "conditional",
      "condition": "{{new_stock <= products.reorder_level}}",
      "true_stack": [
        {
          "function": "add_record",
          "table": "reorder_alerts",
          "data": {
            "product_id": "{{new_record.product_id}}",
            "current_stock": "{{new_stock}}",
            "reorder_level": "{{products.reorder_level}}",
            "created_at": "{{now()}}"
          }
        }
      ]
    }
  ]
}
```

### 3. Error Handling and Rollback
```javascript
// Robust error handling in triggers
{
  "trigger": "after_insert",
  "table": "payments",
  "function_stack": [
    {
      "function": "try_catch",
      "try_stack": [
        {
          "function": "external_api_request",
          "url": "{{env.PAYMENT_PROCESSOR_URL}}",
          "data": "{{new_record}}"
        },
        {
          "function": "edit_record",
          "table": "payments",
          "record_id": "{{new_record.id}}",
          "data": {"status": "processed"}
        }
      ],
      "catch_stack": [
        {
          "function": "edit_record",
          "table": "payments",
          "record_id": "{{new_record.id}}",
          "data": {"status": "failed", "error_message": "{{error.message}}"}
        },
        {
          "function": "add_record",
          "table": "payment_errors",
          "data": {
            "payment_id": "{{new_record.id}}",
            "error": "{{error}}",
            "timestamp": "{{now()}}"
          }
        }
      ]
    }
  ]
}
```

## Try This: Complete Trigger Setup

Create a comprehensive user registration system:

```javascript
// User registration trigger system
{
  "before_insert_trigger": {
    "table": "users",
    "function_stack": [
      {
        "function": "conditional",
        "condition": "{{!is_valid_email(input.email)}}",
        "true_stack": [{"function": "throw_error", "message": "Invalid email"}]
      },
      {
        "function": "update_variable",
        "variable": "input.email",
        "value": "{{lowercase(trim(input.email))}}"
      },
      {
        "function": "update_variable",
        "variable": "input.password",
        "value": "{{hash_password(input.password)}}"
      },
      {
        "function": "update_variable",
        "variable": "input.verification_token",
        "value": "{{generate_uuid()}}"
      }
    ]
  },
  "after_insert_trigger": {
    "table": "users",
    "function_stack": [
      {
        "function": "external_api_request",
        "url": "{{env.EMAIL_SERVICE_URL}}",
        "data": {
          "template": "email_verification",
          "to": "{{new_record.email}}",
          "verification_url": "{{env.APP_URL}}/verify/{{new_record.verification_token}}"
        }
      },
      {
        "function": "add_record",
        "table": "user_stats",
        "data": {
          "user_id": "{{new_record.id}}",
          "registration_date": "{{now()}}",
          "login_count": 0
        }
      },
      {
        "function": "realtime_publish",
        "channel": "admin_dashboard",
        "event": "new_user_registered",
        "data": {"user_id": "{{new_record.id}}", "email": "{{new_record.email}}"}
      }
    ]
  }
}
```

## Common Trigger Mistakes to Avoid

### ❌ Poor Practices
- Creating infinite trigger loops
- Not handling trigger failures gracefully
- Performing heavy operations in before triggers
- Missing error handling and validation
- Creating triggers without performance considerations

### ✅ Best Practices
- Use after triggers for external API calls
- Implement proper error handling
- Keep before triggers lightweight
- Add conditional logic to prevent unnecessary executions
- Test triggers thoroughly in development

## Pro Tips

### 💡 **Performance Optimization**
- Use background tasks for heavy operations
- Add conditions to prevent unnecessary trigger executions
- Index frequently filtered columns
- Batch similar operations when possible

### 🔒 **Security Considerations**
- Validate all trigger inputs
- Use environment variables for sensitive data
- Implement proper authorization checks
- Log trigger executions for audit trails

### 📊 **Monitoring and Debugging**
- Add logging to track trigger executions
- Monitor trigger performance metrics
- Set up alerts for trigger failures
- Use conditional logging for debugging

### 🔄 **Reliability Patterns**
- Implement retry logic for external calls
- Use try-catch blocks for error handling
- Create fallback mechanisms for failures
- Test edge cases thoroughly

## Troubleshooting Trigger Issues

### Common Problems
1. **Trigger loops**: Check for circular trigger dependencies
2. **Performance issues**: Review trigger complexity and frequency
3. **Data inconsistency**: Ensure proper error handling and rollback
4. **External API failures**: Implement retry logic and fallbacks

Database triggers provide powerful automation capabilities in Xano. Proper implementation ensures data integrity, business rule enforcement, and seamless integration with no-code platforms.