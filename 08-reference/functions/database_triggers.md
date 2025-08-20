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
- Triggers
- Automation
- Events
- Realtime
title: 'Database Triggers & Event Automation'
---

# Database Triggers & Event Automation

## 📋 **Quick Summary**
Database triggers in Xano are automated workflows that execute in response to database events like record creation, updates, or deletion. Build sophisticated event-driven automation that integrates seamlessly with n8n, WeWeb, and external systems for real-time data processing and business logic execution.

## 🎯 **Core Concepts**

### Event-Driven Architecture
Triggers enable reactive programming patterns where actions automatically happen in response to data changes, creating powerful automation workflows without manual intervention.

### Trigger Types Available
- **Database Triggers**: Respond to CRUD operations
- **Realtime Triggers**: React to channel events
- **Workspace Triggers**: Handle branch operations
- **MCP Triggers**: Manage server connections
- **AI Agent Triggers**: Control agent interactions

## 🔧 **Database Triggers**

### Trigger Events

```javascript
// Database operations that can trigger workflows
{
  "trigger_events": {
    "insert": {
      "description": "New record added to table",
      "data_available": "new record data",
      "use_cases": ["User registration", "Order creation", "Content publishing"]
    },
    "update": {
      "description": "Existing record modified",
      "data_available": "old and new record data",
      "use_cases": ["Status changes", "Profile updates", "Inventory adjustments"]
    },
    "delete": {
      "description": "Record removed from table",
      "data_available": "deleted record data",
      "use_cases": ["Cleanup operations", "Audit logging", "Cascade deletions"]
    },
    "truncate": {
      "description": "All records cleared from table",
      "data_available": "table information",
      "use_cases": ["Bulk resets", "Data migrations", "System maintenance"]
    }
  }
}
```

### Trigger Data Structure

```javascript
// Available inputs in database trigger workflows
{
  "trigger_inputs": {
    "new": {
      "description": "Contents of new/updated record",
      "available_on": ["insert", "update"],
      "example": {
        "id": 123,
        "email": "user@example.com",
        "status": "active",
        "created_at": "2025-01-23T10:00:00Z"
      }
    },
    "old": {
      "description": "Contents of record before change",
      "available_on": ["update", "delete"],
      "example": {
        "id": 123,
        "email": "user@example.com",
        "status": "pending",
        "created_at": "2025-01-23T09:00:00Z"
      }
    },
    "action": {
      "description": "Type of operation that triggered the event",
      "values": ["insert", "update", "delete", "truncate"],
      "example": "insert"
    },
    "data_source": {
      "description": "Database source where operation occurred",
      "example": "primary_database"
    }
  }
}
```

## 🛠️ **Implementation Examples**

### User Registration Automation

```javascript
// Trigger: User table INSERT
{
  "trigger_name": "new_user_onboarding",
  "table": "users",
  "events": ["insert"],
  "conditions": {
    "status": "active"
  },
  "workflow": [
    // Create default user preferences
    {
      "function": "Add Record",
      "table": "user_preferences",
      "data": {
        "user_id": "{{new.id}}",
        "notifications": true,
        "theme": "light",
        "language": "en"
      }
    },
    // Send welcome email asynchronously
    {
      "function": "Custom Function",
      "custom_function": "send_welcome_email",
      "execution_mode": "async",
      "parameters": {
        "user_email": "{{new.email}}",
        "user_name": "{{new.first_name}}",
        "user_id": "{{new.id}}"
      }
    },
    // Create initial activity log
    {
      "function": "Add Record",
      "table": "activity_logs",
      "data": {
        "user_id": "{{new.id}}",
        "action": "user_registered",
        "timestamp": "{{timestamp}}",
        "details": {
          "registration_method": "{{new.registration_source}}",
          "ip_address": "{{request.ip}}"
        }
      }
    },
    // Trigger external integrations
    {
      "function": "External API Request",
      "url": "{{env.CRM_WEBHOOK_URL}}",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{env.CRM_API_KEY}}",
        "Content-Type": "application/json"
      },
      "body": {
        "event": "user_registered",
        "user": "{{new}}",
        "timestamp": "{{timestamp}}"
      }
    }
  ]
}
```

