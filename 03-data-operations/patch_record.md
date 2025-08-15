---
title: "Patch Record - Selective Field Updates"
description: "Master selective database updates with Xano's Patch Record function. Learn partial updates, field increments, conditional patching, and integration patterns for flexible data management"
category: data-operations
tags:
  - Patch Record
  - Database Operations
  - Partial Updates
  - CRUD Operations
  - Field Updates
  - Data Modification
difficulty: intermediate
reading_time: 12 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of database operations
  - Familiarity with Add Record and Edit Record
  - Knowledge of JSON data structures
---

# Patch Record - Selective Field Updates

## 📋 **Quick Summary**

**What it does:** Patch Record selectively updates specific fields in database records without requiring all field values, perfect for partial updates and incremental changes.

**Why it matters:** Patch operations enable you to:
- **Update only changed fields** without affecting others
- **Increment counters** and numeric values efficiently
- **Handle partial form submissions** from users
- **Preserve data integrity** by avoiding overwrites
- **Optimize performance** with minimal data transfer

**Time to implement:** 10-15 minutes for basic patches, 20-30 minutes with validation and conditional logic

---

## What You'll Learn

- How to use Patch Record for selective updates
- Strategies for handling null and empty values
- Field increment and decrement patterns
- Integration with no-code platforms
- Best practices for safe partial updates

## Understanding Patch vs Edit

### When to Use Patch Record

**Patch Record** is ideal when you need flexible, partial updates where only some fields might be changed in each operation.

**Edit Record** works best when you have a static expectation for which fields need updating (like a dedicated password change endpoint).

### Key Differences

```javascript
// Edit Record - Updates specific, known fields
function updatePassword(userId, newPassword) {
  return editRecord({
    table: 'users',
    id: userId,
    fields: {
      password_hash: hashPassword(newPassword),
      updated_at: new Date().toISOString()
    }
  });
}

// Patch Record - Updates any combination of fields
function updateUserProfile(userId, changes) {
  // Only updates fields that are provided
  return patchRecord({
    table: 'users',
    id: userId,
    data: filterNullValues(changes) // Only non-null values
  });
}
```

## Basic Patch Record Usage

### Simple Selective Update

```javascript
// Current user record:
// {
//   id: 123,
//   name: "John Doe",
//   email: "john@example.com",
//   city: "New York",
//   phone: "555-1234",
//   status: "active"
// }

// Update only the city field
const patchData = {
  city: "San Francisco"
};

const updatedUser = patchRecord({
  table: 'users',
  id: 123,
  data: patchData
});

// Result: Only city is updated, all other fields remain unchanged
// {
//   id: 123,
//   name: "John Doe",
//   email: "john@example.com",
//   city: "San Francisco",  // Updated
//   phone: "555-1234",
//   status: "active"
// }
```

### Handling Multiple Field Updates

```javascript
// Update multiple fields at once
function updateContactInfo(userId, updates) {
  const patchData = {};
  
  // Only include fields that have values
  if (updates.phone && updates.phone.trim()) {
    patchData.phone = updates.phone.trim();
  }
  
  if (updates.address && updates.address.trim()) {
    patchData.address = updates.address.trim();
  }
  
  if (updates.city && updates.city.trim()) {
    patchData.city = updates.city.trim();
  }
  
  // Always update the timestamp
  patchData.updated_at = new Date().toISOString();
  
  return patchRecord({
    table: 'users',
    id: userId,
    data: patchData
  });
}
```

## Advanced Patch Patterns

### Safe Patching with Filter Functions

```javascript
// Complete user profile update with data filtering
function updateUserProfile(userId, rawInput) {
  // Get all raw input from the request
  const allInputs = getRawInput();
  
  // Filter out null and empty values
  let cleanData = filterNull(allInputs);
  cleanData = filterEmptyText(cleanData);
  
  // Add business logic
  if (cleanData.email) {
    cleanData.email = cleanData.email.toLowerCase().trim();
    
    // Check if email is already taken
    const existingUser = queryAllRecords({
      table: 'users',
      filters: {
        email: cleanData.email,
        id: { '!=': userId }
      },
      limit: 1
    });
    
    if (existingUser.length > 0) {
      throw new Error('Email already in use');
    }
  }
  
  // Validate phone format if provided
  if (cleanData.phone) {
    const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
    if (!phoneRegex.test(cleanData.phone.replace(/[\s\-\(\)]/g, ''))) {
      throw new Error('Invalid phone format');
    }
    cleanData.phone = cleanData.phone.replace(/[\s\-\(\)]/g, '');
  }
  
  // Always update timestamp
  cleanData.updated_at = new Date().toISOString();
  
  return patchRecord({
    table: 'users',
    id: userId,
    data: cleanData
  });
}
```

