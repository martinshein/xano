---
title: "Loops - Iterate Through Data Collections"
description: "Use loops to process arrays, repeat operations, and handle bulk data"
category: function-stack
subcategory: data-manipulation
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- loops
- iteration
- foreach
- while
- arrays
---

# Loops - Iterate Through Data Collections



## Quick Summary

> **What it is:** Functions that repeat operations over data collections or a specific number of times
> 
> **When to use:** Processing arrays, bulk operations, data transformation, or repeated tasks
> 
> **Key benefit:** Efficient processing of multiple items without writing repetitive code
> 
> **Perfect for:** Non-developers building bulk email systems, data processing, or batch operations

## What You'll Learn

- For Each loop for arrays
- For loop for counting
- While loop for conditions
- Loop control (break/continue)
- Performance optimization
- Real-world examples

## For Each Loop - Process Arrays

### Step 1: Add For Each Function
1. Click + in function stack
2. Select "Data Manipulation"
3. Choose "Loops" → "For Each"

### Step 2: Configure Loop
```javascript
For Each item in $var.user_list {
  // Process each user
  Send_Email {
    to: item.email,
    subject: "Welcome " ~ item.name
  }
}
```

## Integration Examples

### With n8n - Batch Processing
```javascript
// n8n sends array of orders to process
orders = Input.orders

// Process each order
For Each order in orders {
  // Validate order
  If (order.total > 0 && order.status == "pending") {
    // Update inventory
    For Each item in order.items {
      current_stock = Get_Record {
        table: "products",
        field_name: "id",
        field_value: item.product_id
      }
      
      new_stock = current_stock.quantity - item.quantity
      
      Edit_Record {
        id: item.product_id,
        quantity: new_stock
      }
    }
    
    // Update order status
    Edit_Record {
      id: order.id,
      status: "processed",
      processed_at: timestamp()
    }
    
    // Send confirmation
    External_API_Request {
      url: env.EMAIL_SERVICE + "/send",
      method: "POST",
      params: {
        to: order.customer_email,
        template: "order_confirmed",
        data: order
      }
    }
  }
}

return {
  success: true,
  processed_count: orders | length,
  message: "All orders processed successfully"
}
```

### With WeWeb - User Management
```javascript
// WeWeb sends list of users to activate
user_ids = Input.user_ids

results = []

For Each user_id in user_ids {
  // Get user details
  user = Get_Record {
    table: "users",
    field_name: "id", 
    field_value: user_id
  }
  
  If (user) {
    // Activate user
    Edit_Record {
      id: user_id,
      status: "active",
      activated_at: timestamp()
    }
    
    // Send welcome email
    welcome_result = External_API_Request {
      url: env.EMAIL_API + "/welcome",
      method: "POST",
      params: {
        email: user.email,
        name: user.name,
        login_url: env.APP_URL + "/login"
      }
    }
    
    // Track result
    results.push({
      user_id: user_id,
      email: user.email,
      status: "activated",
      email_sent: welcome_result.success
    })
  } else {
    results.push({
      user_id: user_id,
      status: "user_not_found"
    })
  }
}

return {
  processed: results,
  total_count: user_ids | length,
  success_count: results | filter:"status,activated" | length
}
```

## For Loop - Count-Based Iteration

### Basic For Loop
```javascript
// Send 5 reminder emails
For i from 1 to 5 {
  // Use index variable 'i'
  External_API_Request {
    url: env.EMAIL_SERVICE + "/remind",
    method: "POST",
    params: {
      template: "reminder_" ~ i,
      recipient: Input.user_email
    }
  }
  
  // Wait between sends
  Wait(1000)  // 1 second delay
}
```

### Dynamic Count
```javascript
// Send notifications based on user tier
notification_count = Input.user_tier == "premium" ? 10 : 
                    Input.user_tier == "gold" ? 5 : 3

For i from 1 to notification_count {
  Add_Record {
    table: "notifications",
    user_id: Input.user_id,
    message: "Daily update #" ~ i,
    priority: i <= 3 ? "high" : "normal"
  }
}
```

## While Loop - Condition-Based

### Basic While Loop
```javascript
// Process pending orders until queue is empty
has_pending = true

While (has_pending) {
  // Get next pending order
  pending_order = Query_All_Records {
    table: "orders",
    filter: {status: "pending"},
    limit: 1,
    sort: "created_at ASC"
  }
  
  If (pending_order | length > 0) {
    order = pending_order[0]
    
    // Process the order
    Process_Order(order)
    
    // Mark as processed
    Edit_Record {
      id: order.id,
      status: "processed"
    }
  } Else {
    // No more pending orders
    has_pending = false
  }
}
```

### Rate-Limited Processing
```javascript
// Process API calls with rate limiting
api_calls = Input.api_requests
processed = 0
max_per_minute = 60

While (processed < api_calls | length) {
  // Process batch
  batch_end = processed + max_per_minute
  
  For i from processed to batch_end {
    If (i < api_calls | length) {
      request = api_calls[i]
      
      External_API_Request {
        url: request.url,
        method: request.method,
        params: request.data
      }
    }
  }
  
  processed = batch_end
  
  // Wait 1 minute between batches
  If (processed < api_calls | length) {
    Wait(60000)  // 60 seconds
  }
}
```

## Loop Control Functions

