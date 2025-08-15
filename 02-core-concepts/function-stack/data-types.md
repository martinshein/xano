---
title: "Data Types - Complete Type System Guide"
description: "Master all Xano data types with practical examples for text, numbers, objects, arrays, timestamps, and advanced type handling in function stacks"
category: function-stack
tags:
  - Data Types
  - Type System
  - Variables
  - Data Validation
  - Type Conversion
  - Schema Design
  - Input Handling
difficulty: intermediate
reading_time: 10 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of programming concepts
  - Familiarity with Xano function stacks
  - Knowledge of JSON structure
---

# Data Types - Complete Type System Guide

## 📋 **Quick Summary**

**What it does:** Xano's data type system provides structured ways to handle different kinds of data including text, numbers, objects, arrays, timestamps, and more, ensuring data integrity and enabling type-safe operations.

**Why it matters:** Understanding data types enables you to:
- **Build robust APIs** with proper input validation
- **Design efficient databases** with appropriate field types
- **Handle user input safely** with type checking and conversion
- **Create dynamic interfaces** with proper data binding
- **Optimize performance** with correct type selection

**Time to implement:** 5-10 minutes for basic types, 30+ minutes for complex type validation systems

---

## What You'll Learn

- Complete overview of all Xano data types
- Type conversion and validation techniques
- Best practices for type selection
- Dynamic type handling patterns
- Integration with no-code platforms

## Core Data Types

### 🔤 **Text (String)**

**Purpose:** Store textual data including names, descriptions, and formatted content
**Database Storage:** VARCHAR, TEXT fields
**JSON Representation:** `"string value"`

```javascript
// Basic text handling
const userName = "John Doe";
const description = "User profile description";
const htmlContent = "<p>Rich text content</p>";

// Text validation
function validateText(input, minLength = 1, maxLength = 255) {
  if (typeof input !== 'string') {
    throw new Error('Input must be a string');
  }
  
  if (input.length < minLength) {
    throw new Error(`Text must be at least ${minLength} characters`);
  }
  
  if (input.length > maxLength) {
    throw new Error(`Text must not exceed ${maxLength} characters`);
  }
  
  return input.trim();
}
```

### 🔢 **Integer**

**Purpose:** Store whole numbers including IDs, counts, and status codes
**Database Storage:** INTEGER, BIGINT fields
**JSON Representation:** `42`

```javascript
// Integer handling
const userId = 1001;
const itemCount = 25;
const statusCode = 200;

// Integer validation
function validateInteger(input, min = null, max = null) {
  const num = parseInt(input);
  
  if (isNaN(num)) {
    throw new Error('Input must be a valid integer');
  }
  
  if (min !== null && num < min) {
    throw new Error(`Value must be at least ${min}`);
  }
  
  if (max !== null && num > max) {
    throw new Error(`Value must not exceed ${max}`);
  }
  
  return num;
}
```

### 💰 **Decimal**

**Purpose:** Store precise decimal numbers for currency, measurements, and calculations
**Database Storage:** DECIMAL, NUMERIC fields
**JSON Representation:** `19.99`

```javascript
// Decimal handling
const price = 19.99;
const taxRate = 0.08;
const measurement = 15.75;

// Decimal validation and formatting
function validateDecimal(input, precision = 2) {
  const num = parseFloat(input);
  
  if (isNaN(num)) {
    throw new Error('Input must be a valid decimal');
  }
  
  // Round to specified precision
  return Math.round(num * Math.pow(10, precision)) / Math.pow(10, precision);
}

// Currency formatting
function formatCurrency(amount, currency = 'USD') {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currency
  }).format(amount);
}
```

### ✅ **Boolean**

**Purpose:** Store true/false values for flags, settings, and status indicators
**Database Storage:** BOOLEAN fields
**JSON Representation:** `true` or `false`

```javascript
// Boolean handling
const isActive = true;
const hasPermission = false;
const isSubscribed = true;

// Boolean validation
function validateBoolean(input) {
  if (typeof input === 'boolean') {
    return input;
  }
  
  if (typeof input === 'string') {
    const lower = input.toLowerCase();
    if (lower === 'true' || lower === '1' || lower === 'yes') {
      return true;
    }
    if (lower === 'false' || lower === '0' || lower === 'no') {
      return false;
    }
  }
  
  if (typeof input === 'number') {
    return input !== 0;
  }
  
  throw new Error('Input cannot be converted to boolean');
}
```

