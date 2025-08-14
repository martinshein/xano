---
title: "Expression - Dynamic Data Processing"
description: "Use expressions for real-time calculations, conditions, and data transformation"
category: function-stack
subcategory: data-types
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- expression
- dynamic
- calculations
- conditions
- filters
---

# Expression - Dynamic Data Processing



## Quick Summary

> **What it is:** Flexible data type for real-time calculations, conditions, and data transformation
> 
> **When to use:** Complex calculations, conditional logic, data filtering, or dynamic value generation
> 
> **Key benefit:** Powerful inline syntax combining math, logic, and filters in one expression
> 
> **Perfect for:** Non-developers building dynamic pricing, conditional flows, or calculated fields

## What You'll Learn

- Expression syntax and operators
- Using variables and inputs
- Mathematical and logical operations
- Filter integration
- Conditional expressions
- Real-world examples

## Basic Expression Setup

### Step 1: Enable Expression Type
1. Click any value field
2. Select "Expression" data type
3. Or click "Use Expression" link

### Step 2: Build Expression
```javascript
// Simple calculation
$input.price * 1.20

// With conditions
$input.quantity > 10 ? $input.price * 0.9 : $input.price

// Using filters
$input.name | upper ~ " - " ~ $input.category | lower
```

## Integration Examples

### With n8n - Dynamic Pricing
```javascript
// n8n sends order data
base_price = $input.base_price
quantity = $input.quantity
user_tier = $input.user_tier

// Dynamic pricing expression
final_price = base_price * (
  quantity >= 100 ? 0.8 :   // 20% bulk discount
  quantity >= 50 ? 0.9 :    // 10% volume discount
  quantity >= 10 ? 0.95 :   // 5% quantity discount
  1.0                       // no discount
) * (
  user_tier == "premium" ? 0.9 :  // 10% premium discount
  user_tier == "vip" ? 0.85 :     // 15% VIP discount
  1.0                             // regular price
)

return {
  original_price: base_price,
  final_price: final_price,
  savings: base_price - final_price,
  discount_percent: ((base_price - final_price) / base_price * 100) | round:2
}
```

### With WeWeb - Content Personalization
```javascript
// WeWeb user data
user_name = $input.user_name
last_login = $input.last_login_days
purchase_count = $input.total_purchases
user_region = $input.region

// Dynamic welcome message
welcome_message = "Hello " ~ (
  user_name ? user_name | upper : "Valued Customer"
) ~ "! " ~ (
  last_login > 30 ? "We missed you! Welcome back after " ~ last_login ~ " days." :
  last_login > 7 ? "Great to see you again!" :
  "Welcome back!"
) ~ " " ~ (
  purchase_count == 0 ? "Ready to make your first purchase?" :
  purchase_count < 5 ? "Thanks for your " ~ purchase_count ~ " purchases!" :
  "Thank you for being a loyal customer with " ~ purchase_count ~ " orders!"
)

// Regional content
content_language = user_region == "ES" ? "spanish" :
                  user_region == "FR" ? "french" :
                  user_region == "DE" ? "german" :
                  "english"

return {
  message: welcome_message,
  language: content_language,
  show_regional_offers: user_region != "US"
}
```

## Mathematical Operators

### Basic Operations
```javascript
// Addition
total = $input.price + $input.tax + $input.shipping

// Subtraction  
profit = $input.revenue - $input.costs

// Multiplication
area = $input.width * $input.height

// Division
average = $input.total_score / $input.test_count

// Parentheses for precedence
complex = ($input.a + $input.b) * ($input.c - $input.d)
```

### Advanced Math
```javascript
// Power operations
squared = $input.number * $input.number

// Percentage calculations
percentage = ($input.part / $input.whole) * 100

// Compound interest
compound = $input.principal * (1 + $input.rate) ^ $input.years
```

## Comparison Operators

### Equality and Inequality
```javascript
// Loose equality (type conversion)
is_equal = $input.score == "100"  // true if score is 100

// Strict equality (no type conversion)
is_strict_equal = $input.score === 100  // only true if score is integer 100

// Not equal
is_different = $input.status != "active"

// Strict not equal
is_strict_different = $input.count !== "0"
```

### Numerical Comparisons
```javascript
// Greater than
is_premium = $input.price > 99.99

// Greater than or equal
is_eligible = $input.age >= 18

// Less than
is_discount = $input.quantity < 5

// Less than or equal
is_budget = $input.budget <= 1000
```

## Logical Operators

### AND, OR, NOT
```javascript
// AND - both conditions must be true
is_qualified = $input.age >= 18 && $input.income > 50000

// OR - either condition can be true
has_discount = $input.is_member || $input.first_purchase

// NOT - reverses boolean
is_not_admin = !$input.is_admin

// Complex combinations
can_purchase = ($input.age >= 18 || $input.has_guardian_consent) && 
               $input.account_verified && 
               !$input.account_suspended
```

## Conditional Operators

### Ternary (if/else)
```javascript
// Basic ternary
status = $input.is_active ? "Active" : "Inactive"

// Nested ternary
user_level = $input.points >= 1000 ? "Gold" :
             $input.points >= 500 ? "Silver" :
             $input.points >= 100 ? "Bronze" :
             "Basic"

// With calculations
shipping = $input.total >= 50 ? 0 :
           $input.weight > 10 ? 15.99 :
           9.99
```

