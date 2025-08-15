---
title: "Get Database Schema - Inspect Database Structure"
description: "Learn to dynamically inspect database schemas in Xano. Master table discovery, field analysis, relationship mapping, and metadata extraction for flexible database operations"
category: data-operations
tags:
  - Database Schema
  - Database Operations
  - Metadata
  - Table Structure
  - Dynamic Queries
  - Database Inspection
difficulty: advanced
reading_time: 14 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of database concepts
  - Familiarity with SQL and database structures
  - Knowledge of Xano database operations
---

# Get Database Schema - Inspect Database Structure

## 📋 **Quick Summary**

**What it does:** Get Database Schema retrieves structural information about your database tables, fields, relationships, and constraints, enabling dynamic query generation and database introspection.

**Why it matters:** Schema inspection enables you to:
- **Build dynamic forms** that adapt to table structures
- **Create flexible APIs** that work with any table
- **Generate documentation** automatically from database structure
- **Validate data** against actual field types and constraints
- **Build admin interfaces** that work with any table structure

**Time to implement:** 20-30 minutes for basic schema inspection, 45-60 minutes for dynamic query systems

---

## What You'll Learn

- How to retrieve and analyze database schema information
- Building dynamic query systems based on schema
- Creating flexible data validation from schema metadata
- Integration patterns with no-code platforms
- Best practices for schema-driven applications

## Understanding Database Schema

### What Schema Information Includes

```javascript
// Example schema response structure
const schemaResponse = {
  tables: [
    {
      name: 'users',
      fields: [
        {
          name: 'id',
          type: 'integer',
          primary_key: true,
          auto_increment: true,
          nullable: false
        },
        {
          name: 'email',
          type: 'text',
          unique: true,
          nullable: false,
          max_length: 255
        },
        {
          name: 'created_at',
          type: 'timestamp',
          nullable: true,
          default_value: 'CURRENT_TIMESTAMP'
        }
      ],
      relationships: [
        {
          type: 'has_many',
          related_table: 'orders',
          foreign_key: 'user_id'
        }
      ]
    }
  ]
};
```

### Basic Schema Retrieval

```javascript
// Get schema for all tables
function getAllTableSchemas() {
  try {
    const schema = getDatabaseSchema();
    
    return {
      success: true,
      schema: schema,
      table_count: schema.tables ? schema.tables.length : 0,
      retrieved_at: new Date().toISOString()
    };
    
  } catch (error) {
    return {
      success: false,
      error: `Failed to retrieve schema: ${error.message}`
    };
  }
}

// Get schema for specific table
function getTableSchema(tableName) {
  try {
    const fullSchema = getDatabaseSchema();
    const tableSchema = fullSchema.tables.find(table => table.name === tableName);
    
    if (!tableSchema) {
      throw new Error(`Table '${tableName}' not found`);
    }
    
    return {
      success: true,
      table: tableSchema,
      field_count: tableSchema.fields.length,
      has_relationships: tableSchema.relationships && tableSchema.relationships.length > 0
    };
    
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
}
```

## Dynamic Query Generation

### Schema-Based Query Builder

