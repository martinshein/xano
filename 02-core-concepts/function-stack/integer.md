---
title: "Integer - Whole Numbers for Counting and IDs"
description: "Work with whole numbers for counting, quantities, IDs, and mathematical operations"
category: function-stack
subcategory: data-types
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- integer
- numbers
- whole-numbers
- counting
- ids
---

# Integer - Whole Numbers for Counting and IDs



## Quick Summary

> **What it is:** Data type for whole numbers (no decimals) like counts, IDs, quantities, and rankings
> 
> **When to use:** User IDs, product quantities, page numbers, counters, or any whole number data
> 
> **Key benefit:** Precise for counting and mathematical operations without decimal complexity
> 
> **Perfect for:** Non-developers building apps with inventory, user counts, or sequential numbering

## What You'll Learn

- Integer basics and ranges
- Common use cases
- Mathematical operations
- Type conversion
- Best practices
- Performance considerations

## Integer Basics

### What are Integers?
```javascript
// Valid integers
user_id = 12345
quantity = 50
page_number = 1
score = 0
negative_balance = -100
```

### Range and Limits
```javascript
// Safe integer range (recommended)
min_safe = -9007199254740991
max_safe = 9007199254740991

// Common practical ranges
user_id = 1234567      // User IDs
product_count = 500    // Inventory counts
priority_level = 5     // Rankings 1-10
```

## Integration Examples

### With n8n - Inventory Management
```javascript
// n8n sends product update
product_id = Input.product_id
quantity_change = Input.quantity_change  // Can be positive or negative

// Get current inventory
current_stock = Get_Record {
  table: "products",
  field_name: "id",
  field_value: product_id
}

if (current_stock) {
  // Calculate new quantity
  new_quantity = current_stock.quantity + quantity_change
  
  // Ensure quantity doesn't go negative
  if (new_quantity < 0) {
    return {
      error: "Insufficient stock",
      current_quantity: current_stock.quantity,
      requested_change: quantity_change,
      available_for_decrease: current_stock.quantity
    }
  }
  
  // Update inventory
  Edit_Record {
    id: product_id,
    quantity: new_quantity,
    updated_at: timestamp()
  }
  
  // Check if reorder needed
  reorder_alert = new_quantity <= current_stock.reorder_point
  
  if (reorder_alert) {
    Add_Record {
      table: "reorder_alerts",
      product_id: product_id,
      current_quantity: new_quantity,
      reorder_point: current_stock.reorder_point,
      suggested_order: current_stock.reorder_quantity
    }
  }
  
  return {
    success: true,
    product_id: product_id,
    old_quantity: current_stock.quantity,
    new_quantity: new_quantity,
    change_amount: quantity_change,
    reorder_needed: reorder_alert
  }
}
```

### With WeWeb - User Statistics Dashboard
```javascript
// WeWeb requests dashboard data
date_range = Input.days ?? 30

// Count new users in date range
new_users = Query_All_Records {
  table: "users",
  filter: {
    created_at: ">=" ~ (timestamp() - (date_range * 86400))
  }
}

new_user_count = new_users | length

// Count active users (logged in recently)
active_users = Query_All_Records {
  table: "users", 
  filter: {
    last_login: ">=" ~ (timestamp() - (7 * 86400))  // Last 7 days
  }
}

active_user_count = active_users | length

// Get total user count
total_users = Query_All_Records {
  table: "users"
}

total_user_count = total_users | length

// Calculate growth rate
previous_period_users = Query_All_Records {
  table: "users",
  filter: {
    created_at: "<" ~ (timestamp() - (date_range * 86400))
  }
}

previous_count = previous_period_users | length
growth_rate = previous_count > 0 ? 
              ((new_user_count / previous_count) * 100) | round:1 : 0

// Count orders by status
pending_orders = Query_All_Records {
  table: "orders",
  filter: {status: "pending"}
}

completed_orders = Query_All_Records {
  table: "orders", 
  filter: {status: "completed"}
}

return {
  user_stats: {
    total_users: total_user_count,
    new_users_period: new_user_count,
    active_users: active_user_count,
    growth_rate_percent: growth_rate
  },
  order_stats: {
    pending_orders: pending_orders | length,
    completed_orders: completed_orders | length,
    completion_rate: ((completed_orders | length) / 
                     ((pending_orders | length) + (completed_orders | length)) * 100) | round:1
  },
  period_days: date_range,
  generated_at: timestamp()
}
```

