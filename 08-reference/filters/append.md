---
title: Array Filters Reference - Complete Guide for No-Code Development
description: Master Xano's array manipulation filters including append, merge, sort, filter operations, and more for powerful data processing in n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - filters-overview.md
  - text-filters.md
  - object-filters.md
tags:
  - array-filters
  - data-manipulation
  - reference
  - append
  - merge
  - sort
  - filter
  - transform
---

## 📋 **Quick Summary**

Master Xano's comprehensive array filter library to manipulate, transform, and process arrays efficiently. This reference covers all array operations from basic append/prepend to advanced filtering, sorting, and merging operations perfect for no-code developers using n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Complete array filter reference with practical examples
- Array manipulation techniques (append, merge, sort, filter)
- Data transformation patterns for no-code platforms
- Performance optimization tips for large datasets
- Common use cases and best practices
- Integration patterns with external platforms

# Array Filters Reference

## 🔧 **Basic Array Operations**

### append

**Purpose**: Adds a new element to the end of an array and returns the updated array.

**Parameters:**
- `parent value`: The original array to modify
- `value`: The value to add to the end of the array

**Examples:**

**Basic Number Array:**
```javascript
// Input
parent_value: [1, 2, 3, 4]
value: 5

// Output
[1, 2, 3, 4, 5]
```

**String Array:**
```javascript
// Input
parent_value: ["Think Visually", "Build Confidently"]
value: "Deploy Securely"

// Output
["Think Visually", "Build Confidently", "Deploy Securely"]
```

**Object Array:**
```javascript
// Input
parent_value: [
  {"id": 1, "name": "John"},
  {"id": 2, "name": "Jane"}
]
value: {"id": 3, "name": "Bob"}

// Output
[
  {"id": 1, "name": "John"},
  {"id": 2, "name": "Jane"},
  {"id": 3, "name": "Bob"}
]
```

**💡 Pro Tip for n8n/WeWeb Integration:**
```javascript
// Use append to build dynamic arrays in workflows
// n8n example: Building a list of processed items
const processedItems = [];
// In loop: append each processed item
items.forEach(item => {
  processedItems.append(processItem(item));
});
```

### prepend

**Purpose**: Adds an element to the beginning of an array.

**Examples:**
```javascript
// Input
parent_value: [2, 3, 4]
value: 1

// Output
[1, 2, 3, 4]
```

### push

**Purpose**: Adds an element to the end of an array (alias for append).

### count

**Purpose**: Returns the number of items in an array.

**Examples:**
```javascript
// Input
parent_value: [1, 2, 3, 4, 5]

// Output
5

// Complex objects
parent_value: [
  {"id": 1, "status": "active"},
  {"id": 2, "status": "inactive"}
]

// Output
2
```

**🔗 Integration Use Case:**
```javascript
// WeWeb: Display total items count
const totalProducts = productArray.count();
// Use in WeWeb component: "Showing {{totalProducts}} products"
```

## 🔄 **Array Transformation**

### first

**Purpose**: Gets the first entry of an array.

**Examples:**
```javascript
// Input
parent_value: [1, 2, 3]

// Output
1

// Object array
parent_value: [
  {"name": "Alice", "age": 30},
  {"name": "Bob", "age": 25}
]

// Output
{"name": "Alice", "age": 30}
```

### last

**Purpose**: Gets the last entry of an array.

**Examples:**
```javascript
// Input
parent_value: [1, 2, 3]

// Output
3
```

### slice

**Purpose**: Extracts and returns a section of an array.

**Parameters:**
- `offset`: Starting index (0-based)
- `length`: Number of items to extract

**Examples:**
```javascript
// Input
parent_value: [1, 2, 3, 4, 5, 6]
offset: 2
length: 3

// Output
[3, 4, 5]

// Pagination example
parent_value: users_array
offset: 20  // Skip first 20 users
length: 10  // Take next 10 users

// Output: Users 21-30 for page 3
```

### flatten

**Purpose**: Flattens a multi-level array into a single-level array.

**Examples:**
```javascript
// Input
parent_value: [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

// Output
[1, 2, 3, 4, 5, 6, 7, 8, 9]

// Nested objects
parent_value: [
  {
    id: 1,
    name: "John",
    pets: [
      {"type": "dog", "name": "Rex"},
      {"type": "cat", "name": "Whiskers"}
    ]
  },
  {
    id: 2,
    name: "Sarah",
    pets: [
      {"type": "bird", "name": "Tweety"}
    ]
  }
]

// After flattening pets arrays
[
  {"type": "dog", "name": "Rex"},
  {"type": "cat", "name": "Whiskers"},
  {"type": "bird", "name": "Tweety"}
]
```

