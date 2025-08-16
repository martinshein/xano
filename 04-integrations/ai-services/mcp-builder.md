---
title: MCP Builder - Build AI-Native Tools with Visual Development
description: Create Model Context Protocol (MCP) servers in Xano to build AI-native functionalities that connect LLMs to your database and external services
category: ai-services
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - mcp-functions.md
  - connecting-clients.md
  - xano-mcp-server.md
subcategory: 04-integrations/ai-services
tags:
  - mcp-builder
  - model-context-protocol
  - ai-native
  - tools
  - llm-integration
  - visual-development
  - no-code
---

## 📋 **Quick Summary**

MCP Builder enables you to create AI-native tools using Xano's visual development platform. Build Model Context Protocol (MCP) servers that allow AI models to interact directly with your database, APIs, and external services. Perfect for creating intelligent automation workflows in n8n, WeWeb, and AI-powered applications that need structured access to your backend data.

## What You'll Learn

- Understanding Model Context Protocol (MCP) and its benefits
- Creating MCP servers and tools in Xano
- Building AI-native functionalities with visual development
- Connecting AI clients to your MCP servers
- Best practices for MCP tool design and security
- Integration patterns for no-code platforms

# MCP Builder

## Overview

**MCP (Model Context Protocol)** is a standardized framework that enables seamless communication between AI models and external services. Think of it as a universal language that allows AI models to intelligently leverage your databases, APIs, and business logic without complex custom integrations.

Xano's **MCP Builder** empowers you to create AI-native tools using the same visual development approach you use for building APIs. Instead of building traditional REST endpoints, you're creating tools specifically designed for AI models to use.

### Why MCP Matters

Traditional AI integrations require custom code and complex API management. MCP changes this by providing:

- **Standardized Communication**: Consistent interface for all AI-service interactions
- **Tool Discovery**: AI models can automatically discover available capabilities
- **Context Awareness**: AI understands how and when to use each tool
- **Security Built-in**: Proper authentication and authorization for AI operations

## Key Concepts

### MCP Servers
Containers that house multiple tools and provide authentication and configuration

### MCP Tools
Individual actions that AI models can perform, built using Xano's function stacks

### Clients
AI applications (like Claude Desktop, Cursor, or custom applications) that connect to your MCP servers

## 🚀 **Getting Started**

### Step 1: Create Your First MCP Server

1. **Navigate to AI Tools**: From the left-hand navigation menu, click **AI Tools**
2. **Add Server**: Click **+ Add MCP Server** to create your first server
3. **Configure Server**:

| Field | Purpose | Example |
|-------|---------|---------|
| **Name** | Clear server identifier | "Customer Database Server" |
| **Description** | Internal purpose description | "Handles customer data operations for AI agents" |
| **Allow Connections** | Enable/disable server access | Enabled for production |
| **Tags** | Organization and search | "customer", "database", "production" |
| **MCP Instructions** | Client-facing documentation | "This server provides customer data access tools..." |

**Pro Tip**: Use Markdown in MCP Instructions for better readability by AI models and developers.

### Step 2: Add Tools to Your Server

You can create tools in two ways:

#### Option A: Convert Existing Function Stacks

1. **Open Existing Function Stack**: Navigate to any existing API endpoint
2. **Convert to Tool**: Click the ⋮ settings icon → **Use As AI Tool**
3. **Configure Tool**: Choose your MCP server and provide a clear tool name

#### Option B: Create Tools from Scratch

1. **Navigate to Tools**: Click **Tools** → **+ Add Tool**
2. **Configure Tool Settings**:

```javascript
// Tool Configuration Example
{
  "name": "get_customer_orders",
  "description": "Retrieves order history for a specific customer",
  "authentication": true,
  "instructions": "Use this tool to get complete order history for a customer. Requires customer_id as input."
}
```

3. **Build Function Stack**: Use visual development to create your tool's logic
4. **Publish Changes**: Deploy your tool when ready

## 🔗 **No-Code Platform Integration**

### n8n Workflow with MCP Tools

**Automated Customer Support with MCP:**

```javascript
// n8n HTTP Request node calling Xano MCP tool
{
  "method": "POST",
  "url": "https://your-xano-instance.com/x2/mcp/{{server_id}}/{{token}}/sse",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{ $json.mcp_token }}"
  },
  "body": {
    "tool": "analyze_customer_inquiry",
    "args": {
      "customer_message": "{{ $json.support_request }}",
      "customer_id": "{{ $json.customer_id }}",
      "context": "support_ticket"
    }
  }
}
```

### WeWeb Integration with MCP

**Frontend AI Assistant Component:**

