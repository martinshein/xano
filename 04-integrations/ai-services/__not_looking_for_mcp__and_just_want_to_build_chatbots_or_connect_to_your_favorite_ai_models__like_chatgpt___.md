---
title: Simple Chatbot Development - Building AI Bots Without MCP Complexity
description: Streamlined guide for building chatbots and connecting to AI models like ChatGPT without using Model Context Protocol. Perfect for quick implementations, customer service bots, and basic AI integrations in n8n and WeWeb
category: ai-services
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - mcp-builder.md
  - agents.md
  - ai-tools.md
subcategory: 04-integrations/ai-services
tags:
  - chatbots
  - simple-ai
  - external-api
  - conversation-flow
  - customer-service
  - basic-integration
  - no-code
---

## 📋 **Quick Summary**

Build conversational AI chatbots and connect to popular AI models without the complexity of Model Context Protocol (MCP). This guide covers simple external API integrations for creating customer service bots, FAQ assistants, and basic conversational interfaces using n8n, WeWeb, and Xano's external API functions. Perfect for straightforward AI implementations.

## What You'll Learn

- When to choose simple chatbots over MCP or Agent solutions
- Setting up external API connections to AI services
- Building conversation flows and context management
- Creating persistent chat histories and user sessions
- Implementing customer service chatbot patterns
- Cost-effective AI integration strategies

# Simple Chatbot Development

## Overview

While **MCP (Model Context Protocol)** and **Xano Agents** offer powerful capabilities for complex AI workflows, sometimes you need a straightforward chatbot solution. Simple chatbot development focuses on external API integrations that provide conversational AI without the overhead of tool management or complex reasoning systems.

### Simple Chatbots vs Advanced AI Solutions

| Approach | Complexity | Best For | Features |
|----------|------------|----------|----------|
| **Simple Chatbots** | Low | FAQ, customer service, basic conversations | API calls, conversation history |
| **MCP Integration** | Medium | Structured tool usage, database operations | Standardized AI tool protocols |
| **Xano Agents** | High | Complex decision-making, multi-step workflows | Tools, reasoning, structured outputs |

### Common Chatbot Use Cases

**Customer Service:**
- Frequently asked questions
- Order status inquiries
- Basic troubleshooting
- Contact information routing

**Content Assistance:**
- Product recommendations
- Content search and retrieval
- Simple data lookups
- Form completion help

## 🚀 **Basic Chatbot Architecture**

### Core Components

1. **Conversation Management**: Store and retrieve chat history
2. **External AI Integration**: Connect to AI services via API
3. **Context Handling**: Maintain conversation context across messages
4. **Response Processing**: Format and deliver AI responses
5. **User Session Management**: Track individual user conversations

### Database Schema for Simple Chatbots