### Loop Break
```javascript
// Find first admin user
For Each user in $var.all_users {
  If (user.role == "admin") {
    admin_user = user
    Break  // Exit loop early
  }
}
```

### Loop Continue
```javascript
// Process only active users
For Each user in $var.users {
  If (user.status != "active") {
    Continue  // Skip to next iteration
  }
  
  // Process active user
  Send_Email {
    to: user.email,
    subject: "Monthly Newsletter"
  }
}
```

### Remove Entry
```javascript
// Clean up expired sessions
sessions = Query_All_Records {
  table: "sessions"
}

For Each session in sessions {
  If (session.expires_at < timestamp()) {
    // Remove expired session from array
    Remove_Entry
    
    // Also delete from database
    Delete_Record {
      id: session.id
    }
  }
}

// sessions array now only contains active sessions
```

## Performance Optimization

### Stream Processing for Large Datasets
```javascript
// Use stream return type for memory efficiency
large_dataset = Query_All_Records {
  table: "large_table",
  return_type: "stream"  // Memory efficient!
}

For Each record in large_dataset {
  // Process each record without loading all into memory
  Process_Record(record)
}
```

### Batch Operations
```javascript
// Process records in batches
batch_size = 100
offset = 0
has_more = true

While (has_more) {
  batch = Query_All_Records {
    table: "records",
    limit: batch_size,
    offset: offset
  }
  
  If (batch | length == 0) {
    has_more = false
  } Else {
    // Process batch
    For Each record in batch {
      Update_Record(record)
    }
    
    offset = offset + batch_size
  }
}
```

### Conditional Processing
```javascript
// Skip unnecessary processing
For Each order in $var.orders {
  // Quick checks first
  If (order.status == "cancelled") {
    Continue
  }
  
  If (order.total == 0) {
    Continue
  }
  
  // Only process valid orders
  Expensive_Processing(order)
}
```

## Common Patterns

### Data Transformation
```javascript
// Transform array of objects
users = Input.raw_users
formatted_users = []

For Each user in users {
  formatted_user = {
    id: user.id,
    name: user.first_name ~ " " ~ user.last_name,
    email: user.email | lower,
    profile_complete: user.bio && user.avatar ? true : false,
    member_since: user.created_at | date:"Y-m-d"
  }
  
  formatted_users.push(formatted_user)
}

return formatted_users
```

### Nested Loops
```javascript
// Process orders with items
For Each order in $var.orders {
  order_total = 0
  
  For Each item in order.items {
    // Calculate item total
    item_total = item.price * item.quantity
    order_total = order_total + item_total
    
    // Update inventory
    current_stock = Get_Record {
      table: "products",
      field_name: "id",
      field_value: item.product_id
    }
    
    Edit_Record {
      id: item.product_id,
      quantity: current_stock.quantity - item.quantity
    }
  }
  
  // Update order total
  Edit_Record {
    id: order.id,
    calculated_total: order_total
  }
}
```

### Error Handling in Loops
```javascript
errors = []
successes = []

For Each item in Input.items {
  Try {
    result = Process_Item(item)
    successes.push({
      item_id: item.id,
      result: result
    })
  } Catch (error) {
    errors.push({
      item_id: item.id,
      error: error.message
    })
    Continue  // Continue processing other items
  }
}

return {
  success_count: successes | length,
  error_count: errors | length,
  errors: errors
}
```

## Loop Types Comparison

### When to Use Each Type

**For Each Loop:**
- Processing arrays/lists
- Database records
- API response arrays
- User-provided data

**For Loop:**
- Fixed number of iterations
- Counting operations
- Generating sequences
- Retry logic

**While Loop:**
- Unknown iteration count
- Condition-based processing
- Queue processing
- Polling operations

## Try This

Create a bulk email system:
1. Add For Each loop
2. Process user list
3. Send personalized emails
4. Handle errors gracefully
5. Track success/failure rates

## Pro Tips

💡 **Use Stream Mode:** Set return_type to "stream" for large datasets

💡 **Batch Processing:** Process large datasets in smaller chunks

💡 **Early Exit:** Use Break to exit loops when condition is met

💡 **Error Handling:** Wrap risky operations in Try/Catch

💡 **Progress Tracking:** Track loop progress for user feedback

## Common Gotchas

### Memory Issues
```javascript
// Problem: Loading huge dataset into memory
huge_dataset = Query_All_Records("large_table")  // Loads everything!

// Solution: Use stream processing
huge_dataset = Query_All_Records {
  table: "large_table",
  return_type: "stream"  // Memory efficient
}
```

### Infinite Loops
```javascript
// Problem: Condition never changes
counter = 0
While (counter < 10) {
  Process_Something()
  // Forgot to increment counter!
}

// Solution: Always update loop condition
counter = 0
While (counter < 10) {
  Process_Something()
  counter = counter + 1  // Update condition
}
```

### Variable Scope
```javascript
// Access the loop item variable correctly
For Each user in users {
  // Use 'user' not 'users'
  Send_Email {
    to: user.email,  // Correct
    subject: "Hello " ~ user.name
  }
}
```

## Next Steps

1. Practice basic loops
2. Implement error handling
3. Optimize for large datasets
4. Build nested loop logic
5. Monitor performance

Remember: Loops are powerful for bulk operations - start simple and optimize as needed!