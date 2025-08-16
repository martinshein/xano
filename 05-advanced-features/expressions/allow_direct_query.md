---
title: Allow Direct Query - Security Policy and Database Access Control
description: Complete guide to configuring Direct Query security policy in Xano, including when to enable/disable, security implications, and best practices for no-code platforms
category: expressions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - advanced_back_end_features.md
  - __when_to_convert_to_standard_sql_format___.md
  - configuring-expressions.md
subcategory: 05-advanced-features/expressions
tags:
  - security-policy
  - direct-query
  - database-security
  - access-control
  - enterprise-features
  - no-code
---

## 📋 **Quick Summary**

The Allow Direct Query security policy controls whether Direct Database Query functions can be used in your Xano function stacks. This enterprise security feature helps prevent unauthorized database access and ensures team members can only perform approved operations, making it essential for secure no-code applications with n8n, WeWeb, and other platforms.

## What You'll Learn

- Understanding Direct Query security policy and its implications
- When to enable or disable Direct Query functionality
- Security best practices for database access control
- Implementation strategies for team-based access control
- Integration patterns for secure no-code development
- Monitoring and audit capabilities for database operations

# Allow Direct Query Security Policy

## Overview

**Allow Direct Query** is a critical security policy setting in Xano that determines whether team members can execute Direct Database Query functions within their function stacks. This policy provides enterprise-level control over database access, preventing potentially dangerous SQL operations while maintaining necessary functionality for authorized users.

### Policy Impact

**When Enabled (Default):**
- Team members can use Direct Database Query functions
- Custom SQL queries can be executed against the database
- Advanced database operations are available
- Greater flexibility for complex data operations

**When Disabled:**
- Direct Database Query function is blocked
- Team members limited to standard Xano database functions
- Enhanced security against SQL injection and unauthorized access
- Reduced risk of accidental data manipulation

## 🔐 **Security Implications and Use Cases**

### Why Disable Direct Query?

**Security Concerns:**
- **SQL Injection Protection**: Prevents malicious or accidental SQL injection attacks
- **Data Integrity**: Limits ability to bypass Xano's built-in data validation
- **Access Control**: Ensures all database operations go through Xano's permission system
- **Audit Trail**: Maintains comprehensive logging of all database operations

**Team Management:**
- **Role Separation**: Limit advanced database access to senior developers only
- **Training Requirements**: Prevent junior team members from executing dangerous queries
- **Compliance**: Meet enterprise security requirements and regulations
- **Risk Mitigation**: Reduce chances of accidental data deletion or corruption

### When to Keep Direct Query Enabled

**Development Requirements:**
- **Complex Analytics**: Need for advanced reporting and data analysis
- **Data Migration**: Bulk data operations and schema modifications
- **Custom Integrations**: Third-party tool integration requiring direct SQL access
- **Performance Optimization**: Custom query optimization for specific use cases

### n8n Integration with Direct Query Security

