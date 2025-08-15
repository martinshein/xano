---
title: "Finding Your Database Identifier - Configuration and Setup"
description: "Learn how to locate and configure your Xano database identifier for API connections, external integrations, and automated workflows"
category: data-operations
tags:
  - Database Identifier
  - Configuration
  - API Setup
  - Database Connection
  - Instance Settings
  - External Integrations
difficulty: beginner
reading_time: 8 minutes
last_updated: '2025-01-15'
prerequisites:
  - Active Xano account
  - Basic understanding of database concepts
  - Familiarity with API connections
---

# Finding Your Database Identifier - Configuration and Setup

## 📋 **Quick Summary**

**What it does:** Your database identifier is a unique key that allows external applications and integrations to connect securely to your specific Xano database instance.

**Why it matters:** Database identifiers enable you to:
- **Connect external applications** to your Xano database
- **Set up automated workflows** with n8n, Make.com, and Zapier
- **Configure development environments** with proper database targeting
- **Implement secure API connections** with authentication
- **Enable data synchronization** between systems

**Time to implement:** 5-10 minutes to locate and configure, additional time for integration setup

---

## What You'll Learn

- How to locate your database identifier in Xano
- Configuration steps for external integrations
- Security best practices for database connections
- Common integration patterns with no-code platforms
- Troubleshooting connection issues

## Locating Your Database Identifier

### In the Xano Dashboard

```javascript
// Your database identifier format
{
  "database_id": "abc123-def456-ghi789",
  "instance_url": "https://your-instance.xano.io",
  "api_base_url": "https://your-instance.xano.io/api:abc123",
  "region": "us-east-1"
}
```

**Step-by-step location process:**

1. **Login to Xano Dashboard**
   - Navigate to [app.xano.com](https://app.xano.com)
   - Access your workspace

2. **Navigate to Instance Settings**
   - Click on your instance name
   - Select "Settings" from the menu
   - Find "Instance Information" section

3. **Copy Database Identifier**
   - Look for "Database ID" or "Instance ID"
   - Copy the full identifier string
   - Note the associated region

### Using the API

```javascript
// Get instance information via API
const getInstanceInfo = async () => {
  try {
    const response = await fetch('https://your-instance.xano.io/api:your-db-id/info', {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + authToken,
        'Content-Type': 'application/json'
      }
    });
    
    const instanceData = await response.json();
    
    return {
      database_id: instanceData.database_id,
      instance_name: instanceData.name,
      region: instanceData.region,
      api_url: instanceData.api_base_url
    };
  } catch (error) {
    console.error('Failed to get instance info:', error);
    return null;
  }
};
```

## Configuration for Integrations

### Environment Variables Setup

```bash
# .env file configuration
XANO_DATABASE_ID=abc123-def456-ghi789
XANO_INSTANCE_URL=https://your-instance.xano.io
XANO_API_BASE_URL=https://your-instance.xano.io/api:abc123
XANO_API_KEY=your-api-key-here
XANO_REGION=us-east-1

# Development vs Production
XANO_DATABASE_ID_DEV=dev-abc123-def456
XANO_DATABASE_ID_PROD=prod-xyz789-uvw012
```

### Configuration File Example

```javascript
// config/database.js
const databaseConfig = {
  development: {
    database_id: process.env.XANO_DATABASE_ID_DEV,
    api_url: process.env.XANO_API_BASE_URL_DEV,
    timeout: 5000,
    retry_attempts: 3
  },
  
  staging: {
    database_id: process.env.XANO_DATABASE_ID_STAGING,
    api_url: process.env.XANO_API_BASE_URL_STAGING,
    timeout: 10000,
    retry_attempts: 2
  },
  
  production: {
    database_id: process.env.XANO_DATABASE_ID_PROD,
    api_url: process.env.XANO_API_BASE_URL_PROD,
    timeout: 15000,
    retry_attempts: 1
  }
};

const getCurrentConfig = () => {
  const environment = process.env.NODE_ENV || 'development';
  return databaseConfig[environment];
};

module.exports = { getCurrentConfig, databaseConfig };
```

## No-Code Platform Integration

### 🔗 **n8n Integration Setup**

```javascript
// n8n Xano node configuration
{
  "name": "Xano",
  "type": "xano",
  "typeVersion": 1,
  "position": [250, 300],
  "parameters": {
    "authentication": "apiKey",
    "resource": "database",
    "operation": "query",
    "databaseId": "abc123-def456-ghi789",
    "instanceUrl": "https://your-instance.xano.io",
    "apiKey": "={{$node[\"Set Credentials\"].json[\"xano_api_key\"]}}"
  }
}

// n8n workflow for database connection testing
function testXanoConnection($input) {
  const config = {
    database_id: $input.credentials.database_id,
    api_url: $input.credentials.api_url,
    api_key: $input.credentials.api_key
  };
  
  // Test connection with simple query
  try {
    const testResponse = fetch(`${config.api_url}/health`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${config.api_key}`,
        'X-Database-ID': config.database_id
      }
    });
    
    return {
      success: true,
      database_id: config.database_id,
      connection_status: 'active',
      timestamp: new Date().toISOString()
    };
  } catch (error) {
    return {
      success: false,
      error: error.message,
      database_id: config.database_id
    };
  }
}
```

### 🌐 **WeWeb Integration**

```javascript
// WeWeb Xano data source configuration
class WeWebXanoConfig {
  static setupDataSource() {
    // Configure Xano as data source
    wwLib.datasources.add({
      name: 'xano_primary',
      type: 'api',
      config: {
        baseUrl: wwLib.envVars.XANO_API_BASE_URL,
        headers: {
          'Authorization': 'Bearer ' + wwLib.envVars.XANO_API_KEY,
          'X-Database-ID': wwLib.envVars.XANO_DATABASE_ID,
          'Content-Type': 'application/json'
        },
        timeout: 10000
      }
    });
  }
  
