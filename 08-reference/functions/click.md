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
- Background Tasks
- Cron Jobs
- Scheduling
title: Background Tasks (Cron Jobs)
---

# Background Tasks (Cron Jobs)

## 📋 **Quick Summary**
Background tasks (cron jobs) in Xano are scheduled workflows that run automatically at specified intervals. Perfect for marketing emails, report generation, analytics processing, and data maintenance tasks without manual intervention or API calls.

## 🎯 **Core Concepts**

### Background Task Features
- **Scheduled Execution**: Run workflows on time-based triggers
- **No Input/Output**: Self-contained tasks without external parameters
- **Automatic Retry**: Built-in error handling and retry mechanisms
- **Resource Management**: Prevents overlapping executions
- **Monitoring**: Track execution history and performance

### Available Plans
- **Starter Plan and Higher**: Background tasks included
- **Execution Limits**: Based on plan tier
- **Concurrent Tasks**: Multiple tasks can run simultaneously
- **Schedule Flexibility**: From minutes to months intervals

## 🛠️ **Implementation Guide**

### Step 1: Access Background Tasks

```javascript
// Navigate to Background Tasks in Xano
// 1. Click "Background Tasks" in left-hand menu
// 2. View existing scheduled tasks
// 3. Monitor task execution status and history
```

### Step 2: Create New Background Task

```javascript
// Background Task Configuration
{
  "name": "Daily Report Generation",
  "description": "Generate and email daily analytics reports",
  "tags": ["reporting", "analytics", "daily"],
  "request_history": true,
  "data_source": "primary_database",
  "status": "inactive" // Start inactive for testing
}
```

### Step 3: Build Function Stack

```javascript
// Example: Daily Report Generation Task
{
  "function_stack": [
    // Step 1: Query daily metrics
    {
      "function": "Query All Records",
      "table": "user_activities",
      "filter": {
        "created_at": {
          ">=": "{{start_of_day}}",
          "<": "{{end_of_day}}"
        }
      },
      "return_variable": "daily_activities"
    },
    
    // Step 2: Calculate metrics
    {
      "function": "Math",
      "operation": "count",
      "values": "{{daily_activities}}",
      "return_variable": "total_activities"
    },
    
    // Step 3: Query revenue data
    {
      "function": "Query All Records",
      "table": "orders",
      "filter": {
        "status": "completed",
        "created_at": {
          ">=": "{{start_of_day}}",
          "<": "{{end_of_day}}"
        }
      },
      "return_variable": "daily_orders"
    },
    
    // Step 4: Calculate revenue
    {
      "function": "Math",
      "operation": "sum",
      "values": "{{daily_orders.total}}",
      "return_variable": "daily_revenue"
    },
    
    // Step 5: Create report record
    {
      "function": "Add Record",
      "table": "daily_reports",
      "data": {
        "report_date": "{{current_date}}",
        "total_activities": "{{total_activities}}",
        "total_orders": "{{daily_orders.length}}",
        "total_revenue": "{{daily_revenue}}",
        "generated_at": "{{timestamp}}"
      },
      "return_variable": "report_record"
    },
    
    // Step 6: Send email notification
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
          "to": [{"email": "admin@company.com"}],
          "subject": "Daily Report - {{current_date}}"
        }],
        "from": {"email": "reports@company.com"},
        "content": [{
          "type": "text/html",
          "value": "<h2>Daily Report</h2><p>Activities: {{total_activities}}</p><p>Orders: {{daily_orders.length}}</p><p>Revenue: ${{daily_revenue}}</p>"
        }]
      }
    }
  ]
}
```

### Step 4: Configure Schedule

```javascript
// Schedule Configuration Options
const scheduleExamples = {
  "every_minute": "* * * * *",
  "every_5_minutes": "*/5 * * * *",
  "every_hour": "0 * * * *",
  "daily_at_9am": "0 9 * * *",
  "daily_at_midnight": "0 0 * * *",
  "weekly_monday_9am": "0 9 * * 1",
  "monthly_first_day": "0 9 1 * *",
  "quarterly": "0 9 1 1,4,7,10 *"
}

// Example: Daily report at 8 AM
{
  "schedule": {
    "cron_expression": "0 8 * * *",
    "timezone": "America/New_York",
    "skip_if_running": true // Prevent overlapping executions
  }
}
```

