---
title: Background Tasks - Scheduled Workflows and Cron Jobs
description: Complete guide to building and managing background tasks in Xano including scheduled workflows, automated data processing, report generation, and integration with no-code platforms
category: custom-functions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - async-functions.md
  - custom-functions.md
  - building-with-visual-development.md
subcategory: 05-advanced-features/custom-functions
tags:
  - background-tasks
  - cron-jobs
  - scheduled-workflows
  - automation
  - data-processing
  - no-code
---

## 📋 **Quick Summary**

Background tasks (cron jobs) are scheduled workflows that run automatically at specified intervals. Perfect for automated data processing, report generation, email campaigns, data synchronization, and maintenance tasks. Seamlessly integrate with n8n, WeWeb, and other no-code platforms for comprehensive automation workflows.

## What You'll Learn

- How to create and configure background tasks effectively
- Scheduling patterns and cron expression syntax
- Best practices for automated workflow design
- Performance optimization for large-scale processing
- Integration patterns with external systems
- Monitoring and error handling strategies

# Background Tasks

## Overview

**Background Tasks** are server-side workflows that execute automatically on a predetermined schedule. Unlike API endpoints that respond to external requests, background tasks run independently and are ideal for maintenance operations, data processing, and automated business processes that need to occur regularly without user intervention.

### Background Tasks vs Other Xano Features

**Background Tasks:**
- Scheduled execution (cron-style)
- No external triggers required
- No user inputs or HTTP responses
- Long-running operations supported
- Automated and self-contained

**API Endpoints:**
- Request-response pattern
- External triggers required
- User inputs and HTTP responses
- Real-time execution
- Interactive and responsive

**Custom Functions:**
- Called by other function stacks
- Internal reusable components
- Parameters and return values
- Synchronous or asynchronous
- Modular and composable

## 🚀 **Creating Background Tasks**

### Basic Task Configuration

**Essential Components:**

```javascript
// Background task configuration
{
  "name": "daily_user_analytics",
  "description": "Generate daily user analytics report and send to administrators",
  "tags": ["analytics", "reporting", "daily"],
  "schedule": "0 6 * * *", // Daily at 6 AM UTC
  "data_source": "primary_database",
  "request_history": {
    "enabled": true,
    "retention_days": 30
  },
  "timeout": 300, // 5 minutes
  "retry_policy": {
    "max_retries": 3,
    "retry_delay": 60
  }
}
```

### Cron Expression Syntax

**Schedule Pattern Reference:**

```javascript
// Cron expression format: "minute hour day_of_month month day_of_week"
{
  "common_schedules": {
    "every_minute": "* * * * *",
    "every_5_minutes": "*/5 * * * *",
    "every_hour": "0 * * * *",
    "daily_at_midnight": "0 0 * * *",
    "daily_at_6am": "0 6 * * *",
    "weekly_sunday_6am": "0 6 * * 0",
    "monthly_first_day": "0 0 1 * *",
    "every_weekday_9am": "0 9 * * 1-5",
    "twice_daily": "0 6,18 * * *"
  },
  "advanced_examples": {
    "business_hours_every_2_hours": "0 9-17/2 * * 1-5",
    "last_day_of_month": "0 0 L * *",
    "first_monday_of_month": "0 9 1-7 * 1",
    "quarterly_report": "0 0 1 1,4,7,10 *"
  }
}
```

## 🔗 **No-Code Platform Integration**

### n8n Workflow Coordination

**Triggering n8n Workflows from Xano Background Tasks:**

```javascript
// n8n webhook integration from background task
[
  {
    "function": "create_variable",
    "name": "processing_summary",
    "value": {
      "task_name": "daily_data_sync",
      "started_at": "{{ now }}",
      "records_processed": 0,
      "status": "running"
    }
  },
  {
    "function": "query_all_records",
    "table": "pending_sync_items",
    "filter": {
      "status": "pending",
      "created_at": {"$gte": "{{ now - 86400 }}"}
    },
    "return_as": "sync_items"
  },
  {
    "function": "external_api_request",
    "url": "{{ env.N8N_WEBHOOK_URL }}/xano-data-sync",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.N8N_API_KEY }}",
      "Content-Type": "application/json"
    },
    "body": {
      "source": "xano_background_task",
      "task_id": "daily_data_sync",
      "data": "{{ sync_items }}",
      "metadata": {
        "total_items": "{{ sync_items|length }}",
        "initiated_at": "{{ processing_summary.started_at }}"
      }
    },
    "return_as": "n8n_response"
  },
  {
    "function": "update_variable",
    "name": "processing_summary",
    "operation": "merge",
    "value": {
      "n8n_workflow_triggered": true,
      "n8n_execution_id": "{{ n8n_response.execution_id }}",
      "records_sent": "{{ sync_items|length }}"
    }
  },
  {
    "function": "add_record",
    "table": "task_execution_logs",
    "data": {
      "task_name": "daily_data_sync",
      "status": "completed",
      "summary": "{{ processing_summary }}",
      "executed_at": "{{ now }}"
    }
  }
]
```

