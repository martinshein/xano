---
title: "Comparison Functions - Data Matching and Validation"
description: "Master comparison operations for data validation, filtering, and conditional logic in Xano"
category: function-stack
subcategory: logic
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- comparison
- validation
- filtering
- conditionals
- logic
---

# Comparison Functions - Data Matching and Validation

## Quick Summary

> **What it is:** Functions that compare values to make decisions - checking if things are equal, greater than, less than, or match specific patterns
> 
> **When to use:** For data validation, filtering records, conditional logic, access control, and any decision-making in your workflows
> 
> **Key benefit:** Build intelligent applications that respond differently based on data conditions
> 
> **Most common:** Equality checks, range validations, and null checking

## What You'll Learn

- Basic comparison operators and their uses
- String and number comparisons
- Null and empty value checking
- Complex comparison patterns
- Best practices for n8n and WeWeb integrations

## Basic Comparison Operators

### Equality Operators

```javascript
// Equal to
user.role == "admin"  // Is user an admin?
price == 100         // Is price exactly 100?

// Not equal to
status != "cancelled"  // Is status anything except cancelled?
user_id != null       // Does user_id have a value?

// Strict equality (type-safe)
count === "5"   // false (number vs string)
count === 5     // true (both numbers)
```

### Numeric Comparisons

```javascript
// Greater than
age > 18              // Over 18?
price > discount_threshold

// Greater than or equal
score >= passing_grade  // Did they pass?
inventory >= minimum_stock

// Less than
days_remaining < 7     // Less than a week left?
usage < quota_limit

// Less than or equal
discount <= max_discount  // Within discount limits?
attempts <= max_attempts
```

## String Comparisons

### Text Matching

```javascript
// Case-sensitive comparison
username == "JohnDoe"  // Exact match

// Case-insensitive (use LOWER filter)
LOWER(email) == LOWER(input_email)

// Pattern matching
email CONTAINS "@company.com"  // Company email?
phone STARTS_WITH "+1"         // US phone number?
filename ENDS_WITH ".pdf"      // PDF file?
```

### String Operations

```javascript
// Check if text contains substring
description CONTAINS "urgent"
tags CONTAINS "featured"

// Check if in list
status IN ["active", "pending", "processing"]
category IN allowed_categories

// Regular expression matching
email MATCHES "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
```

## Null and Empty Checking

### Null Validation

```javascript
// Check for null/undefined
user.profile_image != null  // Has profile image?
optional_field == null      // Is field empty?

// Check for empty string
name != ""                  // Name provided?
description != ""           // Has description?

// Combined empty check
(email != null AND email != "")  // Email exists and not empty
```

### Default Value Pattern

```javascript
// Use default if null
display_name = username || "Guest User"
profile_image = user.avatar || "/default-avatar.png"
theme = user.theme || "light"
```

## Practical Examples

### Example 1: User Access Control

```javascript
// Multi-level permission check
can_edit = (
  user.role == "admin" OR 
  (user.role == "editor" AND resource.status != "locked") OR
  (user.id == resource.owner_id AND resource.editable == true)
)

// Time-based access
is_business_hours = (
  current_hour >= 9 AND 
  current_hour < 17 AND 
  day_of_week != "Saturday" AND 
  day_of_week != "Sunday"
)

// Subscription check
has_premium_access = (
  user.subscription_tier IN ["premium", "enterprise"] AND
  user.subscription_expiry > NOW()
)
```

### Example 2: Data Validation

```javascript
// Form validation
is_valid_email = (
  email != null AND 
  email != "" AND 
  email CONTAINS "@" AND 
  email CONTAINS "."
)

// Password strength
is_strong_password = (
  LENGTH(password) >= 8 AND
  password MATCHES "[A-Z]" AND  // Has uppercase
  password MATCHES "[a-z]" AND  // Has lowercase
  password MATCHES "[0-9]"      // Has number
)

// Age verification
is_eligible = (
  age >= 18 AND 
  age <= 65 AND
  country IN approved_countries
)
```

### Example 3: Dynamic Filtering

```javascript
// E-commerce filters
show_product = (
  (price >= min_price OR min_price == null) AND
  (price <= max_price OR max_price == null) AND
  (category == selected_category OR selected_category == "all") AND
  in_stock == true AND
  active == true
)

// Search relevance
is_relevant = (
  title CONTAINS search_term OR
  description CONTAINS search_term OR
  tags CONTAINS search_term
)
```

