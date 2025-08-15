---
title: "Filters - Advanced Data Processing Functions"
description: "Master Xano's powerful filter functions for data transformation, manipulation, text processing, and advanced data operations in function stacks"
category: function-stack
tags:
  - Filters
  - Data Processing
  - Text Functions
  - Array Functions
  - Date Functions
  - Math Functions
  - String Manipulation
difficulty: intermediate
reading_time: 12 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of function stacks
  - Basic knowledge of data types
  - Familiarity with data manipulation concepts
---

# Filters - Advanced Data Processing Functions

## 📋 **Quick Summary**

**What it does:** Filter functions provide powerful data transformation and manipulation capabilities, enabling you to process, format, and modify data within your function stacks without complex custom code.

**Why it matters:** Filter functions enable you to:
- **Transform data efficiently** with built-in processing functions
- **Format output dynamically** for different display requirements
- **Manipulate strings and arrays** with powerful utilities
- **Process dates and numbers** with precision and flexibility
- **Build complex data pipelines** with chained operations

**Time to implement:** 5-10 minutes for basic filters, 30+ minutes for complex data processing workflows

---

## What You'll Learn

- Complete overview of all filter categories
- Practical examples for common use cases
- Advanced filter chaining techniques
- Performance optimization patterns
- Integration with no-code platforms

## Filter Categories

### 🔤 **Text Filters**

Transform and manipulate string data with powerful text processing functions.

```javascript
// Common text filters
const processedText = {
  uppercase: "hello world".toUpperCase(), // "HELLO WORLD"
  lowercase: "HELLO WORLD".toLowerCase(), // "hello world"
  title_case: "hello world".replace(/\w\S*/g, (txt) => 
    txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()), // "Hello World"
  trim: "  hello world  ".trim(), // "hello world"
  replace: "hello world".replace("world", "universe"), // "hello universe"
  substring: "hello world".substring(0, 5), // "hello"
  length: "hello world".length, // 11
  split: "hello,world".split(","), // ["hello", "world"]
  contains: "hello world".includes("world"), // true
  starts_with: "hello world".startsWith("hello"), // true
  ends_with: "hello world".endsWith("world") // true
};
```

### 🔢 **Math Filters**

Perform mathematical operations and number formatting.

```javascript
// Math filter examples
const mathOperations = {
  add: 10 + 5, // 15
  subtract: 10 - 5, // 5
  multiply: 10 * 5, // 50
  divide: 10 / 5, // 2
  modulo: 10 % 3, // 1
  power: Math.pow(2, 3), // 8
  square_root: Math.sqrt(16), // 4
  absolute: Math.abs(-10), // 10
  round: Math.round(3.14159), // 3
  floor: Math.floor(3.14159), // 3
  ceiling: Math.ceil(3.14159), // 4
  random: Math.random(), // 0.123456789...
  min: Math.min(1, 2, 3), // 1
  max: Math.max(1, 2, 3) // 3
};
```

### 📅 **Date/Timestamp Filters**

Process and format date and time data.

```javascript
// Date filter utilities
class DateFilters {
  static formatDate(timestamp, format = 'YYYY-MM-DD') {
    const date = new Date(timestamp);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    
    switch (format) {
      case 'YYYY-MM-DD':
        return `${year}-${month}-${day}`;
      case 'MM/DD/YYYY':
        return `${month}/${day}/${year}`;
      case 'DD/MM/YYYY':
        return `${day}/${month}/${year}`;
      default:
        return date.toLocaleDateString();
    }
  }
  
  static addDays(timestamp, days) {
    const date = new Date(timestamp);
    date.setDate(date.getDate() + days);
    return date.toISOString();
  }
  
  static timeDifference(start, end, unit = 'days') {
    const startDate = new Date(start);
    const endDate = new Date(end);
    const diffTime = Math.abs(endDate - startDate);
    
    switch (unit) {
      case 'seconds':
        return Math.floor(diffTime / 1000);
      case 'minutes':
        return Math.floor(diffTime / (1000 * 60));
      case 'hours':
        return Math.floor(diffTime / (1000 * 60 * 60));
      case 'days':
        return Math.floor(diffTime / (1000 * 60 * 60 * 24));
      default:
        return diffTime;
    }
  }
}
```

### 📋 **Array Filters**

