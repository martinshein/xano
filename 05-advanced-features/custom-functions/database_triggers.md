---
title: Database Triggers - Event-Driven Automation
description: Complete guide to database triggers in Xano including automatic workflows on data changes, realtime events, workspace operations, and MCP server connections with no-code platform integration
category: custom-functions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - custom-functions.md
  - background-tasks.md
  - building-with-visual-development.md
subcategory: 05-advanced-features/custom-functions
tags:
  - database-triggers
  - event-driven
  - automation
  - data-hooks
  - realtime
  - no-code
---

## 📋 **Quick Summary**

Database triggers are event-driven workflows that automatically execute when specific database operations occur. They enable real-time automation for data validation, audit logging, notifications, and business logic enforcement without manual intervention. Perfect for maintaining data integrity and automating responses in n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- How to create and configure database triggers effectively
- Event types and trigger patterns for different use cases
- Advanced automation workflows and business logic
- Integration with external systems and notifications
- Performance optimization and trigger management
- Best practices for event-driven architecture

# Database Triggers

## Overview

**Database Triggers** are automated workflows that execute in response to specific database events such as record creation, updates, or deletions. Unlike API endpoints or background tasks, triggers run automatically whenever their triggering conditions are met, making them ideal for enforcing business rules, maintaining data consistency, and enabling real-time automation.

### Trigger Types Available

**Database Triggers:**
- INSERT: New records added
- UPDATE: Existing records modified
- DELETE: Records removed
- TRUNCATE: All table data cleared

**Realtime Triggers:**
- MESSAGE: Channel messages received
- JOIN: New channel connections

**Workspace Triggers:**
- BRANCH_NEW: New branch created
- BRANCH_MERGE: Branch merged
- BRANCH_LIVE: Branch set to live

**MCP Server Triggers:**
- CLIENT_CONNECT: MCP client connection

## 🚀 **Database Trigger Configuration**

### Basic INSERT Trigger

**User Registration Automation:**

```javascript
// Database trigger for user table INSERT events
{
  "trigger_name": "user_registration_automation",
  "table": "users",
  "events": ["insert"],
  "conditions": {
    "new.status": "active",
    "new.email_verified": false
  },
  "function_stack": [
    {
      "function": "create_variable",
      "name": "new_user",
      "value": "{{ trigger.new }}"
    },
    {
      "function": "custom_function",
      "name": "send_welcome_email",
      "inputs": {
        "user_id": "{{ new_user.id }}",
        "email": "{{ new_user.email }}",
        "name": "{{ new_user.first_name }}"
      },
      "execution_mode": "async"
    },
    {
      "function": "add_record",
      "table": "user_onboarding_tasks",
      "data": {
        "user_id": "{{ new_user.id }}",
        "task_type": "welcome_sequence",
        "status": "pending",
        "created_at": "{{ now }}"
      }
    },
    {
      "function": "external_api_request",
      "url": "{{ env.ANALYTICS_WEBHOOK_URL }}",
      "method": "POST",
      "body": {
        "event": "user_registered",
        "user_id": "{{ new_user.id }}",
        "timestamp": "{{ now }}",
        "properties": {
          "email_domain": "{{ new_user.email|split('@')|last }}",
          "registration_source": "{{ new_user.source || 'direct' }}"
        }
      }
    }
  ]
}
```

### UPDATE Trigger with Conditional Logic

**Order Status Change Automation:**