## Range Comparisons

### Between Values

```javascript
// Check if value is in range
is_in_range = (value >= min AND value <= max)

// Business hours check
is_business_hour = (hour >= 9 AND hour < 17)

// Date range
is_current_month = (
  date >= MONTH_START() AND 
  date <= MONTH_END()
)
```

### Threshold Checks

```javascript
// Inventory alerts
needs_reorder = (stock_level <= reorder_point)
is_overstocked = (stock_level > max_inventory)

// Performance thresholds
is_slow_response = (response_time > 2000)  // Over 2 seconds
is_high_cpu = (cpu_usage > 80)            // Over 80%
```

## Integration Patterns

### With n8n

```javascript
// Webhook validation
is_valid_webhook = (
  webhook.signature == expected_signature AND
  webhook.timestamp > (NOW() - 300) AND  // Within 5 minutes
  webhook.event_type IN supported_events
)

// Conditional workflow routing
route_to_workflow = 
  IF (priority == "high") THEN "urgent-workflow"
  ELSE IF (priority == "medium") THEN "standard-workflow"
  ELSE "low-priority-workflow"
```

### With WeWeb

```javascript
// Form field visibility
show_company_field = (user_type == "business")
show_vat_field = (country IN eu_countries)
show_discount_code = (is_first_purchase == false)

// Button state management
can_submit = (
  all_required_filled == true AND
  form_is_valid == true AND
  is_submitting == false
)
```

## Advanced Comparisons

### Fuzzy Matching

```javascript
// Similarity checking (requires custom function)
is_similar = SIMILARITY(input_text, target_text) > 0.8

// Approximate number matching
is_approximately_equal = ABS(value1 - value2) < 0.01

// Date proximity
is_recent = (NOW() - created_at) < (24 * 60 * 60)  // Within 24 hours
```

### Set Operations

```javascript
// Array contains value
tags CONTAINS "featured"
users_array CONTAINS user_id

// Array intersection
has_common_tags = (ARRAY_INTERSECT(tags1, tags2).length > 0)

// Array subset
has_all_permissions = ARRAY_IS_SUBSET(required_perms, user_perms)
```

## Common Mistakes to Avoid

1. **Type Mismatches**
   ```javascript
   // Bad: Comparing different types
   "5" == 5  // May cause issues
   
   // Good: Ensure same type
   parseInt("5") == 5
   ```

2. **Null Reference Errors**
   ```javascript
   // Bad: Not checking for null
   user.profile.image  // Error if profile is null
   
   // Good: Safe navigation
   user.profile != null AND user.profile.image != null
   ```

3. **Case Sensitivity**
   ```javascript
   // Bad: Case-sensitive when shouldn't be
   email == "John@Example.com"
   
   // Good: Case-insensitive for emails
   LOWER(email) == LOWER(input_email)
   ```

## Best Practices

### Readable Conditions

```javascript
// Bad: Complex inline condition
IF ((a > b AND c != null) OR (d == "x" AND e < 10))

// Good: Named variables
is_primary_condition = (a > b AND c != null)
is_secondary_condition = (d == "x" AND e < 10)
IF (is_primary_condition OR is_secondary_condition)
```

### Defensive Comparisons

```javascript
// Always check for null first
IF (user != null AND user.role == "admin")

// Use parentheses for clarity
IF ((a AND b) OR (c AND d))

// Provide defaults
value = input_value || default_value
```

## Try This

Build a smart filtering system:
1. Create multiple filter conditions
2. Combine with AND/OR logic
3. Handle null/empty filters
4. Apply to data query
5. Return filtered results

## Pro Tips

💡 **Order Matters:** Put cheapest comparisons first for performance

💡 **Use Constants:** Define magic numbers as named variables

💡 **Null Safety:** Always check for null before accessing properties

💡 **Type Conversion:** Ensure data types match before comparing

## Performance Optimization

- Simple comparisons are faster than complex ones
- Use indexed fields for database comparisons
- Avoid regex when simple operators work
- Cache comparison results when reused

Remember: Comparisons are the foundation of intelligent applications. Master them to build dynamic, responsive systems!