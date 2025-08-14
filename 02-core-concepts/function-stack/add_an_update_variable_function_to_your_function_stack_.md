---
title: "Update Variable - Modifying Existing Data"
description: "Learn how to update and modify existing variables dynamically in your Xano function stacks"
category: function-stack
subcategory: data-manipulation
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- variables
- updates
- data-modification
- state-management
- calculations
---

# Update Variable - Modifying Existing Data

## Quick Summary

> **What it is:** A function that modifies the value of an existing variable without creating a new one
> 
> **When to use:** When you need to change variable values during execution - counters, accumulators, status updates, or data transformations
> 
> **Key benefit:** Efficiently manage state changes without creating multiple variables
> 
> **Common uses:** Running totals, loop counters, progressive data building

## What You'll Learn

- Updating different types of variables
- Mathematical operations on variables
- Array and object modifications
- Best practices for state management
- Common patterns for automation

## Basic Update Operations

### Numeric Updates

```javascript
// Increment counter
counter = counter + 1

// Running total
total = total + item.price

// Percentage calculation
progress = (completed / total) * 100

// Compound interest
balance = balance * (1 + interest_rate)
```

### String Updates

```javascript
// Append to string
message = message + "\nNew line added"

// Build CSV row
csv_row = csv_row + "," + new_value

// Status updates
status_text = "Processing: " + current_step
```

### Boolean Toggles

```javascript
// Toggle boolean
is_active = !is_active

// Conditional update
has_errors = (error_count > 0)

// Combined conditions
is_valid = is_valid && current_check_passed
```

## Practical Examples

### Example 1: Shopping Cart Total

```javascript
// Initialize
cart_total = 0
tax_total = 0

// In loop through items
FOR EACH item IN cart_items {
  // Update running totals
  cart_total = cart_total + (item.price * item.quantity)
  tax_total = tax_total + (item.price * item.quantity * 0.08)
}

// Final calculation
final_total = cart_total + tax_total + shipping_cost
```

### Example 2: Progress Tracking

```javascript
// Initialize
processed_count = 0
failed_count = 0
success_count = 0

// Process records
FOR EACH record IN records {
  processed_count = processed_count + 1
  
  IF (process_record_success) {
    success_count = success_count + 1
  } ELSE {
    failed_count = failed_count + 1
  }
  
  // Update progress percentage
  progress = (processed_count / total_records) * 100
}
```

### Example 3: Building Complex Objects

```javascript
// Start with basic user object
user_data = {
  id: user.id,
  email: user.email
}

// Add profile data
user_data.profile = {
  name: profile.full_name,
  avatar: profile.image_url
}

// Add permissions
user_data.permissions = query_permissions_result

// Add calculated fields
user_data.account_age_days = DAYS_BETWEEN(user.created_at, NOW())
```

## Array Operations

### Adding Elements

```javascript
// Initialize array
results = []

// Add elements dynamically
FOR EACH item IN source_data {
  IF (item.matches_criteria) {
    results = ARRAY_PUSH(results, item)
  }
}
```

### Removing Elements

```javascript
// Remove specific item
active_users = ARRAY_REMOVE(active_users, inactive_user_id)

// Filter array
active_users = ARRAY_FILTER(users, status == "active")
```

### Modifying Array Elements

```javascript
// Update specific index
products[index].quantity = products[index].quantity - 1

// Map transformation
prices = ARRAY_MAP(products, price * discount_rate)
```

## Object Updates

### Adding Properties

```javascript
// Add new property
response_object.timestamp = timestamp_now()

// Add nested property
user_object.preferences.theme = "dark"

// Conditional property
IF (has_discount) {
  order.discount_amount = calculated_discount
}
```

### Updating Properties

```javascript
// Simple update
user.last_login = timestamp_now()

// Nested update
user.stats.login_count = user.stats.login_count + 1

// Computed update
product.final_price = product.base_price * (1 - discount_percentage)
```

## Advanced Patterns

### State Machine Updates

