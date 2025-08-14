---
title: "Environment Variables - Secure Configuration"
description: "Store API keys, secrets, and configuration safely across your workspace"
category: function-stack
subcategory: configuration
difficulty: beginner
has_code_examples: true
last_updated: '2025-01-23'
tags:
- environment
- variables
- security
- configuration
- secrets
---

# Environment Variables - Secure Configuration



## Quick Summary

> **What it is:** Secure storage for sensitive data like API keys that work across your entire workspace
> 
> **When to use:** Storing credentials, API keys, configuration values, or any sensitive information
> 
> **Key benefit:** Keep secrets safe and centralized, never hardcode sensitive data
> 
> **Perfect for:** Non-developers managing integrations and API connections securely

## What You'll Learn

- Creating environment variables
- Using them in functions
- Security best practices
- System variables
- Environment-specific configs

## Why Environment Variables?

### Without Environment Variables (BAD!)
```javascript
// NEVER DO THIS!
api_key = "sk-1234567890abcdef"  // Exposed in code!
Send_To_API(api_key, data)
```

### With Environment Variables (GOOD!)
```javascript
// Safe and secure
api_key = env.OPENAI_API_KEY  // Hidden from code
Send_To_API(api_key, data)
```

## Setting Up Environment Variables

### Step 1: Navigate to Settings
1. Click Settings in left navigation
2. Select Environment Variables
3. Click Edit button

### Step 2: Add New Variable
```javascript
Name: OPENAI_API_KEY
Value: sk-your-actual-api-key-here
```

### Step 3: Use in Function Stack
```javascript
// Access from dropdown
api_key = [ENV] → OPENAI_API_KEY

// Use in API call
External_API_Request {
  url: "https://api.openai.com/v1/chat",
  headers: {
    Authorization: "Bearer " + env.OPENAI_API_KEY
  }
}
```

## Common Use Cases

### API Integrations
```javascript
// Store different API keys
env.STRIPE_SECRET_KEY
env.SENDGRID_API_KEY
env.TWILIO_AUTH_TOKEN
env.AWS_ACCESS_KEY
env.GOOGLE_MAPS_KEY
```

### Configuration Values
```javascript
// App settings
env.APP_URL = "https://myapp.com"
env.SUPPORT_EMAIL = "support@myapp.com"
env.MAX_UPLOAD_SIZE = "10485760"  // 10MB
env.TIMEZONE = "America/New_York"
```

### Feature Flags
```javascript
// Toggle features
env.ENABLE_PAYMENTS = "true"
env.MAINTENANCE_MODE = "false"
env.BETA_FEATURES = "true"
```

## Integration Examples

### With n8n - Webhook Security
```javascript
// n8n sends webhook with secret
webhook_secret = Input.headers.x_webhook_secret

// Verify against environment variable
if (webhook_secret != env.WEBHOOK_SECRET) {
  return { 
    error: "Unauthorized",
    status: 401 
  }
}

// Process verified webhook
Process_Webhook_Data(Input.body)
```

### With WeWeb - API Configuration
```javascript
// Different APIs per environment
if (env.ENVIRONMENT == "production") {
  api_base = env.PROD_API_URL
} else {
  api_base = env.DEV_API_URL
}

// Make API call
External_API {
  url: api_base + "/endpoint",
  key: env.API_KEY
}
```

## System Environment Variables

Xano provides built-in variables:

### Request Information
```javascript
$remote_ip       // Client IP address
$http_headers    // Request headers
$request_uri     // Full request URL
$request_method  // GET, POST, etc.
```

### Environment Context
```javascript
$datasource      // Current data source
$branch          // Current branch
$request_querystring  // URL parameters
```

### Usage Example
```javascript
// Log API access
Add_Record {
  table: "api_logs",
  ip_address: $remote_ip,
  endpoint: $request_uri,
  method: $request_method,
  timestamp: now()
}

// Rate limit by IP
rate_key = "rate_limit_" + $remote_ip
Rate_Limit(rate_key, 100, 3600)
```

## Environment-Specific Configuration

### Development vs Production
```javascript
// Set different values per environment
DEV_API_URL = "https://api-dev.example.com"
PROD_API_URL = "https://api.example.com"

DEV_DEBUG_MODE = "true"
PROD_DEBUG_MODE = "false"

// Use based on current environment
if (env.ENVIRONMENT == "production") {
  use_live_payments = true
  api_url = env.PROD_API_URL
} else {
  use_live_payments = false
  api_url = env.DEV_API_URL
}
```

## Security Best Practices

### What to Store
✅ **Good for Environment Variables:**
- API keys and secrets
- Database connection strings
- Third-party service credentials
- Configuration values
- Feature flags

❌ **Don't Store:**
- User passwords
- Personal information
- Large data sets
- Temporary values
- Computed values

### Naming Conventions
```javascript
// Use clear, consistent names
STRIPE_SECRET_KEY     // Service + Type
AWS_ACCESS_KEY_ID     // Service + Specific Key
DB_CONNECTION_STRING  // Purpose + Type
SMTP_PASSWORD        // Protocol + Type
```

## Common Patterns

### API Key Rotation
```javascript
// Support multiple keys
primary_key = env.API_KEY_PRIMARY
backup_key = env.API_KEY_BACKUP

Try {
  result = Call_API(primary_key)
} Catch {
  // Fallback to backup
  result = Call_API(backup_key)
  Log_Alert("Primary key failed")
}
```

### Multi-Tenant Configuration
```javascript
// Different settings per client
client = Input.client_id

if (client == "client_a") {
  api_key = env.CLIENT_A_API_KEY
  webhook = env.CLIENT_A_WEBHOOK
} else if (client == "client_b") {
  api_key = env.CLIENT_B_API_KEY
  webhook = env.CLIENT_B_WEBHOOK
}
```

### Dynamic Configuration
```javascript
// Load config from environment
config = {
  max_retries: to_int(env.MAX_RETRIES || "3"),
  timeout: to_int(env.TIMEOUT_SECONDS || "30"),
  debug: env.DEBUG_MODE == "true"
}
```

## Try This

Set up secure API integration:
1. Add API key to environment variables
2. Create function using the key
3. Add error handling
4. Test with invalid key
5. Monitor usage

## Pro Tips

💡 **Never Hardcode:** Always use env vars for sensitive data

💡 **Use Descriptive Names:** Make it clear what each variable is for

💡 **Document Variables:** Keep a list of required env vars

💡 **Rotate Regularly:** Change API keys periodically

💡 **Different Per Environment:** Use separate keys for dev/prod

## Common Gotchas

### Missing Variables
```javascript
// Problem: Variable doesn't exist
api_key = env.MISSING_KEY  // Returns null

// Solution: Add default or check
api_key = env.API_KEY || "default_key"

if (!env.API_KEY) {
  return { error: "API key not configured" }
}
```

### Type Conversion
```javascript
// Problem: All env vars are strings
max_size = env.MAX_SIZE  // "1000" as string

// Solution: Convert types
max_size = to_int(env.MAX_SIZE)
enabled = env.FEATURE_ENABLED == "true"
```

### Case Sensitivity
```javascript
// Variables are case-sensitive
env.api_key  // Different from
env.API_KEY  // This one

// Be consistent with naming
```

## Next Steps

1. Audit hardcoded secrets
2. Move to environment variables
3. Document all variables
4. Set up for each environment
5. Implement key rotation

Remember: Environment variables keep your secrets safe - never expose sensitive data in code!