---
title: "Custom Functions - Reusable Code Components"
description: "Create and manage custom functions in Xano for reusable code components, modular design patterns, and efficient development workflows"
category: function-stack
tags:
  - Custom Functions
  - Reusable Code
  - Modular Design
  - Code Organization
  - Function Libraries
difficulty: intermediate
reading_time: 8 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of function stacks
  - Knowledge of programming concepts
  - Familiarity with modular design
---

# Custom Functions - Reusable Code Components

## 📋 **Quick Summary**

**What it does:** Custom functions allow you to create reusable code components that can be called from multiple function stacks, promoting code reuse, maintainability, and modular design.

**Why it matters:** Custom functions enable you to:
- **Reduce code duplication** by creating reusable components
- **Improve maintainability** with centralized logic
- **Build function libraries** for common operations
- **Standardize implementations** across your application
- **Accelerate development** with proven components

**Time to implement:** 10-15 minutes for basic functions, 30+ minutes for complex utilities

---

## What You'll Learn

- How to create and manage custom functions
- Best practices for reusable code design
- Common patterns for function libraries
- Parameter handling and return values
- Testing and documentation strategies

## Creating Custom Functions

### Basic Function Structure

```javascript
// Custom Function: validateEmail
// Input: email (string)
// Output: { valid: boolean, message: string }

function validateEmail(email) {
  const result = {
    valid: false,
    message: ''
  };
  
  // Check if email is provided
  if (!email || typeof email !== 'string') {
    result.message = 'Email is required';
    return result;
  }
  
  // Trim whitespace
  email = email.trim();
  
  // Check email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    result.message = 'Invalid email format';
    return result;
  }
  
  // Check email length
  if (email.length > 254) {
    result.message = 'Email address too long';
    return result;
  }
  
  result.valid = true;
  result.message = 'Valid email address';
  return result;
}
```

## Utility Function Examples

### String Processing

```javascript
// Generate URL-friendly slug
function generateSlug(text, maxLength = 50) {
  if (!text || typeof text !== 'string') {
    return '';
  }
  
  let slug = text
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
  
  if (slug.length > maxLength) {
    slug = slug.substring(0, maxLength).replace(/-[^-]*$/, '');
  }
  
  return slug || 'untitled';
}

// Truncate text with ellipsis
function truncateText(text, length = 100, suffix = '...') {
  if (!text || typeof text !== 'string') {
    return '';
  }
  
  if (text.length <= length) {
    return text;
  }
  
  return text.substring(0, length - suffix.length).trim() + suffix;
}
```

### Date and Time Utilities

```javascript
// Format date for display
function formatDate(timestamp, format = 'YYYY-MM-DD') {
  try {
    const date = new Date(timestamp);
    
    if (isNaN(date.getTime())) {
      return null;
    }
    
    switch (format) {
      case 'YYYY-MM-DD':
        return date.toISOString().split('T')[0];
      case 'MM/DD/YYYY':
        return date.toLocaleDateString('en-US');
      case 'DD/MM/YYYY':
        return date.toLocaleDateString('en-GB');
      default:
        return date.toLocaleDateString();
    }
  } catch (error) {
    return null;
  }
}

// Calculate age from birth date
function calculateAge(birthDate) {
  try {
    const birth = new Date(birthDate);
    const today = new Date();
    
    if (isNaN(birth.getTime()) || birth > today) {
      return null;
    }
    
    let age = today.getFullYear() - birth.getFullYear();
    const monthDiff = today.getMonth() - birth.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
      age--;
    }
    
    return age;
  } catch (error) {
    return null;
  }
}
```

### Business Logic Functions

