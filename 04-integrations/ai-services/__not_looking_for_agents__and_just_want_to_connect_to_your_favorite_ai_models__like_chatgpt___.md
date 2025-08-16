---
title: Direct AI Model Integration - Connecting to ChatGPT, Claude, and Other LLMs
description: Simple guide for connecting directly to AI models like ChatGPT, Claude, Gemini without using Xano Agents. Perfect for basic chatbots, content generation, and simple AI integrations in n8n, WeWeb workflows
category: ai-services
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - agents.md
  - ai-tools.md
  - external-api-request.md
subcategory: 04-integrations/ai-services
tags:
  - chatgpt
  - claude
  - gemini
  - external-api
  - direct-integration
  - simple-ai
  - no-code
---

## 📋 **Quick Summary**

Connect directly to popular AI models like ChatGPT, Claude, and Gemini without using Xano's Agent system. This approach is perfect for simple AI integrations, basic chatbots, content generation, and workflows that don't need complex decision-making or tool usage. Ideal for n8n automations and WeWeb applications requiring straightforward AI responses.

## What You'll Learn

- How to integrate directly with OpenAI, Anthropic, and Google AI APIs
- When to use direct AI integration vs Xano Agents
- Setting up external API requests for various AI models
- Building simple chatbots and content generation workflows
- Authentication and security for AI model APIs
- Cost-effective patterns for basic AI functionality

# Direct AI Model Integration

## Overview

While **Xano Agents** are powerful for complex workflows requiring decision-making and tool usage, sometimes you just need simple AI responses. Direct integration with AI models through external API requests provides a lightweight solution for basic AI functionality without the overhead of agent systems.

### Direct Integration vs Agents

| Approach | Best For | Complexity | Features |
|----------|----------|------------|----------|
| **Direct API** | Simple responses, content generation | Low | Basic text generation |
| **Xano Agents** | Complex workflows, decision-making | High | Tools, reasoning, structured outputs |

### Supported AI Models

**OpenAI (ChatGPT):**
- GPT-4, GPT-4 Turbo, GPT-3.5
- Text generation, conversation, code assistance
- Function calling capabilities

**Anthropic (Claude):**
- Claude 3.5 Sonnet, Claude 3 Haiku
- Advanced reasoning, long context
- Safety-focused responses

**Google (Gemini):**
- Gemini Pro, Gemini Flash
- Multimodal capabilities (text, images)
- Fast response times

## 🚀 **Setting Up Direct AI Integration**

### Basic External API Configuration

1. **Add External API Request Function**: In your function stack, add the "External API Request" function
2. **Configure Endpoint**: Set up the specific AI model endpoint
3. **Handle Authentication**: Add API key authentication
4. **Process Response**: Parse and format the AI response

### OpenAI ChatGPT Integration

**Function Stack Configuration:**

```javascript
// External API Request function configuration
{
  "function": "external_api_request",
  "url": "https://api.openai.com/v1/chat/completions",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
    "Content-Type": "application/json"
  },
  "body": {
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user", 
        "content": "{{ request.body.user_message }}"
      }
    ],
    "max_tokens": 1000,
    "temperature": 0.7
  }
}
```

### Anthropic Claude Integration

**Function Stack Configuration:**

```javascript
// External API Request for Claude
{
  "function": "external_api_request",
  "url": "https://api.anthropic.com/v1/messages",
  "method": "POST",
  "headers": {
    "x-api-key": "{{ env.ANTHROPIC_API_KEY }}",
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01"
  },
  "body": {
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user",
        "content": "{{ request.body.user_message }}"
      }
    ]
  }
}
```

### Google Gemini Integration

**Function Stack Configuration:**

```javascript
// External API Request for Gemini
{
  "function": "external_api_request",
  "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "query_params": {
    "key": "{{ env.GOOGLE_AI_API_KEY }}"
  },
  "body": {
    "contents": [
      {
        "parts": [
          {
            "text": "{{ request.body.user_message }}"
          }
        ]
      }
    ],
    "generationConfig": {
      "temperature": 0.7,
      "maxOutputTokens": 1000
    }
  }
}
```

## 🔗 **No-Code Platform Integration**