## Common Integer Uses

### User and Record IDs
```javascript
// Auto-incrementing user IDs
new_user = Add_Record {
  table: "users",
  email: Input.email,
  name: Input.name
}

user_id = new_user.id  // Integer ID assigned automatically

// Using ID for relationships
Add_Record {
  table: "user_profiles",
  user_id: user_id,
  bio: Input.bio,
  avatar_url: Input.avatar
}
```

### Quantities and Counts
```javascript
// Shopping cart quantities
cart_item = {
  product_id: Input.product_id,
  quantity: Input.quantity,  // Integer: 1, 2, 3, etc.
  user_id: Auth.user_id
}

// Validate quantity is positive integer
if (cart_item.quantity <= 0) {
  return {
    error: "Quantity must be a positive number",
    provided: cart_item.quantity
  }
}

// Check stock availability
product = Get_Record {
  table: "products",
  field_name: "id",
  field_value: cart_item.product_id
}

if (product.stock_quantity < cart_item.quantity) {
  return {
    error: "Insufficient stock",
    requested: cart_item.quantity,
    available: product.stock_quantity
  }
}
```

### Rankings and Scores
```javascript
// User scoring system
user_score = 0

// Award points for various actions
if (Input.action == "login") {
  user_score += 10
} else if (Input.action == "post_content") {
  user_score += 50
} else if (Input.action == "get_like") {
  user_score += 5
} else if (Input.action == "complete_profile") {
  user_score += 100
}

// Update user total score
current_user = Get_Record {
  table: "users",
  field_name: "id",
  field_value: Auth.user_id
}

new_total_score = current_user.total_score + user_score

Edit_Record {
  id: Auth.user_id,
  total_score: new_total_score
}

// Determine user level based on score
user_level = new_total_score >= 10000 ? 5 :
             new_total_score >= 5000 ? 4 :
             new_total_score >= 2000 ? 3 :
             new_total_score >= 500 ? 2 : 1

return {
  points_earned: user_score,
  total_score: new_total_score,
  user_level: user_level,
  action: Input.action
}
```

### Pagination
```javascript
// Page-based pagination
page = Input.page ?? 1  // Default to page 1
items_per_page = 20

// Calculate offset
offset = (page - 1) * items_per_page

// Get paginated results
products = Query_All_Records {
  table: "products",
  limit: items_per_page,
  offset: offset,
  sort: "created_at DESC"
}

// Get total count for pagination info
total_products = Query_All_Records {
  table: "products"
}

total_count = total_products | length
total_pages = Math.ceil(total_count / items_per_page)

return {
  data: products,
  pagination: {
    current_page: page,
    items_per_page: items_per_page,
    total_items: total_count,
    total_pages: total_pages,
    has_next_page: page < total_pages,
    has_previous_page: page > 1
  }
}
```

## Mathematical Operations

### Basic Arithmetic
```javascript
// Addition
total_items = cart_quantity + wishlist_quantity + saved_quantity

// Subtraction
remaining_stock = initial_stock - sold_quantity

// Multiplication
total_cost = item_price * quantity

// Division (results in decimal if not evenly divisible)
average_score = total_points / number_of_tests

// Integer division (floor result)
complete_batches = total_items / batch_size | floor
```

### Advanced Operations
```javascript
// Modulo (remainder)
remainder_items = total_items % batch_size

// Power
exponential_growth = base_users * (growth_rate ^ months)

// Absolute value
distance = Math.abs(point_a - point_b)

// Min/Max
final_quantity = Math.min(requested_quantity, available_stock)
priority_level = Math.max(1, Math.min(user_priority, 10))  // Clamp 1-10
```

## Type Conversion

### String to Integer
```javascript
// Convert string input to integer
age_string = Input.age  // "25"
age_integer = age_string | int  // 25

// Handle conversion errors
Try {
  user_age = Input.age | int
  
  if (user_age < 13 || user_age > 120) {
    return {
      error: "Age must be between 13 and 120",
      provided: user_age
    }
  }
} Catch (conversion_error) {
  return {
    error: "Invalid age format",
    provided: Input.age
  }
}
```

