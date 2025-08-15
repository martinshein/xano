---
title: "Boolean Data Type - True/False Logic"
description: "Master Boolean values in Xano - the foundation of logical operations, conditional statements, and decision-making in your applications"
category: function-stack
tags:
  - Data Types
  - Boolean
  - Logic
  - Conditionals
  - True/False
  - Decision Making
difficulty: beginner
reading_time: 6 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of logical concepts
  - Familiarity with data types
---

# Boolean Data Type - True/False Logic

## 📋 **Quick Summary**

**What it does:** Booleans represent simple true/false values that form the foundation of logical operations and decision-making in applications.

**Why it matters:** This enables you to:
- Control conditional logic and branching in function stacks
- Store yes/no, on/off, enabled/disabled states
- Build feature toggles and user preferences
- Create dynamic filtering and search functionality

**Time to understand:** 5 minutes for basics, essential for conditional logic

---

## What You'll Learn

- Understanding true and false values
- How booleans control conditional logic
- Common boolean use cases in applications
- Working with boolean operations
- Integration with n8n and WeWeb platforms

## Understanding Boolean Values

Booleans are the simplest data type - they can only be one of two values:
- **true** (yes, on, enabled, active)
- **false** (no, off, disabled, inactive)

### Boolean Syntax
```json
{
  "is_active": true,
  "is_verified": false,
  "has_premium": true,
  "email_notifications": false
}
```

## Common Boolean Use Cases

### User Preferences & Settings
```json
{
  "user_id": 123,
  "notifications_enabled": true,
  "dark_mode": false,
  "newsletter_subscribed": true,
  "two_factor_enabled": false
}
```

### Feature Flags & Toggles
```json
{
  "feature_beta_ui": true,
  "maintenance_mode": false,
  "payment_enabled": true,
  "debug_logging": false
}
```

### Status & State Management
```json
{
  "order_id": 456,
  "is_paid": true,
  "is_shipped": false,
  "is_delivered": false,
  "is_cancelled": false
}
```

### Content & Visibility Control
```json
{
  "post_id": 789,
  "is_published": true,
  "is_featured": false,
  "comments_enabled": true,
  "is_archived": false
}
```

## Boolean Operations & Logic

### Comparison Operations
These operations return boolean values:

| Operation | Symbol | Example | Result |
|-----------|--------|---------|--------|
| **Equal** | `==` | `5 == 5` | `true` |
| **Not Equal** | `!=` | `5 != 3` | `true` |
| **Greater Than** | `>` | `10 > 5` | `true` |
| **Less Than** | `<` | `3 < 8` | `true` |
| **Greater/Equal** | `>=` | `5 >= 5` | `true` |
| **Less/Equal** | `<=` | `4 <= 6` | `true` |

### Logical Operations
Combine multiple boolean values:

| Operation | Symbol | Description | Example |
|-----------|--------|-------------|---------|
| **AND** | `&&` | Both must be true | `true && false = false` |
| **OR** | `\|\|` | At least one must be true | `true \|\| false = true` |
| **NOT** | `!` | Flips the value | `!true = false` |

## No-Code Platform Integration

### 🌐 **WeWeb Boolean Handling**

Use booleans to control UI elements dynamically:

```javascript
// WeWeb conditional visibility
// Show element only if user is premium
{
  display: user.has_premium ? 'block' : 'none'
}

// WeWeb form validation
// Enable submit button only if form is valid
{
  disabled: !form.is_valid
}

// WeWeb feature toggles
// Show beta features for eligible users
{
  visible: user.beta_access && feature_flags.beta_ui_enabled
}
```

### 🔗 **n8n Workflow Logic**

Control workflow branches with boolean conditions:

```yaml
n8n Workflow: User Onboarding
1. Webhook Trigger → New user registration
2. IF Node → Check if user.email_verified == true
   - TRUE Branch: Send welcome email
   - FALSE Branch: Send verification reminder
3. IF Node → Check if user.has_premium == true
   - TRUE Branch: Add to premium group
   - FALSE Branch: Add to free tier group
```

