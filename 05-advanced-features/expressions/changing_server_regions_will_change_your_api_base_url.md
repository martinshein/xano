---
title: "Changing Server Regions - URL Impact Guide"
description: "Learn how changing your Xano server region affects your API URLs and what you need to update for seamless migration."
category: expressions
has_code_examples: true
last_updated: '2025-01-16'
tags:
  - server-regions
  - api-urls
  - migration
  - deployment
  - configuration
---

# Changing Server Regions - URL Impact Guide

## 📋 **Quick Summary**

When you change your Xano server region, your API base URL will change completely. This requires updating all external connections, webhooks, and integrations before migration to prevent service disruption.

## What You'll Learn

- How server region changes affect your API URLs
- Which external connections need updating
- Step-by-step migration process
- Best practices for zero-downtime migration

## Available Server Regions

Xano's paid plans support multiple global server regions for optimal performance:

**Americas:**
- United States (Oregon)
- Canada (Montreal)  
- Brazil (São Paulo)

**Europe:**
- Germany (Frankfurt)
- France (Paris)
- United Kingdom (London)
- Belgium

**Asia-Pacific:**
- Japan (Tokyo)
- Singapore
- South Korea (Seoul)
- Australia (Sydney)
- India (Mumbai)
- Indonesia (Jakarta)

**Middle East:**
- Saudi Arabia (Dammam)

## Critical Pre-Migration Checklist

### ⚠️ **URL Change Impact**

Your instance URL will completely change:
- **Before:** `https://abc1-def2-ghi3.xano.io/`
- **After:** `https://xyz4-uvw5-rst6.xano.io/`

### 🔄 **What Needs Updating**

**n8n Workflows:**
```javascript
// Update HTTP Request nodes
{
  "url": "https://NEW-BASE-URL.xano.io/api:your-api-group/endpoint",
  "headers": {
    "Authorization": "Bearer {token}"
  }
}
```

**WeWeb Connections:**
```javascript
// Update API base URL in WeWeb data sources
const apiBaseUrl = "https://NEW-BASE-URL.xano.io/api:your-api-group";
```

**Make.com Scenarios:**
- Update HTTP module URLs
- Verify webhook endpoints
- Test all API connections

## Migration Process

### Step 1: Access Billing Settings

1. Click your name in the lower-left corner
2. Select **Billing**
3. Click the plan modification button

### Step 2: Select New Region

1. Choose your existing plan (prevents billing changes)
2. Scroll to **Server Region**
3. Select your preferred region from dropdown

> **💰 Pro Tip:** Region changes are free, but you'll be billed for a new subscription period minus unused time from your current period.

### Step 3: Pre-Migration Preparation

```javascript
// Document all current API endpoints
const currentEndpoints = [
  "https://old-url.xano.io/api:auth/login",
  "https://old-url.xano.io/api:users/profile",
  "https://old-url.xano.io/api:data/records"
];

// Prepare update list for external services
const externalServices = [
  "n8n workflows",
  "WeWeb data sources", 
  "Make.com scenarios",
  "Mobile app configs",
  "Third-party webhooks"
];
```

### Step 4: Complete Migration

1. Proceed through checkout
2. **STOP** - Review your new server URL
3. Update all external connections
4. Test critical endpoints
5. Click migration button when ready

## Common Migration Mistakes

❌ **Don't Do This:**
- Migrate without updating external connections
- Forget to publish draft changes before migration
- Skip testing after URL updates

✅ **Best Practices:**
- Create a migration checklist
- Test in staging environment first
- Coordinate with your team
- Monitor for errors post-migration

## Try This: Migration Checklist

Create this checklist before starting your migration:

```markdown
## Pre-Migration Checklist
- [ ] Document current API base URL
- [ ] List all external integrations
- [ ] Publish all draft changes
- [ ] Backup critical data
- [ ] Notify team members

## Post-Migration Checklist  
- [ ] Update n8n workflow URLs
- [ ] Update WeWeb data source URLs
- [ ] Update Make.com scenario URLs
- [ ] Test critical API endpoints
- [ ] Monitor error logs
- [ ] Update documentation
```

## Integration Examples

### n8n Workflow Update

```javascript
// Before migration - HTTP Request node
{
  "method": "GET",
  "url": "https://old-url.xano.io/api:users/{{$json.user_id}}",
  "headers": {
    "Authorization": "Bearer {{$json.token}}"
  }
}

// After migration - Updated URL
{
  "method": "GET", 
  "url": "https://new-url.xano.io/api:users/{{$json.user_id}}",
  "headers": {
    "Authorization": "Bearer {{$json.token}}"
  }
}
```

### WeWeb Configuration Update

```javascript
// Update WeWeb API plugin configuration
const xanoConfig = {
  baseURL: "https://new-url.xano.io",
  apiGroup: "your-api-group",
  endpoints: {
    login: "/auth/login",
    users: "/users",
    data: "/data"
  }
};
```

## Pro Tips

💡 **Planning Migration:**
- Schedule during low-traffic periods
- Have rollback plan ready
- Test thoroughly in staging first

💡 **Zero-Downtime Strategy:**
- Use DNS switching if possible
- Implement gradual traffic migration
- Monitor performance metrics

💡 **Post-Migration:**
- Update all documentation
- Inform API consumers
- Monitor for 48 hours minimum

⚠️ **Critical Warning:** Unpublished drafts will NOT be migrated. Publish all changes before proceeding with region migration.