### n8n Workflow with Direct AI Integration

**Multi-Model AI Content Generation:**

```javascript
// n8n workflow for content generation using multiple AI models
{
  "nodes": [
    {
      "name": "Content Request",
      "type": "Webhook",
      "parameters": {
        "path": "generate-content",
        "responseMode": "responseNode"
      }
    },
    {
      "name": "Choose AI Model",
      "type": "Switch",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{ $json.ai_model }}",
              "value2": "openai"
            },
            {
              "value1": "{{ $json.ai_model }}",
              "value2": "claude"
            },
            {
              "value1": "{{ $json.ai_model }}",
              "value2": "gemini"
            }
          ]
        }
      }
    },
    {
      "name": "OpenAI Request",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/openai-completion",
        "method": "POST",
        "body": {
          "user_message": "{{ $json.content_request }}",
          "context": "{{ $json.additional_context }}"
        }
      }
    },
    {
      "name": "Claude Request",
      "type": "HTTP Request", 
      "parameters": {
        "url": "https://your-xano-instance.com/api/claude-completion",
        "method": "POST",
        "body": {
          "user_message": "{{ $json.content_request }}",
          "style": "{{ $json.writing_style }}"
        }
      }
    },
    {
      "name": "Gemini Request",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/gemini-completion", 
        "method": "POST",
        "body": {
          "user_message": "{{ $json.content_request }}",
          "format": "{{ $json.output_format }}"
        }
      }
    }
  ]
}
```

### WeWeb Simple AI Chat Integration

**Direct AI Chat Component:**

```javascript
// WeWeb component for simple AI chat using direct API integration
class SimpleAIChat {
  constructor(xanoBaseUrl, aiModel = 'openai') {
    this.baseUrl = xanoBaseUrl;
    this.aiModel = aiModel;
    this.conversationHistory = [];
  }
  
  async sendMessage(userMessage, context = {}) {
    try {
      // Add user message to history
      this.conversationHistory.push({
        role: 'user',
        content: userMessage,
        timestamp: new Date().toISOString()
      });
      
      const response = await fetch(`${this.baseUrl}/api/${this.aiModel}-chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          user_message: userMessage,
          conversation_history: this.conversationHistory.slice(-10), // Last 10 messages
          context: context
        })
      });
      
      const aiResponse = await response.json();
      
      // Add AI response to history
      this.conversationHistory.push({
        role: 'assistant',
        content: aiResponse.response,
        timestamp: new Date().toISOString()
      });
      
      // Update WeWeb variables
      wwLib.wwVariable.updateValue('chat_history', this.conversationHistory);
      wwLib.wwVariable.updateValue('last_ai_response', aiResponse.response);
      
      return aiResponse.response;
    } catch (error) {
      console.error('AI chat request failed:', error);
      return 'Sorry, I encountered an error. Please try again.';
    }
  }
  
  async generateContent(prompt, contentType = 'article') {
    try {
      const response = await fetch(`${this.baseUrl}/api/content-generation`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          prompt: prompt,
          content_type: contentType,
          ai_model: this.aiModel,
          options: {
            max_tokens: contentType === 'summary' ? 200 : 1000,
            temperature: contentType === 'creative' ? 0.9 : 0.7
          }
        })
      });
      
      const generatedContent = await response.json();
      
      // Update WeWeb content variables
      wwLib.wwVariable.updateValue('generated_content', generatedContent.content);
      wwLib.wwVariable.updateValue('content_metadata', {
        word_count: generatedContent.word_count,
        model_used: this.aiModel,
        generated_at: new Date().toISOString()
      });
      
      return generatedContent.content;
    } catch (error) {
      console.error('Content generation failed:', error);
      return 'Content generation failed. Please try again.';
    }
  }
  
  clearHistory() {
    this.conversationHistory = [];
    wwLib.wwVariable.updateValue('chat_history', []);
  }
  
  switchModel(newModel) {
    this.aiModel = newModel;
    wwLib.wwVariable.updateValue('current_ai_model', newModel);
  }
}

// Usage in WeWeb
const aiChat = new SimpleAIChat(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('selected_ai_model') || 'openai'
);