### Field Increment and Decrement

```javascript
// Increment post view count
function incrementPostViews(postId) {
  // Get current record
  const post = getRecord({
    table: 'posts',
    id: postId
  });
  
  if (!post) {
    throw new Error('Post not found');
  }
  
  // Increment view count
  return patchRecord({
    table: 'posts',
    id: postId,
    data: {
      view_count: (post.view_count || 0) + 1,
      last_viewed_at: new Date().toISOString()
    }
  });
}

// Update user points and level
function awardPoints(userId, points) {
  const user = getRecord({
    table: 'users',
    id: userId
  });
  
  const newPoints = (user.total_points || 0) + points;
  const newLevel = Math.floor(newPoints / 1000) + 1;
  
  return patchRecord({
    table: 'users',
    id: userId,
    data: {
      total_points: newPoints,
      level: newLevel,
      last_points_awarded: new Date().toISOString()
    }
  });
}
```

### Conditional Patching

```javascript
// Update order status with validation
function updateOrderStatus(orderId, newStatus, userId) {
  const order = getRecord({
    table: 'orders',
    id: orderId
  });
  
  if (!order) {
    throw new Error('Order not found');
  }
  
  // Define valid status transitions
  const validTransitions = {
    'pending': ['confirmed', 'cancelled'],
    'confirmed': ['processing', 'cancelled'],
    'processing': ['shipped', 'cancelled'],
    'shipped': ['delivered'],
    'delivered': [], // Final state
    'cancelled': [] // Final state
  };
  
  const currentStatus = order.status;
  const allowedStatuses = validTransitions[currentStatus] || [];
  
  if (!allowedStatuses.includes(newStatus)) {
    throw new Error(`Cannot change status from ${currentStatus} to ${newStatus}`);
  }
  
  const patchData = {
    status: newStatus,
    updated_at: new Date().toISOString(),
    updated_by: userId
  };
  
  // Add status-specific fields
  if (newStatus === 'shipped') {
    patchData.shipped_at = new Date().toISOString();
  } else if (newStatus === 'delivered') {
    patchData.delivered_at = new Date().toISOString();
  } else if (newStatus === 'cancelled') {
    patchData.cancelled_at = new Date().toISOString();
  }
  
  return patchRecord({
    table: 'orders',
    id: orderId,
    data: patchData
  });
}
```

## No-Code Platform Integration

### 🔗 **n8n Integration**

```javascript
// n8n workflow for user preference updates
function updateUserPreferences($input) {
  const userId = $input.query.user_id;
  const preferences = $input.body;
  
  try {
    // Validate user exists
    const user = getRecord({
      table: 'users',
      id: userId
    });
    
    if (!user) {
      return {
        success: false,
        error: 'User not found'
      };
    }
    
    // Prepare preference updates
    const updates = {};
    
    if (preferences.email_notifications !== undefined) {
      updates.email_notifications = Boolean(preferences.email_notifications);
    }
    
    if (preferences.theme !== undefined) {
      const validThemes = ['light', 'dark', 'auto'];
      if (validThemes.includes(preferences.theme)) {
        updates.theme = preferences.theme;
      }
    }
    
    if (preferences.language !== undefined) {
      const validLanguages = ['en', 'es', 'fr', 'de'];
      if (validLanguages.includes(preferences.language)) {
        updates.language = preferences.language;
      }
    }
    
    // Only update if there are changes
    if (Object.keys(updates).length === 0) {
      return {
        success: true,
        message: 'No changes to update'
      };
    }
    
    updates.preferences_updated_at = new Date().toISOString();
    
    const updatedUser = patchRecord({
      table: 'users',
      id: userId,
      data: updates
    });
    
    return {
      success: true,
      user: updatedUser,
      updated_fields: Object.keys(updates)
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
}
```

### 🌐 **WeWeb Integration**

