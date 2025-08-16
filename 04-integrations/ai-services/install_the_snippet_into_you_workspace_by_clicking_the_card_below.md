---
title: Installing Xano AI Snippets - Quick Start Templates for AI Agents
description: Complete guide to installing and configuring Xano AI templates including Agent History & Debugging Mode and Conversation History snippets for building intelligent chatbots and automated workflows
category: ai-services
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - templates.md
  - ai-tools.md
  - agents.md
subcategory: 04-integrations/ai-services
tags:
  - templates
  - snippets
  - installation
  - agent-history
  - conversation-management
  - chatbots
  - no-code
---

## 📋 **Quick Summary**

Install pre-built AI templates into your Xano workspace to rapidly set up agent monitoring, conversation history, and chatbot functionality. These snippets provide complete database schemas, API endpoints, and monitoring dashboards that integrate seamlessly with n8n, WeWeb, and other no-code platforms for building intelligent applications.

## What You'll Learn

- How to install and configure Xano AI snippets
- Setting up Agent History & Debugging Mode for monitoring
- Implementing Conversation History for chatbot persistence
- Configuring authentication and security for AI templates
- Integration patterns for no-code platform development
- Best practices for template customization

# Installing Xano AI Snippets

## Overview

**Xano AI Snippets** are pre-built templates that provide complete infrastructure for common AI use cases. Instead of building agent monitoring, conversation management, and debugging tools from scratch, these snippets give you production-ready functionality that you can customize for your specific needs.

### Available Templates

**Agent History & Debugging Mode:**
- Complete agent execution logging
- Performance monitoring dashboard
- Debugging tools for AI behavior analysis
- Database tables for run history and analytics

**Conversation History:**
- Persistent user interaction storage
- Message threading and context management
- Authentication system for secure access
- Ready-to-use chatbot interface

## 🚀 **Agent History & Debugging Mode**

### What This Template Provides

**Database Architecture:**
- `agents` table: Store agent configurations and metadata
- `agent_runs` table: Log each agent execution with timestamps
- `agent_steps` table: Track individual steps within runs
- `agent_tool_calls` table: Monitor tool usage and performance

**API Infrastructure:**
- Automated logging functions
- Performance monitoring endpoints
- Dashboard for debugging agent behavior
- Analytics queries for usage patterns

**Monitoring Dashboard:**
- Real-time agent performance statistics
- Detailed run analysis and debugging
- Tool usage analytics
- Error tracking and reporting

### Installation Steps

#### Step 1: Install the Snippet

1. **Access Templates**: Navigate to your Xano workspace
2. **Browse Snippets**: Go to the Templates or Snippets section
3. **Select Template**: Click on **"Agent History & Debugging Mode"** card
4. **Install**: Click the install button to add to your workspace

#### Step 2: Configure API Group

1. **Find Agent History API Group**: Locate the newly created API group
2. **Copy Base URL**: Copy the API group's base URL from the settings
3. **Update Dashboard**: Navigate to the Dashboard API endpoint
4. **Set Base URL Variable**: Paste the URL into the `api_group_base_url` variable
5. **Publish Endpoint**: Deploy the dashboard endpoint

#### Step 3: Database Configuration

1. **Add Agent Record**: In the `agents` table, create a record for your AI agent
2. **Create Dashboard User**: Add credentials to the `agent_user` table for secure access
3. **Configure Permissions**: Set appropriate access levels for monitoring

#### Step 4: Integrate Logging

1. **Find Function Stacks**: Locate existing function stacks that use AI agents
2. **Add Logging Function**: After each "Call Agent" function, add the `log_agent` custom function
3. **Configure Capture**: Ensure the logging function captures the agent's response

## 🔗 **No-Code Platform Integration**

### n8n Workflow with Agent Monitoring

**Automated Agent Performance Tracking:**

```javascript
// n8n HTTP Request node for agent logging
{
  "method": "POST",
  "url": "https://your-xano-instance.com/api/agent-history/log",
  "headers": {
    "Authorization": "Bearer {{ $json.auth_token }}",
    "Content-Type": "application/json"
  },
  "body": {
    "agent_id": "{{ $json.agent_id }}",
    "user_input": "{{ $json.user_message }}",
    "agent_response": "{{ $json.ai_response }}",
    "execution_time": "{{ $json.response_time }}",
    "tools_used": "{{ $json.tools_called }}",
    "success": "{{ $json.execution_success }}"
  }
}
```

### WeWeb Agent Dashboard Integration

**Real-time Agent Monitoring Component:**

