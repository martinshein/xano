---
title: "Bulk Operations - Mass Database Actions"
description: "Process multiple records efficiently with bulk insert, update, and delete operations in Xano"
category: function-stack
subcategory: database-operations
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- bulk-operations
- performance
- database
- batch-processing
- optimization
---

# Bulk Operations - Mass Database Actions

## Quick Summary

> **What it is:** Database functions that process multiple records in a single operation instead of one-by-one
> 
> **When to use:** When you need to create, update, or delete many records at once - imports, mass updates, batch processing
> 
> **Key benefit:** 10-100x faster than individual operations, reduces database load
> 
> **Common uses:** CSV imports, mass updates, batch deletions, data migrations

## What You'll Learn

- Bulk insert, update, and delete operations
- Performance comparison with loops
- Error handling in bulk operations
- Best practices for large datasets
- Integration patterns with n8n and WeWeb

## Why Use Bulk Operations?

### Performance Comparison

```javascript
// Bad: Loop with individual operations (slow)
FOR EACH item IN 1000_items {
  Add Record: products (item)  // 1000 database calls
}
// Time: ~10 seconds

// Good: Bulk operation (fast)
Bulk Add Records: products (1000_items)  // 1 database call
// Time: ~0.5 seconds

// Result: 20x faster!
```

## Bulk Insert

### Basic Bulk Insert

```javascript
// Prepare data array
new_products = [
  { name: "Product A", price: 19.99, sku: "SKU-001" },
  { name: "Product B", price: 29.99, sku: "SKU-002" },
  { name: "Product C", price: 39.99, sku: "SKU-003" }
  // ... hundreds more
]

// Single operation to insert all
Bulk Add Records: products
  Data: new_products
  Return: inserted_records

// Returns array of created records with IDs
```

### CSV Import Example

```javascript
// Import CSV data
Import Products From CSV:
  // Parse CSV file
  csv_data = Parse_CSV(input.file)
  
  // Transform to match database schema
  products_to_import = []
  FOR EACH row IN csv_data {
    product = {
      name: row.product_name,
      price: DECIMAL(row.price),
      sku: row.sku_code,
      category: row.category,
      stock: INTEGER(row.quantity),
      created_at: NOW()
    }
    ARRAY_PUSH(products_to_import, product)
  }
  
  // Bulk insert all at once
  imported = Bulk Add Records: products (products_to_import)
  
  Return {
    success: true,
    imported_count: imported.length,
    first_id: imported[0].id,
    last_id: imported[imported.length - 1].id
  }
```

## Bulk Update

### Update Multiple Records

```javascript
// Update prices for multiple products
Bulk Update Records: products
  Filter: category = "electronics"
  Updates: {
    price: price * 1.1,  // 10% increase
    last_modified: NOW(),
    modified_by: auth.user_id
  }
  
// Returns count of updated records
```

### Conditional Bulk Updates

```javascript
// Different updates for different records
updates_list = [
  { id: 1, status: "active", discount: 10 },
  { id: 2, status: "inactive", discount: 0 },
  { id: 3, status: "active", discount: 15 }
]

// Apply specific updates to specific records
FOR EACH update IN updates_list {
  Bulk Update Records: products
    Filter: id = update.id
    Updates: {
      status: update.status,
      discount_percentage: update.discount
    }
}
```

### Mass Status Update

```javascript
// Archive old orders
Bulk Update Records: orders
  Filter: {
    created_at: { "<": "2023-01-01" },
    status: "completed"
  }
  Updates: {
    archived: true,
    archived_date: NOW(),
    archived_by: "system"
  }

// Activate seasonal products
Bulk Update Records: products
  Filter: {
    seasonal: true,
    season: "winter"
  }
  Updates: {
    active: true,
    featured: true
  }
```

## Bulk Delete

### Safe Bulk Delete

```javascript
// Delete with confirmation
records_to_delete = Query: temporary_data
  WHERE created_at < DATE_SUB(NOW(), 30, 'days')

IF (records_to_delete.count > 0) {
  // Log before deletion
  Log("Deleting " + records_to_delete.count + " old records")
  
  // Perform bulk delete
  deleted_count = Bulk Delete Records: temporary_data
    Filter: created_at < DATE_SUB(NOW(), 30, 'days')
  
  Return {
    deleted: deleted_count,
    message: "Cleanup completed"
  }
}
```

### Cascade Delete Pattern

```javascript
// Delete user and all related data
Delete User With Data:
  user_id = input.user_id
  
  // Delete in correct order (dependencies first)
  Bulk Delete Records: user_sessions WHERE user_id = user_id
  Bulk Delete Records: user_preferences WHERE user_id = user_id
  Bulk Delete Records: user_activities WHERE user_id = user_id
  Bulk Delete Records: user_files WHERE user_id = user_id
  
  // Finally delete user
  Delete Record: users WHERE id = user_id
  
  Return { success: true, message: "User and data deleted" }
```

## Advanced Patterns

### Batch Processing Large Datasets

```javascript
// Process millions of records in batches
Process Large Dataset:
  batch_size = 1000
  offset = 0
  total_processed = 0
  
  WHILE (true) {
    // Get batch
    batch = Query: large_table
      LIMIT batch_size
      OFFSET offset
    
    IF (batch.count == 0) BREAK
    
    // Process batch
    processed_batch = []
    FOR EACH record IN batch {
      processed = {
        ...record,
        processed: true,
        processed_date: NOW()
      }
      ARRAY_PUSH(processed_batch, processed)
    }
    
    // Bulk update
    Bulk Update Records: large_table (processed_batch)
    
    total_processed += batch.count
    offset += batch_size
    
    // Progress tracking
    Log("Processed " + total_processed + " records")
  }
  
  Return { total_processed: total_processed }
```

