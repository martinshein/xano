---
title: "Async Functions - Non-Blocking Operations"
description: "Execute functions asynchronously for better performance and user experience in Xano"
category: function-stack
subcategory: performance
difficulty: advanced
has_code_examples: true
last_updated: '2025-01-23'
tags:
- async
- performance
- non-blocking
- parallel-processing
- optimization
---

# Async Functions - Non-Blocking Operations

## Quick Summary

> **What it is:** Functions that run independently without blocking your main execution flow, allowing multiple operations to happen simultaneously
> 
> **When to use:** When you have time-consuming operations that don't need immediate results - emails, notifications, data processing, external API calls
> 
> **Key benefit:** Dramatically improves API response times by offloading slow operations
> 
> **Common pattern:** Return success immediately, process in background

## What You'll Learn

- Understanding async vs sync execution
- Setting up async functions properly
- Common async patterns
- Error handling in async operations
- Best practices for n8n and WeWeb

## Sync vs Async Execution

### Synchronous (Default)
```javascript
// User waits for everything
1. Receive request
2. Process payment (2 seconds)
3. Send email (1 second)
4. Update inventory (0.5 seconds)
5. Return response
// Total wait: 3.5 seconds
```

### Asynchronous (Optimized)
```javascript
// User gets instant response
1. Receive request
2. Process payment (2 seconds)
3. Queue async tasks:
   - Send email (runs in background)
   - Update inventory (runs in background)
4. Return response immediately
// Total wait: 2 seconds
```

## Creating Async Functions

### Basic Setup

```javascript
// Mark function as async
Function Settings:
  Type: Async
  Timeout: 30 seconds
  Retry on failure: Yes

// Function executes independently
Async Function: send_notification
  - Get user email
  - Generate email content
  - Send via email service
  - Log delivery status
```

### Calling Async Functions

```javascript
// In your main function stack
1. Process critical operations
2. Call Async Function: send_notification
   // Doesn't wait for completion
3. Return success to user

// Notification sends in background
```

## Practical Examples

### Example 1: Order Processing

```javascript
// Main API endpoint
Process Order:
  // Critical path (synchronous)
  - Validate order
  - Process payment
  - Create order record
  
  // Non-critical (async)
  ASYNC: send_order_confirmation_email
  ASYNC: update_inventory_levels
  ASYNC: notify_warehouse_system
  ASYNC: generate_invoice_pdf
  
  // Return immediately
  Return {
    success: true,
    order_id: new_order.id,
    message: "Order processed successfully"
  }
```

### Example 2: User Registration

```javascript
// Registration endpoint
Register User:
  // Must complete before response
  - Validate input
  - Check email uniqueness
  - Create user record
  - Generate auth token
  
  // Can happen later
  ASYNC: send_welcome_email
  ASYNC: create_default_preferences
  ASYNC: sync_to_crm
  ASYNC: trigger_onboarding_sequence
  
  Return {
    user_id: new_user.id,
    token: auth_token
  }
```

### Example 3: Data Import

```javascript
// CSV import endpoint
Import Data:
  // Quick validation
  - Check file format
  - Validate headers
  - Create import job
  
  // Heavy processing (async)
  ASYNC: process_csv_rows {
    FOR EACH row IN csv_data {
      - Validate row data
      - Transform fields
      - Insert/update record
      - Log results
    }
    - Send completion email
  }
  
  Return {
    job_id: import_job.id,
    status: "processing",
    check_status_url: "/import/status/" + job_id
  }
```

## Error Handling

### Async Error Patterns

```javascript
// Async function with error handling
ASYNC: risky_operation
  TRY {
    - Call external API
    - Process response
    - Update database
  } CATCH (error) {
    - Log error details
    - Send alert to admin
    - Queue for retry
    - Update job status: "failed"
  }
```

### Retry Logic

```javascript
// Configure retry behavior
Async Function Settings:
  Max retries: 3
  Retry delay: 60 seconds
  Backoff multiplier: 2

// Automatic retry on failure
// Delays: 60s, 120s, 240s
```

## Status Tracking

### Job Status Pattern

```javascript
// Create job record
job = Create Record: jobs {
  type: "data_import",
  status: "pending",
  created_at: NOW()
}

// Start async processing
ASYNC: process_job(job.id)

// In async function
Update Record: jobs
  id: job_id
  status: "processing"
  started_at: NOW()

// On completion
Update Record: jobs
  id: job_id
  status: "completed"
  completed_at: NOW()
  result: process_result
```

### Status Check Endpoint

```javascript
// GET /job/status/{id}
Get Job Status:
  job = Get Record: jobs WHERE id = input.id
  
  Return {
    id: job.id,
    status: job.status,
    progress: job.progress_percentage,
    result: job.result,
    error: job.error_message
  }
```

## Integration Patterns

### With n8n

```javascript
// Webhook triggers async processing
Webhook Endpoint:
  // Quick validation
  - Validate webhook signature
  - Parse payload
  
  // Queue for processing
  ASYNC: process_webhook {
    // Complex workflow
    - Transform data
    - Update multiple systems
    - Trigger n8n workflow
    - Log all activities
  }
  
  // Immediate response to n8n
  Return { received: true }
```

### With WeWeb

```javascript
// File upload with processing
Upload Endpoint:
  // Quick operations
  - Save file to storage
  - Create file record
  
  // Background processing
  ASYNC: process_upload {
    - Generate thumbnails
    - Extract metadata
    - Scan for viruses
    - Optimize file size
    - Update file record
  }
  
  // WeWeb gets immediate response
  Return {
    file_id: file.id,
    status: "processing",
    preview_url: temp_url
  }
```

## Best Practices

### What to Make Async

**Good Candidates:**
- Email sending
- SMS notifications
- Report generation
- File processing
- External API calls
- Data synchronization
- Cleanup operations

**Keep Synchronous:**
- Authentication
- Authorization checks
- Data validation
- Critical business logic
- Payment processing

### Performance Tips

```javascript
// Batch operations
ASYNC: batch_process
  items = Get 100 records
  FOR EACH item IN items {
    // Process item
  }

// Instead of
FOR EACH item IN all_items {
  ASYNC: process_single_item
}
```

### Monitoring

```javascript
// Add logging to async functions
ASYNC: important_operation
  Log: "Starting operation " + operation_id
  
  TRY {
    // Do work
    Log: "Operation successful " + operation_id
  } CATCH (error) {
    Log: "Operation failed " + operation_id + ": " + error
  }
```

## Common Mistakes to Avoid

1. **Making Everything Async**
   - Critical path must be synchronous
   - User needs confirmation of success

2. **No Error Handling**
   - Async errors are silent
   - Always add try/catch

3. **Forgetting Status Tracking**
   - Users can't check progress
   - No way to debug failures

4. **Circular Dependencies**
   - Async calling async infinitely
   - Causes resource exhaustion

## Try This

Build an async image processing pipeline:
1. Accept image upload (sync)
2. Store original (sync)
3. Generate thumbnails (async)
4. Extract metadata (async)
5. Apply AI tagging (async)
6. Return upload confirmation immediately

## Pro Tips

💡 **Queue Pattern:** Use a queue table for reliable async processing

💡 **Idempotency:** Make async functions safe to retry

💡 **Timeouts:** Set appropriate timeouts for long operations

💡 **Webhooks:** Notify completion via webhooks for long tasks

## Performance Impact

- Sync operation: 5 seconds response time
- With async: 500ms response time
- 10x improvement in user experience
- Handle more concurrent requests

Remember: Async functions are about user experience. Move anything that doesn't need immediate feedback to async processing!