---
title: "Math Operations - Calculations and Number Processing"
description: "Perform mathematical calculations and number manipulations in your Xano function stacks"
category: function-stack
subcategory: data-manipulation
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- math
- calculations
- numbers
- arithmetic
- formulas
---

# Math Operations - Calculations and Number Processing

## Quick Summary

> **What it is:** A comprehensive set of mathematical functions for performing calculations in your function stacks
> 
> **When to use:** Whenever you need arithmetic operations, percentage calculations, rounding, or complex mathematical formulas
> 
> **Key benefit:** Visual interface for building calculations without writing complex code
> 
> **Common uses:** Pricing calculations, statistics, financial computations, data analysis

## What You'll Learn

- Basic arithmetic operations
- Working with decimals and rounding
- Percentage and financial calculations
- Statistical functions
- Complex formula building

## Basic Arithmetic

### Addition and Subtraction

```javascript
// Simple addition
total = price + tax + shipping

// Subtraction
remaining = inventory - quantity_sold

// Combined operations
net_profit = revenue - (costs + expenses)
```

### Multiplication and Division

```javascript
// Multiplication
line_total = price * quantity

// Division
average = total / count

// Percentage calculation
tax_amount = subtotal * (tax_rate / 100)
```

### Order of Operations

```javascript
// Parentheses control order
result = (a + b) * c  // Different from a + b * c

// Complex calculations
final_price = (base_price * quantity - discount) * (1 + tax_rate)
```

## Working with Decimals

### Rounding Functions

```javascript
// Round to nearest integer
ROUND(19.7) = 20
ROUND(19.4) = 19

// Round up (ceiling)
CEIL(19.1) = 20

// Round down (floor)
FLOOR(19.9) = 19

// Round to specific decimal places
ROUND(19.756, 2) = 19.76
```

### Precision Control

```javascript
// Money calculations (2 decimal places)
price = ROUND(raw_price * discount_rate, 2)

// Percentage display (1 decimal)
completion = ROUND((done / total) * 100, 1) + "%"

// Scientific precision (4 decimals)
measurement = ROUND(sensor_value, 4)
```

## Financial Calculations

### Pricing Examples

```javascript
// Discount calculation
discount_amount = original_price * (discount_percent / 100)
sale_price = original_price - discount_amount

// Markup calculation
selling_price = cost * (1 + markup_percentage / 100)

// Tax calculation
tax = subtotal * tax_rate
total = subtotal + tax
```

### Commission and Fees

```javascript
// Tiered commission
IF (sales < 10000) {
  commission = sales * 0.05  // 5%
} ELSE IF (sales < 50000) {
  commission = sales * 0.08  // 8%
} ELSE {
  commission = sales * 0.10  // 10%
}

// Transaction fees
processing_fee = MAX(transaction_amount * 0.029 + 0.30, 0.50)
net_amount = transaction_amount - processing_fee
```

### Interest Calculations

```javascript
// Simple interest
interest = principal * rate * time

// Compound interest
final_amount = principal * POWER(1 + rate, periods)

// Monthly payment
payment = principal * (rate * POWER(1 + rate, months)) / (POWER(1 + rate, months) - 1)
```

## Statistical Functions

### Averages and Totals

```javascript
// Sum array of numbers
total = SUM(numbers_array)

// Average (mean)
average = AVG(scores_array)

// Count non-null values
count = COUNT(valid_entries)
```

### Min/Max Operations

```javascript
// Find minimum
lowest_price = MIN(price_array)

// Find maximum
highest_score = MAX(scores)

// Clamp value to range
clamped = MAX(MIN(value, upper_limit), lower_limit)
```

### Advanced Statistics

```javascript
// Median (middle value)
median_value = MEDIAN(data_array)

// Standard deviation
std_dev = STDDEV(measurements)

// Variance
variance = VARIANCE(data_points)
```

## Practical Examples

### Example 1: E-commerce Cart