### Upsert Pattern (Insert or Update)

```javascript
// Bulk upsert implementation
Bulk Upsert:
  items = input.items
  
  // Get existing records
  existing_skus = ARRAY_MAP(items, sku)
  existing = Query: products WHERE sku IN existing_skus
  existing_map = ARRAY_TO_MAP(existing, "sku")
  
  to_insert = []
  to_update = []
  
  FOR EACH item IN items {
    IF (existing_map[item.sku]) {
      // Prepare for update
      update = {
        id: existing_map[item.sku].id,
        ...item
      }
      ARRAY_PUSH(to_update, update)
    } ELSE {
      // Prepare for insert
      ARRAY_PUSH(to_insert, item)
    }
  }
  
  // Perform bulk operations
  inserted = Bulk Add Records: products (to_insert)
  updated = Bulk Update Records: products (to_update)
  
  Return {
    inserted_count: inserted.length,
    updated_count: updated.length
  }
```

## Error Handling

### Transaction Safety

```javascript
// Wrap bulk operations in transaction
Database Transaction {
  TRY {
    // Multiple bulk operations
    Bulk Delete Records: old_inventory
    Bulk Add Records: new_inventory (import_data)
    Bulk Update Records: products (stock_updates)
    
    // All succeed or all fail
    COMMIT
    
  } CATCH (error) {
    // Rollback all changes
    ROLLBACK
    Log_Error("Bulk operation failed: " + error)
    THROW error
  }
}
```

### Validation Before Bulk Operations

```javascript
// Validate before bulk insert
Validate And Import:
  items = input.items
  errors = []
  valid_items = []
  
  // Validate each item
  FOR EACH item IN items {
    validation_errors = []
    
    IF (!item.sku) {
      ARRAY_PUSH(validation_errors, "Missing SKU")
    }
    IF (item.price < 0) {
      ARRAY_PUSH(validation_errors, "Invalid price")
    }
    
    IF (validation_errors.length > 0) {
      ARRAY_PUSH(errors, {
        item: item,
        errors: validation_errors
      })
    } ELSE {
      ARRAY_PUSH(valid_items, item)
    }
  }
  
  // Only import valid items
  IF (valid_items.length > 0) {
    imported = Bulk Add Records: products (valid_items)
  }
  
  Return {
    imported: valid_items.length,
    errors: errors
  }
```

## Integration Patterns

### With n8n

```javascript
// n8n sends batch data for processing
Process n8n Batch:
  webhook_data = input.batch_data
  
  // Transform for Xano
  records = ARRAY_MAP(webhook_data, {
    source: "n8n",
    data: item,
    received_at: NOW()
  })
  
  // Bulk insert
  inserted = Bulk Add Records: webhook_queue (records)
  
  // Process async
  ASYNC: process_webhook_batch(inserted)
  
  Return {
    received: inserted.length,
    status: "processing"
  }
```

### With WeWeb

```javascript
// Bulk operations for WeWeb data tables
Update Table Data:
  table_updates = input.updates  // From WeWeb
  
  // Separate operations by type
  to_add = ARRAY_FILTER(table_updates, operation == "add")
  to_update = ARRAY_FILTER(table_updates, operation == "update")
  to_delete = ARRAY_FILTER(table_updates, operation == "delete")
  
  results = {}
  
  IF (to_add.length > 0) {
    results.added = Bulk Add Records: table_data (to_add)
  }
  
  IF (to_update.length > 0) {
    results.updated = Bulk Update Records: table_data (to_update)
  }
  
  IF (to_delete.length > 0) {
    delete_ids = ARRAY_MAP(to_delete, id)
    results.deleted = Bulk Delete Records: table_data 
      WHERE id IN delete_ids
  }
  
  Return results
```

## Performance Tips

### Optimal Batch Sizes

```javascript
// Different operations have different optimal sizes
Bulk Insert: 100-1000 records per batch
Bulk Update: 500-5000 records per batch
Bulk Delete: 1000-10000 records per batch

// Adjust based on record size
small_records (< 1KB): larger batches
large_records (> 10KB): smaller batches
```

### Index Optimization

```javascript
// Before bulk operations on filtered data
1. Ensure indexes exist on filter columns
2. Run bulk operations
3. Rebuild indexes if necessary

// Example
Create Index: products (category, status)
Bulk Update Records: products WHERE category = "X" AND status = "Y"
```

## Common Mistakes to Avoid

1. **No Validation** - Invalid data crashes bulk operations
2. **Too Large Batches** - Can timeout or run out of memory
3. **No Transaction** - Partial success leaves inconsistent data
4. **Missing Indexes** - Slow filters on large tables
5. **No Progress Tracking** - Can't monitor long operations

## Try This

Build a data import system:
1. Accept CSV file upload
2. Validate all rows
3. Show validation errors
4. Bulk import valid rows
5. Return import summary

## Pro Tips

💡 **Chunk Large Operations:** Process in batches of 1000 for stability

💡 **Use Transactions:** Ensure all-or-nothing for related operations

💡 **Pre-validate:** Check data before bulk operations to avoid failures

💡 **Monitor Performance:** Track execution time for optimization

Remember: Bulk operations are your performance secret weapon. Use them whenever you're processing multiple records!