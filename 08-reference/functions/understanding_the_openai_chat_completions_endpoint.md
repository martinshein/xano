---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- CRUD
- OpenAI
- Chatbots
- AI Integration
title: Understanding the OpenAI Chat Completions Endpoint
---

# Understanding the OpenAI Chat Completions Endpoint

## 📋 **Quick Summary**
The OpenAI Chat Completions endpoint enables building conversational AI applications in Xano. It requires sending the complete conversation history with each request, proper authentication, and structured message objects to maintain context and generate intelligent responses from GPT models.
## 🎯 **Core Concepts**

### OpenAI Chat Completions API
- **Endpoint**: `/v1/chat/completions`
- **Method**: POST requests with JSON payload
- **Authentication**: Bearer token (OpenAI API key)
- **Conversation History**: Complete message array required for each request
- **Model Selection**: Choose from available GPT models (gpt-3.5-turbo, gpt-4, etc.)

### Message Structure
- **Role-based messaging**: `system`, `user`, `assistant` roles
- **Content preservation**: Full conversation context maintained
- **Sequential processing**: Messages processed in chronological order
- **Context management**: API stateless, requires complete history

## 🛠️ **Implementation Guide**

### Prerequisites
Before building a chatbot with Xano and OpenAI, ensure you understand:
- Database table creation and management
- Xano function stack development
- External API Request function usage
- User authentication and data handling
### Step 1: Understanding OpenAI Chat Completions Endpoint

```javascript
// OpenAI Chat Completions API Structure
const apiRequest = {
  "url": "https://api.openai.com/v1/chat/completions",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer sk-...", // Your OpenAI API key
    "Content-Type": "application/json"
  },
  "body": {
    "model": "gpt-3.5-turbo", // or gpt-4, gpt-4-turbo, etc.
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful customer service assistant."
      },
      {
        "role": "user", 
        "content": "Hello, I need help with my order."
      },
      {
        "role": "assistant",
        "content": "I'd be happy to help! Can you provide your order number?"
      },
      {
        "role": "user",
        "content": "My order number is 12345."
      }
    ],
    "temperature": 0.7, // Optional: creativity level (0-2)
    "max_tokens": 1000   // Optional: response length limit
  }
}

// API Response Structure
const apiResponse = {
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I found your order #12345. It was shipped yesterday and should arrive by tomorrow."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 56,
    "completion_tokens": 31,
    "total_tokens": 87
  }
}
```

### Step 2: Database Schema Design

```sql
-- User Table
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Conversation Table (Parent)
CREATE TABLE conversations (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL, -- "Customer Support Chat", "Product Questions"
  model TEXT DEFAULT 'gpt-3.5-turbo', -- OpenAI model used
  user_id INTEGER REFERENCES users(id),
  system_prompt TEXT, -- Initial AI context/instructions
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Messages Table (Child)
CREATE TABLE messages (
  id INTEGER PRIMARY KEY,
  conversation_id INTEGER REFERENCES conversations(id),
  role TEXT CHECK(role IN ('system', 'user', 'assistant')),
  content TEXT NOT NULL,
  index INTEGER NOT NULL, -- Message order (0, 1, 2, ...)
  tokens_used INTEGER, -- Track token consumption
  created_at TIMESTAMP DEFAULT NOW()
);
```

```javascript
// Xano Database Table Configuration
const databaseTables = {
  "users": {
    "fields": {
      "id": { "type": "integer", "primary_key": true },
      "name": { "type": "text", "required": true },
      "email": { "type": "text", "unique": true },
      "created_at": { "type": "datetime", "default": "now" }
    }
  },
  "conversations": {
    "fields": {
      "id": { "type": "integer", "primary_key": true },
      "name": { "type": "text", "required": true },
      "model": { "type": "text", "default": "gpt-3.5-turbo" },
      "user_id": { "type": "table_reference", "reference": "users" },
      "system_prompt": { "type": "text" },
      "created_at": { "type": "datetime", "default": "now" },
      "updated_at": { "type": "datetime", "default": "now" }
    }
  },
  "messages": {
    "fields": {
      "id": { "type": "integer", "primary_key": true },
      "conversation_id": { "type": "table_reference", "reference": "conversations" },
      "role": { "type": "text", "enum": ["system", "user", "assistant"] },
      "content": { "type": "text", "required": true },
      "index": { "type": "integer", "required": true },
      "tokens_used": { "type": "integer" },
      "created_at": { "type": "datetime", "default": "now" }
    }
  }
}
```