async function handleUserMessage() {
  const userInput = wwLib.wwVariable.getValue('user_input');
  const conversationContext = wwLib.wwVariable.getValue('conversation_context');
  
  if (userInput.trim()) {
    const response = await aiChat.sendMessage(userInput, conversationContext);
    
    // Clear input and scroll to bottom
    wwLib.wwVariable.updateValue('user_input', '');
    wwLib.wwUtils.scrollToElement('#chat-bottom');
  }
}

async function generateBlogPost() {
  const topic = wwLib.wwVariable.getValue('blog_topic');
  const style = wwLib.wwVariable.getValue('writing_style');
  
  const prompt = `Write a comprehensive blog post about ${topic} in a ${style} style. Include an introduction, main sections with headers, and a conclusion.`;
  
  const content = await aiChat.generateContent(prompt, 'article');
  
  if (content) {
    wwLib.wwModal.open('content-preview-modal');
  }
}
```

## 🛠️ **Advanced Integration Patterns**

### Multi-Model Comparison

**Function Stack for Model Comparison:**

```javascript
// Function stack that queries multiple AI models for comparison
[
  {
    "function": "create_variable",
    "name": "user_prompt",
    "value": "{{ request.body.prompt }}"
  },
  {
    "function": "external_api_request",
    "url": "https://api.openai.com/v1/chat/completions",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
      "Content-Type": "application/json"
    },
    "body": {
      "model": "gpt-4",
      "messages": [{"role": "user", "content": "{{ user_prompt }}"}],
      "max_tokens": 500
    },
    "return_as": "openai_response"
  },
  {
    "function": "external_api_request",
    "url": "https://api.anthropic.com/v1/messages",
    "method": "POST",
    "headers": {
      "x-api-key": "{{ env.ANTHROPIC_API_KEY }}",
      "Content-Type": "application/json",
      "anthropic-version": "2023-06-01"
    },
    "body": {
      "model": "claude-3-5-sonnet-20241022",
      "max_tokens": 500,
      "messages": [{"role": "user", "content": "{{ user_prompt }}"}]
    },
    "return_as": "claude_response"
  },
  {
    "function": "create_variable",
    "name": "comparison_result",
    "value": {
      "prompt": "{{ user_prompt }}",
      "responses": {
        "openai": {
          "content": "{{ openai_response.choices[0].message.content }}",
          "model": "gpt-4",
          "tokens": "{{ openai_response.usage.total_tokens }}"
        },
        "claude": {
          "content": "{{ claude_response.content[0].text }}",
          "model": "claude-3-5-sonnet",
          "tokens": "{{ claude_response.usage.input_tokens + claude_response.usage.output_tokens }}"
        }
      },
      "timestamp": "{{ now }}"
    }
  }
]
```

### Content Generation Pipeline

**Automated Content Creation Workflow:**

```javascript
// Function stack for automated content generation pipeline
[
  {
    "function": "create_variable",
    "name": "content_brief",
    "value": "{{ request.body.brief }}"
  },
  // Step 1: Generate outline
  {
    "function": "external_api_request",
    "url": "https://api.openai.com/v1/chat/completions",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
      "Content-Type": "application/json"
    },
    "body": {
      "model": "gpt-4",
      "messages": [
        {
          "role": "system",
          "content": "Create a detailed outline for content based on the brief provided."
        },
        {
          "role": "user",
          "content": "{{ content_brief }}"
        }
      ],
      "max_tokens": 800
    },
    "return_as": "outline_response"
  },
  // Step 2: Generate full content
  {
    "function": "external_api_request",
    "url": "https://api.anthropic.com/v1/messages",
    "method": "POST",
    "headers": {
      "x-api-key": "{{ env.ANTHROPIC_API_KEY }}",
      "Content-Type": "application/json",
      "anthropic-version": "2023-06-01"
    },
    "body": {
      "model": "claude-3-5-sonnet-20241022",
      "max_tokens": 2000,
      "messages": [
        {
          "role": "user",
          "content": "Based on this outline: {{ outline_response.choices[0].message.content }}, write comprehensive content for: {{ content_brief }}"
        }
      ]
    },
    "return_as": "content_response"
  },
  // Step 3: Store generated content
  {
    "function": "add_record",
    "table": "generated_content",
    "data": {
      "brief": "{{ content_brief }}",
      "outline": "{{ outline_response.choices[0].message.content }}",
      "content": "{{ content_response.content[0].text }}",
      "word_count": "{{ content_response.content[0].text|split(' ')|length }}",
      "generated_at": "{{ now }}",
      "status": "draft"
    }
  }
]
```

## 💰 **Cost Optimization Strategies**

### Model Selection by Use Case

**Cost-Effective Model Choices:**

```javascript
// Function to choose optimal model based on request type
{
  "function": "conditional",
  "condition": "{{ request.body.request_type }}",
  "cases": {
    "simple_chat": {
      "model": "gpt-3.5-turbo",
      "provider": "openai",
      "max_tokens": 150
    },
    "content_generation": {
      "model": "claude-3-haiku",
      "provider": "anthropic", 
      "max_tokens": 1000
    },
    "complex_analysis": {
      "model": "gpt-4",
      "provider": "openai",
      "max_tokens": 2000
    },
    "quick_summary": {
      "model": "gemini-flash",
      "provider": "google",
      "max_tokens": 200
    }
  }
}
```

### Token Usage Monitoring

**Function Stack with Usage Tracking:**

```javascript
[
  {
    "function": "external_api_request",
    "url": "{{ ai_provider_url }}",
    "method": "POST",
    "headers": "{{ ai_headers }}",
    "body": "{{ ai_request_body }}",
    "return_as": "ai_response"
  },
  {
    "function": "add_record",
    "table": "ai_usage_logs",
    "data": {
      "provider": "{{ ai_provider }}",
      "model": "{{ ai_model }}",
      "input_tokens": "{{ ai_response.usage.prompt_tokens }}",
      "output_tokens": "{{ ai_response.usage.completion_tokens }}",
      "total_tokens": "{{ ai_response.usage.total_tokens }}",
      "cost_estimate": "{{ calculate_cost(ai_response.usage.total_tokens, ai_provider, ai_model) }}",
      "request_type": "{{ request.body.type }}",
      "timestamp": "{{ now }}"
    }
  }
]
```

## 🔐 **Security and Best Practices**

### API Key Management

**Environment Variable Configuration:**
```bash
# Environment variables for AI API keys
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
GOOGLE_AI_API_KEY=your-google-ai-key
```

**Secure Function Stack Pattern:**
```javascript
{
  "function": "conditional",
  "condition": "{{ !env.OPENAI_API_KEY }}",
  "true_branch": [
    {
      "function": "return_response",
      "status": 500,
      "body": {"error": "AI service configuration error"}
    }
  ]
}
```

### Input Validation and Sanitization

```javascript
// Input validation function stack
[
  {
    "function": "conditional",
    "condition": "{{ !request.body.user_message || request.body.user_message|length > 4000 }}",
    "true_branch": [
      {
        "function": "return_response",
        "status": 400,
        "body": {"error": "Invalid message length"}
      }
    ]
  },
  {
    "function": "create_variable",
    "name": "sanitized_message",
    "value": "{{ request.body.user_message|escape_html|trim }}"
  }
]
```

## 💡 **Pro Tips**

- **Start Simple**: Begin with basic text generation before adding complexity
- **Monitor Costs**: Track token usage to optimize model selection
- **Cache Responses**: Store common responses to reduce API calls
- **Fallback Models**: Have backup models for when primary services are unavailable
- **Rate Limiting**: Implement request throttling to avoid API limits
- **Content Filtering**: Add output validation for inappropriate content

## 🔧 **Troubleshooting**

### Common Issues

**Problem**: API rate limits exceeded  
**Solution**: Implement request queuing and retry logic with exponential backoff

**Problem**: High token costs  
**Solution**: Use shorter prompts, choose appropriate models, implement response caching

**Problem**: Inconsistent response quality  
**Solution**: Fine-tune prompts, adjust temperature settings, add context

**Problem**: API authentication failures  
**Solution**: Verify API keys, check environment variable configuration

---

**Next Steps**: Ready for more advanced AI features? Explore [Agents](agents.md) for complex workflows or check out [AI Tools](ai-tools.md) for additional integrations