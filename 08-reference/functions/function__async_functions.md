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
- Async
- Background Tasks
- Performance
- Concurrency
title: 'Async Functions & Concurrent Execution'
---

# Async Functions & Concurrent Execution

## 📋 **Quick Summary**
Async functions in Xano enable non-blocking execution of custom functions, allowing your main workflow to continue while background operations run concurrently. Perfect for time-consuming operations like external API calls, file processing, and bulk operations that shouldn't block user interactions.

## 🎯 **Core Concepts**

### Asynchronous Execution Model
Async functions execute in parallel with your main function stack, returning immediately with an execution ID while the actual work happens in the background.

### Key Benefits
- **Non-blocking Operations**: Main workflow continues without waiting
- **Improved Performance**: Parallel execution of independent tasks
- **Better User Experience**: Responsive interfaces during heavy operations
- **Resource Optimization**: Efficient handling of I/O-bound tasks

## 🚀 **When to Use Async Functions**

### High-Impact Use Cases

```javascript
// Scenarios Perfect for Async Functions
{
  "external_api_calls": {
    "description": "Third-party API requests that may be slow",
    "examples": ["Payment processing", "Email delivery", "Social media posting"],
    "benefit": "Avoid timeout issues and maintain responsiveness"
  },
  "file_processing": {
    "description": "Image resizing, document conversion, data imports",
    "examples": ["PDF generation", "Image optimization", "CSV processing"],
    "benefit": "Handle large files without blocking user interface"
  },
  "bulk_operations": {
    "description": "Mass data operations and batch processing",
    "examples": ["Email campaigns", "Data migrations", "Report generation"],
    "benefit": "Process thousands of records efficiently"
  },
  "notification_systems": {
    "description": "Communications that don't require immediate response",
    "examples": ["Push notifications", "SMS alerts", "Webhook calls"],
    "benefit": "Instant user feedback while messages send in background"
  }
}
```

## 🛠️ **Implementation Guide**

### Basic Async Function Setup

```javascript
// Step 1: Create Custom Function for Background Task
{
  "function_name": "send_welcome_email",
  "parameters": {
    "user_email": "string",
    "user_name": "string",
    "template_id": "string"
  },
  "steps": [
    {
      "function": "External API Request",
      "url": "https://api.sendgrid.com/v3/mail/send",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{env.SENDGRID_API_KEY}}",
        "Content-Type": "application/json"
      },
      "body": {
        "personalizations": [{
          "to": [{"email": "{{user_email}}"}],
          "dynamic_template_data": {
            "user_name": "{{user_name}}"
          }
        }],
        "template_id": "{{template_id}}"
      }
    },
    {
      "function": "Add Record",
      "table": "email_logs",
      "data": {
        "user_email": "{{user_email}}",
        "template_id": "{{template_id}}",
        "sent_at": "{{timestamp}}",
        "status": "sent"
      }
    }
  ]
}

// Step 2: Call Function Asynchronously in Main Stack
{
  "main_workflow": "user_registration",
  "steps": [
    {
      "function": "Add Record",
      "table": "users",
      "data": {
        "email": "{{inputs.email}}",
        "name": "{{inputs.name}}"
      },
      "output_variable": "new_user"
    },
    {
      "function": "Custom Function",
      "custom_function": "send_welcome_email",
      "execution_mode": "async",
      "parameters": {
        "user_email": "{{new_user.email}}",
        "user_name": "{{new_user.name}}",
        "template_id": "welcome_template"
      },
      "output_variable": "email_execution_id"
    },
    {
      "function": "Response",
      "status_code": 201,
      "body": {
        "user": "{{new_user}}",
        "message": "User registered successfully",
        "email_status": "sending"
      }
    }
  ]
}
```

### Retrieving Async Function Results

```javascript
// Using Async Function Await to get results
{
  "function_stack": [
    {
      "function": "Async Function Await",
      "execution_ids": ["{{email_execution_id}}"],
      "timeout": 30,
      "output_variable": "email_results"
    },
    {
      "function": "Conditional",
      "condition": "{{email_results[0].status === 'completed'}}",
      "true_steps": [
        {
          "function": "Response",
          "body": {
            "status": "success",
            "email_sent": true,
            "result": "{{email_results[0].output}}"
          }
        }
      ],
      "false_steps": [
        {
          "function": "Response",
          "body": {
            "status": "pending",
            "email_sent": false,
            "execution_id": "{{email_execution_id}}"
          }
        }
      ]
    }
  ]
}
```

## 🔗 **Integration Examples**

### n8n Async Processing Workflow