## 🔍 **Array Filtering**

### filter_empty

**Purpose**: Returns a new array with only entries that are not empty.

**Empty values**: `[]`, `""`, `0`, `null`, `false`

**Parameters:**
- `parent value`: The array to filter
- `path` (optional): For object arrays, specify a key to check for emptiness

**Examples:**
```javascript
// Basic filtering
parent_value: [1, 0, 2, "", 3, null, 4]

// Output
[1, 2, 3, 4]

// Object filtering with path
parent_value: [
  {"name": "John", "email": "john@example.com"},
  {"name": "", "email": "jane@example.com"},
  {"name": "Bob", "email": ""}
]
path: "name"

// Output
[
  {"name": "John", "email": "john@example.com"},
  {"name": "Bob", "email": ""}
]
```

### Specialized Filter Functions

**filter_empty_array**: Removes empty arrays `[]`
**filter_empty_object**: Removes empty objects `{}`
**filter_empty_text**: Removes empty strings `""`
**filter_false**: Removes `false` values
**filter_null**: Removes `null` values
**filter_zero**: Removes `0` values

**Example - Cleaning API Response:**
```javascript
// Input: Data from external API with mixed empty values
parent_value: {
  "title": "",
  "name": false,
  "width": 0,
  "items": [],
  "data": {"valid": true},
  "info": null
}

// After filter_empty_text
{
  "name": false,
  "width": 0,
  "items": [],
  "data": {"valid": true},
  "info": null
}

// After filter_null
{
  "name": false,
  "width": 0,
  "items": [],
  "data": {"valid": true}
}
```

**🔗 Real-World Use Case (WeWeb Form Processing):**
```javascript
// Clean user form data before saving
const cleanFormData = formData
  .filter_empty_text()
  .filter_null()
  .filter_empty_array();
```

### unique

**Purpose**: Returns unique values of an array. For object arrays, specify a path to determine uniqueness.

**Examples:**
```javascript
// Simple array
parent_value: [1, 2, 2, 3, 3, 4]

// Output
[1, 2, 3, 4]

// Object array - unique by ID
parent_value: [
  {"id": 1, "name": "John"},
  {"id": 2, "name": "Jane"},
  {"id": 1, "name": "John Doe"} // Duplicate ID
]
path: "id"

// Output
[
  {"id": 1, "name": "John"},
  {"id": 2, "name": "Jane"}
]
```

### remove

**Purpose**: Removes elements from array that match the supplied value.

**Parameters:**
- `value`: Value to remove
- `path` (optional): For objects, specify which field to check
- `strict` (optional): Precise matching (treats 100 and "100" differently)

**Examples:**
```javascript
// Remove specific value
parent_value: [1, 2, 3, 2, 4]
value: 2

// Output
[1, 3, 4]

// Remove by object property
parent_value: [
  {"status": "active", "name": "John"},
  {"status": "inactive", "name": "Jane"},
  {"status": "active", "name": "Bob"}
]
value: "inactive"
path: "status"

// Output
[
  {"status": "active", "name": "John"},
  {"status": "active", "name": "Bob"}
]
```

## 🔄 **Array Comparison**

### diff / diff_assoc

**Purpose**: Shows values from the first array that are NOT in the second array.

- `diff`: For simple values
- `diff_assoc`: For arrays of objects

**Examples:**
```javascript
// Basic diff
parent_value: [1, 2, 3, 4, 5]
value: [3, 4, 5, 6, 7]

// Output
[1, 2]

// Object diff_assoc
parent_value: [
  {"id": 1, "name": "John"},
  {"id": 2, "name": "Jane"},
  {"id": 3, "name": "Bob"}
]
value: [
  {"id": 2, "name": "Jane"}
]

// Output
[
  {"id": 1, "name": "John"},
  {"id": 3, "name": "Bob"}
]
```

### intersect / intersect_assoc

**Purpose**: Shows values from the first array that ARE in the second array.

**Examples:**
```javascript
// Basic intersect
parent_value: [1, 2, 3, 4, 5]
value: [3, 4, 5, 6, 7]

// Output
[3, 4, 5]
```

**💡 Use Case - Finding Common Elements:**
```javascript
// n8n: Find products available in both stores
const store1Products = [1, 2, 3, 4, 5];
const store2Products = [3, 4, 5, 6, 7];
const commonProducts = store1Products.intersect(store2Products);
// Result: [3, 4, 5]
```

## 🔗 **Array Merging**

### merge / merge_recursive

**Purpose**: Merge two arrays or objects together.

- `merge`: For single-level data
- `merge_recursive`: For multi-level data

