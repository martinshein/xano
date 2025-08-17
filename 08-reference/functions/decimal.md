---
title: Decimal Data Type Reference
description: Complete guide to working with decimal numbers in Xano - precise floating-point arithmetic for financial calculations and no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- decimal
- data-types
- numbers
- floating-point
- financial-calculations
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: beginner
has_code_examples: true
related_docs:
- integer.md
- 08-reference/filters/math.md
- 02-core-concepts/function-stack/math.md
---

# Decimal Data Type Reference

## 📋 **Quick Summary**
Decimal values in Xano handle precise floating-point numbers with decimal places. Essential for financial calculations, measurements, ratings, and precise mathematical operations in no-code platforms like n8n, WeWeb, and Make.com.

## What You'll Learn
- Decimal number syntax and precision
- Working with floating-point arithmetic
- Financial calculation best practices
- Integration patterns for no-code platforms
- Rounding and formatting operations
- Common decimal use cases

## Decimal Number Format

Decimal numbers contain a decimal point and fractional digits:

### Basic Decimal Syntax

**Simple Decimals:**
```javascript
29.99
3.14159
0.5
-12.75
```

**Scientific Notation:**
```javascript
1.23e4    // 12300
5.67e-3   // 0.00567
```

**Financial Values:**
```javascript
{
  "product_price": 49.99,
  "tax_rate": 0.08,
  "discount_percent": 15.5,
  "shipping_cost": 12.95
}
```

## 🔄 **No-Code Platform Integration**

### n8n Integration
```javascript
// In n8n Set node - calculate totals
{
  "subtotal": "{{$json.price * $json.quantity}}",
  "tax": "{{($json.price * $json.quantity) * $json.tax_rate}}",
  "total": "{{($json.price * $json.quantity) * (1 + $json.tax_rate)}}"
}
```

### WeWeb Integration
```javascript
// WeWeb formula for price calculations
Math.round((price * quantity * (1 + tax_rate)) * 100) / 100
```

### Make.com Integration
```javascript
// Make.com mathematical operations
{
  "price_with_tax": "{{parseFloat(price) * (1 + parseFloat(tax_rate))}}",
  "formatted_price": "${{round(parseFloat(price); 2)}}"
}
```

## Common Decimal Use Cases

### E-commerce Pricing
```javascript
{
  "product_id": 123,
  "base_price": 99.99,
  "sale_price": 79.99,
  "cost": 45.50,
  "profit_margin": 0.43,
  "tax_rate": 0.0875,
  "shipping_weight": 2.5
}
```

### Financial Calculations
```javascript
{
  "loan_amount": 250000.00,
  "interest_rate": 0.035,
  "monthly_payment": 1123.89,
  "balance_remaining": 247876.11
}
```

### Measurements and Ratings
```javascript
{
  "user_rating": 4.7,
  "product_weight": 1.25,
  "dimensions": {
    "length": 10.5,
    "width": 7.25,
    "height": 3.75
  },
  "temperature": 98.6
}
```

## 💡 **Try This: Build a Price Calculator**

Create a comprehensive pricing system:

```javascript
{
  "item": {
    "base_price": 89.99,
    "quantity": 2,
    "discount_rate": 0.15
  },
  "calculations": {
    "subtotal": 179.98,
    "discount_amount": 26.997,
    "discounted_total": 152.983,
    "tax_rate": 0.08,
    "tax_amount": 12.24,
    "final_total": 165.22
  },
  "formatted": {
    "subtotal": "$179.98",
    "savings": "$27.00",
    "tax": "$12.24",
    "total": "$165.22"
  }
}
```

## Decimal Operations

### Arithmetic Operations
```javascript
// Addition
12.50 + 7.25 = 19.75

// Multiplication
29.99 * 1.08 = 32.3892

// Division
100.00 / 3 = 33.333333...

// Rounding
round(33.333333, 2) = 33.33
```

### Built-in Math Functions
```javascript
// Round to specific decimal places
round(123.456, 2) // 123.46

// Ceiling (round up)
ceil(123.1) // 124

// Floor (round down)
floor(123.9) // 123

// Absolute value
abs(-45.67) // 45.67
```

## ⚠️ **Common Mistakes to Avoid**

1. **Floating Point Precision**: Be aware of precision limitations
2. **Currency Formatting**: Always round financial calculations appropriately
3. **Division by Zero**: Check for zero denominators
4. **String vs Number**: Ensure proper type conversion

### Precision Issues Example
```javascript
// Problem: Floating point precision
0.1 + 0.2 = 0.30000000000000004

// Solution: Round appropriately
round(0.1 + 0.2, 2) = 0.30
```

## 🚀 **Pro Tips**

### Financial Best Practices
```javascript
// Good: Store monetary values as integers (cents)
{
  "price_cents": 2999,  // $29.99
  "display_price": 29.99
}

// Better: Use proper rounding for currency
{
  "price": parseFloat((price_cents / 100).toFixed(2))
}
```

### Database Field Configuration
```javascript
// Decimal field setup
{
  "field_name": "product_price",
  "field_type": "decimal",
  "precision": 10,    // Total digits
  "scale": 2,         // Decimal places
  "default_value": 0.00
}
```

### Validation Patterns
```javascript
// Validate decimal input
function validatePrice(value) {
  const decimal = parseFloat(value);
  return !isNaN(decimal) && decimal >= 0 && 
         (decimal * 100) % 1 === 0; // Max 2 decimal places
}
```

## Integration Best Practices

### For n8n Workflows
- Use parseFloat() for string to decimal conversion
- Implement proper error handling for invalid numbers
- Round financial calculations to 2 decimal places

### For WeWeb Apps
- Use computed properties for decimal calculations
- Format decimals for display using toFixed()
- Implement input validation for decimal fields

### For Make.com Scenarios
- Use round() function for precise calculations
- Handle null/empty decimal values gracefully
- Format currency displays consistently

## Decimal Formatting

### Display Formatting
```javascript
// Currency formatting
const price = 1234.567;
price.toFixed(2) // "1234.57"
"$" + price.toFixed(2) // "$1234.57"

// Percentage formatting
const rate = 0.0875;
(rate * 100).toFixed(2) + "%" // "8.75%"

// Number formatting with commas
const large_number = 12345.67;
large_number.toLocaleString() // "12,345.67"
```

### API Response Patterns
```javascript
// Clean decimal API response
{
  "success": true,
  "data": {
    "product": {
      "price": 89.99,
      "sale_price": 69.99,
      "savings": 20.00,
      "tax_rate": 0.08
    }
  },
  "formatted": {
    "price": "$89.99",
    "sale_price": "$69.99",
    "you_save": "$20.00 (22%)"
  }
}
```

## Related Functions
- [Integer Data Type](integer.md) - Working with whole numbers
- [Math Filters](../filters/math.md) - Mathematical operations
- [Math Functions](../../02-core-concepts/function-stack/math.md) - Advanced calculations

Decimal numbers are essential for precise calculations in Xano. Master these patterns to build reliable financial applications and measurement systems that work seamlessly with your no-code platforms.