```javascript
// n8n workflow with async Xano operations
{
  "workflow_name": "Order Processing with Async Operations",
  "nodes": [
    {
      "name": "Order Webhook",
      "type": "Webhook",
      "parameters": {
        "httpMethod": "POST",
        "path": "new-order"
      }
    },
    {
      "name": "Create Order (Xano)",
      "type": "HTTP Request",
      "parameters": {
        "method": "POST",
        "url": "https://your-xano.xano.io/api:v1/orders",
        "body": {
          "customer_id": "={{$json.customer_id}}",
          "items": "={{$json.items}}",
          "total": "={{$json.total}}"
        }
      }
    },
    {
      "name": "Start Async Operations",
      "type": "HTTP Request",
      "parameters": {
        "method": "POST",
        "url": "https://your-xano.xano.io/api:v1/process-order-async",
        "body": {
          "order_id": "={{$json.order.id}}"
        }
      }
    },
    {
      "name": "Immediate Response",
      "type": "HTTP Request",
      "parameters": {
        "method": "POST",
        "url": "={{$node['Order Webhook'].json.response_url}}",
        "body": {
          "status": "order_received",
          "order_id": "={{$json.order.id}}",
          "processing": true
        }
      }
    }
  ]
}

// Corresponding Xano Async Function Stack
{
  "endpoint": "/process-order-async",
  "method": "POST",
  "functions": [
    {
      "function": "Get Record",
      "table": "orders",
      "record_id": "{{inputs.order_id}}",
      "output_variable": "order"
    },
    {
      "function": "Custom Function",
      "custom_function": "update_inventory",
      "execution_mode": "async",
      "parameters": {
        "order_items": "{{order.items}}"
      },
      "output_variable": "inventory_task_id"
    },
    {
      "function": "Custom Function",
      "custom_function": "send_order_confirmation",
      "execution_mode": "async",
      "parameters": {
        "customer_email": "{{order.customer.email}}",
        "order_details": "{{order}}"
      },
      "output_variable": "email_task_id"
    },
    {
      "function": "Custom Function",
      "custom_function": "process_payment",
      "execution_mode": "async",
      "parameters": {
        "order_id": "{{order.id}}",
        "amount": "{{order.total}}"
      },
      "output_variable": "payment_task_id"
    },
    {
      "function": "Response",
      "body": {
        "status": "processing",
        "task_ids": {
          "inventory": "{{inventory_task_id}}",
          "email": "{{email_task_id}}",
          "payment": "{{payment_task_id}}"
        }
      }
    }
  ]
}
```

### WeWeb Real-time Status Updates

```javascript
// WeWeb component tracking async operations
{
  "component_name": "OrderStatus",
  "data_sources": {
    "order_status": {
      "type": "api_collection",
      "endpoint": "https://your-xano.xano.io/api:v1/order-status",
      "method": "GET",
      "headers": {
        "Authorization": "Bearer {{user.authToken}}"
      },
      "auto_refresh": true,
      "refresh_interval": 5000
    }
  },
  "computed_properties": {
    "all_tasks_complete": "{{order_status.inventory_complete && order_status.email_sent && order_status.payment_processed}}"
  }
}

// Xano Status Endpoint
{
  "endpoint": "/order-status",
  "method": "GET",
  "functions": [
    {
      "function": "Get Record",
      "table": "orders",
      "filter": {
        "customer_id": "{{auth_user.id}}"
      },
      "sort": [{"created_at": "desc"}],
      "limit": 1,
      "output_variable": "latest_order"
    },
    {
      "function": "Async Function Await",
      "execution_ids": [
        "{{latest_order.inventory_task_id}}",
        "{{latest_order.email_task_id}}",
        "{{latest_order.payment_task_id}}"
      ],
      "timeout": 1,
      "output_variable": "task_results"
    },
    {
      "function": "Response",
      "body": {
        "order_id": "{{latest_order.id}}",
        "inventory_complete": "{{task_results[0].status === 'completed'}}",
        "email_sent": "{{task_results[1].status === 'completed'}}",
        "payment_processed": "{{task_results[2].status === 'completed'}}",
        "overall_status": "{{task_results | all_complete ? 'ready' : 'processing'}}"
      }
    }
  ]
}
```

## 🚀 **Advanced Async Patterns**

### Parallel Processing with Result Aggregation