### 📅 **Timestamp**

**Purpose:** Store date and time information with timezone awareness
**Database Storage:** TIMESTAMP, DATETIME fields
**JSON Representation:** `"2024-01-15T10:30:00Z"`

```javascript
// Timestamp handling
const now = new Date().toISOString();
const userCreated = "2024-01-15T10:30:00Z";
const expirationDate = "2024-12-31T23:59:59Z";

// Timestamp validation and manipulation
class TimestampHandler {
  static validate(input) {
    const date = new Date(input);
    
    if (isNaN(date.getTime())) {
      throw new Error('Invalid timestamp format');
    }
    
    return date.toISOString();
  }
  
  static isExpired(timestamp) {
    return new Date(timestamp) < new Date();
  }
  
  static addDays(timestamp, days) {
    const date = new Date(timestamp);
    date.setDate(date.getDate() + days);
    return date.toISOString();
  }
  
  static formatForDisplay(timestamp, locale = 'en-US') {
    return new Date(timestamp).toLocaleString(locale);
  }
}
```

### 📦 **Object**

**Purpose:** Store structured data with key-value pairs
**Database Storage:** JSON, JSONB fields
**JSON Representation:** `{"key": "value"}`

```javascript
// Object handling
const userProfile = {
  name: "John Doe",
  email: "john@example.com",
  preferences: {
    theme: "dark",
    notifications: true
  }
};

// Object validation and manipulation
class ObjectHandler {
  static validate(input, schema) {
    if (typeof input !== 'object' || input === null || Array.isArray(input)) {
      throw new Error('Input must be a valid object');
    }
    
    // Validate against schema
    for (const [key, type] of Object.entries(schema)) {
      if (!(key in input)) {
        throw new Error(`Missing required field: ${key}`);
      }
      
      if (typeof input[key] !== type) {
        throw new Error(`Field ${key} must be of type ${type}`);
      }
    }
    
    return input;
  }
  
  static sanitize(input, allowedKeys) {
    const sanitized = {};
    
    for (const key of allowedKeys) {
      if (key in input) {
        sanitized[key] = input[key];
      }
    }
    
    return sanitized;
  }
  
  static merge(base, updates) {
    return { ...base, ...updates };
  }
}
```

### 📋 **Array**

**Purpose:** Store ordered collections of items
**Database Storage:** JSON array fields
**JSON Representation:** `["item1", "item2", "item3"]`

```javascript
// Array handling
const tags = ["javascript", "api", "backend"];
const userIds = [1, 2, 3, 4, 5];
const mixedArray = ["text", 123, true, { key: "value" }];

// Array validation and manipulation
class ArrayHandler {
  static validate(input, itemType = null, maxLength = null) {
    if (!Array.isArray(input)) {
      throw new Error('Input must be an array');
    }
    
    if (maxLength && input.length > maxLength) {
      throw new Error(`Array length cannot exceed ${maxLength}`);
    }
    
    if (itemType) {
      for (let i = 0; i < input.length; i++) {
        if (typeof input[i] !== itemType) {
          throw new Error(`Item at index ${i} must be of type ${itemType}`);
        }
      }
    }
    
    return input;
  }
  
  static unique(array) {
    return [...new Set(array)];
  }
  
  static filterEmpty(array) {
    return array.filter(item => 
      item !== null && 
      item !== undefined && 
      item !== ''
    );
  }
}
```

### ❌ **Null**

**Purpose:** Represent absence of value or empty state
**Database Storage:** NULL values
**JSON Representation:** `null`

```javascript
// Null handling
const optionalField = null;
const unsetValue = null;

// Null validation and handling
function handleNullable(input, defaultValue = null) {
  if (input === null || input === undefined) {
    return defaultValue;
  }
  
  return input;
}

function requireNonNull(input, fieldName) {
  if (input === null || input === undefined) {
    throw new Error(`${fieldName} cannot be null or undefined`);
  }
  
  return input;
}
```

## Advanced Type Handling

### Dynamic Type Validation

