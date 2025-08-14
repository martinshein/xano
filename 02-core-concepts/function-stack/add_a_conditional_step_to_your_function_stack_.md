---
title: "Conditional Logic - If/Then/Else in Function Stacks"
description: "Add intelligent branching logic to your Xano functions with conditional statements"
category: function-stack
subcategory: control-flow
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- conditionals
- logic
- branching
- if-else
- control-flow
---

# Conditional Logic - If/Then/Else in Function Stacks

## Quick Summary

> **What it is:** A control flow function that executes different code paths based on conditions you define
> 
> **When to use:** When you need different behavior based on user roles, data values, time of day, or any other criteria
> 
> **Key benefit:** Creates smart, adaptive APIs that respond differently to different situations
> 
> **Visual Builder:** Drag-and-drop interface for complex logic without code

## What You'll Learn

- Setting up if/then/else logic visually
- Creating complex conditions with AND/OR operators
- Nesting conditionals for advanced flows
- Common patterns for n8n and WeWeb
- Performance optimization tips

## Understanding Conditionals

Think of conditionals like a traffic controller directing data flow:
- **IF** the condition is true → Execute Path A
- **ELSE** → Execute Path B
- **ELSE IF** → Check another condition (optional)

## Basic Configuration

### Simple Condition

```javascript
IF (user.role == "admin") {
  // Admin-only functions
  Get all user records
  Include sensitive data
} ELSE {
  // Regular user functions
  Get own records only
  Exclude sensitive data
}
```

### Setting Up Conditions

1. **Add Conditional Function** to your stack
2. **Define the condition** using the expression builder
3. **Add functions** to the IF branch
4. **Add functions** to the ELSE branch (optional)

## Condition Types

### Comparison Operators

```javascript
// Equality
user.status == "active"
order.total != 0

// Numeric comparisons
age >= 18
quantity > 0
price <= budget

// String operations
email CONTAINS "@company.com"
name STARTS_WITH "Dr."
status IN ["active", "pending"]
```

### Boolean Checks

```javascript
// Direct boolean
is_verified == true
has_subscription

// Null checks
profile_image != null
deleted_at == null
```

### Complex Conditions

```javascript
// AND operator (all must be true)
(user.role == "premium") AND (subscription.status == "active")

// OR operator (any can be true)
(user.role == "admin") OR (user.role == "moderator")

// Combined logic
(age >= 18) AND ((country == "US") OR (country == "CA"))
```

## Practical Examples

### Example 1: User Access Control

```javascript
Condition: auth.user_id == resource.owner_id

IF TRUE:
  - Get full record details
  - Include private fields
  - Allow editing

ELSE:
  - Get public fields only
  - Read-only access
  - Log access attempt
```

### Example 2: Dynamic Pricing

```javascript
Condition: user.subscription_tier == "premium"

IF TRUE:
  - Apply 20% discount
  - Free shipping
  - Priority support flag

ELSE IF: user.total_purchases > 1000
  - Apply 10% discount
  - Free shipping

ELSE:
  - Standard pricing
  - Calculate shipping
```

### Example 3: Time-Based Logic

```javascript
Condition: current_hour >= 9 AND current_hour < 17

IF TRUE:
  - Send immediate notification
  - Mark as "business hours"

ELSE:
  - Queue for next business day
  - Send email only
```

## Advanced Patterns

### Nested Conditionals

```javascript
IF (user.authenticated) {
  IF (user.role == "admin") {
    // Admin logic
  } ELSE IF (user.role == "manager") {
    // Manager logic
  } ELSE {
    // Regular user logic
  }
} ELSE {
  // Guest user logic
}
```

### Early Returns

```javascript
IF (invalid_input) {
  Return error response
  STOP  // No further execution
}

// Continue with normal flow
Process valid input
```

### Guard Clauses

```javascript
// Check prerequisites first
IF (NOT user.email_verified) {
  Return "Please verify email"
}

IF (NOT user.profile_complete) {
  Return "Please complete profile"
}

// Main logic here
```

## Integration Patterns

### With n8n Workflows

```javascript
// Webhook routing based on event type
Condition: webhook.event_type

IF ("user.created"):
  - Send welcome email
  - Create CRM contact
  - Start onboarding sequence

ELSE IF ("user.deleted"):
  - Cancel subscriptions
  - Archive data
  - Send confirmation
```

### With WeWeb Forms

```javascript
// Form validation and submission
Condition: form.accept_terms == true

IF TRUE:
  - Validate all fields
  - Create account
  - Send to dashboard

ELSE:
  - Return error
  - Highlight terms checkbox
```

## Performance Tips

### Order Matters

```javascript
// Check simple conditions first
IF (user == null) return  // Fast check
IF (complex_calculation) return  // Slower check
```

### Avoid Redundant Checks

```javascript
// Bad: Multiple database queries
IF (get_user.role == "admin")
IF (get_user.status == "active")

// Good: Single query, multiple checks
user = get_user
IF (user.role == "admin" AND user.status == "active")
```

### Use Variables

```javascript
// Calculate once, use multiple times
is_premium = (user.tier == "premium" OR user.lifetime_value > 1000)

IF (is_premium) {
  // Premium features
}
```

## Common Mistakes to Avoid

1. **Wrong Operator Types**
   ```javascript
   // Bad: String comparison on number
   age == "18"  
   
   // Good: Numeric comparison
   age == 18
   ```

2. **Missing ELSE Handling**
   ```javascript
   // Always handle the else case
   ELSE {
     // Even if just logging
     Log "Unexpected condition"
   }
   ```

3. **Complex Nested Logic**
   ```javascript
   // Consider using Switch for many conditions
   // Or break into separate functions
   ```

## Best Practices

### Clear Condition Names

```javascript
// Use descriptive variable names
is_premium_user = (conditions...)
has_valid_subscription = (conditions...)
can_access_resource = (conditions...)

IF (is_premium_user AND has_valid_subscription)
```

### Consistent Return Structure

```javascript
// Both branches return same structure
IF (success) {
  Return { status: "success", data: result }
} ELSE {
  Return { status: "error", data: null }
}
```

### Documentation

```javascript
Description: "Check user permissions before allowing delete"
// Helps team understand logic flow
```

## Try This

Build a smart content access system:
1. Check if user is authenticated
2. Check subscription status
3. Check content restrictions
4. Apply different rules for each tier
5. Log access for analytics

## Pro Tips

💡 **Expression Builder:** Use the visual builder for complex conditions - it prevents syntax errors

💡 **Test Both Paths:** Always test both IF and ELSE branches during development

💡 **Variable Reuse:** Assign condition results to variables for reuse in multiple places

💡 **Switch Alternative:** For many conditions on the same variable, consider using Switch instead

## Debugging Conditionals

1. **Add Debug Output**
   ```javascript
   Create Variable: "condition_result" = your_condition
   // Check what the condition evaluated to
   ```

2. **Test with Sample Data**
   - Use the debugger with different inputs
   - Verify each branch executes correctly

3. **Log Branch Execution**
   ```javascript
   IF (...) {
     Log "Executing admin branch"
     // Your logic
   }
   ```

Remember: Good conditional logic makes your APIs smart and adaptive. Use them to create powerful, flexible backends that handle any scenario!