```javascript
// Database trigger for order table UPDATE events
{
  "trigger_name": "order_status_automation",
  "table": "orders",
  "events": ["update"],
  "conditions": {
    "old.status": {"$ne": "{{ new.status }}"},
    "new.status": {"$in": ["confirmed", "shipped", "delivered", "cancelled"]}
  },
  "function_stack": [
    {
      "function": "create_variable",
      "name": "status_change",
      "value": {
        "order_id": "{{ trigger.new.id }}",
        "old_status": "{{ trigger.old.status }}",
        "new_status": "{{ trigger.new.status }}",
        "customer_id": "{{ trigger.new.customer_id }}",
        "changed_at": "{{ now }}"
      }
    },
    {
      "function": "add_record",
      "table": "order_status_history",
      "data": "{{ status_change }}"
    },
    {
      "function": "conditional",
      "condition": "{{ status_change.new_status == 'confirmed' }}",
      "true_branch": [
        {
          "function": "custom_function",
          "name": "process_payment",
          "inputs": {
            "order_id": "{{ status_change.order_id }}",
            "amount": "{{ trigger.new.total_amount }}"
          },
          "execution_mode": "async"
        },
        {
          "function": "custom_function",
          "name": "update_inventory",
          "inputs": {
            "order_items": "{{ trigger.new.items }}"
          }
        }
      ]
    },
    {
      "function": "conditional",
      "condition": "{{ status_change.new_status == 'shipped' }}",
      "true_branch": [
        {
          "function": "custom_function",
          "name": "send_shipping_notification",
          "inputs": {
            "order_id": "{{ status_change.order_id }}",
            "tracking_number": "{{ trigger.new.tracking_number }}",
            "customer_email": "{{ trigger.new.customer.email }}"
          },
          "execution_mode": "async"
        }
      ]
    },
    {
      "function": "conditional",
      "condition": "{{ status_change.new_status == 'cancelled' }}",
      "true_branch": [
        {
          "function": "custom_function",
          "name": "process_refund",
          "inputs": {
            "order_id": "{{ status_change.order_id }}",
            "refund_amount": "{{ trigger.new.total_amount }}",
            "reason": "{{ trigger.new.cancellation_reason }}"
          },
          "execution_mode": "async"
        },
        {
          "function": "custom_function",
          "name": "restore_inventory",
          "inputs": {
            "order_items": "{{ trigger.new.items }}"
          }
        }
      ]
    }
  ]
}
```

## 🔗 **No-Code Platform Integration**

### n8n Trigger-Based Workflows

**External System Synchronization:**

