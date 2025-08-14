---
title: "Managing Database Content with Metadata API - Complete Guide"
description: "Master Xano's Metadata API for creating, updating, deleting, and managing database records programmatically - perfect for n8n, WeWeb, and Make automations"
category: api-endpoints
tags:
  - Metadata API
  - Database Operations
  - CRUD
  - Records Management
  - API Integration
difficulty: intermediate
reading_time: 10 minutes
last_updated: '2025-01-23'
prerequisites:
  - Basic understanding of APIs
  - Xano workspace with tables
  - Metadata API access token
---

# Managing Database Content with Metadata API

## 📋 **Quick Summary**

**What it does:** The Metadata API provides programmatic access to create, read, update, and delete database records in Xano without building custom API endpoints.

**Why it matters:** This API enables you to:
- Manage database content directly from external tools
- Build admin dashboards without custom endpoints
- Automate bulk data operations
- Integrate with no-code tools for dynamic data management

**Time to implement:** 5-10 minutes per operation

---

## What You'll Learn

- How to create new database records via API
- Updating existing records with partial data
- Deleting single or multiple records
- Truncating entire tables safely
- Searching and browsing content programmatically
- Best practices for production use

## Understanding the Metadata API

Think of the Metadata API as your direct database access tool - like having a master key to your database that bypasses the need for custom endpoints.

### 🎯 **Perfect For:**
- Building admin panels in WeWeb
- Bulk data operations in n8n
- Database maintenance workflows in Make
- Quick prototyping without API development

## Authentication Setup

### Getting Your Access Token

Before using the Metadata API, you need proper authentication:

```yaml
1. Navigate to Settings → API Keys
2. Generate a Metadata API token
3. Store securely in your environment
4. Include in all requests as Bearer token
```

### 💡 **Integration Tip**
```javascript
// n8n HTTP Request node
Headers: {
  "Authorization": "Bearer YOUR_METADATA_TOKEN",
  "Content-Type": "application/json"
}
```

## Creating Content

### Basic Record Creation

To create a new record, you need three pieces of information:

| Parameter | Description | Example |
|-----------|-------------|---------|
| workspace_id | Your workspace identifier | `12345` |
| table_id | Target table ID | `67890` |
| fields | Data for the new record | `{"name": "value"}` |

### 📝 **Example: Creating a Product**

```json
POST /api:metadata/content
{
  "workspace_id": 12345,
  "table_id": 67890,
  "fields": {
    "name": "Wireless Headphones",
    "description": "Premium noise-canceling headphones",
    "category_id": 3,
    "price": 99.99,
    "in_stock": true
  }
}
```

**Response:**
```json
{
  "id": 11,
  "created_at": 1681349436618,
  "name": "Wireless Headphones",
  "description": "Premium noise-canceling headphones",
  "category_id": 3,
  "price": 99.99,
  "in_stock": true
}
```

### 🔧 **n8n Workflow Example**

```yaml
1. Trigger: Webhook received from form
2. Set Node: Prepare product data
3. HTTP Request: POST to Metadata API
4. IF Node: Check if creation successful
5. Email: Notify admin of new product
```

## Updating Existing Content

### Partial Updates

The Metadata API supports partial updates - you only send the fields you want to change:

```json
PATCH /api:metadata/content/{content_id}
{
  "workspace_id": 12345,
  "table_id": 67890,
  "fields": {
    "price": 149.99,
    "on_sale": true
  }
}
```

### 💡 **Smart Update Pattern**

Only update what's changed to:
- Reduce payload size
- Minimize database writes
- Preserve unchanged data
- Improve performance

### Bulk Updates

For updating multiple records:

```javascript
// Process array of updates
const updates = [
  { id: 1, price: 99 },
  { id: 2, price: 149 },
  { id: 3, price: 199 }
];

for (const update of updates) {
  await updateRecord(update.id, { price: update.price });
}
```

## Deleting Content

### Single Record Deletion

```json
DELETE /api:metadata/content/{content_id}
{
  "workspace_id": 12345,
  "table_id": 67890
}
```

### ⚠️ **Safety Checklist**

Before deleting:
- [ ] Verify record exists
- [ ] Check for related records
- [ ] Consider soft delete instead
- [ ] Log the deletion
- [ ] Have a backup strategy

### Implementing Soft Delete

Instead of permanent deletion:

```json
PATCH /api:metadata/content/{content_id}
{
  "fields": {
    "deleted_at": "2024-01-23T10:00:00Z",
    "deleted_by": "user_123"
  }
}
```

## Truncating Tables

### Complete Table Reset

Truncate removes ALL records from a table:

```json
POST /api:metadata/truncate
{
  "workspace_id": 12345,
  "table_id": 67890,
  "reset_primary_key": true
}
```