### E-commerce Order Processing

```javascript
// Trigger: Orders table UPDATE when status changes
{
  "trigger_name": "order_status_automation",
  "table": "orders",
  "events": ["update"],
  "conditions": {
    "status_changed": "{{old.status !== new.status}}"
  },
  "workflow": [
    // Handle different status transitions
    {
      "function": "Switch",
      "variable": "{{new.status}}",
      "cases": {
        "confirmed": [
          {
            "function": "Custom Function",
            "custom_function": "process_payment",
            "parameters": {
              "order_id": "{{new.id}}",
              "amount": "{{new.total}}"
            }
          },
          {
            "function": "Custom Function",
            "custom_function": "update_inventory",
            "execution_mode": "async",
            "parameters": {
              "order_items": "{{new.items}}"
            }
          }
        ],
        "shipped": [
          {
            "function": "Custom Function",
            "custom_function": "send_shipping_notification",
            "parameters": {
              "customer_email": "{{new.customer.email}}",
              "tracking_number": "{{new.tracking_number}}",
              "order_id": "{{new.id}}"
            }
          }
        ],
        "cancelled": [
          {
            "function": "Custom Function",
            "custom_function": "process_refund",
            "parameters": {
              "order_id": "{{new.id}}",
              "reason": "{{new.cancellation_reason}}"
            }
          },
          {
            "function": "Custom Function",
            "custom_function": "restore_inventory",
            "parameters": {
              "order_items": "{{new.items}}"
            }
          }
        ]
      }
    },
    // Log status change
    {
      "function": "Add Record",
      "table": "order_history",
      "data": {
        "order_id": "{{new.id}}",
        "old_status": "{{old.status}}",
        "new_status": "{{new.status}}",
        "changed_at": "{{timestamp}}",
        "changed_by": "system"
      }
    }
  ]
}
```

### Content Moderation System

```javascript
// Trigger: Posts table INSERT for automatic moderation
{
  "trigger_name": "content_moderation",
  "table": "posts",
  "events": ["insert"],
  "workflow": [
    // Check content against moderation rules
    {
      "function": "External API Request",
      "url": "{{env.MODERATION_API_URL}}",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{env.MODERATION_API_KEY}}"
      },
      "body": {
        "content": "{{new.content}}",
        "title": "{{new.title}}"
      },
      "output_variable": "moderation_result"
    },
    // Handle moderation results
    {
      "function": "Conditional",
      "condition": "{{moderation_result.flagged === true}}",
      "true_steps": [
        {
          "function": "Edit Record",
          "table": "posts",
          "record_id": "{{new.id}}",
          "data": {
            "status": "under_review",
            "moderation_flags": "{{moderation_result.flags}}"
          }
        },
        {
          "function": "Add Record",
          "table": "moderation_queue",
          "data": {
            "post_id": "{{new.id}}",
            "flags": "{{moderation_result.flags}}",
            "confidence": "{{moderation_result.confidence}}",
            "created_at": "{{timestamp}}"
          }
        },
        {
          "function": "Custom Function",
          "custom_function": "notify_moderators",
          "parameters": {
            "post_id": "{{new.id}}",
            "flags": "{{moderation_result.flags}}"
          }
        }
      ],
      "false_steps": [
        {
          "function": "Edit Record",
          "table": "posts",
          "record_id": "{{new.id}}",
          "data": {
            "status": "published",
            "published_at": "{{timestamp}}"
          }
        }
      ]
    }
  ]
}
```

## 🔗 **Integration Examples**

### n8n Workflow Trigger Integration

