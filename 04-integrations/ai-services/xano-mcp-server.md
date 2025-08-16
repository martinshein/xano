---
title: Xano MCP Server - Direct Instance Management with AI
description: Access and manage your Xano instance directly through MCP clients like Claude Desktop, Cursor, and other AI tools using the built-in MCP server
category: ai-services
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - mcp-builder.md
  - connecting-clients.md
  - mcp-functions.md
subcategory: 04-integrations/ai-services
tags:
  - xano-mcp-server
  - metadata-api
  - instance-management
  - ai-native
  - direct-access
  - no-code
---

## 📋 **Quick Summary**

The Xano MCP Server allows you to manage your Xano instance directly through any MCP client. Powered by the Metadata API, it enables AI tools to create tables, manage data, analyze request history, and perform administrative tasks without leaving your AI environment. Perfect for AI-assisted development workflows in Claude Desktop, Cursor, and other MCP-compatible tools.

## What You'll Learn

- How to connect to Xano's built-in MCP server
- Available tools for instance and workspace management
- Best practices for AI-assisted Xano development
- Security considerations for MCP access
- Integration patterns with popular AI clients
- Advanced automation workflows

# Xano MCP Server

## Overview

The **Xano MCP Server** is a built-in service that exposes your Xano instance capabilities through the Model Context Protocol. Unlike custom MCP servers you build with MCP Builder, this server provides direct access to Xano's administrative and development functions, enabling AI tools to help you manage your entire Xano instance.

### Key Capabilities

- **Instance Management**: Create and configure workspaces and branches
- **Database Administration**: Design tables, manage schemas, and manipulate data
- **API Development**: Access and analyze your API groups and endpoints
- **Request Analysis**: Search and analyze API request history
- **Security Management**: Configure access controls and permissions
- **Real-time Monitoring**: Access workspace and instance health information

### Powered by Metadata API

The Xano MCP Server leverages the [Metadata API](../xano-features/metadata-api/master-metadata-api.md) to provide comprehensive access to your Xano instance. This ensures that all operations are secure, audited, and consistent with Xano's built-in capabilities.

## 🚀 **Getting Started**

### Step 1: Access the MCP Server Settings

1. **Navigate to Instance Settings**: From your Xano dashboard, click the ⚙️ icon next to your instance
2. **Select MCP Server**: Choose **Metadata API & MCP Server**
3. **Review Capabilities**: Familiarize yourself with available tools and permissions

### Step 2: Generate Access Token

1. **Create Token**: Click **Generate Access Token**
2. **Set Permissions**: Configure appropriate scope for your use case:

| Permission Level | Capabilities | Best For |
|------------------|--------------|----------|
| **Read Only** | View data, schemas, and request history | Analysis and monitoring |
| **Read/Write** | Full data manipulation and table management | Development and maintenance |
| **Full Access** | Complete instance administration | Advanced automation |

3. **Save Token**: Store your token securely for client configuration

### Step 3: Choose Connection Method

**Server-Sent Events (SSE)** - Recommended for most clients
```
https://your-instance.xano.io/api/mcp/sse?token=your_access_token
```

**Streaming Connection** - For advanced clients
```
wss://your-instance.xano.io/api/mcp/stream?token=your_access_token
```

## 🔗 **No-Code Platform Integration**

### n8n Workflow with Xano MCP Server

**Automated Database Management:**

```javascript
// n8n HTTP Request node for Xano MCP Server
{
  "method": "POST",
  "url": "https://your-instance.xano.io/api/mcp/sse",
  "headers": {
    "Authorization": "Bearer {{ $json.access_token }}",
    "Content-Type": "application/json"
  },
  "body": {
    "tool": "addTable",
    "args": {
      "workspace_id": "{{ $json.workspace_id }}",
      "table_name": "{{ $json.new_table_name }}",
      "schema": {
        "name": {"type": "text", "required": true},
        "email": {"type": "text", "unique": true},
        "created_at": {"type": "datetime", "default": "now"}
      }
    }
  }
}
```

### WeWeb Integration

**AI-Powered Admin Dashboard:**