### Step 3: Create OpenAI Endpoint in Xano
```javascript
// Xano Function Stack for OpenAI Integration

// API Endpoint: send_message_to_openai
// Inputs:
// - conversation_id (Table Reference -> conversations)
// - user_message (Text)

// Function Stack Steps:
{
  "steps": [
    // Step 1: Get OpenAI API Key from Environment Variables
    {
      "function": "Get Environment Variable",
      "variable": "OPENAI_API_KEY",
      "return_variable": "openai_key"
    },
    
    // Step 2: Get Conversation History
    {
      "function": "Query All Records",
      "table": "messages",
      "filter": {
        "conversation_id": "{{inputs.conversation_id}}"
      },
      "sort": {
        "field": "index",
        "order": "ascending"
      },
      "return_variable": "message_history"
    },
    
    // Step 3: Get Next Index Number
    {
      "function": "Math",
      "operation": "add",
      "value1": "{{message_history.length}}",
      "value2": 1,
      "return_variable": "next_index"
    },
    
    // Step 4: Add User Message to History (Temporary)
    {
      "function": "Arrays",
      "operation": "append",
      "array": "{{message_history}}",
      "item": {
        "role": "user",
        "content": "{{inputs.user_message}}"
      },
      "return_variable": "updated_history"
    },
    
    // Step 5: Call OpenAI API
    {
      "function": "External API Request",
      "url": "https://api.openai.com/v1/chat/completions",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer {{openai_key}}",
        "Content-Type": "application/json"
      },
      "body": {
        "model": "gpt-3.5-turbo",
        "messages": "{{updated_history}}",
        "temperature": 0.7,
        "max_tokens": 1000
      },
      "return_variable": "openai_response"
    },
    
    // Step 6: Extract Assistant Response
    {
      "function": "Create Variable",
      "variable": "assistant_message",
      "value": "{{openai_response.choices[0].message.content}}"
    },
    
    // Step 7: Save User Message to Database
    {
      "function": "Add Record",
      "table": "messages",
      "data": {
        "conversation_id": "{{inputs.conversation_id}}",
        "role": "user",
        "content": "{{inputs.user_message}}",
        "index": "{{next_index}}",
        "tokens_used": "{{openai_response.usage.prompt_tokens}}"
      }
    },
    
    // Step 8: Save Assistant Response to Database
    {
      "function": "Add Record",
      "table": "messages",
      "data": {
        "conversation_id": "{{inputs.conversation_id}}",
        "role": "assistant",
        "content": "{{assistant_message}}",
        "index": "{{next_index + 1}}",
        "tokens_used": "{{openai_response.usage.completion_tokens}}"
      }
    },
    
    // Step 9: Update Conversation Timestamp
    {
      "function": "Edit Record",
      "table": "conversations",
      "record_id": "{{inputs.conversation_id}}",
      "data": {
        "updated_at": "{{timestamp}}"
      }
    }
  ],
  
  // Return Response
  "response": {
    "success": true,
    "assistant_message": "{{assistant_message}}",
    "conversation_id": "{{inputs.conversation_id}}",
    "tokens_used": "{{openai_response.usage.total_tokens}}"
  }
}
```

## 🔗 **Integration Examples**

### n8n Chatbot Workflow
```javascript
// n8n HTTP Request to Xano Chatbot Endpoint
{
  "method": "POST",
  "url": "https://your-xano.xano.io/api:v1/send_message_to_openai",
  "headers": {
    "Authorization": "Bearer {{$json.user_token}}",
    "Content-Type": "application/json"
  },
  "body": {
    "conversation_id": "{{$json.conversation_id}}",
    "user_message": "{{$json.message}}"
  }
}

// Follow-up n8n processing
// Send response to user via email, SMS, or webhook
{
  "recipient": "{{$json.user_email}}",
  "subject": "AI Assistant Response",
  "message": "{{$json.assistant_message}}"
}
```

