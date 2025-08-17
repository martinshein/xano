---
title: Object Data Type Reference
description: Complete guide to working with objects in Xano - store, manipulate, and process structured data for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- object
- data-types
- json
- key-value
- structured-data
- nested-objects
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- array.md
- 02-core-concepts/function-stack/objects.md
- expressions/configuring-expressions.md
---

# Object Data Type Reference

## 📋 **Quick Summary**
Objects in Xano store structured key-value data in JSON format. Perfect for complex data structures, API responses, user profiles, and nested information in no-code platforms like n8n, WeWeb, and Make.com.

## What You'll Learn
- Object structure and JSON syntax
- Creating and manipulating objects
- Nested object operations
- Integration patterns for no-code platforms
- Best practices for object design
- Common object use cases

## Object Structure

Objects are contained within curly braces and store key-value pairs:

### Basic Object Syntax

**Simple Object:**
```javascript
{
  "name": "John Doe",
  "age": 30,
  "active": true
}
```

**Nested Objects:**
```javascript
{
  "user": {
    "profile": {
      "name": "Jane Smith",
      "email": "jane@example.com"
    },
    "preferences": {
      "theme": "dark",
      "notifications": true
    }
  }
}
```

**Objects with Arrays:**
```javascript
{
  "product": {
    "name": "Laptop",
    "tags": ["electronics", "computers"],
    "variants": [
      {"color": "black", "price": 999},
      {"color": "silver", "price": 1099}
    ]
  }
}
```

**Empty Object:**
```javascript
{}
```

## 🔄 **No-Code Platform Integration**

### n8n Integration
```javascript
// In n8n Set node - object manipulation
{
  "user_data": {
    "name": "{{$json.first_name}} {{$json.last_name}}",
    "contact": {
      "email": "{{$json.email}}",
      "phone": "{{$json.phone}}"
    },
    "metadata": {
      "created_at": "{{Date.now()}}",
      "source": "api_import"
    }
  }
}
```

### WeWeb Integration
```javascript
// WeWeb formula for object access
user.profile.address.city
// Object construction
{
  name: user.name,
  settings: {
    theme: 'dark',
    language: user.preferences?.language || 'en'
  }
}
```

### Make.com Integration
```javascript
// Make.com object operations
{
  "profile": {
    "user_id": "{{get(user.id)}}",
    "preferences": {
      "notifications": "{{get(settings.notifications)}}",
      "timezone": "{{get(user.timezone)}}"
    }
  }
}
```

## Common Object Use Cases

### User Profiles
```javascript
{
  "user_profile": {
    "basic_info": {
      "id": 123,
      "username": "johndoe",
      "email": "john@example.com",
      "full_name": "John Doe"
    },
    "personal_details": {
      "birth_date": "1990-05-15",
      "location": {
        "country": "USA",
        "state": "California",
        "city": "San Francisco"
      }
    },
    "preferences": {
      "language": "en",
      "timezone": "America/Los_Angeles",
      "notifications": {
        "email": true,
        "push": false,
        "sms": true
      }
    },
    "social_links": {
      "twitter": "@johndoe",
      "linkedin": "linkedin.com/in/johndoe",
      "website": "johndoe.dev"
    }
  }
}
```

### API Response Structure
```javascript
{
  "api_response": {
    "status": "success",
    "data": {
      "products": [
        {
          "id": 1,
          "name": "Product A",
          "pricing": {
            "base_price": 99.99,
            "currency": "USD",
            "discounts": {
              "bulk": 0.1,
              "seasonal": 0.15
            }
          }
        }
      ]
    },
    "meta": {
      "total_count": 150,
      "page": 1,
      "per_page": 20,
      "has_more": true
    }
  }
}
```

### Configuration Objects
```javascript
{
  "app_config": {
    "features": {
      "authentication": {
        "enabled": true,
        "providers": ["email", "google", "facebook"],
        "settings": {
          "require_verification": true,
          "password_strength": "medium"
        }
      },
      "payments": {
        "enabled": true,
        "providers": {
          "stripe": {
            "public_key": "pk_live_...",
            "webhook_endpoint": "/webhooks/stripe"
          },
          "paypal": {
            "client_id": "client_123",
            "sandbox_mode": false
          }
        }
      }
    }
  }
}
```

## 💡 **Try This: E-commerce Product System**

Create a comprehensive product management object:

```javascript
{
  "product": {
    "basic_info": {
      "id": 12345,
      "sku": "LAPTOP-MBP-16-2024",
      "name": "MacBook Pro 16-inch",
      "brand": "Apple",
      "category": {
        "primary": "Electronics",
        "secondary": "Computers",
        "tertiary": "Laptops"
      }
    },
    "specifications": {
      "processor": "M3 Pro",
      "memory": "18GB",
      "storage": "512GB SSD",
      "display": {
        "size": "16.2 inches",
        "resolution": "3456 x 2234",
        "type": "Liquid Retina XDR"
      },
      "connectivity": {
        "ports": ["Thunderbolt 4", "HDMI", "MagSafe 3"],
        "wireless": ["WiFi 6E", "Bluetooth 5.3"]
      }
    },
    "pricing": {
      "base_price": 2499.00,
      "currency": "USD",
      "tax_rate": 0.08,
      "shipping": {
        "standard": 0,
        "express": 29.99,
        "overnight": 59.99
      }
    },
    "inventory": {
      "stock_level": 45,
      "reserved": 12,
      "available": 33,
      "reorder_point": 10,
      "supplier_info": {
        "name": "Apple Inc.",
        "lead_time_days": 14
      }
    },
    "media": {
      "images": [
        {
          "url": "/images/mbp-16-front.jpg",
          "alt": "MacBook Pro 16-inch front view",
          "is_primary": true
        },
        {
          "url": "/images/mbp-16-side.jpg",
          "alt": "MacBook Pro 16-inch side view",
          "is_primary": false
        }
      ],
      "videos": [
        {
          "url": "/videos/mbp-16-demo.mp4",
          "title": "Product Demo",
          "duration": 120
        }
      ]
    }
  }
}
```

## Object Operations

### Accessing Properties
```javascript
// Dot notation
user.profile.name

// Bracket notation
user["profile"]["name"]

// Safe access (handles null/undefined)
user?.profile?.name
```

### Modifying Objects
```javascript
// Add property
user.last_login = now()

// Update nested property
user.preferences.theme = "dark"

// Remove property
delete user.temporary_data
```

### Object Merging
```javascript
// Merge objects
merge(user_defaults, user_input)

// Deep merge
deep_merge(base_config, user_config)
```

## ⚠️ **Common Mistakes to Avoid**

1. **Missing Quotes**: All keys must be in quotes in JSON
2. **Trailing Commas**: JSON doesn't allow trailing commas
3. **Circular References**: Avoid objects that reference themselves
4. **Deep Nesting**: Limit nesting levels for performance

### Safe Object Handling
```javascript
// Problem: Accessing undefined properties
user.profile.address.city  // Error if profile is null

// Solution: Safe property access
user?.profile?.address?.city || "Unknown"

// Alternative: Check before access
if (user && user.profile && user.profile.address) {
  return user.profile.address.city;
}
```

## 🚀 **Pro Tips**

### Object Validation
```javascript
// Validate required properties
function validateUser(user) {
  const required = ['name', 'email', 'id'];
  return required.every(field => user.hasOwnProperty(field));
}

// Type checking
function isObject(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}
```

### Object Transformation
```javascript
// Extract specific fields
function extractUserSummary(user) {
  return {
    id: user.id,
    name: user.profile.name,
    email: user.contact.email,
    active: user.status.active
  };
}

// Flatten nested object
function flattenObject(obj, prefix = '') {
  let result = {};
  for (let key in obj) {
    if (typeof obj[key] === 'object' && obj[key] !== null) {
      Object.assign(result, flattenObject(obj[key], prefix + key + '.'));
    } else {
      result[prefix + key] = obj[key];
    }
  }
  return result;
}
```

### Performance Optimization
```javascript
// Good: Shallow objects for frequent access
{
  "user_id": 123,
  "name": "John",
  "status": "active"
}

// Better: Group related data
{
  "user": {
    "id": 123,
    "name": "John"
  },
  "status": {
    "active": true,
    "last_seen": 1705507200000
  }
}
```

## Integration Best Practices

### For n8n Workflows
- Use Set nodes to construct complex objects
- Handle nested property access safely
- Validate object structure before processing

### For WeWeb Apps
- Bind object properties to UI components
- Use computed properties for object transformations
- Implement proper loading states for object data

### For Make.com Scenarios
- Use get() function for safe property access
- Construct objects step by step in complex scenarios
- Handle object arrays with iterator modules

## Database Storage

### JSON Field Configuration
```javascript
// JSON database field
{
  "field_name": "user_preferences",
  "field_type": "json",
  "default_value": {},
  "validation": {
    "max_size": "10KB",
    "required_keys": ["theme", "language"]
  }
}
```

### Querying JSON Fields
```sql
-- Query JSON properties
SELECT * FROM users 
WHERE JSON_EXTRACT(preferences, '$.theme') = 'dark'

-- Update JSON property
UPDATE users 
SET preferences = JSON_SET(preferences, '$.notifications.email', true)
WHERE id = 123
```

## API Response Patterns

### Consistent Object Structure
```javascript
// Good: Consistent response format
{
  "success": true,
  "data": {
    "user": {
      "id": 123,
      "profile": {
        "name": "John Doe",
        "avatar": "/avatars/123.jpg"
      }
    }
  },
  "meta": {
    "timestamp": 1705507200000,
    "version": "1.0"
  }
}
```

## Related Functions
- [Array Data Type](array.md) - Working with arrays
- [Object Functions](../../02-core-concepts/function-stack/objects.md) - Advanced object operations
- [Configuring Expressions](../../05-advanced-features/expressions/configuring-expressions.md) - Using objects in expressions

Objects are the foundation for complex data structures in Xano. Master these patterns to build sophisticated applications that handle rich, nested data efficiently across all your no-code platform integrations.