### 🔧 **Make Scenario Filtering**

Filter data based on boolean conditions:

```yaml
Make Scenario: Content Publishing
1. Xano API → Get all posts
2. Filter → Only posts where is_published == true
3. Iterator → Process each published post
4. Social Media → Share if social_sharing == true
```

## Boolean in Conditional Logic

### Basic Conditional Structure
```javascript
// Xano function stack conditional
if (user.is_verified == true) {
  // Allow access to premium features
  grant_premium_access();
} else {
  // Redirect to verification page
  require_verification();
}
```

### Complex Boolean Logic
```javascript
// Multiple conditions
if (user.is_active && user.subscription_valid && !user.is_suspended) {
  // User can access the service
  allow_service_access();
}

// Alternative conditions  
if (user.is_admin || user.is_moderator || user.has_special_permission) {
  // User has elevated privileges
  grant_admin_features();
}
```

## Practical Examples

### E-commerce Application
```json
{
  "product_id": 123,
  "is_available": true,
  "is_featured": false,
  "free_shipping": true,
  "requires_age_verification": false,
  "digital_product": true,
  "taxable": true
}
```

### User Management System
```json
{
  "user_id": 456,
  "is_active": true,
  "email_verified": true,
  "phone_verified": false,
  "terms_accepted": true,
  "marketing_consent": false,
  "is_admin": false
}
```

### Content Management
```json
{
  "article_id": 789,
  "is_published": true,
  "is_draft": false,
  "featured_article": true,
  "comments_enabled": true,
  "seo_optimized": false,
  "requires_subscription": true
}
```

## 💡 **Try This: User Permission System**

Build a permission checking system using booleans:

### Step 1: Define User Permissions
```json
{
  "user_id": 123,
  "can_read": true,
  "can_write": false,
  "can_delete": false,
  "is_admin": false,
  "account_verified": true
}
```

### Step 2: Create Permission Logic
```javascript
// Check if user can perform action
function canUserEdit(user, resource) {
  return user.can_write && 
         user.account_verified && 
         !resource.is_locked &&
         (user.is_admin || resource.owner_id === user.id);
}
```

### Step 3: Use in Conditional
```javascript
if (canUserEdit(currentUser, document)) {
  // Show edit button
  showEditOptions();
} else {
  // Hide edit functionality
  hideEditOptions();
}
```

## Common Mistakes to Avoid

❌ **Confusing boolean with string**
- Use `true`, not `"true"`
- Use `false`, not `"false"`

❌ **Complex boolean expressions without parentheses**
- Use `(A && B) || (C && D)` for clarity
- Avoid `A && B || C && D` (ambiguous)

❌ **Not handling null/undefined values**
- Check if value exists before boolean operations
- Use default values: `user.is_active || false`

❌ **Redundant boolean comparisons**
- Use `if (is_active)`, not `if (is_active == true)`
- Use `if (!is_deleted)`, not `if (is_deleted == false)`

## Pro Tips

💡 **Default Values**
Always provide boolean defaults to prevent errors:
```json
{
  "notifications_enabled": true,
  "dark_mode": false
}
```

💡 **Meaningful Names**
Use descriptive boolean field names:
- ✅ `is_verified`, `has_premium`, `can_edit`
- ❌ `status`, `flag`, `check`

💡 **Database Design**
Store booleans as actual boolean fields, not integers (0/1) for clarity.

💡 **API Responses**
Be consistent with boolean values in API responses - always use `true`/`false`.

## Performance Considerations

- Boolean operations are extremely fast
- Index boolean fields used in frequent queries
- Use booleans for feature flags instead of string comparisons
- Boolean filters are more efficient than text searches

---

**Next Steps:** Ready to use booleans in logic? Learn about [Conditional Functions](conditional.md) for building decision trees or explore [Comparison Functions](comparison.md) for boolean operations.