### WeWeb Dashboard Integration

**Background Task Status Monitoring:**

```javascript
// WeWeb component for monitoring background tasks
class XanoBackgroundTaskMonitor {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.pollInterval = null;
  }
  
  async getTaskExecutionHistory(taskName, limit = 10) {
    try {
      const response = await fetch(`${this.baseUrl}/api/admin/task-history`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          task_name: taskName,
          limit: limit,
          sort: 'executed_at desc'
        })
      });
      
      const history = await response.json();
      
      wwLib.wwVariable.updateValue(`task_history_${taskName}`, history);
      return history;
    } catch (error) {
      console.error('Failed to fetch task history:', error);
      return [];
    }
  }
  
  async getActiveTaskStatus() {
    try {
      const response = await fetch(`${this.baseUrl}/api/admin/active-tasks`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`
        }
      });
      
      const activeTasks = await response.json();
      
      wwLib.wwVariable.updateValue('active_background_tasks', activeTasks);
      
      // Update individual task statuses
      activeTasks.forEach(task => {
        wwLib.wwVariable.updateValue(`task_status_${task.name}`, task.status);
        wwLib.wwVariable.updateValue(`task_next_run_${task.name}`, task.next_execution);
      });
      
      return activeTasks;
    } catch (error) {
      console.error('Failed to fetch active tasks:', error);
      return [];
    }
  }
  
  startTaskMonitoring(refreshInterval = 30000) {
    this.pollInterval = setInterval(async () => {
      await this.getActiveTaskStatus();
      
      // Get history for visible tasks
      const monitoredTasks = wwLib.wwVariable.getValue('monitored_task_names') || [];
      for (const taskName of monitoredTasks) {
        await this.getTaskExecutionHistory(taskName, 5);
      }
    }, refreshInterval);
  }
  
  stopTaskMonitoring() {
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
      this.pollInterval = null;
    }
  }
  
  async triggerManualExecution(taskName) {
    try {
      const response = await fetch(`${this.baseUrl}/api/admin/trigger-task`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          task_name: taskName,
          trigger_source: 'manual_dashboard'
        })
      });
      
      const result = await response.json();
      
      if (response.ok) {
        wwLib.wwUtils.showSuccessToast(`Task ${taskName} triggered successfully`);
        // Refresh task status
        setTimeout(() => this.getActiveTaskStatus(), 2000);
      } else {
        wwLib.wwUtils.showErrorToast(`Failed to trigger task: ${result.message}`);
      }
      
      return result;
    } catch (error) {
      console.error('Manual task trigger failed:', error);
      wwLib.wwUtils.showErrorToast('Network error occurred');
      return { error: 'Trigger failed' };
    }
  }
}

// Initialize task monitor
const taskMonitor = new XanoBackgroundTaskMonitor(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('admin_auth_token')
);

// Usage functions
async function initializeTaskDashboard() {
  await taskMonitor.getActiveTaskStatus();
  taskMonitor.startTaskMonitoring();
  
  // Set up monitored tasks
  wwLib.wwVariable.updateValue('monitored_task_names', [
    'daily_user_analytics',
    'weekly_report_generation',
    'data_cleanup',
    'backup_database'
  ]);
}

async function triggerTaskManually() {
  const taskName = wwLib.wwVariable.getValue('selected_task_name');
  if (taskName) {
    await taskMonitor.triggerManualExecution(taskName);
  }
}