### WeWeb Chatbot Interface
```vue
<template>
  <div class="chatbot-container">
    <div class="chat-messages" ref="messagesContainer">
      <div 
        v-for="message in messages" 
        :key="message.id"
        :class="['message', message.role]"
      >
        <div class="message-content">{{ message.content }}</div>
        <div class="message-time">{{ formatTime(message.created_at) }}</div>
      </div>
      
      <div v-if="isTyping" class="typing-indicator">
        AI is typing...
      </div>
    </div>
    
    <div class="chat-input">
      <input 
        v-model="newMessage" 
        @keyup.enter="sendMessage"
        :disabled="isTyping"
        placeholder="Type your message..."
      />
      <button 
        @click="sendMessage" 
        :disabled="isTyping || !newMessage.trim()"
      >
        Send
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    conversationId: String,
    userId: String
  },
  data() {
    return {
      messages: [],
      newMessage: '',
      isTyping: false
    }
  },
  async mounted() {
    await this.loadConversationHistory()
  },
  methods: {
    async loadConversationHistory() {
      try {
        const response = await this.$xano.auth.get(`/messages`, {
          filter: { conversation_id: this.conversationId },
          sort: { field: 'index', order: 'asc' }
        })
        this.messages = response.data
        this.scrollToBottom()
      } catch (error) {
        console.error('Error loading conversation:', error)
      }
    },
    
    async sendMessage() {
      if (!this.newMessage.trim()) return
      
      // Add user message to UI immediately
      const userMessage = {
        role: 'user',
        content: this.newMessage,
        created_at: new Date().toISOString()
      }
      this.messages.push(userMessage)
      
      const messageToSend = this.newMessage
      this.newMessage = ''
      this.isTyping = true
      
      try {
        // Call Xano chatbot endpoint
        const response = await this.$xano.auth.post('/send_message_to_openai', {
          conversation_id: this.conversationId,
          user_message: messageToSend
        })
        
        // Add assistant response to UI
        const assistantMessage = {
          role: 'assistant',
          content: response.assistant_message,
          created_at: new Date().toISOString()
        }
        this.messages.push(assistantMessage)
        
      } catch (error) {
        console.error('Error sending message:', error)
        // Add error message to UI
        this.messages.push({
          role: 'assistant',
          content: 'Sorry, I encountered an error. Please try again.',
          created_at: new Date().toISOString()
        })
      } finally {
        this.isTyping = false
        this.scrollToBottom()
      }
    },
    
    scrollToBottom() {
      this.$nextTick(() => {
        const container = this.$refs.messagesContainer
        container.scrollTop = container.scrollHeight
      })
    },
    
    formatTime(timestamp) {
      return new Date(timestamp).toLocaleTimeString([], {
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  }
}
</script>

<style scoped>
.chatbot-container {
  display: flex;
  flex-direction: column;
  height: 500px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  background-color: #f9f9f9;
}

.message {
  margin-bottom: 12px;
  padding: 8px 12px;
  border-radius: 8px;
  max-width: 80%;
}

.message.user {
  background-color: #007bff;
  color: white;
  margin-left: auto;
  text-align: right;
}

.message.assistant {
  background-color: white;
  border: 1px solid #ddd;
}

.message.system {
  background-color: #6c757d;
  color: white;
  font-style: italic;
  text-align: center;
  margin: 0 auto;
}

.message-time {
  font-size: 0.8em;
  opacity: 0.7;
  margin-top: 4px;
}

.typing-indicator {
  font-style: italic;
  color: #6c757d;
  padding: 8px 12px;
}

.chat-input {
  display: flex;
  padding: 16px;
  border-top: 1px solid #ddd;
  background-color: white;
}

.chat-input input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 8px;
}

.chat-input button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.chat-input button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}
</style>
```