```javascript
// Calculate tax amount
function calculateTax(amount, taxRate, inclusive = false) {
  if (typeof amount !== 'number' || amount < 0) {
    throw new Error('Invalid amount');
  }
  
  if (typeof taxRate !== 'number' || taxRate < 0 || taxRate > 1) {
    throw new Error('Tax rate must be between 0 and 1');
  }
  
  let taxAmount, netAmount, totalAmount;
  
  if (inclusive) {
    // Tax included in amount
    totalAmount = amount;
    netAmount = amount / (1 + taxRate);
    taxAmount = amount - netAmount;
  } else {
    // Tax added to amount
    netAmount = amount;
    taxAmount = amount * taxRate;
    totalAmount = amount + taxAmount;
  }
  
  return {
    netAmount: Math.round(netAmount * 100) / 100,
    taxAmount: Math.round(taxAmount * 100) / 100,
    totalAmount: Math.round(totalAmount * 100) / 100,
    taxRate: taxRate
  };
}

// Calculate discount
function calculateDiscount(originalPrice, discountValue, discountType = 'percentage') {
  if (typeof originalPrice !== 'number' || originalPrice < 0) {
    throw new Error('Invalid original price');
  }
  
  let discountAmount = 0;
  
  switch (discountType) {
    case 'percentage':
      if (discountValue > 100) discountValue = 100;
      discountAmount = (originalPrice * discountValue) / 100;
      break;
    case 'fixed':
      discountAmount = Math.min(discountValue, originalPrice);
      break;
    default:
      throw new Error('Invalid discount type');
  }
  
  const finalPrice = originalPrice - discountAmount;
  const savingsPercentage = (discountAmount / originalPrice) * 100;
  
  return {
    originalPrice: originalPrice,
    discountAmount: Math.round(discountAmount * 100) / 100,
    finalPrice: Math.round(finalPrice * 100) / 100,
    savingsPercentage: Math.round(savingsPercentage * 100) / 100
  };
}
```

## Advanced Validation Functions

### Comprehensive Input Validator

```javascript
// Multi-field validation function
function validateUserInput(userData, rules) {
  const result = {
    valid: true,
    errors: [],
    cleaned: {}
  };
  
  if (!userData || typeof userData !== 'object') {
    result.valid = false;
    result.errors.push('Invalid input data');
    return result;
  }
  
  for (const [field, fieldRules] of Object.entries(rules)) {
    const value = userData[field];
    
    // Required field check
    if (fieldRules.required && (!value && value !== 0)) {
      result.valid = false;
      result.errors.push(`${field} is required`);
      continue;
    }
    
    // Skip if optional and empty
    if (!fieldRules.required && (!value && value !== 0)) {
      continue;
    }
    
    // Type validation
    if (fieldRules.type && !validateType(value, fieldRules.type)) {
      result.valid = false;
      result.errors.push(`${field} must be of type ${fieldRules.type}`);
      continue;
    }
    
    // Length validation
    if (fieldRules.minLength && typeof value === 'string' && value.length < fieldRules.minLength) {
      result.valid = false;
      result.errors.push(`${field} must be at least ${fieldRules.minLength} characters`);
      continue;
    }
    
    // Pattern validation
    if (fieldRules.pattern && typeof value === 'string' && !new RegExp(fieldRules.pattern).test(value)) {
      result.valid = false;
      result.errors.push(`${field} format is invalid`);
      continue;
    }
    
    // Clean and store
    result.cleaned[field] = typeof value === 'string' ? value.trim() : value;
  }
  
  return result;
}

// Type validation helper
function validateType(value, expectedType) {
  switch (expectedType) {
    case 'string': return typeof value === 'string';
    case 'number': return typeof value === 'number' && !isNaN(value);
    case 'integer': return Number.isInteger(Number(value));
    case 'boolean': return typeof value === 'boolean';
    case 'email': return typeof value === 'string' && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    case 'url':
      try {
        new URL(value);
        return true;
      } catch {
        return false;
      }
    default: return true;
  }
}
```

## Security and Authentication

### Password Validation

