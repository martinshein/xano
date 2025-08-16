---
title: Connecting Clients to Xano MCP Servers - AI Tool Integration Guide
description: Complete setup guide for connecting popular AI clients like Cursor, Claude Desktop, and Windsurf to your Xano MCP servers for seamless AI-powered development
category: ai-services
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - mcp-builder.md
  - xano-mcp-server.md
  - mcp-functions.md
subcategory: 04-integrations/ai-services
tags:
  - client-configuration
  - cursor
  - claude-desktop
  - windsurf
  - mcp-setup
  - ai-tools
  - no-code
---

## 📋 **Quick Summary**

Learn how to connect popular AI clients to your Xano MCP servers for seamless integration. This guide covers setup for Cursor IDE, Claude Desktop, Windsurf, and custom clients, enabling you to use AI-powered development tools directly with your Xano backend. Perfect for building intelligent no-code workflows with automated database operations and API management.

## What You'll Learn

- How to configure popular AI clients for MCP integration
- Authentication setup for secure MCP connections
- Troubleshooting common connection issues
- Best practices for client configuration
- Advanced setup options for custom workflows
- Integration patterns for development teams

# Connecting Clients to Xano MCP Servers

## Overview

Once you've built MCP servers in Xano, you need to connect AI clients to access your tools. This guide covers the most popular AI clients and provides step-by-step configuration instructions for each platform.

### Supported Clients

| Client | Best For | Authentication | Platform Support |
|--------|----------|----------------|------------------|
| **Cursor IDE** | Code development and editing | Bearer tokens | macOS, Windows, Linux |
| **Claude Desktop** | General AI assistance | Bearer tokens | macOS, Windows |
| **Windsurf** | AI-powered development | Bearer tokens | Cross-platform |
| **Custom Clients** | Specialized integrations | Custom methods | Any platform |

### Connection Methods

**SSE (Server-Sent Events)** - Recommended for most clients
- More compatible with existing systems
- Simpler to implement
- Better for request-response patterns

**Streaming** - For real-time applications
- Enables chunked responses
- Better user experience for long operations
- Requires streaming support in client

## 🚀 **Client Setup Guides**

### 💻 **Cursor IDE Setup**

Cursor offers two setup methods: global configuration and per-project setup.

#### Option 1: Global Configuration (No Authentication)

**Best for**: General development across all projects

1. **Open Cursor Settings**
   - Navigate to **Cursor → Settings** (macOS) or **File → Settings** (Windows/Linux)

2. **Find MCP Servers Section**
   - Under **Features**, scroll to **MCP Servers**

3. **Add New Server**
   - Click **+ Add new MCP Server**
   - **Name**: Give your server a descriptive name (e.g., "Xano Customer DB")
   - **Type**: Select `sse`
   - **Server URL**: Paste your Xano MCP server URL

4. **Test Connection**
   - Your MCP server should appear as "Ready" in the list
   - Open a chat window and set conversation type to **Agent**

#### Option 2: Per-Project Configuration (With Authentication)

**Best for**: Project-specific tools with authentication

1. **Create MCP Configuration Directory**
   ```bash
   mkdir .cursor
   cd .cursor
   ```

2. **Create MCP Configuration File**
   ```bash
   touch mcp.json
   ```

3. **Configure MCP Servers**
   ```json
   {
     "mcpServers": {
       "xano_production": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse",
           "--header",
           "Authorization: Bearer ${AUTH_TOKEN}"
         ],
         "env": {
           "AUTH_TOKEN": "your_auth_token_here"
         }
       },
       "xano_development": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://dev-instance.xano.com/x2/mcp/DEV_SERVER_ID/sse"
         ]
       }
     }
   }
   ```

4. **Restart Cursor**
   - Close and reopen Cursor
   - Set conversation type to **Agent** in chat window

### 🤖 **Claude Desktop Setup**

Claude Desktop provides powerful AI assistance with MCP tool integration.

#### Prerequisites