```javascript
// WeWeb component for MCP-powered AI features
async function callMCPTool(toolName, args) {
  try {
    const mcpResponse = await fetch(`${wwLib.wwVariable.getValue('xano_base_url')}/x2/mcp/${wwLib.wwVariable.getValue('mcp_server_id')}/${wwLib.wwVariable.getValue('mcp_token')}/sse`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        tool: toolName,
        args: args
      })
    });
    
    const result = await mcpResponse.json();
    
    // Update UI with AI-processed results
    wwLib.wwVariable.updateValue('ai_response', result);
    
    return result;
  } catch (error) {
    console.error('MCP tool call failed:', error);
    return { error: 'AI assistant unavailable' };
  }
}

// Example usage in WeWeb
const customerInsight = await callMCPTool('analyze_customer_behavior', {
  customer_id: currentCustomer.id,
  timeframe: '30_days'
});
```

## 🛠️ **Practical Examples**

### Example 1: E-commerce Customer Intelligence

**MCP Tool: Customer Behavior Analysis**

```javascript
// Function stack for customer behavior tool
[
  {
    "function": "get_record",
    "table": "customers",
    "filter": {"id": "{{ args.customer_id }}"}
  },
  {
    "function": "query_all_records",
    "table": "orders",
    "filter": {
      "customer_id": "{{ args.customer_id }}",
      "created_at": ">{{ now - (args.days * 86400) }}"
    }
  },
  {
    "function": "create_variable",
    "name": "customer_insights",
    "value": {
      "total_orders": "{{ orders|length }}",
      "total_spent": "{{ orders|sum('total_amount') }}",
      "avg_order_value": "{{ orders|avg('total_amount') }}",
      "favorite_categories": "{{ orders|group_by('category')|keys }}",
      "customer_tier": "{{ customer.tier }}",
      "last_order_date": "{{ orders|max('created_at') }}"
    }
  }
]
```

**Tool Instructions:**
```markdown
# Customer Behavior Analysis Tool

Analyzes customer purchasing patterns and behavior over a specified time period.

## Parameters
- `customer_id` (required): The unique ID of the customer
- `days` (optional): Number of days to analyze (default: 30)

## Returns
- Customer profile information
- Order history and spending patterns
- Product category preferences
- Customer tier and value metrics

Use this tool when you need to understand customer behavior for personalization, support, or marketing purposes.
```

### Example 2: Inventory Management Intelligence

**MCP Tool: Smart Inventory Alerts**

```javascript
// Function stack for inventory intelligence
[
  {
    "function": "query_all_records",
    "table": "products",
    "filter": {
      "stock_quantity": "<{{ args.threshold || 10 }}"
    }
  },
  {
    "function": "loop",
    "array": "{{ low_stock_products }}",
    "iterations": [
      {
        "function": "query_all_records",
        "table": "order_items",
        "filter": {
          "product_id": "{{ item.id }}",
          "created_at": ">{{ now - 2592000 }}"
        }
      },
      {
        "function": "create_variable",
        "name": "sales_velocity",
        "value": "{{ recent_orders|length / 30 }}"
      }
    ]
  },
  {
    "function": "create_variable",
    "name": "inventory_alerts",
    "value": {
      "low_stock_count": "{{ low_stock_products|length }}",
      "critical_items": "{{ products_with_velocity|where('stock_quantity', '<', 5) }}",
      "recommended_actions": "{{ generate_reorder_recommendations }}"
    }
  }
]
```

### Example 3: AI-Powered Content Management

**MCP Tool: Content Performance Analysis**

```javascript
// Function stack for content analysis
[
  {
    "function": "query_all_records",
    "table": "blog_posts",
    "filter": {
      "published_at": ">{{ args.start_date }}",
      "status": "published"
    }
  },
  {
    "function": "external_api_request",
    "url": "https://api.analytics-service.com/content-metrics",
    "method": "POST",
    "body": {
      "content_ids": "{{ blog_posts|pluck('id') }}",
      "metrics": ["views", "engagement", "shares"]
    }
  },
  {
    "function": "create_variable",
    "name": "content_insights",
    "value": {
      "top_performing": "{{ posts_with_metrics|sort_by('engagement')|reverse|slice(0, 5) }}",
      "trending_topics": "{{ extract_trending_topics }}",
      "optimization_suggestions": "{{ generate_content_suggestions }}"
    }
  }
]
```

## 🔐 **Authentication and Security**

### MCP Authentication Methods

**Bearer Token Authentication:**
```
https://your-xano-instance.com/x2/mcp/{server_id}/{token}/sse
```

**URL Parameters for Context:**
```
https://your-xano-instance.com/x2/mcp/{server_id}/{token}/sse?user_tier=premium&region=us-west
```

### Security Best Practices

1. **Token Rotation**: Regularly update MCP tokens
2. **Scope Limitation**: Create specific tools for specific purposes
3. **Input Validation**: Always validate tool arguments
4. **Rate Limiting**: Implement usage limits for AI tools
5. **Audit Logging**: Track all MCP tool usage