```javascript
// Processing multiple operations and waiting for all to complete
{
  "function_name": "bulk_user_import",
  "steps": [
    {
      "function": "Create Variable",
      "variable_name": "batch_size",
      "value": 100
    },
    {
      "function": "Math",
      "operation": "ceiling",
      "value1": "{{inputs.users.length}}",
      "value2": "{{batch_size}}",
      "output_variable": "batch_count"
    },
    {
      "function": "Create Variable",
      "variable_name": "async_task_ids",
      "value": []
    },
    {
      "function": "Loop",
      "input_array": "{{range(batch_count)}}",
      "loop_item_variable": "batch_index",
      "steps": [
        {
          "function": "Arrays",
          "operation": "slice",
          "array": "{{inputs.users}}",
          "start": "{{batch_index * batch_size}}",
          "end": "{{(batch_index + 1) * batch_size}}",
          "output_variable": "batch_users"
        },
        {
          "function": "Custom Function",
          "custom_function": "process_user_batch",
          "execution_mode": "async",
          "parameters": {
            "users": "{{batch_users}}",
            "batch_number": "{{batch_index + 1}}"
          },
          "output_variable": "batch_task_id"
        },
        {
          "function": "Arrays",
          "operation": "push",
          "array": "{{async_task_ids}}",
          "value": "{{batch_task_id}}",
          "output_variable": "async_task_ids"
        }
      ]
    },
    {
      "function": "Async Function Await",
      "execution_ids": "{{async_task_ids}}",
      "timeout": 300,
      "output_variable": "batch_results"
    },
    {
      "function": "Arrays",
      "operation": "reduce",
      "array": "{{batch_results}}",
      "initial_value": 0,
      "reducer": "{{acc + current.output.processed_count}}",
      "output_variable": "total_processed"
    },
    {
      "function": "Response",
      "body": {
        "status": "completed",
        "batches_processed": "{{batch_count}}",
        "total_users_processed": "{{total_processed}}",
        "execution_time": "{{processing_duration}}"
      }
    }
  ]
}
```

### Error Handling in Async Operations

