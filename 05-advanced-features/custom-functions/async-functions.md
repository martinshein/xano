---
title: Async Functions - Non-Blocking Custom Function Execution
description: Complete guide to implementing asynchronous custom functions in Xano, including async/await patterns, background processing, performance optimization, and integration with no-code platforms
category: custom-functions
difficulty: advanced
last_updated: '2025-01-16'
related_docs:
  - custom-functions.md
  - background-tasks.md
  - function-stack-performance.md
subcategory: 05-advanced-features/custom-functions
tags:
  - async-functions
  - background-processing
  - performance
  - custom-functions
  - concurrency
  - no-code
---

## 📋 **Quick Summary**

Async functions allow custom functions to execute in the background without blocking the main function stack execution. This enables better performance, improved user experience, and efficient handling of long-running operations. Perfect for file processing, email sending, data synchronization, and other time-consuming tasks in n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- How to configure and use async custom functions
- Async/await patterns and execution tracking
- Best practices for background processing
- Performance optimization with asynchronous execution
- Integration patterns for no-code platforms
- Error handling and monitoring for async operations

# Async Functions

## Overview

**Async Functions** enable custom functions to execute asynchronously, allowing the main function stack to continue processing without waiting for the async operation to complete. This is similar to background tasks but provides more control and integration within your function stacks.

### Synchronous vs Asynchronous Execution

**Synchronous Execution:**
- Function stack waits for each function to complete
- Sequential execution blocks subsequent operations
- Simple but can cause performance bottlenecks
- User experiences delays during long operations

**Asynchronous Execution:**
- Function executes in background
- Main stack continues immediately
- Non-blocking operation improves performance
- Returns execution ID for later retrieval

## 🚀 **When to Use Async Functions**

### Ideal Use Cases

**Data Processing:**
- Large file uploads and processing
- Batch data transformations
- Complex calculations and analytics
- External API integrations with slow responses

**Communication:**
- Email sending and delivery
- SMS notifications
- Push notifications
- Webhook dispatching

**Background Operations:**
- Report generation
- Data synchronization
- Backup operations
- Cache warming

**Long-Running Tasks:**
- Image/video processing
- PDF generation
- Data export operations
- Third-party service integrations

### Performance Benefits

```javascript
// Performance comparison example
{
  "synchronous_execution": {
    "total_time": "15 seconds",
    "user_wait_time": "15 seconds",
    "operations": [
      {"task": "send_email", "time": "5s"},
      {"task": "generate_report", "time": "8s"},
      {"task": "update_cache", "time": "2s"}
    ]
  },
  "asynchronous_execution": {
    "total_time": "2 seconds",
    "user_wait_time": "2 seconds",
    "background_time": "15 seconds",
    "operations": [
      {"task": "send_email", "time": "5s", "async": true},
      {"task": "generate_report", "time": "8s", "async": true},
      {"task": "update_cache", "time": "2s", "sync": true}
    ]
  }
}
```

## 🔗 **No-Code Platform Integration**

### n8n Async Workflow Patterns

**Fire-and-Forget Pattern:**

```javascript
// n8n workflow with async Xano functions
{
  "nodes": [
    {
      "name": "Trigger Async Processing",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/process-data",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $json.auth_token }}",
          "Content-Type": "application/json"
        },
        "body": {
          "data": "{{ $json.user_data }}",
          "process_type": "async",
          "callback_url": "{{ $json.webhook_url }}"
        }
      }
    },
    {
      "name": "Continue Workflow",
      "type": "Set",
      "parameters": {
        "values": {
          "processing_started": true,
          "execution_id": "{{ $json.async_execution_id }}",
          "timestamp": "{{ new Date().toISOString() }}"
        }
      }
    },
    {
      "name": "Send Immediate Response",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $json.user_callback_url }}",
        "method": "POST",
        "body": {
          "status": "processing",
          "execution_id": "{{ $json.async_execution_id }}",
          "estimated_completion": "5 minutes"
        }
      }
    }
  ]
}
```

**Poll-and-Wait Pattern:**

