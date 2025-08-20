---
category: functions
description: Master data manipulation in Xano with advanced database operations, transformations, validation patterns, and integration workflows
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - database-operations.md
  - data-validation.md
  - transformations.md
  - bulk-operations.md
subcategory: 08-reference/functions
tags:
  - data-processing
  - database
  - transformations
  - validation
  - bulk-operations
  - integration
title: Working With Data
---

# Working With Data

## 📋 **Quick Summary**
Master advanced data manipulation in Xano with comprehensive database operations, transformations, validation, and bulk processing for scalable, efficient data workflows.

## What You'll Learn
- Advanced database query patterns and optimization
- Data transformation and manipulation techniques
- Validation strategies and error handling
- Bulk operations and batch processing
- Integration with external data sources
- Performance optimization for data operations

## Core Data Operations

### CRUD Operations with Advanced Patterns
```javascript
// Enhanced CRUD operations
const advancedCrudPatterns = {
  // Smart upsert (add or update)
  upsert: {
    logic: `
      // Check if record exists
      const existing = await queryDatabase(
        "SELECT id FROM users WHERE email = ?", 
        [inputs.email]
      );
      
      if (existing.length > 0) {
        // Update existing record
        return await updateRecord("users", existing[0].id, {
          name: inputs.name,
          updated_at: new Date()
        });
      } else {
        // Create new record
        return await addRecord("users", {
          email: inputs.email,
          name: inputs.name,
          created_at: new Date()
        });
      }
    `
  },
  
  // Conditional updates
  conditionalUpdate: {
    logic: `
      // Update only if conditions are met
      const result = await queryDatabase(
        "UPDATE products SET price = ? WHERE id = ? AND status = 'active' AND inventory > 0",
        [inputs.new_price, inputs.product_id]
      );
      
      if (result.affectedRows === 0) {
        return error(400, "Product cannot be updated - inactive or out of stock");
      }
      
      return { updated: true, product_id: inputs.product_id };
    `
  },
  
  // Soft delete with audit trail
  softDelete: {
    logic: `
      // Mark as deleted instead of removing
      const deleteResult = await updateRecord("users", inputs.user_id, {
        deleted_at: new Date(),
        deleted_by: auth.user.id,
        status: 'deleted'
      });
      
      // Log deletion for audit
      await addRecord("audit_log", {
        action: "delete",
        table_name: "users",
        record_id: inputs.user_id,
        performed_by: auth.user.id,
        timestamp: new Date()
      });
      
      return deleteResult;
    `
  }
};
```

### Complex Query Patterns
```javascript
// Advanced database queries
const complexQueries = {
  // Hierarchical data retrieval
  getHierarchicalData: {
    query: `
      WITH RECURSIVE category_tree AS (
        -- Base case: root categories
        SELECT id, name, parent_id, 0 as level
        FROM categories 
        WHERE parent_id IS NULL
        
        UNION ALL
        
        -- Recursive case: child categories
        SELECT c.id, c.name, c.parent_id, ct.level + 1
        FROM categories c
        INNER JOIN category_tree ct ON c.parent_id = ct.id
      )
      SELECT * FROM category_tree ORDER BY level, name;
    `
  },
  
  // Window functions for analytics
  analyticsQuery: {
    query: `
      SELECT 
        user_id,
        order_date,
        total_amount,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date DESC) as order_rank,
        SUM(total_amount) OVER (PARTITION BY user_id) as user_total,
        AVG(total_amount) OVER (
          PARTITION BY user_id 
          ORDER BY order_date 
          ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) as rolling_avg
      FROM orders
      WHERE order_date >= DATE_SUB(NOW(), INTERVAL 90 DAY)
      ORDER BY user_id, order_date DESC;
    `
  },
  
  // Dynamic filtering with JSON
  dynamicFilter: {
    query: `
      SELECT * FROM products 
      WHERE 1=1
        AND (? IS NULL OR category_id = ?)
        AND (? IS NULL OR price BETWEEN ? AND ?)
        AND (? IS NULL OR JSON_CONTAINS(tags, JSON_QUOTE(?)))
        AND (? IS NULL OR name LIKE CONCAT('%', ?, '%'))
      ORDER BY 
        CASE WHEN ? = 'price_asc' THEN price END ASC,
        CASE WHEN ? = 'price_desc' THEN price END DESC,
        CASE WHEN ? = 'name' THEN name END ASC
      LIMIT ? OFFSET ?;
    `,
    params: [
      "category_id", "category_id",
      "price_min", "price_min", "price_max", 
      "tag_filter", "tag_filter",
      "search_term", "search_term",
      "sort_by", "sort_by", "sort_by",
      "limit", "offset"
    ]
  }
};
```