  static async testConnection() {
    try {
      const response = await wwLib.api.get({
        url: `${wwLib.envVars.XANO_API_BASE_URL}/health`,
        headers: {
          'Authorization': 'Bearer ' + wwLib.envVars.XANO_API_KEY,
          'X-Database-ID': wwLib.envVars.XANO_DATABASE_ID
        }
      });
      
      if (response.data) {
        wwLib.showAlert('Xano connection successful!', 'success');
        wwLib.variables.xanoConnectionStatus = 'connected';
        return true;
      }
    } catch (error) {
      console.error('Xano connection failed:', error);
      wwLib.showAlert('Failed to connect to Xano database', 'error');
      wwLib.variables.xanoConnectionStatus = 'disconnected';
      return false;
    }
  }
  
  static getConnectionInfo() {
    return {
      database_id: wwLib.envVars.XANO_DATABASE_ID,
      api_url: wwLib.envVars.XANO_API_BASE_URL,
      status: wwLib.variables.xanoConnectionStatus || 'unknown',
      last_check: wwLib.variables.lastConnectionCheck
    };
  }
}
```

### 🔧 **Make.com Integration**

```javascript
// Make.com Xano module configuration
{
  "connection": {
    "name": "Xano Primary Database",
    "type": "xano",
    "parameters": {
      "database_id": "abc123-def456-ghi789",
      "instance_url": "https://your-instance.xano.io",
      "api_key": "your-api-key-here",
      "region": "us-east-1"
    }
  },
  "scenario": {
    "name": "Sync Data to Xano",
    "modules": [
      {
        "name": "Watch for New Data",
        "type": "trigger"
      },
      {
        "name": "Process Data",
        "type": "transformer"
      },
      {
        "name": "Create Xano Record",
        "type": "xano",
        "operation": "addRecord",
        "parameters": {
          "table": "contacts",
          "data": "{{processed_data}}"
        }
      }
    ]
  }
}

// Make.com webhook processor
function processMakeWebhook(webhookData) {
  const xanoConfig = {
    database_id: webhookData.connection.database_id,
    api_url: webhookData.connection.instance_url + '/api:' + webhookData.connection.database_id,
    headers: {
      'Authorization': 'Bearer ' + webhookData.connection.api_key,
      'X-Database-ID': webhookData.connection.database_id
    }
  };
  
  return {
    success: true,
    config: xanoConfig,
    ready_for_operations: true
  };
}
```

## Security Best Practices

### API Key Management

```javascript
// Secure API key handling
class XanoSecurityManager {
  static validateDatabaseId(databaseId) {
    // Validate format (UUID-like structure)
    const idPattern = /^[a-zA-Z0-9]{6,8}-[a-zA-Z0-9]{6,8}-[a-zA-Z0-9]{6,8}$/;
    
    if (!idPattern.test(databaseId)) {
      throw new Error('Invalid database identifier format');
    }
    
    return true;
  }
  
  static createSecureConnection(config) {
    // Validate all required parameters
    const required = ['database_id', 'api_url', 'api_key'];
    const missing = required.filter(field => !config[field]);
    
    if (missing.length > 0) {
      throw new Error(`Missing required config: ${missing.join(', ')}`);
    }
    
    // Validate database ID format
    this.validateDatabaseId(config.database_id);
    
    // Create secure headers
    return {
      'Authorization': `Bearer ${config.api_key}`,
      'X-Database-ID': config.database_id,
      'X-Request-Origin': 'external-integration',
      'Content-Type': 'application/json'
    };
  }
  
  static rotateApiKey(oldKey, newKey) {
    // Key rotation process
    console.log('Rotating API key...');
    
    // Update environment variables
    process.env.XANO_API_KEY = newKey;
    
    // Test new key
    return this.testConnection({ api_key: newKey });
  }
  
  static async testConnection(config) {
    try {
      const headers = this.createSecureConnection(config);
      
      const response = await fetch(`${config.api_url}/health`, {
        method: 'GET',
        headers: headers
      });
      
      return response.ok;
    } catch (error) {
      console.error('Connection test failed:', error);
      return false;
    }
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Set up basic database connection:
1. Locate your database identifier in Xano dashboard
2. Set up environment variables
3. Test connection with simple API call
4. Document your configuration

### Intermediate Challenge
Configure multi-environment setup:
1. Set up development, staging, and production identifiers
2. Create configuration management system
3. Implement connection testing utilities
4. Add error handling and retries

### Advanced Challenge
Build secure integration framework:
1. Create comprehensive security layer
2. Implement API key rotation system
3. Add connection monitoring and alerting
4. Build integration testing suite

## Common Mistakes to Avoid

1. **Hardcoding identifiers** - Always use environment variables
2. **Mixing environments** - Keep dev/staging/production separate
3. **Ignoring security** - Properly manage API keys and access
4. **No connection testing** - Always verify connections work
5. **Missing error handling** - Plan for connection failures

## Best Practices

1. **Use environment variables** - Never hardcode identifiers
2. **Test connections regularly** - Implement health checks
3. **Secure API keys** - Rotate keys periodically
4. **Document configurations** - Maintain clear setup guides
5. **Monitor usage** - Track API calls and performance
6. **Plan for scale** - Design for multiple environments

## Next Steps

- Learn [External Database Query](external_database_query.md) for external connections
- Master [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for complex operations
- Explore [Get Database Schema](get_database_schema.md) for dynamic operations
- Understand [API Authentication](../authentication/) for secure access

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Configuration discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Setup guides
- 📖 [Integration Examples](../integrations/) - Platform-specific guides
- 🔧 [Support](https://xano.com/support) - Configuration assistance