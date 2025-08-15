---
title: "Add Record - Create New Database Entries"
description: "Learn how to create new records in your Xano database using the Add Record function with validation, error handling, and best practices for data integrity"
category: data-operations
tags:
  - Add Record
  - Database Operations
  - CRUD Operations
  - Data Creation
  - Validation
  - Error Handling
difficulty: beginner
reading_time: 8 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of databases
  - Knowledge of Xano tables and fields
  - Familiarity with function stacks
---

# Add Record - Create New Database Entries

## 📋 **Quick Summary**

**What it does:** The Add Record function creates new entries in your Xano database tables, allowing you to insert data with proper validation and error handling.

**Why it matters:** Adding records enables you to:
- **Create user accounts** and profiles
- **Store form submissions** from your applications
- **Build content management** systems
- **Capture transaction data** and orders
- **Maintain data integrity** with validation

**Time to implement:** 5-10 minutes for basic operations, 15-30 minutes with validation and error handling

---

## What You'll Learn

- How to use the Add Record function effectively
- Data validation and sanitization techniques
- Error handling patterns for record creation
- Integration with no-code platforms
- Best practices for secure data insertion

## Basic Add Record Usage

### Simple Record Creation

```javascript
// Basic add record example
const newUser = await addRecord({
  table: 'users',
  data: {
    email: 'john@example.com',
    name: 'John Doe',
    status: 'active',
    created_at: new Date().toISOString()
  }
});

// Returns the created record with auto-generated ID
console.log(newUser);
// Output: { id: 123, email: 'john@example.com', name: 'John Doe', ... }
```

### Function Stack Implementation

```javascript
// Complete add record function with validation
function createUserAccount(input) {
  // 1. Validate input data
  if (!input.email || !input.name) {
    throw new Error('Email and name are required');
  }
  
  // 2. Check email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(input.email)) {
    throw new Error('Invalid email format');
  }
  
  // 3. Sanitize input
  const sanitizedData = {
    email: input.email.toLowerCase().trim(),
    name: input.name.trim(),
    phone: input.phone ? input.phone.trim() : null,
    status: 'pending_verification'
  };
  
  // 4. Add timestamps
  const timestamp = new Date().toISOString();
  sanitizedData.created_at = timestamp;
  sanitizedData.updated_at = timestamp;
  
  // 5. Create the record
  const newUser = addRecord({
    table: 'users',
    data: sanitizedData
  });
  
  return {
    success: true,
    user: newUser,
    message: 'User account created successfully'
  };
}
```

## Advanced Add Record Patterns

### With Data Validation

```javascript
// Comprehensive user registration with validation
function registerUser(input) {
  const errors = [];
  
  // Required field validation
  if (!input.email) errors.push('Email is required');
  if (!input.password) errors.push('Password is required');
  if (!input.name) errors.push('Name is required');
  
  // Format validation
  if (input.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.email)) {
    errors.push('Invalid email format');
  }
  
  // Password strength validation
  if (input.password && input.password.length < 8) {
    errors.push('Password must be at least 8 characters');
  }
  
  if (errors.length > 0) {
    throw new Error(`Validation failed: ${errors.join(', ')}`);
  }
  
  // Check if user already exists
  const existingUser = queryAllRecords({
    table: 'users',
    filters: { email: input.email.toLowerCase() },
    limit: 1
  });
  
  if (existingUser.length > 0) {
    throw new Error('User with this email already exists');
  }
  
  // Hash password (placeholder - use actual hashing)
  const hashedPassword = hashPassword(input.password);
  
  // Create user record
  const newUser = addRecord({
    table: 'users',
    data: {
      email: input.email.toLowerCase().trim(),
      password_hash: hashedPassword,
      name: input.name.trim(),
      status: 'active',
      email_verified: false,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    }
  });
  
  // Create user profile
  const userProfile = addRecord({
    table: 'user_profiles',
    data: {
      user_id: newUser.id,
      display_name: input.name.trim(),
      bio: '',
      avatar_url: null,
      created_at: new Date().toISOString()
    }
  });
  
  return {
    success: true,
    user: {
      id: newUser.id,
      email: newUser.email,
      name: newUser.name,
      profile: userProfile
    },
    message: 'Registration successful'
  };
}
```

### E-commerce Order Creation