Process and manipulate array data structures.

```javascript
// Array filter operations
class ArrayFilters {
  static map(array, transformer) {
    return array.map(transformer);
  }
  
  static filter(array, predicate) {
    return array.filter(predicate);
  }
  
  static reduce(array, reducer, initialValue) {
    return array.reduce(reducer, initialValue);
  }
  
  static sort(array, key = null, direction = 'asc') {
    const sorted = [...array];
    
    if (key) {
      sorted.sort((a, b) => {
        const aVal = a[key];
        const bVal = b[key];
        
        if (direction === 'desc') {
          return bVal > aVal ? 1 : -1;
        }
        return aVal > bVal ? 1 : -1;
      });
    } else {
      sorted.sort((a, b) => {
        if (direction === 'desc') {
          return b > a ? 1 : -1;
        }
        return a > b ? 1 : -1;
      });
    }
    
    return sorted;
  }
  
  static unique(array) {
    return [...new Set(array)];
  }
  
  static flatten(array) {
    return array.flat();
  }
  
  static join(array, separator = ',') {
    return array.join(separator);
  }
  
  static slice(array, start, end) {
    return array.slice(start, end);
  }
  
  static chunk(array, size) {
    const chunks = [];
    for (let i = 0; i < array.length; i += size) {
      chunks.push(array.slice(i, i + size));
    }
    return chunks;
  }
}
```

### 🔄 **Conversion Filters**

Convert between different data types and formats.

```javascript
// Type conversion utilities
class ConversionFilters {
  static toString(value) {
    if (value === null || value === undefined) {
      return '';
    }
    return String(value);
  }
  
  static toNumber(value) {
    const num = Number(value);
    return isNaN(num) ? 0 : num;
  }
  
  static toBoolean(value) {
    if (typeof value === 'boolean') return value;
    if (typeof value === 'string') {
      return ['true', '1', 'yes', 'on'].includes(value.toLowerCase());
    }
    if (typeof value === 'number') {
      return value !== 0;
    }
    return Boolean(value);
  }
  
  static toArray(value) {
    if (Array.isArray(value)) return value;
    if (value === null || value === undefined) return [];
    return [value];
  }
  
  static toJSON(value) {
    return JSON.stringify(value, null, 2);
  }
  
  static fromJSON(jsonString) {
    try {
      return JSON.parse(jsonString);
    } catch (error) {
      return null;
    }
  }
  
  static toBase64(text) {
    return btoa(text);
  }
  
  static fromBase64(base64) {
    try {
      return atob(base64);
    } catch (error) {
      return '';
    }
  }
}
```

## Real-World Filter Applications

### E-commerce Product Processing

```javascript
// Product data transformation pipeline
class ProductProcessor {
  static processProducts(rawProducts) {
    return rawProducts
      .filter(product => product.status === 'active')
      .map(product => ({
        ...product,
        name: this.formatProductName(product.name),
        price: this.formatCurrency(product.price),
        description: this.truncateDescription(product.description, 150),
        tags: this.normalizeTags(product.tags),
        availability: this.checkAvailability(product.stock_quantity),
        discount_percentage: this.calculateDiscount(product.original_price, product.price)
      }))
      .sort((a, b) => b.featured - a.featured);
  }
  
  static formatProductName(name) {
    return name
      .trim()
      .replace(/\s+/g, ' ')
      .replace(/\b\w/g, l => l.toUpperCase());
  }
  
  static formatCurrency(amount, currency = 'USD') {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency
    }).format(amount);
  }
  
  static truncateDescription(text, maxLength) {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength).trim() + '...';
  }
  
  static normalizeTags(tags) {
    return tags
      .map(tag => tag.toLowerCase().trim())
      .filter(tag => tag.length > 0)
      .filter((tag, index, array) => array.indexOf(tag) === index);
  }
  
  static checkAvailability(stock) {
    if (stock > 10) return 'in_stock';
    if (stock > 0) return 'low_stock';
    return 'out_of_stock';
  }
  
  static calculateDiscount(original, current) {
    if (original <= current) return 0;
    return Math.round(((original - current) / original) * 100);
  }
}
```

### User Data Sanitization

