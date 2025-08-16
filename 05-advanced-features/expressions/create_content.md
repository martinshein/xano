---
title: Create Content - Database Record Management with Metadata API
description: Complete guide to creating, updating, and managing database content using Xano's Metadata API, with comprehensive examples for no-code platforms
category: expressions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - api__master_metadata_api.md
  - search_where_id___10.md
  - get_workspaces.md
subcategory: 05-advanced-features/expressions
tags:
  - metadata-api
  - content-management
  - database-records
  - crud-operations
  - data-manipulation
  - no-code
---

## 📋 **Quick Summary**

The Metadata API provides comprehensive content management capabilities for creating, updating, deleting, and manipulating database records in Xano. This system enables full CRUD operations through RESTful endpoints, making it perfect for building dynamic content management systems with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Creating new database records using the Metadata API
- Updating existing content with flexible field-level modifications
- Implementing secure delete and truncate operations
- Building batch operations for efficient data management
- Content validation and error handling strategies
- Integration patterns for automated content workflows

# Create Content with Metadata API

## Overview

**Content Management** through the Metadata API allows you to programmatically interact with your Xano database records. This RESTful API provides full CRUD (Create, Read, Update, Delete) capabilities with workspace and table-level isolation, ensuring secure and organized data operations.

### API Structure

**Required Parameters:**
- **Workspace ID**: Identifies the target workspace
- **Table ID**: Specifies the database table
- **Content Data**: Field names and values for the operation
- **Authentication**: Bearer token with appropriate permissions

**Optional Parameters:**
- **Content ID**: Required for update and delete operations
- **Validation Rules**: Custom validation for data integrity
- **Relationship Handling**: Automatic relationship management

## 🔨 **Content Creation Operations**

### Basic Content Creation

**API Endpoint**: `POST /api/metadata/content`

**Required Headers:**
```javascript
{
  "Authorization": "Bearer YOUR_API_KEY",
  "Content-Type": "application/json",
  "X-Workspace-ID": "workspace_uuid",
  "X-Table-ID": "table_uuid"
}
```

### n8n Content Management Workflow

