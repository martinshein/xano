---
title: "Transform Functions"
description: "Master data transformation operations in Xano function stacks for converting and reshaping data efficiently"
category: function-stack
difficulty: intermediate
tags:
  - transform
  - data-manipulation
  - conversion
  - formatting
  - filters
  - mapping
related_docs:
  - filters
  - data-types
  - expressions
  - arrays
last_updated: '2025-01-23'
---

# Transform Functions

## Quick Summary
Transform functions in Xano convert and reshape data between different formats and structures. Essential for API integrations, data processing, and ensuring consistent data formats across your application.

## What You'll Learn
- Data transformation fundamentals
- Converting between data types
- Reshaping data structures
- Filtering and mapping operations
- Complex transformation patterns
- Performance optimization techniques

## Core Transform Operations

### Data Type Conversion

**To String**: Convert any data type to text
```javascript
// Convert number to string
input: 123
transform: "to_string"
result: "123"
```

**To Number**: Convert text to numeric value
```javascript
// Convert string to number
input: "123.45"
transform: "to_number"
result: 123.45
```

**To Boolean**: Convert value to true/false
```javascript
// Convert to boolean
input: "true"
transform: "to_boolean"
result: true
```

### Array Transformations

**Map**: Transform each array element
```javascript
// Transform array elements
input: [1, 2, 3, 4, 5]
transform: "multiply_by_2"
result: [2, 4, 6, 8, 10]
```

**Filter**: Select elements meeting criteria
```javascript
// Filter even numbers
input: [1, 2, 3, 4, 5, 6]
filter: "is_even"
result: [2, 4, 6]
```

**Reduce**: Combine array elements into single value
```javascript
// Sum array elements
input: [1, 2, 3, 4, 5]
operation: "sum"
result: 15
```

## Integration Patterns

### For n8n Users
Data transformation for workflow processing:

```javascript
// n8n data transformation
{
  "transform_user_data": {
    "full_name": "{{$node['Input'].json['first_name']}} {{$node['Input'].json['last_name']}}",
    "email_normalized": "{{$node['Input'].json['email'].toLowerCase()}}",
    "age_group": "{{$node['Input'].json['age'] >= 18 ? 'adult' : 'minor'}}",
    "profile_complete": "{{Object.keys($node['Input'].json).length >= 5}}"
  }
}
```

### For WeWeb Users
UI data transformation and display:

```javascript
// WeWeb data transformation
{
  "display_data": {
    "formatted_price": "{{price.toFixed(2)}}",
    "status_color": "{{status === 'active' ? 'green' : 'red'}}",
    "created_relative": "{{formatDistanceToNow(created_at)}}",
    "tags_string": "{{tags.join(', ')}}"
  }
}
```

### API Response Transformation

```json
{
  "user": {
    "id": 123,
    "profile": {
      "display_name": "John D.",
      "avatar_url": "https://example.com/avatars/123.jpg",
      "member_since": "January 2025",
      "is_premium": true,
      "settings": {
        "notifications": true,
        "privacy": "public"
      }
    }
  }
}
```

## Common Use Cases

### API Integration
Transform external API responses to match your data structure:

```javascript
// External API transformation
external_response: {
  "firstName": "John",
  "lastName": "Doe",
  "emailAddress": "john@example.com"
}

transformed: {
  "full_name": "John Doe",
  "email": "john@example.com",
  "display_name": "John D."
}
```

### Data Export
Convert internal data for external consumption:

```javascript
// CSV export transformation
internal_data: {
  "user_id": 123,
  "profile": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}

csv_format: "123,John Doe,john@example.com"
```

### Database Migration
Transform data between different schemas:

```javascript
// Schema migration
old_format: {
  "user_name": "john_doe",
  "user_email": "john@example.com"
}

new_format: {
  "username": "john_doe",
  "email": "john@example.com",
  "created_at": "2025-01-23T15:30:00Z"
}
```

## Try This
1. **Type Conversion**: Practice converting between strings, numbers, and booleans
2. **Array Operations**: Transform arrays with map, filter, and reduce
3. **Object Restructuring**: Reshape complex objects for different use cases
4. **API Transformation**: Convert external API data to internal format
5. **Export Formatting**: Transform data for CSV, JSON, or XML export

## Common Mistakes to Avoid

❌ **Don't:**
- Transform data unnecessarily
- Ignore data validation before transformation
- Create overly complex transformation chains
- Forget to handle null/empty values
- Lose important data during transformation

✅ **Do:**
- Validate data before transformation
- Keep transformations simple and readable
- Handle edge cases and null values
- Document complex transformation logic
- Test transformations with various input types

## Pro Tips

💡 **Efficiency:**
- Combine multiple transformations when possible
- Cache transformation results for repeated use
- Use built-in functions over custom logic
- Validate input data early

🚀 **Performance:**
- Avoid unnecessary nested transformations
- Use efficient array operations
- Batch similar transformations together
- Consider memory usage for large datasets

⚡ **Maintainability:**
- Use descriptive transformation names
- Break complex transformations into steps
- Document transformation business rules
- Test edge cases thoroughly

Transform functions provide the flexibility to handle any data format conversion your application requires.