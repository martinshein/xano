---
title: "Get Database Schema Function"
description: "Learn how to retrieve database table schemas programmatically using Xano's Get Database Schema function for dynamic API responses"
category: function-stack
difficulty: intermediate
tags:
  - database
  - schema
  - functions
  - api
  - metadata
  - dynamic-forms
related_docs:
  - database-requests
  - get-record
  - query-all-records
  - external-database-query
last_updated: '2025-01-23'
---

# Get Database Schema Function

## Quick Summary
The Get Database Schema function retrieves complete table structure information in JSON format, including field types, relationships, and validation rules. This is essential for building dynamic forms, API documentation, and schema-aware applications.

## What You'll Learn
- How to retrieve database table schemas programmatically
- Using schema data to build dynamic forms and interfaces
- Filtering schema results to specific fields
- Real-world applications for schema introspection
- Integration patterns with n8n and WeWeb

## What This Function Does

The Get Database Schema function returns detailed information about your database table structure, including:
- Field names and data types
- Required field indicators
- Relationship definitions
- Validation rules
- Default values
- Enum options for select fields

## Basic Usage

### Retrieve Complete Table Schema
```json
{
  "table": "users",
  "path": null  // Returns all fields
}
```

**Response Example:**
```json
{
  "schema": {
    "id": {
      "type": "integer",
      "required": true,
      "auto_increment": true,
      "primary_key": true
    },
    "email": {
      "type": "string",
      "required": true,
      "unique": true,
      "max_length": 255
    },
    "role": {
      "type": "enum",
      "required": true,
      "options": ["admin", "user", "moderator"],
      "default": "user"
    },
    "created_at": {
      "type": "timestamp",
      "required": true,
      "auto_populate": true
    }
  }
}
```

### Get Specific Field Schema
```json
{
  "table": "users",
  "path": "role"  // Returns only the 'role' field schema
}
```

## Integration with n8n

### Dynamic Form Generation
Use schema data to create dynamic forms in your n8n workflows:

```javascript
// n8n Function Node - Generate form fields from schema
const schema = $json.schema;
const formFields = [];

Object.keys(schema).forEach(fieldName => {
  const field = schema[fieldName];
  
  if (!field.auto_increment && fieldName !== 'id') {
    formFields.push({
      name: fieldName,
      type: field.type,
      required: field.required || false,
      options: field.options || null,
      maxLength: field.max_length || null
    });
  }
});

return { formFields };
```

### Validation Rules Generation
Create validation rules automatically:

```javascript
// Generate validation rules from schema
const validationRules = {};

Object.keys(schema).forEach(fieldName => {
  const field = schema[fieldName];
  const rules = [];
  
  if (field.required) rules.push('required');
  if (field.max_length) rules.push(`max:${field.max_length}`);
  if (field.type === 'email') rules.push('email');
  if (field.options) rules.push(`in:${field.options.join(',')}`);
  
  validationRules[fieldName] = rules;
});

return { validationRules };
```

## Integration with WeWeb

### Dynamic Form Components
Build adaptive forms that adjust to your database schema:

```javascript
// WeWeb component using schema data
export default {
  data() {
    return {
      schema: {},
      formData: {},
      formFields: []
    };
  },
  
  async mounted() {
    // Fetch schema from Xano
    const response = await this.$xano.get('/api/get-schema', {
      table: 'users'
    });
    
    this.schema = response.data.schema;
    this.generateFormFields();
  },
  
  methods: {
    generateFormFields() {
      this.formFields = Object.keys(this.schema)
        .filter(key => !this.schema[key].auto_increment)
        .map(key => ({
          name: key,
          label: this.formatLabel(key),
          type: this.mapFieldType(this.schema[key].type),
          required: this.schema[key].required,
          options: this.schema[key].options
        }));
    },
    
    mapFieldType(xanoType) {
      const typeMap = {
        'string': 'text',
        'text': 'textarea',
        'integer': 'number',
        'decimal': 'number',
        'boolean': 'checkbox',
        'enum': 'select',
        'timestamp': 'datetime-local'
      };
      return typeMap[xanoType] || 'text';
    }
  }
};
```

## Real-World Use Cases

### 1. API Documentation Generator
Automatically generate API documentation from your schema:

```javascript
// Generate OpenAPI documentation
function generateAPIDoc(schema, tableName) {
  const properties = {};
  const required = [];
  
  Object.keys(schema).forEach(fieldName => {
    const field = schema[fieldName];
    
    properties[fieldName] = {
      type: mapToOpenAPIType(field.type),
      description: field.description || `${fieldName} field`
    };
    
    if (field.required) {
      required.push(fieldName);
    }
    
    if (field.options) {
      properties[fieldName].enum = field.options;
    }
  });
  
  return {
    [tableName]: {
      type: 'object',
      properties,
      required
    }
  };
}
```

### 2. Database Migration Helper
Compare schemas across environments:

