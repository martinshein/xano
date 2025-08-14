---
title: "Decimal Data Type - Precision Numbers"
description: "Work with decimal numbers for accurate financial and measurement calculations"
category: function-stack
subcategory: data-types
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- decimal
- data-types
- numbers
- precision
- calculations
---

# Decimal Data Type - Precision Numbers



## Quick Summary

> **What it is:** Numbers with decimal points for precise calculations (1.99, 3.14159, 0.01)
> 
> **When to use:** Financial calculations, measurements, percentages, or any math requiring precision
> 
> **Key benefit:** Maintains accuracy in calculations without rounding errors
> 
> **Perfect for:** Non-developers handling money, measurements, or scientific data

## What You'll Learn

- Understanding decimal precision
- When to use decimals vs integers
- Common decimal operations
- Formatting for display
- Avoiding calculation errors

## What Are Decimals?

Decimals are numbers with fractional parts:
- **Money:** $19.99, €45.50
- **Measurements:** 5.5 inches, 2.75 kg
- **Percentages:** 15.5%, 99.9%
- **Coordinates:** 40.7128° N

## Decimal vs Integer

### Use Decimals For:
```javascript
price = 19.99        // Money
weight = 2.5         // Measurements
percentage = 15.75   // Percentages
rating = 4.8         // Ratings
```

### Use Integers For:
```javascript
quantity = 5         // Whole items
user_id = 12345     // IDs
age = 25            // Years
count = 100         // Counts
```

## Creating Decimals

### In Variables
```javascript
// Direct assignment
price = 29.99
tax_rate = 0.08

// From calculations
subtotal = quantity * price
tax = subtotal * tax_rate
total = subtotal + tax
```

### In Database
```sql
// Field type: Decimal
price DECIMAL(10,2)  // Up to 10 digits, 2 after decimal
latitude DECIMAL(10,8)  // GPS precision
```

## Common Operations

### Basic Math
```javascript
// Addition
total = price + shipping  // 19.99 + 5.00 = 24.99

// Subtraction
change = payment - total  // 30.00 - 24.99 = 5.01

// Multiplication
subtotal = price * quantity  // 19.99 * 3 = 59.97

// Division
unit_price = total / quantity  // 59.97 / 3 = 19.99
```

### Rounding
```javascript
// Round to 2 decimal places
price = 19.999
rounded = price | round(2)  // 20.00

// Round up (ceiling)
shipping = 4.01
rounded_up = shipping | ceil  // 5

// Round down (floor)
discount = 2.99
rounded_down = discount | floor  // 2
```

## Integration Examples

### With n8n - Price Calculations
```javascript
// n8n sends order data
order = Webhook.data

// Calculate with decimals
subtotal = 0.00
For Each item in order.items {
  item_total = item.price * item.quantity
  subtotal = subtotal + item_total
}

// Apply tax
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax

// Round for display
final_total = total | round(2)
```

### With WeWeb - Form Validation
```javascript
// WeWeb form input
input_price = Input.price

// Validate decimal
if (input_price < 0.01) {
  error = "Price must be at least $0.01"
}

if (input_price > 99999.99) {
  error = "Price exceeds maximum"
}

// Format for storage
formatted_price = input_price | round(2)
```

## Currency Handling

### Best Practices
```javascript
// Store as decimal
price_decimal = 19.99

// Display with formatting
display_price = "$" + price_decimal | round(2)

// Calculate precisely
subtotal = 19.99 * 3  // 59.97
discount = subtotal * 0.10  // 5.997
final = subtotal - discount  // 53.973
display = final | round(2)  // 53.97
```

### Multi-Currency
```javascript
// Store exchange rates
rates = {
  USD_to_EUR: 0.85,
  USD_to_GBP: 0.73
}

// Convert currencies
usd_amount = 100.00
eur_amount = usd_amount * rates.USD_to_EUR
eur_display = eur_amount | round(2)  // 85.00
```

## Percentage Calculations

### Working with Percentages
```javascript
// Store as decimal
discount_percent = 15  // 15%
discount_decimal = discount_percent / 100  // 0.15

// Apply percentage
original_price = 49.99
discount_amount = original_price * discount_decimal
final_price = original_price - discount_amount
```

### Tax Calculations
```javascript
// Multiple tax rates
federal_tax = 0.05  // 5%
state_tax = 0.08    // 8%
total_tax_rate = federal_tax + state_tax  // 0.13

// Apply taxes
subtotal = 100.00
tax_amount = subtotal * total_tax_rate  // 13.00
total = subtotal + tax_amount  // 113.00
```

## Common Patterns

### Shopping Cart Total
```javascript
cart_items = [
  {price: 19.99, quantity: 2},
  {price: 5.50, quantity: 3},
  {price: 99.00, quantity: 1}
]

subtotal = 0.00
For Each item in cart_items {
  subtotal += item.price * item.quantity
}

shipping = 10.00
tax = subtotal * 0.08
total = subtotal + shipping + tax
```

### Discount Tiers
```javascript
order_total = 150.00
discount = 0.00

if (order_total >= 100) {
  discount = 0.10  // 10% off
} else if (order_total >= 50) {
  discount = 0.05  // 5% off
}

discount_amount = order_total * discount
final_total = order_total - discount_amount
```

## Precision Issues

### Common Problems
```javascript
// Floating point errors
0.1 + 0.2  // May equal 0.30000000000000004

// Solution: Round when displaying
result = (0.1 + 0.2) | round(2)  // 0.30
```

### Safe Calculations
```javascript
// For money, work in cents
price_cents = 1999  // $19.99 in cents
quantity = 3
total_cents = price_cents * quantity
total_dollars = total_cents / 100  // 59.97
```

## Try This

Create a price calculator:
1. Create decimal variable for price
2. Add quantity input
3. Calculate subtotal
4. Apply 10% discount if > $50
5. Add 8% tax
6. Round and display total

## Pro Tips

💡 **Always Round Display:** Round to 2 decimals for currency display

💡 **Store Full Precision:** Keep all decimals in database, round only for display

💡 **Use Cents for Money:** Store 1999 instead of 19.99 to avoid errors

💡 **Validate Ranges:** Check min/max values for decimal inputs

💡 **Test Edge Cases:** Check calculations with 0, negative, and very large numbers

## Common Gotchas

### Division by Zero
```javascript
// Problem
average = total / count  // Error if count is 0

// Solution
if (count > 0) {
  average = total / count
} else {
  average = 0
}
```

### String Concatenation
```javascript
// Problem
price = "19" + ".99"  // "19.99" as text, not number

// Solution
price = to_decimal("19.99")  // 19.99 as decimal
```

## Next Steps

1. Practice decimal calculations
2. Build a price calculator
3. Handle multiple currencies
4. Implement percentage discounts
5. Create financial reports

Remember: Decimals give you precision for real-world calculations - use them whenever accuracy matters!