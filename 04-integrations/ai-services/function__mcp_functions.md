---
title: MCP Functions Reference - Essential Tools for AI Integration
description: Complete reference guide for MCP functions in Xano including Run API Endpoint, Run Task, MCP List Tools, and MCP Call Tool for building powerful AI workflows
category: ai-services
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - mcp-functions.md
  - mcp-builder.md
  - connecting-clients.md
subcategory: 04-integrations/ai-services
tags:
  - mcp-functions
  - function-reference
  - api-endpoints
  - task-execution
  - ai-workflows
  - no-code
---

## 📋 **Quick Summary**

MCP Functions are specialized tools within Xano's function stack that enable seamless integration with Model Context Protocol servers and AI tools. These functions allow you to execute API endpoints, run tasks, and communicate with external MCP servers directly from your function stacks. Essential for building AI-powered automation workflows in n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- How to use each MCP function in your function stacks
- Best practices for API endpoint execution and task management
- External MCP server integration patterns
- Authentication and security considerations
- Real-world examples for no-code platforms
- Troubleshooting common integration issues

# MCP Functions Reference

## Overview

MCP Functions provide the building blocks for AI-native applications in Xano. These functions enable your function stacks to interact with external AI services, execute internal operations, and manage complex workflows with minimal configuration.

### Available MCP Functions

| Function | Purpose | Use Case |
|----------|---------|----------|
| **Run API Endpoint** | Execute internal Xano APIs | Call other endpoints in workflows |
| **Run Task** | Execute background tasks | Async operations and workflows |
| **MCP List Tools** | Discover external tools | Dynamic tool discovery |
| **MCP Call Tool** | Execute external tools | AI service integration |

## 🚀 **Function Detailed Reference**

### 1. Run API Endpoint

**Purpose**: Executes an API endpoint as part of an MCP Server Tool function stack

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **API Group** | String | Yes | The API group containing the target endpoint |
| **Endpoint** | String | Yes | The specific API endpoint to execute |
| **Return as** | String | No | Variable name to store the API response |

#### Key Features

- **No Authentication Required**: Authentication tokens are bypassed for internal calls
- **Direct Access**: Call any endpoint within your Xano instance
- **Variable Storage**: Capture response data for further processing

#### Example Usage

```javascript
// Function stack example
[
  {
    "function": "run_api_endpoint",
    "parameters": {
      "api_group": "user_management",
      "endpoint": "get_user_profile",
      "return_as": "user_data"
    }
  },
  {
    "function": "conditional",
    "condition": "{{ user_data.status == 'active' }}",
    "true_branch": [
      {
        "function": "run_api_endpoint",
        "parameters": {
          "api_group": "notifications",
          "endpoint": "send_welcome_email",
          "return_as": "email_result"
        }
      }
    ]
  }
]
```

#### No-Code Integration

**n8n Workflow Pattern:**
```javascript
// HTTP Request node for Xano MCP tool that uses Run API Endpoint
{
  "method": "POST",
  "url": "https://your-xano-instance.com/x2/mcp/SERVER_ID/sse",
  "body": {
    "tool": "process_user_workflow",
    "args": {
      "user_id": "{{ $json.user_id }}",
      "action": "activate_account"
    }
  }
}
```

### 2. Run Task

**Purpose**: Executes a task as part of an MCP Server Tool function stack

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **Task** | String | Yes | The name of the task to execute |

#### Key Features

- **Background Execution**: Tasks run asynchronously
- **No Return Value**: Tasks do not produce output data
- **Workflow Triggers**: Perfect for triggering side effects

#### Example Usage

```javascript
// Function stack with task execution
[
  {
    "function": "add_record",
    "table": "orders",
    "data": {
      "customer_id": "{{ request.body.customer_id }}",
      "total": "{{ request.body.total }}",
      "status": "pending"
    }
  },
  {
    "function": "run_task",
    "parameters": {
      "task": "send_order_confirmation"
    }
  },
  {
    "function": "run_task",
    "parameters": {
      "task": "update_inventory_levels"
    }
  }
]
```

#### Common Task Patterns

**Email Notifications:**
```javascript
{
  "function": "run_task",
  "parameters": {
    "task": "send_notification_email"
  }
}
```

**Data Synchronization:**
```javascript
{
  "function": "run_task",
  "parameters": {
    "task": "sync_external_database"
  }
}
```

**Analytics Updates:**
```javascript
{
  "function": "run_task",
  "parameters": {
    "task": "update_analytics_dashboard"
  }
}
```

### 3. MCP List Tools

**Purpose**: Provides a list of available tools and their configurations from an MCP server

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **url** | String | Yes | The URL to access the MCP server |
| **bearer token** | String | No | Authentication token for server access |