```javascript
// Database trigger that notifies n8n workflow
{
  "trigger_name": "inventory_alert_n8n",
  "table": "products",
  "events": ["update"],
  "conditions": {
    "low_stock": "{{new.stock <= new.reorder_level && old.stock > new.reorder_level}}"
  },
  "workflow": [
    {
      "function": "External API Request",
      "url": "{{env.N8N_WEBHOOK_URL}}/inventory-alert",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": {
        "event": "low_stock_alert",
        "product": {
          "id": "{{new.id}}",
          "name": "{{new.name}}",
          "current_stock": "{{new.stock}}",
          "reorder_level": "{{new.reorder_level}}",
          "supplier": "{{new.supplier}}"
        },
        "timestamp": "{{timestamp}}"
      }
    }
  ]
}

// Corresponding n8n workflow
{
  "workflow_name": "Inventory Management",
  "trigger": {
    "node": "Webhook",
    "path": "inventory-alert"
  },
  "nodes": [
    {
      "name": "Check Supplier",
      "type": "IF",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.product.supplier}}",
              "operation": "notEmpty"
            }
          ]
        }
      }
    },
    {
      "name": "Generate Purchase Order",
      "type": "HTTP Request",
      "parameters": {
        "method": "POST",
        "url": "https://your-xano.xano.io/api:v1/purchase-orders",
        "body": {
          "product_id": "={{$json.product.id}}",
          "quantity": "={{$json.product.reorder_level * 2}}",
          "supplier": "={{$json.product.supplier}}"
        }
      }
    }
  ]
}
```

### WeWeb Real-time Updates

```javascript
// Database trigger for real-time UI updates
{
  "trigger_name": "user_activity_realtime",
  "table": "user_sessions",
  "events": ["insert", "update", "delete"],
  "workflow": [
    {
      "function": "Realtime Functions",
      "action": "broadcast",
      "channel": "admin_dashboard",
      "message": {
        "type": "user_activity_update",
        "action": "{{action}}",
        "user_data": "{{action === 'delete' ? old : new}}",
        "timestamp": "{{timestamp}}"
      }
    }
  ]
}

// WeWeb component listening for real-time updates
{
  "component_name": "LiveUsersDashboard",
  "realtime_connection": {
    "channel": "admin_dashboard",
    "endpoint": "wss://your-xano.xano.io/realtime"
  },
  "event_handlers": {
    "user_activity_update": {
      "handler": "updateUsersList",
      "code": `
        if (event.action === 'insert') {
          this.activeUsers.push(event.user_data);
        } else if (event.action === 'delete') {
          this.activeUsers = this.activeUsers.filter(u => u.id !== event.user_data.id);
        } else if (event.action === 'update') {
          const index = this.activeUsers.findIndex(u => u.id === event.user_data.id);
          if (index >= 0) this.activeUsers[index] = event.user_data;
        }
      `
    }
  }
}
```

## 🚀 **Advanced Trigger Patterns**

### Audit Trail Implementation

```javascript
// Universal audit trigger for all tables
{
  "trigger_name": "audit_trail",
  "table": "*", // Applied to all tables
  "events": ["insert", "update", "delete"],
  "workflow": [
    {
      "function": "Add Record",
      "table": "audit_logs",
      "data": {
        "table_name": "{{trigger.table_name}}",
        "record_id": "{{(action === 'delete' ? old : new).id}}",
        "action": "{{action}}",
        "old_data": "{{action === 'insert' ? null : old}}",
        "new_data": "{{action === 'delete' ? null : new}}",
        "user_id": "{{auth_user.id || null}}",
        "timestamp": "{{timestamp}}",
        "ip_address": "{{request.ip}}",
        "user_agent": "{{request.user_agent}}"
      }
    },
    // Conditional sensitive data alerts
    {
      "function": "Conditional",
      "condition": "{{trigger.table_name === 'users' && action === 'update' && (old.email !== new.email || old.password !== new.password)}}",
      "true_steps": [
        {
          "function": "Custom Function",
          "custom_function": "send_security_alert",
          "parameters": {
            "user_id": "{{new.id}}",
            "change_type": "{{old.email !== new.email ? 'email_change' : 'password_change'}}",
            "old_value": "{{old.email !== new.email ? old.email : 'password'}}",
            "new_value": "{{old.email !== new.email ? new.email : 'password'}}"
          }
        }
      ]
    }
  ]
}
```