```javascript
// Comprehensive type validation system
class TypeValidator {
  static validateBySchema(data, schema) {
    const errors = [];
    
    for (const [field, rules] of Object.entries(schema)) {
      try {
        this.validateField(data[field], rules, field);
      } catch (error) {
        errors.push(error.message);
      }
    }
    
    if (errors.length > 0) {
      throw new Error(`Validation failed: ${errors.join(', ')}`);
    }
    
    return true;
  }
  
  static validateField(value, rules, fieldName) {
    // Required validation
    if (rules.required && (value === null || value === undefined)) {
      throw new Error(`${fieldName} is required`);
    }
    
    // Skip type checking if value is null and not required
    if (value === null || value === undefined) {
      return;
    }
    
    // Type validation
    switch (rules.type) {
      case 'string':
        this.validateString(value, rules, fieldName);
        break;
      case 'integer':
        this.validateInteger(value, rules, fieldName);
        break;
      case 'decimal':
        this.validateDecimal(value, rules, fieldName);
        break;
      case 'boolean':
        this.validateBoolean(value, rules, fieldName);
        break;
      case 'timestamp':
        this.validateTimestamp(value, rules, fieldName);
        break;
      case 'object':
        this.validateObject(value, rules, fieldName);
        break;
      case 'array':
        this.validateArray(value, rules, fieldName);
        break;
      default:
        throw new Error(`Unknown type: ${rules.type}`);
    }
  }
  
  static validateString(value, rules, fieldName) {
    if (typeof value !== 'string') {
      throw new Error(`${fieldName} must be a string`);
    }
    
    if (rules.minLength && value.length < rules.minLength) {
      throw new Error(`${fieldName} must be at least ${rules.minLength} characters`);
    }
    
    if (rules.maxLength && value.length > rules.maxLength) {
      throw new Error(`${fieldName} must not exceed ${rules.maxLength} characters`);
    }
    
    if (rules.pattern && !new RegExp(rules.pattern).test(value)) {
      throw new Error(`${fieldName} does not match required pattern`);
    }
  }
  
  static validateInteger(value, rules, fieldName) {
    const num = parseInt(value);
    
    if (isNaN(num)) {
      throw new Error(`${fieldName} must be a valid integer`);
    }
    
    if (rules.min !== undefined && num < rules.min) {
      throw new Error(`${fieldName} must be at least ${rules.min}`);
    }
    
    if (rules.max !== undefined && num > rules.max) {
      throw new Error(`${fieldName} must not exceed ${rules.max}`);
    }
  }
}
```

### Type Conversion Utilities

