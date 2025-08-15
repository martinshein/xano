---
title: "Text Data Type and Functions"
description: "Master text manipulation and string operations in Xano function stacks for data processing and formatting"
category: function-stack
difficulty: beginner
tags:
  - text
  - strings
  - data-types
  - manipulation
  - formatting
  - validation
related_docs:
  - data-types
  - filters
  - expressions
  - validation
last_updated: '2025-01-23'
---

# Text Data Type and Functions

## Quick Summary
Text functions in Xano provide powerful string manipulation capabilities for processing user inputs, formatting outputs, and validating data. Essential for creating robust APIs that handle text data effectively.

## What You'll Learn
- Working with text data types in function stacks
- Essential text manipulation functions
- String validation and testing
- Text formatting for different outputs
- Best practices for handling user input
- Integration patterns with external systems

## Understanding Text Data Types

### Basic Text Operations

Text in Xano supports Unicode characters and can handle various string operations:

```javascript
// Text variable examples
{
  "user_name": "John Doe",
  "email": "john@example.com",
  "description": "Software developer with 5+ years experience",
  "formatted_phone": "+1 (555) 123-4567"
}
```

### Text Properties
- **Length**: Character count including spaces
- **Encoding**: UTF-8 support for international characters
- **Case sensitivity**: Preserved unless explicitly modified
- **Whitespace**: Leading/trailing spaces preserved

## Core Text Functions

### Adding and Removing Text

**Append**: Add text to the end
```javascript
// Example: Add file extension
input: "document"
append: ".pdf"
result: "document.pdf"
```

**Prepend**: Add text to the beginning  
```javascript
// Example: Add URL protocol
input: "example.com"
prepend: "https://"
result: "https://example.com"
```

**Trim**: Remove whitespace from both sides
```javascript
// Example: Clean user input
input: "  john@example.com  "
trim: true
result: "john@example.com"
```

**Left Trim**: Remove whitespace from left side
```javascript
// Example: Clean leading spaces
input: "   Hello World"
left_trim: true
result: "Hello World"
```

**Right Trim**: Remove whitespace from right side
```javascript
// Example: Clean trailing spaces  
input: "Hello World   "
right_trim: true
result: "Hello World"
```

### Text Testing and Validation

**Starts With**: Check if text begins with specific string
```javascript
// Example: Validate email domain
input: "john@company.com"
starts_with: "john@"
result: true
```

**Ends With**: Check if text ends with specific string
```javascript
// Example: Check file type
input: "document.pdf"
ends_with: ".pdf"
result: true
```

**Contains**: Check if text includes specific string
```javascript
// Example: Content filtering
input: "This is a test message"
contains: "test"
result: true
```

### Advanced Text Operations

**Replace**: Substitute text patterns
```javascript
// Example: Clean phone numbers
input: "(555) 123-4567"
replace: ["(", ")", " ", "-"]
with: ""
result: "5551234567"
```

**Split**: Break text into array
```javascript
// Example: Parse CSV data
input: "name,email,phone"
split: ","
result: ["name", "email", "phone"]
```

**Join**: Combine array into text
```javascript
// Example: Create full name
input: ["John", "Doe"]
join: " "
result: "John Doe"
```

## Integration Patterns

### For n8n Users
Text processing for workflow automation:

```javascript
// n8n text manipulation example
{
  "user_input": "{{$node['Form'].json['name']}}",
  "processed": {
    "clean_name": "{{$node['Form'].json['name'].trim()}}",
    "email_domain": "{{$node['Form'].json['email'].split('@')[1]}}",
    "formatted_phone": "+1 {{$node['Form'].json['phone']}}"
  }
}
```

### For WeWeb Users
Dynamic text binding and formatting:

```javascript
// WeWeb text binding
{
  "display_name": "{{user.first_name}} {{user.last_name}}",
  "formatted_address": "{{address.street}}, {{address.city}} {{address.zip}}",
  "status_text": "{{status.toUpperCase()}}"
}
```

### API Response Formatting
Structure text data for consistent API responses:

```json
{
  "user": {
    "full_name": "{{first_name}} {{last_name}}",
    "display_email": "{{email.toLowerCase()}}",
    "formatted_bio": "{{bio.trim()}}",
    "profile_url": "https://example.com/users/{{username.toLowerCase()}}"
  }
}
```

## Common Use Cases

### User Input Validation

```javascript
// Email validation workflow
1. Trim whitespace from input
2. Convert to lowercase
3. Check contains "@" symbol
4. Validate domain format
5. Return cleaned email or error
```

### Content Processing

```javascript
// Blog post processing
1. Trim title and content
2. Extract tags from content
3. Generate URL slug from title
4. Format publication date
5. Calculate reading time
```

### Data Import/Export

```javascript
// CSV processing
1. Split CSV row by commas
2. Trim each field
3. Validate required fields
4. Format dates and numbers
5. Prepare for database insertion
```

## Try This
1. **Basic Operations**: Practice append, prepend, and trim functions
2. **Validation Logic**: Create email and phone validation
3. **Format Conversion**: Transform user input to consistent format
4. **Content Processing**: Extract and format text from longer content
5. **API Integration**: Format data for external service consumption

## Common Mistakes to Avoid

❌ **Don't:**
- Forget to trim user inputs
- Ignore case sensitivity in comparisons
- Skip validation of required text fields
- Assume text format without checking
- Leave special characters unescaped

✅ **Do:**
- Always trim and validate user inputs
- Use consistent text formatting
- Handle empty and null text values
- Validate text length limits
- Escape special characters for security

## Pro Tips

💡 **Input Processing:**
- Trim all user inputs immediately
- Validate format before processing
- Normalize case for comparisons
- Check for required fields first

🚀 **Performance Optimization:**
- Cache formatted text when possible
- Batch text operations together
- Use filters for multiple operations
- Validate early to avoid processing invalid data

⚡ **Security Best Practices:**
- Sanitize all user text inputs
- Validate against expected patterns
- Limit text length appropriately
- Escape special characters for output

## Advanced Techniques

### Pattern Matching
Use regular expressions for complex validation:

```javascript
// Email pattern validation
pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
input: "user@example.com"
result: true
```

### Text Templates
Create dynamic text with placeholders:

```javascript
// Email template
template: "Hello {{name}}, welcome to {{company}}!"
variables: {
  "name": "John",
  "company": "Acme Corp"
}
result: "Hello John, welcome to Acme Corp!"
```

### Multi-language Support
Handle international text properly:

```javascript
// Unicode text handling
input: "Café résumé naïve"
operations: ["trim", "normalize"]
result: "Café résumé naïve"
```

## Performance Considerations

### Text Processing Efficiency
- Minimize string concatenation in loops
- Use built-in functions for common operations
- Cache processed text when reusing
- Validate input format early

### Memory Management
- Avoid storing large text strings unnecessarily
- Process text in chunks for large content
- Clean up temporary text variables
- Use streaming for large text processing

Text functions provide the foundation for robust data processing, ensuring your APIs handle text data reliably and consistently across all use cases.