```javascript
// User input processing and sanitization
class UserDataProcessor {
  static sanitizeUserInput(userData) {
    return {
      name: this.sanitizeName(userData.name),
      email: this.sanitizeEmail(userData.email),
      phone: this.sanitizePhone(userData.phone),
      bio: this.sanitizeText(userData.bio, 500),
      tags: this.sanitizeArray(userData.tags),
      preferences: this.sanitizePreferences(userData.preferences)
    };
  }
  
  static sanitizeName(name) {
    return name
      .trim()
      .replace(/[^\w\s]/gi, '')
      .replace(/\s+/g, ' ')
      .substring(0, 50);
  }
  
  static sanitizeEmail(email) {
    return email.toLowerCase().trim();
  }
  
  static sanitizePhone(phone) {
    return phone.replace(/[^\d+\-\(\)\s]/g, '');
  }
  
  static sanitizeText(text, maxLength = 1000) {
    return text
      .trim()
      .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
      .substring(0, maxLength);
  }
  
  static sanitizeArray(array, maxItems = 10) {
    if (!Array.isArray(array)) return [];
    
    return array
      .slice(0, maxItems)
      .map(item => String(item).trim())
      .filter(item => item.length > 0);
  }
  
  static sanitizePreferences(prefs) {
    const allowedKeys = ['theme', 'notifications', 'language', 'timezone'];
    const sanitized = {};
    
    for (const key of allowedKeys) {
      if (key in prefs) {
        sanitized[key] = prefs[key];
      }
    }
    
    return sanitized;
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Filter Workflows**

```javascript
// n8n data transformation function
function transformData($input) {
  const data = $input.body;
  
  // Apply multiple filters in sequence
  const processed = data
    .filter(item => item.status === 'active')
    .map(item => ({
      id: item.id,
      title: item.title.trim().toLowerCase().replace(/\b\w/g, l => l.toUpperCase()),
      price: parseFloat(item.price).toFixed(2),
      created_date: new Date(item.created_at).toLocaleDateString(),
      tags: item.tags.split(',').map(tag => tag.trim().toLowerCase()),
      has_discount: parseFloat(item.original_price) > parseFloat(item.price)
    }))
    .sort((a, b) => new Date(b.created_date) - new Date(a.created_date));
  
  return {
    success: true,
    data: processed,
    total: processed.length,
    processed_at: new Date().toISOString()
  };
}
```

### 🌐 **WeWeb Filter Integration**

```javascript
// WeWeb filter utilities
class WeWebFilters {
  static formatCurrency(amount, element) {
    const formatted = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
    
    if (element) {
      element.textContent = formatted;
    }
    
    return formatted;
  }
  
  static formatDate(timestamp, element, format = 'short') {
    const date = new Date(timestamp);
    const options = {
      short: { year: 'numeric', month: 'short', day: 'numeric' },
      long: { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' },
      time: { hour: '2-digit', minute: '2-digit' }
    };
    
    const formatted = date.toLocaleDateString('en-US', options[format]);
    
    if (element) {
      element.textContent = formatted;
    }
    
    return formatted;
  }
  
  static truncateText(text, maxLength = 100, element = null) {
    const truncated = text.length > maxLength ? 
      text.substring(0, maxLength) + '...' : text;
    
    if (element) {
      element.textContent = truncated;
      element.title = text; // Show full text on hover
    }
    
    return truncated;
  }
  
  static formatArray(array, element = null, separator = ', ') {
    const formatted = Array.isArray(array) ? array.join(separator) : '';
    
    if (element) {
      element.textContent = formatted;
    }
    
    return formatted;
  }
}

// Usage in WeWeb
wwLib.registerFilter('currency', WeWebFilters.formatCurrency);
wwLib.registerFilter('date', WeWebFilters.formatDate);
wwLib.registerFilter('truncate', WeWebFilters.truncateText);
wwLib.registerFilter('arrayJoin', WeWebFilters.formatArray);
```

## Advanced Filter Patterns

### Chained Filter Operations

```javascript
// Complex data processing pipeline
class FilterPipeline {
  constructor(data) {
    this.data = data;
  }
  
  filter(predicate) {
    this.data = this.data.filter(predicate);
    return this;
  }
  
  map(transformer) {
    this.data = this.data.map(transformer);
    return this;
  }
  
  sort(compareFn) {
    this.data = this.data.sort(compareFn);
    return this;
  }
  