```javascript
// WeWeb component for agent performance monitoring
class XanoAgentMonitor {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async getAgentStats(agentId, timeframe = '24h') {
    try {
      const response = await fetch(`${this.baseUrl}/api/agent-history/stats`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          agent_id: agentId,
          timeframe: timeframe
        })
      });
      
      const stats = await response.json();
      
      // Update WeWeb dashboard variables
      wwLib.wwVariable.updateValue('agent_total_runs', stats.total_runs);
      wwLib.wwVariable.updateValue('agent_success_rate', stats.success_rate);
      wwLib.wwVariable.updateValue('agent_avg_response_time', stats.avg_response_time);
      wwLib.wwVariable.updateValue('agent_tool_usage', stats.tool_usage);
      
      return stats;
    } catch (error) {
      console.error('Agent stats retrieval failed:', error);
      return { error: 'Stats unavailable' };
    }
  }
  
  async getRecentRuns(agentId, limit = 10) {
    try {
      const response = await fetch(`${this.baseUrl}/api/agent-history/recent-runs`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          agent_id: agentId,
          limit: limit
        })
      });
      
      const runs = await response.json();
      
      // Update recent runs display
      wwLib.wwVariable.updateValue('recent_agent_runs', runs);
      
      return runs;
    } catch (error) {
      console.error('Recent runs retrieval failed:', error);
      return [];
    }
  }
  
  async debugRun(runId) {
    try {
      const response = await fetch(`${this.baseUrl}/api/agent-history/debug/${runId}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        }
      });
      
      const debugInfo = await response.json();
      
      // Open debug modal with detailed information
      wwLib.wwVariable.updateValue('debug_run_details', debugInfo);
      wwLib.wwModal.open('agent-debug-modal');
      
      return debugInfo;
    } catch (error) {
      console.error('Debug run failed:', error);
      return { error: 'Debug info unavailable' };
    }
  }
}

// Usage in WeWeb
const agentMonitor = new XanoAgentMonitor(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

async function loadAgentDashboard() {
  const agentId = wwLib.wwVariable.getValue('current_agent_id');
  
  // Load performance stats
  const stats = await agentMonitor.getAgentStats(agentId);
  
  // Load recent runs
  const recentRuns = await agentMonitor.getRecentRuns(agentId);
  
  // Update dashboard display
  if (!stats.error && !recentRuns.error) {
    wwLib.wwVariable.updateValue('dashboard_loaded', true);
  }
}
```

## 💬 **Conversation History Template**

### What This Template Provides

**Database Schema:**
- `conversations` table: Store conversation threads and metadata
- `messages` table: Individual message storage with context
- `agent_user` table: User authentication and session management

**API Endpoints:**
- Authentication endpoints (`auth/login`, `auth/me`)
- Conversation management APIs
- Message persistence and retrieval
- Chatbot interface endpoints

**Ready-to-Use Interface:**
- Complete chatbot UI for testing
- Authentication flow implementation
- Message threading and history display

### Installation and Configuration

#### Step 1: Install Conversation History Snippet

1. **Select Template**: Click on the **"Conversation History"** snippet card
2. **Install to Workspace**: Add the template to your workspace
3. **Verify Installation**: Check that all tables and API groups were created

#### Step 2: Configure API Endpoints

1. **Navigate to Chatbot API Group**: Find the newly created API group
2. **Copy Base URL**: Get the API group's base URL
3. **Update Variables**: In the `/chatbot` endpoint, update the `api_group_base_url` variable
4. **Configure Agent Integration**: In the `/conversation` endpoint, add your AI agent

#### Step 3: Set Up Agent Integration

**Prerequisites Check:**
- Agent must be configured with prompt type set to **"Messages"**
- Agent messages value must be set to: `{}`

**Integration Steps:**
1. **Add Call AI Agent Function**: In step 4 of the conversation endpoint
2. **Configure Agent Output**: In step 5, update `agent_response` variable to use the agent's output
3. **Test Integration**: Verify agent responds correctly to conversation context

### WeWeb Chatbot Integration

**Complete Chatbot Component:**

```javascript
// WeWeb chatbot integration with Xano conversation history
class XanoChatbot {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.conversationId = null;
  }
  
  async authenticate(username, password) {
    try {
      const response = await fetch(`${this.baseUrl}/api/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: username,
          password: password
        })
      });
      
      const authResult = await response.json();
      
      if (authResult.authToken) {
        this.authToken = authResult.authToken;
        wwLib.wwVariable.updateValue('chat_auth_token', authResult.authToken);
        wwLib.wwVariable.updateValue('current_user', authResult.user);
        return true;
      }
      
      return false;
    } catch (error) {
      console.error('Authentication failed:', error);
      return false;
    }
  }
  
  async startConversation() {
    try {
      const response = await fetch(`${this.baseUrl}/api/chatbot/start-conversation`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          user_id: wwLib.wwVariable.getValue('current_user').id
        })
      });
      
      const conversation = await response.json();
      this.conversationId = conversation.id;
      
      wwLib.wwVariable.updateValue('current_conversation_id', conversation.id);
      wwLib.wwVariable.updateValue('conversation_messages', []);
      
      return conversation;
    } catch (error) {
      console.error('Failed to start conversation:', error);
      return null;
    }
  }
  
  async sendMessage(messageText) {
    if (!this.conversationId) {
      await this.startConversation();
    }
    
    try {
      const response = await fetch(`${this.baseUrl}/api/chatbot/conversation`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          conversation_id: this.conversationId,
          message: messageText
        })
      });
      
      const result = await response.json();
      
      // Update message history
      const currentMessages = wwLib.wwVariable.getValue('conversation_messages') || [];
      const updatedMessages = [
        ...currentMessages,
        {
          type: 'user',
          content: messageText,
          timestamp: new Date().toISOString()
        },
        {
          type: 'assistant',
          content: result.agent_response,
          timestamp: new Date().toISOString()
        }
      ];
      
      wwLib.wwVariable.updateValue('conversation_messages', updatedMessages);
      
      return result.agent_response;
    } catch (error) {
      console.error('Failed to send message:', error);
      return 'Sorry, I encountered an error. Please try again.';
    }
  }
  
  async loadConversationHistory(conversationId) {
    try {
      const response = await fetch(`${this.baseUrl}/api/chatbot/history/${conversationId}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        }
      });
      
      const history = await response.json();
      wwLib.wwVariable.updateValue('conversation_messages', history.messages);
      
      return history;
    } catch (error) {
      console.error('Failed to load conversation history:', error);
      return { messages: [] };
    }
  }
}