### Null Coalescing
```javascript
// Use default if null/undefined
display_name = $input.nickname ?? $input.first_name ?? "Guest"

// Chain multiple fallbacks
contact_method = $input.mobile ?? $input.email ?? $input.phone ?? "No contact"

// With expressions
final_price = $input.sale_price ?? ($input.regular_price * 0.9) ?? 0
```

## Working with Arrays

### Array Operations
```javascript
// Create arrays
numbers = [1, 2, 3, 4, 5]
mixed = [$input.name, $input.age, $input.city]

// Array indexing
first_item = $var.items[0]
last_item = $var.items[-1]  // negative indexing

// Range operator
range = 1..10  // [1,2,3,4,5,6,7,8,9,10]

// Spread operator
combined = [1, 2, ...$var.more_numbers, 9, 10]
```

### Array with Filters
```javascript
// Get maximum value
highest_score = $var.scores | max

// Count items
item_count = $var.products | length

// Filter and count
active_count = $var.users | filter:"status,active" | length

// Sum with condition
total_revenue = $var.orders | filter:"status,completed" | sum:"amount"
```

## Working with Objects

### Object Creation
```javascript
// Simple object
user_data = {
  name: $input.name,
  age: $input.age,
  active: true
}

// Dynamic keys
response = {
  user_id: $input.id,
  timestamp: $env.current_timestamp,
  region: $input.country | lower,
  premium: $input.subscription == "premium"
}

// Spread operator
extended = {
  id: $input.id,
  ...$var.user_data,
  updated: true
}
```

## Text Operations

### String Concatenation
```javascript
// Concatenation with ~
full_name = $input.first_name ~ " " ~ $input.last_name

// Complex string building
greeting = "Hello " ~ ($input.name | upper) ~ "! " ~ 
          "You have " ~ $var.message_count ~ " new messages."

// URL building
api_url = $env.base_url ~ "/api/v1/users/" ~ $input.user_id ~ "/profile"
```

### String Filters
```javascript
// Transform text
clean_email = $input.email | lower | trim
formatted_phone = $input.phone | replace:" ","" | replace:"-",""

// Text validation
is_valid_email = $input.email | contains:"@" && $input.email | contains:"."

// Extract and format
initials = ($input.first_name | slice:0:1) ~ ($input.last_name | slice:0:1) | upper
```

## Variable Access

### Function Stack Variables
```javascript
// Access created variables
user_score = $var.calculated_score
processed_data = $var.api_response.data

// Complex variable paths
user_preference = $var.user_settings.preferences.theme
order_items = $var.cart_data.items[0].product_name
```

### Inputs and Authentication
```javascript
// API inputs
request_data = $input.user_data.email
query_param = $input.search_query

// Authentication data
current_user = $auth.user_id
user_roles = $auth.user.roles

// System environment
server_time = $env.current_timestamp
app_version = $env.app_version
```

## Common Patterns

### Validation Expressions
```javascript
// Email validation
is_valid_email = $input.email | contains:"@" && 
                $input.email | length > 5 && 
                $input.email | contains:"."

// Password strength
password_strength = $input.password | length >= 8 && 
                   $input.password | regex:"[A-Z]" && 
                   $input.password | regex:"[0-9]"

// Age verification
can_register = $input.age >= 13 && $input.age <= 120
```

### Data Formatting
```javascript
// Currency formatting
price_display = "$" ~ ($input.price | round:2)

// Date formatting
readable_date = $input.created_at | date:"F j, Y"

// Phone formatting
formatted_phone = "(" ~ ($input.phone | slice:0:3) ~ ") " ~ 
                  ($input.phone | slice:3:3) ~ "-" ~ 
                  ($input.phone | slice:6:4)
```

### Score Calculations
```javascript
// Weighted score
final_grade = ($var.homework * 0.3) + 
              ($var.midterm * 0.3) + 
              ($var.final_exam * 0.4)

// Rating average
avg_rating = ($var.ratings | sum) / ($var.ratings | length)

// Performance metric
efficiency = ($var.completed_tasks / $var.total_tasks) * 100 | round:1
```

## Try This

Create a dynamic pricing calculator:
1. Set up expression data type
2. Add quantity, base price, and user tier inputs
3. Build tiered discount logic
4. Include tax calculations
5. Format final output

## Pro Tips

💡 **Use Parentheses:** Control evaluation order with parentheses

💡 **Test in Playground:** Use expression playground to test complex expressions

💡 **Chain Filters:** Combine multiple filters with pipe operator

💡 **Default Values:** Use null coalescing for safer expressions

💡 **Performance:** Keep expressions simple for better performance

## Common Gotchas

### Type Coercion
```javascript
// Problem: Unexpected string concatenation
result = $input.num1 + $input.num2  // might be "12" + "34" = "1234"

// Solution: Convert to numbers
result = ($input.num1 | int) + ($input.num2 | int)  // 12 + 34 = 46
```

### Null Handling
```javascript
// Problem: Null reference errors
result = $input.user.profile.name  // fails if user or profile is null

// Solution: Safe navigation
result = $input.user?.profile?.name ?? "Unknown"
```

### Operator Precedence
```javascript
// Problem: Unexpected evaluation
result = 1 + 2 * 3  // = 7 (not 9)

// Solution: Use parentheses
result = (1 + 2) * 3  // = 9
```

## Next Steps

1. Practice basic expressions
2. Learn filter combinations
3. Build conditional logic
4. Test complex calculations
5. Optimize for performance

Remember: Expressions are powerful - start simple and build complexity as needed!