---
title: "Master Metadata API - Instance and Snippet Management Guide"
description: "Master the Xano Master Metadata API for programmatic instance management, snippet control, and account-level operations for no-code automation"
category: api-endpoints
tags:
  - Master Metadata API
  - Instance Management
  - Snippets
  - Account Management
  - Personal Access Token
difficulty: advanced
reading_time: 12 minutes
last_updated: '2025-01-23'
prerequisites:
  - Personal Access Token configured
  - Understanding of Xano instances
  - Basic API authentication knowledge
---

# Master Metadata API - Instance and Snippet Management

## 📋 **Quick Summary**

**What it does:** The Master Metadata API provides account-level access to manage your Xano instances, snippets, and access tokens programmatically.

**Why it matters:** This enables you to:
- List and manage multiple Xano instances from one API
- Build multi-tenant applications with instance switching
- Automate snippet distribution and access control
- Create admin dashboards for Xano account management

**Time to implement:** 15-30 minutes for basic instance listing, hours for full snippet management

---

## What You'll Learn

- How to authenticate with Personal Access Tokens
- Managing multiple Xano instances programmatically  
- Working with snippets and access tokens
- Building instance selection interfaces
- Best practices for account-level operations

## Understanding the Master Metadata API

Think of the Master Metadata API as your command center for managing your entire Xano account - like having administrative access to all your instances and shared resources from a single API.

### 🎯 **Perfect For:**
- Multi-tenant SaaS applications
- Agency dashboards managing client instances
- Snippet marketplace applications
- Account management interfaces
- Instance switching functionality

## API Authentication

### Personal Access Token Setup

The Master Metadata API requires a Personal Access Token (PAT) for authentication:

1. Navigate to your Xano account settings
2. Generate a Personal Access Token
3. Store securely (never expose in frontend code)
4. Use as Bearer token in API requests

### Authentication Format

```javascript
headers: {
  'Authorization': 'Bearer YOUR_PERSONAL_ACCESS_TOKEN',
  'Content-Type': 'application/json'
}
```

## Instance Management

### Listing All Instances

Get a complete list of instances associated with your account:

```javascript
GET https://app.xano.com/api:meta/instance
Authorization: Bearer YOUR_PAT
```

**Response:**
```json
[
  {
    "id": "prod-instance-123",
    "name": "Production Environment",
    "domain": "x8d0-doy0-xx99.n0.xano.io",
    "custom_domain": "api.yourapp.com",
    "meta_api": "https://x8d0-doy0-xx99.n0.xano.io/api:metadata",
    "swagger_spec": "https://x8d0-doy0-xx99.n0.xano.io/api:metadata/swagger.json",
    "created_at": "2024-01-15T10:30:00Z",
    "plan": "pro",
    "status": "active"
  },
  {
    "id": "dev-instance-456", 
    "name": "Development Environment",
    "domain": "y9e1-fpy1-yy00.n0.xano.io",
    "custom_domain": null,
    "meta_api": "https://y9e1-fpy1-yy00.n0.xano.io/api:metadata",
    "swagger_spec": "https://y9e1-fpy1-yy00.n0.xano.io/api:metadata/swagger.json",
    "created_at": "2024-01-10T14:20:00Z",
    "plan": "starter", 
    "status": "active"
  }
]
```

### Getting Single Instance Details

Retrieve specific instance information:

```javascript
GET https://app.xano.com/api:meta/instance/{name}
Authorization: Bearer YOUR_PAT
```

**Parameters:**
- `{name}`: The instance name identifier

### 📝 **Instance Switching Pattern**

```javascript
// Build instance selector
async function buildInstanceSelector() {
  const instances = await fetch('https://app.xano.com/api:meta/instance', {
    headers: { 'Authorization': `Bearer ${personalAccessToken}` }
  }).then(r => r.json());
  
  return instances.map(instance => ({
    id: instance.id,
    name: instance.name,
    apiUrl: instance.meta_api,
    environment: instance.name.includes('prod') ? 'production' : 'development'
  }));
}
```

## No-Code Platform Integration

### 🔗 **n8n Multi-Instance Workflow**

```yaml
1. HTTP Request (Get instances list)
2. Set Node (Process instance data)
3. Function Node (Filter by criteria)
4. Switch Node (Route by environment)
5. HTTP Request (Call specific instance API)
```

### 🌐 **WeWeb Instance Switcher**

```javascript
// WeWeb collection for instances
async function loadUserInstances() {
  const instances = await wwLib.api.get({
    url: 'https://app.xano.com/api:meta/instance',
    headers: {
      'Authorization': `Bearer ${wwLib.envVars.PERSONAL_ACCESS_TOKEN}`
    }
  });
  
  // Update WeWeb collection
  wwLib.collections.instances.update(instances.data);
  
  return instances.data;
}
```

