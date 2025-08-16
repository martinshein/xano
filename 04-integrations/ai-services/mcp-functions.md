---
title: MCP Functions in Xano - Model Context Protocol Integration
description: Connect Xano to external AI services and tools using MCP (Model Context Protocol) functions for seamless AI integrations
category: ai-services
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - ai-tools.md
  - agents.md
  - mcp-builder.md
subcategory: 04-integrations/ai-services
tags:
  - mcp
  - model-context-protocol
  - external-ai
  - integrations
  - functions
  - no-code
---

## 📋 **Quick Summary**

MCP (Model Context Protocol) Functions enable Xano to connect with external AI services and tools. These functions allow your agents and workflows to access remote AI capabilities, databases, and services through standardized protocols. Perfect for integrating with external AI platforms in n8n, WeWeb, and other no-code applications.

## What You'll Learn

- Understanding MCP (Model Context Protocol) and its benefits
- Setting up MCP server connections in Xano
- Using MCP List Tools and MCP Call Tool functions
- Integrating MCP functions with AI agents and workflows
- Best practices for MCP security and performance
- Troubleshooting common MCP connection issues

# MCP Functions in Xano

## Overview

Model Context Protocol (MCP) Functions in Xano provide a standardized way to connect your backend to external AI services, tools, and data sources. MCP enables seamless communication between Xano and various AI platforms, allowing your agents and workflows to access external capabilities without complex API integrations.

### What is MCP?

MCP (Model Context Protocol) is an open standard that enables AI applications to connect to external data sources and tools in a consistent way. Think of it as a universal adapter that allows different AI systems to communicate with each other and with external services.

**Key Benefits:**
- ✅ **Standardized Connections**: Consistent interface for all external AI services
- ✅ **Scalable Integration**: Easy to add new AI services without custom code
- ✅ **Security**: Built-in authentication and permission management
- ✅ **Performance**: Optimized for real-time AI operations
- ✅ **Flexibility**: Works with any MCP-compatible service

## Core MCP Functions

Xano provides two primary MCP functions for external integrations:

### 1. MCP List Tools

**Purpose**: Retrieves a list of available tools and their configurations from an MCP server

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **url** | String | Yes | The URL to access the MCP server |
| **bearer_token** | String | No | Authentication token for the server (if required) |

**Example Usage:**

```javascript
// Function stack configuration
{
  "function": "mcp_list_tools",
  "parameters": {
    "url": "https://api.external-ai-service.com/mcp",
    "bearer_token": "{{ env.EXTERNAL_AI_TOKEN }}"
  }
}
```

**Response Format:**
```json
{
  "tools": [
    {
      "name": "analyze_sentiment",
      "description": "Analyzes sentiment of text input",
      "parameters": {
        "text": "string",
        "language": "string (optional)"
      }
    },
    {
      "name": "translate_text", 
      "description": "Translates text between languages",
      "parameters": {
        "text": "string",
        "from_lang": "string",
        "to_lang": "string"
      }
    }
  ]
}
```

### 2. MCP Call Tool

**Purpose**: Executes a specific tool available on a remote MCP server

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **url** | String | Yes | The URL to access the MCP server |
| **bearer_token** | String | No | Authentication token for the server (if required) |
| **tool_name** | String | Yes | The name of the tool to execute |
| **args** | Object | No | JSON object containing tool-specific arguments |

**Example Usage:**

```javascript
// Function stack configuration
{
  "function": "mcp_call_tool",
  "parameters": {
    "url": "https://api.external-ai-service.com/mcp",
    "bearer_token": "{{ env.EXTERNAL_AI_TOKEN }}",
    "tool_name": "analyze_sentiment",
    "args": {
      "text": "{{ request.body.feedback }}",
      "language": "en"
    }
  }
}
```

**Response Format:**
```json
{
  "result": {
    "sentiment": "positive",
    "confidence": 0.95,
    "score": 0.8,
    "details": {
      "positive": 0.8,
      "negative": 0.1,
      "neutral": 0.1
    }
  },
  "status": "success",
  "execution_time": 245
}
```

## Setting Up MCP Connections

### Step 1: Configure Environment Variables

Store your API keys and endpoints securely:

1. Navigate to **Instance Settings** in Xano
2. Go to **Environment Variables**
3. Add your MCP server credentials:

```env
ANTHROPIC_MCP_URL=https://api.anthropic.com/mcp
ANTHROPIC_API_KEY=your_api_key_here
OPENAI_MCP_URL=https://api.openai.com/mcp
OPENAI_API_KEY=your_openai_key_here
```

### Step 2: Test MCP Connection

Create a simple test endpoint to verify connectivity:

```javascript
// Test function stack
[
  {
    "function": "mcp_list_tools",
    "parameters": {
      "url": "{{ env.ANTHROPIC_MCP_URL }}",
      "bearer_token": "{{ env.ANTHROPIC_API_KEY }}"
    }
  }
]
```

### Step 3: Integrate with Agents

Add MCP tools to your AI agents for enhanced capabilities:

```javascript
// Agent configuration with MCP tool
{
  "agent_name": "Enhanced Support Agent",
  "tools": [
    "get_user_data",           // Local Xano tool
    "analyze_sentiment",       // MCP tool
    "translate_message"        // MCP tool
  ],
  "system_prompt": "You can analyze customer sentiment and translate messages when needed."
}
```

## 🔗 **No-Code Platform Integration**

### n8n Integration

**MCP Function Call in n8n Workflow:**

```javascript
// HTTP Request node for MCP integration
{
  "method": "POST",
  "url": "https://your-xano-instance.com/api/mcp-processor",
  "headers": {
    "Authorization": "Bearer {{ $json.auth_token }}",
    "Content-Type": "application/json"
  },
  "body": {
    "mcp_action": "call_tool",
    "tool_name": "analyze_sentiment",
    "input_data": {
      "text": "{{ $json.customer_feedback }}",
      "metadata": "{{ $json.request_context }}"
    }
  }
}
```

**n8n Workflow Pattern:**
1. **Trigger** → Webhook receives data
2. **Data Processing** → Prepare data for MCP call
3. **HTTP Request** → Call Xano MCP endpoint
4. **Switch** → Route based on MCP response
5. **Actions** → Execute appropriate follow-up actions

### WeWeb Integration

**Frontend MCP Integration:**