### 🚨 **DANGER ZONE**

Truncating is irreversible! Always:
1. **Backup first** - Export data before truncating
2. **Confirm table** - Double-check table ID
3. **Test in staging** - Never first-time in production
4. **Document reason** - Log why truncation was needed

### Safe Truncation Pattern

```yaml
Workflow:
1. Export current data to CSV
2. Store backup in cloud storage
3. Log truncation request
4. Perform truncate operation
5. Verify table is empty
6. Reset auto-increment if needed
```

## Common Integration Patterns

### Pattern 1: Form to Database

```yaml
User Form → Validation → Metadata API → Database → Confirmation
```

### Pattern 2: Spreadsheet Sync

```yaml
Google Sheets → n8n → Transform Data → Metadata API → Xano Database
```

### Pattern 3: Bulk Import

```yaml
CSV File → Parse → Validate → Batch Create → Progress Updates
```

### Pattern 4: Database Cleanup

```yaml
Schedule → Query Old Records → Soft Delete → Archive → Truncate
```

## Error Handling

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| 401 | Invalid token | Check authentication |
| 404 | Record not found | Verify IDs exist |
| 422 | Validation failed | Check field requirements |
| 429 | Rate limited | Implement retry logic |
| 500 | Server error | Contact support |

### Retry Logic Example

```javascript
async function createWithRetry(data, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await createRecord(data);
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await sleep(1000 * Math.pow(2, i)); // Exponential backoff
    }
  }
}
```

## Performance Optimization

### Batch Operations

Instead of individual requests:

```javascript
// ❌ Slow - Individual requests
for (const item of items) {
  await createRecord(item);
}

// ✅ Fast - Batch request
await batchCreate(items);
```

### Caching Strategies

1. **Cache workspace/table IDs** - They don't change often
2. **Batch similar operations** - Group creates/updates
3. **Use pagination** - For large result sets
4. **Implement request pooling** - Limit concurrent requests

## Security Best Practices

### 1. Token Management

```yaml
✅ DO:
- Store tokens in environment variables
- Rotate tokens regularly
- Use different tokens for dev/prod
- Limit token permissions

❌ DON'T:
- Hardcode tokens in code
- Share tokens between projects
- Use admin tokens for public apps
- Log tokens in plain text
```

### 2. Data Validation

Always validate before sending:

```javascript
function validateProduct(data) {
  const errors = [];
  
  if (!data.name || data.name.length < 3) {
    errors.push("Name must be at least 3 characters");
  }
  
  if (data.price && data.price < 0) {
    errors.push("Price cannot be negative");
  }
  
  return errors;
}
```

### 3. Audit Logging

Track all Metadata API operations:

```json
{
  "action": "create",
  "table": "products",
  "user": "admin_123",
  "timestamp": "2024-01-23T10:00:00Z",
  "data": { /* sanitized data */ }
}
```

## 💡 **Try This**

### Beginner Challenge
Create a simple n8n workflow that:
1. Receives webhook data
2. Creates a record using Metadata API
3. Returns the new record ID

### Intermediate Challenge
Build a WeWeb admin panel that:
1. Lists all records from a table
2. Allows inline editing
3. Updates via Metadata API
4. Shows success notifications

### Advanced Challenge
Design a data migration system that:
1. Reads from external API
2. Transforms data format
3. Validates all records
4. Bulk imports to Xano
5. Generates import report

## Common Mistakes to Avoid

1. **Not handling errors** - Always implement try/catch
2. **Missing validation** - Validate before sending
3. **Ignoring rate limits** - Implement backoff strategies
4. **No backup before truncate** - Always backup first
5. **Using wrong IDs** - Double-check workspace/table IDs

## Platform-Specific Examples

### 🔗 **n8n Integration**
```yaml
HTTP Request Node:
- Method: POST
- URL: https://[instance].xano.io/api:metadata/content
- Authentication: Header Auth
- Header Name: Authorization
- Header Value: Bearer [token]
```

### 🌐 **WeWeb Setup**
```javascript
// In WeWeb API configuration
const metadata = {
  baseURL: 'https://[instance].xano.io/api:metadata',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  }
};
```

### 🔧 **Make Module**
```yaml
HTTP Module:
- URL: Metadata API endpoint
- Method: Choose operation
- Headers: Add Authorization
- Body: JSON with parameters
- Parse Response: Yes
```

## Next Steps

- Learn about [Search Operations](search.md) for querying content
- Explore [File Management](file.md) via Metadata API
- Master [Schema Management](tables-and-schema.md)
- Understand [Token Scopes](token-scopes-reference.md) for security

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Ask questions
- 🎥 [Video Tutorials](https://university.xano.com) - See examples
- 📖 [API Reference](https://docs.xano.com/api) - Full documentation