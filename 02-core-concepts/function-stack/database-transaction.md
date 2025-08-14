---
title: "Database Transactions - All or Nothing Operations"
description: "Ensure database operations succeed together or fail together for data integrity"
category: function-stack
subcategory: database
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- database
- transactions
- data-integrity
- safety
- operations
---

# Database Transactions - All or Nothing Operations



## Quick Summary

> **What it is:** A way to group database operations so they all succeed or all fail together
> 
> **When to use:** Critical operations where partial completion would corrupt data (payments, transfers, multi-table updates)
> 
> **Key benefit:** Guarantees data consistency - no half-completed operations
> 
> **Perfect for:** Non-developers building reliable financial, inventory, or booking systems

## What You'll Learn

- Understanding transaction safety
- When to use transactions
- Setting up transaction blocks
- Handling success and failure
- Best practices for reliability

## What Are Database Transactions?

Think of transactions like a bank transfer:
1. **Withdraw** $100 from Account A
2. **Deposit** $100 to Account B

If step 2 fails, step 1 must be reversed - otherwise money disappears!

Transactions ensure:
- **All steps complete** = Changes saved
- **Any step fails** = All changes reversed

## Real-World Examples

### Money Transfer
```javascript
Transaction {
  1. Check balance >= amount
  2. Deduct from sender
  3. Add to receiver
  4. Create transfer record
}
// If ANY step fails, ALL are reversed
```

### Inventory Purchase
```javascript
Transaction {
  1. Check stock availability
  2. Reduce inventory count
  3. Create order record
  4. Reserve items for customer
}
// All succeed or none do
```

### User Registration
```javascript
Transaction {
  1. Create user account
  2. Create profile record
  3. Create settings record
  4. Send welcome email (not in transaction)
}
// Email isn't critical for data integrity
```

## Setting Up Transactions

### Step 1: Add Transaction Block

1. Click + in function stack
2. Select "Database Transaction"
3. No additional settings needed
4. Click Save

### Step 2: Add Database Operations

Drag operations INTO the transaction:
- Query All Records
- Add Record
- Edit Record
- Delete Record
- Any database function

### Step 3: Non-Database Functions

You can include:
- Conditionals
- Variables
- Data manipulation
- Calculations

These won't trigger rollback on error!

## Important: What Triggers Rollback

### WILL Rollback Transaction
❌ Database errors:
- Constraint violations
- Foreign key errors
- Duplicate unique values
- Connection failures

### WON'T Rollback Transaction
✅ Non-database errors:
- API call failures
- Variable errors
- Conditional logic
- Math errors

## Integration Examples

### With n8n - Order Processing

```javascript
// n8n sends order data
Order_Data = Webhook Input

Transaction {
  // All must succeed
  1. Create order record
  2. Update inventory
  3. Apply customer credit
  4. Create shipping record
}

// Outside transaction (can fail safely)
Send_Confirmation_Email()
Update_Analytics()
```

### With WeWeb - Booking System

```javascript
// WeWeb booking form
Booking_Data = Input

Transaction {
  // Critical operations
  1. Check availability
  2. Create booking
  3. Mark slots as taken
  4. Apply payment hold
}

// Non-critical (outside)
Send_Notification()
Log_Activity()
```

## Common Transaction Patterns

### Parent-Child Records

```javascript
Transaction {
  // Create parent
  order = Add_Order_Record()
  
  // Create children
  For Each item in cart {
    Add_Order_Item(order.id, item)
  }
}
```

### Balance Updates

```javascript
Transaction {
  // Get current balance
  account = Get_Account(user_id)
  
  // Update balance
  new_balance = account.balance - amount
  
  // Save updated balance
  Update_Account(user_id, new_balance)
  
  // Create transaction log
  Add_Transaction_Log(user_id, amount)
}
```

### Multi-Table Updates

```javascript
Transaction {
  // Update user table
  Update_User_Status(user_id, "premium")
  
  // Update subscription table
  Add_Subscription(user_id, plan_id)
  
  // Update billing table
  Add_Billing_Record(user_id, amount)
}
```

## Error Handling

### With Transactions

```javascript
Try {
  Transaction {
    // Database operations
    Update_Inventory()
    Create_Order()
  }
  return { success: true }
} Catch {
  // All changes reversed automatically
  return { success: false, error: "Order failed" }
}
```

### Without Transactions (Dangerous!)

```javascript
// DON'T DO THIS for critical operations
Update_Inventory()  // Succeeds
Create_Order()      // Fails
// Now inventory is wrong!
```

## Best Practices

### Keep Transactions Small

```javascript
// Good: Focused transaction
Transaction {
  Update_Balance()
  Create_Log()
}

// Avoid: Too many operations
Transaction {
  20+ database operations
  Complex logic
  External API calls
}
```

### Critical Operations Only

```javascript
Transaction {
  // Critical: Must succeed together
  Charge_Payment()
  Create_Order()
}

// Non-critical: Outside transaction
Send_Email()
Update_Analytics()
```

### Test Rollback Scenarios

```javascript
Transaction {
  Update_Record_1()  // Will succeed
  Update_Record_2()  // Force error to test
}
// Verify Record_1 changes were reversed
```

## Performance Considerations

### Transaction Locks

During transaction:
- Tables may be locked
- Other operations wait
- Keep transactions quick

### Resource Usage

- Transactions use more memory
- Rollback requires overhead
- Balance safety vs performance

## Common Gotchas

### External Services

```javascript
// WRONG: API call in transaction
Transaction {
  Update_Database()
  Call_Payment_API()  // If this fails, database rolls back
                      // but payment might have processed!
}

// RIGHT: API call outside
Call_Payment_API()
if (payment_success) {
  Transaction {
    Update_Database()
  }
}
```

### Read Operations

```javascript
// Reads don't need transactions
Transaction {
  Get_User()  // Unnecessary
  Get_Settings()  // Unnecessary
}

// Better
user = Get_User()
settings = Get_Settings()
Transaction {
  Update_User()
  Update_Settings()
}
```

## Try This

Create a points transfer system:
1. Add transaction block
2. Check sender has enough points
3. Deduct from sender
4. Add to receiver
5. Create transfer log
6. Test with insufficient points

## Pro Tips

💡 **Test Failures:** Intentionally cause errors to verify rollback

💡 **Log Outside:** Keep audit logs outside transactions

💡 **Quick Operations:** Minimize time in transaction

💡 **Validate First:** Check conditions before starting transaction

💡 **Document Critical:** Mark which operations require transactions

## When NOT to Use Transactions

- Simple read operations
- Single record updates
- Non-critical operations
- External API calls
- File operations

## Next Steps

1. Identify critical operations
2. Add transaction blocks
3. Test rollback scenarios
4. Monitor performance
5. Document transaction logic

Remember: Transactions are your safety net for critical operations - use them to build bulletproof systems!