```javascript
// Compare production vs development schemas
function compareSchemas(prodSchema, devSchema) {
  const differences = {
    added: [],
    removed: [],
    modified: []
  };
  
  // Find added fields
  Object.keys(devSchema).forEach(field => {
    if (!prodSchema[field]) {
      differences.added.push(field);
    }
  });
  
  // Find removed fields
  Object.keys(prodSchema).forEach(field => {
    if (!devSchema[field]) {
      differences.removed.push(field);
    }
  });
  
  // Find modified fields
  Object.keys(prodSchema).forEach(field => {
    if (devSchema[field] && 
        JSON.stringify(prodSchema[field]) !== JSON.stringify(devSchema[field])) {
      differences.modified.push({
        field,
        production: prodSchema[field],
        development: devSchema[field]
      });
    }
  });
  
  return differences;
}
```

### 3. Dynamic Search Interface
Build search forms that adapt to table structure:

```javascript
// Generate search filters based on schema
function generateSearchFilters(schema) {
  const searchableFields = Object.keys(schema).filter(key => {
    const field = schema[key];
    return ['string', 'text', 'enum', 'integer', 'decimal'].includes(field.type);
  });
  
  return searchableFields.map(fieldName => {
    const field = schema[fieldName];
    
    return {
      name: fieldName,
      label: formatLabel(fieldName),
      type: getSearchInputType(field.type),
      options: field.options || null,
      operators: getAvailableOperators(field.type)
    };
  });
}

function getAvailableOperators(fieldType) {
  const operatorMap = {
    'string': ['contains', 'equals', 'starts_with', 'ends_with'],
    'text': ['contains', 'equals'],
    'integer': ['equals', 'greater_than', 'less_than', 'between'],
    'decimal': ['equals', 'greater_than', 'less_than', 'between'],
    'enum': ['equals', 'in'],
    'boolean': ['equals'],
    'timestamp': ['equals', 'greater_than', 'less_than', 'between']
  };
  
  return operatorMap[fieldType] || ['equals'];
}
```

## Try This: Build a Schema Explorer

1. **Create a schema endpoint:**
   - Add Get Database Schema function
   - Allow table name as parameter
   - Return formatted schema data

2. **Build a simple schema viewer:**
   - List all tables in your database
   - Show field details for each table
   - Display relationships and constraints

3. **Add export functionality:**
   - Generate CSV of schema information
   - Create TypeScript interfaces
   - Export OpenAPI specifications

## Common Use Cases

### Form Generation
- **Dynamic user registration** - Adapt forms based on user types
- **Content management** - Generate edit forms for any content type
- **Survey builders** - Create forms from database definitions

### API Management
- **Documentation generation** - Automatic API docs from schema
- **Validation rules** - Generate client-side validation
- **Type definitions** - Create TypeScript/Flow types

### Data Migration
- **Schema comparison** - Compare across environments
- **Migration scripts** - Generate database migration code
- **Backup validation** - Verify schema integrity

## Common Mistakes to Avoid

❌ **Caching schema too aggressively** - Schema can change, refresh periodically
❌ **Ignoring field constraints** - Always respect required fields and validation rules
❌ **Not handling enum options** - Use the provided options for select fields
❌ **Hardcoding field types** - Use schema data to determine appropriate input types
❌ **Forgetting relationships** - Include related table information where needed

## Pro Tips

💡 **Cache schema responses** but implement cache invalidation when schema changes
💡 **Use path parameter** to fetch only needed field information for performance
💡 **Combine with metadata API** for complete database documentation
💡 **Create schema version tracking** to manage database evolution
💡 **Build schema-aware validation** that updates automatically
💡 **Use for API contract testing** to ensure frontend/backend compatibility
💡 **Generate database seeds** based on schema constraints

## Performance Considerations

### Optimize Schema Requests
- Use specific field paths when possible
- Cache schema data at the application level
- Combine multiple schema requests when building complex forms

### Schema Change Management
```javascript
// Implement schema versioning
const schemaCache = new Map();
const CACHE_TTL = 5 * 60 * 1000; // 5 minutes

async function getCachedSchema(tableName) {
  const cacheKey = `schema_${tableName}`;
  const cached = schemaCache.get(cacheKey);
  
  if (cached && (Date.now() - cached.timestamp) < CACHE_TTL) {
    return cached.data;
  }
  
  const schema = await fetchSchemaFromXano(tableName);
  schemaCache.set(cacheKey, {
    data: schema,
    timestamp: Date.now()
  });
  
  return schema;
}
```

## Security Considerations

### Field Filtering
Always filter sensitive fields from schema responses:

```javascript
// Remove sensitive field information
function sanitizeSchema(schema) {
  const sensitiveFields = ['password', 'secret', 'token'];
  const sanitized = { ...schema };
  
  sensitiveFields.forEach(field => {
    if (sanitized[field]) {
      delete sanitized[field];
    }
  });
  
  return sanitized;
}
```

The Get Database Schema function is powerful for building dynamic, schema-aware applications that adapt automatically as your database evolves.