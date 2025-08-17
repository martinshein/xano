---
title: Boolean Data Type Reference
description: Complete guide to working with boolean values in Xano - true/false logic for conditions, flags, and decision-making in no-code workflows
category: functions
subcategory: 08-reference/functions
tags:
- boolean
- data-types
- true-false
- conditional-logic
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: beginner
has_code_examples: true
related_docs:
- 05-advanced-features/conditionals/the-development-life-cycle.md
- 02-core-concepts/function-stack/conditional.md
- expressions/configuring-expressions.md
---

# Boolean Data Type Reference

## 📋 **Quick Summary**
Boolean values represent true/false logic in Xano. Essential for feature flags, user permissions, status tracking, and conditional workflows in no-code platforms like n8n, WeWeb, and Make.com.

## What You'll Learn
- Boolean value syntax and usage
- Creating conditional logic with booleans
- Boolean operations and comparisons
- Integration patterns for no-code platforms
- Best practices for boolean flags
- Common boolean use cases

## Boolean Values

Boolean data type has only two possible values:
- `true` (enabled, yes, on, active)
- `false` (disabled, no, off, inactive)

### Basic Boolean Syntax

**Simple Boolean Values:**
```javascript
true
false
```

**In Objects:**
```javascript
{
  "is_active": true,
  "is_premium": false,
  "email_verified": true,
  "notifications_enabled": false
}
```

**In Arrays:**
```javascript
[true, false, true, true, false]
```

## 🔄 **No-Code Platform Integration**

### n8n Integration
```javascript
// In n8n If node - condition based on boolean
{
  "conditions": {
    "boolean": [
      {
        "value1": "{{$json.user.is_active}}",
        "operation": "equal",
        "value2": true
      }
    ]
  }
}
```

### WeWeb Integration
```javascript
// WeWeb conditional display formula
user.is_premium && user.subscription_active
```

### Make.com Integration
```javascript
// Make.com filter condition
{
  "condition": "{{user.email_verified}} = true AND {{user.account_status}} = active"
}
```

## Common Boolean Use Cases

### User Management
```javascript
{
  "user_id": 123,
  "is_active": true,
  "email_verified": true,
  "is_premium": false,
  "notifications": {
    "email": true,
    "sms": false,
    "push": true
  }
}
```

### Feature Flags
```javascript
{
  "features": {
    "dark_mode": true,
    "beta_features": false,
    "advanced_search": true,
    "ai_assistant": false
  }
}
```

### Content Management
```javascript
{
  "post_id": 456,
  "title": "My Blog Post",
  "is_published": true,
  "is_featured": false,
  "allow_comments": true,
  "is_pinned": false
}
```

## Boolean Operations

### Comparison Operations
```javascript
// Equal comparison
user.is_active == true

// Not equal comparison
user.is_banned != true

// Direct boolean check
user.is_verified  // true or false
```

### Logical Operations
```javascript
// AND operation
user.is_active && user.email_verified

// OR operation
user.is_admin || user.is_moderator

// NOT operation
!user.is_suspended
```

## 💡 **Try This: User Permission System**

Create a boolean-based permission system:

```javascript
{
  "user_id": 789,
  "permissions": {
    "can_read": true,
    "can_write": false,
    "can_delete": false,
    "can_admin": false
  },
  "features": {
    "premium_content": true,
    "api_access": false,
    "priority_support": true
  },
  "settings": {
    "email_notifications": true,
    "sms_notifications": false,
    "marketing_emails": false,
    "security_alerts": true
  }
}
```

## Boolean in Database Fields

### Field Configuration
```javascript
// Boolean database field setup
{
  "field_name": "is_active",
  "field_type": "boolean",
  "default_value": true,
  "required": true
}
```

### Query Examples
```javascript
// Find active users
WHERE is_active = true

// Find users with verified emails
WHERE email_verified = true AND is_active = true

// Find inactive premium users
WHERE is_premium = true AND is_active = false
```

## ⚠️ **Common Mistakes to Avoid**

1. **String vs Boolean**: Don't use `"true"` (string) instead of `true` (boolean)
2. **Null Confusion**: Remember `null` is not the same as `false`
3. **Inconsistent Naming**: Use clear, consistent boolean field names
4. **Default Values**: Always set appropriate default values for boolean fields

## 🚀 **Pro Tips**

### Naming Conventions
```javascript
// Good boolean naming patterns
{
  "is_active": true,      // State
  "has_access": false,    // Possession
  "can_edit": true,       // Permission
  "should_notify": false, // Instruction
  "was_sent": true        // Past action
}
```

### Boolean Aggregation
```javascript
// Count boolean values
SELECT 
  COUNT(*) as total_users,
  SUM(is_active) as active_users,
  SUM(is_premium) as premium_users
FROM users
```

### Toggle Functionality
```javascript
// Toggle boolean value
UPDATE users 
SET is_active = NOT is_active 
WHERE user_id = 123
```

## Integration Best Practices

### For n8n Workflows
- Use Switch nodes for multiple boolean conditions
- Implement proper boolean validation in Set nodes
- Use boolean fields for workflow routing decisions

### For WeWeb Apps
- Bind boolean values to toggle components
- Use boolean expressions for conditional styling
- Implement boolean-based user interface states

### For Make.com Scenarios
- Use boolean filters for scenario routing
- Set up boolean-based trigger conditions
- Implement boolean status tracking across modules

## Boolean Conversion

### From Other Types
```javascript
// String to boolean
"true" → true (using proper conversion)
"false" → false
"" → false (empty string)
"anything" → true (non-empty string)

// Number to boolean
0 → false
1 → true
-1 → true (any non-zero)

// Null/undefined to boolean
null → false
undefined → false
```

### API Response Patterns
```javascript
// Clean boolean API response
{
  "success": true,
  "data": {
    "user": {
      "is_active": true,
      "permissions": {
        "read": true,
        "write": false
      }
    }
  },
  "has_more": false
}
```

## Related Functions
- [Conditional Functions](../../02-core-concepts/function-stack/conditional.md) - Using booleans in conditions
- [Configuring Expressions](../../05-advanced-features/expressions/configuring-expressions.md) - Boolean expressions
- [Development Lifecycle](../../05-advanced-features/conditionals/the-development-life-cycle.md) - Boolean logic in workflows

Boolean values are the backbone of decision-making in Xano. Use them effectively to create smart, responsive applications that adapt to user needs and business logic.