---
title: "Variables - Store and Use Data"
description: "Create and manage variables to store data in your function stack"
category: function-stack
subcategory: data-manipulation
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- variables
- data-storage
- function-stack
- basics
- no-code
---

# Variables - Store and Use Data



## Quick Summary

> **What it is:** Containers that hold information in your function stack for later use
> 
> **When to use:** Storing API responses, calculations, user data, or any value you need to reference
> 
> **Key benefit:** Keep data organized and accessible throughout your backend logic
> 
> **Perfect for:** Non-developers learning to manage data flow in their applications

## What You'll Learn

- Creating and naming variables
- Understanding data types
- Setting variable values
- Using variables in functions
- Best practices for organization

## What Are Variables?

Think of variables like labeled boxes where you store things:
- **Box** = The variable
- **Label** = The variable name
- **Contents** = The data value

You can put anything in the box, look inside later, and use what's there!

## Creating Your First Variable

### Step-by-Step

1. **Add Function**
   - Click + in function stack
   - Select "Create Variable"

2. **Name Your Variable**
   - Use descriptive names
   - No spaces (use underscore)
   - Example: `user_email`, `total_price`

3. **Set The Value**
   - Type directly
   - Select from dropdowns
   - Reference other variables

## Data Types Explained

### Text (String)
```javascript
name = "John Smith"
email = "john@example.com"
message = "Welcome back!"
```

### Numbers (Integer/Decimal)
```javascript
age = 25              // Integer
price = 19.99        // Decimal
quantity = 3         // Integer
```

### Boolean (True/False)
```javascript
is_active = true
has_subscription = false
email_verified = true
```

### Objects (Structured Data)
```javascript
user = {
  name: "John",
  age: 25,
  email: "john@example.com"
}
```

### Arrays (Lists)
```javascript
colors = ["red", "blue", "green"]
prices = [10, 20, 30, 40]
users = [user1, user2, user3]
```

## Common Use Cases

### Store API Response
```javascript
// After calling external API
weather_data = API_Response
temperature = weather_data.current.temp
```

### Calculate Values
```javascript
// Store calculation result
subtotal = 100
tax_rate = 0.08
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
```

### Build Response Data
```javascript
// Prepare data to return
response = {
  success: true,
  message: "Order completed",
  order_id: 12345,
  total: total
}
```

## Integration Examples

### With n8n
```javascript
// n8n sends data
webhook_data = Input

// Store in variables
customer_name = webhook_data.name
order_items = webhook_data.items
total_amount = webhook_data.total

// Process and return
processed_order = {
  customer: customer_name,
  items: order_items,
  amount: total_amount,
  status: "received"
}
```

### With WeWeb
```javascript
// WeWeb form submission
form_data = Input

// Create variables for validation
email = form_data.email
password = form_data.password
confirm_password = form_data.confirm

// Store validation result
passwords_match = (password == confirm_password)
```

## Variable Scope

### Function Stack Scope
- Variables exist within current function
- Available to all steps after creation
- Destroyed when function completes

### Passing Between Functions
```javascript
// Function 1: Create variable
user_id = 123

// Call Function 2 with variable
Function2(user_id)

// Function 2: Receive as input
received_id = Input.user_id
```

## Dynamic Values

### Using Expressions
```javascript
// Reference other variables
full_name = first_name + " " + last_name

// Use dot notation
user_email = user.profile.email

// Array access
first_item = items[0]
```

### With Filters
```javascript
// Apply filters to transform
upper_name = name | uppercase
rounded_price = price | round(2)
formatted_date = timestamp | format("MM/DD/YYYY")
```

## Best Practices

### Naming Conventions
```javascript
// Good names
user_email
total_price
is_verified
order_items

// Avoid
var1
temp
data
x
```

### Organize by Purpose
```javascript
// Input variables
input_email = Input.email
input_password = Input.password

// Processing variables
hashed_password = hash(input_password)
user_record = database_result

// Output variables
response_message = "Success"
response_data = user_record
```

### Initialize Early
```javascript
// Set defaults at start
error_messages = []
total_cost = 0
is_valid = true

// Update as needed
if (condition) {
  error_messages.push("Invalid input")
  is_valid = false
}
```

## Common Patterns

### Accumulator Pattern
```javascript
// Start with empty/zero
total = 0
items = []

// Add to it in loop
For Each item {
  total = total + item.price
  items.push(item.name)
}
```

### Flag Pattern
```javascript
// Set flag variable
has_errors = false

// Check conditions
if (email == null) {
  has_errors = true
}

// Use flag later
if (has_errors) {
  return error_response
}
```

### Temporary Storage
```javascript
// Store while processing
temp_user = Get_User()
temp_user.last_login = now()
Update_User(temp_user)
```

## Data Type Indicators

Watch the type indicator to avoid issues:
- 📝 Text (String)
- 🔢 Number (Integer/Decimal)
- ✓❌ Boolean
- {} Object
- [] Array
- ⌀ Null

## Try This

Create a user welcome flow:
1. Create variable for user name
2. Create variable for signup date
3. Create welcome message variable
4. Combine them into response object
5. Test with sample data

## Pro Tips

💡 **Use Clear Names:** `customer_email` beats `email1` every time

💡 **Group Related:** Keep similar variables together in your stack

💡 **Check Types:** Always verify the data type indicator

💡 **Document Complex:** Add descriptions for complex variable logic

💡 **Reuse Common:** Create variables for values used multiple times

## Common Gotchas

### Type Mismatches
```javascript
// Problem
age = "25"          // String
new_age = age + 1   // "251" not 26!

// Solution
age = 25            // Number
new_age = age + 1   // 26
```

### Undefined Variables
```javascript
// Problem
result = user.name  // Error if user doesn't exist

// Solution
if (user) {
  result = user.name
}
```

### Overwriting Values
```javascript
// Problem
total = 100
total = 50  // Lost original value!

// Solution
original_total = 100
discounted_total = 50
```

## Next Steps

1. Practice creating variables
2. Work with different data types
3. Build calculation chains
4. Pass variables between functions
5. Create complex data structures

Remember: Variables are the building blocks of your backend logic - master them and you can build anything!