**Examples:**
```javascript
// Basic merge
parent_value: ["a", "b", "c"]
value: ["d", "e", "f"]

// Output
["a", "b", "c", "d", "e", "f"]

// Object merge_recursive
parent_value: {
  "user": {
    "name": "John",
    "email": "john@example.com"
  },
  "preferences": {
    "theme": "dark"
  }
}
value: {
  "user": {
    "age": 30
  },
  "preferences": {
    "language": "en"
  }
}

// Output
{
  "user": {
    "name": "John",
    "email": "john@example.com",
    "age": 30
  },
  "preferences": {
    "theme": "dark",
    "language": "en"
  }
}
```

**🔗 Integration Example:**
```javascript
// WeWeb: Merge user data from multiple sources
const userData = basicProfile.merge_recursive(preferences);
const completeProfile = userData.merge_recursive(activityData);
```

## 📊 **Array Sorting**

### sort

**Purpose**: Sort an array with optional path, sort type, and direction.

**Sort Types:**
- `text`: Case-sensitive text sort
- `itext`: Case-insensitive text sort  
- `number`: Numeric sort
- `natural`: Alphanumeric, human-friendly sort
- `inatural`: Case-insensitive natural sort

**Parameters:**
- `path`: For objects, field to sort by
- `type`: Sort type (see above)
- `ascending`: `true` for ascending, `false` for descending

**Examples:**
```javascript
// Simple number sort
parent_value: [3, 1, 4, 1, 5, 9, 2, 6]
type: "number"
ascending: true

// Output
[1, 1, 2, 3, 4, 5, 6, 9]

// Object sort by name
parent_value: [
  {"name": "Charlie", "age": 30},
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 35}
]
path: "name"
type: "text"
ascending: true

// Output
[
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 35},
  {"name": "Charlie", "age": 30}
]

// Natural vs regular sorting
parent_value: ["item1", "item10", "item2", "item20"]

// Regular text sort
["item1", "item10", "item2", "item20"]

// Natural sort  
["item1", "item2", "item10", "item20"]
```

**🔗 Real-World Examples:**

**E-commerce Product Sorting:**
```javascript
// Sort products by price (low to high)
products.sort("price", "number", true)

// Sort by popularity (high to low)
products.sort("popularity_score", "number", false)

// Sort by name (A-Z, case-insensitive)
products.sort("name", "itext", true)
```

### shuffle

**Purpose**: Returns the array in randomized order.

**Example:**
```javascript
// Input
parent_value: [1, 2, 3, 4, 5]

// Output (random)
[3, 1, 5, 2, 4]
```

## 🔧 **Array Manipulation**

### join

**Purpose**: Converts an array into a text string using a separator.

**Parameters:**
- `separator` (optional): Character(s) to place between items

**Examples:**
```javascript
// Basic join with underscore
parent_value: ["a", "b", "c"]
separator: "_"

// Output
"a_b_c"

// Join without separator
parent_value: [1, 2, 3, 4, 5]
separator: ""

// Output
"12345"

// Create CSV format
parent_value: ["John", "25", "Engineer"]
separator: ","

// Output
"John,25,Engineer"
```

**🔗 Use Cases:**
```javascript
// Generate tags for display
const tagString = tagArray.join(", ");
// Result: "React, JavaScript, API, Database"

// Create file path
const pathParts = ["uploads", "2025", "01", "file.jpg"];
const filePath = pathParts.join("/");
// Result: "uploads/2025/01/file.jpg"
```

### range

**Purpose**: Returns array of values between specified start/stop.

**Examples:**
```javascript
// Generate number sequence
start: 1
stop: 5

// Output
[1, 2, 3, 4, 5]

// Generate years
start: 2020
stop: 2025

// Output
[2020, 2021, 2022, 2023, 2024, 2025]
```

### safe_array

**Purpose**: Always returns an array. Uses existing value if array, otherwise creates single-element array.

**Examples:**
```javascript
// Already an array
parent_value: [1, 2, 3]

// Output
[1, 2, 3]

// Single value
parent_value: "hello"

// Output
["hello"]

// Null value
parent_value: null

// Output
[null]
```

## 🎯 **Object Operations**

### pick / unpick

**Purpose**: Select or exclude specific fields from objects.

**pick**: Keep only specified fields
**unpick**: Remove specified fields

**Examples:**

**Pick Example:**
```javascript
// Input object
parent_value: {
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secret123",
  "internal_notes": "VIP customer",
  "created_at": "2025-01-16"
}

// Pick only public fields
fields: ["id", "name", "email", "created_at"]

// Output
{
  "id": 123,
  "name": "John Doe", 
  "email": "john@example.com",
  "created_at": "2025-01-16"
}
```

