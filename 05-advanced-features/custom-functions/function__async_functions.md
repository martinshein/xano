---
title: Async Functions Function Reference
description: Reference guide for implementing asynchronous custom function execution in Xano function stacks, including execution modes and await patterns
category: custom-functions
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - async-functions.md
  - custom-functions.md
  - building-with-visual-development.md
subcategory: 05-advanced-features/custom-functions
tags:
  - async-functions
  - function-reference
  - execution-modes
  - await-patterns
  - no-code
---

## 📋 **Quick Summary**

The Async Functions function allows you to execute custom functions asynchronously in your function stacks. When a custom function is set to async mode, it returns an execution ID instead of blocking the main function stack. Use the Async Function Await function to retrieve results when needed.

## What You'll Learn

- How to enable async execution mode for custom functions
- Working with execution IDs and await patterns
- When to use async vs synchronous execution
- Best practices for async function implementation

# Async Functions Function Reference

## Overview

The **Async Functions** execution mode enables custom functions to run in the background without blocking the main function stack. This is particularly useful for time-consuming operations like file processing, external API calls, or complex calculations.

### Key Concepts

**Async Execution:**
- Returns immediately with execution ID
- Function runs in background
- Main stack continues without waiting
- Results retrieved separately using await

**Synchronous Execution:**
- Blocks until function completes
- Returns function results directly
- Main stack waits for completion
- Simpler but can cause delays

## 🚀 **Basic Implementation**

### Enabling Async Mode

**Step 1: Add Custom Function to Stack**
```javascript
{
  "function": "custom_function",
  "name": "process_large_dataset",
  "inputs": {
    "dataset": "{{ user_data }}",
    "processing_options": {
      "batch_size": 1000,
      "validate": true
    }
  },
  "execution_mode": "async",  // Enable async execution
  "return_as": "processing_execution_id"
}
```

**Step 2: Continue Main Stack**
```javascript
{
  "function": "return_response",
  "status": 202,
  "body": {
    "message": "Processing started",
    "execution_id": "{{ processing_execution_id }}",
    "status_url": "/api/status/{{ processing_execution_id }}"
  }
}
```

### Retrieving Async Results

**Using Async Function Await:**
```javascript
[
  {
    "function": "async_function_await",
    "execution_ids": ["{{ request.body.execution_id }}"],
    "return_as": "async_results"
  },
  {
    "function": "conditional",
    "condition": "{{ async_results[0].status == 'completed' }}",
    "true_branch": [
      {
        "function": "return_response",
        "body": {
          "status": "completed",
          "result": "{{ async_results[0].output }}"
        }
      }
    ],
    "false_branch": [
      {
        "function": "return_response",
        "body": {
          "status": "{{ async_results[0].status }}",
          "message": "Processing still in progress"
        }
      }
    ]
  }
]
```

## 🛠️ **Common Patterns**

### Fire-and-Forget Pattern

**For operations that don't need result retrieval:**
```javascript
{
  "function": "custom_function",
  "name": "send_notification_email",
  "inputs": {
    "user_id": "{{ auth.user.id }}",
    "notification_type": "welcome",
    "template_data": "{{ user_profile }}"
  },
  "execution_mode": "async"
  // No return_as needed for fire-and-forget
}
```

### Batch Processing Pattern

**For multiple async operations:**
```javascript
[
  {
    "function": "create_variable",
    "name": "execution_ids",
    "value": []
  },
  {
    "function": "loop",
    "array": "{{ data_batches }}",
    "operations": [
      {
        "function": "custom_function",
        "name": "process_batch",
        "inputs": {
          "batch_data": "{{ item }}",
          "batch_number": "{{ loop.index }}"
        },
        "execution_mode": "async",
        "return_as": "batch_execution_id"
      },
      {
        "function": "update_variable",
        "name": "execution_ids",
        "operation": "append",
        "value": "{{ batch_execution_id }}"
      }
    ]
  },
  {
    "function": "return_response",
    "body": {
      "message": "Batch processing started",
      "execution_ids": "{{ execution_ids }}",
      "total_batches": "{{ execution_ids|length }}"
    }
  }
]
```

### Status Monitoring Pattern

**For checking multiple async operations:**
```javascript
[
  {
    "function": "async_function_await",
    "execution_ids": "{{ request.body.execution_ids }}",
    "return_as": "all_results"
  },
  {
    "function": "create_variable",
    "name": "status_summary",
    "value": {
      "total": "{{ all_results|length }}",
      "completed": "{{ all_results|select('status', 'completed')|length }}",
      "running": "{{ all_results|select('status', 'running')|length }}",
      "failed": "{{ all_results|select('status', 'error')|length }}"
    }
  },
  {
    "function": "return_response",
    "body": {
      "summary": "{{ status_summary }}",
      "details": "{{ all_results }}",
      "all_complete": "{{ status_summary.completed == status_summary.total }}"
    }
  }
]
```

## ⚡ **Performance Considerations**

### When to Use Async

**Recommended for:**
- File processing operations
- External API calls with slow responses
- Complex data transformations
- Email/SMS sending
- Report generation
- Image/video processing

**Not recommended for:**
- Simple calculations
- Quick database queries
- Operations needed for immediate response
- Functions with dependencies on return values

### Resource Management

**Monitoring Async Functions:**
```javascript
// Check execution status
{
  "function": "async_function_await",
  "execution_ids": ["{{ execution_id }}"],
  "timeout": 30,  // Wait up to 30 seconds
  "return_as": "status_check"
}
```

## 💡 **Best Practices**

- **Use Meaningful Return Variables**: Name execution IDs clearly for tracking
- **Implement Timeout Handling**: Set appropriate timeouts for await operations
- **Provide Status Endpoints**: Create APIs for checking async operation status
- **Log Execution IDs**: Store IDs for later retrieval and debugging
- **Handle Errors Gracefully**: Check for error status in await results

## 🔧 **Common Issues**

**Problem**: Async function execution ID not returned  
**Solution**: Ensure `return_as` is specified when using async mode

**Problem**: Await function timing out  
**Solution**: Increase timeout value or check if async function is still running

**Problem**: Cannot retrieve async results  
**Solution**: Verify execution ID is correct and function completed successfully

---

**Next Steps**: For comprehensive async function implementation, see [Async Functions](async-functions.md). For general custom function creation, check [Custom Functions](custom-functions.md).