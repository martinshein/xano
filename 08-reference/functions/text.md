---
title: Text Data Type Reference
description: Complete guide to working with text strings in Xano - store, manipulate, and process textual data for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- text
- strings
- data-types
- text-processing
- content-management
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: beginner
has_code_examples: true
related_docs:
- 08-reference/filters/format__timestamp.md
- 02-core-concepts/function-stack/text.md
- expressions/configuring-expressions.md
---

# Text Data Type Reference

## 📋 **Quick Summary**
Text values in Xano store character strings for names, descriptions, content, and any textual data. Essential for user content, messaging, search functionality, and text processing in no-code platforms like n8n, WeWeb, and Make.com.

## What You'll Learn
- Text string syntax and formatting
- String manipulation and processing
- Text validation and sanitization
- Integration patterns for no-code platforms
- Content management best practices
- Common text operations and filters

## Text String Format

Text strings are enclosed in double quotes and can contain any characters:

### Basic Text Syntax

**Simple Strings:**
```javascript
"Hello World"
"Welcome to Xano!"
"john@example.com"
"555-123-4567"
```

**Multi-line Text:**
```javascript
"This is a long description\nthat spans multiple lines\nand contains line breaks."
```

**Special Characters:**
```javascript
"Text with \"quotes\" inside"
"Path with \\ backslashes"
"Unicode: ✓ ✗ 🚀"
```

**Empty String:**
```javascript
""
```

## 🔄 **No-Code Platform Integration**

### n8n Integration
```javascript
// In n8n Set node - text processing
{
  "full_name": "{{$json.first_name}} {{$json.last_name}}",
  "email_domain": "{{$json.email.split('@')[1]}}",
  "clean_phone": "{{$json.phone.replace(/[^0-9]/g, '')}}",
  "slug": "{{$json.title.toLowerCase().replace(/\s+/g, '-')}}"
}
```

### WeWeb Integration
```javascript
// WeWeb formula for text formatting
user.first_name + " " + user.last_name
// Text transformation
product.name.toLowerCase().replace(/ /g, "-")
```

### Make.com Integration
```javascript
// Make.com text functions
{
  "formatted_name": "{{capitalize(trim(name))}}",
  "search_keywords": "{{split(keywords, ',')}}",
  "clean_content": "{{stripHTML(content)}}"
}
```

## Common Text Use Cases

### User Information
```javascript
{
  "user_profile": {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1 (555) 123-4567",
    "bio": "Software developer passionate about no-code solutions.",
    "website": "https://johndoe.dev"
  }
}
```

### Content Management
```javascript
{
  "blog_post": {
    "title": "Getting Started with Xano",
    "slug": "getting-started-with-xano",
    "excerpt": "Learn the basics of building APIs with Xano's visual interface.",
    "content": "Full blog post content goes here...",
    "tags": "xano,no-code,api,tutorial",
    "meta_description": "Complete guide to starting with Xano platform."
  }
}
```

### Product Information
```javascript
{
  "product": {
    "name": "Wireless Bluetooth Headphones",
    "sku": "WBH-001-BLK",
    "description": "High-quality wireless headphones with noise cancellation.",
    "category": "Electronics > Audio > Headphones",
    "brand": "AudioTech",
    "color": "Matte Black"
  }
}
```

## 💡 **Try This: Build a Content Management System**

Create a comprehensive text-based content structure:

```javascript
{
  "article": {
    "id": 123,
    "title": "The Future of No-Code Development",
    "slug": "future-of-no-code-development",
    "author": "Jane Smith",
    "excerpt": "Exploring how no-code platforms are revolutionizing software development.",
    "content": "<p>No-code development platforms have transformed...</p>",
    "status": "published",
    "tags": [
      "no-code",
      "development",
      "automation",
      "future-tech"
    ],
    "meta": {
      "description": "Learn about the future trends in no-code development",
      "keywords": "no-code, low-code, development, automation",
      "og_title": "The Future of No-Code Development | TechBlog"
    }
  }
}
```

## Text Operations

### String Manipulation
```javascript
// Concatenation
"Hello" + " " + "World" // "Hello World"

// Length
length("Hello") // 5

// Substring
substr("Hello World", 0, 5) // "Hello"

// Replace
replace("Hello World", "World", "Xano") // "Hello Xano"
```

### Case Conversion
```javascript
// Uppercase
upper("hello") // "HELLO"

// Lowercase
lower("HELLO") // "hello"

// Title Case
title("hello world") // "Hello World"

// Capitalize first letter
capitalize("hello") // "Hello"
```

