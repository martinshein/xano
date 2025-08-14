---
title: "Add or Edit Record - Smart Database Updates"
description: "Automatically add new records or update existing ones with a single function in Xano"
category: function-stack
subcategory: database-operations
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- database
- crud
- upsert
- records
- automation
---

# Add or Edit Record - Smart Database Updates

## Quick Summary

> **What it is:** A smart database function that automatically decides whether to create a new record or update an existing one based on your criteria
> 
> **When to use:** Perfect for syncing data, updating user preferences, managing shopping carts, or any scenario where you're not sure if a record already exists
> 
> **Key benefit:** Eliminates the need for separate "check if exists" logic - one function handles both scenarios
> 
> **Common name:** Also known as "Upsert" (Update + Insert) in database terminology

## What You'll Learn

- Setting up automatic add-or-update logic
- Configuring lookup criteria for finding existing records
- Managing field updates efficiently
- Real-world patterns for n8n and WeWeb
- Avoiding common pitfalls with upserts

## How It Works

The Add or Edit Record function follows this simple logic:
1. **Searches** for a record matching your criteria
2. **Updates** the record if found
3. **Creates** a new record if not found
4. **Returns** the final record (whether new or updated)

Think of it like a smart assistant that knows whether to update your existing shopping cart or create a new one.

## Configuration

### 1. Define Your Lookup Criteria

Tell Xano how to identify if a record already exists:

**Field Name:** The database field to search in
**Field Value:** The value to look for

**Common Examples:**
```javascript
// User preferences (one per user)
Field Name: user_id
Field Value: 123

// Shopping cart (one per session)
Field Name: session_token
Field Value: "abc-xyz-789"

// Product inventory (by SKU)
Field Name: sku
Field Value: "PROD-001"
```

### 2. Specify Data Fields

Configure which fields to set when adding or updating:

**Quick Actions:**
- Click the toggle icon to enable/disable all fields at once
- Hover and click the disable icon for specific fields
- Use auto-fill from an existing object variable

**Field Management Tips:**
- Disabled fields keep their current values (on update)
- Disabled fields use database defaults (on add)
- Only enable fields you actually need to change

## Practical Examples

### Example 1: User Profile Sync

Sync user data from an external system:
```javascript
// Lookup
Field Name: email
Field Value: "user@example.com"

// Data
{
  name: "John Doe",
  last_login: timestamp_now(),
  subscription_status: "active",
  updated_at: timestamp_now()
}

// Result: Updates existing user or creates new one
```

### Example 2: Shopping Cart Management

Manage cart items intelligently:
```javascript
// Lookup
Field Name: compound_key  // "user_123_prod_456"
Field Value: user_id + "_" + product_id

// Data
{
  user_id: 123,
  product_id: 456,
  quantity: new_quantity,
  price: current_price,
  updated_at: timestamp_now()
}

// Result: Updates quantity or adds new item
```

### Example 3: Activity Tracking

Track user activities without duplicates:
```javascript
// Lookup
Field Name: activity_key  // "user_123_video_789"
Field Value: user_id + "_" + content_type + "_" + content_id

// Data
{
  user_id: 123,
  content_type: "video",
  content_id: 789,
  view_count: INCREMENT(1),  // Using expression
  last_viewed: timestamp_now()
}
```

## Advanced Features

### Custom Return Fields

Optimize performance by returning only needed fields:
1. Click the output configuration icon
2. Select specific fields to return
3. Reduces response size and improves speed

### Variable Naming

Use consistent variable names across conditional logic:
```javascript
// Both branches use same variable name
If (condition) {
  Add or Edit Record -> user_data
} Else {
  Get Record -> user_data
}
// Easy to use user_data in response
```

### Add Descriptions

Make your function stack readable:
```javascript
Description: "Sync user profile from CRM system"
// This appears in the function stack for clarity
```

## Integration Patterns

### With n8n

**Webhook Data Sync:**
```javascript
1. n8n sends webhook with user data
2. Add or Edit using email as lookup
3. Return success/failure to n8n
4. n8n continues workflow based on result
```

### With WeWeb

**Form Submissions:**
```javascript
1. WeWeb form collects user preferences
2. Add or Edit using user_id
3. Return updated preferences
4. WeWeb updates UI with new data
```

## Common Mistakes to Avoid

1. **Wrong Lookup Field**
   - Use unique fields (email, user_id, SKU)
   - Avoid non-unique fields (name, status)
   - Consider compound keys for complex lookups

2. **Overwriting Important Data**
   - Disable fields you don't want to change
   - Be careful with timestamps and system fields
   - Test with sample data first

3. **Performance Issues**
   - Index your lookup field for speed
   - Return only necessary fields
   - Consider batch operations for multiple records

4. **Missing Error Handling**
   - Handle unique constraint violations
   - Check for required fields
   - Validate data before upsert

## Best Practices

### 1. Use Appropriate Lookup Fields
```javascript
// Good: Unique identifiers
email, user_id, sku, session_token

// Bad: Non-unique fields
first_name, status, category
```

### 2. Manage Timestamps Properly
```javascript
// Add or Edit data
{
  // ... other fields
  created_at: IF_NULL(existing.created_at, timestamp_now()),
  updated_at: timestamp_now()
}
```

### 3. Handle Concurrent Updates
For high-traffic scenarios, consider:
- Using database transactions
- Implementing optimistic locking
- Adding retry logic in your frontend

## Try This

Build a user preference system:
1. Create a preferences table with user_id as unique
2. Use Add or Edit with user_id lookup
3. Allow users to update theme, language, notifications
4. Return preferences on every login
5. Cache preferences for performance

## Pro Tips

💡 **Compound Keys:** For many-to-many relationships, create a compound key field combining both IDs

💡 **Audit Trail:** Always update an `updated_at` timestamp to track changes

💡 **Partial Updates:** Use PATCH Record if you only need to update, never add

💡 **Bulk Operations:** For multiple records, use bulk operations instead of loops

## Performance Optimization

- **Index your lookup field** for faster searches
- **Return minimal fields** to reduce payload size
- **Use caching** for frequently accessed records
- **Consider database views** for complex lookups

## When NOT to Use

Avoid Add or Edit when:
- You always know if the record exists
- You need different logic for add vs edit
- You're dealing with sensitive operations requiring explicit control
- You need to track whether an add or edit occurred

Remember: Add or Edit is your Swiss Army knife for data synchronization - use it wisely to simplify your backend logic!