### Access Control Patterns

```javascript
// Function stack with role-based access
[
  {
    "function": "conditional",
    "condition": "{{ token_user.role != 'admin' }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 403,
        "body": {"error": "Admin access required for this tool"}
      }
    ]
  },
  {
    "function": "proceed_with_tool_logic"
  }
]
```

## 🔧 **MCP Variables and Context**

### Special Variables Available in MCP Tools

| Variable | Description | Example Usage |
|----------|-------------|---------------|
| `{{ token }}` | Authentication token from URL | User identification and permissions |
| `{{ params }}` | URL query parameters | Context and configuration settings |
| `{{ args }}` | Tool arguments from AI client | Input data and parameters |

### Using Variables for Dynamic Behavior

```javascript
// Dynamic tool behavior based on context
[
  {
    "function": "conditional",
    "condition": "{{ params.environment == 'development' }}",
    "true_branch": [
      {"function": "enable_debug_mode"}
    ]
  },
  {
    "function": "conditional", 
    "condition": "{{ params.user_tier == 'premium' }}",
    "true_branch": [
      {"function": "enable_advanced_features"}
    ]
  }
]
```

## 🎯 **Connecting Clients to Your MCP Server**

### Popular MCP Clients

#### Cursor IDE Integration
```json
{
  "mcpServers": {
    "xano-customer-db": {
      "command": "curl",
      "args": [
        "-N",
        "-H", "Accept: text/event-stream",
        "https://your-xano-instance.com/x2/mcp/server_id/your_token/sse"
      ]
    }
  }
}
```

#### Claude Desktop Integration
```json
{
  "mcpServers": {
    "xano-tools": {
      "command": "mcp-client",
      "args": ["https://your-xano-instance.com/x2/mcp/server_id/your_token/sse"]
    }
  }
}
```

#### Custom Client Integration
```javascript
// Custom client connection example
class XanoMCPClient {
  constructor(serverUrl, token) {
    this.serverUrl = serverUrl;
    this.token = token;
  }
  
  async callTool(toolName, args) {
    const response = await fetch(`${this.serverUrl}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        tool: toolName,
        args: args
      })
    });
    
    return await response.json();
  }
  
  async listTools() {
    // Implementation for discovering available tools
  }
}
```

## 📊 **Best Practices**

### Tool Design Principles

1. **Single Responsibility**: Each tool should have one clear purpose
2. **Clear Naming**: Use descriptive names that AI models can understand
3. **Comprehensive Instructions**: Provide detailed tool documentation
4. **Error Handling**: Include clear error messages for AI retry logic
5. **Input Validation**: Validate all arguments before processing

### Optimization Strategies

```javascript
// Efficient tool with caching
[
  {
    "function": "get_cached_data",
    "key": "customer_analysis_{{ args.customer_id }}_{{ today }}",
    "ttl": 3600
  },
  {
    "function": "conditional",
    "condition": "{{ !cached_result }}",
    "true_branch": [
      {"function": "perform_expensive_analysis"},
      {"function": "cache_result"}
    ]
  }
]
```

### Performance Considerations

- **Use Enum Inputs**: Help AI models understand available options
- **Minimize Token Usage**: Keep instructions concise but clear
- **Implement Caching**: Cache expensive operations
- **Background Processing**: Use async functions for long-running tasks

## 🔍 **Troubleshooting**

### Common Issues

**Problem**: MCP client can't connect to server  
**Solution**: Verify server URL format and token validity

**Problem**: Tools not appearing in client  
**Solution**: Check tool permissions and server connection status

**Problem**: Tool execution fails  
**Solution**: Review tool instructions and validate input parameters

**Problem**: Authentication errors  
**Solution**: Confirm token format and check user permissions

### Debugging Tips

1. **Test Tools Directly**: Use Xano's function stack testing
2. **Check Logs**: Monitor request history for errors
3. **Validate Instructions**: Ensure tool instructions are clear
4. **Start Simple**: Begin with basic tools before adding complexity

## 💡 **Pro Tips**

- **Version Your Tools**: Keep track of tool changes and compatibility
- **Document Everything**: Good documentation improves AI performance
- **Test with Real AI**: Validate tools with actual AI client interactions
- **Monitor Usage**: Track which tools are used most frequently
- **Iterate Based on Feedback**: Improve tools based on AI behavior

## 🎯 **Quick Start Challenge**

**Build Your First MCP Tool**:

1. Create an MCP server for your business domain
2. Build a simple data retrieval tool
3. Add proper authentication and instructions
4. Connect with a client like Cursor
5. Test the tool with natural language queries

---

**Next Steps**: Ready to connect clients? Check out [Connecting Clients](connecting-clients.md) or explore the [Xano MCP Server](xano-mcp-server.md) for advanced configurations