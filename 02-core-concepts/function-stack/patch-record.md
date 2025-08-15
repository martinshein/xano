---
title: "Patch Record Function"
description: "Update specific database record fields efficiently using Xano's Patch Record function for flexible data updates"
category: function-stack
difficulty: intermediate
tags:
  - database
  - patch
  - update
  - crud
  - partial-update
  - flexible-editing
related_docs:
  - edit-record
  - add-or-edit-record
  - get-record
  - database-requests
last_updated: '2025-01-23'
---

# Patch Record Function

## Quick Summary
Patch Record allows you to update only specific fields in a database record without needing to specify every field. Perfect for flexible user profiles, settings updates, and APIs where you don't know which fields will be modified in advance.

## What You'll Learn
- When to use Patch Record vs Edit Record
- Building flexible update endpoints
- Working with partial data updates
- Best practices for safe patching operations

## Patch Record vs Edit Record

### Use Patch Record When:
- **Updating variable fields** - Not all fields will be modified every time
- **User profile editors** - Users may only update some profile information
- **Settings panels** - Only changed preferences need updating
- **Mobile apps** - Bandwidth-conscious partial updates
- **Form builders** - Dynamic forms with varying field sets

### Use Edit Record When:
- **Complete record replacement** - You know exactly which fields to update
- **Validation requirements** - Need to process each field individually
- **Complex transformations** - Fields require individual processing
- **Audit trails** - Need detailed tracking of each field change

## How Patch Record Works

### Basic Structure
Unlike Edit Record, Patch Record expects:
1. **Record identifier** (ID or unique field)
2. **JSON object** containing only the fields to update
3. **Table specification**

### Example: User Profile Update

**Current record:**
```json
{
  "id": 123,
  "firstName": "Chris",
  "lastName": "Johnson", 
  "email": "chris@example.com",
  "city": "New York",
  "country": "USA",
  "phone": "555-0123",
  "newsletter": true
}
```

**User wants to update only city:**
```json
{
  "city": "Los Angeles"
}
```

**Result:** Only the city field gets updated, all other fields remain unchanged.

## Building Flexible Update Endpoints

### Method 1: Get All Raw Input + Patch Record

This combination creates extremely flexible endpoints:

1. **Get All Raw Input** - Captures whatever fields the client sends
2. **Patch Record** - Updates only those fields in the database

```json
// Client can send any combination of fields
{
  "firstName": "Christopher",
  "city": "Los Angeles"
}
// Only these two fields get updated
```

### Method 2: Selective Field Processing

For more control, process specific fields:

```json
// Function stack logic
1. Get input fields
2. Validate required fields exist
3. Build patch object with only allowed fields
4. Apply Patch Record
5. Return updated record
```

## Integration with n8n

### Webhook-Driven Updates
```javascript
// n8n webhook data for user profile updates
{
  "userId": 123,
  "updates": {
    "preferences": {
      "theme": "dark",
      "language": "es"
    },
    "notifications": {
      "email": false,
      "push": true
    }
  }
}
```

### n8n Function Node Processing
```javascript
// Prepare data for Xano Patch Record
const userId = $json.userId;
const updates = $json.updates;

// Flatten nested updates if needed
const flatUpdates = {
  theme: updates.preferences.theme,
  language: updates.preferences.language,
  emailNotifications: updates.notifications.email,
  pushNotifications: updates.notifications.push
};

return {
  id: userId,
  patchData: flatUpdates
};
```

## Integration with WeWeb

### WeWeb Profile Editor Component
```javascript
// WeWeb component for user profile editing
export default {
  data() {
    return {
      user: {},
      changedFields: {},
      isUpdating: false
    };
  },
  
  methods: {
    // Track which fields have changed
    trackChange(fieldName, newValue) {
      this.changedFields[fieldName] = newValue;
    },
    
    // Save only changed fields
    async saveChanges() {
      if (Object.keys(this.changedFields).length === 0) {
        return; // No changes to save
      }
      
      this.isUpdating = true;
      
      try {
        // Send only changed fields to Xano
        const response = await this.$xano.patch(`/users/${this.user.id}`, {
          ...this.changedFields
        });
        
        // Update local user object
        this.user = { ...this.user, ...response.data };
        this.changedFields = {}; // Clear changes
        
        this.$toast.success('Profile updated successfully');
      } catch (error) {
        this.$toast.error('Failed to update profile');
      } finally {
        this.isUpdating = false;
      }
    },
    
    // Check if form has unsaved changes
    hasUnsavedChanges() {
      return Object.keys(this.changedFields).length > 0;
    }
  },
  
  // Warn user about unsaved changes
  beforeUnload() {
    if (this.hasUnsavedChanges()) {
      return 'You have unsaved changes. Are you sure you want to leave?';
    }
  }
};
```

