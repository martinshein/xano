---
title: Array Functions
description: Master array manipulation in Xano with powerful functions for filtering, sorting, transforming, and processing collections of data
category: function-stack
difficulty: intermediate
last_updated: '2025-01-23'
related_docs:
  - array
  - data-manipulation
  - loops
  - filters
subcategory: 02-core-concepts/function-stack
tags:
  - arrays
  - data-manipulation
  - functions
  - collections
  - filtering
  - transformation
---

# Array Functions

**Quick Summary**
Array functions are like powerful tools for working with lists of data. They help you add, remove, find, sort, and transform collections efficiently - whether you're managing user lists, product catalogs, or any group of related information.

## What You'll Learn

- Essential array manipulation functions
- Advanced array operations (Map, Partition, Group By)
- Set operations (Union, Intersection, Difference)
- Practical patterns for data processing
- When to use each array function

---

## Understanding Array Index

Before diving into functions, remember that arrays use **index** numbering starting from 0:

```json
["Apple", "Banana", "Cherry"]
```
- Index 0: "Apple"
- Index 1: "Banana" 
- Index 2: "Cherry"

This numbering system helps arrays keep track of item positions for efficient operations.

---

## Basic Array Operations

### Add to End of Array
Appends an item to the end of your list.

**Example:** Adding a new user to your user list
```json
// Before: ["Alice", "Bob"]
// After adding "Carol": ["Alice", "Bob", "Carol"]
```

### Add to Beginning of Array
Inserts an item at the start of your list.

**Example:** Adding a priority item to a task list
```json
// Before: ["Task 2", "Task 3"]
// After adding "Urgent Task": ["Urgent Task", "Task 2", "Task 3"]
```

### Remove from End of Array
Takes off the last item in your list.

**Example:** Removing the most recent item
```json
// Before: ["Item 1", "Item 2", "Item 3"]
// After removal: ["Item 1", "Item 2"]
```

### Remove from Beginning of Array  
Takes off the first item in your list.

**Example:** Processing a queue (first in, first out)
```json
// Before: ["First", "Second", "Third"]
// After removal: ["Second", "Third"]
```

### Merge Arrays
Combines two arrays into one.

**Example:** Combining two product lists
```json
// Array 1: ["Laptop", "Mouse"]
// Array 2: ["Keyboard", "Monitor"]
// Merged: ["Laptop", "Mouse", "Keyboard", "Monitor"]
```

---

## Search and Filter Functions

### Find First Element
Locates the first item that matches your criteria.

**Example:** Find first user with admin role
```json
// Array: [{"name": "Alice", "role": "user"}, {"name": "Bob", "role": "admin"}]
// Find first where role = "admin" → {"name": "Bob", "role": "admin"}
```

### Find First Element Index
Returns the position number of the first matching item.

**Example:** Find position of specific product
```json
// Array: ["Laptop", "Mouse", "Keyboard"]
// Find index of "Mouse" → 1
```

### Has Any Element
Checks if at least one item matches your criteria (returns true/false).

**Example:** Check if any order is pending
```json
// Returns true if any order has status "pending"
```

### Has Every Element
Checks if all items match your criteria (returns true/false).

**Example:** Verify all users have email addresses
```json
// Returns true only if every user object has an email field
```

### Find All Elements
Returns all items that match your criteria.

**Example:** Get all high-priority tasks
```json
// Returns array of all tasks where priority = "high"
```

### Get Element Count
Counts how many items match your criteria.

**Example:** Count active users
```json
// Returns number: how many users have status = "active"
```

---

## Advanced Array Transformations

### Array: Map
Transforms each item using a formula and creates a new array.

**Example: Format Prices as Currency**

**Before:**
```json
[11124.12, 235632.12, 393938.52]
```

**After:**
```json
["$11,124.12", "$235,632.12", "$393,938.52"]
```

**How it works:**
- For each number, apply: `concat("$", number_format($this, 2, ".", ","))`
- `$this` represents the current item being processed

| Field | Value | Purpose |
|-------|-------|---------|
| **Collection** | Your input array | The data to transform |
| **Output Type** | Array of Values | What kind of results you want |
| **Mapping Function** | `concat("$", number_format($this, 2, ".", ","))` | Formula to apply to each item |
| **Result As** | `formatted_prices` | Variable name to store results |

### Array: Partition
Splits an array into two groups based on a true/false condition.

**Example: Separate Text from Numbers**

**Before:**
```json
[1, 2, "hello", 3, 4, "goodbye"]
```

**After:**
```json
{
  "true": ["hello", "goodbye"],
  "false": [1, 2, 3, 4]
}
```

**How it works:**
- Test each item: `$this|is_text == true`
- Items that pass the test go in the "true" group
- Items that fail go in the "false" group