```javascript
// Automatic type conversion with validation
class TypeConverter {
  static toType(value, targetType, options = {}) {
    switch (targetType) {
      case 'string':
        return this.toString(value, options);
      case 'integer':
        return this.toInteger(value, options);
      case 'decimal':
        return this.toDecimal(value, options);
      case 'boolean':
        return this.toBoolean(value, options);
      case 'timestamp':
        return this.toTimestamp(value, options);
      case 'object':
        return this.toObject(value, options);
      case 'array':
        return this.toArray(value, options);
      default:
        throw new Error(`Cannot convert to type: ${targetType}`);
    }
  }
  
  static toString(value, options = {}) {
    if (value === null || value === undefined) {
      return options.defaultValue || '';
    }
    
    return String(value);
  }
  
  static toInteger(value, options = {}) {
    if (value === null || value === undefined) {
      return options.defaultValue || 0;
    }
    
    const num = parseInt(value);
    
    if (isNaN(num)) {
      if (options.strict) {
        throw new Error('Cannot convert to integer');
      }
      return options.defaultValue || 0;
    }
    
    return num;
  }
  
  static toBoolean(value, options = {}) {
    if (value === null || value === undefined) {
      return options.defaultValue || false;
    }
    
    if (typeof value === 'boolean') {
      return value;
    }
    
    if (typeof value === 'string') {
      const lower = value.toLowerCase();
      return ['true', '1', 'yes', 'on'].includes(lower);
    }
    
    if (typeof value === 'number') {
      return value !== 0;
    }
    
    return Boolean(value);
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Type Handling**

```javascript
// n8n type validation function
function validateInput($input, schema) {
  const errors = [];
  
  for (const [field, rules] of Object.entries(schema)) {
    const value = $input.body[field];
    
    // Required field check
    if (rules.required && (value === null || value === undefined || value === '')) {
      errors.push(`${field} is required`);
      continue;
    }
    
    // Skip validation if field is optional and empty
    if (!rules.required && (value === null || value === undefined || value === '')) {
      continue;
    }
    
    // Type-specific validation
    switch (rules.type) {
      case 'email':
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          errors.push(`${field} must be a valid email`);
        }
        break;
        
      case 'url':
        try {
          new URL(value);
        } catch {
          errors.push(`${field} must be a valid URL`);
        }
        break;
        
      case 'phone':
        if (!/^\+?[\d\s\-\(\)]+$/.test(value)) {
          errors.push(`${field} must be a valid phone number`);
        }
        break;
        
      case 'integer':
        if (!Number.isInteger(Number(value))) {
          errors.push(`${field} must be an integer`);
        }
        break;
    }
  }
  
  if (errors.length > 0) {
    return { error: errors.join(', ') };
  }
  
  return { success: true };
}
```

### 🌐 **WeWeb Type Binding**

```javascript
// WeWeb type-safe data binding
class WeWebTypedBinding {
  static bindData(element, data, type) {
    try {
      switch (type) {
        case 'text':
          element.textContent = String(data || '');
          break;
          
        case 'number':
          const num = Number(data);
          element.textContent = isNaN(num) ? '0' : num.toLocaleString();
          break;
          
        case 'currency':
          const amount = Number(data);
          element.textContent = isNaN(amount) ? '$0.00' : 
            new Intl.NumberFormat('en-US', {
              style: 'currency',
              currency: 'USD'
            }).format(amount);
          break;
          
        case 'date':
          const date = new Date(data);
          element.textContent = isNaN(date) ? 'Invalid Date' : 
            date.toLocaleDateString();
          break;
          
        case 'boolean':
          element.textContent = Boolean(data) ? 'Yes' : 'No';
          break;
          
        case 'array':
          if (Array.isArray(data)) {
            element.textContent = data.length + ' items';
          } else {
            element.textContent = '0 items';
          }
          break;
          
        default:
          element.textContent = String(data || '');
      }
      
      // Add data attributes for styling
      element.setAttribute('data-type', type);
      element.setAttribute('data-value', String(data));
      
    } catch (error) {
      console.error('Type binding error:', error);
      element.textContent = 'Error displaying data';
    }
  }
}
```

## Common Type Patterns

### Form Input Validation

```javascript
// Complete form validation with type checking
class FormValidator {
  static validateUserRegistration(input) {
    const schema = {
      name: { type: 'string', required: true, minLength: 2, maxLength: 50 },
      email: { type: 'string', required: true, pattern: '^[^\s@]+@[^\s@]+\.[^\s@]+$' },
      age: { type: 'integer', required: true, min: 13, max: 120 },
      phone: { type: 'string', required: false, pattern: '^\\+?[\\d\\s\\-\\(\\)]+$' },
      terms_accepted: { type: 'boolean', required: true }
    };
    
    return TypeValidator.validateBySchema(input, schema);
  }
  
  static validateProductData(input) {
    const schema = {
      name: { type: 'string', required: true, maxLength: 100 },
      price: { type: 'decimal', required: true, min: 0 },
      category_id: { type: 'integer', required: true, min: 1 },
      description: { type: 'string', required: false, maxLength: 1000 },
      tags: { type: 'array', required: false },
      is_featured: { type: 'boolean', required: false },
      available_from: { type: 'timestamp', required: false }
    };
    
    return TypeValidator.validateBySchema(input, schema);
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Build basic type validation:
1. Create input validators for common types
2. Add type conversion functions
3. Implement form validation
4. Test with various data inputs

### Intermediate Challenge
Build dynamic type system:
1. Create schema-based validation
2. Add custom type definitions
3. Implement type coercion
4. Build error handling system

### Advanced Challenge
Create enterprise type management:
1. Build runtime type checking
2. Add type inference system
3. Create type documentation generator
4. Implement performance optimization

## Type Selection Best Practices

1. **Use appropriate precision** - Choose decimal for currency, integer for counts
2. **Consider storage efficiency** - Smaller types for better performance
3. **Plan for scale** - Use BIGINT for large number ranges
4. **Validate at boundaries** - Check types at API entry points
5. **Document type requirements** - Clear specifications for developers

## Next Steps

- Learn [Data Manipulation](data-manipulation.md) for processing typed data
- Explore [Arrays](arrays.md) for collection handling
- Master [Objects](objects.md) for structured data
- Understand [Text Functions](text.md) for string processing

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Type system discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Data type guides
- 📖 [Best Practices](../../best-practices/data-modeling.md) - Type selection guidance
- 🔧 [Support](https://xano.com/support) - Complex type assistance