---
title: "Realtime Functions"
description: "Enable live data updates and real-time communication in your applications using Xano's realtime functions"
category: function-stack
difficulty: advanced
tags:
  - realtime
  - websockets
  - live-updates
  - notifications
  - channels
  - collaboration
related_docs:
  - triggers
  - webhooks
  - middleware
  - background-tasks
last_updated: '2025-01-23'
---

# Realtime Functions

## Quick Summary
Realtime functions enable live data updates, instant notifications, and real-time communication features in your applications without complex WebSocket management. Perfect for chat systems, collaborative tools, live dashboards, and instant notifications.

## What You'll Learn
- Setting up realtime channels and subscriptions
- Broadcasting live data updates to connected clients
- Building collaborative features with realtime sync
- Implementing chat and messaging systems
- Integration patterns for n8n automation and WeWeb interfaces

## Core Realtime Concepts

### Channels and Subscriptions
- **Channels** - Named rooms where clients can subscribe to receive updates
- **Subscriptions** - Client connections listening for channel updates
- **Broadcasting** - Sending data to all channel subscribers
- **Private Channels** - Secured channels with authentication
- **Presence** - Track who's currently online in a channel

### Event Types
- **Data Updates** - Real-time database changes
- **User Messages** - Chat and communication
- **System Notifications** - Alerts and status updates
- **Presence Changes** - User join/leave events
- **Custom Events** - Application-specific realtime data

## Basic Realtime Setup

### Channel Creation and Subscription
```javascript
// Xano function to create/join a realtime channel
function joinChannel(channelName, userId) {
  return {
    action: 'subscribe',
    channel: channelName,
    user_id: userId,
    timestamp: new Date().toISOString()
  };
}

// Example: Join a project collaboration channel
joinChannel('project_123', user.id);
```

### Broadcasting Updates
```javascript
// Broadcast data to all channel subscribers
function broadcastUpdate(channelName, updateData) {
  return {
    action: 'broadcast',
    channel: channelName,
    data: updateData,
    timestamp: new Date().toISOString()
  };
}

// Example: Notify team of project status change
broadcastUpdate('project_123', {
  type: 'status_change',
  project_id: 123,
  new_status: 'completed',
  updated_by: user.name
});
```

## Chat and Messaging Implementation

### Real-time Chat System
```javascript
// Chat message broadcasting
function sendChatMessage(channelId, userId, message) {
  // 1. Save message to database
  const messageRecord = {
    channel_id: channelId,
    user_id: userId,
    message: message,
    created_at: new Date().toISOString()
  };
  
  // 2. Broadcast to channel subscribers
  broadcastUpdate(`chat_${channelId}`, {
    type: 'new_message',
    message: messageRecord,
    user: getUserInfo(userId)
  });
  
  return messageRecord;
}
```

### Typing Indicators
```javascript
// Show when users are typing
function broadcastTyping(channelId, userId, isTyping) {
  broadcastUpdate(`chat_${channelId}`, {
    type: 'typing_indicator',
    user_id: userId,
    is_typing: isTyping,
    timestamp: new Date().toISOString()
  });
}
```

### Message Read Receipts
```javascript
// Track message read status
function markMessageRead(messageId, userId) {
  // Update read status in database
  updateMessageReadStatus(messageId, userId);
  
  // Broadcast read receipt
  broadcastUpdate(`message_${messageId}`, {
    type: 'read_receipt',
    message_id: messageId,
    read_by: userId,
    read_at: new Date().toISOString()
  });
}
```

## Collaborative Features

### Real-time Document Editing
```javascript
// Collaborative document updates
function broadcastDocumentChange(documentId, userId, changes) {
  broadcastUpdate(`document_${documentId}`, {
    type: 'document_change',
    document_id: documentId,
    user_id: userId,
    changes: changes,
    version: getDocumentVersion(documentId),
    timestamp: new Date().toISOString()
  });
}

// Example document change
broadcastDocumentChange(456, user.id, {
  operation: 'insert',
  position: 100,
  text: 'New paragraph content',
  selection: { start: 100, end: 120 }
});
```

### Cursor Tracking
```javascript
// Show other users' cursors in real-time
function broadcastCursorPosition(documentId, userId, cursorData) {
  broadcastUpdate(`cursors_${documentId}`, {
    type: 'cursor_update',
    user_id: userId,
    cursor: cursorData,
    timestamp: new Date().toISOString()
  });
}
```

### Live Comments and Annotations
```javascript
// Real-time commenting system
function addLiveComment(targetId, userId, comment) {
  const commentData = {
    id: generateId(),
    target_id: targetId,
    user_id: userId,
    comment: comment,
    created_at: new Date().toISOString()
  };
  
  // Save to database
  saveComment(commentData);
  
  // Broadcast to subscribers
  broadcastUpdate(`comments_${targetId}`, {
    type: 'new_comment',
    comment: commentData,
    user: getUserInfo(userId)
  });
  
  return commentData;
}
```