```javascript
// n8n workflow for comprehensive content management
{
  "nodes": [
    {
      "name": "Create Content Record",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/metadata/content",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_METADATA_API_KEY }}",
          "Content-Type": "application/json",
          "X-Workspace-ID": "{{ $env.WORKSPACE_ID }}",
          "X-Table-ID": "{{ $env.TABLE_ID }}"
        },
        "body": {
          "data": {
            "name": "{{ $env.PRODUCT_NAME }}",
            "description": "{{ $env.PRODUCT_DESCRIPTION }}",
            "price": "{{ $env.PRODUCT_PRICE }}",
            "category": "{{ $env.PRODUCT_CATEGORY }}",
            "in_stock": true,
            "tags": "{{ $env.PRODUCT_TAGS.split(',') }}",
            "metadata": {
              "created_by": "{{ $env.USER_ID }}",
              "source": "api_import",
              "batch_id": "{{ $env.BATCH_ID }}"
            }
          },
          "options": {
            "validate_schema": true,
            "handle_relationships": true,
            "return_created_record": true
          }
        }
      }
    },
    {
      "name": "Validate Created Content",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const response = $input.first().json;
          
          // Validate the creation response
          const validation = {
            success: response.success || false,
            record_id: response.data?.id || null,
            validation_errors: response.errors || [],
            created_at: response.data?.created_at || null,
            warnings: []
          };
          
          // Perform additional validation checks
          if (validation.success && validation.record_id) {
            // Check required fields
            const requiredFields = ['name', 'price', 'category'];
            const missingFields = requiredFields.filter(field => 
              !response.data[field] || response.data[field] === ''
            );
            
            if (missingFields.length > 0) {
              validation.warnings.push({
                type: 'missing_data',
                message: \`Missing or empty required fields: \${missingFields.join(', ')}\`,
                fields: missingFields
              });
            }
            
            // Validate price format
            if (response.data.price && (isNaN(response.data.price) || response.data.price < 0)) {
              validation.warnings.push({
                type: 'invalid_price',
                message: 'Price should be a positive number',
                current_value: response.data.price
              });
            }
            
            // Check relationships
            if (response.data.category && !response.data.category_details) {
              validation.warnings.push({
                type: 'relationship_missing',
                message: 'Category relationship not properly established',
                category_id: response.data.category
              });
            }
          }
          
          return [{ json: validation }];
        `
      }
    },
    {
      "name": "Handle Creation Errors",
      "type": "IF",
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "{{ $json.success }}",
              "value2": false
            }
          ]
        }
      }
    },
    {
      "name": "Log Creation Error",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.ERROR_LOG_ENDPOINT }}",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.LOG_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "event_type": "content_creation_failed",
          "workspace_id": "{{ $env.WORKSPACE_ID }}",
          "table_id": "{{ $env.TABLE_ID }}",
          "errors": "{{ $json.validation_errors }}",
          "input_data": {
            "name": "{{ $env.PRODUCT_NAME }}",
            "category": "{{ $env.PRODUCT_CATEGORY }}",
            "price": "{{ $env.PRODUCT_PRICE }}"
          },
          "timestamp": "{{ new Date().toISOString() }}",
          "source": "n8n_content_workflow"
        }
      }
    },
    {
      "name": "Update Content Record",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/metadata/content/{{ $('Validate Created Content').first().json.record_id }}",
        "method": "PUT",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_METADATA_API_KEY }}",
          "Content-Type": "application/json",
          "X-Workspace-ID": "{{ $env.WORKSPACE_ID }}",
          "X-Table-ID": "{{ $env.TABLE_ID }}"
        },
        "body": {
          "data": {
            "price": "{{ $env.UPDATED_PRICE }}",
            "last_updated_by": "{{ $env.USER_ID }}",
            "update_reason": "{{ $env.UPDATE_REASON }}"
          },
          "options": {
            "partial_update": true,
            "track_changes": true,
            "validate_schema": true
          }
        }
      }
    },
    {
      "name": "Batch Content Operations",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const batchData = $env.BATCH_CONTENT_DATA ? JSON.parse($env.BATCH_CONTENT_DATA) : [];
          
          // Process batch content creation
          const batchOperations = batchData.map((item, index) => ({
            operation: 'create',
            data: {
              ...item,
              batch_index: index,
              batch_id: $env.BATCH_ID,
              created_at: new Date().toISOString()
            },
            validation: {
              required_fields: ['name'],
              type_checks: {
                price: 'number',
                in_stock: 'boolean'
              }
            }
          }));
          
          // Validate each item in the batch
          const validatedOperations = batchOperations.map(operation => {
            const errors = [];
            
            // Check required fields
            operation.validation.required_fields.forEach(field => {
              if (!operation.data[field]) {
                errors.push(\`Missing required field: \${field}\`);
              }
            });
            
            // Check data types
            Object.entries(operation.validation.type_checks).forEach(([field, expectedType]) => {
              if (operation.data[field] !== undefined) {
                const actualType = typeof operation.data[field];
                if (actualType !== expectedType) {
                  errors.push(\`Field '\${field}' should be \${expectedType}, got \${actualType}\`);
                }
              }
            });
            
            return {
              ...operation,
              validation_errors: errors,
              is_valid: errors.length === 0
            };
          });
          
          const validOperations = validatedOperations.filter(op => op.is_valid);
          const invalidOperations = validatedOperations.filter(op => !op.is_valid);
          
          return [{
            json: {
              total_operations: batchOperations.length,
              valid_operations: validOperations.length,
              invalid_operations: invalidOperations.length,
              valid_data: validOperations.map(op => op.data),
              invalid_data: invalidOperations,
              batch_summary: {
                batch_id: $env.BATCH_ID,
                created_at: new Date().toISOString(),
                success_rate: (validOperations.length / batchOperations.length * 100).toFixed(2)
              }
            }
          }];
        `
      }
    },
    {
      "name": "Execute Batch Creation",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/metadata/content/batch",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_METADATA_API_KEY }}",
          "Content-Type": "application/json",
          "X-Workspace-ID": "{{ $env.WORKSPACE_ID }}",
          "X-Table-ID": "{{ $env.TABLE_ID }}"
        },
        "body": {
          "operations": "{{ $json.valid_data }}",
          "options": {
            "transaction": true,
            "continue_on_error": false,
            "return_created_records": true,
            "batch_size": 100
          }
        }
      }
    }
  ]
}
```

### WeWeb Content Management Component

```javascript
// WeWeb component for comprehensive content management
class XanoContentManager {
  constructor(xanoBaseUrl, apiKey, workspaceId) {
    this.baseUrl = xanoBaseUrl;
    this.apiKey = apiKey;
    this.workspaceId = workspaceId;
    this.defaultOptions = {
      validate_schema: true,
      handle_relationships: true,
      return_created_record: true
    };
  }
  
  async createContent(tableId, data, options = {}) {
    try {
      const requestOptions = { ...this.defaultOptions, ...options };
      
      // Validate required data
      this.validateContentData(data, requestOptions);
      
      const response = await fetch(`${this.baseUrl}/api/metadata/content`, {
        method: 'POST',
        headers: this.getHeaders(tableId),
        body: JSON.stringify({
          data: data,
          options: requestOptions
        })
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('last_created_content', result.data);
        wwLib.wwVariable.updateValue('content_operation_status', 'success');
        wwLib.wwUtils.showSuccessToast('Content created successfully');
        
        // Track analytics
        this.trackContentOperation('create', result.data.id, tableId);
      } else {
        throw new Error(result.error || 'Content creation failed');
      }
      
      return result;
    } catch (error) {
      console.error('Content creation failed:', error);
      wwLib.wwVariable.updateValue('content_operation_status', 'error');
      wwLib.wwUtils.showErrorToast(`Creation failed: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  async updateContent(tableId, contentId, updates, options = {}) {
    try {
      const requestOptions = {
        partial_update: true,
        track_changes: true,
        validate_schema: true,
        ...options
      };
      
      const response = await fetch(`${this.baseUrl}/api/metadata/content/${contentId}`, {
        method: 'PUT',
        headers: this.getHeaders(tableId),
        body: JSON.stringify({
          data: updates,
          options: requestOptions
        })
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('last_updated_content', result.data);
        wwLib.wwVariable.updateValue('content_operation_status', 'success');
        wwLib.wwUtils.showSuccessToast('Content updated successfully');
        
        // Track changes if enabled
        if (requestOptions.track_changes && result.changes) {
          this.logContentChanges(contentId, result.changes);
        }
        
        this.trackContentOperation('update', contentId, tableId);
      } else {
        throw new Error(result.error || 'Content update failed');
      }
      
      return result;
    } catch (error) {
      console.error('Content update failed:', error);
      wwLib.wwVariable.updateValue('content_operation_status', 'error');
      wwLib.wwUtils.showErrorToast(`Update failed: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  async deleteContent(tableId, contentId, options = {}) {
    try {
      const requestOptions = {
        soft_delete: options.soft_delete || false,
        cascade_delete: options.cascade_delete || false,
        ...options
      };
      
      // Confirm deletion if required
      if (options.require_confirmation && !options.confirmed) {
        const confirmed = await this.confirmDeletion(contentId);
        if (!confirmed) {
          return { success: false, error: 'Deletion cancelled by user' };
        }
      }
      
      const response = await fetch(`${this.baseUrl}/api/metadata/content/${contentId}`, {
        method: 'DELETE',
        headers: this.getHeaders(tableId),
        body: JSON.stringify({ options: requestOptions })
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('content_operation_status', 'success');
        wwLib.wwUtils.showSuccessToast('Content deleted successfully');
        
        // Update local data
        this.removeFromLocalCache(contentId);
        this.trackContentOperation('delete', contentId, tableId);
      } else {
        throw new Error(result.error || 'Content deletion failed');
      }
      
      return result;
    } catch (error) {
      console.error('Content deletion failed:', error);
      wwLib.wwVariable.updateValue('content_operation_status', 'error');
      wwLib.wwUtils.showErrorToast(`Deletion failed: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  async truncateTable(tableId, options = {}) {
    try {
      const requestOptions = {
        reset_primary_key: options.reset_primary_key || false,
        confirm_truncate: true,
        ...options
      };
      
      // Double confirmation for truncate operations
      const confirmed = await this.confirmTruncation(tableId);
      if (!confirmed) {
        return { success: false, error: 'Truncation cancelled by user' };
      }
      
      const response = await fetch(`${this.baseUrl}/api/metadata/content/truncate`, {
        method: 'POST',
        headers: this.getHeaders(tableId),
        body: JSON.stringify({ options: requestOptions })
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('content_operation_status', 'success');
        wwLib.wwUtils.showSuccessToast('Table truncated successfully');
        
        // Clear local cache
        this.clearLocalCache(tableId);
        this.trackContentOperation('truncate', null, tableId);
      } else {
        throw new Error(result.error || 'Table truncation failed');
      }
      
      return result;
    } catch (error) {
      console.error('Table truncation failed:', error);
      wwLib.wwVariable.updateValue('content_operation_status', 'error');
      wwLib.wwUtils.showErrorToast(`Truncation failed: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  async batchOperations(tableId, operations, options = {}) {
    try {
      const requestOptions = {
        transaction: true,
        continue_on_error: false,
        return_created_records: true,
        batch_size: 100,
        ...options
      };
      
      // Validate batch operations
      const validatedOperations = this.validateBatchOperations(operations);
      
      if (validatedOperations.invalid_operations.length > 0) {
        wwLib.wwUtils.showWarningToast(
          `${validatedOperations.invalid_operations.length} invalid operations found`
        );
      }
      
      const response = await fetch(`${this.baseUrl}/api/metadata/content/batch`, {
        method: 'POST',
        headers: this.getHeaders(tableId),
        body: JSON.stringify({
          operations: validatedOperations.valid_operations,
          options: requestOptions
        })
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('batch_operation_result', result);
        wwLib.wwVariable.updateValue('content_operation_status', 'success');
        wwLib.wwUtils.showSuccessToast(
          `Batch operation completed: ${result.processed_count} records processed`
        );
        
        this.trackContentOperation('batch', null, tableId, result.processed_count);
      } else {
        throw new Error(result.error || 'Batch operation failed');
      }
      
      return result;
    } catch (error) {
      console.error('Batch operation failed:', error);
      wwLib.wwVariable.updateValue('content_operation_status', 'error');
      wwLib.wwUtils.showErrorToast(`Batch operation failed: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  validateContentData(data, options) {
    if (!data || typeof data !== 'object') {
      throw new Error('Content data must be a valid object');
    }
    
    // Check for required fields if specified in options
    if (options.required_fields) {
      const missingFields = options.required_fields.filter(field => !data[field]);
      if (missingFields.length > 0) {
        throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
      }
    }
    
    // Validate data types if specified
    if (options.field_types) {
      Object.entries(options.field_types).forEach(([field, expectedType]) => {
        if (data[field] !== undefined && typeof data[field] !== expectedType) {
          throw new Error(`Field '${field}' should be ${expectedType}`);
        }
      });
    }
  }
  
  validateBatchOperations(operations) {
    const valid_operations = [];
    const invalid_operations = [];
    
    operations.forEach((operation, index) => {
      try {
        // Validate operation structure
        if (!operation.type || !['create', 'update', 'delete'].includes(operation.type)) {
          throw new Error('Invalid operation type');
        }
        
        if (operation.type !== 'delete' && !operation.data) {
          throw new Error('Operation data is required');
        }
        
        if (['update', 'delete'].includes(operation.type) && !operation.content_id) {
          throw new Error('Content ID is required for update/delete operations');
        }
        
        valid_operations.push(operation);
      } catch (error) {
        invalid_operations.push({
          index: index,
          operation: operation,
          error: error.message
        });
      }
    });
    
    return { valid_operations, invalid_operations };
  }
  
  getHeaders(tableId) {
    return {
      'Authorization': `Bearer ${this.apiKey}`,
      'Content-Type': 'application/json',
      'X-Workspace-ID': this.workspaceId,
      'X-Table-ID': tableId,
      'X-Request-ID': this.generateRequestId()
    };
  }
  
  generateRequestId() {
    return `req_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
  
  async confirmDeletion(contentId) {
    return new Promise((resolve) => {
      wwLib.wwUtils.showConfirmDialog({
        title: 'Confirm Deletion',
        message: `Are you sure you want to delete content ID: ${contentId}?`,
        confirmText: 'Delete',
        cancelText: 'Cancel',
        onConfirm: () => resolve(true),
        onCancel: () => resolve(false)
      });
    });
  }
  
  async confirmTruncation(tableId) {
    return new Promise((resolve) => {
      wwLib.wwUtils.showConfirmDialog({
        title: 'Confirm Table Truncation',
        message: `This will delete ALL content in the table. This action cannot be undone. Are you sure?`,
        confirmText: 'Truncate',
        cancelText: 'Cancel',
        onConfirm: () => resolve(true),
        onCancel: () => resolve(false)
      });
    });
  }
  
  trackContentOperation(operation, contentId, tableId, recordCount = 1) {
    if (typeof gtag !== 'undefined') {
      gtag('event', 'content_operation', {
        operation_type: operation,
        content_id: contentId,
        table_id: tableId,
        record_count: recordCount,
        workspace_id: this.workspaceId
      });
    }
  }
  
  logContentChanges(contentId, changes) {
    const changeLog = {
      content_id: contentId,
      changes: changes,
      timestamp: new Date().toISOString(),
      user_id: wwLib.wwVariable.getValue('current_user_id')
    };
    
    // Store in local storage for audit trail
    const existingLogs = JSON.parse(localStorage.getItem('content_change_logs') || '[]');
    existingLogs.push(changeLog);
    localStorage.setItem('content_change_logs', JSON.stringify(existingLogs));
  }
  
  removeFromLocalCache(contentId) {
    // Update any cached content lists
    const cachedContent = wwLib.wwVariable.getValue('cached_content') || [];
    const updatedContent = cachedContent.filter(item => item.id !== contentId);
    wwLib.wwVariable.updateValue('cached_content', updatedContent);
  }
  
  clearLocalCache(tableId) {
    wwLib.wwVariable.updateValue('cached_content', []);
    wwLib.wwVariable.updateValue('table_content_count', 0);
  }
}

// Initialize content manager
const contentManager = new XanoContentManager(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('metadata_api_key'),
  wwLib.wwVariable.getValue('workspace_id')
);

// Usage functions for WeWeb
async function createNewContent() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const contentData = wwLib.wwVariable.getValue('new_content_data');
  const options = wwLib.wwVariable.getValue('content_options') || {};
  
  await contentManager.createContent(tableId, contentData, options);
}

async function updateExistingContent() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const contentId = wwLib.wwVariable.getValue('content_id_to_update');
  const updates = wwLib.wwVariable.getValue('content_updates');
  const options = wwLib.wwVariable.getValue('update_options') || {};
  
  await contentManager.updateContent(tableId, contentId, updates, options);
}

async function deleteSelectedContent() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const contentId = wwLib.wwVariable.getValue('content_id_to_delete');
  const options = { require_confirmation: true };
  
  await contentManager.deleteContent(tableId, contentId, options);
}

async function executeBatchOperations() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const operations = wwLib.wwVariable.getValue('batch_operations');
  const options = wwLib.wwVariable.getValue('batch_options') || {};
  
  await contentManager.batchOperations(tableId, operations, options);
}

async function truncateTableContent() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const options = { reset_primary_key: wwLib.wwVariable.getValue('reset_primary_key') };
  
  await contentManager.truncateTable(tableId, options);
}
```

## 📊 **Content Operation Examples**

### Create Content Example

**Request Body:**
```json
{
  "data": {
    "name": "Premium Laptop",
    "description": "High-performance laptop for professionals",
    "price": 1299.99,
    "category": "electronics",
    "in_stock": true,
    "tags": ["laptop", "professional", "high-performance"],
    "specifications": {
      "cpu": "Intel i7",
      "ram": "16GB",
      "storage": "512GB SSD"
    }
  },
  "options": {
    "validate_schema": true,
    "handle_relationships": true,
    "return_created_record": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "Premium Laptop",
    "description": "High-performance laptop for professionals",
    "price": 1299.99,
    "category": "electronics",
    "in_stock": true,
    "tags": ["laptop", "professional", "high-performance"],
    "specifications": {
      "cpu": "Intel i7",
      "ram": "16GB",
      "storage": "512GB SSD"
    },
    "created_at": "2025-01-16T10:30:00Z",
    "updated_at": "2025-01-16T10:30:00Z"
  }
}
```

### Update Content Example

**Request Body:**
```json
{
  "data": {
    "price": 1199.99,
    "discount_active": true,
    "discount_percentage": 10
  },
  "options": {
    "partial_update": true,
    "track_changes": true,
    "validate_schema": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "price": 1199.99,
    "discount_active": true,
    "discount_percentage": 10,
    "updated_at": "2025-01-16T11:15:00Z"
  },
  "changes": {
    "price": { "from": 1299.99, "to": 1199.99 },
    "discount_active": { "from": false, "to": true }
  }
}
```

## 💡 **Pro Tips**

- **Validation First**: Always validate data before creation to prevent database inconsistencies
- **Batch Operations**: Use batch operations for multiple records to improve performance
- **Relationship Handling**: Enable automatic relationship management for connected data
- **Change Tracking**: Implement change tracking for audit trails and version control
- **Error Handling**: Provide comprehensive error handling for better user experience
- **Performance**: Use partial updates when modifying existing records

## 🔧 **Troubleshooting**

### Common Content Management Issues

**Problem**: Content creation fails with validation errors  
**Solution**: Check field requirements and data types; ensure all required fields are provided

**Problem**: Update operations not reflecting changes  
**Solution**: Verify content ID is correct and user has appropriate permissions

**Problem**: Batch operations partially failing  
**Solution**: Enable `continue_on_error` option and review individual operation errors

**Problem**: Truncate operation blocked  
**Solution**: Ensure proper permissions and confirm no foreign key constraints prevent truncation

---

**Next Steps**: Ready to manage content effectively? Explore [Search and Browse Content](search_where_id___10.md) for retrieval operations or check [Master Metadata API](api__master_metadata_api.md) for comprehensive API capabilities