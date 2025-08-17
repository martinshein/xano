---
title: Integer Data Type Reference
description: Complete guide to working with integer numbers in Xano - whole numbers for counting, IDs, and precise calculations in no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- integer
- data-types
- numbers
- whole-numbers
- counting
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: beginner
has_code_examples: true
related_docs:
- decimal.md
- 08-reference/filters/math.md
- 02-core-concepts/function-stack/math.md
---

# Integer Data Type Reference

## 📋 **Quick Summary**
Integer values in Xano represent whole numbers without decimal places. Perfect for IDs, counters, quantities, status codes, and precise counting operations in no-code platforms like n8n, WeWeb, and Make.com.

## What You'll Learn
- Integer number syntax and operations
- Working with whole number calculations
- ID generation and management
- Integration patterns for no-code platforms
- Counting and enumeration techniques
- Common integer use cases

## Integer Number Format

Integers are whole numbers without decimal points:

### Basic Integer Syntax

**Positive Integers:**
```javascript
1
42
1000
999999
```

**Negative Integers:**
```javascript
-1
-50
-999
```

**Zero:**
```javascript
0
```

**In Objects:**
```javascript
{
  "user_id": 12345,
  "quantity": 3,
  "status_code": 200,
  "retry_count": 0,
  "max_attempts": 5
}
```

## 🔄 **No-Code Platform Integration**

### n8n Integration
```javascript
// In n8n Set node - counter operations
{
  "current_page": "{{$json.page || 1}}",
  "items_per_page": 20,
  "total_items": "{{$json.count}}",
  "total_pages": "{{Math.ceil($json.count / 20)}}"
}
```

### WeWeb Integration
```javascript
// WeWeb formula for pagination
Math.ceil(totalItems / itemsPerPage)
```

### Make.com Integration
```javascript
// Make.com increment counter
{
  "counter": "{{add(get(counter); 1)}}",
  "batch_size": 50,
  "processed_items": "{{add(get(processed_items); get(batch_size))}}"
}
```

## Common Integer Use Cases

### Database IDs and Keys
```javascript
{
  "user_id": 789,
  "product_id": 12345,
  "order_id": 98765,
  "category_id": 5,
  "brand_id": 23
}
```

### Quantities and Counters
```javascript
{
  "inventory": {
    "in_stock": 150,
    "reserved": 25,
    "available": 125,
    "reorder_level": 50
  },
  "metrics": {
    "page_views": 1247,
    "unique_visitors": 89,
    "bounce_rate": 35
  }
}
```

### Status and Configuration
```javascript
{
  "http_status": 200,
  "error_code": 0,
  "retry_attempts": 3,
  "timeout_seconds": 30,
  "max_file_size": 10485760
}
```

## 💡 **Try This: Build a Counter System**

Create a comprehensive counting and tracking system:

```javascript
{
  "user_activity": {
    "user_id": 456,
    "login_count": 47,
    "posts_created": 12,
    "comments_made": 89,
    "likes_given": 156,
    "points_earned": 2340
  },
  "system_metrics": {
    "total_users": 1567,
    "active_sessions": 23,
    "api_calls_today": 89456,
    "errors_logged": 3
  },
  "pagination": {
    "current_page": 1,
    "items_per_page": 25,
    "total_items": 1567,
    "total_pages": 63
  }
}
```

## Integer Operations

### Arithmetic Operations
```javascript
// Addition
10 + 5 = 15

// Subtraction
20 - 8 = 12

// Multiplication
6 * 7 = 42

// Division (returns integer if divisible)
20 / 4 = 5

// Modulo (remainder)
17 % 5 = 2
```

### Comparison Operations
```javascript
// Greater than
10 > 5 // true

// Less than or equal
5 <= 5 // true

// Equal
10 == 10 // true

// Not equal
8 != 9 // true
```

### Built-in Math Functions
```javascript
// Absolute value
abs(-42) // 42

// Minimum/Maximum
min(5, 10, 3) // 3
max(5, 10, 3) // 10

// Power
pow(2, 3) // 8

// Square root (may return decimal)
sqrt(16) // 4
```

## ⚠️ **Common Mistakes to Avoid**

1. **Division Results**: Integer division may produce decimal results
2. **Overflow**: Very large integers may exceed limits
3. **String Concatenation**: `"5" + "3" = "53"` not `8`
4. **Type Conversion**: Ensure proper integer parsing

### Type Conversion Examples
```javascript
// String to integer
parseInt("123") // 123
parseInt("123.45") // 123
parseInt("abc") // NaN

// Ensure integer result
Math.floor(123.89) // 123
Math.ceil(123.1) // 124
Math.round(123.5) // 124
```

## 🚀 **Pro Tips**

### ID Generation
```javascript
// Auto-incrementing ID
{
  "next_id": "SELECT MAX(id) + 1 FROM table_name",
  "uuid_alternative": "Use create_uid() for unique strings"
}

// Timestamp-based ID
{
  "timestamp_id": 1642781234567 // Unix timestamp in milliseconds
}
```

### Pagination Logic
```javascript
// Calculate pagination values
function calculatePagination(total, page, perPage) {
  return {
    "current_page": page,
    "per_page": perPage,
    "total_items": total,
    "total_pages": Math.ceil(total / perPage),
    "offset": (page - 1) * perPage,
    "has_next": page < Math.ceil(total / perPage),
    "has_prev": page > 1
  }
}
```

### Counter Increment
```javascript
// Safe counter increment
UPDATE counters 
SET count = count + 1 
WHERE id = 123

// Batch increment
UPDATE products 
SET view_count = view_count + 1 
WHERE id IN (1, 2, 3, 4, 5)
```

## Integration Best Practices

### For n8n Workflows
- Use parseInt() for string to integer conversion
- Implement counters with database increment operations
- Handle pagination with proper offset calculations

### For WeWeb Apps
- Bind integer values to numeric input components
- Use integer fields for quantity selectors
- Implement proper validation for integer inputs

### For Make.com Scenarios
- Use add() and subtract() functions for integer math
- Implement loop counters for batch processing
- Handle integer arrays with iterator modules

## Database Configuration

### Integer Field Setup
```javascript
// Integer database field
{
  "field_name": "quantity",
  "field_type": "integer",
  "default_value": 0,
  "min_value": 0,
  "max_value": 999999,
  "required": true
}
```

### Auto-Increment Primary Key
```javascript
// Primary key configuration
{
  "field_name": "id",
  "field_type": "integer",
  "auto_increment": true,
  "primary_key": true
}
```

## Validation Patterns

### Input Validation
```javascript
// Validate integer input
function validateInteger(value, min = null, max = null) {
  const int = parseInt(value);
  if (isNaN(int)) return false;
  if (min !== null && int < min) return false;
  if (max !== null && int > max) return false;
  return true;
}
```

### Range Checking
```javascript
// Check if integer is in valid range
function isInRange(value, min, max) {
  return value >= min && value <= max;
}
```

## API Response Patterns

### Clean Integer API Response
```javascript
{
  "success": true,
  "data": {
    "user_id": 789,
    "total_orders": 15,
    "points_balance": 2450
  },
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 156,
    "pages": 8
  },
  "meta": {
    "request_id": 12345,
    "timestamp": 1642781234
  }
}
```

## Related Functions
- [Decimal Data Type](decimal.md) - Working with decimal numbers
- [Math Filters](../filters/math.md) - Mathematical operations
- [Math Functions](../../02-core-concepts/function-stack/math.md) - Advanced calculations

Integers are fundamental for counting, identification, and precise whole number operations in Xano. Use them effectively to build robust applications with accurate data tracking and seamless no-code platform integration.