```javascript
// WeWeb component for Xano instance management
class XanoMCPManager {
  constructor(accessToken) {
    this.token = accessToken;
    this.baseUrl = 'https://your-instance.xano.io/api/mcp/sse';
  }
  
  async callMCPTool(toolName, args) {
    try {
      const response = await fetch(this.baseUrl, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          tool: toolName,
          args: args
        })
      });
      
      return await response.json();
    } catch (error) {
      console.error('MCP tool call failed:', error);
      throw new Error('Failed to execute Xano operation');
    }
  }
  
  // Workspace management
  async getWorkspaces() {
    return this.callMCPTool('listWorkspaces', {});
  }
  
  async analyzeRequestHistory(workspaceId, filters = {}) {
    return this.callMCPTool('searchRequestHistory', {
      workspace_id: workspaceId,
      ...filters
    });
  }
  
  // Table management
  async createTable(workspaceId, tableConfig) {
    return this.callMCPTool('addTable', {
      workspace_id: workspaceId,
      ...tableConfig
    });
  }
  
  async updateTableData(workspaceId, tableId, updates) {
    return this.callMCPTool('patchTableContentBulk', {
      workspace_id: workspaceId,
      table_id: tableId,
      updates: updates
    });
  }
}

// Usage in WeWeb
const xanoManager = new XanoMCPManager(wwLib.wwVariable.getValue('xano_mcp_token'));

async function setupNewCustomerWorkspace() {
  const workspaces = await xanoManager.getWorkspaces();
  const customerWorkspace = workspaces.find(w => w.name === 'customer-data');
  
  if (!customerWorkspace) {
    throw new Error('Customer workspace not found');
  }
  
  // Create tables with AI assistance
  await xanoManager.createTable(customerWorkspace.id, {
    name: 'customer_profiles',
    fields: {
      id: { type: 'integer', primary: true, auto_increment: true },
      name: { type: 'text', required: true },
      email: { type: 'text', unique: true, required: true },
      subscription_tier: { type: 'enum', options: ['free', 'pro', 'enterprise'] },
      created_at: { type: 'datetime', default: 'now' }
    }
  });
  
  wwLib.wwVariable.updateValue('workspace_setup_complete', true);
}
```

## 🛠️ **Available Tools Reference**

### Authentication Tools

#### `getLoggedInUser`
Validates access token and returns account details.

**Usage:**
```javascript
{
  "tool": "getLoggedInUser",
  "args": {}
}
```

**Response:**
```json
{
  "user_id": 12345,
  "email": "developer@company.com",
  "name": "John Developer",
  "permissions": ["read", "write", "admin"],
  "instance_access": ["production", "staging"]
}
```

### Workspace Management Tools

#### `listWorkspaces`
Lists all accessible workspaces.

```javascript
{
  "tool": "listWorkspaces",
  "args": {}
}
```

#### `getWorkspace`
Retrieves detailed workspace information.

```javascript
{
  "tool": "getWorkspace",
  "args": {
    "workspace_id": "ws_12345"
  }
}
```

#### `getWorkspaceBranches`
Lists all branches within a workspace.

```javascript
{
  "tool": "getWorkspaceBranches",
  "args": {
    "workspace_id": "ws_12345"
  }
}
```

### Table Management Tools

#### `addTable`
Creates a new table with specified schema.

```javascript
{
  "tool": "addTable",
  "args": {
    "workspace_id": "ws_12345",
    "name": "customer_analytics",
    "description": "Customer behavior and analytics data",
    "fields": {
      "id": {"type": "integer", "primary": true, "auto_increment": true},
      "customer_id": {"type": "integer", "required": true, "foreign_key": "customers.id"},
      "event_type": {"type": "enum", "options": ["login", "purchase", "view", "click"]},
      "event_data": {"type": "json"},
      "timestamp": {"type": "datetime", "default": "now"},
      "ip_address": {"type": "text"},
      "user_agent": {"type": "text"}
    }
  }
}
```

#### `getTables`
Lists all tables in a workspace.

```javascript
{
  "tool": "getTables",
  "args": {
    "workspace_id": "ws_12345"
  }
}
```

#### `updateTableMeta`
Modifies table schema and metadata.

```javascript
{
  "tool": "updateTableMeta",
  "args": {
    "workspace_id": "ws_12345",
    "table_id": "tbl_67890",
    "schema_updates": {
      "add_fields": {
        "last_updated": {"type": "datetime", "default": "now"}
      },
      "modify_fields": {
        "email": {"unique": true, "required": true}
      }
    }
  }
}
```

