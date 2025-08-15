---
title: "Switch Function"
description: "Implement efficient multi-path logic using Xano's Switch function for clean conditional branching"
category: function-stack
difficulty: beginner
tags:
  - switch
  - conditional
  - logic
  - branching
  - control-flow
related_docs:
  - conditional
  - loops
  - data-manipulation
  - expressions
last_updated: '2025-01-23'
---

# Switch Function

## Quick Summary
Switch functions provide an efficient way to handle multiple conditional paths based on a single value. Think of it as a clean alternative to multiple if-then statements when you need to check one variable against many possible values.

## What You'll Learn
- When to use Switch vs Conditional statements
- Building efficient multi-path logic
- Real-world Switch function patterns
- Performance benefits of Switch over nested conditionals

## Switch vs Conditional - When to Use Each

### Use Switch When:
- **Single value checking** - Testing one variable against multiple options
- **Simple equality comparisons** - "If color is red, blue, green..."
- **Menu/option handling** - Processing user selections
- **Status-based workflows** - Different actions for each status
- **Clean, readable code** - Multiple similar conditions

### Use Conditional When:
- **Complex logic** - "If user joined before 2020 AND is subscriber"
- **Range comparisons** - "If age is between 18 and 65"
- **Multiple variables** - Comparing different fields together
- **Boolean operations** - Complex AND/OR conditions

## Basic Switch Structure

### Example: Order Status Processing
```
Switch on: order.status
├── Case: "pending" → Send confirmation email
├── Case: "processing" → Update inventory
├── Case: "shipped" → Generate tracking
├── Case: "delivered" → Request review
└── Default → Log unknown status
```

### User Role Permissions
```
Switch on: user.role
├── Case: "admin" → Full access permissions
├── Case: "editor" → Content editing permissions  
├── Case: "viewer" → Read-only permissions
├── Case: "guest" → Limited access
└── Default → Deny access
```

## Real-World Use Cases

### 1. E-commerce Order Processing
```
Switch on: payment.status
├── "completed" → 
    ├── Update order status
    ├── Send receipt
    └── Begin fulfillment
├── "failed" →
    ├── Send payment failed email
    └── Hold order
├── "pending" →
    └── Send pending notification
└── Default → Log error
```

### 2. User Subscription Handling
```
Switch on: subscription.tier
├── "premium" →
    ├── Access all features
    ├── Priority support
    └── Advanced analytics
├── "standard" →
    ├── Core features only
    └── Standard support
├── "trial" →
    ├── Limited features
    └── Trial messaging
└── Default → Redirect to signup
```

### 3. Content Moderation
```
Switch on: content.type
├── "image" → Run image moderation API
├── "video" → Queue for manual review
├── "text" → Check against word filters
├── "audio" → Convert to text and check
└── Default → Approve automatically
```

## Integration with n8n

### Processing Webhook Data
```javascript
// n8n Function Node - Prepare data for Xano Switch
const eventType = $json.event_type;
const eventData = $json.data;

// Send to Xano endpoint with Switch function
return {
  switch_value: eventType,
  event_data: eventData,
  timestamp: new Date().toISOString()
};
```

### Xano Switch Response
```
Switch on: input.switch_value
├── "user_signup" → Create user record + send welcome email
├── "payment_completed" → Update subscription + send receipt
├── "support_ticket" → Create ticket + notify team
├── "product_review" → Store review + update ratings
└── Default → Log unknown event type
```

## Integration with WeWeb

### Dynamic UI Rendering
```javascript
// WeWeb component using Switch-processed data
export default {
  props: {
    userStatus: String,
    userData: Object
  },
  
  computed: {
    // Switch function in Xano already processed the status
    // Now we just use the results
    displayContent() {
      return this.userData.content_for_status;
    },
    
    availableActions() {
      return this.userData.allowed_actions || [];
    },
    
    statusClass() {
      const statusClasses = {
        'active': 'text-green-500',
        'pending': 'text-yellow-500', 
        'suspended': 'text-red-500',
        'trial': 'text-blue-500'
      };
      return statusClasses[this.userStatus] || 'text-gray-500';
    }
  }
};
```

## Try This: Build a Notification Router

Create a Switch function that routes notifications based on type:

1. **Email notifications** → Format for email service
2. **SMS notifications** → Format for SMS gateway
3. **Push notifications** → Format for mobile push
4. **In-app notifications** → Store in user notifications table
5. **Webhook notifications** → Send to external URL

**Implementation:**
```
1. Get notification type from input
2. Switch on notification.type
3. Each case formats data appropriately
4. Return formatted notification for delivery
```

## Advanced Switch Patterns

### Nested Switch Functions
```
Primary Switch on: user.account_type
├── "business" → 
    └── Secondary Switch on: business.size
        ├── "enterprise" → Enterprise features
        ├── "small" → SMB features
        └── Default → Standard business
├── "personal" → Personal features
└── Default → Basic features
```

### Switch with Database Lookups
```
Switch on: product.category
├── "electronics" → 
    ├── Get electronics pricing rules
    ├── Apply electronics-specific taxes
    └── Set electronics shipping options
├── "clothing" →
    ├── Get clothing size charts
    ├── Apply seasonal discounts
    └── Set clothing return policy
└── Default → Apply general rules
```

## Performance Benefits

### Switch vs Multiple Conditionals
```
❌ Multiple If-Then (Inefficient):
If color = "red" → action1
If color = "blue" → action2  
If color = "green" → action3
If color = "yellow" → action4
// Checks every condition even after match

✅ Switch (Efficient):
Switch on color:
├── "red" → action1
├── "blue" → action2
├── "green" → action3
└── "yellow" → action4
// Stops checking after first match
```

## Common Mistakes to Avoid

❌ **Using Switch for complex conditions** - Use Conditional for AND/OR logic
❌ **Forgetting Default case** - Always handle unexpected values
❌ **Too many cases** - Consider lookup tables for 10+ options
❌ **Nested complexity** - Keep Switch cases simple and focused
❌ **Case-sensitive issues** - Normalize values before switching

## Pro Tips

💡 **Normalize input values** before switching (trim, lowercase)
💡 **Use meaningful case labels** that match your data exactly
💡 **Always include a Default case** for unexpected values
💡 **Keep case logic simple** - complex logic belongs in separate functions
💡 **Document case meanings** especially for status codes or IDs
💡 **Consider performance** - Switch is faster than multiple conditionals
💡 **Group related cases** logically for better maintainability

## Error Handling

### Robust Switch Implementation
```
1. Validate input exists and is not null
2. Normalize input value (trim, case)
3. Execute Switch with comprehensive cases
4. Handle Default case gracefully
5. Log unexpected values for debugging
6. Return consistent response format
```

### Default Case Best Practices
```
Default case should:
├── Log the unexpected value
├── Return safe fallback behavior
├── Maintain response consistency
└── Not break the workflow
```

Switch functions are essential for clean, efficient conditional logic that's easy to read, maintain, and debug.