```javascript
// Robust error handling for async functions
{
  "function_name": "resilient_data_sync",
  "steps": [
    {
      "function": "Custom Function",
      "custom_function": "sync_external_data",
      "execution_mode": "async",
      "parameters": {
        "data_source": "{{inputs.source}}",
        "sync_type": "{{inputs.type}}"
      },
      "output_variable": "sync_task_id"
    },
    {
      "function": "Create Variable",
      "variable_name": "retry_count",
      "value": 0
    },
    {
      "function": "Create Variable",
      "variable_name": "max_retries",
      "value": 3
    },
    {
      "function": "Loop",
      "condition": "{{retry_count < max_retries}}",
      "steps": [
        {
          "function": "Async Function Await",
          "execution_ids": ["{{sync_task_id}}"],
          "timeout": 60,
          "output_variable": "sync_result"
        },
        {
          "function": "Conditional",
          "condition": "{{sync_result[0].status === 'completed'}}",
          "true_steps": [
            {
              "function": "Response",
              "body": {
                "status": "success",
                "data": "{{sync_result[0].output}}",
                "attempts": "{{retry_count + 1}}"
              }
            }
          ],
          "false_steps": [
            {
              "function": "Math",
              "operation": "add",
              "value1": "{{retry_count}}",
              "value2": 1,
              "output_variable": "retry_count"
            },
            {
              "function": "Conditional",
              "condition": "{{retry_count < max_retries}}",
              "true_steps": [
                {
                  "function": "Custom Function",
                  "custom_function": "sync_external_data",
                  "execution_mode": "async",
                  "parameters": {
                    "data_source": "{{inputs.source}}",
                    "sync_type": "{{inputs.type}}"
                  },
                  "output_variable": "sync_task_id"
                }
              ],
              "false_steps": [
                {
                  "function": "Response",
                  "status_code": 500,
                  "body": {
                    "status": "failed",
                    "error": "Max retries exceeded",
                    "attempts": "{{retry_count}}"
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

## 📊 **Performance Optimization**

### Concurrent API Calls

```javascript
// Making multiple API calls in parallel
{
  "function_name": "fetch_user_profile_data",
  "steps": [
    {
      "function": "Custom Function",
      "custom_function": "fetch_social_media_data",
      "execution_mode": "async",
      "parameters": {
        "user_id": "{{inputs.user_id}}"
      },
      "output_variable": "social_task_id"
    },
    {
      "function": "Custom Function",
      "custom_function": "fetch_analytics_data",
      "execution_mode": "async",
      "parameters": {
        "user_id": "{{inputs.user_id}}"
      },
      "output_variable": "analytics_task_id"
    },
    {
      "function": "Custom Function",
      "custom_function": "fetch_preferences_data",
      "execution_mode": "async",
      "parameters": {
        "user_id": "{{inputs.user_id}}"
      },
      "output_variable": "preferences_task_id"
    },
    {
      "function": "Async Function Await",
      "execution_ids": [
        "{{social_task_id}}",
        "{{analytics_task_id}}",
        "{{preferences_task_id}}"
      ],
      "timeout": 30,
      "output_variable": "all_data"
    },
    {
      "function": "Response",
      "body": {
        "user_id": "{{inputs.user_id}}",
        "social_data": "{{all_data[0].output}}",
        "analytics": "{{all_data[1].output}}",
        "preferences": "{{all_data[2].output}}",
        "fetch_time": "{{processing_duration}}"
      }
    }
  ]
}
```

### Background Task Scheduling

```javascript
// Scheduling recurring async tasks
{
  "function_name": "schedule_maintenance_tasks",
  "steps": [
    {
      "function": "Query All Records",
      "table": "scheduled_tasks",
      "filter": {
        "next_run": {"<=": "{{timestamp}}"},
        "active": true
      },
      "output_variable": "due_tasks"
    },
    {
      "function": "Loop",
      "input_array": "{{due_tasks}}",
      "loop_item_variable": "task",
      "steps": [
        {
          "function": "Custom Function",
          "custom_function": "{{task.function_name}}",
          "execution_mode": "async",
          "parameters": "{{task.parameters}}",
          "output_variable": "execution_id"
        },
        {
          "function": "Edit Record",
          "table": "scheduled_tasks",
          "record_id": "{{task.id}}",
          "data": {
            "last_execution_id": "{{execution_id}}",
            "last_run": "{{timestamp}}",
            "next_run": "{{timestamp + task.interval_seconds * 1000}}"
          }
        }
      ]
    }
  ]
}
```

## 🎯 **Best Practices**

### 1. Async Function Design

```javascript
// Design principles for async functions
{
  "design_principles": {
    "idempotency": {
      "description": "Functions should produce same result when run multiple times",
      "implementation": "Check for existing results before processing"
    },
    "timeout_handling": {
      "description": "Always set appropriate timeouts",
      "recommendation": "30-300 seconds based on operation complexity"
    },
    "error_logging": {
      "description": "Log errors for async debugging",
      "implementation": "Add error records to dedicated logging table"
    },
    "result_persistence": {
      "description": "Store results for later retrieval",
      "implementation": "Save outputs to database with execution ID"
    }
  }
}
```

### 2. Monitoring and Debugging

```javascript
// Async function monitoring system
{
  "monitoring_setup": {
    "execution_tracking": {
      "table": "async_executions",
      "fields": {
        "execution_id": "UUID of async function",
        "function_name": "Name of executed function",
        "status": "pending|running|completed|failed",
        "started_at": "Execution start time",
        "completed_at": "Execution end time",
        "duration": "Total execution time",
        "result": "Function output or error"
      }
    },
    "performance_metrics": {
      "average_duration": "Track typical execution times",
      "success_rate": "Monitor completion vs failure rates",
      "concurrent_executions": "Number of parallel operations"
    }
  }
}
```

### 3. Resource Management

```javascript
// Managing async function resources
{
  "resource_management": {
    "concurrency_limits": {
      "max_parallel": 10,
      "queue_size": 100,
      "priority_handling": "Critical operations first"
    },
    "memory_optimization": {
      "batch_size_limits": "Process data in chunks",
      "cleanup_completed": "Remove old execution records",
      "result_compression": "Compress large outputs"
    },
    "timeout_strategies": {
      "short_operations": "30 seconds",
      "medium_operations": "300 seconds",
      "long_operations": "3600 seconds",
      "cleanup_timeout": "Auto-cleanup after 24 hours"
    }
  }
}
```

## ⚠️ **Common Pitfalls and Solutions**

### Avoiding Async Anti-patterns

```javascript
// Common mistakes and solutions
{
  "anti_patterns": {
    "blocking_on_async": {
      "mistake": "Immediately awaiting async function defeating purpose",
      "solution": "Use async for fire-and-forget or delayed processing"
    },
    "no_error_handling": {
      "mistake": "Not handling async function failures",
      "solution": "Always check execution status before using results"
    },
    "memory_leaks": {
      "mistake": "Not cleaning up completed execution records",
      "solution": "Implement automatic cleanup of old executions"
    },
    "infinite_polling": {
      "mistake": "Continuously checking async status without limits",
      "solution": "Implement exponential backoff and max attempts"
    }
  }
}
```

---

*Async functions enable powerful concurrent processing patterns that can dramatically improve your application's performance and user experience when implemented correctly.*