```javascript
// Create order with multiple related records
function createOrder(input) {
  // Validate customer
  const customer = getRecord({
    table: 'customers',
    id: input.customer_id
  });
  
  if (!customer) {
    throw new Error('Customer not found');
  }
  
  // Calculate order totals
  let subtotal = 0;
  const processedItems = [];
  
  for (const item of input.items) {
    const product = getRecord({
      table: 'products',
      id: item.product_id
    });
    
    if (!product || product.status !== 'active') {
      throw new Error(`Product ${item.product_id} is not available`);
    }
    
    const itemTotal = product.price * item.quantity;
    subtotal += itemTotal;
    
    processedItems.push({
      product_id: product.id,
      product_name: product.name,
      quantity: item.quantity,
      unit_price: product.price,
      total_price: itemTotal
    });
  }
  
  const tax = subtotal * 0.08; // 8% tax
  const total = subtotal + tax;
  
  // Create order record
  const order = addRecord({
    table: 'orders',
    data: {
      customer_id: customer.id,
      order_number: `ORD-${Date.now()}`,
      subtotal: subtotal,
      tax_amount: tax,
      total_amount: total,
      status: 'pending',
      created_at: new Date().toISOString()
    }
  });
  
  // Create order items
  for (const item of processedItems) {
    addRecord({
      table: 'order_items',
      data: {
        order_id: order.id,
        ...item,
        created_at: new Date().toISOString()
      }
    });
  }
  
  return {
    success: true,
    order: order,
    items: processedItems,
    message: 'Order created successfully'
  };
}
```

## No-Code Platform Integration

### 🔗 **n8n Integration**

```javascript
// n8n workflow for processing form submissions
function processFormSubmission($input) {
  const formData = $input.body;
  
  try {
    // Validate required fields
    const required = ['name', 'email', 'message'];
    const missing = required.filter(field => !formData[field]);
    
    if (missing.length > 0) {
      return {
        success: false,
        error: `Missing required fields: ${missing.join(', ')}`
      };
    }
    
    // Create contact record
    const contact = addRecord({
      table: 'contacts',
      data: {
        name: formData.name.trim(),
        email: formData.email.toLowerCase().trim(),
        message: formData.message.trim(),
        source: 'website_form',
        status: 'new',
        created_at: new Date().toISOString()
      }
    });
    
    // Send notification email
    sendEmail({
      to: 'admin@company.com',
      subject: 'New Contact Form Submission',
      body: `New contact from ${contact.name} (${contact.email}): ${contact.message}`
    });
    
    return {
      success: true,
      contact_id: contact.id,
      message: 'Contact created successfully'
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
// WeWeb form submission handler
class WeWebDataSubmission {
  static async submitForm(formData) {
    try {
      // Show loading state
      wwLib.showLoading();
      
      // Validate form data
      const validation = this.validateForm(formData);
      if (!validation.valid) {
        wwLib.showAlert(validation.message, 'error');
        return false;
      }
      
      // Submit to Xano
      const response = await wwLib.api.post({
        url: `${wwLib.envVars.XANO_API_URL}/contacts`,
        data: {
          name: formData.name,
          email: formData.email,
          phone: formData.phone,
          message: formData.message,
          source: 'webapp'
        },
        headers: {
          'Content-Type': 'application/json'
        }
      });
      
      if (response.data.success) {
        // Clear form
        wwLib.form.reset();
        
        // Show success message
        wwLib.showAlert('Thank you! Your message has been sent.', 'success');
        
        // Redirect to thank you page
        wwLib.navigate('/thank-you');
        
        return true;
      } else {
        wwLib.showAlert('Failed to submit form. Please try again.', 'error');
        return false;
      }
      
    } catch (error) {
      console.error('Form submission error:', error);
      wwLib.showAlert('An error occurred. Please try again.', 'error');
      return false;
    } finally {
      wwLib.hideLoading();
    }
  }
  
  static validateForm(formData) {
    if (!formData.name || formData.name.trim().length < 2) {
      return { valid: false, message: 'Name must be at least 2 characters' };
    }
    
    if (!formData.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      return { valid: false, message: 'Please enter a valid email address' };
    }
    
    if (!formData.message || formData.message.trim().length < 10) {
      return { valid: false, message: 'Message must be at least 10 characters' };
    }
    
    return { valid: true };
  }
}
```

### 🔧 **Make.com Integration**