#### Example Usage

```javascript
// Discover available tools from external MCP server
[
  {
    "function": "mcp_list_tools",
    "parameters": {
      "url": "https://ai-service.example.com/mcp",
      "bearer_token": "{{ env.EXTERNAL_AI_TOKEN }}"
    },
    "return_as": "available_tools"
  },
  {
    "function": "create_variable",
    "name": "tool_names",
    "value": "{{ available_tools.tools|pluck('name') }}"
  }
]
```

#### Response Format

```json
{
  "tools": [
    {
      "name": "analyze_sentiment",
      "description": "Analyzes the sentiment of provided text",
      "parameters": {
        "text": "string",
        "language": "string (optional)"
      }
    },
    {
      "name": "generate_summary",
      "description": "Creates a summary of long text content",
      "parameters": {
        "content": "string",
        "max_length": "integer (optional)"
      }
    }
  ]
}
```

### 4. MCP Call Tool

**Purpose**: Executes a tool available on a remote MCP server

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **url** | String | Yes | The URL to access the MCP server |
| **bearer token** | String | No | Authentication token for server access |
| **tool name** | String | Yes | The name of the tool to execute |
| **args** | Object | No | JSON object containing tool-specific arguments |

#### Example Usage

```javascript
// Call external AI tool for sentiment analysis
[
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "https://ai-analytics.example.com/mcp",
      "bearer_token": "{{ env.ANALYTICS_AI_TOKEN }}",
      "tool_name": "analyze_sentiment",
      "args": {
        "text": "{{ request.body.customer_feedback }}",
        "language": "en",
        "include_confidence": true
      }
    },
    "return_as": "sentiment_analysis"
  },
  {
    "function": "add_record",
    "table": "feedback_analysis",
    "data": {
      "feedback_id": "{{ request.body.feedback_id }}",
      "sentiment": "{{ sentiment_analysis.sentiment }}",
      "confidence": "{{ sentiment_analysis.confidence }}",
      "processed_at": "{{ now }}"
    }
  }
]
```

## 🔗 **No-Code Platform Integration**

### n8n Workflow Integration

**Complete AI Processing Workflow:**

```javascript
// n8n workflow using MCP functions
{
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "Webhook",
      "parameters": {
        "path": "process-feedback"
      }
    },
    {
      "name": "List AI Tools",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/mcp-list-tools",
        "method": "POST",
        "body": {
          "mcp_url": "https://external-ai.com/mcp",
          "token": "{{ $env.AI_TOKEN }}"
        }
      }
    },
    {
      "name": "Process with AI",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/mcp-call-tool",
        "method": "POST",
        "body": {
          "mcp_url": "https://external-ai.com/mcp",
          "tool_name": "analyze_content",
          "args": {
            "text": "{{ $json.content }}",
            "analysis_type": "comprehensive"
          }
        }
      }
    },
    {
      "name": "Run Notification Task",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/run-task",
        "method": "POST",
        "body": {
          "task": "send_analysis_notification",
          "context": "{{ $json }}"
        }
      }
    }
  ]
}
```

### WeWeb Integration

**AI-Powered Content Analysis Component:**

```javascript
// WeWeb component using MCP functions
class AIContentAnalyzer {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async getAvailableTools(mcpServerUrl) {
    try {
      const response = await fetch(`${this.baseUrl}/api/mcp-list-tools`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          mcp_url: mcpServerUrl,
          bearer_token: wwLib.wwVariable.getValue('ai_service_token')
        })
      });
      
      const result = await response.json();
      return result.tools;
    } catch (error) {
      console.error('Failed to list MCP tools:', error);
      return [];
    }
  }
  
  async analyzeContent(content, toolName = 'analyze_content') {
    try {
      const response = await fetch(`${this.baseUrl}/api/mcp-call-tool`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          mcp_url: wwLib.wwVariable.getValue('ai_service_url'),
          tool_name: toolName,
          args: {
            text: content,
            options: {
              sentiment: true,
              keywords: true,
              summary: true
            }
          }
        })
      });
      
      const analysis = await response.json();
      
      // Update UI with analysis results
      wwLib.wwVariable.updateValue('content_analysis', analysis);
      
      // Trigger notification task
      await this.runNotificationTask(analysis);
      
      return analysis;
    } catch (error) {
      console.error('Content analysis failed:', error);
      return { error: 'Analysis unavailable' };
    }
  }
  
  async runNotificationTask(analysisData) {
    try {
      await fetch(`${this.baseUrl}/api/run-task`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          task: 'send_analysis_complete_notification',
          context: analysisData
        })
      });
    } catch (error) {
      console.error('Failed to run notification task:', error);
    }
  }
}

// Usage in WeWeb
const analyzer = new AIContentAnalyzer(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

async function handleContentSubmission() {
  const content = wwLib.wwVariable.getValue('user_content');
  const analysis = await analyzer.analyzeContent(content);
  
  if (!analysis.error) {
    wwLib.wwModal.open('analysis-results-modal');
  }
}
```