```javascript
// WeWeb profile update component
class ProfileUpdateManager {
  static async updateField(fieldName, fieldValue, userId) {
    try {
      // Show loading for specific field
      wwLib.showFieldLoading(fieldName);
      
      // Validate the specific field
      const validation = this.validateField(fieldName, fieldValue);
      if (!validation.valid) {
        wwLib.showFieldError(fieldName, validation.message);
        return false;
      }
      
      // Prepare patch data
      const patchData = {
        [fieldName]: fieldValue,
        updated_at: new Date().toISOString()
      };
      
      // Send patch request
      const response = await wwLib.api.patch({
        url: `${wwLib.envVars.XANO_API_URL}/users/${userId}`,
        data: patchData,
        headers: {
          'Authorization': `Bearer ${wwLib.auth.getToken()}`,
          'Content-Type': 'application/json'
        }
      });
      
      if (response.data.success) {
        // Update local state
        wwLib.user.updateField(fieldName, fieldValue);
        
        // Show success feedback
        wwLib.showFieldSuccess(fieldName, 'Updated successfully');
        
        return true;
      } else {
        wwLib.showFieldError(fieldName, 'Update failed');
        return false;
      }
      
    } catch (error) {
      console.error(`Error updating ${fieldName}:`, error);
      wwLib.showFieldError(fieldName, 'An error occurred');
      return false;
    } finally {
      wwLib.hideFieldLoading(fieldName);
    }
  }
  
  static validateField(fieldName, value) {
    switch (fieldName) {
      case 'email':
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          return { valid: false, message: 'Invalid email format' };
        }
        break;
      case 'phone':
        if (!/^[\+]?[1-9][\d]{9,14}$/.test(value.replace(/[\s\-\(\)]/g, ''))) {
          return { valid: false, message: 'Invalid phone format' };
        }
        break;
      case 'name':
        if (!value || value.trim().length < 2) {
          return { valid: false, message: 'Name must be at least 2 characters' };
        }
        break;
    }
    
    return { valid: true };
  }
  
  static async bulkUpdate(updates, userId) {
    try {
      wwLib.showLoading();
      
      // Validate all fields
      for (const [field, value] of Object.entries(updates)) {
        const validation = this.validateField(field, value);
        if (!validation.valid) {
          wwLib.showAlert(`${field}: ${validation.message}`, 'error');
          return false;
        }
      }
      
      // Add timestamp
      updates.updated_at = new Date().toISOString();
      
      const response = await wwLib.api.patch({
        url: `${wwLib.envVars.XANO_API_URL}/users/${userId}`,
        data: updates
      });
      
      if (response.data.success) {
        // Update local user data
        wwLib.user.updateFields(updates);
        wwLib.showAlert('Profile updated successfully', 'success');
        return true;
      }
      
    } catch (error) {
      wwLib.showAlert('Failed to update profile', 'error');
      return false;
    } finally {
      wwLib.hideLoading();
    }
  }
}
```

### 🔧 **Make.com Integration**

```javascript
// Make.com scenario for incremental data updates
function processDataUpdate(inputData) {
  const { recordId, table, updates, source } = inputData;
  
  try {
    // Get current record
    const currentRecord = getRecord({
      table: table,
      id: recordId
    });
    
    if (!currentRecord) {
      return {
        success: false,
        error: 'Record not found',
        record_id: recordId
      };
    }
    
    // Prepare incremental updates
    const patchData = {};
    
    // Handle numeric increments
    if (updates.incrementFields) {
      for (const [field, increment] of Object.entries(updates.incrementFields)) {
        const currentValue = currentRecord[field] || 0;
        patchData[field] = currentValue + increment;
      }
    }
    
    // Handle direct field updates
    if (updates.directFields) {
      Object.assign(patchData, updates.directFields);
    }
    
    // Handle array additions
    if (updates.arrayFields) {
      for (const [field, newItems] of Object.entries(updates.arrayFields)) {
        const currentArray = currentRecord[field] || [];
        patchData[field] = [...currentArray, ...newItems];
      }
    }
    
    // Add metadata
    patchData.last_updated_by = source;
    patchData.last_updated_via = 'make_automation';
    patchData.updated_at = new Date().toISOString();
    
    // Apply patch
    const updatedRecord = patchRecord({
      table: table,
      id: recordId,
      data: patchData
    });
    
    return {
      success: true,
      record: updatedRecord,
      changes_applied: Object.keys(patchData),
      message: 'Record updated successfully'
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message,
      record_id: recordId
    };
  }
}
```

## Data Filtering Strategies

### Comprehensive Input Filtering

