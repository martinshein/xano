---
title: "Environment Variables & Settings Management"
description: "Comprehensive guide to managing environment variables, workspace settings, and configuration in Xano for secure API key storage and cross-function access."
category: configuration
difficulty: beginner
has_code_examples: true
last_updated: '2025-08-21'
tags:
  - environment-variables
  - settings
  - configuration
  - security
  - workspace-management
---

# Environment Variables & Settings Management

## 📋 **Quick Summary**
Complete guide to managing environment variables and workspace settings in Xano. Learn how to securely store API keys, configure cross-function variables, and optimize workspace settings for n8n, WeWeb, Make.com, and other no-code platform integrations.

## What You'll Learn
- How to create and manage environment variables securely
- Workspace settings navigation and configuration
- Built-in Xano system variables and their uses
- Best practices for API key and sensitive data management
- Integration setup for external services and no-code platforms

## 🚀 Understanding Environment Variables

Environment Variables are persistent variables available across your entire workspace. They're perfect for storing:
- **API Keys & Secrets** - External service credentials
- **Configuration Values** - URLs, domains, feature flags
- **Sensitive Information** - Database connections, tokens
- **Cross-Function Data** - Values used in multiple function stacks

## 🎯 Try This: Adding Environment Variables

### Step 1: Navigate to Settings
```bash
# From Xano dashboard:
Left Navigation → Settings → Environment Variables

# Or use the direct path:
Workspace → Settings → Environment Variables Tab
```

### Step 2: Create New Variable
```javascript
// Environment variable setup example
environment_variable = {
  name: "STRIPE_SECRET_KEY",           // Descriptive name
  value: "sk_live_abc123...",          // Secret value
  description: "Stripe payment processing key" // Optional description
}

// Common naming conventions:
API_BASE_URL = "https://api.myservice.com"
JWT_SECRET_KEY = "your-jwt-secret-here"
EMAIL_API_KEY = "your-email-service-key"
```

### Step 3: Use in Function Stacks
```javascript
// Access environment variables in function stacks
external_api_request({
  url: process.env.API_BASE_URL + "/users",
  headers: {
    "Authorization": "Bearer " + process.env.API_KEY,
    "Content-Type": "application/json"
  }
})

// Available under ENV dropdown in Visual Builder
// Select from: ENV → YOUR_VARIABLE_NAME
```

## 🔗 Integration Examples

### n8n Integration Setup
```javascript
// Environment variables for n8n webhooks
N8N_WEBHOOK_URL = "https://your-n8n-instance.com/webhook/abc123"
N8N_API_KEY = "your-n8n-api-key"

// Usage in function stack
trigger_n8n_workflow = external_api_request({
  url: process.env.N8N_WEBHOOK_URL,
  method: "POST",
  headers: {
    "X-N8N-API-KEY": process.env.N8N_API_KEY
  },
  data: {
    event: "user_created",
    user_id: request.data.id
  }
})
```

### WeWeb Integration Variables
```javascript
// WeWeb frontend connection
WEWEB_API_ENDPOINT = "https://your-weweb-app.com/api"
WEWEB_AUTH_TOKEN = "your-weweb-auth-token"

// Usage for WeWeb data sync
sync_to_weweb = external_api_request({
  url: process.env.WEWEB_API_ENDPOINT + "/sync",
  method: "POST",
  headers: {
    "Authorization": "Bearer " + process.env.WEWEB_AUTH_TOKEN
  },
  data: response_data
})
```

### Make.com Webhook Configuration
```javascript
// Make.com scenario triggers
MAKE_WEBHOOK_USER_CREATED = "https://hook.integromat.com/abc123"
MAKE_WEBHOOK_ORDER_UPDATED = "https://hook.integromat.com/def456"

// Usage in different function stacks
notify_make_user_created = external_api_request({
  url: process.env.MAKE_WEBHOOK_USER_CREATED,
  method: "POST",
  data: {
    user: new_user_data,
    timestamp: now()
  }
})
```