## 🔗 **Integration Examples**

### n8n Background Task Triggering
```javascript
// Trigger n8n workflow from Xano background task
{
  "function": "External API Request",
  "url": "https://your-n8n-instance.com/webhook/xano-trigger",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{env.N8N_WEBHOOK_TOKEN}}",
    "Content-Type": "application/json"
  },
  "body": {
    "task_type": "daily_cleanup",
    "timestamp": "{{timestamp}}",
    "data": "{{collected_data}}"
  }
}

// n8n can then process the data and trigger additional workflows
```

### WeWeb Data Refresh
```javascript
// Update WeWeb app data through background task
{
  "function": "External API Request",
  "url": "https://api.weweb.io/v1/collections/refresh",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{env.WEWEB_API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "collection_id": "user_dashboard_data",
    "force_refresh": true,
    "updated_records": "{{processed_records}}"
  }
}
```

## 🚀 **Advanced Usage Patterns**

### Data Cleanup and Archival
```javascript
// Monthly data archival background task
{
  "function_stack": [
    // Archive old records
    {
      "function": "Query All Records",
      "table": "user_sessions",
      "filter": {
        "created_at": {
          "<": "{{timestamp - (30 * 24 * 60 * 60 * 1000)}}" // 30 days ago
        }
      },
      "return_variable": "old_sessions"
    },
    
    // Move to archive table
    {
      "function": "Loop",
      "input_array": "{{old_sessions}}",
      "loop_item_variable": "session",
      "steps": [
        {
          "function": "Add Record",
          "table": "archived_sessions",
          "data": "{{session}}"
        },
        {
          "function": "Delete Record",
          "table": "user_sessions",
          "record_id": "{{session.id}}"
        }
      ]
    }
  ],
  "schedule": "0 2 1 * *" // First day of month at 2 AM
}
```

### Cache Warming
```javascript
// Pre-populate cache with frequently accessed data
{
  "function_stack": [
    // Get popular products
    {
      "function": "Query All Records",
      "table": "products",
      "sort": { "field": "view_count", "order": "desc" },
      "limit": 100,
      "return_variable": "popular_products"
    },
    
    // Cache product data
    {
      "function": "Loop",
      "input_array": "{{popular_products}}",
      "loop_item_variable": "product",
      "steps": [
        {
          "function": "Data Caching (Redis)",
          "operation": "set",
          "key": "product_{{product.id}}",
          "value": "{{product}}",
          "ttl": 3600 // 1 hour
        }
      ]
    }
  ],
  "schedule": "*/30 * * * *" // Every 30 minutes
}
```

### Subscription Management
```javascript
// Check and update subscription statuses
{
  "function_stack": [
    // Find expiring subscriptions
    {
      "function": "Query All Records",
      "table": "subscriptions",
      "filter": {
        "status": "active",
        "expires_at": {
          "<=": "{{timestamp + (24 * 60 * 60 * 1000)}}" // Next 24 hours
        }
      },
      "return_variable": "expiring_subscriptions"
    },
    
    // Send renewal notifications
    {
      "function": "Loop",
      "input_array": "{{expiring_subscriptions}}",
      "loop_item_variable": "subscription",
      "steps": [
        {
          "function": "External API Request",
          "url": "https://api.stripe.com/v1/customers/{{subscription.stripe_customer_id}}",
          "method": "GET",
          "headers": {
            "Authorization": "Bearer {{env.STRIPE_SECRET_KEY}}"
          },
          "return_variable": "customer_data"
        },
        {
          "function": "External API Request", // Send email
          "url": "https://api.sendgrid.com/v3/mail/send",
          "method": "POST",
          "body": {
            "personalizations": [{
              "to": [{"email": "{{customer_data.email}}"}],
              "subject": "Subscription Renewal Reminder"
            }],
            "content": [{
              "type": "text/html",
              "value": "Your subscription expires tomorrow. <a href='{{renewal_link}}'>Renew now</a>"
            }]
          }
        }
      ]
    }
  ],
  "schedule": "0 10 * * *" // Daily at 10 AM
}
```