### Data Management Tools

#### `getTableContent`
Retrieves records with filtering and pagination.

```javascript
{
  "tool": "getTableContent",
  "args": {
    "workspace_id": "ws_12345",
    "table_id": "tbl_67890",
    "limit": 100,
    "offset": 0,
    "filters": {
      "status": "active",
      "created_at": ">2024-01-01"
    },
    "sort": [{"field": "created_at", "direction": "desc"}]
  }
}
```

#### `searchTableContent`
Advanced search with complex criteria.

```javascript
{
  "tool": "searchTableContent",
  "args": {
    "workspace_id": "ws_12345",
    "table_id": "tbl_67890",
    "query": {
      "and": [
        {"field": "subscription_tier", "operator": "in", "value": ["pro", "enterprise"]},
        {"field": "last_login", "operator": ">", "value": "2024-01-01"},
        {
          "or": [
            {"field": "region", "operator": "=", "value": "US"},
            {"field": "priority", "operator": "=", "value": "high"}
          ]
        }
      ]
    },
    "limit": 50
  }
}
```

#### `addTableContentBulk`
Bulk insert records for efficient data loading.

```javascript
{
  "tool": "addTableContentBulk",
  "args": {
    "workspace_id": "ws_12345",
    "table_id": "tbl_67890",
    "records": [
      {
        "name": "John Doe",
        "email": "john@example.com",
        "subscription_tier": "pro"
      },
      {
        "name": "Jane Smith", 
        "email": "jane@example.com",
        "subscription_tier": "enterprise"
      }
    ]
  }
}
```

### API Management Tools

#### `listAPIGroups`
Lists all API groups in workspace.

```javascript
{
  "tool": "listAPIGroups",
  "args": {
    "workspace_id": "ws_12345"
  }
}
```

#### `getApiGroupSwagger`
Returns OpenAPI/Swagger documentation.

```javascript
{
  "tool": "getApiGroupSwagger",
  "args": {
    "workspace_id": "ws_12345",
    "api_group_id": "ag_11111"
  }
}
```

### Request History Tools

#### `getRequestHistory`
Retrieves API request logs.

```javascript
{
  "tool": "getRequestHistory",
  "args": {
    "workspace_id": "ws_12345",
    "limit": 100,
    "start_date": "2024-01-01",
    "end_date": "2024-01-31"
  }
}
```

#### `searchRequestHistory`
Advanced request history analysis.

```javascript
{
  "tool": "searchRequestHistory",
  "args": {
    "workspace_id": "ws_12345",
    "filters": {
      "status_code": ">= 400",
      "endpoint": "contains /api/users",
      "response_time": "> 1000"
    },
    "sort": [{"field": "timestamp", "direction": "desc"}]
  }
}
```

## 🎯 **Practical Use Cases**

### Use Case 1: AI-Assisted Database Design

**Prompt to AI Client:**
"Analyze my customer data needs and create an optimized database schema for an e-commerce platform. Include proper relationships and indexing."

**AI Response with MCP Tools:**
```javascript
// AI will use these tools automatically
[
  {
    "tool": "listWorkspaces",
    "args": {}
  },
  {
    "tool": "addTable",
    "args": {
      "workspace_id": "ws_12345",
      "name": "customers",
      "fields": {
        "id": {"type": "integer", "primary": true, "auto_increment": true},
        "email": {"type": "text", "unique": true, "required": true},
        "first_name": {"type": "text", "required": true},
        "last_name": {"type": "text", "required": true},
        "created_at": {"type": "datetime", "default": "now"},
        "updated_at": {"type": "datetime", "default": "now", "on_update": "now"}
      }
    }
  }
  // AI continues creating related tables
]
```

### Use Case 2: Performance Monitoring and Analysis

**Prompt to AI Client:**
"Analyze my API performance from the last week and identify slow endpoints."

**AI Analysis:**
```javascript
// AI executes analysis automatically
{
  "tool": "searchRequestHistory",
  "args": {
    "workspace_id": "ws_12345",
    "filters": {
      "timestamp": ">= 2024-01-15",
      "response_time": "> 1000"
    },
    "sort": [{"field": "response_time", "direction": "desc"}],
    "limit": 100
  }
}
```

### Use Case 3: Data Migration and Cleanup

