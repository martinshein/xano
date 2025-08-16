---
title: Accessing Xano MCP Server - Instance Configuration Guide
description: Step-by-step guide to accessing the Xano MCP Server through your instance settings, configuring access tokens, and choosing the right connection method for your AI client setup
category: ai-services
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - xano-mcp-server.md
  - connecting-clients.md
  - mcp-builder.md
subcategory: 04-integrations/ai-services
tags:
  - instance-settings
  - metadata-api
  - mcp-server-access
  - configuration
  - setup
  - no-code
---

## 📋 **Quick Summary**

This guide shows you how to access the Xano MCP Server from your instance settings. The MCP Server provides direct AI client access to your Xano instance, enabling automated database management, API exploration, and data operations through AI tools like Claude Desktop, Cursor, and Windsurf. Essential first step for setting up AI-powered workflows.

## What You'll Learn

- How to access MCP Server settings from your instance
- Understanding the ⚙️ settings icon and navigation
- Difference between Metadata API and MCP Server options
- When to use the built-in MCP Server vs custom tools
- Security considerations for instance-level access
- Integration with popular AI development tools

# Accessing Xano MCP Server Settings

## Overview

The **Xano MCP Server** is accessed through your instance settings and provides comprehensive access to your entire Xano instance through AI clients. Unlike custom MCP tools you build, this server gives AI direct access to administrative functions, database management, and API exploration capabilities.

### What You Get Access To

**Instance Management:**
- Workspace creation and configuration
- Database schema management
- Table creation and modification
- API endpoint documentation
- Request history analysis

**Direct AI Capabilities:**
- Natural language database queries
- Automated table creation
- Data analysis and reporting
- API testing and documentation
- Performance monitoring

## 🚀 **Step-by-Step Access Guide**

### Step 1: Navigate to Instance Settings

1. **Open Xano Dashboard**: Log into your Xano account and view your instances
2. **Locate Your Instance**: Find the instance you want to connect to AI clients
3. **Click Settings Icon**: Click the **⚙️** icon next to your instance name

### Step 2: Choose Metadata API & MCP Server

1. **Settings Menu Opens**: A dropdown menu will appear with various options
2. **Select MCP Option**: Choose **"Metadata API & MCP Server"**
3. **Access Configuration**: You'll be taken to the MCP server configuration screen

### Step 3: Understanding Your Options

**What You'll See:**
- **Access Token Generation**: Create authentication tokens for AI clients
- **Connection URLs**: Pre-configured endpoints for different connection types
- **Available Tools**: List of built-in tools your AI clients can use
- **Usage Monitoring**: Track how AI clients interact with your instance

## 🔗 **No-Code Platform Integration**

### n8n Workflow for Instance Management

**Automated Instance Monitoring:**

```javascript
// n8n HTTP Request node for instance health checks
{
  "method": "GET",
  "url": "https://your-xano-instance.com/api/mcp/health",
  "headers": {
    "Authorization": "Bearer {{ $json.mcp_token }}",
    "Content-Type": "application/json"
  },
  "schedule": "0 */6 * * *"  // Every 6 hours
}
```

### WeWeb Admin Dashboard Integration

**Instance Management Component:**

```javascript
// WeWeb component for instance administration
class XanoInstanceManager {
  constructor(instanceUrl, mcpToken) {
    this.instanceUrl = instanceUrl;
    this.mcpToken = mcpToken;
  }
  
  async getInstanceStatus() {
    try {
      const response = await fetch(`${this.instanceUrl}/api/mcp/status`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.mcpToken}`,
          'Content-Type': 'application/json'
        }
      });
      
      const status = await response.json();
      
      // Update WeWeb variables
      wwLib.wwVariable.updateValue('instance_status', status);
      wwLib.wwVariable.updateValue('last_health_check', new Date().toISOString());
      
      return status;
    } catch (error) {
      console.error('Instance status check failed:', error);
      return { error: 'Status unavailable' };
    }
  }
  
  async monitorWorkspaces() {
    try {
      const response = await fetch(`${this.instanceUrl}/api/mcp/sse`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.mcpToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          tool: 'listWorkspaces',
          args: {}
        })
      });
      
      const workspaces = await response.json();
      
      // Update workspace monitoring dashboard
      wwLib.wwVariable.updateValue('workspace_list', workspaces);
      
      return workspaces;
    } catch (error) {
      console.error('Workspace monitoring failed:', error);
      return [];
    }
  }
}