### Data Synchronization

```javascript
// Multi-system data sync trigger
{
  "trigger_name": "customer_data_sync",
  "table": "customers",
  "events": ["insert", "update"],
  "conditions": {
    "sync_enabled": "{{new.sync_enabled === true}}"
  },
  "workflow": [
    {
      "function": "Create Variable",
      "variable_name": "sync_operations",
      "value": []
    },
    // Sync to CRM system
    {
      "function": "Custom Function",
      "custom_function": "sync_to_crm",
      "execution_mode": "async",
      "parameters": {
        "customer_data": "{{new}}",
        "operation": "{{action}}"
      },
      "output_variable": "crm_sync_id"
    },
    {
      "function": "Arrays",
      "operation": "push",
      "array": "{{sync_operations}}",
      "value": {
        "system": "CRM",
        "execution_id": "{{crm_sync_id}}",
        "status": "pending"
      },
      "output_variable": "sync_operations"
    },
    // Sync to email marketing platform
    {
      "function": "Custom Function",
      "custom_function": "sync_to_email_platform",
      "execution_mode": "async",
      "parameters": {
        "customer_data": "{{new}}",
        "operation": "{{action}}"
      },
      "output_variable": "email_sync_id"
    },
    {
      "function": "Arrays",
      "operation": "push",
      "array": "{{sync_operations}}",
      "value": {
        "system": "Email Platform",
        "execution_id": "{{email_sync_id}}",
        "status": "pending"
      },
      "output_variable": "sync_operations"
    },
    // Log sync operations
    {
      "function": "Add Record",
      "table": "sync_logs",
      "data": {
        "customer_id": "{{new.id}}",
        "sync_operations": "{{sync_operations}}",
        "triggered_at": "{{timestamp}}"
      }
    }
  ]
}
```

### Cascade Operations

```javascript
// Cascade delete with complex relationships
{
  "trigger_name": "user_cascade_delete",
  "table": "users",
  "events": ["delete"],
  "workflow": [
    // Delete related records in order of dependencies
    {
      "function": "Delete Record",
      "table": "user_sessions",
      "filter": {
        "user_id": "{{old.id}}"
      }
    },
    {
      "function": "Delete Record",
      "table": "user_preferences",
      "filter": {
        "user_id": "{{old.id}}"
      }
    },
    {
      "function": "Query All Records",
      "table": "orders",
      "filter": {
        "user_id": "{{old.id}}"
      },
      "output_variable": "user_orders"
    },
    {
      "function": "Loop",
      "input_array": "{{user_orders}}",
      "loop_item_variable": "order",
      "steps": [
        {
          "function": "Edit Record",
          "table": "orders",
          "record_id": "{{order.id}}",
          "data": {
            "user_id": null,
            "customer_email": "{{old.email}}",
            "customer_name": "{{old.first_name}} {{old.last_name}}",
            "anonymized": true
          }
        }
      ]
    },
    // Archive user data for compliance
    {
      "function": "Add Record",
      "table": "deleted_users_archive",
      "data": {
        "original_id": "{{old.id}}",
        "email": "{{old.email}}",
        "deleted_at": "{{timestamp}}",
        "deletion_reason": "user_request",
        "anonymized_data": {
          "registration_date": "{{old.created_at}}",
          "last_login": "{{old.last_login_at}}",
          "order_count": "{{user_orders.length}}"
        }
      }
    }
  ]
}
```

## 📊 **Performance Considerations**

### Trigger Optimization

