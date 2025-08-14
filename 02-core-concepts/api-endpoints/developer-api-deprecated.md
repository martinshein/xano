---
title: "Developer API (Deprecated) - Migration Guide"
description: "Learn about Xano's deprecated Developer API and how to migrate to the modern Metadata API for programmatic account management"
category: api-endpoints
tags:
  - Developer API
  - Deprecated
  - Migration
  - Account Management
  - Swagger Documentation
difficulty: advanced
reading_time: 8 minutes
last_updated: '2025-01-23'
prerequisites:
  - Understanding of API authentication
  - Account-level access to Xano
  - Basic knowledge of Swagger/OpenAPI
deprecation:
  status: deprecated
  replacement: "Metadata API"
  sunset_date: "To be announced"
---

# Developer API (Deprecated) - Migration Guide

## 🚨 **Deprecation Notice**

**This API is deprecated.** Please use the [Metadata API](master-metadata-api.md) for all new implementations.

**What's changing:**
- Developer API will be phased out
- New features won't be added
- Metadata API is the recommended replacement

**Timeline:**
- Current: Both APIs available
- Future: Developer API will be sunset (date TBA)

---

## 📋 **Quick Summary**

**What it was:** The Developer API provided programmatic access to your Xano account, instances, and workspace documentation.

**Why it's being replaced:** 
- Limited functionality compared to Metadata API
- Complex multi-step authentication
- Better alternatives now available

**Migration path:** Use the Metadata API for modern, comprehensive programmatic access

---

## What You'll Learn

- How the legacy Developer API worked
- Why it's being deprecated
- How to migrate to the Metadata API
- What functionality is available in the replacement

## Understanding the Legacy Developer API

The Developer API was Xano's first attempt at programmatic account management. It provided a way to:

### 🎯 **Core Capabilities**
- List your Xano instances
- Retrieve Swagger documentation
- Access workspace information
- Authenticate with individual instances

### ⚠️ **Limitations**
- Complex multi-step authentication
- Limited to documentation retrieval
- No direct data manipulation
- Single Developer API key per account

## How It Worked (Legacy)

### Authentication Flow

The Developer API used a complex 4-step authentication process:

```yaml
Step 1: Generate Developer API Key
Step 2: Authenticate with Master Service
Step 3: Get Instance Token
Step 4: Access Instance APIs
```

### Step 1: Generate Developer API Key

Navigate to your Account page to generate a single Developer API key:

**⚠️ Security Warning:** Once generated, the key couldn't be viewed again - only regenerated.

### Step 2: Master Service Authentication

```bash
curl -X 'GET' \
  'https://app.xano.com/api:developer/instance' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOUR_DEVELOPER_API_KEY'
```

This returned a list of your instances:

```json
[
  {
    "id": "instance-1",
    "name": "Production",
    "tokenUrl": "https://app.xano.com/api:developer/token/instance-1"
  },
  {
    "id": "instance-2", 
    "name": "Development",
    "tokenUrl": "https://app.xano.com/api:developer/token/instance-2"
  }
]
```

### Step 3: Instance Token Retrieval

Each instance required its own authentication token:

```bash
curl 'https://app.xano.com/api:developer/token/instance-1'
```

Response:
```json
{
  "authToken": "eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJ...",
  "api": "https://instance-1.xano.io/api:developer",
  "swaggerspec": "https://instance-1.xano.io/api:developer/swagger.json",
  "origin": "https://instance-1.xano.io"
}
```

### Step 4: Instance API Access

Finally, you could access instance-specific data:

```bash
curl -X 'GET' \
  'https://instance-1.xano.io/api:developer/workspace' \
  -H 'Authorization: Bearer eyJhbGciOiJBMjU2S1ci...'
```

## Why It's Being Deprecated

### 1. **Complexity**
- Required 4 separate API calls just to authenticate
- Different tokens for each instance
- Difficult to implement and maintain

### 2. **Limited Functionality**
- Only provided read access to documentation
- No data manipulation capabilities
- No bulk operations

### 3. **Better Alternatives**
- Metadata API provides comprehensive access
- Simpler authentication
- Direct data operations

## Migration to Metadata API

### What's Better in Metadata API

| Feature | Developer API | Metadata API |
|---------|---------------|--------------|
| Authentication | 4-step process | Single token |
| Data Access | Documentation only | Full CRUD operations |
| Instance Management | Complex | Streamlined |
| Bulk Operations | Not supported | Supported |
| Real-time Access | No | Yes |

### Migration Steps

#### 1. **Switch to Metadata API Authentication**

