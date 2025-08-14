---
title: "Background Tasks - Scheduled and Recurring Operations"
description: "Set up scheduled jobs, recurring tasks, and background processing in Xano for automated workflows"
category: function-stack
subcategory: automation
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- background-tasks
- scheduling
- cron
- automation
- recurring-jobs
---

# Background Tasks - Scheduled and Recurring Operations

## Quick Summary

> **What it is:** Automated functions that run on a schedule or in the background without user interaction
> 
> **When to use:** For recurring operations like daily reports, data cleanup, synchronization, or any task that needs to run at specific times
> 
> **Key benefit:** Automate repetitive tasks and maintain your system without manual intervention
> 
> **Common uses:** Daily backups, email digests, data synchronization, cleanup operations

## What You'll Learn

- Setting up scheduled tasks with cron expressions
- Creating recurring background jobs
- Managing task execution and monitoring
- Best practices for reliable automation
- Integration patterns with n8n and WeWeb

## Types of Background Tasks

### Scheduled Tasks
Run at specific times:
- Daily reports at 9 AM
- Weekly backups on Sunday
- Monthly billing on the 1st

### Recurring Tasks
Run at intervals:
- Check for updates every 5 minutes
- Process queue every 30 seconds
- Sync data every hour

### Triggered Tasks
Run based on conditions:
- When queue reaches threshold
- After system events
- On data changes

## Setting Up Background Tasks

### Basic Configuration

```javascript
Background Task Settings:
  Name: daily_report_generator
  Schedule: "0 9 * * *"  // Every day at 9 AM
  Timezone: "America/New_York"
  Enabled: true
  
Function Stack:
  - Query yesterday's data
  - Generate report
  - Send email to stakeholders
  - Log execution
```

### Cron Expression Guide

```javascript
* * * * *
│ │ │ │ │
│ │ │ │ └─ Day of Week (0-7, Sun=0 or 7)
│ │ │ └─── Month (1-12)
│ │ └───── Day of Month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)

Common Patterns:
"0 0 * * *"      // Daily at midnight
"0 */2 * * *"    // Every 2 hours
"*/15 * * * *"   // Every 15 minutes
"0 9 * * 1"      // Mondays at 9 AM
"0 0 1 * *"      // First day of month
```

## Practical Examples

### Example 1: Daily Email Digest

```javascript
// Runs daily at 8 AM
Background Task: send_daily_digest
  
  // Get active users
  users = Query: users WHERE subscribed = true
  
  FOR EACH user IN users {
    // Get user's activity
    activities = Query: activities 
      WHERE user_id = user.id 
      AND created_at > yesterday()
    
    // Skip if no activity
    IF (activities.count == 0) CONTINUE
    
    // Generate personalized email
    email_content = Template_Engine(
      digest_template,
      {
        user_name: user.name,
        activities: activities,
        stats: calculate_stats(activities)
      }
    )
    
    // Send email
    Send_Email(user.email, "Your Daily Digest", email_content)
  }
  
  // Log completion
  Create_Log("Daily digest sent to " + users.count + " users")
```

### Example 2: Data Cleanup

```javascript
// Runs nightly at 2 AM
Background Task: cleanup_old_data
  
  // Delete old logs (>30 days)
  deleted_logs = Delete_Records: logs 
    WHERE created_at < DATE_SUB(NOW(), 30, 'days')
  
  // Archive old orders (>1 year)
  old_orders = Query: orders 
    WHERE created_at < DATE_SUB(NOW(), 1, 'year')
    AND status = 'completed'
  
  FOR EACH order IN old_orders {
    // Move to archive table
    Create_Record: archived_orders (order)
    Delete_Record: orders WHERE id = order.id
  }
  
  // Clean temporary files
  temp_files = Query: files WHERE temporary = true
    AND created_at < DATE_SUB(NOW(), 24, 'hours')
  
  FOR EACH file IN temp_files {
    Delete_File(file.path)
    Delete_Record: files WHERE id = file.id
  }
  
  Log("Cleanup completed: " + deleted_logs + " logs, " + 
      old_orders.count + " orders archived")
```

### Example 3: Data Synchronization

```javascript
// Runs every 30 minutes
Background Task: sync_with_external_system
  
  // Get last sync timestamp
  last_sync = Get_Setting("last_sync_time") || DATE_SUB(NOW(), 1, 'hour')
  
  // Fetch updates from external API
  external_updates = External_API_Request(
    "https://api.example.com/updates",
    { since: last_sync }
  )
  
  // Process updates
  success_count = 0
  error_count = 0
  
  FOR EACH update IN external_updates.data {
    TRY {
      // Find or create local record
      local_record = Query: records 
        WHERE external_id = update.id
      
      IF (local_record) {
        Update_Record: records (update)
      } ELSE {
        Create_Record: records (update)
      }
      success_count++
    } CATCH (error) {
      error_count++
      Log_Error("Sync failed for " + update.id + ": " + error)
    }
  }
  
  // Update last sync time
  Update_Setting("last_sync_time", NOW())
  
  // Send notification if errors
  IF (error_count > 0) {
    Send_Alert("Sync completed with " + error_count + " errors")
  }
```