```javascript
// n8n workflow that polls for async completion
{
  "nodes": [
    {
      "name": "Start Async Function",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/generate-report",
        "method": "POST",
        "body": {
          "user_id": "{{ $json.user_id }}",
          "report_type": "monthly",
          "async": true
        }
      }
    },
    {
      "name": "Wait Before Check",
      "type": "Wait",
      "parameters": {
        "amount": 30,
        "unit": "seconds"
      }
    },
    {
      "name": "Check Async Status",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/async-status",
        "method": "POST",
        "body": {
          "execution_ids": ["{{ $json.async_execution_id }}"]
        }
      }
    },
    {
      "name": "Is Complete?",
      "type": "If",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{ $json.status }}",
              "operation": "equal",
              "value2": "completed"
            }
          ]
        }
      }
    },
    {
      "name": "Process Results",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const result = $input.first().json;
          if (result.status === 'completed') {
            return [{ json: result.output }];
          } else if (result.status === 'error') {
            throw new Error(result.error_message);
          } else {
            // Still processing, loop back
            return [];
          }
        `
      }
    }
  ]
}
```

### WeWeb Async Function Management

**Async Operation Component:**

```javascript
// WeWeb component for managing async operations
class XanoAsyncManager {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.pollInterval = null;
    this.activeOperations = new Map();
  }
  
  async startAsyncOperation(endpoint, data, options = {}) {
    try {
      const response = await fetch(`${this.baseUrl}/api/${endpoint}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          ...data,
          async: true
        })
      });
      
      const result = await response.json();
      
      if (response.ok && result.async_execution_id) {
        const operation = {
          id: result.async_execution_id,
          endpoint: endpoint,
          startTime: new Date(),
          status: 'running',
          options: options
        };
        
        this.activeOperations.set(result.async_execution_id, operation);
        
        // Update UI state
        wwLib.wwVariable.updateValue('async_operations', Array.from(this.activeOperations.values()));
        
        // Start polling if callback provided
        if (options.onComplete || options.onError) {
          this.startPolling(result.async_execution_id, options);
        }
        
        return result.async_execution_id;
      } else {
        throw new Error(result.message || 'Failed to start async operation');
      }
    } catch (error) {
      console.error('Async operation failed to start:', error);
      throw error;
    }
  }
  
  async checkAsyncStatus(executionIds) {
    try {
      const response = await fetch(`${this.baseUrl}/api/async-await`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          execution_ids: Array.isArray(executionIds) ? executionIds : [executionIds]
        })
      });
      
      const results = await response.json();
      
      // Update operation states
      results.forEach(result => {
        if (this.activeOperations.has(result.execution_id)) {
          const operation = this.activeOperations.get(result.execution_id);
          operation.status = result.status;
          operation.output = result.output;
          operation.error = result.error;
          operation.completedAt = result.status !== 'running' ? new Date() : null;
        }
      });
      
      // Update UI
      wwLib.wwVariable.updateValue('async_operations', Array.from(this.activeOperations.values()));
      
      return results;
    } catch (error) {
      console.error('Failed to check async status:', error);
      throw error;
    }
  }
  
  startPolling(executionId, options = {}) {
    const pollInterval = options.pollInterval || 5000; // 5 seconds default
    
    const poll = async () => {
      try {
        const [result] = await this.checkAsyncStatus([executionId]);
        
        if (result.status === 'completed') {
          this.stopPolling(executionId);
          if (options.onComplete) {
            options.onComplete(result.output);
          }
        } else if (result.status === 'error') {
          this.stopPolling(executionId);
          if (options.onError) {
            options.onError(result.error);
          }
        } else {
          // Still running, continue polling
          setTimeout(poll, pollInterval);
        }
      } catch (error) {
        this.stopPolling(executionId);
        if (options.onError) {
          options.onError(error.message);
        }
      }
    };
    
    setTimeout(poll, pollInterval);
  }
  
  stopPolling(executionId) {
    const operation = this.activeOperations.get(executionId);
    if (operation && operation.pollTimeout) {
      clearTimeout(operation.pollTimeout);
    }
  }
  
  async cancelAsyncOperation(executionId) {
    try {
      const response = await fetch(`${this.baseUrl}/api/async-cancel`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          execution_id: executionId
        })
      });
      
      if (response.ok) {
        this.activeOperations.delete(executionId);
        wwLib.wwVariable.updateValue('async_operations', Array.from(this.activeOperations.values()));
        return true;
      }
      
      return false;
    } catch (error) {
      console.error('Failed to cancel async operation:', error);
      return false;
    }
  }
  
  getOperationStatus(executionId) {
    return this.activeOperations.get(executionId);
  }
  
  getAllOperations() {
    return Array.from(this.activeOperations.values());
  }
}

// Initialize async manager
const asyncManager = new XanoAsyncManager(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage examples
async function startReportGeneration() {
  try {
    const executionId = await asyncManager.startAsyncOperation(
      'generate-report',
      {
        user_id: wwLib.wwVariable.getValue('current_user_id'),
        report_type: 'monthly'
      },
      {
        onComplete: (result) => {
          wwLib.wwVariable.updateValue('generated_report', result);
          wwLib.wwUtils.showSuccessToast('Report generated successfully!');
          wwLib.wwModal.open('report-preview-modal');
        },
        onError: (error) => {
          wwLib.wwUtils.showErrorToast(`Report generation failed: ${error}`);
        },
        pollInterval: 3000
      }
    );
    
    wwLib.wwUtils.showInfoToast('Report generation started...');
    wwLib.wwVariable.updateValue('current_report_execution_id', executionId);
  } catch (error) {
    wwLib.wwUtils.showErrorToast(`Failed to start report generation: ${error.message}`);
  }
}

async function checkAllOperations() {
  const operations = asyncManager.getAllOperations();
  const runningIds = operations
    .filter(op => op.status === 'running')
    .map(op => op.id);
  
  if (runningIds.length > 0) {
    await asyncManager.checkAsyncStatus(runningIds);
  }
}
```

## 🛠️ **Implementation Patterns**

### Basic Async Function Configuration

**Custom Function with Async Execution:**

```javascript
// Async email sending function
[
  {
    "function": "create_variable",
    "name": "email_data",
    "value": {
      "to": "{{ input.recipient_email }}",
      "subject": "{{ input.subject }}",
      "template": "{{ input.template_name }}",
      "variables": "{{ input.template_variables }}"
    }
  },
  {
    "function": "external_api_request",
    "url": "{{ env.EMAIL_SERVICE_URL }}",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.EMAIL_API_KEY }}",
      "Content-Type": "application/json"
    },
    "body": "{{ email_data }}",
    "return_as": "email_result"
  },
  {
    "function": "add_record",
    "table": "email_logs",
    "data": {
      "recipient": "{{ email_data.to }}",
      "subject": "{{ email_data.subject }}",
      "status": "{{ email_result.status }}",
      "external_id": "{{ email_result.id }}",
      "sent_at": "{{ now }}"
    }
  },
  {
    "function": "return_response",
    "body": {
      "success": true,
      "email_id": "{{ email_result.id }}",
      "message": "Email sent successfully"
    }
  }
]
```

### Async Function Execution in API Endpoint

**API Endpoint with Async Custom Function:**

```javascript
// Main API endpoint function stack
[
  {
    "function": "add_record",
    "table": "orders",
    "data": {
      "customer_id": "{{ request.body.customer_id }}",
      "total": "{{ request.body.total }}",
      "status": "confirmed"
    },
    "return_as": "new_order"
  },
  {
    "function": "custom_function",
    "name": "send_order_confirmation_email",
    "inputs": {
      "order_id": "{{ new_order.id }}",
      "customer_email": "{{ new_order.customer.email }}"
    },
    "execution_mode": "async",
    "return_as": "email_execution_id"
  },
  {
    "function": "custom_function",
    "name": "update_inventory",
    "inputs": {
      "order_items": "{{ request.body.items }}"
    },
    "execution_mode": "async",
    "return_as": "inventory_execution_id"
  },
  {
    "function": "return_response",
    "status": 201,
    "body": {
      "order": "{{ new_order }}",
      "background_tasks": {
        "email_execution_id": "{{ email_execution_id }}",
        "inventory_execution_id": "{{ inventory_execution_id }}"
      },
      "message": "Order created successfully. Confirmation email and inventory update in progress."
    }
  }
]
```

### Async Function Await Pattern

**Retrieving Async Function Results:**

```javascript
// Function stack to check async function completion
[
  {
    "function": "async_function_await",
    "execution_ids": [
      "{{ request.body.email_execution_id }}",
      "{{ request.body.inventory_execution_id }}"
    ],
    "return_as": "async_results"
  },
  {
    "function": "create_variable",
    "name": "completion_status",
    "value": {
      "email": "{{ async_results|where('execution_id', request.body.email_execution_id)|first }}",
      "inventory": "{{ async_results|where('execution_id', request.body.inventory_execution_id)|first }}"
    }
  },
  {
    "function": "conditional",
    "condition": "{{ completion_status.email.status == 'completed' && completion_status.inventory.status == 'completed' }}",
    "true_branch": [
      {
        "function": "return_response",
        "body": {
          "all_completed": true,
          "email_result": "{{ completion_status.email.output }}",
          "inventory_result": "{{ completion_status.inventory.output }}"
        }
      }
    ],
    "false_branch": [
      {
        "function": "return_response",
        "body": {
          "all_completed": false,
          "status": "{{ completion_status }}",
          "message": "Some operations still in progress"
        }
      }
    ]
  }
]
```

## ⚡ **Performance Optimization**

### Async Function Best Practices

**Execution Patterns:**

```javascript
// Optimized async execution patterns
{
  "parallel_execution": {
    "description": "Execute multiple async functions simultaneously",
    "pattern": [
      {
        "function": "custom_function",
        "name": "process_images",
        "execution_mode": "async",
        "return_as": "image_processing_id"
      },
      {
        "function": "custom_function", 
        "name": "generate_thumbnails",
        "execution_mode": "async",
        "return_as": "thumbnail_id"
      },
      {
        "function": "custom_function",
        "name": "extract_metadata",
        "execution_mode": "async", 
        "return_as": "metadata_id"
      }
    ]
  },
  "sequential_with_dependencies": {
    "description": "Execute async functions with dependencies",
    "pattern": [
      {
        "function": "custom_function",
        "name": "validate_data",
        "execution_mode": "sync",
        "return_as": "validation_result"
      },
      {
        "function": "conditional",
        "condition": "{{ validation_result.valid }}",
        "true_branch": [
          {
            "function": "custom_function",
            "name": "process_data",
            "execution_mode": "async",
            "return_as": "processing_id"
          }
        ]
      }
    ]
  }
}
```

### Resource Management

**Memory and CPU Optimization:**

```javascript
// Async function with resource limits
{
  "async_function_config": {
    "execution_mode": "async",
    "resource_limits": {
      "max_execution_time": 300, // 5 minutes
      "memory_limit": "512MB",
      "cpu_limit": "1 core"
    },
    "retry_policy": {
      "max_retries": 3,
      "backoff_strategy": "exponential",
      "initial_delay": 1000
    },
    "timeout_handling": {
      "on_timeout": "cancel",
      "cleanup_resources": true,
      "notify_callback": true
    }
  }
}
```

## 🔐 **Error Handling and Monitoring**

### Comprehensive Error Handling

**Async Function Error Management:**

```javascript
// Error handling for async functions
[
  {
    "function": "try_catch",
    "try_block": [
      {
        "function": "custom_function",
        "name": "risky_operation",
        "execution_mode": "async",
        "return_as": "operation_id"
      }
    ],
    "catch_block": [
      {
        "function": "add_record",
        "table": "error_logs",
        "data": {
          "function_name": "risky_operation",
          "error_message": "{{ error.message }}",
          "stack_trace": "{{ error.stack }}",
          "timestamp": "{{ now }}"
        }
      },
      {
        "function": "return_response",
        "status": 500,
        "body": {
          "error": "Operation failed to start",
          "execution_id": null
        }
      }
    ]
  }
]
```

### Monitoring and Alerting

**Async Operation Monitoring:**

```javascript
// Monitoring function stack for async operations
[
  {
    "function": "query_all_records",
    "table": "async_executions",
    "filter": {
      "status": "running",
      "created_at": {"$lt": "{{ now - 300 }}"}  // 5 minutes ago
    },
    "return_as": "stuck_operations"
  },
  {
    "function": "conditional",
    "condition": "{{ stuck_operations|length > 0 }}",
    "true_branch": [
      {
        "function": "loop",
        "array": "{{ stuck_operations }}",
        "operations": [
          {
            "function": "add_record",
            "table": "alerts",
            "data": {
              "type": "async_timeout",
              "execution_id": "{{ item.execution_id }}",
              "function_name": "{{ item.function_name }}",
              "stuck_duration": "{{ now - item.created_at }}",
              "severity": "warning"
            }
          }
        ]
      }
    ]
  }
]
```

## 💡 **Pro Tips**

- **Use Async for I/O Operations**: File uploads, external API calls, and email sending benefit most from async execution
- **Monitor Execution Times**: Track async function performance to optimize resource allocation
- **Implement Timeouts**: Always set reasonable timeout limits for async operations
- **Provide User Feedback**: Show progress indicators and status updates for long-running operations
- **Handle Failures Gracefully**: Implement retry logic and fallback mechanisms
- **Clean Up Resources**: Ensure async functions properly clean up temporary files and connections

## 🔧 **Troubleshooting**

### Common Async Function Issues

**Problem**: Async function appears to hang indefinitely  
**Solution**: Check function logs for errors, implement timeout handling, and verify resource limits

**Problem**: Cannot retrieve async function results  
**Solution**: Verify execution ID is correct and function completed successfully before calling await

**Problem**: Async functions consuming too many resources  
**Solution**: Implement resource limits, throttling, and queue management for concurrent operations

**Problem**: Lost execution IDs preventing result retrieval  
**Solution**: Store execution IDs in database with proper indexing and cleanup policies

---

**Next Steps**: Ready to implement async functions? Check out [Custom Functions](custom-functions.md) for function creation basics or explore [Background Tasks](background-tasks.md) for scheduled operations