```javascript
// Advanced data cleaning for patch operations
function cleanPatchData(rawData, allowedFields = []) {
  let cleanData = {};
  
  // Filter by allowed fields if specified
  if (allowedFields.length > 0) {
    for (const field of allowedFields) {
      if (rawData.hasOwnProperty(field)) {
        cleanData[field] = rawData[field];
      }
    }
  } else {
    cleanData = { ...rawData };
  }
  
  // Remove null values
  cleanData = filterNull(cleanData);
  
  // Remove empty strings
  cleanData = filterEmptyText(cleanData);
  
  // Remove undefined values
  for (const key in cleanData) {
    if (cleanData[key] === undefined) {
      delete cleanData[key];
    }
  }
  
  // Sanitize string values
  for (const [key, value] of Object.entries(cleanData)) {
    if (typeof value === 'string') {
      cleanData[key] = sanitizeString(value);
    }
  }
  
  return cleanData;
}

function sanitizeString(str) {
  return str
    .trim()
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '') // Remove scripts
    .replace(/[<>"'&]/g, match => { // Escape HTML entities
      const entities = {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;',
        '&': '&amp;'
      };
      return entities[match];
    });
}
```

### Smart Field Validation

```javascript
// Context-aware field validation
function validatePatchFields(data, recordType) {
  const errors = [];
  
  // Define validation rules per record type
  const validationRules = {
    user: {
      email: (value) => {
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          return 'Invalid email format';
        }
      },
      phone: (value) => {
        const cleaned = value.replace(/[\s\-\(\)]/g, '');
        if (!/^[\+]?[1-9][\d]{9,14}$/.test(cleaned)) {
          return 'Invalid phone format';
        }
      },
      age: (value) => {
        if (value < 13 || value > 120) {
          return 'Age must be between 13 and 120';
        }
      }
    },
    product: {
      price: (value) => {
        if (value < 0) {
          return 'Price cannot be negative';
        }
      },
      sku: (value) => {
        if (!/^[A-Z0-9\-]{3,20}$/.test(value)) {
          return 'Invalid SKU format';
        }
      }
    }
  };
  
  const rules = validationRules[recordType] || {};
  
  for (const [field, value] of Object.entries(data)) {
    if (rules[field]) {
      const error = rules[field](value);
      if (error) {
        errors.push(`${field}: ${error}`);
      }
    }
  }
  
  if (errors.length > 0) {
    throw new Error(`Validation failed: ${errors.join(', ')}`);
  }
  
  return true;
}
```

## 💡 **Try This**

### Beginner Challenge
Build a user preference updater:
1. Create a function that updates only email notification settings
2. Use patch to update just the notification fields
3. Add timestamp tracking for when preferences were last changed
4. Test with different combinations of preferences

### Intermediate Challenge
Create a post engagement tracker:
1. Build functions to increment view counts, likes, and comments
2. Use patch operations to update only the relevant counters
3. Add validation to prevent negative values
4. Implement rate limiting for rapid increments

### Advanced Challenge
Design a progressive profile completion system:
1. Track which profile fields are completed vs empty
2. Calculate completion percentage with each patch
3. Implement field-level validation and error handling
4. Create a system that awards points for profile completion

## Common Mistakes to Avoid

1. **Not filtering null/empty values** - Always clean data before patching
2. **Overwriting with blanks** - Patch will write empty values if provided
3. **Missing validation** - Validate patch data just like full records
4. **Forgetting timestamps** - Update modified timestamps when patching
5. **No error handling** - Handle validation and database errors gracefully
6. **Ignoring data types** - Ensure patched values match field types

## Best Practices

1. **Filter your inputs** - Use filterNull() and filterEmptyText() for safety
2. **Validate selectively** - Only validate fields being updated
3. **Use allowlists** - Define which fields can be patched
4. **Track changes** - Log what was modified and when
5. **Handle conflicts** - Check for concurrent modifications
6. **Sanitize data** - Clean user input before patching
7. **Test edge cases** - Verify behavior with null, empty, and invalid data

## Next Steps

- Explore [Edit Record](edit_record.md) for full record updates
- Master [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for atomic operations
- Learn [Query All Records](query_all_records.md) for data retrieval
- Understand [Data Validation](../best-practices/validation.md) patterns

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Patch operation discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Selective update techniques
- 📖 [CRUD Examples](../examples/database-operations.md) - Complete patch patterns
- 🔧 [Support](https://xano.com/support) - Database operation assistance