### Decimal to Integer
```javascript
// Round decimal to integer
price_decimal = 19.99
price_cents = (price_decimal * 100) | round  // 1999 cents

// Floor, ceil, round
score_decimal = 87.6
score_floor = score_decimal | floor    // 87
score_ceil = score_decimal | ceil      // 88
score_round = score_decimal | round    // 88
```

### Boolean to Integer
```javascript
// Convert boolean to integer (0 or 1)
is_active = true
active_flag = is_active | int  // 1

is_premium = false
premium_flag = is_premium | int  // 0

// Useful for counting
total_active_features = 
  (feature_a_enabled | int) + 
  (feature_b_enabled | int) + 
  (feature_c_enabled | int)
```

## Validation Patterns

### Range Validation
```javascript
// Validate integer within range
function validateRange(value, min, max, field_name) {
  if (value < min || value > max) {
    return {
      valid: false,
      error: field_name ~ " must be between " ~ min ~ " and " ~ max,
      provided: value
    }
  }
  return {valid: true, value: value}
}

// Usage
age_validation = validateRange(Input.age, 13, 120, "Age")
if (!age_validation.valid) {
  return age_validation
}

quantity_validation = validateRange(Input.quantity, 1, 100, "Quantity") 
if (!quantity_validation.valid) {
  return quantity_validation
}
```

### Positive Integer Check
```javascript
// Ensure positive integer
function validatePositiveInteger(value, field_name) {
  if (value <= 0) {
    return {
      valid: false,
      error: field_name ~ " must be a positive number",
      provided: value
    }
  }
  return {valid: true, value: value}
}
```

## Performance Considerations

### Efficient Counting
```javascript
// Use COUNT queries instead of loading all records
user_count = Direct_Database_Query {
  query: "SELECT COUNT(*) as count FROM users WHERE status = 'active'"
}

total_users = user_count[0].count  // More efficient than loading all users
```

### Index Usage
```javascript
// Queries on integer fields are fast with indexes
// Ensure indexes on frequently queried integer fields:
// - user_id
// - product_id  
// - status (if using integers for status)
// - created_at (timestamp integers)

fast_lookup = Get_Record {
  table: "orders",
  field_name: "user_id",  // Should be indexed
  field_value: user_id
}
```

## Try This

Create a simple counter system:
1. Add integer field for count
2. Increment on user action
3. Validate range (0-1000)
4. Display formatted count
5. Reset when needed

## Pro Tips

💡 **Validate Ranges:** Always check integer inputs are within expected ranges

💡 **Use for IDs:** Integers are perfect for database record IDs

💡 **Index Integer Fields:** Index frequently queried integer columns

💡 **Convert Safely:** Use filters for safe type conversion

💡 **Consider Limits:** Be aware of integer size limits for large numbers

## Common Gotchas

### String vs Integer
```javascript
// Problem: String arithmetic
user_input = "5"  // String
result = user_input + 3  // "53" (string concatenation)

// Solution: Convert to integer first
user_number = user_input | int  // 5
result = user_number + 3  // 8 (addition)
```

### Division Results
```javascript
// Problem: Integer division might return decimal
total_items = 7
batches = 3
items_per_batch = total_items / batches  // 2.333...

// Solution: Use floor for whole numbers
items_per_batch = (total_items / batches) | floor  // 2
remainder = total_items % batches  // 1
```

### Large Numbers
```javascript
// Problem: Very large integers might lose precision
huge_number = 9007199254740992  // Might be imprecise

// Solution: Use strings for very large IDs or numbers
large_id = "12345678901234567890"  // Keep as string
```

### Null vs Zero
```javascript
// Problem: Treating null as zero
quantity = Input.quantity  // might be null
total = quantity * price   // null * price = null

// Solution: Handle null values
quantity = Input.quantity ?? 0  // Default to 0 if null
total = quantity * price
```

## Next Steps

1. Practice integer validation
2. Build counting systems
3. Implement pagination
4. Create scoring mechanisms
5. Use integers for efficient queries

Remember: Integers are fundamental for counting, IDs, and whole number calculations!