## 🔒 Built-in System Variables

Xano provides several built-in environment variables for request context:

### Request Information Variables
```javascript
// Access request details in function stacks
request_context = {
  ip_address: $remote_ip,           // Client IP address
  headers: $http_headers,           // All request headers
  url: $request_uri,               // Full request URL
  query_params: $request_querystring, // URL parameters
  http_method: $request_method      // GET, POST, PUT, DELETE, etc.
}

// Example usage for logging
audit_log = {
  user_ip: $remote_ip,
  user_agent: $http_headers['User-Agent'],
  endpoint: $request_uri,
  method: $request_method,
  timestamp: now()
}
```

### Database & Environment Context
```javascript
// System context variables
system_context = {
  datasource: $datasource,    // Current database connection
  branch: $branch,           // Development branch (dev/staging/prod)
  workspace_id: $workspace_id // Current workspace identifier
}

// Use for multi-environment logic
database_config = conditional({
  if: $branch == "production",
  then: {
    connection: $datasource,
    logging: false,
    cache_ttl: 300
  },
  else: {
    connection: $datasource,
    logging: true,
    cache_ttl: 60
  }
})
```

## ⚙️ Advanced Configuration Patterns

### Conditional Environment Loading
```javascript
// Environment-specific configurations
api_config = conditional({
  if: $branch == "production",
  then: {
    base_url: process.env.PROD_API_URL,
    api_key: process.env.PROD_API_KEY,
    timeout: 30000
  },
  else_if: $branch == "staging",
  then: {
    base_url: process.env.STAGING_API_URL,
    api_key: process.env.STAGING_API_KEY,
    timeout: 15000
  },
  else: {
    base_url: process.env.DEV_API_URL,
    api_key: process.env.DEV_API_KEY,
    timeout: 5000
  }
})
```

### Dynamic Service Configuration
```javascript
// Service registry using environment variables
service_registry = {
  email: {
    provider: process.env.EMAIL_PROVIDER || "sendgrid",
    api_key: process.env.EMAIL_API_KEY,
    from_address: process.env.FROM_EMAIL
  },
  payment: {
    provider: process.env.PAYMENT_PROVIDER || "stripe",
    secret_key: process.env.PAYMENT_SECRET_KEY,
    webhook_secret: process.env.PAYMENT_WEBHOOK_SECRET
  },
  storage: {
    provider: process.env.STORAGE_PROVIDER || "aws",
    access_key: process.env.STORAGE_ACCESS_KEY,
    secret_key: process.env.STORAGE_SECRET_KEY,
    bucket: process.env.STORAGE_BUCKET
  }
}
```

## 🔧 Workspace Settings Navigation

### Settings Organization
```bash
# Main settings categories:
Workspace Settings/
├── General Settings          # Basic workspace info
├── Environment Variables     # Custom variables
├── Team Management          # User access & roles
├── API Configuration        # Endpoint settings
├── Database Settings        # Connection & performance
├── Security Policies        # Access control & auth
├── Integrations            # External service connections
└── Billing & Usage         # Plan & resource monitoring
```

### Quick Access Paths
```javascript
// Common settings locations:
settings_paths = {
  env_variables: "Settings → Environment Variables",
  api_keys: "Settings → Environment Variables → Add New",
  team_access: "Settings → Team Management → Members",
  security: "Settings → Security Policies → Authentication",
  integrations: "Settings → Integrations → External Services"
}
```

## 💡 Pro Tips

- **Naming Convention**: Use UPPER_CASE with underscores for environment variables
- **Security First**: Never commit sensitive values to version control
- **Environment Separation**: Use different variables for dev/staging/production
- **Documentation**: Add descriptions to complex environment variables
- **Regular Rotation**: Periodically update API keys and secrets

## 🆘 Common Mistakes to Avoid

