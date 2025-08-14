---
title: "Switch Statement - Multiple Path Branching"
description: "Create efficient multi-path logic flows with switch statements in Xano function stacks"
category: function-stack
subcategory: control-flow
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- switch
- branching
- control-flow
- conditionals
- case-logic
---

# Switch Statement - Multiple Path Branching

## Quick Summary

> **What it is:** A control flow function that executes different code based on matching a value against multiple cases
> 
> **When to use:** When you have 3+ different paths based on a single variable value - much cleaner than nested if/else statements
> 
> **Key benefit:** Readable, maintainable code for complex branching logic
> 
> **Best for:** Status handling, event routing, user role logic, API response codes

## What You'll Learn

- Building switch statements visually
- Defining cases and default paths
- When to use switch vs if/else
- Real-world patterns for automation
- Performance considerations

## Understanding Switch Logic

Think of a switch like a smart traffic router:
```javascript
SWITCH (status) {
  CASE "pending": 
    // Do pending logic
  CASE "approved":
    // Do approved logic
  CASE "rejected":
    // Do rejected logic
  DEFAULT:
    // Handle unexpected values
}
```

## Basic Configuration

### Setting Up a Switch

1. **Add Switch Function** to your stack
2. **Define the switch variable** (what to check)
3. **Add cases** for each possible value
4. **Add default** for unmatched values (optional but recommended)

## Practical Examples

### Example 1: Order Status Processing

```javascript
SWITCH (order.status) {
  CASE "new":
    - Send order confirmation email
    - Create invoice
    - Update inventory
    
  CASE "processing":
    - Notify warehouse
    - Generate shipping label
    - Update tracking
    
  CASE "shipped":
    - Send tracking email
    - Update delivery estimate
    - Notify customer
    
  CASE "delivered":
    - Request review
    - Close order
    - Update metrics
    
  DEFAULT:
    - Log unknown status
    - Send alert to admin
}
```

### Example 2: User Role Permissions

```javascript
SWITCH (user.role) {
  CASE "admin":
    permissions = {
      read: true,
      write: true,
      delete: true,
      manage_users: true
    }
    
  CASE "editor":
    permissions = {
      read: true,
      write: true,
      delete: false,
      manage_users: false
    }
    
  CASE "viewer":
    permissions = {
      read: true,
      write: false,
      delete: false,
      manage_users: false
    }
    
  DEFAULT:
    permissions = {
      read: false,
      write: false,
      delete: false,
      manage_users: false
    }
}
```

### Example 3: Webhook Event Router

```javascript
SWITCH (webhook.event_type) {
  CASE "payment.success":
    - Update order to paid
    - Send receipt
    - Start fulfillment
    
  CASE "payment.failed":
    - Mark payment failed
    - Send retry email
    - Log failure reason
    
  CASE "subscription.created":
    - Create user account
    - Send welcome email
    - Set up billing
    
  CASE "subscription.cancelled":
    - Update user status
    - Send cancellation email
    - Schedule data export
    
  DEFAULT:
    - Log unhandled event
    - Send to dead letter queue
}
```

## Advanced Patterns

### Multiple Cases Same Action

```javascript
SWITCH (day_of_week) {
  CASE "Monday":
  CASE "Tuesday":
  CASE "Wednesday":
  CASE "Thursday":
  CASE "Friday":
    business_hours = "9 AM - 5 PM"
    is_open = true
    
  CASE "Saturday":
    business_hours = "10 AM - 2 PM"
    is_open = true
    
  CASE "Sunday":
    business_hours = "Closed"
    is_open = false
}
```

### Nested Switch Statements

```javascript
SWITCH (request.method) {
  CASE "GET":
    SWITCH (request.resource) {
      CASE "users":
        Return all users
      CASE "products":
        Return all products
    }
    
  CASE "POST":
    SWITCH (request.resource) {
      CASE "users":
        Create new user
      CASE "products":
        Create new product
    }
}
```

### Switch with Variables

```javascript
// Calculate discount tier
SWITCH (customer.loyalty_points) {
  CASE (points < 100):
    discount = 0
    tier = "Bronze"
    
  CASE (points < 500):
    discount = 5
    tier = "Silver"
    
  CASE (points < 1000):
    discount = 10
    tier = "Gold"
    
  DEFAULT:
    discount = 15
    tier = "Platinum"
}
```

## Integration Patterns

### With n8n Workflows

```javascript
// Route n8n webhook by action
SWITCH (input.action) {
  CASE "sync_customer":
    - Query customer data
    - Format for CRM
    - Return sync status
    
  CASE "generate_report":
    - Aggregate data
    - Create PDF
    - Send email with attachment
    
  CASE "trigger_automation":
    - Validate permissions
    - Execute automation
    - Log execution
}
```

### With WeWeb Actions

```javascript
// Handle form submission types
SWITCH (form.type) {
  CASE "contact":
    - Send to support team
    - Create ticket
    - Auto-reply to user
    
  CASE "registration":
    - Create account
    - Send verification
    - Add to mailing list
    
  CASE "feedback":
    - Store feedback
    - Analyze sentiment
    - Route to department
}
```

## When to Use Switch vs If/Else

### Use Switch When:
- Checking one variable against multiple values
- You have 3+ different paths
- Values are discrete (not ranges)
- Code readability is important

### Use If/Else When:
- Complex conditions with AND/OR
- Checking ranges or inequalities
- Only 2 paths needed
- Multiple variables involved

## Common Mistakes to Avoid

1. **Missing Default Case**
   ```javascript
   // Always include default
   DEFAULT:
     Log "Unexpected value: " + switch_value
     Handle gracefully
   ```

2. **Fall-through Logic**
   ```javascript
   // Each case is independent in Xano
   // No need for 'break' statements
   ```

3. **Complex Conditions**
   ```javascript
   // Bad: Complex logic in switch
   SWITCH (age > 18 AND status == "active")
   
   // Good: Use if/else for complex conditions
   IF (age > 18 AND status == "active")
   ```

## Best Practices

### Clear Case Values

```javascript
// Use constants or enums
ORDER_STATUS_NEW = "new"
ORDER_STATUS_PROCESSING = "processing"

SWITCH (order.status) {
  CASE ORDER_STATUS_NEW:
    // Clear what this handles
}
```

### Document Cases

```javascript
SWITCH (api_response_code) {
  CASE 200:  // Success
    Process successful response
    
  CASE 404:  // Not found
    Handle missing resource
    
  CASE 500:  // Server error
    Retry with backoff
}
```

### Group Related Logic

```javascript
SWITCH (notification.type) {
  // Email notifications
  CASE "email_welcome":
  CASE "email_reset":
  CASE "email_invoice":
    Send via email service
    
  // SMS notifications  
  CASE "sms_verify":
  CASE "sms_alert":
    Send via SMS service
}
```

## Try This

Build a dynamic pricing engine:
1. Switch on customer type (new, returning, VIP)
2. Apply appropriate discount
3. Switch on product category
4. Apply category rules
5. Calculate final price

## Pro Tips

💡 **Order Matters:** Put most common cases first for readability

💡 **Use Constants:** Define case values as variables for reusability

💡 **Always Default:** Include default case to catch unexpected values

💡 **Combine Cases:** Multiple cases can share the same logic block

## Performance Optimization

- Switch statements are O(1) - very fast
- More efficient than multiple if/else chains
- Consider lookup tables for very large switches
- Use early returns in complex cases

Remember: Switch statements make your code cleaner and more maintainable when dealing with multiple paths based on a single value!