  slice(start, end) {
    this.data = this.data.slice(start, end);
    return this;
  }
  
  groupBy(keyFn) {
    const groups = {};
    
    for (const item of this.data) {
      const key = keyFn(item);
      if (!groups[key]) {
        groups[key] = [];
      }
      groups[key].push(item);
    }
    
    this.data = groups;
    return this;
  }
  
  get result() {
    return this.data;
  }
}

// Usage example
const processedData = new FilterPipeline(rawUserData)
  .filter(user => user.status === 'active')
  .map(user => ({
    ...user,
    full_name: `${user.first_name} ${user.last_name}`,
    age: Math.floor((Date.now() - new Date(user.birth_date)) / (365.25 * 24 * 60 * 60 * 1000))
  }))
  .filter(user => user.age >= 18)
  .sort((a, b) => a.full_name.localeCompare(b.full_name))
  .slice(0, 50)
  .result;
```

### Conditional Filter Application

```javascript
// Dynamic filter application based on conditions
class ConditionalFilters {
  static applyFilters(data, filterConfig) {
    let result = [...data];
    
    // Apply filters conditionally
    if (filterConfig.textSearch) {
      result = this.applyTextSearch(result, filterConfig.textSearch);
    }
    
    if (filterConfig.dateRange) {
      result = this.applyDateRange(result, filterConfig.dateRange);
    }
    
    if (filterConfig.statusFilter) {
      result = this.applyStatusFilter(result, filterConfig.statusFilter);
    }
    
    if (filterConfig.sortBy) {
      result = this.applySorting(result, filterConfig.sortBy);
    }
    
    if (filterConfig.pagination) {
      result = this.applyPagination(result, filterConfig.pagination);
    }
    
    return result;
  }
  
  static applyTextSearch(data, searchConfig) {
    const { query, fields } = searchConfig;
    
    return data.filter(item => {
      return fields.some(field => {
        const value = item[field];
        return value && value.toString().toLowerCase().includes(query.toLowerCase());
      });
    });
  }
  
  static applyDateRange(data, dateConfig) {
    const { field, start, end } = dateConfig;
    
    return data.filter(item => {
      const itemDate = new Date(item[field]);
      const startDate = new Date(start);
      const endDate = new Date(end);
      
      return itemDate >= startDate && itemDate <= endDate;
    });
  }
  
  static applyStatusFilter(data, statusConfig) {
    const { field, values } = statusConfig;
    
    return data.filter(item => values.includes(item[field]));
  }
  
  static applySorting(data, sortConfig) {
    const { field, direction } = sortConfig;
    
    return data.sort((a, b) => {
      const aVal = a[field];
      const bVal = b[field];
      
      if (direction === 'desc') {
        return bVal > aVal ? 1 : -1;
      }
      return aVal > bVal ? 1 : -1;
    });
  }
  
  static applyPagination(data, pageConfig) {
    const { page, limit } = pageConfig;
    const start = (page - 1) * limit;
    const end = start + limit;
    
    return data.slice(start, end);
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Build basic filter operations:
1. Create text formatting filters
2. Implement number formatting
3. Add date processing functions
4. Test with sample data

### Intermediate Challenge
Build filter pipeline:
1. Create chained filter operations
2. Add conditional filter application
3. Implement custom filter functions
4. Build reusable filter utilities

### Advanced Challenge
Create enterprise filter system:
1. Build performance-optimized filters
2. Add filter composition patterns
3. Create filter documentation system
4. Implement filter testing framework

## Filter Performance Tips

1. **Filter early** - Apply filters that reduce data size first
2. **Avoid nested operations** - Flatten complex operations when possible
3. **Cache computed values** - Store expensive calculations
4. **Use appropriate data structures** - Choose efficient data types
5. **Limit filter chains** - Keep pipeline length reasonable

## Next Steps

- Master [Arrays](arrays.md) for collection processing
- Learn [Text Functions](text.md) for string manipulation
- Explore [Objects](objects.md) for data structure handling
- Understand [Math Functions](math.md) for calculations

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Filter function discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Data processing guides
- 📖 [Advanced Patterns](../../best-practices/data-processing.md) - Filter optimization
- 🔧 [Support](https://xano.com/support) - Complex filter assistance