```javascript
// n8n workflow triggered by Xano database changes
{
  "nodes": [
    {
      "name": "Xano Webhook Trigger",
      "type": "Webhook",
      "parameters": {
        "path": "xano-trigger-sync",
        "httpMethod": "POST",
        "authentication": "headerAuth",
        "options": {}
      }
    },
    {
      "name": "Process Trigger Data",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const triggerData = $input.first().json;
          
          // Extract trigger information
          const action = triggerData.action; // insert, update, delete
          const tableName = triggerData.table;
          const newRecord = triggerData.new;
          const oldRecord = triggerData.old;
          
          // Determine sync operation
          let operation = 'unknown';
          let recordData = null;
          
          if (action === 'insert') {
            operation = 'create';
            recordData = newRecord;
          } else if (action === 'update') {
            operation = 'update';
            recordData = newRecord;
          } else if (action === 'delete') {
            operation = 'delete';
            recordData = oldRecord;
          }
          
          return [{
            json: {
              operation: operation,
              table: tableName,
              record: recordData,
              timestamp: new Date().toISOString()
            }
          }];
        `
      }
    },
    {
      "name": "Route by Table",
      "type": "Switch",
      "parameters": {
        "values": [
          {
            "conditions": [
              {
                "value1": "{{ $json.table }}",
                "operation": "equal",
                "value2": "users"
              }
            ],
            "output": 0
          },
          {
            "conditions": [
              {
                "value1": "{{ $json.table }}",
                "operation": "equal",
                "value2": "orders"
              }
            ],
            "output": 1
          }
        ]
      }
    },
    {
      "name": "Sync to CRM",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.CRM_API_URL }}/sync/users",
        "method": "{{ $json.operation === 'delete' ? 'DELETE' : 'POST' }}",
        "headers": {
          "Authorization": "Bearer {{ $env.CRM_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "operation": "{{ $json.operation }}",
          "data": "{{ $json.record }}",
          "source": "xano",
          "sync_timestamp": "{{ $json.timestamp }}"
        }
      }
    },
    {
      "name": "Sync to Analytics",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.ANALYTICS_API_URL }}/events",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.ANALYTICS_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "event_type": "order_{{ $json.operation }}",
          "properties": "{{ $json.record }}",
          "timestamp": "{{ $json.timestamp }}"
        }
      }
    }
  ]
}
```

### WeWeb Real-Time Updates

**Live Dashboard with Trigger Updates:**

```javascript
// WeWeb component for real-time trigger-based updates
class XanoTriggerManager {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.eventSource = null;
    this.triggerHandlers = new Map();
  }
  
  async setupTriggerWebhook(triggerType, handlerFunction) {
    try {
      const response = await fetch(`${this.baseUrl}/api/triggers/webhook-setup`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          trigger_type: triggerType,
          webhook_url: `${window.location.origin}/api/trigger-handler`,
          active: true
        })
      });
      
      const result = await response.json();
      
      if (response.ok) {
        this.triggerHandlers.set(triggerType, handlerFunction);
        wwLib.wwUtils.showSuccessToast(`Trigger webhook setup for ${triggerType}`);
      }
      
      return result;
    } catch (error) {
      console.error('Trigger webhook setup failed:', error);
      return { error: 'Setup failed' };
    }
  }
  
  handleTriggerEvent(triggerData) {
    const { trigger_type, action, table, new_record, old_record } = triggerData;
    
    // Update UI variables based on trigger type
    if (trigger_type === 'database') {
      this.handleDatabaseTrigger(action, table, new_record, old_record);
    } else if (trigger_type === 'realtime') {
      this.handleRealtimeTrigger(triggerData);
    }
    
    // Call custom handler if registered
    const handler = this.triggerHandlers.get(trigger_type);
    if (handler) {
      handler(triggerData);
    }
  }
  
  handleDatabaseTrigger(action, table, newRecord, oldRecord) {
    const currentData = wwLib.wwVariable.getValue(`${table}_data`) || [];
    
    switch (action) {
      case 'insert':
        // Add new record to list
        const updatedData = [...currentData, newRecord];
        wwLib.wwVariable.updateValue(`${table}_data`, updatedData);
        wwLib.wwVariable.updateValue(`${table}_last_update`, new Date().toISOString());
        
        // Show notification
        wwLib.wwUtils.showSuccessToast(`New ${table.slice(0, -1)} added`);
        break;
        
      case 'update':
        // Update existing record in list
        const updatedList = currentData.map(item => 
          item.id === newRecord.id ? newRecord : item
        );
        wwLib.wwVariable.updateValue(`${table}_data`, updatedList);
        wwLib.wwVariable.updateValue(`${table}_last_update`, new Date().toISOString());
        
        // Highlight updated record
        wwLib.wwVariable.updateValue('highlighted_record_id', newRecord.id);
        setTimeout(() => {
          wwLib.wwVariable.updateValue('highlighted_record_id', null);
        }, 3000);
        break;
        
      case 'delete':
        // Remove record from list
        const filteredData = currentData.filter(item => item.id !== oldRecord.id);
        wwLib.wwVariable.updateValue(`${table}_data`, filteredData);
        wwLib.wwVariable.updateValue(`${table}_last_update`, new Date().toISOString());
        
        wwLib.wwUtils.showInfoToast(`${table.slice(0, -1)} removed`);
        break;
    }
    
    // Update statistics
    this.updateDashboardStats(table, action);
  }
  
  updateDashboardStats(table, action) {
    const currentStats = wwLib.wwVariable.getValue('dashboard_stats') || {};
    const today = new Date().toISOString().split('T')[0];
    
    if (!currentStats[today]) {
      currentStats[today] = {};
    }
    
    if (!currentStats[today][table]) {
      currentStats[today][table] = { inserts: 0, updates: 0, deletes: 0 };
    }
    
    currentStats[today][table][`${action}s`] = (currentStats[today][table][`${action}s`] || 0) + 1;
    
    wwLib.wwVariable.updateValue('dashboard_stats', currentStats);
  }
  
  async createDynamicTrigger(table, events, conditions, functionStack) {
    try {
      const response = await fetch(`${this.baseUrl}/api/triggers/create`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          table: table,
          events: events,
          conditions: conditions,
          function_stack: functionStack,
          active: true
        })
      });
      
      const result = await response.json();
      
      if (response.ok) {
        wwLib.wwUtils.showSuccessToast('Trigger created successfully');
        this.refreshTriggerList();
      } else {
        wwLib.wwUtils.showErrorToast(`Failed to create trigger: ${result.message}`);
      }
      
      return result;
    } catch (error) {
      console.error('Trigger creation failed:', error);
      wwLib.wwUtils.showErrorToast('Network error occurred');
      return { error: 'Creation failed' };
    }
  }
  
  async refreshTriggerList() {
    try {
      const response = await fetch(`${this.baseUrl}/api/triggers/list`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`
        }
      });
      
      const triggers = await response.json();
      wwLib.wwVariable.updateValue('active_triggers', triggers);
      
      return triggers;
    } catch (error) {
      console.error('Failed to refresh trigger list:', error);
      return [];
    }
  }
}

// Initialize trigger manager
const triggerManager = new XanoTriggerManager(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function setupUsersTrigger() {
  await triggerManager.setupTriggerWebhook('database.users', (triggerData) => {
    console.log('Users table triggered:', triggerData);
  });
}

async function createOrderStatusTrigger() {
  const conditions = {
    'old.status': { '$ne': '{{ new.status }}' }
  };
  
  const functionStack = [
    {
      function: 'external_api_request',
      url: 'https://webhook.site/your-endpoint',
      method: 'POST',
      body: {
        order_id: '{{ trigger.new.id }}',
        old_status: '{{ trigger.old.status }}',
        new_status: '{{ trigger.new.status }}'
      }
    }
  ];
  
  await triggerManager.createDynamicTrigger('orders', ['update'], conditions, functionStack);
}
```

## 🛠️ **Advanced Trigger Patterns**

### Data Validation and Enforcement

**Business Rule Enforcement Trigger:**

```javascript
// Database trigger for data validation and business rules
[
  {
    "function": "create_variable",
    "name": "validation_errors",
    "value": []
  },
  {
    "function": "conditional",
    "condition": "{{ trigger.action == 'insert' || trigger.action == 'update' }}",
    "true_branch": [
      {
        "function": "conditional",
        "condition": "{{ trigger.new.email && trigger.action == 'insert' }}",
        "true_branch": [
          {
            "function": "query_single_record",
            "table": "users",
            "filter": {
              "email": "{{ trigger.new.email }}",
              "id": {"$ne": "{{ trigger.new.id }}"}
            },
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
                "value": "Email address already exists"
              }
            ]
          }
        ]
      },
      {
        "function": "conditional",
        "condition": "{{ trigger.new.age && trigger.new.age < 18 }}",
        "true_branch": [
          {
            "function": "update_variable",
            "name": "validation_errors",
            "operation": "append",
            "value": "User must be at least 18 years old"
          }
        ]
      },
      {
        "function": "conditional",
        "condition": "{{ trigger.new.subscription_tier && trigger.action == 'update' }}",
        "true_branch": [
          {
            "function": "conditional",
            "condition": "{{ trigger.old.subscription_tier == 'premium' && trigger.new.subscription_tier == 'basic' }}",
            "true_branch": [
              {
                "function": "query_all_records",
                "table": "user_features",
                "filter": {
                  "user_id": "{{ trigger.new.id }}",
                  "feature_type": "premium_only"
                },
                "return_as": "premium_features"
              },
              {
                "function": "conditional",
                "condition": "{{ premium_features|length > 0 }}",
                "true_branch": [
                  {
                    "function": "update_variable",
                    "name": "validation_errors",
                    "operation": "append",
                    "value": "Cannot downgrade while using premium features"
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ validation_errors|length > 0 }}",
    "true_branch": [
      {
        "function": "add_record",
        "table": "validation_logs",
        "data": {
          "table_name": "{{ trigger.table }}",
          "record_id": "{{ trigger.new.id || trigger.old.id }}",
          "action": "{{ trigger.action }}",
          "errors": "{{ validation_errors }}",
          "timestamp": "{{ now }}"
        }
      },
      {
        "function": "external_api_request",
        "url": "{{ env.VALIDATION_ERROR_WEBHOOK }}",
        "method": "POST",
        "body": {
          "table": "{{ trigger.table }}",
          "errors": "{{ validation_errors }}",
          "record_data": "{{ trigger.new || trigger.old }}"
        }
      }
    ]
  }
]
```

### Audit Trail and Change Tracking

**Comprehensive Audit Logging:**

```javascript
// Universal audit trail trigger
[
  {
    "function": "create_variable",
    "name": "audit_entry",
    "value": {
      "table_name": "{{ trigger.table }}",
      "record_id": "{{ trigger.new.id || trigger.old.id }}",
      "action": "{{ trigger.action }}",
      "user_id": "{{ auth.user.id || 'system' }}",
      "timestamp": "{{ now }}",
      "ip_address": "{{ request.ip || 'trigger' }}",
      "data_source": "{{ trigger.data_source }}"
    }
  },
  {
    "function": "conditional",
    "condition": "{{ trigger.action == 'update' }}",
    "true_branch": [
      {
        "function": "create_variable",
        "name": "field_changes",
        "value": []
      },
      {
        "function": "loop",
        "array": "{{ trigger.new|keys }}",
        "operations": [
          {
            "function": "conditional",
            "condition": "{{ trigger.old[item] != trigger.new[item] }}",
            "true_branch": [
              {
                "function": "update_variable",
                "name": "field_changes",
                "operation": "append",
                "value": {
                  "field": "{{ item }}",
                  "old_value": "{{ trigger.old[item] }}",
                  "new_value": "{{ trigger.new[item] }}"
                }
              }
            ]
          }
        ]
      },
      {
        "function": "update_variable",
        "name": "audit_entry",
        "operation": "merge",
        "value": {
          "changes": "{{ field_changes }}",
          "change_count": "{{ field_changes|length }}"
        }
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ trigger.action == 'insert' }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "audit_entry",
        "operation": "merge",
        "value": {
          "new_data": "{{ trigger.new }}"
        }
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ trigger.action == 'delete' }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "audit_entry",
        "operation": "merge",
        "value": {
          "deleted_data": "{{ trigger.old }}"
        }
      }
    ]
  },
  {
    "function": "add_record",
    "table": "audit_trail",
    "data": "{{ audit_entry }}"
  },
  {
    "function": "conditional",
    "condition": "{{ trigger.table|in(['users', 'orders', 'payments']) }}",
    "true_branch": [
      {
        "function": "external_api_request",
        "url": "{{ env.COMPLIANCE_WEBHOOK_URL }}",
        "method": "POST",
        "body": {
          "audit_type": "sensitive_data_change",
          "table": "{{ trigger.table }}",
          "action": "{{ trigger.action }}",
          "user_id": "{{ audit_entry.user_id }}",
          "timestamp": "{{ audit_entry.timestamp }}"
        }
      }
    ]
  }
]
```

### Cache Invalidation and Synchronization

**Smart Cache Management:**

```javascript
// Cache invalidation trigger
[
  {
    "function": "create_variable",
    "name": "cache_keys_to_invalidate",
    "value": []
  },
  {
    "function": "conditional",
    "condition": "{{ trigger.table == 'users' }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "cache_keys_to_invalidate",
        "operation": "append",
        "value": "user_{{ trigger.new.id || trigger.old.id }}"
      },
      {
        "function": "update_variable",
        "name": "cache_keys_to_invalidate",
        "operation": "append",
        "value": "user_list_*"
      },
      {
        "function": "conditional",
        "condition": "{{ trigger.action == 'update' && trigger.old.status != trigger.new.status }}",
        "true_branch": [
          {
            "function": "update_variable",
            "name": "cache_keys_to_invalidate",
            "operation": "append",
            "value": "active_users_count"
          }
        ]
      }
    ]
  },
  {
    "function": "conditional",
    "condition": "{{ trigger.table == 'products' }}",
    "true_branch": [
      {
        "function": "update_variable",
        "name": "cache_keys_to_invalidate",
        "operation": "append",
        "value": "product_{{ trigger.new.id || trigger.old.id }}"
      },
      {
        "function": "update_variable",
        "name": "cache_keys_to_invalidate",
        "operation": "append",
        "value": "products_category_{{ trigger.new.category || trigger.old.category }}"
      },
      {
        "function": "conditional",
        "condition": "{{ trigger.action == 'update' && trigger.old.price != trigger.new.price }}",
        "true_branch": [
          {
            "function": "update_variable",
            "name": "cache_keys_to_invalidate",
            "operation": "append",
            "value": "price_index_*"
          }
        ]
      }
    ]
  },
  {
    "function": "loop",
    "array": "{{ cache_keys_to_invalidate }}",
    "operations": [
      {
        "function": "redis_delete",
        "key": "{{ item }}"
      }
    ]
  },
  {
    "function": "external_api_request",
    "url": "{{ env.CDN_PURGE_URL }}",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.CDN_API_KEY }}"
    },
    "body": {
      "tags": "{{ cache_keys_to_invalidate }}"
    }
  }
]
```

## 💡 **Pro Tips**

- **Keep Triggers Lightweight**: Use async custom functions for heavy operations to avoid blocking database operations
- **Implement Idempotency**: Ensure triggers can handle duplicate events gracefully
- **Monitor Performance**: Track trigger execution times and optimize slow operations
- **Use Conditional Logic**: Apply filters to prevent unnecessary trigger executions
- **Handle Failures Gracefully**: Implement error handling to prevent trigger failures from affecting the main operation
- **Document Dependencies**: Keep track of which triggers depend on specific data structures

## 🔧 **Troubleshooting**

### Common Database Trigger Issues

**Problem**: Trigger causing infinite loops  
**Solution**: Add conditions to prevent triggers from firing on their own updates and use proper filtering

**Problem**: Trigger execution too slow, blocking database operations  
**Solution**: Move heavy operations to async custom functions or background tasks

**Problem**: Trigger failing silently  
**Solution**: Add comprehensive error logging and monitoring to track trigger execution status

**Problem**: Trigger not firing for expected events  
**Solution**: Check trigger conditions, table permissions, and data source configuration

---

**Next Steps**: Ready to implement event-driven automation? Check out [Custom Functions](custom-functions.md) for reusable logic or explore [Background Tasks](background-tasks.md) for scheduled operations