```sql
-- Conversations table
CREATE TABLE conversations (
  id INTEGER PRIMARY KEY,
  user_identifier VARCHAR(255),
  session_id VARCHAR(255),
  status VARCHAR(50) DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Messages table
CREATE TABLE messages (
  id INTEGER PRIMARY KEY,
  conversation_id INTEGER REFERENCES conversations(id),
  role VARCHAR(20), -- 'user' or 'assistant'
  content TEXT,
  metadata JSON,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat sessions table (optional for analytics)
CREATE TABLE chat_sessions (
  id INTEGER PRIMARY KEY,
  user_identifier VARCHAR(255),
  total_messages INTEGER DEFAULT 0,
  session_duration INTEGER, -- in seconds
  satisfaction_rating INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Basic Chatbot Function Stack

```javascript
// Simple chatbot endpoint function stack
[
  // Get or create conversation
  {
    "function": "conditional",
    "condition": "{{ request.body.conversation_id }}",
    "true_branch": [
      {
        "function": "get_record",
        "table": "conversations",
        "id": "{{ request.body.conversation_id }}"
      }
    ],
    "false_branch": [
      {
        "function": "add_record",
        "table": "conversations",
        "data": {
          "user_identifier": "{{ request.body.user_id || 'anonymous' }}",
          "session_id": "{{ generate_uuid() }}",
          "status": "active"
        }
      }
    ]
  },
  // Store user message
  {
    "function": "add_record",
    "table": "messages",
    "data": {
      "conversation_id": "{{ conversation.id }}",
      "role": "user",
      "content": "{{ request.body.message }}",
      "metadata": {
        "timestamp": "{{ now }}",
        "user_agent": "{{ request.headers.user_agent }}"
      }
    }
  },
  // Get recent conversation history
  {
    "function": "query_all_records",
    "table": "messages",
    "filter": {
      "conversation_id": "{{ conversation.id }}"
    },
    "sort": [{"field": "created_at", "direction": "desc"}],
    "limit": 10
  },
  // Prepare AI request with context
  {
    "function": "create_variable",
    "name": "conversation_context",
    "value": "{{ messages|reverse|map('role', 'content')|to_openai_format }}"
  },
  // Call AI service
  {
    "function": "external_api_request",
    "url": "https://api.openai.com/v1/chat/completions",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
      "Content-Type": "application/json"
    },
    "body": {
      "model": "gpt-3.5-turbo",
      "messages": "{{ conversation_context }}",
      "max_tokens": 500,
      "temperature": 0.7
    }
  },
  // Store AI response
  {
    "function": "add_record",
    "table": "messages",
    "data": {
      "conversation_id": "{{ conversation.id }}",
      "role": "assistant",
      "content": "{{ ai_response.choices[0].message.content }}",
      "metadata": {
        "model": "gpt-3.5-turbo",
        "tokens_used": "{{ ai_response.usage.total_tokens }}",
        "timestamp": "{{ now }}"
      }
    }
  },
  // Return response
  {
    "function": "return_response",
    "body": {
      "conversation_id": "{{ conversation.id }}",
      "message": "{{ ai_response.choices[0].message.content }}",
      "timestamp": "{{ now }}"
    }
  }
]
```

## 🔗 **No-Code Platform Integration**

### n8n Chatbot Workflow

**Complete Customer Service Bot:**

```javascript
// n8n workflow for customer service chatbot
{
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "Webhook",
      "parameters": {
        "path": "chatbot",
        "responseMode": "responseNode"
      }
    },
    {
      "name": "Validate Input",
      "type": "Function",
      "parameters": {
        "functionCode": `
          const message = $json.message;
          const userId = $json.user_id || 'anonymous';
          
          if (!message || message.trim().length === 0) {
            throw new Error('Message is required');
          }
          
          if (message.length > 1000) {
            throw new Error('Message too long');
          }
          
          return {
            message: message.trim(),
            user_id: userId,
            timestamp: new Date().toISOString()
          };
        `
      }
    },
    {
      "name": "Check Intent",
      "type": "Switch",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{ $json.message.toLowerCase() }}",
              "operation": "contains",
              "value2": "order status"
            },
            {
              "value1": "{{ $json.message.toLowerCase() }}",
              "operation": "contains", 
              "value2": "refund"
            },
            {
              "value1": "{{ $json.message.toLowerCase() }}",
              "operation": "contains",
              "value2": "support"
            }
          ]
        }
      }
    },
    {
      "name": "Order Status Bot",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/order-status-chat",
        "method": "POST",
        "body": {
          "message": "{{ $json.message }}",
          "user_id": "{{ $json.user_id }}",
          "conversation_id": "{{ $json.conversation_id }}",
          "context": "order_inquiry"
        }
      }
    },
    {
      "name": "Refund Bot",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/refund-chat",
        "method": "POST",
        "body": {
          "message": "{{ $json.message }}",
          "user_id": "{{ $json.user_id }}",
          "conversation_id": "{{ $json.conversation_id }}",
          "context": "refund_request"
        }
      }
    },
    {
      "name": "General Support Bot",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/general-chat",
        "method": "POST",
        "body": {
          "message": "{{ $json.message }}",
          "user_id": "{{ $json.user_id }}",
          "conversation_id": "{{ $json.conversation_id }}",
          "context": "general_support"
        }
      }
    },
    {
      "name": "Response",
      "type": "Respond to Webhook",
      "parameters": {
        "responseBody": "{{ $json }}"
      }
    }
  ]
}
```

### WeWeb Chatbot Interface

**Complete Chat Component:**

```javascript
// WeWeb chatbot component
class SimpleChatbot {
  constructor(xanoBaseUrl, userId = null) {
    this.baseUrl = xanoBaseUrl;
    this.userId = userId || this.generateAnonymousId();
    this.conversationId = null;
    this.isTyping = false;
  }
  
  generateAnonymousId() {
    return 'anon_' + Math.random().toString(36).substr(2, 9);
  }
  