## Real-World Use Cases

### 1. User Settings Panel
```json
// User updates only notification preferences
{
  "emailNotifications": false,
  "pushNotifications": true,
  "marketingEmails": false
}
// Profile, contact info, etc. remain unchanged
```

### 2. E-commerce Order Status Update
```json
// Update only order status and tracking
{
  "status": "shipped",
  "trackingNumber": "1234567890",
  "shippedAt": "2025-01-23T10:30:00Z"
}
// Customer info, items, etc. stay the same
```

### 3. Content Management
```json
// Author updates only article content
{
  "content": "Updated article content...",
  "updatedAt": "2025-01-23T10:30:00Z"
}
// Title, author, creation date unchanged
```

## Try This: Build a Flexible User Profile Endpoint

1. **Create endpoint** with Patch Record function
2. **Use Get All Raw Input** to capture any fields sent
3. **Add validation** for required fields (like ID)
4. **Filter allowed fields** for security
5. **Return updated record** for client confirmation

**Example implementation:**
```
1. Get All Raw Input → captures client data
2. Conditional → check if user ID provided
3. Create Variable → filter allowed fields only
4. Patch Record → update database
5. Get Record → fetch updated record
6. Return → send confirmation to client
```

## Security Best Practices

### Field Whitelisting
```json
// Only allow specific fields to be updated
{
  "allowedFields": [
    "firstName",
    "lastName", 
    "city",
    "country",
    "phone",
    "preferences"
  ],
  "forbiddenFields": [
    "id",
    "email", 
    "createdAt",
    "role",
    "permissions"
  ]
}
```

### Input Validation
```json
// Validate field types and values
{
  "validations": {
    "firstName": "string, max 50 chars",
    "phone": "string, phone format",
    "age": "integer, 13-120",
    "email": "string, email format"
  }
}
```

### Permission Checks
```json
// Ensure user can update this record
{
  "checks": [
    "User is authenticated",
    "User owns record OR has admin role",
    "Field-level permissions respected"
  ]
}
```

## Common Mistakes to Avoid

❌ **Not validating ownership** - Always check user can update the record
❌ **Allowing dangerous fields** - Block updates to ID, timestamps, permissions
❌ **Missing input validation** - Validate data types and formats
❌ **Not handling conflicts** - Consider concurrent updates
❌ **Forgetting audit trails** - Log who changed what and when

## Pro Tips

💡 **Use field whitelisting** instead of blacklisting for better security
💡 **Track change history** by logging patches in separate audit table
💡 **Implement optimistic locking** to handle concurrent updates
💡 **Return the full updated record** so clients can sync their state
💡 **Use transactions** when patching multiple related records
💡 **Validate business rules** before applying patches
💡 **Consider rate limiting** for patch endpoints to prevent abuse

## Error Handling Patterns

### Common Error Responses
```json
{
  "error": "VALIDATION_FAILED",
  "message": "Invalid field values provided",
  "details": {
    "email": "Must be valid email format",
    "age": "Must be between 13 and 120"
  }
}

{
  "error": "PERMISSION_DENIED", 
  "message": "Cannot update this record"
}

{
  "error": "RECORD_NOT_FOUND",
  "message": "User with ID 123 not found"
}
```

### Optimistic Locking
```json
// Include version field to detect conflicts
{
  "id": 123,
  "version": 5,
  "firstName": "Updated Name"
}

// If version doesn't match current record
{
  "error": "CONFLICT",
  "message": "Record was modified by another user",
  "currentVersion": 6
}
```

Patch Record is essential for building modern, efficient APIs that minimize data transfer and provide flexible update capabilities.