```javascript
// Comprehensive password validation
function validatePassword(password, requirements = {}) {
  const rules = {
    minLength: 8,
    requireUppercase: true,
    requireLowercase: true,
    requireNumbers: true,
    requireSymbols: false,
    ...requirements
  };
  
  const result = {
    valid: true,
    errors: [],
    strength: 0,
    strengthLabel: ''
  };
  
  if (!password || typeof password !== 'string') {
    result.valid = false;
    result.errors.push('Password is required');
    return result;
  }
  
  // Length check
  if (password.length < rules.minLength) {
    result.valid = false;
    result.errors.push(`Password must be at least ${rules.minLength} characters`);
  } else {
    result.strength += 25;
  }
  
  // Character checks
  if (rules.requireUppercase && !/[A-Z]/.test(password)) {
    result.valid = false;
    result.errors.push('Password must contain uppercase letters');
  } else if (/[A-Z]/.test(password)) {
    result.strength += 25;
  }
  
  if (rules.requireLowercase && !/[a-z]/.test(password)) {
    result.valid = false;
    result.errors.push('Password must contain lowercase letters');
  } else if (/[a-z]/.test(password)) {
    result.strength += 25;
  }
  
  if (rules.requireNumbers && !/\d/.test(password)) {
    result.valid = false;
    result.errors.push('Password must contain numbers');
  } else if (/\d/.test(password)) {
    result.strength += 25;
  }
  
  if (rules.requireSymbols && !/[^a-zA-Z0-9]/.test(password)) {
    result.valid = false;
    result.errors.push('Password must contain special characters');
  }
  
  // Set strength label
  if (result.strength < 50) result.strengthLabel = 'Weak';
  else if (result.strength < 75) result.strengthLabel = 'Medium';
  else result.strengthLabel = 'Strong';
  
  return result;
}

// Generate secure token
function generateSecureToken(length = 32) {
  const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  let token = '';
  
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * chars.length);
    token += chars[randomIndex];
  }
  
  return token;
}
```

## Testing Custom Functions

### Function Testing Pattern

```javascript
// Test runner for custom functions
function testFunction(functionName, testCases) {
  const results = [];
  
  for (const testCase of testCases) {
    try {
      const actual = eval(`${functionName}(${JSON.stringify(testCase.input).slice(1, -1)})`);
      const passed = JSON.stringify(actual) === JSON.stringify(testCase.expected);
      
      results.push({
        input: testCase.input,
        expected: testCase.expected,
        actual: actual,
        passed: passed,
        description: testCase.description
      });
    } catch (error) {
      results.push({
        input: testCase.input,
        expected: testCase.expected,
        actual: error.message,
        passed: false,
        description: testCase.description,
        error: true
      });
    }
  }
  
  return {
    functionName: functionName,
    total: testCases.length,
    passed: results.filter(r => r.passed).length,
    failed: results.filter(r => !r.passed).length,
    results: results
  };
}

// Example test suite
function runEmailValidationTests() {
  const testCases = [
    {
      input: 'test@example.com',
      expected: { valid: true, message: 'Valid email address' },
      description: 'Valid email should pass'
    },
    {
      input: 'invalid-email',
      expected: { valid: false, message: 'Invalid email format' },
      description: 'Invalid format should fail'
    },
    {
      input: '',
      expected: { valid: false, message: 'Email is required' },
      description: 'Empty email should fail'
    }
  ];
  
  return testFunction('validateEmail', testCases);
}
```

## 💡 **Try This**

### Beginner Challenge
Create basic utility functions:
1. Email validation function
2. Date formatting utility
3. String manipulation helpers
4. Basic calculation functions

### Intermediate Challenge
Build function libraries:
1. Complete validation library
2. E-commerce calculation suite
3. Text processing toolkit
4. Date/time utility collection

### Advanced Challenge
Create enterprise utilities:
1. Security function library
2. Data transformation pipeline
3. Business rule engine components
4. Performance optimization utilities

## Best Practices

1. **Single responsibility** - Each function should do one thing well
2. **Clear naming** - Function names should describe their purpose
3. **Input validation** - Always validate parameters
4. **Error handling** - Return meaningful error messages
5. **Documentation** - Document parameters and return values
6. **Testing** - Create test functions for validation

## Next Steps

- Learn [Function Stacks](../function-stack/) for using custom functions
- Explore [Testing](testing-and-debugging-function-stacks.md) for quality assurance
- Master [Best Practices](../../best-practices/code-organization.md) for maintainable code
- Understand [Performance](../../best-practices/performance.md) optimization

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Custom function discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Function development guides
- 📖 [Code Examples](../../examples/custom-functions.md) - Real-world implementations
- 🔧 [Support](https://xano.com/support) - Development assistance