// Usage in WeWeb
const instanceManager = new XanoInstanceManager(
  wwLib.wwVariable.getValue('xano_instance_url'),
  wwLib.wwVariable.getValue('mcp_access_token')
);

async function performHealthCheck() {
  const status = await instanceManager.getInstanceStatus();
  
  if (status.error) {
    wwLib.wwModal.open('instance-error-modal');
  } else {
    wwLib.wwVariable.updateValue('health_status', 'healthy');
  }
}
```

## 🛠️ **Understanding the Settings Interface**

### Instance Settings Navigation

**Location in Xano Interface:**
- **Instance List View**: Shows all your instances with settings icons
- **Settings Icon (⚙️)**: Located to the right of each instance name
- **Dropdown Menu**: Contains multiple configuration options

### Settings Menu Options

| Option | Purpose | When to Use |
|--------|---------|-------------|
| **General Settings** | Basic instance configuration | Changing instance name, description |
| **Metadata API & MCP Server** | AI client integration | Setting up AI tools and automation |
| **Security Settings** | Access control and permissions | Managing API keys and user access |
| **Backup & Restore** | Data protection | Regular maintenance and recovery |

### MCP Server vs Other Options

**Choose MCP Server When:**
- Building AI-powered applications
- Need automated database management
- Want natural language interface to your data
- Integrating with AI development tools

**Choose Other Options When:**
- Traditional API development
- Manual database administration
- Standard web application integration
- Non-AI workflow automation

## 🔐 **Security Considerations**

### Access Control Best Practices

1. **Token Management**: Generate tokens with appropriate scopes
2. **Environment Separation**: Use different tokens for development/production
3. **Regular Rotation**: Update access tokens periodically
4. **Audit Monitoring**: Track all MCP server access

### Instance-Level Security

```javascript
// Example of secure token configuration
{
  "token_scope": {
    "read": ["workspaces", "tables", "content"],
    "write": ["content"],
    "admin": []  // Restrict administrative functions
  },
  "rate_limits": {
    "requests_per_minute": 100,
    "burst_limit": 20
  },
  "allowed_clients": [
    "claude-desktop",
    "cursor-ide",
    "custom-client-1"
  ]
}
```

### Common Security Issues

**Problem**: Overly broad token permissions  
**Solution**: Use principle of least privilege - grant only necessary permissions

**Problem**: Shared tokens across environments  
**Solution**: Generate separate tokens for development, staging, and production

**Problem**: No audit trail for AI operations  
**Solution**: Enable request logging and monitor MCP tool usage

## 💡 **Pro Tips**

### Efficient Setup Workflow

1. **Start Simple**: Begin with read-only access to test connectivity
2. **Test Incremental**: Add permissions gradually as needed
3. **Document Everything**: Keep track of token purposes and scopes
4. **Monitor Usage**: Watch for unexpected AI client behavior

### Common Configuration Patterns

**Development Setup:**
```json
{
  "environment": "development",
  "permissions": ["read", "write"],
  "rate_limit": "relaxed",
  "logging": "verbose"
}
```

**Production Setup:**
```json
{
  "environment": "production", 
  "permissions": ["read"],
  "rate_limit": "strict",
  "logging": "errors_only",
  "backup_frequency": "daily"
}
```

## 🔧 **Troubleshooting Access Issues**

### Common Problems

**Problem**: Can't find the ⚙️ settings icon  
**Solution**: Ensure you're viewing the instance list and have appropriate permissions

**Problem**: Settings menu doesn't show MCP Server option  
**Solution**: Verify your account plan includes MCP features

**Problem**: Access denied when opening settings  
**Solution**: Check if you're the instance owner or have admin permissions

### Permission Requirements

**Required Roles:**
- **Instance Owner**: Full access to all settings
- **Admin**: Can configure MCP settings
- **Developer**: Can view but not modify MCP configuration
- **Viewer**: No access to instance settings

## 🎯 **Next Steps After Access**

### Immediate Actions

1. **Generate Access Token**: Create your first MCP authentication token
2. **Choose Connection Method**: Select SSE or streaming based on your needs
3. **Test Connection**: Verify connectivity with a simple AI client
4. **Configure First Tool**: Set up basic database access

### Integration Planning

1. **Identify Use Cases**: Determine which AI operations you need
2. **Plan Security**: Design token scoping and access controls
3. **Choose Clients**: Select AI tools that best fit your workflow
4. **Start Development**: Begin building AI-powered features

---

**Next Steps**: Ready to configure your MCP server? Check out [Xano MCP Server](xano-mcp-server.md) for detailed setup or explore [Connecting Clients](connecting-clients.md) for AI tool integration