// Usage in WeWeb
const chatbot = new XanoChatbot(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('chat_auth_token')
);

async function handleUserMessage() {
  const userInput = wwLib.wwVariable.getValue('user_input');
  
  if (userInput.trim()) {
    const response = await chatbot.sendMessage(userInput);
    
    // Clear input field
    wwLib.wwVariable.updateValue('user_input', '');
    
    // Scroll to bottom of chat
    wwLib.wwUtils.scrollToElement('#chat-container-bottom');
  }
}
```

## 🔐 **Security and Authentication**

### Template Security Features

**Built-in Authentication:**
- Secure user authentication system
- Token-based session management
- Password hashing and validation
- Role-based access control

**Dashboard Protection:**
- Authenticated access to monitoring dashboards
- User session management
- Secure API endpoint access

### Security Best Practices

```javascript
// Secure configuration example
{
  "authentication": {
    "token_expiration": "24h",
    "password_min_length": 8,
    "max_login_attempts": 3,
    "lockout_duration": "15m"
  },
  "dashboard_access": {
    "allowed_roles": ["admin", "developer"],
    "session_timeout": "2h",
    "require_2fa": false
  },
  "api_security": {
    "rate_limiting": {
      "requests_per_minute": 60,
      "burst_limit": 10
    },
    "cors_enabled": true,
    "allowed_origins": ["https://yourdomain.com"]
  }
}
```

## 🛠️ **Customization and Extension**

### Template Modification Patterns

**Adding Custom Fields:**
```sql
-- Extend agent_runs table with custom metrics
ALTER TABLE agent_runs ADD COLUMN custom_metric_1 DECIMAL(10,2);
ALTER TABLE agent_runs ADD COLUMN business_context TEXT;
ALTER TABLE agent_runs ADD COLUMN user_satisfaction INTEGER;
```

**Custom Dashboard Widgets:**
```javascript
// Custom performance metric calculation
{
  "function": "direct_database_query",
  "sql": "SELECT AVG(response_time) as avg_response, COUNT(*) as total_runs FROM agent_runs WHERE created_at >= NOW() - INTERVAL 24 HOUR AND agent_id = ?",
  "parameters": ["{{ request.query.agent_id }}"]
}
```

### Integration Extensions

**Third-Party Analytics:**
- Google Analytics event tracking
- Custom metrics dashboards
- Business intelligence integration
- Performance alerting systems

## 💡 **Pro Tips**

- **Start with Templates**: Use snippets as starting points, then customize for your needs
- **Monitor Performance**: Regularly review agent debugging dashboards
- **Secure Access**: Always configure authentication for production deployments
- **Backup Conversations**: Implement regular backup strategies for conversation data
- **Scale Gradually**: Test templates with small user groups before full deployment

## 🔧 **Troubleshooting**

### Common Installation Issues

**Problem**: Snippet installation fails  
**Solution**: Verify workspace permissions and available storage

**Problem**: API endpoints not working after installation  
**Solution**: Check base URL configuration and publish all endpoints

**Problem**: Dashboard authentication fails  
**Solution**: Verify user records in agent_user table and password encryption

**Problem**: Agent logging not capturing data  
**Solution**: Ensure log_agent function is placed after Call Agent functions

---

**Next Steps**: Ready to explore more AI features? Check out [AI Tools](ai-tools.md) for advanced capabilities or visit [Templates](templates.md) for additional snippets