  async sendMessage(messageText) {
    if (!messageText.trim() || this.isTyping) return;
    
    this.isTyping = true;
    this.updateTypingIndicator(true);
    
    try {
      // Add user message to UI immediately
      this.addMessageToUI('user', messageText);
      
      const response = await fetch(`${this.baseUrl}/api/chatbot`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: messageText,
          user_id: this.userId,
          conversation_id: this.conversationId
        })
      });
      
      const result = await response.json();
      
      if (result.conversation_id) {
        this.conversationId = result.conversation_id;
        wwLib.wwVariable.updateValue('conversation_id', this.conversationId);
      }
      
      // Add bot response to UI
      this.addMessageToUI('assistant', result.message);
      
      // Update conversation metadata
      wwLib.wwVariable.updateValue('last_message_time', new Date().toISOString());
      
      return result.message;
    } catch (error) {
      console.error('Chat request failed:', error);
      this.addMessageToUI('assistant', 'Sorry, I encountered an error. Please try again.');
      return null;
    } finally {
      this.isTyping = false;
      this.updateTypingIndicator(false);
    }
  }
  
  addMessageToUI(role, content) {
    const currentMessages = wwLib.wwVariable.getValue('chat_messages') || [];
    const newMessage = {
      id: Date.now(),
      role: role,
      content: content,
      timestamp: new Date().toISOString()
    };
    
    const updatedMessages = [...currentMessages, newMessage];
    wwLib.wwVariable.updateValue('chat_messages', updatedMessages);
    
    // Auto-scroll to bottom
    setTimeout(() => {
      wwLib.wwUtils.scrollToElement('#chat-container-bottom');
    }, 100);
  }
  
  updateTypingIndicator(isTyping) {
    wwLib.wwVariable.updateValue('bot_is_typing', isTyping);
  }
  
  async loadConversationHistory() {
    if (!this.conversationId) return;
    
    try {
      const response = await fetch(`${this.baseUrl}/api/conversation-history/${this.conversationId}`);
      const history = await response.json();
      
      wwLib.wwVariable.updateValue('chat_messages', history.messages);
    } catch (error) {
      console.error('Failed to load conversation history:', error);
    }
  }
  
  clearConversation() {
    this.conversationId = null;
    wwLib.wwVariable.updateValue('chat_messages', []);
    wwLib.wwVariable.updateValue('conversation_id', null);
  }
  
  async endConversation(rating = null) {
    if (!this.conversationId) return;
    
    try {
      await fetch(`${this.baseUrl}/api/end-conversation`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          conversation_id: this.conversationId,
          satisfaction_rating: rating
        })
      });
      
      this.clearConversation();
    } catch (error) {
      console.error('Failed to end conversation:', error);
    }
  }
}

// Initialize chatbot
const chatbot = new SimpleChatbot(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('current_user_id')
);

// Event handlers for WeWeb
async function handleSendMessage() {
  const userInput = wwLib.wwVariable.getValue('user_input');
  
  if (userInput.trim()) {
    await chatbot.sendMessage(userInput);
    wwLib.wwVariable.updateValue('user_input', '');
  }
}

function handleKeyPress(event) {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    handleSendMessage();
  }
}

async function handleEndChat() {
  const rating = wwLib.wwVariable.getValue('user_rating');
  await chatbot.endConversation(rating);
  wwLib.wwModal.close('chat-modal');
}

