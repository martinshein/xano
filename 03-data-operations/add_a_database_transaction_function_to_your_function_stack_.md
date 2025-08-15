---
title: "Database Transactions - Atomic Operations"
description: "Master database transactions in Xano for atomic operations, data consistency, and error recovery. Learn to build reliable multi-step database workflows"
category: data-operations
tags:
  - Database Transactions
  - Atomic Operations
  - Data Consistency
  - Error Recovery
  - ACID Properties
  - Rollback Operations
difficulty: advanced
reading_time: 12 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of database operations
  - Familiarity with CRUD operations
  - Knowledge of error handling patterns
---

# Database Transactions - Atomic Operations

## 📋 **Quick Summary**

**What it does:** Database transactions ensure that multiple database operations either all succeed together or all fail together, maintaining data consistency and integrity across complex workflows.

**Why it matters:** Transactions enable you to:
- **Maintain data consistency** across multiple operations
- **Prevent partial updates** that could corrupt your data
- **Handle errors gracefully** with automatic rollback
- **Build reliable complex workflows** with confidence
- **Ensure ACID compliance** for critical business operations

**Time to implement:** 20-30 minutes for basic transactions, 1+ hour for complex multi-table workflows

---

## What You'll Learn

- How to implement database transactions in Xano
- Best practices for transaction design
- Error handling and rollback strategies
- Performance optimization for transaction-heavy operations
- Real-world transaction patterns and use cases

## Understanding Database Transactions

### ACID Properties

```javascript
// Transaction example demonstrating ACID properties
async function demonstrateACIDTransaction() {
  const transaction = await startTransaction();
  
  try {
    // Atomicity: All operations succeed or all fail
    const order = await addRecord({
      table: 'orders',
      data: {
        customer_id: 123,
        total_amount: 150.00,
        status: 'processing'
      },
      transaction: transaction
    });
    
    // Consistency: Database remains in valid state
    await patchRecord({
      table: 'customers',
      id: 123,
      fields: {
        total_orders: { increment: 1 },
        total_spent: { increment: 150.00 }
      },
      transaction: transaction
    });
    
    // Isolation: Transaction doesn't interfere with others
    await patchRecord({
      table: 'inventory',
      filters: { product_id: 456 },
      fields: {
        quantity: { decrement: 1 },
        reserved_quantity: { decrement: 1 }
      },
      transaction: transaction
    });
    
    // Durability: Changes persist after commit
    await commitTransaction(transaction);
    
    return { success: true, order_id: order.id };
    
  } catch (error) {
    // Rollback on any error
    await rollbackTransaction(transaction);
    throw error;
  }
}
```

## Basic Transaction Patterns

### Simple Transaction Wrapper

```javascript
// Generic transaction wrapper for any operations
async function withTransaction(operations) {
  const transaction = await startTransaction();
  
  try {
    const results = [];
    
    for (const operation of operations) {
      const result = await operation(transaction);
      results.push(result);
    }
    
    await commitTransaction(transaction);
    return results;
    
  } catch (error) {
    await rollbackTransaction(transaction);
    throw new Error(`Transaction failed: ${error.message}`);
  }
}

// Usage example
const results = await withTransaction([
  (tx) => addRecord({ table: 'users', data: userData, transaction: tx }),
  (tx) => addRecord({ table: 'profiles', data: profileData, transaction: tx }),
  (tx) => addRecord({ table: 'preferences', data: prefsData, transaction: tx })
]);
```

### Error Handling Strategies