```javascript
// Dynamic query builder using schema information
class SchemaQueryBuilder {
  constructor() {
    this.schema = getDatabaseSchema();
    this.tableSchemas = new Map();
    
    // Index schemas by table name for quick lookup
    if (this.schema.tables) {
      this.schema.tables.forEach(table => {
        this.tableSchemas.set(table.name, table);
      });
    }
  }
  
  // Get valid fields for a table
  getTableFields(tableName) {
    const tableSchema = this.tableSchemas.get(tableName);
    if (!tableSchema) {
      throw new Error(`Table '${tableName}' not found in schema`);
    }
    
    return tableSchema.fields.map(field => ({
      name: field.name,
      type: field.type,
      required: !field.nullable,
      primary_key: field.primary_key || false,
      auto_increment: field.auto_increment || false
    }));
  }
  
  // Validate data against schema
  validateData(tableName, data) {
    const fields = this.getTableFields(tableName);
    const errors = [];
    
    // Check required fields
    const requiredFields = fields.filter(f => f.required && !f.auto_increment);
    for (const field of requiredFields) {
      if (!data.hasOwnProperty(field.name) || data[field.name] === null || data[field.name] === undefined) {
        errors.push(`Field '${field.name}' is required`);
      }
    }
    
    // Validate data types
    for (const [fieldName, value] of Object.entries(data)) {
      const field = fields.find(f => f.name === fieldName);
      if (!field) {
        errors.push(`Field '${fieldName}' does not exist in table '${tableName}'`);
        continue;
      }
      
      if (value !== null && value !== undefined) {
        const typeError = this.validateFieldType(field, value);
        if (typeError) {
          errors.push(`Field '${fieldName}': ${typeError}`);
        }
      }
    }
    
    return {
      valid: errors.length === 0,
      errors: errors
    };
  }
  
  validateFieldType(field, value) {
    switch (field.type) {
      case 'integer':
        if (!Number.isInteger(Number(value))) {
          return 'must be an integer';
        }
        break;
        
      case 'decimal':
      case 'float':
        if (isNaN(Number(value))) {
          return 'must be a number';
        }
        break;
        
      case 'boolean':
        if (typeof value !== 'boolean' && value !== 0 && value !== 1) {
          return 'must be a boolean value';
        }
        break;
        
      case 'text':
      case 'string':
        if (typeof value !== 'string') {
          return 'must be a string';
        }
        if (field.max_length && value.length > field.max_length) {
          return `must be no longer than ${field.max_length} characters`;
        }
        break;
        
      case 'timestamp':
      case 'datetime':
        const date = new Date(value);
        if (isNaN(date.getTime())) {
          return 'must be a valid date/time';
        }
        break;
    }
    
    return null;
  }
  
  // Generate dynamic SELECT query
  buildSelectQuery(tableName, options = {}) {
    const fields = this.getTableFields(tableName);
    const { 
      select = ['*'], 
      where = {}, 
      orderBy = [], 
      limit = null,
      offset = null 
    } = options;
    
    // Validate selected fields
    if (select[0] !== '*') {
      const validFields = fields.map(f => f.name);
      const invalidFields = select.filter(field => !validFields.includes(field));
      if (invalidFields.length > 0) {
        throw new Error(`Invalid fields: ${invalidFields.join(', ')}`);
      }
    }
    
    // Build query object
    const query = {
      table: tableName,
      fields: select,
      filters: where
    };
    
    if (orderBy.length > 0) {
      query.sort = orderBy;
    }
    
    if (limit) {
      query.limit = limit;
    }
    
    if (offset) {
      query.offset = offset;
    }
    
    return query;
  }
  
  // Generate form configuration from schema
  generateFormConfig(tableName, options = {}) {
    const fields = this.getTableFields(tableName);
    const { exclude = [], include = null, readOnly = [] } = options;
    
    let formFields = fields.filter(field => {
      // Skip auto-increment primary keys
      if (field.auto_increment) return false;
      
      // Skip excluded fields
      if (exclude.includes(field.name)) return false;
      
      // If include list specified, only include those
      if (include && !include.includes(field.name)) return false;
      
      return true;
    });
    
    return formFields.map(field => {
      const formField = {
        name: field.name,
        label: this.generateFieldLabel(field.name),
        type: this.mapFieldTypeToFormType(field.type),
        required: field.required,
        readOnly: readOnly.includes(field.name)
      };
      
      // Add type-specific properties
      if (field.type === 'text' && field.max_length) {
        formField.maxLength = field.max_length;
      }
      
      return formField;
    });
  }
  
  generateFieldLabel(fieldName) {
    return fieldName
      .split('_')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  }
  
  mapFieldTypeToFormType(dbType) {
    const typeMap = {
      'text': 'text',
      'string': 'text',
      'integer': 'number',
      'decimal': 'number',
      'float': 'number',
      'boolean': 'checkbox',
      'timestamp': 'datetime-local',
      'date': 'date',
      'time': 'time'
    };
    
    return typeMap[dbType] || 'text';
  }
}
```

