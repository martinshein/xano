---
title: "Create Variable - Storing and Managing Data in Functions"
description: "Learn how to create and use variables to store data, perform calculations, and manage state in Xano function stacks"
category: function-stack
subcategory: data-manipulation
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- variables
- data-storage
- state-management
- calculations
- expressions
---

# Create Variable - Storing and Managing Data in Functions

## Quick Summary

> **What it is:** A function that creates named containers to store any type of data for use throughout your function stack
> 
> **When to use:** Whenever you need to store calculated values, transform data, hold temporary results, or prepare response data
> 
> **Key benefit:** Simplifies complex logic by breaking it into manageable pieces with clear, reusable values
> 
> **Pro tip:** Variables make your function stacks readable and maintainable

## What You'll Learn

- Creating different types of variables
- Using expressions to calculate values
- Building complex data structures
- Optimizing with variable reuse
- Best practices for n8n and WeWeb integrations

## Understanding Variables

Think of variables as labeled boxes where you store information:
- **Name:** The label on the box (how you reference it)
- **Value:** What's inside the box (data, calculation result, etc.)
- **Type:** What kind of data it holds (text, number, object, array)

## Basic Variable Creation

### Simple Variables

```javascript
// Text variable
greeting = "Welcome to our platform!"

// Number variable
tax_rate = 0.08

// Boolean variable
is_premium = true

// Timestamp
current_time = timestamp_now()
```

### Calculated Variables

```javascript
// Math calculation
total_price = subtotal + (subtotal * tax_rate)

// String concatenation
full_name = first_name + " " + last_name

// Conditional value
status = (order.paid == true) ? "completed" : "pending"
```

## Variable Types

### 1. Text (String) Variables

```javascript
// Direct text
company_name = "Acme Corp"

// Concatenation
welcome_message = "Hello, " + user.name + "!"

// Template-like construction
order_id = "ORD-" + timestamp_unix() + "-" + user.id
```

### 2. Numeric Variables

```javascript
// Integer
item_count = 5

// Decimal
price = 19.99

// Calculated
discount_amount = original_price * discount_percentage
final_price = original_price - discount_amount
```

### 3. Boolean Variables

```javascript
// Direct boolean
is_active = true

// Comparison result
has_access = (user.role == "admin" OR user.role == "editor")

// Complex logic
can_purchase = (user.age >= 18 AND user.verified AND inventory > 0)
```

### 4. Object Variables

```javascript
// Create structured data
user_profile = {
  id: user.id,
  name: user.full_name,
  email: user.email,
  preferences: {
    theme: "dark",
    notifications: true
  }
}

// API response format
api_response = {
  status: "success",
  data: query_result,
  timestamp: timestamp_now()
}
```

### 5. Array Variables

```javascript
// Direct array
allowed_roles = ["admin", "manager", "supervisor"]

// From query results
active_users = query_all_records.where(status = "active")

// Constructed array
order_items = [
  {id: 1, name: "Product A", quantity: 2},
  {id: 2, name: "Product B", quantity: 1}
]
```

## Practical Examples

### Example 1: E-commerce Calculations

```javascript
// Step 1: Calculate subtotal
subtotal = SUM(cart_items.price * cart_items.quantity)

// Step 2: Apply discount
discount_amount = (has_coupon) ? subtotal * 0.1 : 0

// Step 3: Calculate tax
taxable_amount = subtotal - discount_amount
tax = taxable_amount * 0.08

// Step 4: Final total
order_total = taxable_amount + tax + shipping_cost

// Step 5: Create order summary
order_summary = {
  subtotal: subtotal,
  discount: discount_amount,
  tax: tax,
  shipping: shipping_cost,
  total: order_total
}
```

### Example 2: User Permissions

```javascript
// Check multiple conditions
is_admin = (user.role == "admin")
is_owner = (resource.created_by == user.id)
is_team_member = (user.team_id == resource.team_id)

// Combine permissions
can_edit = (is_admin OR is_owner OR is_team_member)
can_delete = (is_admin OR is_owner)

// Create permission object
permissions = {
  view: true,  // Everyone can view
  edit: can_edit,
  delete: can_delete,
  share: is_owner
}
```

### Example 3: Data Transformation

```javascript
// Transform database record for API
formatted_user = {
  id: user.id,
  displayName: user.first_name + " " + user.last_name,
  avatar: user.profile_image || "/default-avatar.png",
  memberSince: FORMAT_DATE(user.created_at, "MMM YYYY"),
  isPremium: (user.subscription_tier != "free")
}
```