## Advanced Patterns

### Queue Processing

```javascript
// Runs every minute
Background Task: process_email_queue
  
  // Get pending emails (max 50)
  pending = Query: email_queue 
    WHERE status = 'pending'
    LIMIT 50
  
  FOR EACH email IN pending {
    TRY {
      // Send email
      Send_Email(email.to, email.subject, email.body)
      
      // Mark as sent
      Update_Record: email_queue
        id: email.id
        status: 'sent'
        sent_at: NOW()
        
    } CATCH (error) {
      // Increment retry count
      Update_Record: email_queue
        id: email.id
        retry_count: email.retry_count + 1
        last_error: error.message
      
      // Mark as failed after 3 retries
      IF (email.retry_count >= 3) {
        Update_Record: email_queue
          id: email.id
          status: 'failed'
      }
    }
  }
```

### Monitoring and Alerting

```javascript
// Runs every 5 minutes
Background Task: system_monitor
  
  // Check API response time
  start = NOW()
  test_result = External_API_Request("https://api.example.com/health")
  response_time = NOW() - start
  
  IF (response_time > 2000) {  // Over 2 seconds
    Send_Alert("API slow response: " + response_time + "ms")
  }
  
  // Check database size
  db_stats = Query_Database_Stats()
  IF (db_stats.usage_percent > 80) {
    Send_Alert("Database usage at " + db_stats.usage_percent + "%")
  }
  
  // Check failed jobs
  failed_jobs = Query: background_tasks_log 
    WHERE status = 'failed'
    AND created_at > DATE_SUB(NOW(), 1, 'hour')
  
  IF (failed_jobs.count > 5) {
    Send_Alert(failed_jobs.count + " tasks failed in last hour")
  }
```

## Integration Patterns

### With n8n

```javascript
// Trigger n8n workflow on schedule
Background Task: trigger_n8n_workflow
  
  // Collect data for n8n
  daily_stats = {
    users: Count_Records("users"),
    orders: Count_Records("orders", "created_at > yesterday()"),
    revenue: Sum_Field("orders", "total", "created_at > yesterday()")
  }
  
  // Send to n8n webhook
  External_API_Request(
    "https://n8n.example.com/webhook/daily-report",
    {
      method: "POST",
      body: daily_stats
    }
  )
```

### With WeWeb

```javascript
// Prepare cached data for WeWeb
Background Task: cache_dashboard_data
  
  // Calculate expensive metrics
  dashboard_data = {
    total_users: Count_Records("users"),
    active_users: Count_Records("users", "last_login > DATE_SUB(NOW(), 30, 'days')"),
    revenue_mtd: Calculate_Revenue_MTD(),
    top_products: Get_Top_Products(10),
    recent_orders: Get_Recent_Orders(20)
  }
  
  // Cache for frontend
  Set_Cache_Value("dashboard_data", dashboard_data, TTL: 3600)
```

## Best Practices

### Error Handling

```javascript
Background Task: important_task
  TRY {
    // Main logic
    perform_operations()
    
    // Log success
    Create_Log("Task completed successfully")
    
  } CATCH (error) {
    // Log error
    Create_Error_Log(error)
    
    // Send notification
    Send_Alert("Background task failed: " + error.message)
    
    // Re-throw for retry mechanism
    THROW error
  }
```

### Idempotency

Make tasks safe to run multiple times:

```javascript
// Check if already processed
existing = Query: processed_records 
  WHERE date = today()
  
IF (existing) {
  Log("Already processed for today")
  RETURN
}

// Process and mark complete
process_data()
Create_Record: processed_records { date: today() }
```

### Performance

```javascript
// Process in batches
batch_size = 100
offset = 0

WHILE (true) {
  batch = Query: large_table 
    LIMIT batch_size 
    OFFSET offset
  
  IF (batch.count == 0) BREAK
  
  process_batch(batch)
  offset = offset + batch_size
  
  // Prevent timeout
  IF (execution_time() > 50000) {  // 50 seconds
    // Queue remaining for next run
    BREAK
  }
}
```

## Common Mistakes to Avoid

1. **No Error Handling** - Tasks fail silently
2. **Too Frequent Execution** - Overloads system
3. **No Monitoring** - Failures go unnoticed
4. **Long Running Tasks** - Risk timeout
5. **No Idempotency** - Duplicate processing

## Try This

Create a smart cleanup system:
1. Daily: Delete old logs
2. Weekly: Archive completed orders
3. Monthly: Generate usage reports
4. Monitor all task executions
5. Alert on failures

## Pro Tips

💡 **Stagger Schedules:** Don't run all tasks at midnight - spread the load

💡 **Use Queues:** For high-volume processing, use queue pattern

💡 **Monitor Execution:** Track duration and success rates

💡 **Test Locally:** Test background tasks as regular functions first

Remember: Background tasks keep your system healthy and your users happy with automated, reliable operations!