---
title: "Object Data Type"
description: "Work with JSON objects and complex data structures in Xano function stacks for sophisticated data manipulation"
category: function-stack
difficulty: beginner
tags:
  - object
  - json
  - data-types
  - key-value
  - data-structures
related_docs:
  - objects
  - arrays
  - data-manipulation
  - expressions
last_updated: '2025-01-23'
---

# Object Data Type

## Quick Summary
Objects in Xano are JSON-like data structures that store information using key-value pairs. Think of them as labeled containers where each label (key) points to a specific piece of data (value). Objects are fundamental for organizing complex data and building sophisticated APIs.

## What You'll Learn
- Understanding object structure and key-value pairs
- Creating and manipulating objects in function stacks
- Working with nested objects and complex data
- Best practices for object design in APIs

## Object Structure

### Basic Object Format
```json
{
  "key1": "value1",
  "key2": 123,
  "key3": true,
  "key4": null
}
```

### Real-World Example: User Profile
```json
{
  "userId": 12345,
  "email": "john@example.com",
  "profile": {
    "firstName": "John",
    "lastName": "Doe",
    "age": 28,
    "preferences": {
      "theme": "dark",
      "language": "en",
      "notifications": true
    }
  },
  "roles": ["user", "subscriber"],
  "lastLogin": "2025-01-23T10:30:00Z",
  "isActive": true
}
```

## Object Operations in Xano

### Creating Objects
- **Build Object** - Construct objects from individual values
- **Merge Objects** - Combine multiple objects
- **Transform** - Restructure object properties
- **Pick Fields** - Select specific properties
- **Omit Fields** - Remove unwanted properties

### Accessing Object Data
- **Dot Notation** - `user.profile.firstName`
- **Bracket Notation** - `user["profile"]["firstName"]`
- **Safe Access** - Handle missing properties gracefully

## Working with Nested Objects

### E-commerce Order Example
```json
{
  "orderId": "ORD-2025-001",
  "customer": {
    "id": 456,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "address": {
      "street": "123 Main St",
      "city": "Springfield",
      "state": "IL",
      "zipCode": "62701",
      "country": "USA"
    }
  },
  "items": [
    {
      "productId": 789,
      "name": "Wireless Headphones",
      "quantity": 1,
      "price": 99.99,
      "category": "Electronics"
    },
    {
      "productId": 790,
      "name": "Phone Case",
      "quantity": 2,
      "price": 24.99,
      "category": "Accessories"
    }
  ],
  "totals": {
    "subtotal": 149.97,
    "tax": 12.00,
    "shipping": 5.99,
    "total": 167.96
  },
  "status": "confirmed",
  "createdAt": "2025-01-23T09:15:00Z"
}
```

## Integration with n8n

### Preparing Data for n8n
```javascript
// Transform Xano object for n8n consumption
{
  "webhook_data": {
    "event_type": "order_created",
    "order": {
      "id": order.orderId,
      "customer_email": order.customer.email,
      "total_amount": order.totals.total,
      "item_count": order.items.length
    },
    "timestamp": new Date().toISOString()
  }
}
```

### n8n Webhook Processing
```javascript
// n8n Function Node - Process Xano object
const orderData = $json.webhook_data.order;

return {
  customerEmail: orderData.customer_email,
  orderTotal: orderData.total_amount,
  itemCount: orderData.item_count,
  shouldSendEmail: orderData.total_amount > 100
};
```

## Integration with WeWeb

### WeWeb Component Data Binding
```javascript
// WeWeb component expecting user object
export default {
  props: {
    user: {
      type: Object,
      required: true
    }
  },
  
  computed: {
    displayName() {
      return `${this.user.profile.firstName} ${this.user.profile.lastName}`;
    },
    
    canEdit() {
      return this.user.roles.includes('admin') || 
             this.user.roles.includes('editor');
    },
    
    profileImage() {
      return this.user.profile.avatar || '/default-avatar.png';
    }
  },
  
  methods: {
    async updatePreferences(newPrefs) {
      const updatedUser = {
        ...this.user,
        profile: {
          ...this.user.profile,
          preferences: {
            ...this.user.profile.preferences,
            ...newPrefs
          }
        }
      };
      
      await this.$xano.patch('/users/me', updatedUser);
    }
  }
};
```

## Object Validation Patterns

### Required Field Validation
```json
{
  "validation_rules": {
    "required_fields": ["email", "firstName", "lastName"],
    "optional_fields": ["phone", "company", "bio"],
    "nested_required": {
      "address": ["street", "city", "zipCode"],
      "preferences": ["language"]
    }
  }
}
```

### Data Type Validation
```json
{
  "field_types": {
    "email": "string",
    "age": "integer",
    "isActive": "boolean",
    "preferences": "object",
    "roles": "array",
    "lastLogin": "timestamp"
  }
}
```

## Try This: Build a Dynamic Form Object

Create a function stack that:
1. **Receives form data** as an object
2. **Validates required fields** exist
3. **Sanitizes input values** (trim strings, validate emails)
4. **Structures data** for database storage
5. **Returns formatted response** with success/error information

```json
{
  "input": {
    "firstName": "  John  ",
    "lastName": "Doe",
    "email": "JOHN@EXAMPLE.COM",
    "preferences": {
      "newsletter": true,
      "theme": "dark"
    }
  },
  "output": {
    "success": true,
    "user": {
      "firstName": "John",
      "lastName": "Doe", 
      "email": "john@example.com",
      "preferences": {
        "newsletter": true,
        "theme": "dark",
        "language": "en"
      }
    }
  }
}
```

## Advanced Object Patterns

### Object Composition
```json
{
  "base_user": {
    "id": 123,
    "email": "user@example.com"
  },
  "permissions": {
    "canRead": true,
    "canWrite": false,
    "canDelete": false
  },
  "metadata": {
    "createdAt": "2025-01-23T10:00:00Z",
    "updatedAt": "2025-01-23T10:30:00Z",
    "version": 1
  }
}
```

### Object Transformation
```json
// Before: Database format
{
  "user_id": 123,
  "first_name": "John",
  "last_name": "Doe",
  "email_address": "john@example.com"
}

// After: API format
{
  "id": 123,
  "displayName": "John Doe",
  "email": "john@example.com",
  "profileUrl": "/users/123"
}
```

## Common Mistakes to Avoid

❌ **Deep nesting** - Keep object structure as flat as reasonable
❌ **Inconsistent naming** - Use consistent key naming conventions
❌ **Missing null checks** - Always validate object properties exist
❌ **Large objects** - Break down complex objects into manageable pieces
❌ **Sensitive data exposure** - Don't include passwords or tokens in objects

## Pro Tips

💡 **Use consistent naming** - snake_case for database, camelCase for APIs
💡 **Validate object structure** before processing to prevent errors
💡 **Document object schemas** for API consumers
💡 **Use object composition** to build complex data from simple parts
💡 **Implement object versioning** for API evolution
💡 **Cache frequently accessed objects** to improve performance
💡 **Sanitize object data** before storage or transmission

## Performance Considerations

### Object Size Management
- Keep objects focused and avoid unnecessary data
- Use pagination for large object collections
- Implement field selection (pick/omit) for API responses

### Memory Efficiency
- Avoid deep copying large objects unnecessarily
- Use object references where appropriate
- Clean up temporary objects in long-running processes

Objects are the building blocks of sophisticated data structures in Xano, enabling you to model complex real-world scenarios effectively.