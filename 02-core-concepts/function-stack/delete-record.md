---
title: "Delete Record - Remove Data Safely"
description: "Delete database records with proper validation and safety checks"
category: function-stack
subcategory: database
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- delete
- database
- crud
- records
- operations
---

# Delete Record - Remove Data Safely



## Quick Summary

> **What it is:** Function to permanently remove records from your database
> 
> **When to use:** Deleting user accounts, removing old data, cleaning up test records
> 
> **Key benefit:** Safe, controlled deletion with proper validation
> 
> **Perfect for:** Non-developers managing data cleanup and user requests

## What You'll Learn

- Setting up delete operations
- Adding safety checks
- Soft vs hard deletes
- Cascade deletion
- Recovery strategies

## Basic Delete Setup

### Step 1: Add Delete Function
1. Click + in function stack
2. Select "Database Requests"
3. Choose "Delete Record"
4. Select your table

### Step 2: Specify Target
```javascript
// Delete by ID
field_name: "id"
field_value: Input.user_id

// Delete by email
field_name: "email"
field_value: Input.email
```

## Integration Examples

### With n8n - Cleanup Workflow
```javascript
// n8n sends deletion request
user_id = Webhook.user_id

// Verify before deleting
user = Get_Record(user_id)
if (user.can_delete) {
  Delete_Record {
    table: "users",
    field_name: "id",
    field_value: user_id
  }
  return { success: true }
}
```

### With WeWeb - User Account
```javascript
// User requests deletion
user_id = Auth.user_id

// Soft delete first
Edit_Record {
  id: user_id,
  deleted_at: timestamp(),
  status: "deleted"
}

// Schedule hard delete later
Background_Task {
  delay: 30_days,
  Delete_Record(user_id)
}
```

## Soft Delete Pattern

Keep data but mark as deleted:

```javascript
// Instead of deleting
Edit_Record {
  id: record_id,
  is_deleted: true,
  deleted_at: now(),
  deleted_by: Auth.user_id
}

// Filter in queries
Query_All_Records {
  where: is_deleted != true
}
```

## Safety Checks

### Confirm Before Delete
```javascript
// Check dependencies
related_records = Query_All_Records {
  table: "orders",
  where: user_id == Input.user_id
}

if (related_records.length > 0) {
  return {
    error: "Cannot delete: User has active orders"
  }
}

// Proceed with deletion
Delete_Record(Input.user_id)
```

### Archive Before Delete
```javascript
// Backup record
record = Get_Record(id)
Add_Record {
  table: "archive",
  data: record
}

// Then delete
Delete_Record(id)
```

## Cascade Deletion

Delete related records:

```javascript
Transaction {
  // Delete child records first
  Delete_All_Records {
    table: "user_posts",
    where: user_id == Input.user_id
  }
  
  Delete_All_Records {
    table: "user_comments",
    where: user_id == Input.user_id
  }
  
  // Then delete parent
  Delete_Record {
    table: "users",
    id: Input.user_id
  }
}
```

## Bulk Deletion

```javascript
// Delete old records
old_date = timestamp() - 365_days

old_records = Query_All_Records {
  where: created_at < old_date
}

For Each record in old_records {
  Delete_Record(record.id)
}
```

## Common Patterns

### GDPR Compliance
```javascript
// User data deletion
1. Export user data
2. Send copy to user
3. Delete personal info
4. Keep anonymized records
5. Log compliance action
```

### Cleanup Job
```javascript
// Daily cleanup
Background_Task {
  schedule: "daily",
  Delete old logs,
  Delete expired sessions,
  Delete soft-deleted records > 30 days
}
```

## Error Handling

```javascript
Try {
  Delete_Record(id)
  Log_Activity("Record deleted", id)
  return { success: true }
} Catch (error) {
  Log_Error("Delete failed", error)
  return { 
    success: false, 
    error: "Could not delete record" 
  }
}
```

## Try This

Create safe deletion flow:
1. Add delete function
2. Check for dependencies
3. Archive record first
4. Delete with confirmation
5. Log the deletion

## Pro Tips

💡 **Always Soft Delete First:** Mark as deleted before permanent removal

💡 **Check Dependencies:** Verify no related records exist

💡 **Use Transactions:** Ensure all or nothing deletion

💡 **Keep Audit Logs:** Track who deleted what and when

💡 **Add Recovery Period:** Allow undoing deletions within timeframe

## Common Gotchas

### Foreign Key Constraints
- Problem: Can't delete parent with children
- Solution: Delete children first or use cascade

### No Undo
- Problem: Deletion is permanent
- Solution: Implement soft delete with recovery

### Performance Issues
- Problem: Bulk deletion is slow
- Solution: Delete in batches with background tasks

## Next Steps

1. Implement soft deletes
2. Add confirmation dialogs
3. Create archive system
4. Set up cascade rules
5. Build recovery features

Remember: Deletion is permanent - always validate and backup before removing data!