```javascript
// Comprehensive error handling in transactions
class TransactionManager {
  static async executeWithRetry(operations, maxRetries = 3) {
    let lastError;
    
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      const transaction = await startTransaction();
      
      try {
        const results = [];
        
        for (const operation of operations) {
          const result = await operation(transaction);
          results.push(result);
        }
        
        await commitTransaction(transaction);
        return {
          success: true,
          results: results,
          attempts: attempt
        };
        
      } catch (error) {
        await rollbackTransaction(transaction);
        lastError = error;
        
        // Log attempt
        console.warn(`Transaction attempt ${attempt} failed:`, error.message);
        
        // Check if error is retryable
        if (!this.isRetryableError(error) || attempt === maxRetries) {
          break;
        }
        
        // Wait before retry (exponential backoff)
        await this.delay(Math.pow(2, attempt) * 1000);
      }
    }
    
    return {
      success: false,
      error: lastError.message,
      attempts: maxRetries
    };
  }
  
  static isRetryableError(error) {
    const retryableErrors = [
      'deadlock detected',
      'connection timeout',
      'temporary failure',
      'lock timeout'
    ];
    
    return retryableErrors.some(msg => 
      error.message.toLowerCase().includes(msg)
    );
  }
  
  static delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

## Complex Transaction Workflows

### E-commerce Order Processing

```javascript
// Complete order processing with transaction
async function processCompleteOrder(orderData) {
  const transaction = await startTransaction();
  
  try {
    // 1. Validate customer and payment
    const customer = await getRecord({
      table: 'customers',
      id: orderData.customer_id,
      transaction: transaction
    });
    
    if (!customer) {
      throw new Error('Customer not found');
    }
    
    if (customer.status === 'suspended') {
      throw new Error('Customer account is suspended');
    }
    
    // 2. Validate inventory and reserve items
    const reservations = [];
    let totalAmount = 0;
    
    for (const item of orderData.items) {
      const product = await getRecord({
        table: 'products',
        id: item.product_id,
        transaction: transaction
      });
      
      if (!product || product.status !== 'active') {
        throw new Error(`Product ${item.product_id} is not available`);
      }
      
      const inventory = await getRecord({
        table: 'inventory',
        filters: { product_id: item.product_id },
        transaction: transaction
      });
      
      if (inventory.available_quantity < item.quantity) {
        throw new Error(`Insufficient inventory for ${product.name}`);
      }
      
      // Reserve inventory
      await patchRecord({
        table: 'inventory',
        filters: { product_id: item.product_id },
        fields: {
          available_quantity: { decrement: item.quantity },
          reserved_quantity: { increment: item.quantity }
        },
        transaction: transaction
      });
      
      const itemTotal = product.price * item.quantity;
      totalAmount += itemTotal;
      
      reservations.push({
        product_id: item.product_id,
        quantity: item.quantity,
        unit_price: product.price,
        total_price: itemTotal
      });
    }
    
    // 3. Apply discounts and calculate final amount
    let discountAmount = 0;
    if (orderData.coupon_code) {
      const coupon = await getRecord({
        table: 'coupons',
        filters: { 
          code: orderData.coupon_code,
          active: true,
          expires_at: { $gte: new Date().toISOString() }
        },
        transaction: transaction
      });
      
      if (coupon) {
        discountAmount = coupon.type === 'percentage' 
          ? totalAmount * (coupon.value / 100)
          : coupon.value;
        
        // Update coupon usage
        await patchRecord({
          table: 'coupons',
          id: coupon.id,
          fields: {
            usage_count: { increment: 1 }
          },
          transaction: transaction
        });
      }
    }
    
    const taxAmount = (totalAmount - discountAmount) * 0.08;
    const finalAmount = totalAmount - discountAmount + taxAmount;
    
    // 4. Process payment
    const payment = await addRecord({
      table: 'payments',
      data: {
        customer_id: customer.id,
        amount: finalAmount,
        payment_method: orderData.payment_method,
        status: 'processing',
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // Simulate payment processing
    if (finalAmount > customer.credit_limit) {
      throw new Error('Payment amount exceeds credit limit');
    }
    
    // Update payment status
    await patchRecord({
      table: 'payments',
      id: payment.id,
      fields: {
        status: 'completed',
        processed_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 5. Create order record
    const order = await addRecord({
      table: 'orders',
      data: {
        order_number: `ORD-${Date.now()}-${Math.random().toString(36).substr(2, 4)}`,
        customer_id: customer.id,
        payment_id: payment.id,
        subtotal: totalAmount,
        discount_amount: discountAmount,
        tax_amount: taxAmount,
        total_amount: finalAmount,
        status: 'confirmed',
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 6. Create order items
    for (const reservation of reservations) {
      await addRecord({
        table: 'order_items',
        data: {
          order_id: order.id,
          product_id: reservation.product_id,
          quantity: reservation.quantity,
          unit_price: reservation.unit_price,
          total_price: reservation.total_price
        },
        transaction: transaction
      });
    }
    
    // 7. Update customer statistics
    await patchRecord({
      table: 'customers',
      id: customer.id,
      fields: {
        total_orders: { increment: 1 },
        total_spent: { increment: finalAmount },
        last_order_date: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 8. Create audit trail
    await addRecord({
      table: 'order_audit',
      data: {
        order_id: order.id,
        action: 'order_created',
        details: {
          items_count: reservations.length,
          discount_applied: discountAmount > 0,
          coupon_used: orderData.coupon_code || null
        },
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // Commit all changes
    await commitTransaction(transaction);
    
    return {
      success: true,
      order: order,
      payment: payment,
      total_amount: finalAmount,
      message: 'Order processed successfully'
    };
    
  } catch (error) {
    // Rollback all changes on any error
    await rollbackTransaction(transaction);
    
    return {
      success: false,
      error: error.message,
      timestamp: new Date().toISOString()
    };
  }
}
```

### User Registration with Profile Setup

```javascript
// Complete user onboarding transaction
async function createUserWithProfile(registrationData) {
  const transaction = await startTransaction();
  
  try {
    // 1. Validate unique email
    const existingUser = await queryAllRecords({
      table: 'users',
      filters: { email: registrationData.email.toLowerCase() },
      limit: 1,
      transaction: transaction
    });
    
    if (existingUser.length > 0) {
      throw new Error('Email already registered');
    }
    
    // 2. Create user account
    const user = await addRecord({
      table: 'users',
      data: {
        email: registrationData.email.toLowerCase(),
        password_hash: await hashPassword(registrationData.password),
        status: 'active',
        email_verified: false,
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 3. Create user profile
    const profile = await addRecord({
      table: 'user_profiles',
      data: {
        user_id: user.id,
        first_name: registrationData.first_name,
        last_name: registrationData.last_name,
        display_name: `${registrationData.first_name} ${registrationData.last_name}`,
        bio: '',
        avatar_url: null,
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 4. Set default preferences
    const preferences = await addRecord({
      table: 'user_preferences',
      data: {
        user_id: user.id,
        email_notifications: true,
        marketing_emails: registrationData.marketing_consent || false,
        theme: 'light',
        language: 'en',
        timezone: registrationData.timezone || 'UTC'
      },
      transaction: transaction
    });
    
    // 5. Create initial subscription (free tier)
    const subscription = await addRecord({
      table: 'subscriptions',
      data: {
        user_id: user.id,
        plan_type: 'free',
        status: 'active',
        started_at: new Date().toISOString(),
        features: ['basic_access', 'limited_storage']
      },
      transaction: transaction
    });
    
    // 6. Add to default user segments
    await addRecord({
      table: 'user_segments',
      data: {
        user_id: user.id,
        segment_name: 'new_users',
        added_at: new Date().toISOString(),
        source: 'registration'
      },
      transaction: transaction
    });
    
    // 7. Create email verification token
    const verificationToken = generateSecureToken(32);
    await addRecord({
      table: 'email_verification_tokens',
      data: {
        user_id: user.id,
        token: verificationToken,
        expires_at: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(), // 24 hours
        created_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // 8. Update registration statistics
    await patchRecord({
      table: 'app_statistics',
      filters: { metric_name: 'total_registrations' },
      fields: {
        value: { increment: 1 },
        updated_at: new Date().toISOString()
      },
      transaction: transaction
    });
    
    // Commit all changes
    await commitTransaction(transaction);
    
    // Send welcome email (outside transaction)
    try {
      await sendWelcomeEmail(user.email, {
        name: profile.display_name,
        verification_token: verificationToken
      });
    } catch (emailError) {
      console.warn('Welcome email failed:', emailError.message);
      // Don't fail the transaction for email issues
    }
    
    return {
      success: true,
      user: {
        id: user.id,
        email: user.email,
        profile: profile,
        subscription: subscription
      },
      message: 'User created successfully'
    };
    
  } catch (error) {
    await rollbackTransaction(transaction);
    
    return {
      success: false,
      error: error.message,
      code: 'REGISTRATION_FAILED'
    };
  }
}

function generateSecureToken(length) {
  const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  let token = '';
  for (let i = 0; i < length; i++) {
    token += chars[Math.floor(Math.random() * chars.length)];
  }
  return token;
}
```

## Performance Optimization

### Transaction Best Practices

```javascript
// Optimized transaction patterns
class TransactionOptimizer {
  static async optimizeTransactionBatch(operations) {
    // Group operations by table for better lock efficiency
    const groupedOps = this.groupOperationsByTable(operations);
    
    // Execute in order of dependency
    const executionOrder = this.determineDependencyOrder(groupedOps);
    
    const transaction = await startTransaction();
    
    try {
      const results = {};
      
      for (const tableGroup of executionOrder) {
        // Process operations on same table together
        results[tableGroup.table] = await this.executeTableOperations(
          tableGroup.operations, 
          transaction
        );
      }
      
      await commitTransaction(transaction);
      return { success: true, results };
      
    } catch (error) {
      await rollbackTransaction(transaction);
      throw error;
    }
  }
  
  static groupOperationsByTable(operations) {
    const groups = {};
    
    operations.forEach(op => {
      const table = op.table || op.target_table;
      if (!groups[table]) {
        groups[table] = [];
      }
      groups[table].push(op);
    });
    
    return Object.keys(groups).map(table => ({
      table,
      operations: groups[table]
    }));\n  }\n  \n  static determineDependencyOrder(groupedOps) {\n    // Simple dependency resolution\n    const independent = [];\n    const dependent = [];\n    \n    groupedOps.forEach(group => {\n      const hasDependencies = group.operations.some(op => \n        op.depends_on || op.requires\n      );\n      \n      if (hasDependencies) {\n        dependent.push(group);\n      } else {\n        independent.push(group);\n      }\n    });\n    \n    return [...independent, ...dependent];\n  }\n  \n  static async executeTableOperations(operations, transaction) {\n    const results = [];\n    \n    // Batch similar operations\n    const adds = operations.filter(op => op.type === 'add');\n    const updates = operations.filter(op => op.type === 'update');\n    const deletes = operations.filter(op => op.type === 'delete');\n    \n    // Execute adds first (for foreign key dependencies)\n    for (const op of adds) {\n      const result = await this.executeOperation(op, transaction);\n      results.push(result);\n    }\n    \n    // Then updates\n    for (const op of updates) {\n      const result = await this.executeOperation(op, transaction);\n      results.push(result);\n    }\n    \n    // Finally deletes\n    for (const op of deletes) {\n      const result = await this.executeOperation(op, transaction);\n      results.push(result);\n    }\n    \n    return results;\n  }\n  \n  static async executeOperation(operation, transaction) {\n    switch (operation.type) {\n      case 'add':\n        return await addRecord({\n          table: operation.table,\n          data: operation.data,\n          transaction: transaction\n        });\n        \n      case 'update':\n        return await patchRecord({\n          table: operation.table,\n          id: operation.id,\n          fields: operation.fields,\n          transaction: transaction\n        });\n        \n      case 'delete':\n        return await deleteRecord({\n          table: operation.table,\n          id: operation.id,\n          transaction: transaction\n        });\n        \n      default:\n        throw new Error(`Unknown operation type: ${operation.type}`);\n    }\n  }\n}
```

## 💡 **Try This**

### Beginner Challenge
Create basic transactions:
1. Build a simple transfer between two accounts
2. Create user with profile in single transaction
3. Add error handling and rollback
4. Test with intentional failures

### Intermediate Challenge
Build complex workflows:
1. Implement complete order processing system
2. Create multi-step user registration
3. Add inventory management with reservations
4. Build audit trail for all operations

### Advanced Challenge
Design enterprise transaction system:
1. Create transaction optimization framework
2. Implement distributed transaction patterns
3. Add comprehensive error recovery
4. Build transaction monitoring and analytics

## Common Pitfalls to Avoid

1. **Long-running transactions** - Keep transactions short and focused
2. **Nested transactions** - Avoid transactions within transactions
3. **External API calls** - Don't call external services inside transactions
4. **Missing error handling** - Always have rollback strategies
5. **Lock contention** - Design to minimize database locks

## Best Practices

1. **Keep transactions atomic** - Group related operations only
2. **Handle errors gracefully** - Always rollback on failures
3. **Minimize transaction time** - Reduce lock duration
4. **Test failure scenarios** - Verify rollback behavior
5. **Monitor performance** - Track transaction metrics
6. **Use proper isolation** - Choose appropriate isolation levels

## Next Steps

- Master [Database Requests](database_requests.md) for comprehensive operations
- Learn [Error Handling](../best-practices/error-handling.md) patterns
- Explore [Performance Optimization](../best-practices/performance.md) techniques
- Understand [Data Consistency](../best-practices/data-integrity.md) strategies

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Transaction discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Database transaction guides
- 📖 [Advanced Patterns](../best-practices/transaction-patterns.md) - Enterprise patterns
- 🔧 [Support](https://xano.com/support) - Complex transaction assistance