```javascript
// Best practices for trigger performance
{
  "optimization_strategies": {
    "conditional_execution": {
      "description": "Use conditions to prevent unnecessary executions",
      "example": {
        "conditions": {
          "significant_change": "{{abs(new.price - old.price) > 10}}"
        }
      }
    },
    "async_operations": {
      "description": "Use async for non-critical operations",
      "example": "Send notifications asynchronously to avoid blocking"
    },
    "batch_operations": {
      "description": "Group related operations together",
      "implementation": "Use database transactions for related updates"
    },
    "selective_triggers": {
      "description": "Apply triggers only to relevant data sources",
      "configuration": "Specify data sources in trigger settings"
    }
  }
}
```

### Error Handling in Triggers

```javascript
// Robust error handling for triggers
{
  "trigger_name": "resilient_order_processing",
  "table": "orders",
  "events": ["insert"],
  "workflow": [
    {
      "function": "Try-Catch",
      "try_steps": [
        {
          "function": "Custom Function",
          "custom_function": "process_payment",
          "parameters": {
            "order_id": "{{new.id}}"
          }
        }
      ],
      "catch_steps": [
        {
          "function": "Edit Record",
          "table": "orders",
          "record_id": "{{new.id}}",
          "data": {
            "status": "payment_failed",
            "error_message": "{{error.message}}",
            "error_timestamp": "{{timestamp}}"
          }
        },
        {
          "function": "Add Record",
          "table": "error_logs",
          "data": {
            "context": "order_trigger",
            "order_id": "{{new.id}}",
            "error": "{{error}}",
            "timestamp": "{{timestamp}}"
          }
        }
      ]
    }
  ]
}
```

## 🎯 **Best Practices**

### Trigger Design Guidelines

```javascript
// Guidelines for effective trigger implementation
{
  "design_principles": {
    "single_responsibility": {
      "description": "Each trigger should handle one specific concern",
      "example": "Separate triggers for email notifications and data validation"
    },
    "idempotency": {
      "description": "Triggers should handle duplicate executions gracefully",
      "implementation": "Check for existing records before creating"
    },
    "minimal_processing": {
      "description": "Keep trigger logic lightweight",
      "strategy": "Move complex operations to async custom functions"
    },
    "clear_conditions": {
      "description": "Use specific conditions to prevent false triggers",
      "example": "Check for actual value changes, not just updates"
    },
    "error_resilience": {
      "description": "Always handle potential failures",
      "implementation": "Use try-catch blocks for external operations"
    }
  }
}
```

### Testing and Debugging

```javascript
// Trigger testing approach
{
  "testing_strategy": {
    "unit_testing": {
      "method": "Test trigger logic in isolation",
      "tools": "Use Xano's built-in testing interface"
    },
    "integration_testing": {
      "method": "Test full trigger workflows with real data",
      "approach": "Create test records and monitor trigger execution"
    },
    "monitoring": {
      "implementation": "Add logging to track trigger performance",
      "metrics": ["Execution time", "Success rate", "Error frequency"]
    },
    "debugging": {
      "techniques": [
        "Use variable inspection to trace data flow",
        "Add conditional logging for specific scenarios",
        "Monitor external API response times"
      ]
    }
  }
}
```

## ⚠️ **Common Pitfalls**

### Avoiding Trigger Anti-patterns

```javascript
// Common mistakes and solutions
{
  "anti_patterns": {
    "infinite_loops": {
      "mistake": "Trigger modifies same table causing loop",
      "solution": "Use conditions to prevent self-triggering"
    },
    "heavy_synchronous_operations": {
      "mistake": "Blocking operations in trigger workflow",
      "solution": "Use async functions for time-consuming tasks"
    },
    "missing_error_handling": {
      "mistake": "No error handling for external dependencies",
      "solution": "Always wrap external calls in try-catch blocks"
    },
    "overly_broad_conditions": {
      "mistake": "Triggers firing for irrelevant changes",
      "solution": "Use specific field-level conditions"
    }
  }
}
```

---

*Database triggers provide the foundation for building reactive, event-driven applications that automatically respond to data changes with sophisticated business logic and integrations.*