## Data Transformation Patterns

### Field Transformations
```javascript
// Data transformation functions
const transformationPatterns = {
  // Normalize user data
  normalizeUserData: {
    logic: `
      function normalizeUserData(userData) {
        return {
          id: userData.id,
          email: userData.email.toLowerCase().trim(),
          name: userData.name.trim().split(' ').map(word => 
            word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
          ).join(' '),
          phone: userData.phone?.replace(/\D/g, ''), // Keep only digits
          created_at: new Date(userData.created_at).toISOString(),
          metadata: {
            source: userData.source || 'direct',
            verified: userData.verified || false,
            preferences: userData.preferences || {}
          }
        };
      }
      
      return normalizeUserData(inputs.user_data);
    `
  },
  
  // Aggregate order data
  aggregateOrderData: {
    logic: `
      function aggregateOrderData(orders) {
        return orders.reduce((acc, order) => {
          const month = new Date(order.created_at).toISOString().slice(0, 7);
          
          if (!acc[month]) {
            acc[month] = {
              total_orders: 0,
              total_revenue: 0,
              avg_order_value: 0,
              unique_customers: new Set()
            };
          }
          
          acc[month].total_orders += 1;
          acc[month].total_revenue += parseFloat(order.total);
          acc[month].unique_customers.add(order.user_id);
          
          return acc;
        }, {});
      }
      
      // Convert Set to count for final result
      const aggregated = aggregateOrderData(order_data);
      Object.keys(aggregated).forEach(month => {
        const data = aggregated[month];
        data.avg_order_value = data.total_revenue / data.total_orders;
        data.unique_customers = data.unique_customers.size;
      });
      
      return aggregated;
    `
  },
  
  // Data format conversion
  formatConversion: {
    logic: `
      function convertDataFormat(data, targetFormat) {
        switch (targetFormat) {
          case 'csv':
            const headers = Object.keys(data[0]).join(',');
            const rows = data.map(row => Object.values(row).join(',')).join('\n');
            return headers + '\n' + rows;
            
          case 'xml':
            return data.map(item => {
              const xmlFields = Object.entries(item)
                .map(([key, value]) => \`<\${key}>\${value}</\${key}>\`)
                .join('');
              return \`<record>\${xmlFields}</record>\`;
            }).join('');
            
          case 'normalized':
            return data.map(item => ({
              ...item,
              normalized_date: new Date(item.date).toISOString(),
              normalized_amount: parseFloat(item.amount).toFixed(2)
            }));
            
          default:
            return data;
        }
      }
      
      return convertDataFormat(source_data, inputs.target_format);
    `
  }
};
```

## Data Validation Framework

### Comprehensive Validation
```javascript
// Advanced validation patterns
const validationFramework = {
  // Multi-level validation
  validateUserInput: {
    logic: `
      function validateUser(userData) {
        const errors = [];
        const warnings = [];
        
        // Required field validation
        if (!userData.email) errors.push('Email is required');
        if (!userData.name) errors.push('Name is required');
        
        // Format validation
        if (userData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userData.email)) {
          errors.push('Invalid email format');
        }
        
        // Business rule validation
        if (userData.age && userData.age < 13) {
          errors.push('User must be at least 13 years old');
        }
        
        // Data quality warnings
        if (userData.phone && userData.phone.length < 10) {
          warnings.push('Phone number appears incomplete');
        }
        
        return {
          isValid: errors.length === 0,
          errors,
          warnings,
          userData: sanitizeUserData(userData)
        };
      }
      
      function sanitizeUserData(data) {
        return {
          email: data.email?.toLowerCase().trim(),
          name: data.name?.trim(),
          phone: data.phone?.replace(/\D/g, ''),
          age: data.age ? parseInt(data.age) : null
        };
      }
      
      return validateUser(inputs.user_data);
    `
  },
  
  // Schema-based validation
  schemaValidation: {
    logic: `
      function validateAgainstSchema(data, schema) {
        const errors = [];
        
        // Check required fields
        schema.required?.forEach(field => {
          if (!data.hasOwnProperty(field) || data[field] === null || data[field] === undefined) {
            errors.push(\`Required field '\${field}' is missing\`);
          }
        });
        
        // Check field types and constraints
        Object.entries(schema.fields || {}).forEach(([field, rules]) => {
          const value = data[field];
          
          if (value !== undefined && value !== null) {
            // Type validation
            if (rules.type && typeof value !== rules.type) {
              errors.push(\`Field '\${field}' must be of type \${rules.type}\`);
            }
            
            // Length validation
            if (rules.minLength && value.length < rules.minLength) {
              errors.push(\`Field '\${field}' must be at least \${rules.minLength} characters\`);
            }
            
            if (rules.maxLength && value.length > rules.maxLength) {
              errors.push(\`Field '\${field}' cannot exceed \${rules.maxLength} characters\`);
            }
            
            // Pattern validation
            if (rules.pattern && !new RegExp(rules.pattern).test(value)) {
              errors.push(\`Field '\${field}' does not match required pattern\`);
            }
            
            // Custom validation
            if (rules.validator && !rules.validator(value)) {
              errors.push(\`Field '\${field}' failed custom validation\`);
            }
          }
        });
        
        return {
          isValid: errors.length === 0,
          errors,
          validatedData: data
        };
      }
      
      return validateAgainstSchema(inputs.data, inputs.schema);
    `
  }
};
```

## Bulk Operations and Batch Processing

### Efficient Batch Processing
```javascript
// Bulk operation patterns
const bulkOperations = {
  // Batch insert with conflict resolution
  batchInsert: {
    logic: `
      async function batchInsertWithConflictResolution(tableName, records, conflictStrategy = 'skip') {
        const batchSize = 100;
        const results = {
          inserted: 0,
          updated: 0,
          skipped: 0,
          errors: []
        };
        
        for (let i = 0; i < records.length; i += batchSize) {
          const batch = records.slice(i, i + batchSize);
          
          try {
            for (const record of batch) {
              const existing = await checkRecordExists(tableName, record);
              
              if (existing) {
                switch (conflictStrategy) {
                  case 'update':
                    await updateRecord(tableName, existing.id, record);
                    results.updated++;
                    break;
                  case 'skip':
                    results.skipped++;
                    break;
                  case 'error':
                    throw new Error(\`Record already exists: \${JSON.stringify(record)}\`);
                }
              } else {
                await addRecord(tableName, record);
                results.inserted++;
              }
            }
          } catch (error) {
            results.errors.push({
              batch: i / batchSize,
              error: error.message
            });
          }
        }
        
        return results;
      }
      
      return await batchInsertWithConflictResolution(
        inputs.table_name, 
        inputs.records, 
        inputs.conflict_strategy
      );
    `
  },
  
  // Bulk update with conditions
  bulkUpdate: {
    logic: `
      async function bulkUpdateWithConditions(updates) {
        const results = [];
        
        for (const update of updates) {
          try {
            // Validate conditions before update
            const conditionsMet = await validateUpdateConditions(update.conditions);
            
            if (!conditionsMet.valid) {
              results.push({
                id: update.id,
                success: false,
                reason: conditionsMet.reason
              });
              continue;
            }
            
            // Perform update
            const updateResult = await updateRecord(
              update.table, 
              update.id, 
              update.data
            );
            
            results.push({
              id: update.id,
              success: true,
              updated_fields: Object.keys(update.data)
            });
            
          } catch (error) {
            results.push({
              id: update.id,
              success: false,
              error: error.message
            });
          }
        }
        
        return {
          total_processed: updates.length,
          successful: results.filter(r => r.success).length,
          failed: results.filter(r => !r.success).length,
          details: results
        };
      }
      
      return await bulkUpdateWithConditions(inputs.updates);
    `
  }
};
```

## Integration Patterns

### n8n Data Processing Workflows
```javascript
// n8n workflow for data processing
{
  "name": "Advanced Data Processing Pipeline",
  "trigger": {
    "type": "webhook",
    "path": "/process-data"
  },
  "nodes": [
    {
      "name": "Validate Input Data",
      "type": "xano-function",
      "function": "validate-bulk-data",
      "data": {
        "records": "{{ $json.data }}",
        "schema": "{{ $json.validation_schema }}"
      }
    },
    {
      "name": "Transform Data",
      "type": "javascript",
      "code": `
        const records = $json.validatedData;
        return records.map(record => ({
          ...record,
          processed_at: new Date().toISOString(),
          hash: require('crypto').createHash('md5').update(JSON.stringify(record)).digest('hex')
        }));
      `
    },
    {
      "name": "Batch Insert",
      "type": "xano-function", 
      "function": "batch-insert",
      "data": {
        "table": "processed_data",
        "records": "{{ $json }}",
        "conflict_strategy": "update"
      }
    },
    {
      "name": "Generate Report",
      "type": "xano-function",
      "function": "generate-processing-report",
      "data": {
        "results": "{{ $json }}",
        "timestamp": "{{ new Date().toISOString() }}"
      }
    }
  ]
}
```

### WeWeb Data Management
```javascript
// WeWeb data management patterns
const wewebDataManagement = {
  // Real-time data synchronization
  syncData: {
    methods: {
      async syncLocalData() {
        const localChanges = this.getLocalChanges();
        
        if (localChanges.length > 0) {
          const syncResult = await wwLib.executeWorkflow('sync-data', {
            changes: localChanges,
            last_sync: this.lastSyncTimestamp
          });
          
          if (syncResult.success) {
            this.applyRemoteChanges(syncResult.remote_changes);
            this.clearLocalChanges();
            this.lastSyncTimestamp = syncResult.sync_timestamp;
          }
        }
      },
      
      applyRemoteChanges(changes) {
        changes.forEach(change => {
          switch (change.operation) {
            case 'insert':
              this.addToCollection(change.table, change.data);
              break;
            case 'update':
              this.updateInCollection(change.table, change.id, change.data);
              break;
            case 'delete':
              this.removeFromCollection(change.table, change.id);
              break;
          }
        });
      }
    }
  },
  
  // Data validation in WeWeb
  validation: {
    validateForm(formData, schema) {
      const errors = {};
      
      Object.entries(schema).forEach(([field, rules]) => {
        const value = formData[field];
        
        if (rules.required && !value) {
          errors[field] = `${field} is required`;
        }
        
        if (value && rules.pattern && !new RegExp(rules.pattern).test(value)) {
          errors[field] = `${field} format is invalid`;
        }
      });
      
      return {
        isValid: Object.keys(errors).length === 0,
        errors
      };
    }
  }
};
```

## Performance Optimization

### Query Optimization
```javascript
// Database performance patterns
const performanceOptimization = {
  // Efficient pagination
  efficientPagination: `
    -- Cursor-based pagination (more efficient for large datasets)
    SELECT * FROM products 
    WHERE id > ? 
    ORDER BY id ASC 
    LIMIT 20;
    
    -- Instead of OFFSET-based pagination
    -- SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 10000; -- Slow for large offsets
  `,
  
  // Optimized search
  optimizedSearch: `
    -- Use full-text search for text fields
    SELECT *, MATCH(name, description) AGAINST(? IN NATURAL LANGUAGE MODE) as relevance
    FROM products 
    WHERE MATCH(name, description) AGAINST(? IN NATURAL LANGUAGE MODE)
       OR name LIKE CONCAT('%', ?, '%')
    ORDER BY relevance DESC, name ASC;
  `,
  
  // Efficient aggregations
  efficientAggregations: `
    -- Use covering indexes and materialized views for complex aggregations
    SELECT 
      DATE(order_date) as date,
      COUNT(*) as order_count,
      SUM(total_amount) as revenue
    FROM orders_summary -- Materialized view updated via triggers
    WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
    GROUP BY DATE(order_date)
    ORDER BY date DESC;
  `
};
```

## Try This: Build Advanced Data Pipeline

1. **Design Data Schema**
   - Plan relationships and constraints
   - Add indexes for query performance
   - Include audit fields

2. **Implement Validation**
   - Create comprehensive validation rules
   - Add business logic constraints
   - Test error scenarios

3. **Build Processing Functions**
   - Create batch operation handlers
   - Implement transformation logic
   - Add monitoring and logging

4. **Integrate with Frontend**
   - Connect to WeWeb/n8n
   - Implement real-time sync
   - Add user feedback mechanisms

## Common Mistakes to Avoid

- **Missing validation** - Always validate data before processing
- **Inefficient queries** - Use proper indexes and query optimization
- **Poor error handling** - Implement comprehensive error management
- **Ignoring performance** - Test with realistic data volumes
- **Insufficient logging** - Log all data operations for debugging

## Pro Tips

💡 **Use database transactions** - Ensure data consistency in batch operations

💡 **Implement retry logic** - Handle temporary failures gracefully

💡 **Cache frequently accessed data** - Reduce database load with smart caching

💡 **Monitor query performance** - Regular analysis of slow queries

💡 **Plan for scale** - Design data operations for growth from the start