```javascript
// n8n workflow for secure database operations with policy checking
{
  "nodes": [
    {
      "name": "Check Direct Query Policy",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/security/policies/direct-query",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json"
        }
      }
    },
    {
      "name": "Validate Query Permission",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const policyStatus = $input.first().json;
          const userRole = $env.USER_ROLE;
          const queryType = $env.QUERY_TYPE;
          
          // Define allowed operations based on policy and user role
          const allowedOperations = {
            admin: ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'DROP'],
            developer: ['SELECT', 'INSERT', 'UPDATE'],
            analyst: ['SELECT'],
            viewer: []
          };
          
          const userPermissions = allowedOperations[userRole] || [];
          const isDirectQueryEnabled = policyStatus.enabled;
          
          // Check if operation is allowed
          const isAllowed = isDirectQueryEnabled && 
            userPermissions.includes(queryType.toUpperCase());
          
          if (!isAllowed) {
            throw new Error(
              \`Operation denied: \${queryType} not allowed for role \${userRole} with current policy\`
            );
          }
          
          return [{
            json: {
              allowed: true,
              user_role: userRole,
              query_type: queryType,
              policy_enabled: isDirectQueryEnabled,
              timestamp: new Date().toISOString()
            }
          }];
        `
      }
    },
    {
      "name": "Execute Secure Query",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/secure-query",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json",
          "X-User-Role": "{{ $json.user_role }}",
          "X-Query-Type": "{{ $json.query_type }}"
        },
        "body": {
          "query": "{{ $env.SQL_QUERY }}",
          "parameters": "{{ $env.QUERY_PARAMS }}",
          "audit_info": {
            "user_id": "{{ $env.USER_ID }}",
            "workflow_id": "{{ $workflow.id }}",
            "execution_id": "{{ $execution.id }}"
          }
        }
      }
    },
    {
      "name": "Log Database Operation",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.AUDIT_LOG_ENDPOINT }}",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.AUDIT_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "event_type": "database_query",
          "user_id": "{{ $env.USER_ID }}",
          "query_type": "{{ $json.query_type }}",
          "success": "{{ $json.success }}",
          "timestamp": "{{ $json.timestamp }}",
          "source": "n8n_workflow"
        }
      }
    }
  ]
}
```

### WeWeb Secure Query Interface

```javascript
// WeWeb component for secure database query execution
class SecureQueryInterface {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.userRole = wwLib.wwVariable.getValue('user_role');
    this.directQueryEnabled = false;
  }
  
  async checkDirectQueryPolicy() {
    try {
      const response = await fetch(`${this.baseUrl}/api/security/policies/direct-query`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        }
      });
      
      const policy = await response.json();
      this.directQueryEnabled = policy.enabled;
      
      wwLib.wwVariable.updateValue('direct_query_enabled', policy.enabled);
      wwLib.wwVariable.updateValue('query_permissions', this.getQueryPermissions());
      
      return policy;
    } catch (error) {
      console.error('Failed to check direct query policy:', error);
      return { enabled: false, error: error.message };
    }
  }
  
  getQueryPermissions() {
    const rolePermissions = {
      admin: {
        canExecuteSQL: true,
        allowedOperations: ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'DROP'],
        restrictedTables: [],
        maxQueryTimeout: 60000
      },
      developer: {
        canExecuteSQL: true,
        allowedOperations: ['SELECT', 'INSERT', 'UPDATE'],
        restrictedTables: ['system_logs', 'user_credentials'],
        maxQueryTimeout: 30000
      },
      analyst: {
        canExecuteSQL: true,
        allowedOperations: ['SELECT'],
        restrictedTables: ['user_credentials', 'payment_methods'],
        maxQueryTimeout: 15000
      },
      viewer: {
        canExecuteSQL: false,
        allowedOperations: [],
        restrictedTables: ['*'],
        maxQueryTimeout: 0
      }
    };
    
    return rolePermissions[this.userRole] || rolePermissions.viewer;
  }
  
  async executeSecureQuery(queryConfig) {
    try {
      // Check policy status first
      await this.checkDirectQueryPolicy();
      
      const permissions = this.getQueryPermissions();
      
      // Validate user permissions
      if (!permissions.canExecuteSQL || !this.directQueryEnabled) {
        throw new Error('Direct query execution not allowed for your role or disabled by policy');
      }
      
      // Validate query type
      const queryType = this.detectQueryType(queryConfig.query);
      if (!permissions.allowedOperations.includes(queryType)) {
        throw new Error(`Query type '${queryType}' not allowed for role '${this.userRole}'`);
      }
      
      // Check for restricted tables
      const affectedTables = this.extractTableNames(queryConfig.query);
      const restrictedTableFound = affectedTables.some(table => 
        permissions.restrictedTables.includes(table) || 
        permissions.restrictedTables.includes('*')
      );
      
      if (restrictedTableFound) {
        throw new Error('Query affects restricted tables');
      }
      
      // Execute query with proper audit trail
      const response = await fetch(`${this.baseUrl}/api/direct-query`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json',
          'X-User-Role': this.userRole,
          'X-Query-Type': queryType
        },
        body: JSON.stringify({
          ...queryConfig,
          audit_info: {
            user_id: wwLib.wwVariable.getValue('current_user_id'),
            timestamp: new Date().toISOString(),
            source: 'weweb_interface'
          },
          timeout: permissions.maxQueryTimeout
        })
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('last_query_result', result.data);
        wwLib.wwVariable.updateValue('query_execution_time', result.execution_time);
        wwLib.wwUtils.showSuccessToast('Query executed successfully');
        
        // Log successful execution
        this.logQueryExecution(queryConfig, result, 'success');
      } else {
        throw new Error(result.error);
      }
      
      return result;
    } catch (error) {
      console.error('Query execution failed:', error);
      wwLib.wwUtils.showErrorToast(`Query failed: ${error.message}`);
      
      // Log failed execution
      this.logQueryExecution(queryConfig, null, 'error', error.message);
      
      return { success: false, error: error.message };
    }
  }
  
  detectQueryType(query) {
    const normalizedQuery = query.trim().toUpperCase();
    
    if (normalizedQuery.startsWith('SELECT')) return 'SELECT';
    if (normalizedQuery.startsWith('INSERT')) return 'INSERT';
    if (normalizedQuery.startsWith('UPDATE')) return 'UPDATE';
    if (normalizedQuery.startsWith('DELETE')) return 'DELETE';
    if (normalizedQuery.startsWith('CREATE')) return 'CREATE';
    if (normalizedQuery.startsWith('DROP')) return 'DROP';
    if (normalizedQuery.startsWith('ALTER')) return 'ALTER';
    
    return 'UNKNOWN';
  }
  
  extractTableNames(query) {
    // Simple table name extraction (in production, use a proper SQL parser)
    const tables = [];
    const patterns = [
      /FROM\s+(\w+)/gi,
      /JOIN\s+(\w+)/gi,
      /UPDATE\s+(\w+)/gi,
      /INSERT\s+INTO\s+(\w+)/gi,
      /DELETE\s+FROM\s+(\w+)/gi
    ];
    
    patterns.forEach(pattern => {
      let match;
      while ((match = pattern.exec(query)) !== null) {
        tables.push(match[1].toLowerCase());
      }
    });
    
    return [...new Set(tables)]; // Remove duplicates
  }
  
  async logQueryExecution(queryConfig, result, status, error = null) {
    try {
      await fetch(`${this.baseUrl}/api/audit/query-log`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          user_id: wwLib.wwVariable.getValue('current_user_id'),
          user_role: this.userRole,
          query: queryConfig.query,
          query_type: this.detectQueryType(queryConfig.query),
          affected_tables: this.extractTableNames(queryConfig.query),
          status: status,
          error_message: error,
          execution_time: result?.execution_time || null,
          rows_affected: result?.rows_affected || null,
          timestamp: new Date().toISOString(),
          source: 'weweb_secure_interface'
        })
      });
    } catch (logError) {
      console.error('Failed to log query execution:', logError);
    }
  }
  
  async buildSafeQuery(queryBuilder) {
    // Helper method to build parameterized queries safely
    const { table, operation, filters, data, limit } = queryBuilder;
    
    let query;
    const params = [];
    
    switch (operation.toUpperCase()) {
      case 'SELECT':
        query = `SELECT * FROM ${table}`;
        if (filters && Object.keys(filters).length > 0) {
          const conditions = Object.keys(filters).map((key, index) => {
            params.push(filters[key]);
            return `${key} = $${index + 1}`;
          });
          query += ` WHERE ${conditions.join(' AND ')}`;
        }
        if (limit) {
          query += ` LIMIT ${parseInt(limit)}`;
        }
        break;
        
      case 'INSERT':
        const columns = Object.keys(data).join(', ');
        const placeholders = Object.keys(data).map((_, index) => `$${index + 1}`).join(', ');
        params.push(...Object.values(data));
        query = `INSERT INTO ${table} (${columns}) VALUES (${placeholders})`;
        break;
        
      case 'UPDATE':
        const setClauses = Object.keys(data).map((key, index) => {
          params.push(data[key]);
          return `${key} = $${index + 1}`;
        });
        query = `UPDATE ${table} SET ${setClauses.join(', ')}`;
        
        if (filters && Object.keys(filters).length > 0) {
          const conditions = Object.keys(filters).map((key, index) => {
            params.push(filters[key]);
            return `${key} = $${params.length}`;
          });
          query += ` WHERE ${conditions.join(' AND ')}`;
        }
        break;
        
      default:
        throw new Error(`Unsupported operation: ${operation}`);
    }
    
    return { query, params };
  }
}

