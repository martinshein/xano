---
title: "Conditional Logic - Building Smart Decisions"
description: "Create intelligent workflows with if/then/else logic and conditional branching in Xano"
category: function-stack
subcategory: control-flow
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- conditionals
- if-else
- logic
- branching
- decision-making
---

# Conditional Logic - Building Smart Decisions

## Quick Summary

> **What it is:** Visual if/then/else statements that let your functions make decisions and execute different paths based on conditions
> 
> **When to use:** Whenever you need different behavior based on user roles, data values, time conditions, or any business logic
> 
> **Key benefit:** Create adaptive applications that respond intelligently to different scenarios
> 
> **Visual approach:** Drag-and-drop conditional blocks without writing complex code

## What You'll Learn

- Building if/then/else logic visually
- Creating complex multi-condition flows
- Nesting conditionals for advanced logic
- Best practices for maintainable conditions
- Real-world patterns for n8n and WeWeb

## Understanding Conditionals

Conditionals are decision points in your function:
- **IF** condition is true → Do this
- **ELSE IF** another condition is true → Do that
- **ELSE** → Do default action

Think of it like a smart assistant following instructions based on what they observe.

## Basic Conditional Structure

### Simple If/Else

```javascript
IF (user.age >= 18) {
  // Adult user path
  - Show all content
  - Enable purchases
  - No restrictions
} ELSE {
  // Minor user path
  - Show age-appropriate content
  - Disable purchases
  - Apply parental controls
}
```

### Multiple Conditions (Else If)

```javascript
IF (order.total > 1000) {
  discount = 20  // VIP discount
} ELSE IF (order.total > 500) {
  discount = 15  // Gold discount
} ELSE IF (order.total > 100) {
  discount = 10  // Silver discount
} ELSE {
  discount = 0   // No discount
}
```

## Setting Up Conditionals in Xano

### Visual Configuration

1. **Add Conditional block** to function stack
2. **Define condition** using expression builder
3. **Add functions** to IF branch
4. **Add functions** to ELSE branch
5. **Test both paths** with debugger

### Expression Builder

Build conditions visually:
- Select variables from dropdown
- Choose operators (==, !=, >, <, etc.)
- Combine with AND/OR logic
- Preview condition result

## Practical Examples

### Example 1: User Authentication Flow

```javascript
// Check authentication status
IF (auth.token == null) {
  // Not logged in
  Return {
    error: "Authentication required",
    code: 401
  }
} ELSE IF (auth.expired == true) {
  // Token expired
  Refresh token
  IF (refresh.success) {
    Continue with request
  } ELSE {
    Return {
      error: "Session expired",
      code: 401
    }
  }
} ELSE {
  // Valid auth - proceed
  Process request
}
```

### Example 2: Dynamic Pricing Logic

```javascript
// Calculate price based on customer type
IF (customer.type == "wholesale") {
  base_price = product.wholesale_price
  
  IF (order.quantity >= 100) {
    additional_discount = 0.1  // 10% bulk discount
  } ELSE {
    additional_discount = 0
  }
  
} ELSE IF (customer.is_member == true) {
  base_price = product.member_price
  additional_discount = 0.05  // 5% member bonus
  
} ELSE {
  base_price = product.retail_price
  additional_discount = 0
}

final_price = base_price * (1 - additional_discount)
```

### Example 3: Content Visibility Rules

```javascript
// Determine what content to show
IF (user.subscription == "premium") {
  // Premium users see everything
  content = Query: all_content
  ads_enabled = false
  download_enabled = true
  
} ELSE IF (user.subscription == "basic") {
  // Basic users have limits
  content = Query: basic_content
  ads_enabled = true
  download_enabled = false
  
} ELSE {
  // Free users
  content = Query: free_content LIMIT 5
  ads_enabled = true
  download_enabled = false
  show_upgrade_prompt = true
}
```

## Advanced Conditional Patterns

### Nested Conditionals

```javascript
IF (request.method == "POST") {
  // Handle POST requests
  IF (validate_input(request.body)) {
    IF (user.can_create) {
      Create record
      Return success
    } ELSE {
      Return "Permission denied"
    }
  } ELSE {
    Return "Invalid input"
  }
} ELSE IF (request.method == "GET") {
  // Handle GET requests
  IF (user.authenticated) {
    Return user_data
  } ELSE {
    Return public_data
  }
}
```

### Guard Clauses (Early Returns)