| Field | Value | Purpose |
|-------|-------|---------|
| **Array** | Your input array | Data to split |
| **Expression** | `$this\|is_text == true` | True/false test for each item |
| **Result As** | `separated_data` | Variable with true/false groups |

### Array: Group By
Organizes items into groups based on a common value.

**Example: Group People by Age**

**Before:**
```json
[
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 30},
  {"name": "Eve", "age": 25}
]
```

**After:**
```json
{
  "25": [
    {"name": "Alice", "age": 25},
    {"name": "Eve", "age": 25}
  ],
  "30": [
    {"name": "Bob", "age": 30}
  ]
}
```

**How it works:**
- Use `$this.age` as the grouping key
- All items with the same age get grouped together

---

## Set Operations (Advanced)

### Array: Difference
Returns items from the first array that aren't in the second array.

**Example: Students Who Didn't Submit Homework**

**Array 1 (All Students):** `["Amy", "Bob", "Eve"]`  
**Array 2 (Submitted):** `["Amy", "Eve"]`  
**Result:** `["Bob"]`

**Perfect for:** Finding missing items, incomplete tasks, or what's not been done.

### Array: Intersection  
Returns items that appear in both arrays.

**Example: Customers Who Bought Both Products**

**Array 1 (Product A Buyers):** `["Alice", "Bob", "Eve"]`  
**Array 2 (Product B Buyers):** `["Eve", "Charlie", "Bob"]`  
**Result:** `["Bob", "Eve"]`

**Perfect for:** Finding common interests, overlap analysis, or shared characteristics.

### Array: Union
Combines arrays and removes duplicates.

**Example: Merge Mailing Lists**

**List 1:** `["Alice", "Bob"]`  
**List 2:** `["Bob", "Charlie"]`  
**Result:** `["Alice", "Bob", "Charlie"]`

**Perfect for:** Combining datasets, eliminating duplicates, or creating comprehensive lists.

---

## Try This: Build a Product Recommendation System

**Scenario:** Create recommendations based on user purchase history.

### Step 1: Get User's Purchase History
```json
// User's purchased products
["Laptop", "Mouse", "Keyboard", "Monitor"]
```

### Step 2: Get Similar Users (Intersection)
```json
// Find users who bought similar items
// Use Array: Intersection to find common purchases
```

### Step 3: Find Recommendations (Difference)
```json
// Get products similar users bought that this user hasn't
// Use Array: Difference to find new suggestions
```

### Step 4: Group by Category (Group By)
```json
// Group recommendations by product category
// Use Array: Group By with category field
```

### Step 5: Format for Display (Map)
```json
// Transform for frontend display
// Use Array: Map to format product info
```

---

## Expression Builder Guide

Many array functions use the expression builder for conditions. Here's how it works:

### Conditional Types
- **AND** - Both this condition AND previous ones must be true
- **OR** - Either this condition OR others can be true

### Common Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equals | `$this.status == "active"` |
| `!=` | Not equals | `$this.role != "guest"` |
| `>` | Greater than | `$this.age > 18` |
| `<` | Less than | `$this.score < 100` |
| `INCLUDES` | Text contains | `$this.name INCLUDES "john"` |
| `IN` | Value in array | `$this.category IN ["electronics", "gadgets"]` |
| `REGEX MATCHES` | Pattern match | `$this.email REGEX MATCHES ".*@gmail\.com"` |

---

## Integration Patterns

### WeWeb Integration
```javascript
// Process Xano array results in WeWeb
1. Get array from Xano API
2. Use repeater component to display
3. Apply frontend filters for user interaction
4. Sort by user preferences
```

### n8n Integration
```javascript
// Use Xano array functions in n8n workflows
1. Query data from Xano (returns array)
2. Process with Xano array functions
3. Filter/transform results  
4. Send to other services (email, Slack, etc.)
```

---

## Performance Tips

💡 **Optimize Large Arrays**
- Filter arrays before complex operations
- Use pagination for UI display
- Index frequently searched fields

💡 **Choose the Right Function**
- Use Find First for single results
- Use Find All for multiple matches
- Use Has Any/Every for true/false checks

💡 **Memory Considerations**
- Large arrays consume more memory
- Consider processing in batches
- Clean up temporary arrays after use

---

## Common Mistakes to Avoid

❌ **Not handling empty arrays**
- Always check if arrays have items before processing

❌ **Using wrong array functions**
- Map transforms items, Filter finds items - know the difference

❌ **Forgetting index starts at 0**
- First item is at position 0, not 1

❌ **Not optimizing for large datasets**
- Filter before processing to improve performance

---

**Next Steps:** Master array processing with [Loops](/root/xano-knowledge/02-core-concepts/function-stack/loops.md) or explore [Data Manipulation](/root/xano-knowledge/02-core-concepts/function-stack/data-manipulation.md) for working with different data types.