### String Cleaning
```javascript
// Remove whitespace
trim("  hello  ") // "hello"

// Remove HTML tags
strip_tags("<p>Hello</p>") // "Hello"

// URL-safe slug
slug("Hello World!") // "hello-world"
```

## ⚠️ **Common Mistakes to Avoid**

1. **Quote Escaping**: Use `\"` for quotes inside strings
2. **Empty Checks**: Always validate for empty or null strings
3. **Encoding Issues**: Handle special characters properly
4. **Length Limits**: Be aware of database field length constraints

### Safe String Handling
```javascript
// Check if string exists and has content
function isValidString(str) {
  return str && typeof str === 'string' && str.trim().length > 0;
}

// Safe concatenation
function safeConcat(str1, str2, separator = ' ') {
  const s1 = (str1 || '').trim();
  const s2 = (str2 || '').trim();
  if (!s1 && !s2) return '';
  if (!s1) return s2;
  if (!s2) return s1;
  return s1 + separator + s2;
}
```

## 🚀 **Pro Tips**

### Text Search and Indexing
```javascript
// Full-text search preparation
{
  "searchable_content": lower(title + " " + content + " " + tags),
  "keywords": split(keywords, ","),
  "search_weight": {
    "title": 3,
    "excerpt": 2,
    "content": 1
  }
}
```

### URL-Friendly Slugs
```javascript
// Generate SEO-friendly URLs
function createSlug(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '') // Remove special chars
    .replace(/\s+/g, '-')         // Replace spaces with hyphens
    .replace(/-+/g, '-')          // Remove multiple hyphens
    .trim('-');                   // Remove leading/trailing hyphens
}
```

### Content Sanitization
```javascript
// Clean user input
function sanitizeInput(text) {
  return text
    .trim()                       // Remove whitespace
    .replace(/<script[^>]*>.*?<\/script>/gi, '') // Remove scripts
    .replace(/[<>"']/g, '')      // Remove dangerous chars
    .substring(0, 500);          // Limit length
}
```

## Integration Best Practices

### For n8n Workflows
- Use Set nodes for text transformations
- Implement proper encoding for special characters
- Handle empty/null text values gracefully

### For WeWeb Apps
- Bind text values to input and display components
- Use computed properties for dynamic text formatting
- Implement real-time text validation

### For Make.com Scenarios
- Use text functions for string manipulation
- Implement proper error handling for text operations
- Format text consistently across modules

## Text Validation

### Common Patterns
```javascript
// Email validation
function isValidEmail(email) {
  const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return pattern.test(email);
}

// Phone number validation
function isValidPhone(phone) {
  const pattern = /^[\+]?[1-9][\d]{0,3}[\s\-\(\)]?[\d]{1,4}[\s\-\(\)]?[\d]{1,4}[\s\-\(\)]?[\d]{1,9}$/;
  return pattern.test(phone);
}

// URL validation
function isValidURL(url) {
  const pattern = /^https?:\/\/[^\s$.?#].[^\s]*$/;
  return pattern.test(url);
}
```

### Content Length Validation
```javascript
// Validate text length
function validateTextLength(text, min = 0, max = 1000) {
  if (!text || typeof text !== 'string') return false;
  const length = text.trim().length;
  return length >= min && length <= max;
}
```

## Database Configuration

### Text Field Setup
```javascript
// Text database field
{
  "field_name": "description",
  "field_type": "text",
  "max_length": 1000,
  "default_value": "",
  "required": false,
  "searchable": true
}

// Long text field
{
  "field_name": "content",
  "field_type": "longtext",
  "max_length": null, // No limit
  "allow_html": true
}
```

## API Response Patterns

### Clean Text API Response
```javascript
{
  "success": true,
  "data": {
    "title": "Product Name",
    "description": "Product description text",
    "content": "Full product details...",
    "slug": "product-name",
    "tags": ["tag1", "tag2", "tag3"]
  },
  "meta": {
    "character_count": 156,
    "word_count": 23,
    "reading_time": "1 min"
  }
}
```

## Related Functions
- [Text Filters](../filters/format__timestamp.md) - Text formatting operations
- [Text Functions](../../02-core-concepts/function-stack/text.md) - Advanced text manipulation
- [Configuring Expressions](../../05-advanced-features/expressions/configuring-expressions.md) - Using text in expressions

Text handling is fundamental to most applications in Xano. Master these patterns to build robust content management, user interfaces, and data processing workflows that integrate seamlessly with your favorite no-code platforms.