```javascript
// Calculate cart totals
subtotal = 0
total_items = 0

FOR EACH item IN cart {
  line_total = item.price * item.quantity
  subtotal = subtotal + line_total
  total_items = total_items + item.quantity
}

// Apply discounts
discount = (subtotal > 100) ? subtotal * 0.1 : 0
after_discount = subtotal - discount

// Calculate tax and shipping
tax = after_discount * 0.08
shipping = (after_discount > 50) ? 0 : 9.99

// Final total
grand_total = ROUND(after_discount + tax + shipping, 2)
```

### Example 2: Analytics Dashboard

```javascript
// Calculate metrics
conversion_rate = ROUND((conversions / visitors) * 100, 2)
average_order_value = ROUND(total_revenue / order_count, 2)
cart_abandonment_rate = ROUND((abandoned / total_carts) * 100, 1)

// Growth calculations
growth_amount = current_month - previous_month
growth_percentage = ROUND((growth_amount / previous_month) * 100, 1)

// Projections
daily_average = total_month / days_elapsed
projected_month_end = daily_average * days_in_month
```

### Example 3: Inventory Management

```javascript
// Reorder point calculation
reorder_point = (daily_usage * lead_time) + safety_stock

// Economic order quantity
eoq = SQRT((2 * annual_demand * order_cost) / holding_cost)

// Stock value
total_value = SUM(
  FOR EACH product IN inventory {
    product.quantity * product.unit_cost
  }
)
```

## Advanced Math Functions

### Power and Roots

```javascript
// Square and cube
squared = POWER(number, 2)
cubed = POWER(number, 3)

// Square root
sqrt_value = SQRT(number)

// Nth root
nth_root = POWER(number, 1/n)
```

### Logarithms

```javascript
// Natural logarithm
ln_value = LN(number)

// Base 10 logarithm
log_value = LOG10(number)

// Custom base
log_base = LN(number) / LN(base)
```

### Trigonometry

```javascript
// Basic trig functions
sine = SIN(angle_radians)
cosine = COS(angle_radians)
tangent = TAN(angle_radians)

// Convert degrees to radians
radians = degrees * (PI() / 180)
```

## Integration Patterns

### With n8n

```javascript
// Calculate webhook metrics
processing_time = timestamp_end - timestamp_start
requests_per_second = request_count / time_window
average_response = ROUND(total_response_time / request_count, 3)

// Return calculated data
Return {
  metrics: {
    rps: requests_per_second,
    avg_response_ms: average_response * 1000,
    success_rate: (success_count / total_count) * 100
  }
}
```

### With WeWeb

```javascript
// Format numbers for display
display_price = "$" + ROUND(price, 2)
percentage_display = ROUND(value * 100, 1) + "%"
formatted_large = FORMAT_NUMBER(big_number, "#,###")

// Progress calculations
progress_percentage = MIN(ROUND((current / target) * 100, 0), 100)
remaining = MAX(target - current, 0)
```

## Common Mistakes to Avoid

1. **Division by Zero**
   ```javascript
   // Bad: Can cause error
   average = total / count
   
   // Good: Check first
   average = (count > 0) ? total / count : 0
   ```

2. **Floating Point Precision**
   ```javascript
   // Bad: 0.1 + 0.2 = 0.30000000000000004
   total = 0.1 + 0.2
   
   // Good: Round for display
   total = ROUND(0.1 + 0.2, 2)  // 0.3
   ```

3. **Integer Division**
   ```javascript
   // Bad: Integer division loses precision
   percentage = (5 / 10) * 100  // Might return 0
   
   // Good: Use decimals
   percentage = (5.0 / 10.0) * 100  // Returns 50
   ```

## Try This

Build a loan calculator:
1. Input: principal, interest rate, term
2. Calculate monthly payment
3. Generate amortization schedule
4. Show total interest paid
5. Display payment breakdown

## Pro Tips

💡 **Constants:** Define PI, E, and other constants as variables for reuse

💡 **Precision:** Always round money calculations to 2 decimal places

💡 **Validation:** Check for null/zero before division operations

💡 **Performance:** Pre-calculate complex formulas outside of loops

Remember: Math functions are the foundation of business logic. Master them to build powerful calculations and data transformations!