```javascript
// Order state progression
SWITCH (order.status) {
  CASE "pending":
    order.status = "processing"
    order.processed_at = timestamp_now()
    
  CASE "processing":
    order.status = "shipped"
    order.shipped_at = timestamp_now()
    
  CASE "shipped":
    order.status = "delivered"
    order.delivered_at = timestamp_now()
}
```

### Accumulator Pattern

```javascript
// Analytics accumulator
stats = {
  total_views: 0,
  unique_users: [],
  peak_hour: null,
  peak_count: 0
}

FOR EACH event IN today_events {
  // Update totals
  stats.total_views = stats.total_views + 1
  
  // Track unique users
  IF (!ARRAY_CONTAINS(stats.unique_users, event.user_id)) {
    stats.unique_users = ARRAY_PUSH(stats.unique_users, event.user_id)
  }
  
  // Track peak
  IF (event.hour_count > stats.peak_count) {
    stats.peak_hour = event.hour
    stats.peak_count = event.hour_count
  }
}
```

### Recursive Updates

```javascript
// Fibonacci sequence
prev = 0
current = 1

FOR i FROM 1 TO n {
  temp = current
  current = current + prev
  prev = temp
}
```

## Integration Patterns

### With n8n Workflows

```javascript
// Build webhook response progressively
webhook_response = {
  received: true,
  timestamp: timestamp_now()
}

// Add processing results
webhook_response.processed_count = processed_items
webhook_response.errors = error_array

// Add next action
IF (has_more_items) {
  webhook_response.continue_token = next_page_token
}
```

### With WeWeb

```javascript
// Update form validation state
form_state = {
  is_valid: true,
  errors: []
}

// Check each field
IF (email_invalid) {
  form_state.is_valid = false
  form_state.errors = ARRAY_PUSH(form_state.errors, "Invalid email")
}

IF (password_weak) {
  form_state.is_valid = false
  form_state.errors = ARRAY_PUSH(form_state.errors, "Password too weak")
}
```

## Common Mistakes to Avoid

1. **Undefined Variable Updates**
   ```javascript
   // Bad: Variable doesn't exist
   total = total + 10  // Error if total undefined
   
   // Good: Initialize first
   total = 0
   total = total + 10
   ```

2. **Type Mismatches**
   ```javascript
   // Bad: Mixing types
   count = "0"
   count = count + 1  // Results in "01"
   
   // Good: Consistent types
   count = 0
   count = count + 1  // Results in 1
   ```

3. **Overwriting Instead of Updating**
   ```javascript
   // Bad: Loses previous data
   user_data = { new_field: value }
   
   // Good: Preserves existing data
   user_data.new_field = value
   ```

## Best Practices

### Initialize Before Updating

```javascript
// Always initialize
total = 0
items = []
status = "pending"

// Then update safely
total = total + amount
items = ARRAY_PUSH(items, new_item)
status = "processing"
```

### Use Descriptive Updates

```javascript
// Clear update intent
retry_count = retry_count + 1
remaining_stock = remaining_stock - quantity_sold
account_balance = account_balance + deposit_amount
```

### Document State Changes

```javascript
// Add comments for complex updates
// Move to next workflow stage
workflow_stage = workflow_stage + 1

// Apply compound interest monthly
balance = balance * (1 + monthly_rate)
```

## Try This

Build a points calculation system:
1. Initialize user points to 0
2. Add points for various actions
3. Apply multipliers for premium users
4. Deduct points for rewards claimed
5. Track point history in array

## Pro Tips

💡 **Atomic Updates:** Make related updates together to maintain consistency

💡 **Guard Conditions:** Check if variable exists before updating

💡 **Immutable Approach:** Sometimes creating new variables is clearer than updating

💡 **Debug Points:** Log variable values before and after updates during development

## Performance Considerations

- Updating is faster than creating new variables
- Use bulk updates for multiple related changes
- Consider memory usage with large objects/arrays
- Profile performance for loops with many updates

Remember: Update Variable is essential for maintaining state throughout your function execution. Use it to build complex logic step by step!