- **Hardcoding Secrets**: Always use environment variables for sensitive data
- **Poor Naming**: Use descriptive names like `STRIPE_SECRET_KEY` not `KEY1`
- **Missing Validation**: Check if environment variables exist before using them
- **Oversharing**: Don't give all team members access to production secrets
- **No Backup**: Document your environment variables securely

## 🎯 Try This: Complete Setup Example

### E-commerce Integration Setup
```javascript
// 1. Set up environment variables
environment_setup = {
  // Payment processing
  STRIPE_PUBLIC_KEY: "pk_live_abc123...",
  STRIPE_SECRET_KEY: "sk_live_def456...",
  STRIPE_WEBHOOK_SECRET: "whsec_ghi789...",
  
  // Email marketing
  MAILCHIMP_API_KEY: "abc123-us1",
  MAILCHIMP_LIST_ID: "list123",
  
  // External APIs
  SHOPIFY_ADMIN_TOKEN: "shpat_abc123...",
  GOOGLE_ANALYTICS_KEY: "UA-123456-1",
  
  // No-code integrations
  N8N_WEBHOOK_ORDER: "https://n8n.yoursite.com/webhook/order",
  ZAPIER_WEBHOOK_USER: "https://hooks.zapier.com/abc123"
}

// 2. Use in function stack
process_order = function_stack([
  validate_order_data,
  charge_payment({
    api_key: process.env.STRIPE_SECRET_KEY,
    amount: order.total
  }),
  add_to_mailing_list({
    api_key: process.env.MAILCHIMP_API_KEY,
    list_id: process.env.MAILCHIMP_LIST_ID,
    email: customer.email
  }),
  trigger_fulfillment({
    webhook_url: process.env.N8N_WEBHOOK_ORDER,
    order_data: order
  })
])
```

## 📊 Environment Variable Management Table

| Variable Type | Example | Security Level | Update Frequency |
|---------------|---------|----------------|------------------|
| API Keys | `STRIPE_SECRET_KEY` | High | Monthly |
| URLs | `API_BASE_URL` | Low | Rarely |
| Feature Flags | `ENABLE_BETA_FEATURES` | Low | Weekly |
| Database Configs | `DB_CONNECTION_STRING` | High | Rarely |
| Webhook URLs | `N8N_WEBHOOK_URL` | Medium | When needed |

## 🔄 Next Steps

### After Setting Up Environment Variables
1. **Test Connectivity** - Verify all external service connections
2. **Set Up Monitoring** - Track usage of environment-dependent features
3. **Document Integration** - Record which variables are used where
4. **Security Review** - Audit access to sensitive environment variables
5. **Backup Strategy** - Maintain secure backup of critical configurations

## 🔗 Related Documentation

- **[Instance Settings](instance-settings.md)** - Advanced workspace configuration
- **[Security Policy](../../../02-core-concepts/authentication/security-policy.md)** - Security best practices
- **[External API Request](../../../02-core-concepts/api-endpoints/api__external_api_request.md)** - Using environment variables in API calls
- **[Team Management](managing-team-members.md)** - Controlling access to sensitive settings

## 📈 Advanced Use Cases

### Multi-Tenant Configuration
```javascript
// Tenant-specific environment variables
tenant_config = {
  database_url: process.env.TENANT_DB_PREFIX + tenant_id,
  api_domain: tenant_id + "." + process.env.BASE_DOMAIN,
  storage_bucket: process.env.STORAGE_PREFIX + tenant_id
}
```

### A/B Testing Variables
```javascript
// Feature flag management
feature_flags = {
  new_checkout_flow: process.env.ENABLE_NEW_CHECKOUT === "true",
  advanced_analytics: process.env.ENABLE_ANALYTICS === "true",
  beta_features: process.env.BETA_ACCESS_ENABLED === "true"
}
```

Environment variables are the foundation of secure, maintainable Xano applications. Use them wisely to keep your integrations secure and your code clean!