```javascript
// Check prerequisites first
IF (user == null) {
  Return "User not found"
  STOP
}

IF (user.banned == true) {
  Return "Account suspended"
  STOP
}

IF (user.email_verified == false) {
  Return "Please verify email"
  STOP
}

// Main logic (only runs if all checks pass)
Process user request
```

### Switch-like Pattern

```javascript
// Multiple exclusive conditions
IF (status == "pending") {
  color = "yellow"
  icon = "clock"
  message = "Processing..."
  
} ELSE IF (status == "approved") {
  color = "green"
  icon = "check"
  message = "Approved!"
  
} ELSE IF (status == "rejected") {
  color = "red"
  icon = "x"
  message = "Rejected"
  
} ELSE {
  color = "gray"
  icon = "question"
  message = "Unknown status"
}
```

## Combining Conditions

### AND Logic (All must be true)

```javascript
IF (user.age >= 18 AND user.verified AND user.country == "US") {
  // All conditions met
  Enable full access
}
```

### OR Logic (Any can be true)

```javascript
IF (user.role == "admin" OR user.role == "moderator" OR user.is_owner) {
  // Has elevated permissions
  Show admin panel
}
```

### Complex Combinations

```javascript
IF ((user.premium AND user.credits > 0) OR user.role == "admin") {
  // Either premium with credits OR admin
  Allow premium feature
}
```

## Integration Patterns

### With n8n Workflows

```javascript
// Route webhook to appropriate n8n workflow
IF (webhook.event == "order.created") {
  trigger_url = "n8n.com/webhook/new-order"
  
} ELSE IF (webhook.event == "user.signup") {
  trigger_url = "n8n.com/webhook/onboarding"
  
} ELSE IF (webhook.event == "payment.failed") {
  trigger_url = "n8n.com/webhook/payment-recovery"
  
} ELSE {
  // Unknown event
  Log error
  trigger_url = null
}

IF (trigger_url != null) {
  Send to n8n webhook
}
```

### With WeWeb

```javascript
// Conditional data for WeWeb frontend
IF (user.onboarding_complete == false) {
  // Show onboarding data
  Return {
    show_tour: true,
    step: user.onboarding_step,
    tips: onboarding_tips
  }
} ELSE {
  // Regular dashboard
  Return {
    show_tour: false,
    dashboard_data: user_metrics,
    notifications: recent_notifications
  }
}
```

## Best Practices

### Keep Conditions Simple

```javascript
// Bad: Complex nested condition
IF ((a > b AND (c == d OR e != f)) AND (g OR (h AND i)))

// Good: Break into named variables
condition1 = (a > b)
condition2 = (c == d OR e != f)
condition3 = (g OR (h AND i))

IF (condition1 AND condition2 AND condition3)
```

### Use Descriptive Names

```javascript
// Bad
IF (u.t == "p" AND u.s > 100)

// Good
is_premium_user = (user.tier == "premium")
has_high_score = (user.score > 100)

IF (is_premium_user AND has_high_score)
```

### Handle All Cases

```javascript
// Always include ELSE for unexpected cases
IF (known_condition_1) {
  // Handle case 1
} ELSE IF (known_condition_2) {
  // Handle case 2
} ELSE {
  // Handle unexpected
  Log "Unexpected condition"
  Use safe default
}
```

## Common Mistakes to Avoid

1. **Forgetting ELSE clause**
   - Always handle the "what if none match" case

2. **Over-nesting conditions**
   - Break complex logic into separate functions

3. **Duplicate logic in branches**
   - Extract common code outside conditionals

4. **Not testing all paths**
   - Use debugger to verify each branch works

## Try This

Build a smart access control system:
1. Check if user is authenticated
2. Verify user role and permissions
3. Check resource ownership
4. Apply time-based restrictions
5. Return appropriate access level

## Pro Tips

💡 **Early Returns:** Use guard clauses to handle edge cases first

💡 **Named Conditions:** Store complex conditions in variables for clarity

💡 **Consistent Structure:** Keep similar logic patterns across your app

💡 **Comment Complex Logic:** Add descriptions to explain business rules

## Performance Considerations

- Conditions are evaluated sequentially (top to bottom)
- Put most likely conditions first
- Expensive operations should be evaluated last
- Cache condition results if reused

Remember: Good conditional logic makes your applications smart and adaptive. Structure them well for maintainable, intelligent systems!