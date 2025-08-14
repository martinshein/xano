---
title: "Get Record - Fetch Single Database Records"
description: "Retrieve individual records from your database by ID or field value"
category: function-stack
subcategory: database
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- get
- retrieve
- database
- crud
- records
---

# Get Record - Fetch Single Database Records



## Quick Summary

> **What it is:** Function to fetch a single record from your database by searching one field
> 
> **When to use:** Getting user profiles, order details, or any specific record by ID or unique field
> 
> **Key benefit:** Fast, simple way to retrieve individual records
> 
> **Perfect for:** Non-developers building user profiles, detail pages, or record lookups

## What You'll Learn

- Basic record retrieval
- Searching by different fields
- Customizing output fields
- Error handling
- Performance optimization

## Basic Get Record Setup

### Step 1: Add Get Record Function
1. Click + in function stack
2. Select "Database Requests"
3. Choose "Get Record"
4. Select your table

### Step 2: Configure Search
```javascript
Get_Record {
  table: "users",
  field_name: "id",
  field_value: Input.user_id
}
```

## Common Search Patterns

### By ID (Most Common)
```javascript
// Get user by ID
user = Get_Record {
  table: "users",
  field_name: "id", 
  field_value: Input.user_id
}

// Get order by ID
order = Get_Record {
  table: "orders",
  field_name: "id",
  field_value: Input.order_id
}
```

### By Email
```javascript
// Get user by email
user = Get_Record {
  table: "users",
  field_name: "email",
  field_value: Input.email
}
```

### By Slug/Code
```javascript
// Get product by slug
product = Get_Record {
  table: "products",
  field_name: "slug",
  field_value: Input.product_slug
}

// Get discount by code
discount = Get_Record {
  table: "discounts",
  field_name: "code",
  field_value: Input.discount_code
}
```

## Integration Examples

### With n8n - User Lookup
```javascript
// n8n sends user email
email = Webhook.email

// Find user
user = Get_Record {
  table: "users",
  field_name: "email",
  field_value: email
}

if (user) {
  // User exists
  return {
    found: true,
    user_id: user.id,
    name: user.name
  }
} else {
  // User not found
  return {
    found: false,
    message: "User not found"
  }
}
```

### With WeWeb - Profile Page
```javascript
// WeWeb requests user profile
user_id = Input.user_id

// Get full profile
profile = Get_Record {
  table: "users",
  field_name: "id",
  field_value: user_id
}

// Check if user exists
if (!profile) {
  return {
    error: "User not found",
    status: 404
  }
}

// Return profile data
return {
  id: profile.id,
  name: profile.name,
  email: profile.email,
  avatar: profile.avatar_url,
  bio: profile.bio,
  joined: profile.created_at
}
```

## Customizing Output

### Select Specific Fields
```javascript
// Only return needed fields
user = Get_Record {
  table: "users",
  field_name: "id",
  field_value: Input.user_id,
  select: ["id", "name", "email", "avatar_url"]
}
// Excludes sensitive fields like password_hash
```

### Including Related Data
```javascript
// Get user with related posts
user = Get_Record {
  table: "users",
  field_name: "id",
  field_value: Input.user_id,
  include: {
    posts: {
      limit: 10,
      order: "created_at DESC"
    }
  }
}
```

## Error Handling

### Check if Record Exists
```javascript
// Safe record retrieval
user = Get_Record {
  table: "users",
  field_name: "id", 
  field_value: Input.user_id
}

if (!user) {
  return {
    success: false,
    error: "User not found",
    code: "USER_NOT_FOUND"
  }
}

// Continue with user data
return {
  success: true,
  user: user
}
```

### Authentication Check
```javascript
// Get current user's record
current_user = Get_Record {
  table: "users",
  field_name: "id",
  field_value: Auth.user_id
}

if (!current_user) {
  return {
    error: "Authentication required",
    status: 401
  }
}
```

## Performance Optimization

### Index Important Fields
For fields you search frequently:
- id (automatically indexed)
- email (add index in database)
- username (add index)
- slug (add index)

### Limit Field Selection
```javascript
// Bad: Returns all fields
user = Get_Record("users", "id", user_id)

// Good: Returns only needed fields
user = Get_Record {
  table: "users",
  field_name: "id",
  field_value: user_id,
  select: ["name", "email", "status"]
}
```

## Common Patterns

### User Authentication
```javascript
// Login flow
email = Input.email
password = Input.password

// Find user by email
user = Get_Record {
  table: "users",
  field_name: "email",
  field_value: email
}

if (!user) {
  return {error: "Invalid credentials"}
}

// Check password
if (verify_password(password, user.password_hash)) {
  return {
    success: true,
    user_id: user.id,
    token: generate_token(user.id)
  }
}
```

### API Key Validation
```javascript
// Validate API key
api_key = Input.headers.authorization

api_record = Get_Record {
  table: "api_keys",
  field_name: "key_hash",
  field_value: hash(api_key)
}

if (!api_record || !api_record.is_active) {
  return {
    error: "Invalid API key",
    status: 401
  }
}

// Continue with valid key
current_user_id = api_record.user_id
```

### Record Ownership Check
```javascript
// Check if user owns record
post_id = Input.post_id

post = Get_Record {
  table: "posts",
  field_name: "id",
  field_value: post_id
}

if (!post) {
  return {error: "Post not found"}
}

if (post.user_id != Auth.user_id) {
  return {
    error: "Access denied",
    status: 403
  }
}

// User owns the post, continue
```

## Database Locking

For critical operations:
```javascript
// Lock record during transaction
Transaction {
  // Get record with lock
  user = Get_Record {
    table: "users",
    field_name: "id",
    field_value: user_id,
    lock: true
  }
  
  // Modify record
  new_balance = user.balance + amount
  
  // Update record
  Edit_Record {
    id: user_id,
    balance: new_balance
  }
}
// Lock released automatically
```

## When to Use vs Query All Records

### Use Get Record When:
- Searching by one field
- Expecting single result
- Simple lookups by ID/email/slug

### Use Query All Records When:
- Complex filtering (multiple fields)
- Expecting multiple results
- Need sorting/pagination
- Advanced queries

## Try This

Create a user profile endpoint:
1. Add Get Record function
2. Search by user ID
3. Handle "not found" case
4. Return formatted profile
5. Test with invalid IDs

## Pro Tips

💡 **Always Check Null:** Handle cases where record doesn't exist

💡 **Index Search Fields:** Add database indexes for non-ID searches

💡 **Limit Fields:** Only select fields you actually need

💡 **Use Meaningful Errors:** Return helpful error messages

💡 **Consider Caching:** Cache frequently accessed records

## Common Gotchas

### Case Sensitivity
```javascript
// Problem: Case mismatch
user = Get_Record("users", "email", "John@Example.com")
// Won't match john@example.com

// Solution: Normalize case
email = Input.email.toLowerCase()
user = Get_Record("users", "email", email)
```

### Null vs Empty
```javascript
// Check for both null and undefined
if (!user || user === null) {
  return {error: "User not found"}
}
```

### Security
```javascript
// Never expose sensitive fields
return {
  id: user.id,
  name: user.name,
  // Don't return: password_hash, api_keys, etc.
}
```

## Next Steps

1. Add proper error handling
2. Optimize with field selection
3. Add database indexes
4. Implement caching
5. Build authorization checks

Remember: Get Record is your go-to for simple, fast record lookups!