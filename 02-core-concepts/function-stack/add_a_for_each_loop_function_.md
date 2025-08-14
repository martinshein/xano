---
title: "For Each Loop - Processing Lists and Arrays"
description: "Master iterating through arrays and lists to process multiple items efficiently in Xano"
category: function-stack
subcategory: control-flow
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- loops
- iteration
- arrays
- batch-processing
- automation
---

# For Each Loop - Processing Lists and Arrays

## Quick Summary

> **What it is:** A loop function that automatically processes each item in an array or list one by one
> 
> **When to use:** When you need to perform the same operation on multiple items - sending emails to users, updating records, processing order items
> 
> **Key benefit:** Automates repetitive tasks without writing complex code
> 
> **Performance note:** Consider bulk operations for large datasets

## What You'll Learn

- Setting up for-each loops visually
- Accessing current item and index
- Building arrays from loop results
- Nested loops for complex data
- Performance optimization strategies

## Basic Loop Configuration

### Simple Array Processing

```javascript
// Loop through user array
FOR EACH user IN users_array {
  // Current user available as 'item'
  Send email to: item.email
  Update last_contacted: timestamp_now()
}
```

### Loop Variables

Inside each loop, you have access to:
- **item:** The current element being processed
- **index:** The position in the array (starts at 0)
- **parent:** Access to variables outside the loop

## Practical Examples

### Example 1: Send Notifications

```javascript
// Array: pending_notifications
FOR EACH notification IN pending_notifications {
  // Send email
  Send Email:
    to: item.user_email
    subject: item.subject
    body: item.message
  
  // Mark as sent
  Update Record:
    table: notifications
    id: item.id
    sent_at: timestamp_now()
}
```

### Example 2: Calculate Order Total

```javascript
// Initialize total
total = 0

// Loop through cart items
FOR EACH product IN cart_items {
  // Calculate line total
  line_total = item.price * item.quantity
  
  // Add to running total
  total = total + line_total
  
  // Update inventory
  Update Record:
    table: products
    id: item.product_id
    stock: stock - item.quantity
}

// After loop: total contains sum
```

### Example 3: Data Transformation

```javascript
// Create empty result array
formatted_users = []

FOR EACH user IN raw_users {
  // Transform each user
  formatted_user = {
    id: item.id,
    name: item.first_name + " " + item.last_name,
    status: (item.active) ? "Active" : "Inactive",
    joined: FORMAT_DATE(item.created_at)
  }
  
  // Add to result array
  ARRAY_PUSH(formatted_users, formatted_user)
}

// Return transformed array
```

## Advanced Patterns

### Nested Loops

```javascript
// Process orders and their items
FOR EACH order IN orders {
  order_total = 0
  
  // Nested loop for order items
  FOR EACH item IN order.items {
    item_total = item.price * item.quantity
    order_total = order_total + item_total
  }
  
  // Update order with calculated total
  Update Record:
    table: orders
    id: order.id
    total: order_total
}
```

### Conditional Processing

```javascript
FOR EACH user IN users {
  // Skip inactive users
  IF (item.status != "active") {
    CONTINUE  // Skip to next iteration
  }
  
  // Process only active users
  Send newsletter to: item.email
}
```

### Early Exit

```javascript
found = false

FOR EACH record IN search_results {
  IF (item.matches_criteria) {
    found = true
    matching_record = item
    BREAK  // Exit loop early
  }
}
```

## Loop Control

### Continue Statement
Skip current iteration and move to next:
```javascript
FOR EACH item IN items {
  IF (item.skip == true) {
    CONTINUE
  }
  // Process item
}
```

### Break Statement
Exit the loop completely:
```javascript
FOR EACH item IN items {
  IF (limit_reached) {
    BREAK
  }
  // Process item
}
```

## Building Results

### Collecting Processed Data

```javascript
// Initialize results array
results = []

FOR EACH record IN input_data {
  // Process each record
  processed = {
    original_id: item.id,
    processed_at: timestamp_now(),
    result: PROCESS_FUNCTION(item)
  }
  
  // Collect results
  ARRAY_PUSH(results, processed)
}

// Return all results
Return results
```

### Filtering While Looping

```javascript
// Collect only matching items
active_users = []

FOR EACH user IN all_users {
  IF (item.status == "active" AND item.verified) {
    ARRAY_PUSH(active_users, item)
  }
}
```

## Integration Patterns

### With n8n

```javascript
// Process webhook batch data
FOR EACH webhook_event IN input.events {
  // Process each event
  SWITCH (item.type) {
    CASE "user.created":
      Create user record
    CASE "user.updated":
      Update user record
    CASE "user.deleted":
      Soft delete user
  }
  
  // Log processing
  Create audit log entry
}
```

### With WeWeb

```javascript
// Prepare collection data
formatted_products = []

FOR EACH product IN raw_products {
  // Format for WeWeb display
  display_product = {
    id: item.id,
    title: item.name,
    price: "$" + item.price,
    image: item.image_url || "/placeholder.jpg",
    in_stock: item.quantity > 0
  }
  
  ARRAY_PUSH(formatted_products, display_product)
}

Return formatted_products
```

## Performance Optimization

### Use Bulk Operations When Possible

```javascript
// Instead of loop with individual updates
FOR EACH id IN ids_to_update {
  Update Record where id = item
}

// Use bulk update
Bulk Update Records:
  ids: ids_to_update
  data: update_data
```

### Limit Loop Size

```javascript
// Process in chunks
chunk_size = 100
total_processed = 0

FOR EACH item IN large_array {
  // Process item
  total_processed++
  
  IF (total_processed >= chunk_size) {
    BREAK  // Process rest in background task
  }
}
```

### Aggregate First

```javascript
// Instead of multiple queries in loop
FOR EACH user IN users {
  count = Query count where user_id = item.id
}

// Get all counts in one query
counts = Query aggregate counts by user_id
```

## Common Mistakes to Avoid

1. **Modifying Array During Loop**
   ```javascript
   // Bad: Modifying array being looped
   FOR EACH item IN array {
     ARRAY_REMOVE(array, item)  // Causes issues
   }
   
   // Good: Build new array
   filtered = []
   FOR EACH item IN array {
     IF (keep_item) {
       ARRAY_PUSH(filtered, item)
     }
   }
   ```

2. **Database Queries in Loops**
   ```javascript
   // Bad: N+1 query problem
   FOR EACH user IN users {
     profile = Get Record from profiles where user_id = item.id
   }
   
   // Good: Get all profiles first
   profiles = Query all profiles where user_id IN user_ids
   ```

3. **Not Handling Empty Arrays**
   ```javascript
   // Check before looping
   IF (array == null OR array.length == 0) {
     Return "No items to process"
   }
   
   FOR EACH item IN array {
     // Process items
   }
   ```

## Try This

Build a batch email processor:
1. Query users needing notifications
2. Loop through users
3. Check notification preferences
4. Send appropriate email type
5. Update last_notified timestamp
6. Return summary of sent emails

## Pro Tips

💡 **Index Access:** Use the index variable for numbering or position-based logic

💡 **Parent Scope:** Access variables from outside the loop using parent reference

💡 **Result Arrays:** Always initialize result arrays before the loop

💡 **Performance:** For large datasets (>1000 items), consider background tasks

Remember: For Each loops are powerful but use them wisely. For large-scale operations, consider bulk functions or background processing!