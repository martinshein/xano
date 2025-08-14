---
title: "Edit Record - Update Data Easily"
description: "Modify existing database records with validation and control"
category: function-stack
subcategory: database
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- edit
- update
- database
- crud
- records
---

# Edit Record - Update Data Easily



## Quick Summary

> **What it is:** Function to update existing records in your database
> 
> **When to use:** Updating user profiles, changing order status, modifying any existing data
> 
> **Key benefit:** Safe, validated updates without overwriting entire records
> 
> **Perfect for:** Non-developers managing data updates and user modifications

## What You'll Learn

- Setting up edit operations
- Partial vs full updates
- Validation before saving
- Tracking changes
- Optimistic locking

## Basic Edit Setup

### Step 1: Add Edit Function
1. Click + in function stack
2. Select "Database Requests"
3. Choose "Edit Record"
4. Select your table

### Step 2: Configure Updates
```javascript
Edit_Record {
  table: "users",
  id: Input.user_id,
  fields: {
    name: Input.name,
    email: Input.email,
    updated_at: timestamp()
  }
}
```

## Integration Examples

### With n8n - Profile Update
```javascript
// n8n sends update data
update_data = Webhook.data

// Validate changes
if (update_data.email) {
  existing = Query_Records {
    where: email == update_data.email
  }
  if (existing) return "Email already exists"
}

// Apply updates
Edit_Record {
  id: update_data.user_id,
  fields: update_data
}
```

### With WeWeb - Form Submission
```javascript
// WeWeb form data
form_data = Input

// Update with validation
current_user = Get_Record(Auth.user_id)

Edit_Record {
  id: Auth.user_id,
  name: form_data.name || current_user.name,
  bio: form_data.bio || current_user.bio,
  updated_at: now()
}
```

## Partial Updates

Only update changed fields:

```javascript
// Build update object
updates = {}

if (Input.name) {
  updates.name = Input.name
}

if (Input.email) {
  updates.email = Input.email
}

// Only update if changes exist
if (Object.keys(updates).length > 0) {
  updates.updated_at = timestamp()
  Edit_Record {
    id: Input.id,
    fields: updates
  }
}
```

## Validation Patterns

### Before Update
```javascript
// Get current record
current = Get_Record(Input.id)

// Validate changes
if (Input.email != current.email) {
  // Check email uniqueness
  existing = Query_Records {
    where: email == Input.email
  }
  if (existing) {
    return { error: "Email already taken" }
  }
}

// Proceed with update
Edit_Record {
  id: Input.id,
  email: Input.email
}
```

### Business Rules
```javascript
// Status change validation
current = Get_Record(order_id)

// Check valid transitions
valid_transitions = {
  pending: ["processing", "cancelled"],
  processing: ["shipped", "cancelled"],
  shipped: ["delivered"],
  delivered: []
}

if (!valid_transitions[current.status].includes(new_status)) {
  return { error: "Invalid status change" }
}

Edit_Record {
  id: order_id,
  status: new_status
}
```

## Tracking Changes

### Audit Trail
```javascript
// Get before state
before = Get_Record(id)

// Make changes
Edit_Record {
  id: id,
  fields: updates
}

// Log changes
Add_Record {
  table: "audit_log",
  record_id: id,
  user_id: Auth.user_id,
  before: before,
  after: updates,
  timestamp: now()
}
```

### Version History
```javascript
// Save version before update
current = Get_Record(id)
Add_Record {
  table: "document_versions",
  document_id: id,
  content: current.content,
  version: current.version,
  saved_by: Auth.user_id
}

// Update with new version
Edit_Record {
  id: id,
  content: Input.content,
  version: current.version + 1
}
```

## Bulk Updates

Update multiple records:

```javascript
// Update all matching records
records = Query_Records {
  where: status == "pending" AND 
         created_at < yesterday
}

For Each record in records {
  Edit_Record {
    id: record.id,
    status: "expired"
  }
}
```

## Optimistic Locking

Prevent concurrent update conflicts:

```javascript
// Include version in update
current = Get_Record(id)

Edit_Record {
  id: id,
  where: version == current.version,
  fields: {
    ...updates,
    version: current.version + 1
  }
}

// Check if update succeeded
if (affected_rows == 0) {
  return { error: "Record was modified by another user" }
}
```

## Common Patterns

### Toggle Boolean
```javascript
// Toggle active status
current = Get_Record(id)

Edit_Record {
  id: id,
  is_active: !current.is_active
}
```

### Increment Counter
```javascript
// Update view count
Edit_Record {
  id: post_id,
  view_count: current.view_count + 1,
  last_viewed: timestamp()
}
```

### Conditional Updates
```javascript
// Update only if condition met
if (user.role == "admin" || user.id == record.owner_id) {
  Edit_Record {
    id: record_id,
    fields: updates
  }
} else {
  return { error: "Unauthorized" }
}
```

## Try This

Create a profile update flow:
1. Add edit function
2. Get current record
3. Validate changes
4. Apply updates
5. Log the changes

## Pro Tips

💡 **Validate First:** Check data before updating

💡 **Use Transactions:** Group related updates together

💡 **Track Changes:** Keep audit logs for important data

💡 **Partial Updates:** Only modify changed fields

💡 **Add Timestamps:** Always update modified_at field

## Common Gotchas

### Overwriting Data
- Problem: Replacing all fields unintentionally
- Solution: Use partial updates, only change specific fields

### Race Conditions
- Problem: Two users updating simultaneously
- Solution: Implement optimistic locking

### Missing Validation
- Problem: Invalid data gets saved
- Solution: Validate before every update

## Next Steps

1. Add validation rules
2. Implement audit logging
3. Create version history
4. Build approval workflows
5. Add field-level permissions

Remember: Always validate changes and track who modified what for data integrity!