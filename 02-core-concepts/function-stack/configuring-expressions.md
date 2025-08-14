---
title: "Expression Builder - Smart Logic Without Code"
description: "Build complex conditional logic visually using Xano's expression builder"
category: function-stack
subcategory: expressions
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- expressions
- conditionals
- logic
- operators
- no-code
---

# Expression Builder - Smart Logic Without Code



## Quick Summary

> **What it is:** Visual interface for building conditional logic and expressions without writing code
> 
> **When to use:** Creating if/then logic, filtering data, validating inputs, or making decisions in your backend
> 
> **Key benefit:** Build complex business logic with simple drag-and-drop components
> 
> **Perfect for:** Non-developers who need to create sophisticated conditional rules and data validation

## What You'll Learn

- Understanding expression components
- Building conditional statements
- Using different operators
- Combining multiple conditions
- Working with AND/OR logic

## Expression Builder Anatomy

Think of expressions like a decision tree that asks questions about your data:

### The Four Components

1. **Conditional Type (AND/OR)**
   - How conditions relate to each other
   - AND = all must be true
   - OR = at least one must be true

2. **Left Value**
   - What you're checking
   - Usually a field or variable
   - The "question" part

3. **Operator**
   - How to compare
   - Equals, greater than, contains, etc.
   - The "test" part

4. **Right Value**
   - What to compare against
   - Can be static or dynamic
   - The "answer" part

## Available Operators

### Basic Comparisons

```javascript
// Equals (==)
user.role == "admin"

// Not Equals (!=)
status != "deleted"

// Greater Than (>)
age > 18

// Less Than (<)
price < 100

// Greater/Less Than or Equal (≥, ≤)
quantity >= 1
discount <= 50
```

### Type-Safe Comparisons

```javascript
// Strict Equals (===)
// Checks value AND type
var_1 === 123  // Must be number 123

// Strict Not Equals (!==)
input !== "0"  // Not string "0"
```

### Text Operations

```javascript
// LIKE (case-insensitive equals)
email LIKE "John@Example.com"
// Matches: john@example.com

// INCLUDES (partial match)
description INCLUDES "discount"
// Matches: "Special discount offer"

// DOES NOT INCLUDE
title DOES NOT INCLUDE "draft"
```

### Array Operations

```javascript
// IN (value in array)
user_id IN [1, 2, 3, 4]

// NOT IN
status NOT IN ["deleted", "archived"]

// OVERLAPS (arrays share values)
user_tags OVERLAPS ["premium", "vip"]

// CONTAINS (exact schema match)
permissions CONTAINS {"read": true}
```

### Pattern Matching

```javascript
// REGEX MATCHES
email REGEX MATCHES "^[a-z]+@company\.com$"

// REGEX DOES NOT MATCH
phone REGEX DOES NOT MATCH "[a-zA-Z]"
```

## Building Complex Logic

### Combining Conditions

```javascript
// Multiple AND conditions
age >= 18 AND
country == "US" AND
verified == true

// Multiple OR conditions
role == "admin" OR
role == "manager" OR
role == "owner"

// Mixed AND/OR
(role == "user" AND verified == true) OR
(role == "admin")
```

### Nested Expressions

```javascript
// Check user access
IF user.subscription == "premium" AND
   user.payment_status == "active" AND
   (user.credits > 0 OR user.unlimited == true)
THEN
   // Allow access
```

## Integration Examples

### With n8n

```javascript
// n8n sends user data
Webhook Input: {
  email: "user@example.com",
  purchase_amount: 150
}

// Xano expression checks
IF purchase_amount > 100 AND
   email INCLUDES "@company.com"
THEN
   Apply corporate discount
```

### With WeWeb

```javascript
// WeWeb form validation
Form Input: {
  age: user_age,
  country: user_country
}

// Xano validates
IF age >= 21 OR
   (age >= 18 AND country != "US")
THEN
   Allow registration
```

## Common Patterns

### User Authentication

```javascript
// Check login validity
email EXISTS AND
password EXISTS AND
account_status != "suspended"
```

### Data Validation

```javascript
// Validate order
quantity > 0 AND
quantity <= stock_available AND
price >= minimum_price
```

### Access Control

```javascript
// Check permissions
(user.role == "admin") OR
(user.role == "editor" AND resource.owner == user.id) OR
(resource.public == true)
```

### Business Rules

```javascript
// Apply discount rules
IF order_total >= 100 AND
   customer.member_since < "2023-01-01" AND
   customer.orders_count > 5
THEN
   discount = 20
```

## Database vs Regular Expressions

### Database Query Operators
- Optimized for SQL queries
- Limited to database-compatible operations
- Better performance for large datasets

### Function Stack Operators
- More flexible options
- Can use complex logic
- Works with any data type

## Best Practices

### Keep It Simple

```javascript
// Good: Clear and readable
status == "active" AND verified == true

// Avoid: Overly complex
(status == "active" OR status == "pending") AND 
(verified == true OR admin_override == true) AND
(created_date > yesterday OR priority == "high")
```

### Use Meaningful Names

```javascript
// Good
user_age >= minimum_age

// Avoid
var_1 >= var_2
```

### Group Related Logic

```javascript
// Group authentication checks
(email EXISTS AND password EXISTS) AND
// Group permission checks
(role == "admin" OR has_permission == true)
```

## Common Gotchas

### Type Mismatches

```javascript
// Problem: Comparing different types
"123" === 123  // False (string vs number)

// Solution: Use type conversion
to_int("123") === 123  // True
```

### Case Sensitivity

```javascript
// Problem: Case mismatch
email == "John@Example.com"  // Won't match john@example.com

// Solution: Use LIKE
email LIKE "John@Example.com"  // Matches any case
```

### Null Values

```javascript
// Problem: Null comparison
field == null  // May not work as expected

// Solution: Check existence
field EXISTS AND field != null
```

## Try This

Build a user validation expression:
1. Add expression builder to function
2. Check email is not empty
3. Verify age is 18 or older
4. Ensure country is in allowed list
5. Test with sample data

## Pro Tips

💡 **Use Update Payload:** Always click to sync visual changes with the actual query

💡 **Start Simple:** Build one condition at a time, then combine

💡 **Test Edge Cases:** Check with null, empty, and unexpected values

💡 **Document Complex Logic:** Add descriptions to explain business rules

💡 **Reuse Patterns:** Save common expressions as snippets

## Performance Tips

- Put most restrictive conditions first
- Use indexed fields for database queries
- Avoid REGEX when simpler operators work
- Combine related checks

## Next Steps

1. Practice with simple comparisons
2. Build multi-condition logic
3. Create validation rules
4. Implement access control
5. Optimize for performance

Remember: The expression builder lets you create enterprise-grade business logic without writing a single line of code!