## Live Dashboard Updates

### Real-time Metrics Broadcasting
```javascript
// Update dashboard metrics in real-time
function broadcastMetrics(dashboardId, metrics) {
  broadcastUpdate(`dashboard_${dashboardId}`, {
    type: 'metrics_update',
    metrics: metrics,
    timestamp: new Date().toISOString()
  });
}

// Example: Update sales dashboard
broadcastMetrics('sales_dashboard', {
  total_sales: 15750.00,
  orders_today: 45,
  conversion_rate: 3.2,
  active_users: 128
});
```

### Status Monitoring
```javascript
// System status updates
function broadcastSystemStatus(status) {
  broadcastUpdate('system_status', {
    type: 'status_update',
    status: status,
    timestamp: new Date().toISOString()
  });
}

// Example: Service health check
broadcastSystemStatus({
  service: 'payment_processor',
  status: 'operational',
  response_time: 45,
  uptime: '99.9%'
});
```

## Integration with n8n

### Automated Realtime Notifications
```javascript
// n8n workflow triggering realtime notifications
const webhookData = $json;

// Process notification data
const notification = {
  type: 'order_update',
  order_id: webhookData.order_id,
  status: webhookData.new_status,
  customer_id: webhookData.customer_id,
  message: `Order #${webhookData.order_id} is now ${webhookData.new_status}`
};

// Send to Xano realtime endpoint
return {
  method: 'POST',
  url: 'https://your-instance.xano.io/api:realtime/broadcast',
  body: {
    channel: `customer_${webhookData.customer_id}`,
    data: notification
  }
};
```

### Event-Driven Realtime Updates
```javascript
// n8n Function Node - Process and broadcast updates
const eventData = $json;

// Determine which channels need updates
const channels = [];

if (eventData.type === 'inventory_update') {
  channels.push('admin_dashboard');
  channels.push(`product_${eventData.product_id}`);
}

if (eventData.type === 'new_order') {
  channels.push('sales_dashboard');
  channels.push(`vendor_${eventData.vendor_id}`);
}

// Broadcast to multiple channels
const broadcasts = channels.map(channel => ({
  channel: channel,
  data: {
    event_type: eventData.type,
    event_data: eventData,
    timestamp: new Date().toISOString()
  }
}));

