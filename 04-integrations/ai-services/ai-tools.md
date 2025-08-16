---
title: AI Tools in Xano - Complete Integration Guide
description: Master Xano's AI tools including MCP servers, agents, and template engines for automated workflows and intelligent applications
category: ai-services
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - agents.md
  - mcp-functions.md
  - templates.md
subcategory: 04-integrations/ai-services
tags:
  - ai-tools
  - mcp-server
  - agents
  - template-engine
  - automation
  - no-code
  - ai-integration
---






## 📋 **Quick Summary**

Xano's AI Tools empower you to build intelligent applications without coding. These tools include MCP (Model Context Protocol) servers for connecting to external AI services, AI agents for autonomous task execution, and template engines for dynamic content generation. Perfect for automation workflows in n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- How to set up and use MCP servers for AI integrations  
- Creating AI agents that can execute tasks autonomously
- Using the Template Engine for dynamic content generation
- Best practices for AI tool integration in no-code workflows
- Troubleshooting common AI tool configuration issues

# AI Tools in Xano

## Overview

AI Tools in Xano consist of three main components that work together to create intelligent, automated applications:

### 🤖 **AI Agents**
Autonomous entities that can make decisions and execute tasks without human intervention. Perfect for customer support, data processing, and workflow automation.

### 🔌 **MCP (Model Context Protocol) Servers**  
Connect to external AI services and tools, enabling your Xano backend to communicate with popular AI platforms like OpenAI, Claude, and more.

### 📝 **Template Engine**
Powered by Twig, this tool generates dynamic content like AI prompts, HTML, emails, and other large-format text using your database records and API inputs.

## Core AI Tools Reference

### MCP List Tools

Provides a list of available tools and their configurations from an MCP server.

| Parameter | Purpose |
|-----------|---------|
| **url** | The URL to access the MCP server |
| **bearer token** | If required, an authentication token to access the server |

### MCP Call Tool

Executes a tool available on a remote MCP server.

| Parameter | Purpose |
|-----------|---------|
| **url** | The URL to access the MCP server |
| **bearer token** | If required, an authentication token to access the server |
| **tool name** | The name of the tool to call |
| **args** | The data that the tool requires, if any. This should usually be a JSON object |

### Call Agent

Calls an AI Agent that exists in this workspace.

| Parameter | Purpose |
|-----------|---------|
| **args** | a JSON object of arguments the agent needs to run |
| **allow_tool_execution** | true or false, determines if the agent has permission to run tools |

## Template Engine Deep Dive

> 💡 **Best Use Cases**
**The Template Engine excels when:**
- Templates will be edited by non-developers
- Data structure is complex with nested objects  
- Conditional sections are needed
- Consistent data formatting (like dates) is required
- Templates might be reused with different data sources

### Quick Summary

The Template Engine, powered by Twig, is used to manipulate and dynamically generate large blocks of text or code with your own data, such as records from your Xano database, or from inputs sent to your APIs.

It's great for helping generate things like AI prompts, HTML, and other more large-format data without messing around with a bulk of separate functions to do so.

### When to Use Template Engine vs Other Text Filters

You should stick with filters like `replace` or `sprintf` if you're manipulating short strings of text, such as:

- Replacing a name inside of a string like "Hello, [first_name] [last_name]"  
- Dynamically providing a price for a single product

The Template Engine, however, is useful for content templates where the data structure is complex or you need conditional logic.

## Setting Up the Template Engine

### Step 1: Add Template Engine Function

Look for the Template Engine function under Utility Functions in your function stack.

### Step 2: Configure the Editor  

Once you add the Template Engine to your function stack, click the ✏️ button in the panel to open the editor, or use the AI assistant to help write a template for you.

### Step 3: Build Your Template

Take a tour of the editor and begin building your template with the syntax below.

## Template Syntax Guide

### Variables

Variables are wrapped in `{{ curly braces }}`, and begin with a `$` character:

```twig
Hi, {{ $user1.name }}
```

Reference items in an array by using the item index:

```twig  
Hi, {{ $user1[0] }}
```

### Conditionals

Conditionals are helpful for dynamic content based on data conditions. They're wrapped in `{% %}` and support `else` and `elseif`:

```twig
{% if $user.vip %}
  Hey, {{ $user.name }}! Thanks for being a part of our VIP program.
{% else %}
  Hey, {{ $user.name }}! Thanks for reading.
{% endif %}
```

### Loops

Use loops to populate lists without writing separate lines for each item:

```twig
{% for item in $order_items %}
  - {{ item.quantity }}x {{ item.name }} at ${{ item.price }} each
{% endfor %}
```

### Filters

Transform data using Twig's built-in filters:

| Filter | Description | Example | Result |
|--------|-------------|---------|--------|
| `upper` | Converts to uppercase | `{{ $user.name\|upper }}` | "JOHN SMITH" |
| `lower` | Converts to lowercase | `{{ $user.name\|lower }}` | "john smith" |
| `trim` | Removes whitespace | `{{ $user.input\|trim }}` | "hello" |
| `join` | Joins array with delimiter | `{{ $user.tags\|join(', ') }}` | "php, twig, web" |
| `default` | Provides fallback value | `{{ $user.middleName\|default('N/A') }}` | "N/A" |
| `number_format` | Formats numbers | `{{ $product.price\|number_format }}` | "1,234.56" |
| `date` | Formats dates | `{{ $user.createdAt\|date('F j, Y') }}` | "December 25, 2023" |

### Escape Filter for Security

Always use the escape filter when displaying user input to prevent security issues:

```twig
{# HTML Escaping #}
{{ $user_input|e('html') }}

{# JavaScript Escaping #}  
{{ $js_string|e('js') }}

{# URL Escaping #}
{{ $search_query|e('url') }}

{# CSS Escaping #}
{{ $css_value|e('css') }}
```

### Comments

Add comments that won't appear in final output:

```twig
{# This is a hidden comment #}
```

## 🔗 **No-Code Platform Integration**

### n8n Integration

Use Xano AI Tools in n8n workflows:

```javascript
// HTTP Request node configuration for calling Xano AI Agent
{
  "method": "POST",
  "url": "https://your-xano-instance.com/api/call-agent",
  "headers": {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
  },
  "body": {
    "agent_id": "customer-support-agent",
    "args": {
      "customer_inquiry": "{{ $json.inquiry }}",
      "user_id": "{{ $json.user_id }}"
    },
    "allow_tool_execution": true
  }
}
```

### WeWeb Integration

Connect WeWeb frontend to Xano AI Tools:

```javascript
// WeWeb action to call Xano Template Engine
async function generateEmail(userData) {
  const response = await fetch('https://your-xano-instance.com/api/generate-content', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${wwLib.wwVariable.getValue('auth_token')}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      template: 'email_template',
      data: userData
    })
  });
  
  return await response.json();
}
```

### Make.com Integration

Set up Make.com scenarios with Xano AI Tools:

1. **Trigger**: Webhook or scheduled trigger
2. **HTTP Module**: Call Xano AI endpoint
3. **Data Processing**: Use AI-generated responses  
4. **Action**: Send email, update database, etc.

## 🛠️ **Practical Examples**

### Example 1: Customer Support Automation

**Scenario**: Automatically handle customer inquiries with AI agent

```javascript
// Function stack configuration
{
  "agent": "customer-support-agent",
  "args": {
    "inquiry": "{{ request.body.message }}",
    "customer_id": "{{ request.body.customer_id }}",
    "previous_orders": "{{ customer_data.orders }}"
  },
  "tools": [
    "lookup_customer_info",
    "check_order_status", 
    "process_refund",
    "escalate_to_human"
  ]
}
```

### Example 2: Dynamic Email Generation

**Template Engine Example**:

```twig
Subject: Your Order #{{ $order.id }} Update

Dear {{ $customer.first_name }},

{% if $order.status == 'shipped' %}
Great news! Your order has been shipped and is on its way.
Tracking number: {{ $order.tracking_number }}
{% elseif $order.status == 'processing' %}
We're currently processing your order and will update you soon.
{% endif %}

Order Details:
{% for item in $order.items %}
- {{ item.quantity }}x {{ item.name }} - ${{ item.price }}
{% endfor %}

Total: ${{ $order.total|number_format }}

Thank you for your business!
```

### Example 3: MCP Server Integration

**Connect to External AI Service**:

```javascript
// MCP Call Tool configuration
{
  "url": "https://api.anthropic.com/mcp",
  "bearer_token": "{{ env.ANTHROPIC_API_KEY }}",
  "tool_name": "analyze_sentiment",
  "args": {
    "text": "{{ request.body.feedback }}",
    "context": "customer_review"
  }
}
```

## 🔧 **Troubleshooting**

### Common Issues

**Problem**: Template Engine variables not rendering
**Solution**: Ensure variables use correct syntax with `$` prefix: `{{ $variable.field }}`

**Problem**: MCP server connection fails  
**Solution**: Verify bearer token and URL are correct, check network connectivity

**Problem**: AI Agent not executing tools
**Solution**: Confirm `allow_tool_execution` is set to `true` and tools are properly configured

### Best Practices

1. **Always escape user input** when using Template Engine
2. **Test AI agents thoroughly** before production deployment
3. **Monitor MCP server performance** and implement proper error handling
4. **Use structured outputs** for agent responses when chaining multiple agents
5. **Implement proper authentication** for all AI tool endpoints

## 💡 **Pro Tips**

- **Performance**: Cache template results for frequently used content
- **Security**: Always validate and sanitize inputs before processing
- **Scalability**: Use background tasks for long-running AI operations  
- **Monitoring**: Track AI tool usage and costs in your workspace settings
- **Testing**: Create test scenarios for different AI tool combinations

---

**Next Steps**: Ready to implement AI tools? Start with the [Agents guide](agents.md) or explore [MCP Functions](mcp-functions.md) for external integrations