## Advanced Schema Applications

### Dynamic API Generator

```javascript
// Generate CRUD endpoints for any table based on schema
function generateTableAPI(tableName) {
  const queryBuilder = new SchemaQueryBuilder();
  const fields = queryBuilder.getTableFields(tableName);
  
  return {
    // GET /api/{table}
    list: function(filters = {}, pagination = {}) {
      try {
        const query = queryBuilder.buildSelectQuery(tableName, {
          where: filters,
          limit: pagination.limit || 20,
          offset: pagination.offset || 0,
          orderBy: pagination.orderBy || []
        });
        
        const records = queryAllRecords(query);
        
        return {
          success: true,
          data: records,
          meta: {
            table: tableName,
            count: records.length,
            fields: fields.map(f => f.name)
          }
        };
        
      } catch (error) {
        return {
          success: false,
          error: error.message
        };
      }
    },
    
    // GET /api/{table}/{id}
    get: function(id) {
      try {
        const record = getRecord({
          table: tableName,
          id: id
        });
        
        if (!record) {
          return {
            success: false,
            error: 'Record not found'
          };
        }
        
        return {
          success: true,
          data: record,
          meta: {
            table: tableName,
            fields: fields.map(f => f.name)
          }
        };
        
      } catch (error) {
        return {
          success: false,
          error: error.message
        };
      }
    },
    
    // POST /api/{table}
    create: function(data) {
      try {
        // Validate data against schema
        const validation = queryBuilder.validateData(tableName, data);
        if (!validation.valid) {
          return {
            success: false,
            error: 'Validation failed',
            details: validation.errors
          };
        }
        
        // Filter out read-only fields
        const writableFields = fields.filter(f => !f.auto_increment && !f.primary_key);
        const filteredData = {};
        
        writableFields.forEach(field => {
          if (data.hasOwnProperty(field.name)) {
            filteredData[field.name] = data[field.name];
          }
        });
        
        const newRecord = addRecord({
          table: tableName,
          data: filteredData
        });
        
        return {
          success: true,
          data: newRecord,
          message: `${tableName} record created successfully`
        };
        
      } catch (error) {
        return {
          success: false,
          error: error.message
        };
      }
    },
    
    // PATCH /api/{table}/{id}
    update: function(id, data) {
      try {
        // Check if record exists
        const existingRecord = getRecord({
          table: tableName,
          id: id
        });
        
        if (!existingRecord) {
          return {
            success: false,
            error: 'Record not found'
          };
        }
        
        // Validate only provided fields
        const partialValidation = queryBuilder.validateData(tableName, data);
        if (!partialValidation.valid) {
          return {
            success: false,
            error: 'Validation failed',
            details: partialValidation.errors
          };
        }
        
        // Filter out read-only fields
        const updateableFields = fields.filter(f => !f.auto_increment && !f.primary_key);
        const filteredData = {};
        
        updateableFields.forEach(field => {
          if (data.hasOwnProperty(field.name)) {
            filteredData[field.name] = data[field.name];
          }
        });
        
        const updatedRecord = patchRecord({
          table: tableName,
          id: id,
          data: filteredData
        });
        
        return {
          success: true,
          data: updatedRecord,
          message: `${tableName} record updated successfully`
        };
        
      } catch (error) {
        return {
          success: false,
          error: error.message
        };
      }
    },
    
    // DELETE /api/{table}/{id}
    delete: function(id) {
      try {
        const deletedRecord = deleteRecord({
          table: tableName,
          id: id
        });
        
        return {
          success: true,
          data: deletedRecord,
          message: `${tableName} record deleted successfully`
        };
        
      } catch (error) {
        return {
          success: false,
          error: error.message
        };
      }
    },
    
    // GET /api/{table}/schema
    schema: function() {
      return {
        success: true,
        data: {
          table: tableName,
          fields: fields,
          form_config: queryBuilder.generateFormConfig(tableName)
        }
      };
    }
  };
}
```