### 🔧 **Make Instance Management**

```yaml
Scenario Steps:
1. HTTP Request (List instances)
2. Iterator (Process each instance)
3. Filter (Check instance status)
4. HTTP Request (Call instance-specific API)
5. Aggregator (Combine results)
```

## Snippet Management

Snippets are reusable code components that can be shared across instances.

### Listing Your Snippets

```javascript
GET https://app.xano.com/api:meta/snippet
Authorization: Bearer YOUR_PAT
```

**Optional Parameters:**
- `page`: Page number for pagination

**Response:**
```json
{
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "items": [
    {
      "canonical": "kRG3t_-i",
      "name": "User Authentication Flow",
      "created_at": "2024-01-20T09:15:00Z",
      "updated_at": "2024-01-22T16:30:00Z",
      "review": "approved",
      "install_access": "public",
      "featured": false,
      "verified": true
    }
  ]
}
```

### Getting Specific Snippet

```javascript
GET https://app.xano.com/api:meta/snippet/{canonical}
Authorization: Bearer YOUR_PAT
```

**Parameters:**
- `{canonical}`: The snippet's unique identifier (found in snippet URL)

### Updating Snippet Settings

```javascript
POST https://app.xano.com/api:meta/snippet/{canonical}
Authorization: Bearer YOUR_PAT
Content-Type: application/json

{
  "install_access": "token", // "public", "link", or "token"
  "install_access_description": "Premium feature for subscribers only"
}
```

## Access Token Management

Control who can install your snippets with access tokens.

### Creating Access Tokens

```javascript
POST https://app.xano.com/api:meta/snippet/{canonical}/token
Authorization: Bearer YOUR_PAT
Content-Type: application/json

{
  "max_installs": 50
}
```

**Response:**
```json
{
  "created_at": "2024-01-23T10:00:00Z",
  "updated_at": "2024-01-23T10:00:00Z", 
  "token": "OL3T4JYM",
  "max_installs": 50,
  "current_installs": 0
}
```

### Listing Snippet Tokens

```javascript
GET https://app.xano.com/api:meta/snippet/{canonical}/token
Authorization: Bearer YOUR_PAT
```

### Updating Token Limits

```javascript
POST https://app.xano.com/api:meta/snippet/{canonical}/token/{token}
Authorization: Bearer YOUR_PAT
Content-Type: application/json

{
  "max_installs": 100,
  "current_installs": 25
}
```

### Revoking Tokens

```javascript
DELETE https://app.xano.com/api:meta/snippet/{canonical}/token/{token}
Authorization: Bearer YOUR_PAT
```

## Common Use Cases

### Use Case 1: Agency Dashboard

Build a dashboard for managing multiple client instances:

```javascript
// Agency instance manager
class AgencyInstanceManager {
  constructor(personalAccessToken) {
    this.pat = personalAccessToken;
  }
  
  async getClientInstances() {
    const instances = await this.callMasterAPI('/instance');
    
    return instances.map(instance => ({
      clientName: this.extractClientName(instance.name),
      environment: instance.name,
      status: instance.status,
      apiUrl: instance.meta_api,
      lastUpdated: instance.updated_at
    }));
  }
  
  async switchToInstance(instanceId) {
    const instance = await this.callMasterAPI(`/instance/${instanceId}`);
    
    // Update app configuration to use this instance
    this.updateAppConfig({
      currentInstance: instanceId,
      apiUrl: instance.meta_api,
      swaggerUrl: instance.swagger_spec
    });
  }
}
```

### Use Case 2: Snippet Marketplace

Create a marketplace for selling Xano snippets:

```javascript
// Snippet marketplace manager
class SnippetMarketplace {
  async createSnippetListing(snippetCanonical, pricing) {
    // Update snippet to token-based access
    await this.updateSnippetAccess(snippetCanonical, 'token');
    
    // Generate tokens based on pricing tiers
    const tokens = await Promise.all(
      pricing.tiers.map(tier => 
        this.createAccessToken(snippetCanonical, tier.installLimit)
      )
    );
    
    return {
      snippet: snippetCanonical,
      accessTokens: tokens,
      pricing: pricing
    };
  }
  
  async purchaseSnippet(snippetCanonical, customerId, tier) {
    // Find available token for the tier
    const availableToken = await this.findAvailableToken(snippetCanonical, tier);
    
    // Record purchase and provide token to customer
    await this.recordPurchase(customerId, snippetCanonical, availableToken);
    
    return {
      installToken: availableToken.token,
      installInstructions: this.generateInstallInstructions(snippetCanonical, availableToken.token)
    };
  }
}
```

### Use Case 3: Multi-Environment Deployment

Manage deployments across development, staging, and production:

```javascript
// Deployment manager
class DeploymentManager {
  async deployAcrossEnvironments(configChanges) {
    const instances = await this.getInstances();
    
    const environments = {
      dev: instances.filter(i => i.name.includes('dev')),
      staging: instances.filter(i => i.name.includes('staging')), 
      prod: instances.filter(i => i.name.includes('prod'))
    };
    
    // Deploy to dev first
    await this.deployToEnvironment(environments.dev, configChanges);
    await this.runTests(environments.dev);
    
    // Then staging
    await this.deployToEnvironment(environments.staging, configChanges);
    await this.runIntegrationTests(environments.staging);
    
    // Finally production (with approval gate)
    if (await this.getApproval('production deployment')) {
      await this.deployToEnvironment(environments.prod, configChanges);
    }
  }
}
```

## Error Handling

### Common HTTP Status Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 400 | Bad Request | Check request payload format |
| 403 | Forbidden | Verify Personal Access Token permissions |
| 404 | Not Found | Confirm instance/snippet exists |
| 429 | Rate Limited | Implement retry with exponential backoff |
| 500 | Server Error | Contact Xano support |

### Robust Error Handling

```javascript
class MasterAPIClient {
  async callWithRetry(endpoint, options = {}, maxRetries = 3) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      try {
        const response = await fetch(`https://app.xano.com/api:meta${endpoint}`, {
          ...options,
          headers: {
            'Authorization': `Bearer ${this.pat}`,
            'Content-Type': 'application/json',
            ...options.headers
          }
        });
        
        if (response.status === 429) {
          // Rate limited - wait before retry
          await this.sleep(1000 * Math.pow(2, attempt));
          continue;
        }
        
        if (!response.ok) {
          throw new Error(`API Error: ${response.status} - ${response.statusText}`);
        }
        
        return await response.json();
        
      } catch (error) {
        if (attempt === maxRetries) throw error;
        await this.sleep(1000 * attempt);
      }
    }
  }
  
  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

## Security Best Practices

### 1. Token Management

```javascript
// ✅ Good - Server-side PAT usage
const masterAPI = new MasterAPIClient({
  pat: process.env.XANO_PERSONAL_ACCESS_TOKEN,
  environment: 'server'
});

// ❌ Bad - Never expose PAT in frontend
// const pat = "xano_pat_1234567890"; // DON'T DO THIS
```

### 2. Access Control

```javascript
// Implement proper access controls
function checkUserPermissions(userId, action) {
  const permissions = getUserPermissions(userId);
  
  if (action === 'list_instances' && !permissions.includes('read_instances')) {
    throw new Error('Insufficient permissions');
  }
  
  if (action === 'manage_snippets' && !permissions.includes('admin')) {
    throw new Error('Admin access required');
  }
}
```

### 3. Rate Limiting

```javascript
// Implement client-side rate limiting
class RateLimitedClient {
  constructor(requestsPerMinute = 60) {
    this.requests = [];
    this.limit = requestsPerMinute;
  }
  
  async request(endpoint, options) {
    await this.waitForRateLimit();
    this.requests.push(Date.now());
    return this.callAPI(endpoint, options);
  }
  
  async waitForRateLimit() {
    const now = Date.now();
    const oneMinuteAgo = now - 60000;
    
    // Remove old requests
    this.requests = this.requests.filter(time => time > oneMinuteAgo);
    
    if (this.requests.length >= this.limit) {
      const oldestRequest = Math.min(...this.requests);
      const waitTime = 60000 - (now - oldestRequest);
      await this.sleep(waitTime);
    }
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Create a simple instance selector that:
1. Lists all your instances
2. Shows environment type (dev/prod)
3. Allows switching between them

### Intermediate Challenge
Build a snippet manager that:
1. Lists your snippets
2. Creates access tokens
3. Tracks installation counts
4. Manages access permissions

### Advanced Challenge
Design an agency dashboard that:
1. Manages multiple client instances
2. Provides environment-specific deployments
3. Monitors instance health
4. Automated backup management

## Common Mistakes to Avoid

1. **Exposing PAT in frontend** - Always keep server-side
2. **No rate limiting** - Implement client-side throttling
3. **Ignoring pagination** - Handle paginated responses properly
4. **Missing error handling** - Account for all HTTP status codes
5. **Hardcoding instance URLs** - Use dynamic instance discovery

## Next Steps

- Learn about [Individual Instance Metadata API](content.md)
- Explore [Token Scopes and Permissions](token-scopes-reference.md)
- Master [Workspace Import/Export](workspace-import-and-export.md)
- Understand [Request History Tracking](request-history.md)

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Master API discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step guides
- 📖 [API Reference](https://app.xano.com/api:meta) - Live Swagger documentation
- 🔧 [Support](https://xano.com/support) - Technical assistance