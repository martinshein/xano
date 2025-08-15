---
title: "Update Variable Function"
description: "Master variable updating in Xano function stacks for dynamic data manipulation and state management"
category: function-stack
difficulty: beginner
tags:
  - variables
  - state-management
  - data-manipulation
  - expressions
  - logic
  - workflow
related_docs:
  - create-variable
  - expressions
  - conditional
  - loops
last_updated: '2025-01-23'
---

# Update Variable Function

## Quick Summary
The Update Variable function modifies existing variables within your function stack, enabling dynamic data manipulation, calculations, and state changes during workflow execution.

## What You'll Learn
- Variable update fundamentals
- Different update operations
- Conditional variable updates
- Complex variable manipulations
- Performance optimization techniques
- Common update patterns

## Variable Update Operations

### Basic Updates

**Direct Assignment**: Replace variable value completely
```javascript
// Simple value update
variable: "user_count"
new_value: 150
operation: "assign"
result: user_count = 150
```

**Mathematical Operations**: Perform calculations
```javascript
// Increment counter
variable: "page_views"
operation: "add"
value: 1
result: page_views = page_views + 1
```

**String Operations**: Modify text variables
```javascript
// Append to string
variable: "log_message"
operation: "append"
value: " - completed successfully"
result: log_message = "User login - completed successfully"
```

### Advanced Update Operations

**Object Property Updates**: Modify object properties
```javascript
// Update object property
variable: "user_profile"
property: "last_login"
new_value: "{{now}}"
result: user_profile.last_login = "2025-01-23T15:30:00Z"
```

**Array Operations**: Modify array contents
```javascript
// Add item to array
variable: "selected_items"
operation: "push"
value: {"id": 123, "name": "New Item"}
result: selected_items.push(new_item)
```

**Conditional Updates**: Update based on conditions
```javascript
// Conditional update
variable: "status"
condition: "score >= 80"
true_value: "passed"
false_value: "failed"
result: status = (score >= 80) ? "passed" : "failed"
```

## Integration Patterns

### For n8n Users
Variable management in workflows:

```javascript
// n8n variable update pattern
{
  "update_variables": {
    "processing_count": "{{$node['Previous'].json['count'] + 1}}",
    "last_processed": "{{$now}}",
    "status": "{{$node['Previous'].json['success'] ? 'completed' : 'failed'}}",
    "results": "{{$node['Previous'].json['results'].concat($node['Current'].json['new_results'])}}"
  }
}
```

### For WeWeb Users
Dynamic UI state management:

```javascript
// WeWeb variable binding
{
  "form_data": {
    "step": "{{current_step + 1}}",
    "completion": "{{(current_step / total_steps) * 100}}%",
    "valid": "{{validate_current_step()}}",
    "next_enabled": "{{current_step < total_steps && form_valid}}"
  }
}
```

### API State Management

```json
{
  "request_context": {
    "attempt_count": 1,
    "last_error": null,
    "retry_after": null,
    "processing_time": 0,
    "cache_hit": false
  },
  "response_data": {
    "items_processed": 0,
    "total_items": 100,
    "success_count": 0,
    "error_count": 0
  }
}
```

## Common Use Cases

### Counter and Metrics

```javascript
// API usage tracking
variables: {
  "request_count": "increment",
  "total_processing_time": "add_duration",
  "error_rate": "calculate_percentage",
  "last_request_time": "set_timestamp"
}
```

### State Machine Management

```javascript
// Order processing states
state_transitions: {
  "pending": ["processing", "cancelled"],
  "processing": ["completed", "failed"],
  "completed": ["refunded"],
  "failed": ["retry", "cancelled"]
}

current_state: "pending"
action: "start_processing"
new_state: "processing"
```

### Data Accumulation

```javascript
// Report data collection
accumulator: {
  "total_revenue": "sum",
  "order_count": "count",
  "average_order_value": "calculate_average",
  "top_products": "merge_arrays",
  "customer_segments": "group_by_criteria"
}
```

### Progress Tracking

```javascript
// Multi-step process tracking
progress: {
  "current_step": 3,
  "total_steps": 10,
  "completion_percentage": 30,
  "estimated_time_remaining": "7 minutes",
  "steps_completed": ["validate", "process", "verify"]
}
```

## Try This
1. **Basic Updates**: Practice simple variable assignments and calculations
2. **Object Manipulation**: Update properties within complex objects
3. **Array Operations**: Add, remove, and modify array elements
4. **Conditional Logic**: Implement conditional variable updates
5. **State Management**: Build a simple state machine with variables

## Common Mistakes to Avoid

❌ **Don't:**
- Update variables unnecessarily in loops
- Forget to handle null/undefined values
- Create overly complex update chains
- Ignore variable type consistency
- Update variables without proper validation

✅ **Do:**
- Validate data before updating variables
- Use appropriate data types consistently
- Keep update logic simple and readable
- Handle edge cases and error conditions
- Document complex variable update logic

## Pro Tips

💡 **Efficiency:**
- Batch multiple variable updates together
- Use efficient operations for large datasets
- Cache frequently updated variables
- Avoid unnecessary variable copies

🚀 **Performance:**
- Update variables only when values change
- Use appropriate data structures for your use case
- Minimize object property updates in loops
- Consider memory usage for large variables

⚡ **Best Practices:**
- Use descriptive variable names
- Initialize variables with proper default values
- Validate variable updates for business rules
- Track variable changes for debugging

## Advanced Update Patterns

### Atomic Updates

```javascript
// Ensure atomic variable updates
update_transaction: {
  "variables": ["inventory_count", "reserved_count"],
  "operation": "atomic",
  "rollback_on_error": true
}
```

### Calculated Updates

```javascript
// Complex calculations
calculated_update: {
  "variable": "order_total",
  "calculation": {
    "subtotal": "sum(items.price * items.quantity)",
    "tax": "subtotal * tax_rate",
    "shipping": "calculate_shipping(items, address)",
    "total": "subtotal + tax + shipping"
  }
}
```

### Conditional Bulk Updates

```javascript
// Update multiple variables based on conditions
bulk_update: {
  "condition": "payment_status === 'completed'",
  "updates": {
    "order_status": "fulfilled",
    "payment_date": "now()",
    "notification_sent": true,
    "inventory_reserved": false
  }
}
```

Variable updates provide the foundation for dynamic, responsive function stacks that adapt to changing data and business requirements throughout execution.