## 🚀 **Advanced Usage Patterns**

### System Prompt Management
```javascript
// Dynamic system prompts based on conversation type
const systemPrompts = {
  "customer_support": "You are a helpful customer service representative. Be polite, professional, and focus on resolving customer issues efficiently.",
  "technical_support": "You are a technical support specialist. Provide step-by-step instructions and ask clarifying questions when needed.",
  "sales": "You are a sales assistant. Help customers find the right products and answer questions about features and pricing.",
  "general": "You are a helpful AI assistant. Provide accurate information and assist with various tasks."
}

// Function to initialize conversation with system prompt
{
  "function": "Add Record",
  "table": "messages",
  "data": {
    "conversation_id": "{{new_conversation.id}}",
    "role": "system",
    "content": "{{systemPrompts[conversation_type]}}",
    "index": 0
  }
}
```

### Token Usage Tracking
```javascript
// Monitor and limit token usage per user
{
  "function": "Query All Records",
  "table": "messages",
  "filter": {
    "conversation.user_id": "{{auth_user.id}}",
    "created_at": {
      ">=": "{{start_of_month}}"
    }
  },
  "return_variable": "monthly_messages"
}

// Calculate total tokens used this month
{
  "function": "Math",
  "operation": "sum",
  "values": "{{monthly_messages.tokens_used}}",
  "return_variable": "monthly_tokens"
}

// Check if user is within limits
{
  "function": "Conditional",
  "condition": "{{monthly_tokens > user.token_limit}}",
  "true_steps": [
    {
      "function": "Response",
      "status_code": 429,
      "message": "Monthly token limit exceeded. Please upgrade your plan."
    }
  ]
}
```

### Conversation Branching
```javascript
// Create conversation branches for different topics
function createConversationBranch(parentConversationId, branchTopic) {
  return {
    "function": "Add Record",
    "table": "conversations",
    "data": {
      "name": `${branchTopic} - Branch`,
      "user_id": "{{auth_user.id}}",
      "parent_conversation_id": parentConversationId,
      "model": "gpt-3.5-turbo",
      "system_prompt": `Continue the conversation focusing on: ${branchTopic}`
    }
  }
}
```

## 🎯 **Best Practices**

### 1. Error Handling
```javascript
// Robust error handling for OpenAI API calls
try {
  const response = await callOpenAI(messages)
  return response
} catch (error) {
  if (error.status === 429) {
    return "I'm currently experiencing high demand. Please try again in a moment."
  } else if (error.status === 401) {
    return "Authentication error. Please contact support."
  } else if (error.status === 400) {
    return "I had trouble understanding your request. Could you rephrase it?"
  } else {
    return "I'm temporarily unavailable. Please try again later."
  }
}
```

### 2. Message Filtering
```javascript
// Filter sensitive content before sending to OpenAI
const contentFilters = {
  "remove_pii": /\b\d{3}-\d{2}-\d{4}\b|\b\d{16}\b/g, // SSN, credit cards
  "remove_profanity": /\b(badword1|badword2)\b/gi,
  "remove_urls": /https?:\/\/[^\s]+/g
}

function sanitizeMessage(content) {
  let cleaned = content
  Object.values(contentFilters).forEach(filter => {
    cleaned = cleaned.replace(filter, '[REDACTED]')
  })
  return cleaned
}
```

### 3. Performance Optimization
```javascript
// Limit conversation history to prevent large payloads
const MAX_MESSAGES = 20 // Keep last 20 messages for context

{
  "function": "Query All Records",
  "table": "messages",
  "filter": {
    "conversation_id": "{{inputs.conversation_id}}"
  },
  "sort": { "field": "index", "order": "descending" },
  "limit": MAX_MESSAGES,
  "return_variable": "recent_messages"
}

// Reverse array to get chronological order
{
  "function": "Arrays",
  "operation": "reverse",
  "array": "{{recent_messages}}",
  "return_variable": "conversation_history"
}
```

---

*This comprehensive guide enables you to build sophisticated chatbot applications using OpenAI's powerful language models with Xano's backend infrastructure.*