**Unpick Example:**
```javascript
// Remove sensitive fields
fields: ["password", "internal_notes"]

// Output
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com", 
  "created_at": "2025-01-16"
}
```

**🔗 API Security Pattern:**
```javascript
// Clean user data before sending to frontend
const publicUserData = fullUserData.unpick([
  "password_hash",
  "reset_token", 
  "internal_notes",
  "admin_flags"
]);
```

## 🚀 **Advanced Array Operations**

### pop

**Purpose**: Returns the last element of an array.

**Note**: Xano's pop filter does NOT remove the item from the array.

### shift

**Purpose**: Returns the first element of an array and removes it.

### unshift

**Purpose**: Adds an element to the beginning of an array and returns the new array.

## 🔗 **Integration Patterns**

### n8n Workflow Examples

**Building Dynamic Arrays:**
```javascript
// n8n Code node: Process webhook data
const processedItems = [];
for (const item of items) {
  if (item.status === 'active') {
    processedItems.append({
      id: item.id,
      processed_at: new Date().toISOString(),
      data: item.data
    });
  }
}
return processedItems;
```

**Data Transformation Pipeline:**
```javascript
// Clean and transform data
const cleanData = rawData
  .filter_empty()           // Remove empty values
  .unique("id")             // Remove duplicates by ID
  .sort("created_at", "text", false) // Sort newest first
  .slice(0, 10);           // Take first 10 items
```

### WeWeb Component Integration

**Dynamic List Rendering:**
```javascript
// WeWeb computed property
const displayProducts = products
  .filter_empty()
  .sort("price", "number", true)
  .slice((currentPage - 1) * itemsPerPage, itemsPerPage);
```

**Search and Filter:**
```javascript
// WeWeb search functionality
const searchResults = allProducts
  .filter(product => product.name.includes(searchTerm))
  .sort("relevance_score", "number", false);
```

### Make.com Scenario Patterns

**Batch Processing:**
```javascript
// Process items in chunks
const batchSize = 10;
const totalBatches = Math.ceil(items.count() / batchSize);

for (let i = 0; i < totalBatches; i++) {
  const batch = items.slice(i * batchSize, batchSize);
  // Process batch
}
```

## 💡 **Performance Best Practices**

### Optimize Large Arrays

**Chain Operations Efficiently:**
```javascript
// Good: Chain operations to minimize iterations
const result = largeArray
  .filter_empty()
  .unique("id")
  .sort("priority", "number", false)
  .slice(0, 100);

// Avoid: Multiple separate operations
// const filtered = largeArray.filter_empty();
// const unique = filtered.unique("id");
// const sorted = unique.sort("priority", "number", false);
// const limited = sorted.slice(0, 100);
```

**Use Appropriate Filters:**
```javascript
// Specific filters are more efficient than generic ones
data.filter_null()        // Better than filter_empty for nulls
data.filter_empty_text()  // Better than filter_empty for strings
```

### Memory Management

**Process Large Datasets in Chunks:**
```javascript
// For very large arrays, process in smaller chunks
const chunkSize = 1000;
const chunks = [];

for (let i = 0; i < largeArray.count(); i += chunkSize) {
  chunks.append(largeArray.slice(i, chunkSize));
}

// Process each chunk separately
```

## 🔧 **Common Patterns**

### Data Validation Pipeline

```javascript
// Complete data cleaning and validation
const cleanData = rawData
  .filter_empty()                    // Remove empty entries
  .unique("id")                     // Remove duplicates
  .filter(item => item.status !== "deleted") // Remove deleted items
  .sort("updated_at", "text", false) // Sort by most recent
  .pick(["id", "name", "status", "data"]); // Keep only needed fields
```

### Pagination Implementation

```javascript
// Server-side pagination
const page = parseInt(request.page) || 1;
const limit = parseInt(request.limit) || 20;
const offset = (page - 1) * limit;

const paginatedData = {
  data: allRecords.slice(offset, limit),
  pagination: {
    page: page,
    limit: limit,
    total: allRecords.count(),
    pages: Math.ceil(allRecords.count() / limit)
  }
};
```

### Search Implementation

```javascript
// Multi-field search with scoring
const searchResults = products
  .filter(product => 
    product.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    product.description.toLowerCase().includes(searchTerm.toLowerCase())
  )
  .sort("relevance_score", "number", false)
  .slice(0, 50);
```

---

**Next Steps**: Explore more filter types in [Text Filters](text-filters.md) and [Object Filters](object-filters.md) to complete your data manipulation toolkit.