return { broadcasts };
```

## Integration with WeWeb

### Realtime Data Components
```javascript
// WeWeb component with realtime updates
export default {
  data() {
    return {
      messages: [],
      onlineUsers: [],
      connectionStatus: 'disconnected',
      realtimeConnection: null
    };
  },
  
  async mounted() {
    await this.initializeRealtime();
  },
  
  methods: {
    async initializeRealtime() {
      try {
        // Connect to Xano realtime
        this.realtimeConnection = await this.$xano.realtime.connect();
        this.connectionStatus = 'connected';
        
        // Subscribe to chat channel
        await this.subscribeToChat();
        
        // Subscribe to presence updates
        await this.subscribeToPresence();
        
      } catch (error) {
        console.error('Realtime connection failed:', error);
        this.connectionStatus = 'error';
      }
    },
    
    async subscribeToChat() {
      const channelId = this.$route.params.channelId;
      
      this.realtimeConnection.subscribe(`chat_${channelId}`, (data) => {
        switch (data.type) {
          case 'new_message':
            this.messages.push(data.message);
            this.scrollToBottom();
            break;
            
          case 'typing_indicator':
            this.handleTypingIndicator(data);
            break;
            
          case 'message_deleted':
            this.removeMessage(data.message_id);
            break;
        }
      });
    },
    
    async subscribeToPresence() {
      const channelId = this.$route.params.channelId;
      
      this.realtimeConnection.subscribe(`presence_${channelId}`, (data) => {
        switch (data.type) {
          case 'user_joined':
            this.onlineUsers.push(data.user);
            break;
            
          case 'user_left':
            this.onlineUsers = this.onlineUsers.filter(
              user => user.id !== data.user_id
            );
            break;
            
          case 'presence_sync':
            this.onlineUsers = data.users;
            break;
        }
      });
    },
    
    async sendMessage(messageText) {
      if (!messageText.trim()) return;
      
      try {
        await this.$xano.post('/chat/send', {
          channel_id: this.$route.params.channelId,
          message: messageText
        });
        
        // Message will be received via realtime subscription
        this.messageInput = '';
      } catch (error) {
        console.error('Failed to send message:', error);
      }
    },
    
    handleTypingIndicator(data) {
      // Show typing indicator for other users
      if (data.user_id !== this.$auth.user.id) {
        if (data.is_typing) {
          this.showTypingIndicator(data.user_id);
        } else {
          this.hideTypingIndicator(data.user_id);
        }
      }
    }
  },
  
  beforeUnmount() {
    // Clean up realtime connections
    if (this.realtimeConnection) {
      this.realtimeConnection.disconnect();
    }
  }
};
```

### Live Dashboard Component
```javascript
// WeWeb real-time dashboard
export default {
  data() {
    return {
      metrics: {},
      chartData: [],
      alerts: [],
      lastUpdate: null
    };
  },
  
  async mounted() {
    await this.initializeDashboard();
  },
  
  methods: {
    async initializeDashboard() {
      // Load initial data
      await this.loadInitialData();
      
      // Connect to realtime updates
      const connection = await this.$xano.realtime.connect();
      
      connection.subscribe('dashboard_metrics', (data) => {
        this.updateMetrics(data);
      });
      
      connection.subscribe('system_alerts', (data) => {
        this.handleAlert(data);
      });
    },
    
    updateMetrics(data) {
      // Update metrics in real-time
      this.metrics = { ...this.metrics, ...data.metrics };
      this.lastUpdate = new Date().toLocaleTimeString();
      
      // Update charts
      if (data.chart_data) {
        this.updateChartData(data.chart_data);
      }
      
      // Trigger reactive updates
      this.$forceUpdate();
    },
    
    handleAlert(alertData) {
      // Add new alert
      this.alerts.unshift({
        id: alertData.id,
        type: alertData.type,
        message: alertData.message,
        timestamp: new Date(),
        severity: alertData.severity
      });
      
      // Keep only recent alerts
      if (this.alerts.length > 10) {
        this.alerts = this.alerts.slice(0, 10);
      }
      
      // Show notification for high-severity alerts
      if (alertData.severity === 'high') {
        this.$toast.error(alertData.message);
      }
    }
  }
};
```

## Advanced Realtime Patterns

### Channel Authentication and Security
```javascript
// Secure channel access with permissions
function authenticateChannelAccess(channelName, userId, token) {
  // 1. Validate user token
  const user = validateJWT(token);
  
  // 2. Check channel permissions
  const hasAccess = checkChannelPermissions(channelName, user);
  
  if (!hasAccess) {
    throw new Error('Unauthorized channel access');
  }
  
  // 3. Return authenticated subscription
  return {
    authenticated: true,
    user_id: user.id,
    channel: channelName,
    permissions: getUserChannelPermissions(channelName, user)
  };
}
```

### Message Persistence and History
```javascript
// Store realtime messages for history
function persistRealtimeMessage(channelId, messageData) {
  // Save to database
  const savedMessage = saveMessage({
    channel_id: channelId,
    user_id: messageData.user_id,
    content: messageData.content,
    message_type: messageData.type,
    created_at: new Date()
  });
  
  // Broadcast with database ID
  broadcastUpdate(`chat_${channelId}`, {
    ...messageData,
    id: savedMessage.id,
    persisted: true
  });
  
  return savedMessage;
}
```

### Rate Limiting for Realtime
```javascript
// Prevent realtime spam
function checkRealtimeRateLimit(userId, action) {
  const key = `realtime_limit:${userId}:${action}`;
  const limit = getRateLimitForAction(action);
  
  if (exceedsRateLimit(key, limit)) {
    throw new Error('Rate limit exceeded for realtime action');
  }
  
  incrementRateLimitCounter(key);
  return true;
}
```

## Try This: Build a Live Collaboration Tool

1. **Create Real-time Document Editor**
   ```
   1. Set up document channels for each document
   2. Broadcast text changes with operational transforms
   3. Show live cursors for active users
   4. Implement conflict resolution for simultaneous edits
   5. Add presence indicators and user avatars
   ```

2. **Add Communication Features**
   ```
   1. Live comments on document sections
   2. Chat sidebar for team communication
   3. @mention notifications with realtime delivery
   4. Typing indicators for comments and chat
   5. Read receipts for important messages
   ```

3. **Implement Dashboard Monitoring**
   ```
   1. Real-time user activity monitoring
   2. Live document edit statistics
   3. Performance metrics and alerts
   4. User engagement analytics
   5. System health monitoring
   ```

## Common Mistakes to Avoid

❌ **Not implementing authentication** - Secure channels properly
❌ **Broadcasting too frequently** - Rate limit updates to prevent spam
❌ **Not handling disconnections** - Implement reconnection logic
❌ **Sending large payloads** - Keep realtime messages small and focused
❌ **Forgetting message persistence** - Store important messages in database
❌ **Not cleaning up subscriptions** - Prevent memory leaks in clients

## Pro Tips

💡 **Use channel namespacing** for better organization (e.g., `chat_`, `document_`)
💡 **Implement presence heartbeats** to track active users accurately
💡 **Batch similar updates** to reduce message frequency
💡 **Add reconnection logic** for reliable user experiences
💡 **Monitor connection counts** and implement scaling strategies
💡 **Use message queuing** for high-volume realtime applications
💡 **Implement message acknowledgments** for critical updates

Realtime functions bring your applications to life with instant, collaborative features that create engaging user experiences.