---
title: "Add Record - Creating New Database Entries"
description: "Insert new records into your Xano database tables with validation and control"
category: function-stack
subcategory: database-operations
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- database
- crud
- insert
- records
- create
---

# Add Record - Creating New Database Entries

## Quick Summary

> **What it is:** A database function for creating new records in your Xano tables with full control over field values and validation
> 
> **When to use:** Whenever you need to insert new data - user registrations, order creation, content submissions, or any new entry
> 
> **Key benefit:** Simple visual interface for database inserts with automatic validation and type checking
> 
> **Returns:** The complete newly created record with its generated ID

## What You'll Learn

- Creating records with proper field mapping
- Using auto-fill for efficient data entry
- Managing optional vs required fields
- Optimizing return data for performance
- Real-world patterns for n8n and WeWeb
- Best practices for data integrity

## Basic Configuration

### Setting Field Values

The Add Record function displays all available fields from your selected table. For each field, you can:

1. **Enable/Disable Fields**
   - Click the toggle icon to enable/disable all fields at once
   - Hover over individual fields to disable specific ones
   - Disabled fields use database defaults or remain null

2. **Map Data to Fields**
   - Direct values: `"John Doe"`, `123`, `true`
   - Variables: `input.name`, `user_data.email`
   - Expressions: `timestamp_now()`, `UUID()`

3. **Auto-Fill from Objects**
   - Click the auto-fill button when you have a matching object
   - Automatically maps all matching field names
   - Great for webhook data or form submissions

## Practical Examples

### Example 1: User Registration

```javascript
// Table: users
{
  email: input.email,
  password: HASH(input.password),  // Always hash passwords!
  name: input.full_name,
  role: "member",  // Default role
  status: "pending_verification",
  created_at: timestamp_now(),
  verification_token: UUID()
}

// Returns: Complete user record with generated ID
```

### Example 2: Order Creation

```javascript
// Table: orders
{
  user_id: auth.user_id,  // From authentication
  order_number: "ORD-" + timestamp_unix(),
  items: input.cart_items,  // JSON array
  subtotal: calculated_subtotal,
  tax: calculated_tax,
  total: calculated_total,
  status: "pending_payment",
  created_at: timestamp_now()
}
```

### Example 3: Activity Log

```javascript
// Table: activity_logs
{
  user_id: auth.user_id,
  action: "viewed_product",
  resource_type: "product",
  resource_id: input.product_id,
  metadata: {
    referrer: input.referrer,
    session_id: input.session,
    device: input.user_agent
  },
  timestamp: timestamp_now()
}
```

## Advanced Features

### Managing Record IDs

**Default Behavior (Recommended):**
- Let Xano auto-increment IDs
- Ensures uniqueness and sequential ordering
- Prevents conflicts and race conditions

**Manual ID Assignment (Use Carefully):**
```javascript
id: custom_id_value  // Only when migrating data or specific requirements
```

⚠️ **Warning:** Manual IDs can cause conflicts if not properly managed!

### Customizing Return Data

Optimize your API responses by selecting only needed fields:

1. Click the output configuration icon
2. Uncheck unnecessary fields
3. Reduces response payload size

**Performance Tip:** While this doesn't affect insert speed, it improves network transfer and frontend processing.

### Variable Naming

Control the output variable name for use in subsequent functions:

```javascript
Return As: "new_user"  // Instead of default "add_record"

// Now use in next function:
Send Email to: new_user.email
```

### Adding Descriptions

Make your function stacks self-documenting:

```javascript
Description: "Create new customer with Stripe integration"
// Appears in function stack for team clarity
```

## Field Management Best Practices

### Required vs Optional Fields

**Required Fields (Database Level):**
- Must always have a value
- Will cause error if missing
- Examples: email, user_id, order_total

**Optional Fields:**
- Can be left empty (null)
- Use database defaults if configured
- Examples: middle_name, notes, preferences

### Default Values Strategy

```javascript
// Good: Explicit defaults in function
{
  status: input.status || "active",
  priority: input.priority || 5,
  tags: input.tags || []
}

// Better: Database-level defaults
// Configure in table schema for consistency
```

## Integration Patterns

### With n8n Webhooks

```javascript
// n8n sends webhook with user data
1. Receive webhook trigger
2. Validate required fields
3. Add Record with auto-fill from webhook body
4. Return success with new record ID
5. n8n continues workflow with ID
```

### With WeWeb Forms

```javascript
// WeWeb form submission flow
1. User fills form in WeWeb
2. WeWeb validates client-side
3. Send to Xano Add Record endpoint
4. Handle success/error in WeWeb
5. Update UI with new record data
```

## Common Mistakes to Avoid

1. **Forgetting Required Fields**
   ```javascript
   // Bad: Missing required email field
   { name: "John", age: 30 }
   
   // Good: All required fields included
   { email: "john@example.com", name: "John", age: 30 }
   ```

2. **Not Hashing Passwords**
   ```javascript
   // NEVER store plain text passwords!
   // Bad: password: input.password
   
   // Good: Use hash filter
   password: HASH(input.password)
   ```

3. **Duplicate Data Entry**
   ```javascript
   // Check before adding to prevent duplicates
   1. Query for existing record
   2. If not exists, then Add Record
   3. Or use Add or Edit Record function
   ```

4. **Missing Timestamps**
   ```javascript
   // Always track when records are created
   created_at: timestamp_now()
   ```

## Data Validation Tips

### Input Validation Pattern

```javascript
1. Validate email format
2. Check password strength
3. Verify required fields present
4. Add Record only if all validations pass
5. Return appropriate error messages
```

### Business Logic Validation

```javascript
// Example: Check inventory before order
1. Query product inventory
2. If sufficient stock:
   - Add order record
   - Update inventory
3. Else:
   - Return out of stock error
```

## Try This

Create a complete user onboarding flow:
1. Add user record with registration data
2. Add preferences record with defaults
3. Add welcome notification record
4. Send welcome email with user data
5. Return success with user profile

## Pro Tips

💡 **Batch Inserts:** Use Bulk Operations for multiple records instead of loops

💡 **Audit Fields:** Always include created_at, created_by for tracking

💡 **UUIDs:** Use UUID() for public-facing IDs instead of sequential integers

💡 **Transactions:** Wrap related inserts in database transactions for consistency

## Performance Optimization

- **Index Strategy:** Ensure proper indexes on frequently queried fields
- **Batch Processing:** Group multiple inserts when possible
- **Async Processing:** Use background tasks for non-critical inserts
- **Return Only Needed:** Don't return large JSON fields unless necessary

## Error Handling

Common errors and solutions:

1. **Unique Constraint Violation**
   - Check for existing records first
   - Use Add or Edit Record for upserts

2. **Foreign Key Constraint**
   - Ensure referenced records exist
   - Validate IDs before insertion

3. **Data Type Mismatch**
   - Validate input types match schema
   - Use proper type conversion filters

Remember: Add Record is the foundation of data entry - use it wisely with proper validation and error handling!