## 🎯 **Best Practices**

### 1. Error Handling
```javascript
// Implement robust error handling in background tasks
{
  "function": "Try-Catch",
  "try_steps": [
    // Main task logic here
    {
      "function": "External API Request",
      "url": "https://api.third-party.com/data",
      "return_variable": "api_response"
    }
  ],
  "catch_steps": [
    // Log error
    {
      "function": "Add Record",
      "table": "error_logs",
      "data": {
        "task_name": "{{task.name}}",
        "error_message": "{{error.message}}",
        "occurred_at": "{{timestamp}}"
      }
    },
    // Send alert
    {
      "function": "External API Request",
      "url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK",
      "method": "POST",
      "body": {
        "text": "Background task failed: {{task.name}} - {{error.message}}"
      }
    }
  ]
}
```

### 2. Resource Management
```javascript
// Prevent resource exhaustion
{
  "function": "Query All Records",
  "table": "large_dataset",
  "limit": 1000, // Process in batches
  "offset": "{{batch_number * 1000}}",
  "return_variable": "batch_data"
}

// Use conditional logic to process in chunks
{
  "function": "Conditional",
  "condition": "{{batch_data.length > 0}}",
  "true_steps": [
    // Process batch
    // Schedule next batch if needed
  ]
}
```

### 3. Monitoring and Alerting
```javascript
// Track task performance
{
  "function": "Add Record",
  "table": "task_metrics",
  "data": {
    "task_name": "{{task.name}}",
    "execution_time": "{{execution_duration}}",
    "records_processed": "{{processed_count}}",
    "success": true,
    "executed_at": "{{timestamp}}"
  }
}

// Alert on task failures or long execution times
{
  "function": "Conditional",
  "condition": "{{execution_duration > 300000}}", // 5 minutes
  "true_steps": [
    {
      "function": "External API Request",
      "url": "https://api.pagerduty.com/incidents",
      "method": "POST",
      "body": {
        "incident": {
          "type": "incident",
          "title": "Long running background task: {{task.name}}",
          "urgency": "low"
        }
      }
    }
  ]
}
```

## 🔧 **Common Use Cases**

### Marketing Automation
```javascript
// Weekly newsletter generation and sending
{
  "name": "Weekly Newsletter",
  "schedule": "0 9 * * 1", // Monday 9 AM
  "function_stack": [
    // Collect week's content
    // Generate personalized newsletters
    // Send via email service
    // Track delivery metrics
  ]
}
```

### Data Synchronization
```javascript
// Sync with external CRM system
{
  "name": "CRM Data Sync",
  "schedule": "*/15 * * * *", // Every 15 minutes
  "function_stack": [
    // Pull updates from CRM
    // Update local database
    // Push local changes to CRM
    // Log sync status
  ]
}
```

### System Maintenance
```javascript
// Database optimization and cleanup
{
  "name": "Database Maintenance",
  "schedule": "0 2 * * 0", // Sunday 2 AM
  "function_stack": [
    // Archive old records
    // Optimize database indexes
    // Clear temporary files
    // Generate maintenance report
  ]
}
```

### Financial Reporting
```javascript
// Monthly financial reports
{
  "name": "Monthly Financial Report",
  "schedule": "0 8 1 * *", // First day of month 8 AM
  "function_stack": [
    // Calculate monthly revenue
    // Generate expense reports
    // Create financial summaries
    // Email to stakeholders
  ]
}
```

## 🔍 **Troubleshooting**

### Task Not Running
- Verify task is set to "Active" status
- Check cron expression syntax
- Confirm timezone settings
- Review execution history for errors

### Performance Issues
- Limit query result sets
- Process data in batches
- Optimize database queries
- Monitor execution duration

### Failed Executions
- Implement error handling
- Add retry logic for API calls
- Log errors for debugging
- Set up failure notifications

---

*Background tasks provide powerful automation capabilities for scheduled operations, data processing, and system maintenance without manual intervention.*