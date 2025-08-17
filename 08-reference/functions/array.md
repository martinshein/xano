---
title: Array Data Type Reference
description: Complete guide to working with arrays in Xano - store, manipulate, and process collections of data for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- arrays
- data-types
- collections
- list-processing
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: beginner
has_code_examples: true
related_docs:
- filters/append.md
- expressions/configuring-expressions.md
- 02-core-concepts/function-stack/arrays.md
---

# Array Data Type Reference

## 📋 **Quick Summary**
Arrays in Xano store collections of data in ordered lists. Perfect for managing product lists, user collections, API responses, and bulk data operations in no-code platforms like n8n, WeWeb, and Make.com.

## What You'll Learn
- Array structure and syntax in Xano
- Creating and initializing arrays
- Working with array elements
- Integration patterns for no-code platforms
- Best practices for array performance
- Common array operations and filters

## Array Structure

An array is always contained inside square brackets: **[ ]**

### Basic Array Types

**Numeric Arrays:**
```javascript
[1, 2, 3, 4, 5]
```

**String Arrays:**
```javascript
["Hello", "World", "Xano", "Rocks"]
```

**Mixed Data Arrays:**
```javascript
[
  "Product Name",
  29.99,
  true,
  {
    "category": "electronics",
    "in_stock": true
  }
]
```

**Empty Array:**
```javascript
[]
```

## 🔄 **No-Code Platform Integration**

### n8n Integration
```javascript
// In n8n HTTP Request node - process Xano array response
{
  "method": "GET",
  "url": "{{$node.Webhook.body.api_endpoint}}",
  "options": {
    "response": {
      "response.body.products": "{{$json.map(item => item.name)}}"
    }
  }
}
```

### WeWeb Integration
```javascript
// WeWeb formula for array manipulation
products.filter(product => product.price > 20)
        .map(product => ({
          name: product.name,
          displayPrice: `$${product.price}`
        }))
```

### Make.com Integration
```javascript
// Make.com iterator setup for array processing
{
  "array": "{{body.user_orders}}",
  "iterator": {
    "order_id": "{{item.id}}",
    "total": "{{item.total}}",
    "status": "{{item.status}}"
  }
}
```

## 💡 **Try This: Build a Product Collection**

Create an array to manage your e-commerce products:

```javascript
[
  {
    "id": 1,
    "name": "Wireless Headphones",
    "price": 79.99,
    "categories": ["electronics", "audio"],
    "tags": ["wireless", "bluetooth", "music"]
  },
  {
    "id": 2,
    "name": "Smart Watch",
    "price": 199.99,
    "categories": ["electronics", "wearables"],
    "tags": ["fitness", "smart", "notifications"]
  }
]
```

## Common Array Operations

### Array Filters
Use these built-in filters for array manipulation:

- `append` - Add items to array
- `count` - Get array length
- `first` - Get first element
- `last` - Get last element
- `unique` - Remove duplicates
- `sort` - Sort array elements

### Example with Filters
```javascript
// Original array
["apple", "banana", "apple", "orange"]

// Using unique filter
["apple", "banana", "orange"]

// Using count filter
3
```

## ⚠️ **Common Mistakes to Avoid**

1. **Missing Brackets**: Always use square brackets `[]`
2. **Trailing Commas**: Avoid commas after the last element
3. **Inconsistent Data Types**: Be careful mixing different types
4. **Large Array Performance**: Consider pagination for arrays > 1000 items

## 🚀 **Pro Tips**

### Performance Optimization
```javascript
// Good: Use pagination for large datasets
{
  "page": 1,
  "limit": 50,
  "products": [...] // Max 50 items
}

// Better: Include metadata
{
  "data": [...],
  "meta": {
    "total": 500,
    "page": 1,
    "pages": 10
  }
}
```

### Nested Arrays
```javascript
// Organize complex data structures
{
  "user_id": 123,
  "preferences": {
    "categories": ["electronics", "books"],
    "price_ranges": [
      {"min": 0, "max": 50},
      {"min": 100, "max": 200}
    ]
  }
}
```

### API Response Formatting
```javascript
// Structure for easy consumption by no-code tools
{
  "success": true,
  "data": [...],
  "count": 25,
  "has_more": true
}
```

## Integration Best Practices

### For n8n Workflows
- Use Set node to transform array structures
- Implement proper error handling for empty arrays
- Use Split in Batches for large array processing

### For WeWeb Apps
- Bind arrays to collection components
- Use computed formulas for array filtering
- Implement loading states for array data

### For Make.com Scenarios
- Use Array Aggregator for combining data
- Implement iterator modules for array processing
- Set up proper error handling paths

## Related Functions
- [Append Filter](../filters/append.md) - Adding elements to arrays
- [Array Functions](../../02-core-concepts/function-stack/arrays.md) - Advanced array operations
- [Configuring Expressions](../../05-advanced-features/expressions/configuring-expressions.md) - Using arrays in expressions

Arrays are the foundation for managing collections in Xano. Master these patterns to build powerful data processing workflows that integrate seamlessly with your favorite no-code platforms.