// Initialize secure query interface
const secureQuery = new SecureQueryInterface(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function checkQueryPermissions() {
  await secureQuery.checkDirectQueryPolicy();
}

async function executeUserQuery() {
  const queryConfig = {
    query: wwLib.wwVariable.getValue('user_query'),
    parameters: wwLib.wwVariable.getValue('query_parameters') || []
  };
  
  await secureQuery.executeSecureQuery(queryConfig);
}

async function buildAndExecuteSafeQuery() {
  const queryBuilder = {
    table: wwLib.wwVariable.getValue('target_table'),
    operation: wwLib.wwVariable.getValue('query_operation'),
    filters: wwLib.wwVariable.getValue('query_filters'),
    data: wwLib.wwVariable.getValue('query_data'),
    limit: wwLib.wwVariable.getValue('query_limit')
  };
  
  const { query, params } = await secureQuery.buildSafeQuery(queryBuilder);
  await secureQuery.executeSecureQuery({ query, parameters: params });
}
```

## ⚙️ **Policy Configuration and Management**

### Accessing Security Policy Settings

**Navigation Path:**
1. Go to instance selection screen
2. Click the settings icon (⚙️) next to your instance
3. Choose "Security Policy" from the panel
4. Locate "Allow Direct Query" setting

**Policy Levels:**
- **Enabled**: Direct Database Query functions are available to all team members
- **Disabled**: Direct Database Query functions are blocked for all team members
- **Role-Based**: Custom implementation with function stack validation

### Enterprise Policy Implementation

```javascript
// Custom role-based direct query validation function stack
[
  {
    "function": "get_user_role",
    "user_id": "{{ auth.user.id }}",
    "return_as": "user_role"
  },
  {
    "function": "get_security_policy",
    "policy_name": "allow_direct_query",
    "return_as": "direct_query_policy"
  },
  {
    "function": "conditional",
    "condition": "{{ !direct_query_policy.enabled }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 403,
        "body": {
          "error": "Direct query execution disabled by security policy",
          "code": "DIRECT_QUERY_DISABLED"
        }
      }
    ]
  },
  {
    "function": "create_variable",
    "name": "role_permissions",
    "value": {
      "admin": ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP"],
      "developer": ["SELECT", "INSERT", "UPDATE"],
      "analyst": ["SELECT"],
      "viewer": []
    }
  },
  {
    "function": "conditional",
    "condition": "{{ !role_permissions[user_role.name] }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 403,
        "body": {
          "error": "Direct query not allowed for your role",
          "code": "INSUFFICIENT_PERMISSIONS"
        }
      }
    ]
  },
  {
    "function": "validate_query_type",
    "query": "{{ request.body.query }}",
    "allowed_operations": "{{ role_permissions[user_role.name] }}",
    "return_as": "query_validation"
  },
  {
    "function": "conditional",
    "condition": "{{ !query_validation.allowed }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 403,
        "body": {
          "error": "Query type not allowed for your role",
          "query_type": "{{ query_validation.detected_type }}",
          "allowed_types": "{{ role_permissions[user_role.name] }}",
          "code": "QUERY_TYPE_FORBIDDEN"
        }
      }
    ]
  },
  {
    "function": "log_security_event",
    "event_type": "direct_query_attempt",
    "data": {
      "user_id": "{{ auth.user.id }}",
      "user_role": "{{ user_role.name }}",
      "query_type": "{{ query_validation.detected_type }}",
      "allowed": "{{ query_validation.allowed }}",
      "timestamp": "{{ now }}"
    }
  }
]
```

## 📊 **Monitoring and Audit**

### Query Execution Monitoring

**Audit Trail Components:**
- **User Identification**: Track who executed each query
- **Query Content**: Log the actual SQL statements
- **Execution Results**: Record success/failure and affected rows
- **Timing Information**: Monitor query execution times
- **Security Events**: Track policy violations and access attempts

**Monitoring Dashboard Function Stack:**
```javascript
// Query audit dashboard
[
  {
    "function": "query_all_records",
    "table": "query_audit_log",
    "filter": {
      "timestamp": {"$gte": "{{ now - 86400 }}"}
    },
    "sort": "timestamp desc",
    "limit": 100,
    "return_as": "recent_queries"
  },
  {
    "function": "create_variable",
    "name": "audit_summary",
    "value": {
      "total_queries": "{{ recent_queries|length }}",
      "successful_queries": "{{ recent_queries|select(attribute='status', operator='==', value='success')|length }}",
      "failed_queries": "{{ recent_queries|select(attribute='status', operator='==', value='error')|length }}",
      "policy_violations": "{{ recent_queries|select(attribute='violation_type', operator='!=', value=null)|length }}",
      "unique_users": "{{ recent_queries|map(attribute='user_id')|unique|length }}"
    }
  },
  {
    "function": "query_all_records",
    "table": "query_audit_log",
    "filter": {
      "violation_type": {"$ne": null},
      "timestamp": {"$gte": "{{ now - 86400 }}"}
    },
    "return_as": "security_violations"
  },
  {
    "function": "conditional",
    "condition": "{{ security_violations|length > 0 }}",
    "true_branch": [
      {
        "function": "alert_security_team",
        "alert_type": "direct_query_violations",
        "data": {
          "violation_count": "{{ security_violations|length }}",
          "violations": "{{ security_violations }}",
          "summary": "{{ audit_summary }}"
        }
      }
    ]
  }
]
```

## 💡 **Pro Tips**

- **Start Restrictive**: Begin with Direct Query disabled and enable only when necessary
- **Role-Based Access**: Implement custom role validation even when policy is enabled
- **Query Validation**: Always validate and sanitize direct queries before execution
- **Audit Everything**: Maintain comprehensive logs of all direct query activities
- **Regular Reviews**: Periodically review query audit logs for suspicious activity
- **Team Training**: Ensure team members understand the security implications of direct queries

## 🔧 **Troubleshooting**

### Common Direct Query Policy Issues

**Problem**: Team members can't execute necessary database operations  
**Solution**: Review if operations can be accomplished with standard Xano functions; if not, enable policy with role-based restrictions

**Problem**: Security violations appearing in audit logs  
**Solution**: Investigate unauthorized access attempts; consider implementing stricter role-based controls

**Problem**: Performance issues with query validation  
**Solution**: Optimize custom validation function stacks; consider caching role permissions

**Problem**: Policy changes not taking effect immediately  
**Solution**: Verify policy configuration; restart function stacks if necessary

---

**Next Steps**: Ready to implement secure database access? Explore [Advanced Backend Features](advanced_back_end_features.md) for comprehensive security or check [Database Table Formats](__when_to_convert_to_standard_sql_format___.md) for optimization strategies