**Prompt to AI Client:**
"Clean up duplicate customer records and migrate old data format to the new schema."

**AI Migration Process:**
```javascript
[
  {
    "tool": "searchTableContent",
    "args": {
      "workspace_id": "ws_12345",
      "table_id": "customers",
      "query": {
        "group_by": "email",
        "having": "count(*) > 1"
      }
    }
  },
  {
    "tool": "patchTableContentBulk",
    "args": {
      "workspace_id": "ws_12345", 
      "table_id": "customers",
      "updates": [
        // AI-generated cleanup operations
      ]
    }
  }
]
```

## 🔐 **Security and Best Practices**

### Access Token Management

**Token Scoping:**
```javascript
// Recommended token configuration
{
  "permissions": {
    "read": ["workspaces", "tables", "content", "requests"],
    "write": ["content"],
    "admin": []  // Restrict admin access
  },
  "workspace_access": ["production"],  // Limit to specific workspaces
  "expiration": "30d"  // Set appropriate expiration
}
```

### Rate Limiting and Monitoring

```javascript
// Implement rate limiting for MCP operations
{
  "tool": "searchRequestHistory",
  "args": {
    "filters": {
      "user_agent": "contains MCP",
      "timestamp": ">= today"
    }
  }
}
```

### Audit Logging

All MCP server operations are logged through Xano's audit system:

- Tool execution logs
- Data modification tracking
- Access pattern monitoring
- Security event alerting

## 🔧 **Client Configuration Examples**

### Claude Desktop Configuration

```json
{
  "mcpServers": {
    "xano-instance": {
      "command": "curl",
      "args": [
        "-N",
        "-H", "Authorization: Bearer YOUR_ACCESS_TOKEN",
        "-H", "Accept: text/event-stream",
        "https://your-instance.xano.io/api/mcp/sse"
      ]
    }
  }
}
```

### Cursor IDE Configuration

```json
{
  "mcp.servers": {
    "xano": {
      "url": "https://your-instance.xano.io/api/mcp/sse",
      "headers": {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
      }
    }
  }
}
```

### Custom Client Integration

```javascript
// JavaScript MCP client for Xano
class XanoMCPClient {
  constructor(instanceUrl, accessToken) {
    this.instanceUrl = instanceUrl;
    this.accessToken = accessToken;
    this.connected = false;
  }
  
  async connect() {
    this.eventSource = new EventSource(
      `${this.instanceUrl}/api/mcp/sse?token=${this.accessToken}`
    );
    
    this.eventSource.onopen = () => {
      this.connected = true;
      console.log('Connected to Xano MCP Server');
    };
    
    this.eventSource.onmessage = (event) => {
      this.handleResponse(JSON.parse(event.data));
    };
  }
  
  async executeTool(toolName, args) {
    if (!this.connected) {
      await this.connect();
    }
    
    const response = await fetch(`${this.instanceUrl}/api/mcp/sse`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        tool: toolName,
        args: args
      })
    });
    
    return await response.json();
  }
}
```

## 💡 **Pro Tips**

- **Use Workspace Filtering**: Limit MCP access to specific workspaces for security
- **Monitor Token Usage**: Track MCP operations through request history
- **Implement Caching**: Cache frequently accessed data to reduce API calls
- **Batch Operations**: Use bulk tools for efficient data management
- **Error Handling**: Implement robust error handling for MCP operations
- **Documentation**: Keep MCP tool usage documented for team collaboration

## 🔍 **Troubleshooting**

### Common Issues

**Problem**: MCP client cannot connect to server  
**Solution**: Verify access token validity and network connectivity

**Problem**: Tool execution fails with permission error  
**Solution**: Check token permissions and workspace access rights

**Problem**: Large data operations timeout  
**Solution**: Use bulk operations and implement proper pagination

**Problem**: Request history search is slow  
**Solution**: Add specific date ranges and filters to narrow results

### Performance Optimization

1. **Use Specific Filters**: Always include date ranges and relevant filters
2. **Limit Result Sets**: Implement appropriate pagination limits
3. **Cache Results**: Store frequently accessed data locally
4. **Batch Operations**: Group multiple changes into single bulk operations

---

**Next Steps**: Ready to connect your AI client? Check out [Connecting Clients](connecting-clients.md) or explore [MCP Builder](mcp-builder.md) for creating custom tools