**Old Way (Developer API):**
```javascript
// Complex multi-step authentication
const instances = await getInstances(developerApiKey);
const token = await getInstanceToken(instances[0].tokenUrl);
const data = await callInstanceAPI(token);
```

**New Way (Metadata API):**
```javascript
// Simple single-token authentication
const data = await metadataAPI.call({
  headers: { 'Authorization': `Bearer ${metadataToken}` }
});
```

#### 2. **Replace Documentation Access**

**Old Way:**
```javascript
// Get Swagger documentation
const swagger = await fetch(swaggerspecUrl);
```

**New Way:**
```javascript
// Direct API access - no need for separate documentation calls
const schemas = await metadataAPI.getSchemas();
```

#### 3. **Upgrade to Direct Data Operations**

**Old Way (Not Possible):**
```javascript
// Developer API couldn't manipulate data
// Had to use custom endpoints
```

**New Way:**
```javascript
// Direct data operations
await metadataAPI.createRecord({ table: 'users', data: userData });
await metadataAPI.updateRecord({ id: 123, data: updates });
```

## Common Use Cases & Migrations

### Use Case 1: API Documentation Generation

**Legacy Implementation:**
```javascript
async function getAPIDocs() {
  const instances = await getDeveloperInstances();
  const tokens = await Promise.all(
    instances.map(i => getInstanceToken(i.tokenUrl))
  );
  const docs = await Promise.all(
    tokens.map(t => getSwaggerSpec(t.swaggerspec))
  );
  return docs;
}
```

**Modern Implementation:**
```javascript
async function getAPIDocs() {
  // Use Metadata API to get schema information
  const schemas = await metadataAPI.getWorkspaceSchemas();
  return schemas;
}
```

### Use Case 2: Instance Management

**Legacy Implementation:**
```javascript
// Complex instance listing
const instances = await callDeveloperAPI('/instance');
```

**Modern Implementation:**
```javascript
// Direct workspace access
const workspaces = await metadataAPI.getWorkspaces();
```

## Sunset Timeline & Support

### Current Status
- ✅ Developer API still functional
- ✅ Metadata API fully available
- ✅ Migration support provided

### What to Expect
1. **Deprecation warnings** in Developer API responses
2. **Rate limiting** may be applied to encourage migration
3. **Sunset announcement** with 6-month notice period
4. **Full removal** after sunset period

### Getting Help with Migration

#### 🔧 **Migration Tools**
- Automated migration scripts (coming soon)
- Side-by-side comparison guides
- Testing environments for validation

#### 📚 **Resources**
- [Metadata API Documentation](master-metadata-api.md)
- [Migration Workshop Videos](https://university.xano.com)
- [Community Migration Guide](https://community.xano.com)

## Security Considerations

### Current Users
If you're still using the Developer API:

1. **Rotate keys regularly** - Developer keys don't expire
2. **Monitor usage** - Check for any suspicious activity
3. **Plan migration** - Start transition to Metadata API
4. **Update integrations** - Prepare for eventual sunset

### New Implementations
For all new projects:

1. **Use Metadata API only** - Don't build on deprecated foundation
2. **Follow modern auth patterns** - Use proper token management
3. **Implement proper security** - Follow current best practices

## 💡 **Try This**

### Assessment Exercise
Audit your current Developer API usage:
1. List all applications using Developer API
2. Document the functionality being used
3. Map each use case to Metadata API equivalent
4. Create migration timeline

### Quick Migration Test
1. Generate Metadata API token
2. Replicate one Developer API call using Metadata API
3. Compare complexity and functionality
4. Plan full migration

## Common Mistakes to Avoid

1. **Waiting until sunset** - Start migration early
2. **Direct code replacement** - Redesign for better patterns
3. **Ignoring new features** - Leverage Metadata API capabilities
4. **No testing** - Thoroughly test migrated functionality

## Next Steps

- **Start with [Metadata API Overview](master-metadata-api.md)**
- **Review [Authentication Setup](token-scopes-reference.md)**
- **Explore [Content Management](content.md) capabilities**
- **Learn [Schema Operations](tables-and-schema.md)**

## Need Help?

### Migration Support
- 📞 **Enterprise Support** - Direct migration assistance
- 📚 **Community Forum** - Migration discussions and tips
- 🎥 **Video Guides** - Step-by-step migration walkthroughs
- 📖 **Documentation** - Comprehensive API references

### Critical Issues
If you encounter blocking issues during migration:
1. Document the specific use case
2. Contact Xano support with details
3. Request extended deprecated API access if needed
4. Get personalized migration guidance