## 🛠️ **Advanced Integration Patterns**

### Dynamic Tool Discovery and Execution

```javascript
// Function stack that discovers and uses tools dynamically
[
  {
    "function": "mcp_list_tools",
    "parameters": {
      "url": "{{ request.body.mcp_server_url }}",
      "bearer_token": "{{ env.DYNAMIC_AI_TOKEN }}"
    },
    "return_as": "available_tools"
  },
  {
    "function": "conditional",
    "condition": "{{ available_tools.tools|where('name', 'analyze_sentiment')|length > 0 }}",
    "true_branch": [
      {
        "function": "mcp_call_tool",
        "parameters": {
          "url": "{{ request.body.mcp_server_url }}",
          "tool_name": "analyze_sentiment",
          "args": {
            "text": "{{ request.body.text_to_analyze }}"
          }
        },
        "return_as": "sentiment_result"
      }
    ],
    "false_branch": [
      {
        "function": "create_variable",
        "name": "sentiment_result",
        "value": {
          "error": "Sentiment analysis tool not available"
        }
      }
    ]
  }
]
```

### Multi-Service AI Processing

```javascript
// Function stack using multiple MCP services
[
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "{{ env.TRANSLATION_SERVICE_URL }}",
      "tool_name": "translate_text",
      "args": {
        "text": "{{ request.body.original_text }}",
        "target_language": "en"
      }
    },
    "return_as": "translated_text"
  },
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "{{ env.ANALYSIS_SERVICE_URL }}",
      "tool_name": "analyze_content",
      "args": {
        "text": "{{ translated_text.result }}",
        "analysis_types": ["sentiment", "keywords", "topics"]
      }
    },
    "return_as": "content_analysis"
  },
  {
    "function": "run_task",
    "parameters": {
      "task": "store_analysis_results"
    }
  }
]
```

## 🔐 **Security Best Practices**

### Token Management

1. **Environment Variables**: Always store bearer tokens in environment variables
2. **Scope Limiting**: Use tokens with minimal required permissions
3. **Token Rotation**: Regularly rotate external service tokens
4. **Error Handling**: Implement proper error handling for authentication failures

### Input Validation

```javascript
// Secure MCP function usage with validation
[
  {
    "function": "conditional",
    "condition": "{{ !request.body.text || request.body.text|length > 10000 }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {"error": "Invalid text input"}
      }
    ]
  },
  {
    "function": "mcp_call_tool",
    "parameters": {
      "url": "{{ env.SECURE_AI_URL }}",
      "bearer_token": "{{ env.SECURE_AI_TOKEN }}",
      "tool_name": "safe_analyze_text",
      "args": {
        "text": "{{ request.body.text|sanitize }}",
        "safety_level": "high"
      }
    }
  }
]
```

## 🔧 **Troubleshooting**

### Common Issues

**Problem**: MCP server connection timeouts  
**Solution**: Verify server URL and network connectivity. Implement retry logic.

**Problem**: Authentication errors with external services  
**Solution**: Check bearer token validity and permissions. Verify environment variable configuration.

**Problem**: Tool not found errors  
**Solution**: Use MCP List Tools to verify available tools. Check tool name spelling.

**Problem**: Task execution failures  
**Solution**: Verify task exists and has proper permissions. Check task dependencies.

### Debugging Tips

1. **Log MCP Responses**: Use create_variable to capture and log responses
2. **Test Incrementally**: Start with MCP List Tools before calling specific tools
3. **Validate Inputs**: Always validate data before sending to external services
4. **Monitor Performance**: Track response times for external MCP calls

## 💡 **Pro Tips**

- **Cache Tool Lists**: Store frequently used tool lists to reduce API calls
- **Implement Fallbacks**: Always have backup options when external services fail
- **Use Conditional Logic**: Check tool availability before execution
- **Batch Operations**: Group multiple tool calls when possible
- **Monitor Usage**: Track external service usage to manage costs

## 🎯 **Quick Reference**

**Function Selection Guide:**
- Use **Run API Endpoint** for internal Xano API calls
- Use **Run Task** for background operations and side effects
- Use **MCP List Tools** for dynamic tool discovery
- Use **MCP Call Tool** for external AI service integration

---

**Next Steps**: Ready to implement MCP functions? Check out [MCP Functions](mcp-functions.md) for detailed integration examples or explore [MCP Builder](mcp-builder.md) for creating custom tools