```javascript
// WeWeb component for MCP-powered features
async function procesWithAI(inputData) {
  try {
    // First, get available tools
    const toolsResponse = await fetch(`${wwLib.wwVariable.getValue('xano_base_url')}/api/mcp-tools`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${wwLib.wwVariable.getValue('auth_token')}`
      }
    });
    
    const availableTools = await toolsResponse.json();
    
    // Then call specific tool
    const result = await fetch(`${wwLib.wwVariable.getValue('xano_base_url')}/api/mcp-execute`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${wwLib.wwVariable.getValue('auth_token')}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        tool_name: 'analyze_content',
        args: {
          content: inputData.text,
          analysis_type: 'comprehensive'
        }
      })
    });
    
    const analysis = await result.json();
    
    // Update UI with results
    wwLib.wwVariable.updateValue('ai_analysis', analysis);
    
    return analysis;
  } catch (error) {
    console.error('MCP call failed:', error);
    return { error: 'AI analysis unavailable' };
  }
}
```

### Make.com Integration

**Make.com Scenario for MCP:**

1. **Trigger Module**: Gmail, webhook, or scheduler
2. **HTTP Module**: List available MCP tools
3. **Router**: Choose appropriate tool based on data type
4. **HTTP Module**: Execute selected MCP tool
5. **Action Modules**: Process results (send email, update database, etc.)

## 🛠️ **Practical Examples**

### Example 1: Content Analysis Pipeline

**Use Case**: Analyze user-generated content for sentiment, topics, and moderation

**Function Stack:**
```javascript
[
  // Step 1: Get content analysis tools
  {
    "function": "mcp_list_tools",
    "parameters": {
      "url": "{{ env.CONTENT_AI_URL }}",
      "bearer_token": "{{ env.CONTENT_AI_TOKEN }}"
    }
  },
  
  // Step 2: Analyze sentiment
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "{{ env.CONTENT_AI_URL }}",
      "bearer_token": "{{ env.CONTENT_AI_TOKEN }}",
      "tool_name": "analyze_sentiment",
      "args": {
        "text": "{{ request.body.content }}",
        "include_emotions": true
      }
    }
  },
  
  // Step 3: Check for inappropriate content
  {
    "function": "mcp_call_tool", 
    "parameters": {
      "url": "{{ env.MODERATION_AI_URL }}",
      "bearer_token": "{{ env.MODERATION_AI_TOKEN }}",
      "tool_name": "moderate_content",
      "args": {
        "text": "{{ request.body.content }}",
        "strict_mode": true
      }
    }
  },
  
  // Step 4: Store results
  {
    "function": "add_record",
    "parameters": {
      "table": "content_analysis",
      "data": {
        "content_id": "{{ request.body.content_id }}",
        "sentiment_score": "{{ sentiment_result.score }}",
        "moderation_status": "{{ moderation_result.status }}",
        "processed_at": "{{ now }}"
      }
    }
  }
]
```

### Example 2: Multi-Language Customer Support

**Use Case**: Automatically translate and respond to customer inquiries in any language

**Agent Configuration:**
```javascript
{
  "name": "Multilingual Support Agent",
  "system_prompt": "You help customers in any language. Always detect the language first, then provide support in their preferred language.",
  "tools": [
    "detect_language",      // MCP tool
    "translate_text",       // MCP tool  
    "get_customer_info",    // Local tool
    "update_ticket"         // Local tool
  ],
  "workflow": [
    "detect_customer_language",
    "translate_to_english_if_needed", 
    "process_support_request",
    "translate_response_back",
    "send_response"
  ]
}
```

### Example 3: Document Processing Automation

**Use Case**: Process uploaded documents with AI analysis

**Function Stack:**
```javascript
[
  // Step 1: Extract text from document
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "{{ env.DOCUMENT_AI_URL }}",
      "tool_name": "extract_text",
      "args": {
        "document_url": "{{ uploaded_file.url }}",
        "format": "structured"
      }
    }
  },
  
  // Step 2: Summarize content
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "{{ env.LLM_SERVICE_URL }}",
      "tool_name": "summarize_text",
      "args": {
        "text": "{{ extracted_text }}",
        "max_length": 500,
        "style": "business"
      }
    }
  },
  
  // Step 3: Extract key entities
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "{{ env.NLP_SERVICE_URL }}",
      "tool_name": "extract_entities",
      "args": {
        "text": "{{ extracted_text }}",
        "entity_types": ["PERSON", "ORG", "DATE", "MONEY"]
      }
    }
  }
]
```

## Security Best Practices

### Authentication Management

1. **Environment Variables**: Always store API keys in environment variables
2. **Token Rotation**: Regularly rotate API keys and update environment variables
3. **Scope Limitation**: Use tokens with minimal required permissions
4. **Request Validation**: Validate all inputs before sending to MCP servers

### Error Handling

```javascript
// Robust MCP call with error handling
{
  "function": "conditional",
  "condition": "{{ mcp_response.status == 'error' }}",
  "true_branch": [
    {
      "function": "create_variable",
      "name": "fallback_response",
      "value": {
        "status": "fallback",
        "message": "AI service temporarily unavailable",
        "timestamp": "{{ now }}"
      }
    }
  ],
  "false_branch": [
    {
      "function": "process_mcp_result",
      "data": "{{ mcp_response.result }}"
    }
  ]
}
```

### Rate Limiting

Implement rate limiting to avoid exceeding API quotas:

```javascript
// Rate limiting pattern
{
  "function": "get_record",
  "table": "api_usage",
  "filter": {
    "service": "mcp_service",
    "date": "{{ today }}"
  },
  "conditional_execution": {
    "condition": "{{ usage_count < daily_limit }}",
    "true_action": "proceed_with_mcp_call",
    "false_action": "return_rate_limit_error"
  }
}
```

## 🔧 **Troubleshooting**

### Common Issues

**Problem**: MCP server connection timeout  
**Solution**: Check network connectivity and server status. Implement retry logic with exponential backoff.

**Problem**: Authentication errors  
**Solution**: Verify API key is correct and has required permissions. Check token expiration.

**Problem**: Tool not found errors  
**Solution**: Use MCP List Tools to verify available tools. Check tool name spelling and case sensitivity.

**Problem**: Invalid arguments error  
**Solution**: Validate argument structure against tool requirements. Use proper data types.

### Debugging Tips

1. **Test Connections**: Always test MCP connections with simple tool listings first
2. **Log Responses**: Log MCP responses for debugging (remove sensitive data)
3. **Validate Inputs**: Implement input validation before MCP calls
4. **Monitor Performance**: Track response times and error rates
5. **Fallback Strategies**: Always have fallback options when MCP services are unavailable

## 💡 **Pro Tips**

- **Caching**: Cache MCP tool lists to reduce API calls
- **Batch Operations**: Group multiple tool calls when possible
- **Async Processing**: Use background tasks for long-running MCP operations
- **Health Checks**: Implement regular health checks for MCP endpoints
- **Documentation**: Maintain documentation of available MCP tools and their parameters

## 🎯 **Try This**

**Quick Start Challenge**: Set up a basic MCP integration that analyzes text sentiment.

1. Choose an AI service with MCP support (e.g., Anthropic, OpenAI)
2. Configure environment variables with API credentials
3. Create a function stack that lists available tools
4. Implement a sentiment analysis endpoint
5. Test with sample text data

---

**Next Steps**: Ready to build more complex AI workflows? Check out [AI Agents](agents.md) for autonomous task execution or explore [MCP Builder](mcp-builder.md) for advanced configurations