function cleanupTaskMonitoring() {
  taskMonitor.stopTaskMonitoring();
}
```

## 🛠️ **Common Background Task Patterns**

### Data Processing and Analytics

**Daily User Analytics Report:**

```javascript
// Comprehensive analytics processing
[
  {
    "function": "create_variable",
    "name": "report_date",
    "value": "{{ now|date('Y-m-d') }}"
  },
  {
    "function": "create_variable",
    "name": "date_range",
    "value": {
      "start": "{{ now - 86400 }}",
      "end": "{{ now }}"
    }
  },
  {
    "function": "query_all_records",
    "table": "users",
    "filter": {
      "created_at": {
        "$gte": "{{ date_range.start }}",
        "$lt": "{{ date_range.end }}"
      }
    },
    "return_as": "new_users"
  },
  {
    "function": "query_all_records",
    "table": "user_sessions",
    "filter": {
      "created_at": {
        "$gte": "{{ date_range.start }}",
        "$lt": "{{ date_range.end }}"
      }
    },
    "return_as": "daily_sessions"
  },
  {
    "function": "create_variable",
    "name": "analytics_data",
    "value": {
      "date": "{{ report_date }}",
      "new_users": "{{ new_users|length }}",
      "total_sessions": "{{ daily_sessions|length }}",
      "unique_users": "{{ daily_sessions|map(attribute='user_id')|unique|length }}",
      "average_session_duration": "{{ daily_sessions|map(attribute='duration')|average }}",
      "top_pages": "{{ daily_sessions|group_by('page')|limit(10) }}"
    }
  },
  {
    "function": "add_record",
    "table": "daily_analytics",
    "data": "{{ analytics_data }}"
  },
  {
    "function": "custom_function",
    "name": "send_analytics_email",
    "inputs": {
      "recipients": ["admin@company.com", "marketing@company.com"],
      "report_data": "{{ analytics_data }}",
      "report_date": "{{ report_date }}"
    },
    "execution_mode": "async"
  }
]
```

### Email Campaign Automation

**Weekly Newsletter Distribution:**

```javascript
// Automated email campaign processing
[
  {
    "function": "create_variable",
    "name": "campaign_config",
    "value": {
      "campaign_name": "weekly_newsletter",
      "send_date": "{{ now|date('Y-m-d') }}",
      "batch_size": 100,
      "delay_between_batches": 60
    }
  },
  {
    "function": "query_all_records",
    "table": "newsletter_subscribers",
    "filter": {
      "status": "active",
      "unsubscribed": false
    },
    "return_as": "subscribers"
  },
  {
    "function": "custom_function",
    "name": "generate_newsletter_content",
    "inputs": {
      "template_name": "weekly_digest",
      "date_range": {
        "start": "{{ now - 604800 }}",
        "end": "{{ now }}"
      }
    },
    "return_as": "newsletter_content"
  },
  {
    "function": "create_variable",
    "name": "subscriber_batches",
    "value": "{{ subscribers|batch(campaign_config.batch_size) }}"
  },
  {
    "function": "loop",
    "array": "{{ subscriber_batches }}",
    "operations": [
      {
        "function": "loop",
        "array": "{{ item }}",
        "operations": [
          {
            "function": "custom_function",
            "name": "send_personalized_email",
            "inputs": {
              "recipient": "{{ item }}",
              "content": "{{ newsletter_content }}",
              "campaign_id": "{{ campaign_config.campaign_name }}_{{ campaign_config.send_date }}"
            },
            "execution_mode": "async"
          }
        ]
      },
      {
        "function": "wait",
        "duration": "{{ campaign_config.delay_between_batches }}"
      }
    ]
  },
  {
    "function": "add_record",
    "table": "campaign_logs",
    "data": {
      "campaign_name": "{{ campaign_config.campaign_name }}",
      "sent_date": "{{ now }}",
      "recipients_count": "{{ subscribers|length }}",
      "batches_sent": "{{ subscriber_batches|length }}",
      "status": "completed"
    }
  }
]
```

### Data Synchronization

**External System Data Sync:**

```javascript
// Multi-system data synchronization
[
  {
    "function": "create_variable",
    "name": "sync_session",
    "value": {
      "session_id": "{{ uuid }}",
      "started_at": "{{ now }}",
      "systems": ["crm", "inventory", "support"],
      "status": "running"
    }
  },
  {
    "function": "loop",
    "array": "{{ sync_session.systems }}",
    "operations": [
      {
        "function": "external_api_request",
        "url": "{{ env[item|upper + '_API_URL'] }}/export/incremental",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ env[item|upper + '_API_KEY'] }}",
          "Accept": "application/json"
        },
        "query": {
          "since": "{{ now - 3600 }}",
          "format": "json"
        },
        "return_as": "system_data"
      },
      {
        "function": "conditional",
        "condition": "{{ system_data.records|length > 0 }}",
        "true_branch": [
          {
            "function": "loop",
            "array": "{{ system_data.records }}",
            "operations": [
              {
                "function": "add_or_edit_record",
                "table": "{{ item_parent.name }}_sync",
                "data": {
                  "external_id": "{{ item.id }}",
                  "source_system": "{{ item_parent.name }}",
                  "data": "{{ item }}",
                  "synced_at": "{{ now }}",
                  "sync_session": "{{ sync_session.session_id }}"
                },
                "identifier": "external_id"
              }
            ]
          }
        ]
      },
      {
        "function": "add_record",
        "table": "sync_logs",
        "data": {
          "session_id": "{{ sync_session.session_id }}",
          "system": "{{ item }}",
          "records_synced": "{{ system_data.records|length }}",
          "status": "completed",
          "completed_at": "{{ now }}"
        }
      }
    ]
  },
  {
    "function": "edit_record",
    "table": "sync_sessions",
    "id": "{{ sync_session.session_id }}",
    "data": {
      "status": "completed",
      "completed_at": "{{ now }}",
      "duration": "{{ now - sync_session.started_at }}"
    }
  }
]
```

### Cleanup and Maintenance

**Database Cleanup Task:**

```javascript
// Automated database maintenance
[
  {
    "function": "create_variable",
    "name": "cleanup_config",
    "value": {
      "retention_days": 90,
      "batch_size": 1000,
      "tables_to_clean": ["logs", "temp_files", "expired_sessions", "old_notifications"]
    }
  },
  {
    "function": "create_variable",
    "name": "cutoff_date",
    "value": "{{ now - (cleanup_config.retention_days * 86400) }}"
  },
  {
    "function": "loop",
    "array": "{{ cleanup_config.tables_to_clean }}",
    "operations": [
      {
        "function": "create_variable",
        "name": "cleanup_stats",
        "value": {
          "table": "{{ item }}",
          "records_deleted": 0,
          "batches_processed": 0
        }
      },
      {
        "function": "loop",
        "condition": "true",
        "operations": [
          {
            "function": "query_all_records",
            "table": "{{ item }}",
            "filter": {
              "created_at": {"$lt": "{{ cutoff_date }}"}
            },
            "limit": "{{ cleanup_config.batch_size }}",
            "return_as": "records_to_delete"
          },
          {
            "function": "conditional",
            "condition": "{{ records_to_delete|length == 0 }}",
            "true_branch": [
              {
                "function": "break_loop"
              }
            ]
          },
          {
            "function": "loop",
            "array": "{{ records_to_delete }}",
            "operations": [
              {
                "function": "delete_record",
                "table": "{{ item_parent.name }}",
                "id": "{{ item.id }}"
              }
            ]
          },
          {
            "function": "update_variable",
            "name": "cleanup_stats",
            "operation": "merge",
            "value": {
              "records_deleted": "{{ cleanup_stats.records_deleted + records_to_delete|length }}",
              "batches_processed": "{{ cleanup_stats.batches_processed + 1 }}"
            }
          },
          {
            "function": "wait",
            "duration": 5
          }
        ]
      },
      {
        "function": "add_record",
        "table": "cleanup_logs",
        "data": {
          "table_name": "{{ cleanup_stats.table }}",
          "records_deleted": "{{ cleanup_stats.records_deleted }}",
          "batches_processed": "{{ cleanup_stats.batches_processed }}",
          "cleanup_date": "{{ now }}",
          "retention_days": "{{ cleanup_config.retention_days }}"
        }
      }
    ]
  }
]
```

## ⚡ **Performance Optimization**

### Batch Processing Strategies

**Optimized Large Dataset Processing:**

```javascript
// Efficient batch processing pattern
[
  {
    "function": "create_variable",
    "name": "processing_config",
    "value": {
      "batch_size": 500,
      "max_processing_time": 240,
      "memory_threshold": 80,
      "retry_failed_batches": true
    }
  },
  {
    "function": "query_all_records",
    "table": "pending_processing_items",
    "filter": {"status": "pending"},
    "limit": 10000,
    "sort": "priority desc, created_at asc",
    "return_as": "items_to_process"
  },
  {
    "function": "create_variable",
    "name": "batches",
    "value": "{{ items_to_process|batch(processing_config.batch_size) }}"
  },
  {
    "function": "create_variable",
    "name": "processing_stats",
    "value": {
      "started_at": "{{ now }}",
      "total_items": "{{ items_to_process|length }}",
      "batches_total": "{{ batches|length }}",
      "batches_completed": 0,
      "items_processed": 0,
      "failed_items": 0
    }
  },
  {
    "function": "loop",
    "array": "{{ batches }}",
    "operations": [
      {
        "function": "conditional",
        "condition": "{{ (now - processing_stats.started_at) > processing_config.max_processing_time }}",
        "true_branch": [
          {
            "function": "add_record",
            "table": "processing_logs",
            "data": {
              "session_type": "background_task",
              "status": "timeout",
              "message": "Processing stopped due to time limit",
              "stats": "{{ processing_stats }}"
            }
          },
          {
            "function": "break_loop"
          }
        ]
      },
      {
        "function": "try_catch",
        "try_block": [
          {
            "function": "loop",
            "array": "{{ item }}",
            "operations": [
              {
                "function": "custom_function",
                "name": "process_single_item",
                "inputs": {
                  "item_data": "{{ item }}",
                  "processing_options": "{{ processing_config }}"
                },
                "return_as": "processing_result"
              },
              {
                "function": "edit_record",
                "table": "pending_processing_items",
                "id": "{{ item.id }}",
                "data": {
                  "status": "{{ processing_result.success ? 'completed' : 'failed' }}",
                  "processed_at": "{{ now }}",
                  "result": "{{ processing_result }}"
                }
              }
            ]
          }
        ],
        "catch_block": [
          {
            "function": "update_variable",
            "name": "processing_stats",
            "operation": "merge",
            "value": {
              "failed_items": "{{ processing_stats.failed_items + item|length }}"
            }
          }
        ]
      },
      {
        "function": "update_variable",
        "name": "processing_stats",
        "operation": "merge",
        "value": {
          "batches_completed": "{{ processing_stats.batches_completed + 1 }}",
          "items_processed": "{{ processing_stats.items_processed + item|length }}"
        }
      },
      {
        "function": "wait",
        "duration": 2
      }
    ]
  }
]
```

## 🔐 **Error Handling and Monitoring**

### Comprehensive Error Management

**Robust Error Handling Pattern:**

```javascript
// Error handling and recovery system
[
  {
    "function": "create_variable",
    "name": "task_execution",
    "value": {
      "task_name": "data_processing_task",
      "execution_id": "{{ uuid }}",
      "started_at": "{{ now }}",
      "status": "running",
      "retry_count": 0,
      "max_retries": 3
    }
  },
  {
    "function": "try_catch",
    "try_block": [
      {
        "function": "custom_function",
        "name": "main_task_logic",
        "inputs": {
          "execution_context": "{{ task_execution }}"
        },
        "return_as": "task_result"
      },
      {
        "function": "update_variable",
        "name": "task_execution",
        "operation": "merge",
        "value": {
          "status": "completed",
          "completed_at": "{{ now }}",
          "result": "{{ task_result }}"
        }
      }
    ],
    "catch_block": [
      {
        "function": "update_variable",
        "name": "task_execution",
        "operation": "merge",
        "value": {
          "status": "failed",
          "error": "{{ error }}",
          "failed_at": "{{ now }}"
        }
      },
      {
        "function": "conditional",
        "condition": "{{ task_execution.retry_count < task_execution.max_retries }}",
        "true_branch": [
          {
            "function": "add_record",
            "table": "task_retry_queue",
            "data": {
              "task_name": "{{ task_execution.task_name }}",
              "execution_id": "{{ task_execution.execution_id }}",
              "retry_count": "{{ task_execution.retry_count + 1 }}",
              "retry_at": "{{ now + (task_execution.retry_count + 1) * 300 }}",
              "original_error": "{{ error }}"
            }
          }
        ],
        "false_branch": [
          {
            "function": "external_api_request",
            "url": "{{ env.ALERT_WEBHOOK_URL }}",
            "method": "POST",
            "body": {
              "alert_type": "task_failure",
              "task_name": "{{ task_execution.task_name }}",
              "execution_id": "{{ task_execution.execution_id }}",
              "error": "{{ error }}",
              "retry_exhausted": true
            }
          }
        ]
      }
    ]
  },
  {
    "function": "add_record",
    "table": "task_execution_logs",
    "data": "{{ task_execution }}"
  }
]
```

## 💡 **Pro Tips**

- **Start Small**: Begin with simple tasks and gradually add complexity
- **Monitor Performance**: Track execution times and resource usage regularly
- **Handle Failures Gracefully**: Implement retry logic and proper error handling
- **Use Appropriate Scheduling**: Don't over-schedule tasks that could overlap
- **Batch Large Operations**: Process large datasets in manageable chunks
- **Document Task Dependencies**: Keep track of which tasks depend on others

## 🔧 **Troubleshooting**

### Common Background Task Issues

**Problem**: Task runs longer than expected and times out  
**Solution**: Implement batch processing and break large operations into smaller chunks

**Problem**: Tasks are skipping scheduled runs  
**Solution**: Check if previous executions are still running and optimize task duration

**Problem**: Background task errors not being logged  
**Solution**: Add comprehensive error handling and logging to function stacks

**Problem**: Resource usage spikes during task execution  
**Solution**: Implement memory management and add delays between intensive operations

---

**Next Steps**: Ready to automate your workflows? Check out [Custom Functions](custom-functions.md) for reusable logic or explore [Async Functions](async-functions.md) for non-blocking operations