// Auto-load conversation if ID exists
const existingConversationId = wwLib.wwVariable.getValue('conversation_id');
if (existingConversationId) {
  chatbot.conversationId = existingConversationId;
  chatbot.loadConversationHistory();
}
```

## 🛠️ **Specialized Chatbot Patterns**

### FAQ Bot with Context Awareness

**Knowledge Base Integration:**

```javascript
// FAQ bot function stack
[
  // Search knowledge base first
  {
    "function": "query_all_records",
    "table": "knowledge_base",
    "filter": {
      "keywords": {
        "contains": "{{ request.body.message|extract_keywords }}"
      },
      "status": "published"
    },
    "sort": [{"field": "relevance_score", "direction": "desc"}],
    "limit": 3
  },
  // If knowledge base has results, use them
  {
    "function": "conditional",
    "condition": "{{ knowledge_base_results|length > 0 }}",
    "true_branch": [
      {
        "function": "external_api_request",
        "url": "https://api.openai.com/v1/chat/completions",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "model": "gpt-3.5-turbo",
          "messages": [
            {
              "role": "system",
              "content": "You are a helpful FAQ assistant. Use the provided knowledge base articles to answer questions accurately. If the question isn't covered in the knowledge base, say so clearly."
            },
            {
              "role": "user",
              "content": "Question: {{ request.body.message }}\n\nKnowledge Base:\n{{ knowledge_base_results|map('title', 'content')|join('\n\n') }}"
            }
          ],
          "max_tokens": 300
        }
      }
    ],
    "false_branch": [
      {
        "function": "external_api_request",
        "url": "https://api.openai.com/v1/chat/completions",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "model": "gpt-3.5-turbo",
          "messages": [
            {
              "role": "system",
              "content": "You are a helpful assistant. If you cannot answer a question based on general knowledge, suggest contacting customer support."
            },
            {
              "role": "user",
              "content": "{{ request.body.message }}"
            }
          ],
          "max_tokens": 200
        }
      }
    ]
  }
]
```

### Customer Service Bot with Escalation

**Support Escalation Pattern:**

```javascript
// Customer service bot with escalation
[
  // Analyze message intent and urgency
  {
    "function": "external_api_request",
    "url": "https://api.openai.com/v1/chat/completions",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
      "Content-Type": "application/json"
    },
    "body": {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "system",
          "content": "Analyze this customer message and return JSON with intent (billing, technical, general) and urgency (low, medium, high, urgent)."
        },
        {
          "role": "user",
          "content": "{{ request.body.message }}"
        }
      ],
      "max_tokens": 100
    },
    "return_as": "intent_analysis"
  },
  // Check if escalation needed
  {
    "function": "conditional",
    "condition": "{{ intent_analysis.urgency == 'urgent' || request.body.message|contains('speak to human') }}",
    "true_branch": [
      // Create support ticket
      {
        "function": "add_record",
        "table": "support_tickets",
        "data": {
          "user_id": "{{ request.body.user_id }}",
          "conversation_id": "{{ request.body.conversation_id }}",
          "message": "{{ request.body.message }}",
          "priority": "high",
          "status": "open",
          "source": "chatbot_escalation"
        }
      },
      {
        "function": "return_response",
        "body": {
          "message": "I understand this is urgent. I've created a support ticket (#{{ support_ticket.id }}) and a human agent will contact you within 15 minutes.",
          "escalated": true,
          "ticket_id": "{{ support_ticket.id }}"
        }
      }
    ],
    "false_branch": [
      // Continue with AI response
      {
        "function": "external_api_request",
        "url": "https://api.openai.com/v1/chat/completions",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ env.OPENAI_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "model": "gpt-3.5-turbo",
          "messages": [
            {
              "role": "system",
              "content": "You are a friendly customer service assistant. Provide helpful, accurate information. If you cannot resolve an issue, offer to escalate to a human agent."
            },
            {
              "role": "user",
              "content": "{{ request.body.message }}"
            }
          ],
          "max_tokens": 400
        }
      }
    ]
  }
]
```

## 💰 **Cost Optimization for Simple Chatbots**

### Smart Model Selection

**Cost-Effective AI Routing:**

```javascript
// Function to choose AI model based on complexity
{
  "function": "conditional",
  "condition": "{{ request.body.message|word_count < 20 && request.body.message|complexity_score < 5 }}",
  "true_branch": [
    // Use cheaper model for simple queries
    {
      "function": "external_api_request",
      "url": "https://api.openai.com/v1/chat/completions",
      "body": {
        "model": "gpt-3.5-turbo",
        "max_tokens": 150
      }
    }
  ],
  "false_branch": [
    // Use more capable model for complex queries
    {
      "function": "external_api_request", 
      "url": "https://api.openai.com/v1/chat/completions",
      "body": {
        "model": "gpt-4",
        "max_tokens": 300
      }
    }
  ]
}
```

### Response Caching

**Reduce API Calls with Caching:**

```javascript
// Cache common responses
[
  // Check cache first
  {
    "function": "get_cached_data",
    "key": "chat_response_{{ request.body.message|hash }}",
    "ttl": 3600
  },
  {
    "function": "conditional",
    "condition": "{{ !cached_response }}",
    "true_branch": [
      // Generate new response
      {
        "function": "external_api_request",
        "url": "https://api.openai.com/v1/chat/completions",
        "method": "POST",
        "body": "{{ ai_request_body }}"
      },
      // Cache the response
      {
        "function": "set_cached_data",
        "key": "chat_response_{{ request.body.message|hash }}",
        "value": "{{ ai_response.choices[0].message.content }}",
        "ttl": 3600
      }
    ]
  }
]
```

## 💡 **Pro Tips**

- **Start Simple**: Begin with basic Q&A before adding complex features
- **Monitor Conversations**: Track common questions to improve responses
- **Implement Fallbacks**: Always have escalation paths to human support
- **Optimize Context**: Keep conversation history relevant but concise
- **Test Regularly**: Use real user scenarios to validate bot responses
- **Track Metrics**: Monitor response quality and user satisfaction

## 🔧 **Troubleshooting**

### Common Issues

**Problem**: Bot responses are inconsistent  
**Solution**: Improve system prompts and add conversation context

**Problem**: High API costs  
**Solution**: Implement response caching and smart model selection

**Problem**: Users frustrated with bot limitations  
**Solution**: Clear escalation paths and expectation setting

**Problem**: Conversation context gets lost  
**Solution**: Implement proper conversation history management

---

**Next Steps**: Ready for more advanced AI features? Explore [MCP Builder](mcp-builder.md) for tool integration or [Agents](agents.md) for complex decision-making workflows