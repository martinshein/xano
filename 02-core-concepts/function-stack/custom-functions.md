---
title: "Custom Functions - Reusable Logic Blocks"
description: "Create reusable functions to avoid repetition and maintain consistency"
category: function-stack
subcategory: custom-functions
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- custom-functions
- reusability
- organization
- async
- no-code
---

# Custom Functions - Reusable Logic Blocks



## Quick Summary

> **What it is:** Reusable pieces of logic you can insert into multiple function stacks
> 
> **When to use:** When you have logic that repeats across different APIs or workflows
> 
> **Key benefit:** Write once, use everywhere - maintain logic in one place
> 
> **Perfect for:** Non-developers who want to build maintainable, organized backends

## What You'll Learn

- Creating custom functions
- Using functions in multiple places
- Passing data between functions
- Async execution options
- Best practices for reusability

## Why Custom Functions?

Think of custom functions like recipe cards:
- **Write the recipe once** (create function)
- **Use it in many dishes** (call from different APIs)
- **Update the recipe** (changes apply everywhere)
- **Share with team** (everyone uses same logic)

## Creating Custom Functions

### Step 1: Navigate to Library

1. Click Library icon in left navigation
2. Select "Functions" from submenu
3. Click "Add Function" button

### Step 2: Build Your Function

Just like building an API:
- Add inputs (what data it needs)
- Build function stack (the logic)
- Define output (what it returns)

### Step 3: Publish Changes

- Save your work
- Publish to make available
- Version control included

## Common Custom Functions

### Email Validator
```javascript
// Input: email_address

// Function Logic:
1. Check if empty
2. Verify @ symbol exists
3. Check domain format
4. Return is_valid (true/false)

// Usage: Call from any signup/login flow
```

### Price Calculator
```javascript
// Inputs: base_price, quantity, discount_code

// Function Logic:
1. Calculate subtotal
2. Apply discount if valid
3. Add tax
4. Return final_price

// Usage: Shopping cart, checkout, quotes
```

### User Permissions Check
```javascript
// Inputs: user_id, resource_type, action

// Function Logic:
1. Get user role
2. Check permission matrix
3. Return has_permission

// Usage: Every protected API endpoint
```

## Using Custom Functions

### Adding to Function Stack

1. Open any API or function
2. Click + to add function
3. Select "Custom Functions"
4. Choose your function
5. Map inputs and outputs

### Passing Data

```javascript
// In your API
user_email = Input.email

// Call custom function
validation_result = Email_Validator(user_email)

// Use the result
if (validation_result.is_valid) {
  // Continue processing
} else {
  // Return error
}
```

## Async Execution

### What is Async?

Normal execution:
```
Step 1 → Wait → Step 2 → Wait → Step 3
```

Async execution:
```
Step 1 → Step 2 (async) → Step 3
         ↓
    (runs separately)
```

### When to Use Async

**Good for:**
- Sending emails
- Processing uploads
- Generating reports
- Cleanup tasks
- Notifications

**Not for:**
- Getting data you need immediately
- Validation checks
- Authentication
- Critical path operations

### Enabling Async

1. Right-click custom function in stack
2. Select "Async Settings"
3. Choose execution type:
   - **Synchronous** - Wait for completion
   - **Async** - Queue and continue
   - **Async (dedicated)** - Enterprise option

## Integration Examples

### With n8n

```javascript
// n8n webhook triggers
Webhook_Data = Input

// Call validation function
is_valid = Validate_Webhook_Data(Webhook_Data)

// Call processing function
if (is_valid) {
  result = Process_Webhook(Webhook_Data)
}

// Return to n8n
return result
```

### With WeWeb

```javascript
// WeWeb form submission
Form_Data = Input

// Reusable validation
validation = Validate_Form_Input(Form_Data)

if (!validation.success) {
  return validation.errors
}

// Reusable save logic
saved_record = Save_Form_Data(Form_Data)

return saved_record
```

## Best Practices

### Single Responsibility

```javascript
// Good: One clear purpose
Calculate_Tax(amount, tax_rate)
Send_Email(recipient, subject, body)
Validate_Phone(phone_number)

// Avoid: Multiple purposes
Process_Order_And_Send_Email_And_Update_Inventory()
```

### Clear Inputs/Outputs

```javascript
// Good: Obvious what's needed
Format_Currency(
  amount: number,
  currency: text
) → formatted_text

// Avoid: Unclear requirements
Process_Data(data: object) → result
```

### Error Handling

```javascript
// Include error handling
Custom_Function {
  try {
    // Main logic
    return { success: true, data: result }
  } catch {
    return { success: false, error: message }
  }
}
```

## Common Patterns

### Wrapper Functions

Wrap complex operations:
```javascript
// Send SMS wrapper
Send_SMS(phone, message) {
  1. Format phone number
  2. Check credits
  3. Call Twilio API
  4. Log result
  5. Return status
}
```

### Validation Functions

Centralize validation:
```javascript
// Validate order
Validate_Order(order_data) {
  1. Check required fields
  2. Verify quantities
  3. Validate pricing
  4. Check inventory
  5. Return validation_result
}
```

### Transformation Functions

Standardize data formats:
```javascript
// Format for export
Format_For_CSV(records) {
  1. Flatten nested objects
  2. Format dates
  3. Clean special characters
  4. Return csv_ready_data
}
```

## Async Function Patterns

### Fire and Forget

```javascript
// Main API
Process_Order() {
  // Critical path
  save_order()
  charge_payment()
  
  // Async (not critical)
  Send_Confirmation_Email(async)
  Update_Analytics(async)
  
  // Return immediately
  return success
}
```

### Async with Await

```javascript
// Start async functions
email_id = Send_Email(async)
report_id = Generate_Report(async)

// Do other work
process_data()

// Wait for async results
Async_Function_Await([email_id, report_id])
```

## Try This

Create a reusable formatter:
1. Create custom function "Format_Phone"
2. Add input for phone number
3. Strip non-digits
4. Format as (XXX) XXX-XXXX
5. Use in multiple APIs

## Pro Tips

💡 **Version Control:** Always publish with clear descriptions

💡 **Test Separately:** Debug custom functions independently

💡 **Document Inputs:** Be clear about expected data types

💡 **Handle Errors:** Always return success/error status

💡 **Keep Simple:** Complex functions are hard to reuse

## Performance Considerations

### Sync vs Async Impact

**Synchronous:**
- Blocks execution
- Immediate results
- Uses main resources

**Asynchronous:**
- Non-blocking
- Delayed results
- Uses background resources

### Resource Usage

- Async functions use background task allocation
- Monitor usage in dashboard
- Consider dedicated resources for critical async

## Next Steps

1. Identify repeated logic
2. Create first custom function
3. Replace duplicated code
4. Add error handling
5. Experiment with async

Remember: Custom functions are your path to clean, maintainable, professional backend systems!