```javascript
// Make.com scenario for processing webhook data
function processMakeWebhook(inputData) {
  const data = inputData.body;
  
  // Transform data for Xano format
  const transformedData = {
    lead_source: data.source || 'make_automation',
    first_name: data.firstName,
    last_name: data.lastName,
    email: data.email,
    phone: data.phone,
    company: data.company,
    interest_level: data.score > 80 ? 'high' : data.score > 50 ? 'medium' : 'low',
    tags: data.tags ? data.tags.split(',').map(tag => tag.trim()) : [],
    created_at: new Date().toISOString()
  };
  
  // Create lead record
  const newLead = addRecord({
    table: 'leads',
    data: transformedData
  });
  
  // Create follow-up task
  addRecord({
    table: 'tasks',
    data: {
      title: `Follow up with ${newLead.first_name} ${newLead.last_name}`,
      description: `New lead from ${newLead.lead_source}`,
      lead_id: newLead.id,
      assigned_to: getNextSalesRep(),
      due_date: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(), // 24 hours
      status: 'pending',
      created_at: new Date().toISOString()
    }
  });
  
  return {
    success: true,
    lead_id: newLead.id,
    message: 'Lead created and task assigned'
  };
}
```

## Error Handling Patterns

### Comprehensive Error Management

```javascript
// Robust error handling for add record operations
function createRecordWithErrorHandling(table, data) {
  try {
    // Pre-validation
    if (!table || !data) {
      throw new Error('Table name and data are required');
    }
    
    // Sanitize data
    const sanitizedData = sanitizeInputData(data);
    
    // Add audit fields
    sanitizedData.created_at = new Date().toISOString();
    sanitizedData.created_by = getCurrentUserId();
    
    // Attempt to create record
    const newRecord = addRecord({
      table: table,
      data: sanitizedData
    });
    
    // Log successful creation
    logActivity({
      action: 'record_created',
      table: table,
      record_id: newRecord.id,
      user_id: getCurrentUserId()
    });
    
    return {
      success: true,
      data: newRecord,
      message: 'Record created successfully'
    };
    
  } catch (error) {
    // Log error
    logError({
      action: 'add_record_failed',
      table: table,
      error: error.message,
      data: data,
      user_id: getCurrentUserId()
    });
    
    // Return user-friendly error
    return {
      success: false,
      error: formatErrorMessage(error),
      code: getErrorCode(error)
    };
  }
}

function sanitizeInputData(data) {
  const sanitized = {};
  
  for (const [key, value] of Object.entries(data)) {
    if (typeof value === 'string') {
      // Trim whitespace and prevent XSS
      sanitized[key] = value.trim().replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
    } else {
      sanitized[key] = value;
    }
  }
  
  return sanitized;
}
```

## 💡 **Try This**

### Beginner Challenge
Create a simple contact form:
1. Set up a contacts table with name, email, message fields
2. Create an add record function with basic validation
3. Test with sample data
4. Add error handling for duplicate emails

### Intermediate Challenge
Build a user registration system:
1. Create users and user_profiles tables
2. Implement password validation and hashing
3. Add email verification workflow
4. Create welcome email automation

### Advanced Challenge
Design a multi-table order system:
1. Create orders, order_items, and inventory tables
2. Implement atomic transactions
3. Add inventory checking and reservation
4. Build order confirmation email system

## Common Mistakes to Avoid

1. **Missing validation** - Always validate input data before insertion
2. **No error handling** - Implement proper error catching and user feedback
3. **Forgotten timestamps** - Include created_at and updated_at fields
4. **Ignoring duplicates** - Check for existing records when appropriate
5. **No data sanitization** - Clean user input to prevent security issues

## Best Practices

1. **Validate everything** - Never trust user input
2. **Use transactions** - For operations affecting multiple tables
3. **Add audit trails** - Track who created what and when
4. **Handle errors gracefully** - Provide meaningful feedback
5. **Sanitize inputs** - Prevent XSS and injection attacks
6. **Use consistent naming** - Follow table and field naming conventions

## Next Steps

- Learn [Edit Record](edit_record.md) for updating existing data
- Master [Query All Records](query_all_records.md) for data retrieval
- Explore [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for complex operations
- Understand [Validation Patterns](../best-practices/validation.md) for data integrity

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Database operation discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step database guides
- 📖 [CRUD Examples](../examples/database-operations.md) - Complete implementation patterns
- 🔧 [Support](https://xano.com/support) - Database operation assistance