1. **Install Node.js**
   - Download from [nodejs.org](https://nodejs.org/en)
   - Verify installation: `node --version`

#### Configuration Steps

1. **Locate Configuration File**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Edit Configuration File**
   
   **Basic Configuration (No Authentication):**
   ```json
   {
     "mcpServers": {
       "xano_tools": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse"
         ]
       }
     }
   }
   ```

   **With Authentication:**
   ```json
   {
     "mcpServers": {
       "xano_authenticated": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse",
           "--header",
           "Authorization: Bearer ${AUTH_TOKEN}"
         ],
         "env": {
           "AUTH_TOKEN": "your_auth_token_here"
         }
       }
     }
   }
   ```

   **Windows-Specific Configuration** (handles header spacing issues):
   ```json
   {
     "mcpServers": {
       "xano": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse",
           "--header",
           "Authorization:${AUTH_TOKEN}"
         ],
         "env": {
           "AUTH_TOKEN": "Bearer your_auth_token_here"
         }
       }
     }
   }
   ```

3. **Restart Claude Desktop**
   - Close and reopen the application
   - Look for the 🛠️ icon under the chat box
   - Click to view available tools

### 🌊 **Windsurf Setup**

Windsurf provides AI-powered development capabilities with MCP integration.

1. **Open Windsurf Settings**
   - Navigate to **Settings** → **Cascade**

2. **Add New Server**
   - Click **Add Server** → **Add Custom Server**

3. **Configure Server**
   
   **Basic Configuration:**
   ```json
   {
     "mcpServers": {
       "xano_windsurf": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse"
         ]
       }
     }
   }
   ```

   **With Authentication:**
   ```json
   {
     "mcpServers": {
       "xano_secure": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse",
           "--header",
           "Authorization: Bearer ${AUTH_TOKEN}"
         ],
         "env": {
           "AUTH_TOKEN": "your_auth_token_here"
         }
       }
     }
   }
   ```

4. **Refresh and Connect**
   - Click **Refresh** button
   - Verify your MCP server appears in the list

## 🔗 **No-Code Platform Integration**

### n8n Workflow Integration

**MCP Client in n8n Automation:**

```javascript
// HTTP Request node for MCP tool execution
{
  "method": "POST",
  "url": "https://your-xano-instance.com/x2/mcp/{{server_id}}/sse",
  "headers": {
    "Authorization": "Bearer {{ $json.mcp_token }}",
    "Content-Type": "application/json"
  },
  "body": {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "{{ $json.tool_name }}",
      "arguments": "{{ $json.tool_args }}"
    },
    "id": "{{ $runIndex }}"
  }
}
```

### WeWeb Frontend Integration

**MCP Tool Interface Component:**

```javascript
// WeWeb component for MCP tool interaction
class XanoMCPInterface {
  constructor(serverUrl, authToken) {
    this.serverUrl = serverUrl;
    this.authToken = authToken;
  }
  
  async callTool(toolName, args) {
    try {
      const response = await fetch(this.serverUrl, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          jsonrpc: '2.0',
          method: 'tools/call',
          params: {
            name: toolName,
            arguments: args
          },
          id: Date.now()
        })
      });
      
      const result = await response.json();
      return result.result;
    } catch (error) {
      console.error('MCP tool call failed:', error);
      throw new Error('Tool execution failed');
    }
  }
  
  async listTools() {
    const response = await fetch(this.serverUrl, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.authToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        jsonrpc: '2.0',
        method: 'tools/list',
        id: Date.now()
      })
    });
    
    const result = await response.json();
    return result.result.tools;
  }
}

// Usage in WeWeb
const mcpInterface = new XanoMCPInterface(
  wwLib.wwVariable.getValue('mcp_server_url'),
  wwLib.wwVariable.getValue('mcp_auth_token')
);

async function executeCustomerAnalysis(customerId) {
  const result = await mcpInterface.callTool('analyze_customer_behavior', {
    customer_id: customerId,
    timeframe: '30_days'
  });
  
  wwLib.wwVariable.updateValue('customer_analysis', result);
  return result;
}
```

## 🛠️ **Custom Client Development**

### JavaScript MCP Client

```javascript
class CustomMCPClient {
  constructor(serverUrl, options = {}) {
    this.serverUrl = serverUrl;
    this.authToken = options.authToken;
    this.timeout = options.timeout || 30000;
    this.requestId = 0;
  }
  
  async request(method, params = {}) {
    const requestId = ++this.requestId;
    const headers = {
      'Content-Type': 'application/json'
    };
    
    if (this.authToken) {
      headers['Authorization'] = `Bearer ${this.authToken}`;
    }
    
    const payload = {
      jsonrpc: '2.0',
      method: method,
      params: params,
      id: requestId
    };
    
    try {
      const response = await fetch(this.serverUrl, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(payload)
      });
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      const result = await response.json();
      
      if (result.error) {
        throw new Error(`MCP Error: ${result.error.message}`);
      }
      
      return result.result;
    } catch (error) {
      console.error('MCP request failed:', error);
      throw error;
    }
  }
  
  async initialize() {
    return this.request('initialize', {
      protocolVersion: '2024-11-05',
      capabilities: {
        tools: {}
      },
      clientInfo: {
        name: 'CustomMCPClient',
        version: '1.0.0'
      }
    });
  }
  
  async listTools() {
    return this.request('tools/list');
  }
  
  async callTool(name, arguments_) {
    return this.request('tools/call', {
      name: name,
      arguments: arguments_
    });
  }
}

// Usage example
const client = new CustomMCPClient(
  'https://your-xano-instance.com/x2/mcp/SERVER_ID/sse',
  { authToken: 'your_auth_token' }
);

await client.initialize();
const tools = await client.listTools();
const result = await client.callTool('get_customer_data', { customer_id: 123 });
```

### Python MCP Client

```python
import asyncio
import aiohttp
import json

class XanoMCPClient:
    def __init__(self, server_url, auth_token=None):
        self.server_url = server_url
        self.auth_token = auth_token
        self.request_id = 0
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def request(self, method, params=None):
        if not self.session:
            raise RuntimeError("Client not initialized. Use async with.")
        
        self.request_id += 1
        headers = {'Content-Type': 'application/json'}
        
        if self.auth_token:
            headers['Authorization'] = f'Bearer {self.auth_token}'
        
        payload = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params or {},
            'id': self.request_id
        }
        
        async with self.session.post(
            self.server_url,
            headers=headers,
            json=payload
        ) as response:
            if response.status != 200:
                raise Exception(f"HTTP {response.status}")
            
            result = await response.json()
            
            if 'error' in result:
                raise Exception(f"MCP Error: {result['error']['message']}")
            
            return result.get('result')
    
    async def list_tools(self):
        return await self.request('tools/list')
    
    async def call_tool(self, name, arguments):
        return await self.request('tools/call', {
            'name': name,
            'arguments': arguments
        })

# Usage example
async def main():
    async with XanoMCPClient(
        'https://your-xano-instance.com/x2/mcp/SERVER_ID/sse',
        'your_auth_token'
    ) as client:
        tools = await client.list_tools()
        result = await client.call_tool('analyze_data', {'table': 'customers'})
        print(result)

asyncio.run(main())
```

## 🔐 **Security Best Practices**

### Token Management

1. **Environment Variables**: Store tokens in environment variables
2. **Token Rotation**: Regularly rotate authentication tokens
3. **Scope Limitation**: Use minimal required permissions
4. **Secure Storage**: Never commit tokens to version control

### Configuration Security

```json
{
  "mcpServers": {
    "xano_secure": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse",
        "--header",
        "Authorization: Bearer ${XANO_MCP_TOKEN}"
      ],
      "env": {
        "XANO_MCP_TOKEN": "${XANO_AUTH_TOKEN}"
      }
    }
  }
}
```

**Environment Setup:**
```bash
# .env file
XANO_AUTH_TOKEN=your_actual_token_here
XANO_MCP_TOKEN=${XANO_AUTH_TOKEN}
```

## 🔧 **Troubleshooting**

### Common Connection Issues

**Problem**: "Connection refused" or timeout errors  
**Solution**: 
- Verify server URL format and accessibility
- Check if MCP server is enabled in Xano
- Confirm network connectivity

**Problem**: Authentication failures  
**Solution**:
- Verify token format and validity
- Check token permissions in Xano
- Ensure proper header formatting

**Problem**: Tools not appearing in client  
**Solution**:
- Restart the client application
- Verify MCP server configuration
- Check client logs for errors

**Problem**: Windows header spacing issues (Claude Desktop)  
**Solution**: Use the Windows-specific configuration format with `Authorization:${TOKEN}` instead of `Authorization: Bearer ${TOKEN}`

### Debug Configuration

**Enable Verbose Logging:**
```json
{
  "mcpServers": {
    "xano_debug": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse",
        "--verbose"
      ]
    }
  }
}
```

### Multi-Client Issues

**Problem**: Connection errors when using multiple MCP clients  
**Solution**:
- Use only one client at a time during development
- Clear authentication cache: `rm -rf ~/.mcp-auth` (macOS/Linux)
- Restart all MCP clients after configuration changes

## 💡 **Pro Tips**

- **Start Simple**: Begin with basic configuration before adding authentication
- **Test Incrementally**: Verify each step before moving to the next
- **Use Descriptive Names**: Name your MCP servers clearly for easy identification
- **Monitor Logs**: Check client logs for detailed error information
- **Keep Tokens Secure**: Never share or commit authentication tokens
- **Document Configurations**: Maintain team documentation for MCP setups

## 🎯 **Quick Start Checklist**

**For First-Time Setup:**

1. ✅ Choose your preferred AI client
2. ✅ Install prerequisites (Node.js for most clients)
3. ✅ Get your Xano MCP server URL
4. ✅ Generate authentication token (if needed)
5. ✅ Configure client with basic setup
6. ✅ Test connection and tool discovery
7. ✅ Verify tool execution works
8. ✅ Add authentication if required
9. ✅ Document configuration for team

---

**Next Steps**: Ready to build tools? Check out [MCP Builder](mcp-builder.md) or explore the [Xano MCP Server](xano-mcp-server.md) for administrative capabilities