## Advanced Techniques

### Using Expressions

```javascript
// Ternary operator
greeting = (current_hour < 12) ? "Good morning" : "Good afternoon"

// Null coalescing
display_name = user.nickname || user.full_name || "Guest"

// Complex expressions
is_eligible = (
  user.age >= 18 AND 
  user.account_status == "verified" AND
  (user.credit_score > 650 OR user.has_guarantor)
)
```

### Variable Chaining

```javascript
// Build upon previous variables
base_price = 100
member_discount = base_price * 0.2
seasonal_discount = base_price * 0.1
final_discount = MAX(member_discount, seasonal_discount)
final_price = base_price - final_discount
```

### Dynamic Variable Values

```javascript
// Based on conditions
api_endpoint = (environment == "production") 
  ? "https://api.production.com" 
  : "https://api.staging.com"

// Based on user input
sort_field = input.sort_by || "created_at"
sort_order = input.order || "DESC"
```

## Integration Patterns

### With n8n Workflows

```javascript
// Prepare webhook response
webhook_response = {
  received: true,
  processed_at: timestamp_now(),
  record_id: new_record.id,
  next_action: "send_notification"
}

// Format for n8n node
n8n_data = {
  json: transformed_data,
  binary: {},
  headers: {
    "X-Process-ID": process_id
  }
}
```

### With WeWeb

```javascript
// Prepare paginated response
page_data = {
  items: query_results,
  page: input.page || 1,
  per_page: input.per_page || 20,
  total: total_count,
  total_pages: CEIL(total_count / per_page)
}

// Format for WeWeb collections
collection_format = {
  data: page_data.items,
  pagination: {
    current: page_data.page,
    total: page_data.total_pages,
    has_more: (page_data.page < page_data.total_pages)
  }
}
```

## Common Mistakes to Avoid

1. **Overwriting Variables**
   ```javascript
   // Bad: Losing original value
   price = 100
   price = price * 1.2  // Original price lost
   
   // Good: Use new variable
   original_price = 100
   discounted_price = original_price * 1.2
   ```

2. **Type Mismatches**
   ```javascript
   // Bad: Mixing types
   total = "10" + 5  // Results in "105" (string)
   
   // Good: Ensure consistent types
   total = parseInt("10") + 5  // Results in 15 (number)
   ```

3. **Null/Undefined Handling**
   ```javascript
   // Bad: Not handling null
   full_name = user.first + " " + user.last  // Error if null
   
   // Good: Safe handling
   full_name = (user.first || "") + " " + (user.last || "")
   ```

## Best Practices

### Naming Conventions

```javascript
// Use descriptive names
is_active  // Boolean (starts with is_, has_, can_)
user_count  // Number (describes what's counted)
formatted_date  // Processed data (describes transformation)
raw_response  // Original data (prefixed with raw_)
```

### Organize Complex Logic

```javascript
// Break complex calculations into steps
// Step 1: Validate
is_valid_user = (user != null AND user.active)

// Step 2: Check permissions
has_permission = (user.role == "admin" OR user.id == owner_id)

// Step 3: Final check
can_proceed = (is_valid_user AND has_permission)
```

### Document with Variable Names

```javascript
// Self-documenting variable names
days_until_expiration = 30
minimum_order_for_free_shipping = 50
max_retry_attempts = 3
```

## Try This

Create a dynamic pricing calculator:
1. Create base_price variable from product
2. Calculate quantity_discount based on amount
3. Apply member_discount if applicable
4. Add rush_delivery_fee if needed
5. Create final price_breakdown object

## Pro Tips

💡 **Reuse Variables:** Calculate once, use many times to improve performance

💡 **Clear Names:** Use descriptive names that explain the variable's purpose

💡 **Type Safety:** Always consider the data type when creating variables

💡 **Debug Values:** Create variables to inspect intermediate calculation results

## Performance Optimization

- **Calculate Once:** Store database queries in variables instead of repeating them
- **Simplify Expressions:** Break complex expressions into multiple variables
- **Prepare Response Data:** Build your response structure with variables
- **Cache Calculations:** Store expensive calculations for reuse

Remember: Variables are the building blocks of your function logic. Use them liberally to make your code clear, efficient, and maintainable!