### Schema-Driven Validation

```javascript
// Advanced validation using schema constraints
class SchemaValidator {
  constructor() {
    this.queryBuilder = new SchemaQueryBuilder();
  }
  
  validateRecord(tableName, data, operation = 'create') {
    const results = {
      valid: true,
      errors: [],
      warnings: [],
      sanitized_data: { ...data }
    };
    
    const fields = this.queryBuilder.getTableFields(tableName);
    
    // Validate each field
    for (const field of fields) {
      const value = data[field.name];
      const fieldResult = this.validateField(field, value, operation);
      
      if (!fieldResult.valid) {
        results.valid = false;
        results.errors.push(...fieldResult.errors);
      }
      
      if (fieldResult.warnings.length > 0) {
        results.warnings.push(...fieldResult.warnings);
      }
      
      if (fieldResult.sanitized_value !== undefined) {
        results.sanitized_data[field.name] = fieldResult.sanitized_value;
      }
    }
    
    // Check for unknown fields
    const validFieldNames = fields.map(f => f.name);
    const unknownFields = Object.keys(data).filter(key => !validFieldNames.includes(key));
    
    if (unknownFields.length > 0) {
      results.warnings.push(`Unknown fields will be ignored: ${unknownFields.join(', ')}`);
      unknownFields.forEach(field => {
        delete results.sanitized_data[field];
      });
    }
    
    return results;
  }
  
  validateField(field, value, operation) {
    const result = {
      valid: true,
      errors: [],
      warnings: [],
      sanitized_value: value
    };
    
    // Skip auto-increment fields
    if (field.auto_increment) {
      if (value !== undefined && operation === 'create') {
        result.warnings.push(`Auto-increment field '${field.name}' will be ignored`);
        result.sanitized_value = undefined;
      }
      return result;
    }
    
    // Check required fields
    if (field.required && (value === null || value === undefined || value === '')) {
      if (operation === 'create') {
        result.valid = false;
        result.errors.push(`Field '${field.name}' is required`);
      }
      return result;
    }
    
    // Skip null/undefined values for updates
    if (value === null || value === undefined) {
      return result;
    }
    
    // Type validation and sanitization
    switch (field.type) {
      case 'text':
      case 'string':
        result.sanitized_value = String(value).trim();
        
        if (field.max_length && result.sanitized_value.length > field.max_length) {
          result.valid = false;
          result.errors.push(`Field '${field.name}' exceeds maximum length of ${field.max_length}`);
        }
        
        if (result.sanitized_value.length === 0 && field.required) {
          result.valid = false;
          result.errors.push(`Field '${field.name}' cannot be empty`);
        }
        break;
        
      case 'integer':
        const intValue = parseInt(value);
        if (isNaN(intValue)) {
          result.valid = false;
          result.errors.push(`Field '${field.name}' must be an integer`);
        } else {
          result.sanitized_value = intValue;
        }
        break;
        
      case 'decimal':
      case 'float':
        const floatValue = parseFloat(value);
        if (isNaN(floatValue)) {
          result.valid = false;
          result.errors.push(`Field '${field.name}' must be a number`);
        } else {
          result.sanitized_value = floatValue;
        }
        break;
        
      case 'boolean':
        if (typeof value === 'string') {
          const lowerValue = value.toLowerCase();
          if (['true', '1', 'yes', 'on'].includes(lowerValue)) {
            result.sanitized_value = true;
          } else if (['false', '0', 'no', 'off'].includes(lowerValue)) {
            result.sanitized_value = false;
          } else {
            result.valid = false;
            result.errors.push(`Field '${field.name}' must be a boolean value`);
          }
        } else if (typeof value === 'number') {
          result.sanitized_value = Boolean(value);
        } else if (typeof value !== 'boolean') {
          result.valid = false;
          result.errors.push(`Field '${field.name}' must be a boolean value`);
        }
        break;
        
      case 'timestamp':
      case 'datetime':
        const date = new Date(value);
        if (isNaN(date.getTime())) {
          result.valid = false;
          result.errors.push(`Field '${field.name}' must be a valid date/time`);
        } else {
          result.sanitized_value = date.toISOString();
        }
        break;
    }
    
    return result;
  }
  
  // Validate relationships
  validateRelationships(tableName, data) {
    const schema = this.queryBuilder.schema;
    const table = schema.tables.find(t => t.name === tableName);
    
    if (!table || !table.relationships) {
      return { valid: true, errors: [] };
    }
    
    const errors = [];
    
    for (const relationship of table.relationships) {
      if (relationship.type === 'belongs_to' && data[relationship.foreign_key]) {
        // Check if referenced record exists
        try {
          const referencedRecord = getRecord({
            table: relationship.related_table,
            id: data[relationship.foreign_key]
          });
          
          if (!referencedRecord) {
            errors.push(`Referenced ${relationship.related_table} with ID ${data[relationship.foreign_key]} does not exist`);
          }
        } catch (error) {
          errors.push(`Error validating relationship to ${relationship.related_table}: ${error.message}`);
        }
      }
    }
    
    return {
      valid: errors.length === 0,
      errors: errors
    };
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Integration**

```javascript
// n8n workflow for dynamic table operations
function processDynamicTableOperation($input) {
  const { operation, table, data, config } = $input.body;
  
  try {
    const queryBuilder = new SchemaQueryBuilder();
    const validator = new SchemaValidator();
    
    switch (operation) {
      case 'get_schema':
        return {
          success: true,
          schema: queryBuilder.getTableFields(table),
          form_config: queryBuilder.generateFormConfig(table, config)
        };
        
      case 'validate_data':
        const validation = validator.validateRecord(table, data);
        return {
          success: validation.valid,
          validation: validation,
          sanitized_data: validation.sanitized_data
        };
        
      case 'create_record':
        const createValidation = validator.validateRecord(table, data, 'create');
        if (!createValidation.valid) {
          return {
            success: false,
            error: 'Validation failed',
            details: createValidation.errors
          };
        }
        
        const newRecord = addRecord({
          table: table,
          data: createValidation.sanitized_data
        });
        
        return {
          success: true,
          record: newRecord,
          operation: 'created'
        };
        
      case 'generate_api':
        const api = generateTableAPI(table);
        return {
          success: true,
          api_endpoints: {
            list: `GET /api/${table}`,
            get: `GET /api/${table}/{id}`,
            create: `POST /api/${table}`,
            update: `PATCH /api/${table}/{id}`,
            delete: `DELETE /api/${table}/{id}`,
            schema: `GET /api/${table}/schema`
          },
          sample_requests: {
            create: createValidation.sanitized_data,
            update: Object.fromEntries(
              Object.entries(createValidation.sanitized_data).slice(0, 3)
            )
          }
        };
        
      default:
        return {
          success: false,
          error: `Unknown operation: ${operation}`
        };
    }
    
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
// WeWeb dynamic form generator
class DynamicFormGenerator {
  static async generateForm(tableName, options = {}) {
    try {
      wwLib.showLoading();
      
      // Get schema from Xano
      const response = await wwLib.api.get({
        url: `${wwLib.envVars.XANO_API_URL}/schema/${tableName}`,
        headers: {
          'Authorization': `Bearer ${wwLib.auth.getToken()}`
        }
      });
      
      if (!response.data.success) {
        throw new Error(response.data.error);
      }
      
      const formConfig = response.data.data.form_config;
      
      // Generate form elements
      const formElements = formConfig.map(field => {
        return this.createFormElement(field, options);
      });
      
      // Create form container
      const formContainer = wwLib.createElement('form', {
        className: 'dynamic-form',
        onSubmit: (event) => this.handleFormSubmit(event, tableName)
      });
      
      // Add form elements
      formElements.forEach(element => {
        formContainer.appendChild(element);
      });
      
      // Add submit button
      const submitButton = wwLib.createElement('button', {
        type: 'submit',
        textContent: options.submitText || 'Submit',
        className: 'submit-button'
      });
      
      formContainer.appendChild(submitButton);
      
      return formContainer;
      
    } catch (error) {
      console.error('Error generating form:', error);
      wwLib.showAlert('Failed to generate form', 'error');
      return null;
    } finally {
      wwLib.hideLoading();
    }
  }
  
  static createFormElement(field, options) {
    const wrapper = wwLib.createElement('div', {
      className: 'form-field'
    });
    
    // Create label
    const label = wwLib.createElement('label', {
      textContent: field.label,
      htmlFor: field.name,
      className: field.required ? 'required' : ''
    });
    
    // Create input element based on field type
    let input;
    
    switch (field.type) {
      case 'checkbox':
        input = wwLib.createElement('input', {
          type: 'checkbox',
          id: field.name,
          name: field.name,
          required: field.required
        });
        break;
        
      case 'number':
        input = wwLib.createElement('input', {
          type: 'number',
          id: field.name,
          name: field.name,
          required: field.required,
          step: field.type === 'decimal' ? '0.01' : '1'
        });
        break;
        
      case 'datetime-local':
      case 'date':
      case 'time':
        input = wwLib.createElement('input', {
          type: field.type,
          id: field.name,
          name: field.name,
          required: field.required
        });
        break;
        
      default:
        input = wwLib.createElement('input', {
          type: 'text',
          id: field.name,
          name: field.name,
          required: field.required,
          maxLength: field.maxLength
        });
    }
    
    if (field.readOnly) {
      input.readOnly = true;
      input.className += ' readonly';
    }
    
    wrapper.appendChild(label);
    wrapper.appendChild(input);
    
    return wrapper;
  }
  
  static async handleFormSubmit(event, tableName) {
    event.preventDefault();
    
    try {
      wwLib.showLoading();
      
      const formData = new FormData(event.target);
      const data = Object.fromEntries(formData.entries());
      
      // Convert checkbox values
      for (const [key, value] of Object.entries(data)) {
        const input = event.target.querySelector(`[name="${key}"]`);
        if (input && input.type === 'checkbox') {
          data[key] = input.checked;
        }
      }
      
      // Submit to Xano
      const response = await wwLib.api.post({
        url: `${wwLib.envVars.XANO_API_URL}/dynamic/${tableName}`,
        data: data
      });
      
      if (response.data.success) {
        wwLib.showAlert('Record created successfully', 'success');
        event.target.reset();
        
        // Trigger custom event
        wwLib.triggerEvent('recordCreated', {
          table: tableName,
          record: response.data.record
        });
      } else {
        wwLib.showAlert(response.data.error, 'error');
      }
      
    } catch (error) {
      console.error('Form submission error:', error);
      wwLib.showAlert('Failed to submit form', 'error');
    } finally {
      wwLib.hideLoading();
    }
  }
}
```

### 🔧 **Make.com Integration**

```javascript
// Make.com scenario for schema-based operations
function processSchemaBasedOperation(inputData) {
  const { operation, tables, config } = inputData;
  
  try {
    const queryBuilder = new SchemaQueryBuilder();
    
    switch (operation) {
      case 'generate_documentation':
        return generateDatabaseDocumentation(tables);
        
      case 'validate_data_integrity':
        return validateDataIntegrity(tables);
        
      case 'create_backup_schema':
        return createBackupSchema(tables);
        
      case 'sync_schema_changes':
        return syncSchemaChanges(config);
        
      default:
        throw new Error(`Unknown operation: ${operation}`);
    }
    
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
}

function generateDatabaseDocumentation(tables) {
  const queryBuilder = new SchemaQueryBuilder();
  const documentation = {
    generated_at: new Date().toISOString(),
    database_schema: {},
    table_count: 0,
    total_fields: 0
  };
  
  const tablesToDocument = tables || Array.from(queryBuilder.tableSchemas.keys());
  
  for (const tableName of tablesToDocument) {
    try {
      const fields = queryBuilder.getTableFields(tableName);
      const formConfig = queryBuilder.generateFormConfig(tableName);
      
      documentation.database_schema[tableName] = {
        fields: fields,
        form_configuration: formConfig,
        field_count: fields.length,
        required_fields: fields.filter(f => f.required).length,
        primary_keys: fields.filter(f => f.primary_key).map(f => f.name)
      };
      
      documentation.table_count++;
      documentation.total_fields += fields.length;
      
    } catch (error) {
      console.error(`Error documenting table ${tableName}:`, error);
    }
  }
  
  return {
    success: true,
    documentation: documentation
  };
}

function validateDataIntegrity(tables) {
  const queryBuilder = new SchemaQueryBuilder();
  const validator = new SchemaValidator();
  const results = {
    validation_date: new Date().toISOString(),
    tables_checked: 0,
    total_records: 0,
    validation_errors: [],
    warnings: []
  };
  
  const tablesToCheck = tables || Array.from(queryBuilder.tableSchemas.keys());
  
  for (const tableName of tablesToCheck) {
    try {
      const records = queryAllRecords({ table: tableName });
      results.tables_checked++;
      results.total_records += records.length;
      
      for (const record of records) {
        const validation = validator.validateRecord(tableName, record, 'update');
        
        if (!validation.valid) {
          results.validation_errors.push({
            table: tableName,
            record_id: record.id,
            errors: validation.errors
          });
        }
        
        if (validation.warnings.length > 0) {
          results.warnings.push({
            table: tableName,
            record_id: record.id,
            warnings: validation.warnings
          });
        }
      }
      
    } catch (error) {
      results.validation_errors.push({
        table: tableName,
        error: `Failed to validate table: ${error.message}`
      });
    }
  }
  
  return {
    success: true,
    integrity_check: results,
    is_valid: results.validation_errors.length === 0
  };
}
```

## 💡 **Try This**

### Beginner Challenge
Build a schema inspector:
1. Create a function to retrieve schema for a specific table
2. Display field names, types, and constraints
3. Show table relationships if they exist
4. Add error handling for non-existent tables

### Intermediate Challenge
Create a dynamic form generator:
1. Use schema information to generate HTML forms
2. Map database field types to appropriate input types
3. Add client-side validation based on schema constraints
4. Handle required fields and field lengths

### Advanced Challenge
Build a schema-driven API generator:
1. Create CRUD endpoints for any table using schema
2. Implement automatic data validation
3. Add relationship handling and joins
4. Include comprehensive error responses

## Common Mistakes to Avoid

1. **Hardcoding table structures** - Always use schema inspection for flexibility
2. **Ignoring field constraints** - Validate against actual database constraints
3. **Missing error handling** - Schema operations can fail
4. **Not caching schema data** - Avoid repeated schema calls
5. **Forgetting relationships** - Consider foreign key constraints
6. **Skipping data sanitization** - Clean data based on field types

## Best Practices

1. **Cache schema information** - Avoid repeated database calls
2. **Validate dynamically** - Use schema constraints for validation
3. **Handle errors gracefully** - Provide meaningful error messages
4. **Consider performance** - Schema calls can be expensive
5. **Document auto-generated APIs** - Make dynamic endpoints discoverable
6. **Test with real data** - Validate schema assumptions with actual records
7. **Version your schemas** - Track changes over time

## Next Steps

- Learn [Direct Database Query](finding_your_database_identifier.md) for advanced operations
- Master [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for complex workflows
- Explore [Dynamic Queries](query_all_records.md) with schema information
- Understand [API Design](../best-practices/api-design.md) patterns

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Schema operation discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Database schema guides
- 📖 [Dynamic API Examples](../examples/dynamic-apis.md) - Schema-driven patterns
- 🔧 [Support](https://xano.com/support) - Database schema assistance

