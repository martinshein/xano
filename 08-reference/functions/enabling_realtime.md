---
category: functions
description: Complete guide to enabling and configuring realtime features in Xano with WebSocket connections, channel management, and live data synchronization
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - realtime-in-xano.md
  - channel-permissions.md
  - webhooks.md
  - middleware.md
subcategory: 08-reference/functions
tags:
  - realtime
  - websockets
  - channels
  - live-updates
  - synchronization
  - presence
title: Enabling Realtime
---

# Enabling Realtime

## 📋 **Quick Summary**
Enable powerful realtime features in Xano with WebSocket connections, live data synchronization, presence detection, and secure channel management for building collaborative applications and instant updates.

## What You'll Learn
- How to enable and configure realtime in Xano
- Channel creation and permission management
- Live data synchronization patterns
- Presence and user tracking
- Integration with n8n, WeWeb, and frontend frameworks
- Performance optimization for realtime applications

## Enabling Realtime in Xano

### Step 1: Instance Configuration
```javascript
// Enable realtime in instance settings
{
  "realtime": {
    "enabled": true,
    "max_connections": 1000,
    "channel_limit": 100,
    "message_retention": "24h",
    "presence_timeout": 300
  },
  "websocket_config": {
    "ping_interval": 25,
    "pong_timeout": 60,
    "max_frame_size": "64kb"
  }
}
```

### Step 2: Create Realtime Channels
```javascript
// Channel configuration
const channelConfig = {
  "channels": {
    "chat-room": {
      "type": "public",
      "authentication": "optional",
      "presence": true,
      "message_history": 100
    },
    "user-notifications": {
      "type": "private", 
      "authentication": "required",
      "user_specific": true,
      "auto_subscribe": true
    },
    "document-collaboration": {
      "type": "presence",
      "authentication": "required",
      "max_participants": 50,
      "conflict_resolution": "operational_transform"
    }
  }
};
```

## Realtime Function Implementation

### Basic Message Broadcasting
```javascript
// Function stack for broadcasting messages
[
  {
    "function": "Validate Input",
    "logic": `
      if (!inputs.message || inputs.message.trim().length === 0) {
        return error(400, "Message cannot be empty");
      }
      if (inputs.message.length > 1000) {
        return error(400, "Message too long");
      }
    `
  },
  {
    "function": "Get User Context",
    "query": "SELECT id, name, avatar FROM users WHERE id = ?",
    "params": ["auth.user.id"]
  },
  {
    "function": "Save Message",
    "action": "add_record",
    "table": "messages",
    "data": {
      "user_id": "auth.user.id",
      "channel": "inputs.channel",
      "content": "inputs.message",
      "created_at": "now()"
    }
  },
  {
    "function": "Broadcast to Channel",
    "realtime_action": "broadcast",
    "channel": "inputs.channel",
    "event": "new_message",
    "data": {
      "id": "message.id",
      "user": {
        "id": "user_context.id",
        "name": "user_context.name", 
        "avatar": "user_context.avatar"
      },
      "content": "inputs.message",
      "timestamp": "message.created_at"
    }
  }
]
```

### Advanced Channel Management
```javascript
// Dynamic channel subscription
function manageChannelSubscription(userId, action, channelId) {
  const channelActions = {
    "join": async () => {
      // Validate user permissions
      const canJoin = await checkChannelPermissions(userId, channelId);
      if (!canJoin) {
        throw new Error("Access denied to channel");
      }
      
      // Subscribe user to channel
      await realtimeSubscribe(userId, channelId);
      
      // Broadcast user join event
      await realtimeBroadcast(channelId, "user_joined", {
        user_id: userId,
        timestamp: new Date()
      });
      
      // Update presence
      await updatePresence(channelId, userId, "online");
    },
    
    "leave": async () => {
      await realtimeUnsubscribe(userId, channelId);
      
      await realtimeBroadcast(channelId, "user_left", {
        user_id: userId,
        timestamp: new Date()
      });
      
      await removePresence(channelId, userId);
    },
    
    "mute": async () => {
      await updateUserChannelSettings(userId, channelId, {
        muted: true,
        mute_until: Date.now() + (24 * 60 * 60 * 1000) // 24 hours
      });
    }
  };
  
  return channelActions[action]();
}
```

## n8n Integration Patterns

### Realtime Workflow Triggers
```javascript
// n8n workflow: Process realtime events
{
  "name": "Realtime Event Processor",
  "trigger": {
    "type": "xano-realtime",
    "channel": "system-events",
    "events": ["user_action", "data_update", "system_alert"]
  },
  "nodes": [
    {
      "name": "Event Filter",
      "type": "switch",
      "conditions": [
        {
          "case": "user_action",
          "route": "process-user-action"
        },
        {
          "case": "data_update", 
          "route": "sync-external-systems"
        },
        {
          "case": "system_alert",
          "route": "send-notifications"
        }
      ]
    },
    {
      "name": "Process User Action",
      "type": "javascript",
      "code": `
        const { user_id, action, metadata } = $json.data;
        
        // Log user activity
        await $http.post('/api/analytics/track', {
          user_id,
          event: action,
          metadata,
          timestamp: new Date()
        });
        
        // Check for achievements/milestones
        const achievements = await checkUserAchievements(user_id, action);
        
        if (achievements.length > 0) {
          // Broadcast achievements to user's channels
          for (const achievement of achievements) {
            await $http.post('/api/realtime/broadcast', {
              channel: \`user-\${user_id}\`,
              event: 'achievement_unlocked',
              data: achievement
            });
          }
        }
        
        return { processed: true, achievements };
      `
    },
    {
      "name": "Sync External Systems",
      "type": "http-request",
      "url": "https://api.external-service.com/sync",
      "method": "POST",
      "body": {
        "data": "{{ $json.data }}",
        "source": "xano-realtime"
      }
    }
  ]
}
```

### Live Analytics Dashboard
```javascript
// Real-time analytics updates
{
  "name": "Live Analytics Update",
  "trigger": {
    "type": "schedule", 
    "interval": "30s"
  },
  "nodes": [
    {
      "name": "Calculate Metrics",
      "type": "xano-query",
      "query": `
        SELECT 
          COUNT(DISTINCT user_id) as active_users,
          COUNT(*) as total_events,
          AVG(response_time) as avg_response_time,
          COUNT(CASE WHEN status = 'error' THEN 1 END) as error_count
        FROM realtime_events 
        WHERE created_at >= NOW() - INTERVAL 1 MINUTE
      `
    },
    {
      "name": "Broadcast Metrics",
      "type": "xano-realtime-broadcast",
      "channel": "admin-dashboard",
      "event": "metrics_update",
      "data": {
        "timestamp": "{{ new Date().toISOString() }}",
        "metrics": "{{ $json }}"
      }
    }
  ]
}
```

## WeWeb Realtime Integration

### Live Data Components
```javascript
// WeWeb realtime data binding
const realtimeComponent = {
  // Initialize realtime connection
  mounted() {
    this.connectRealtime();
  },
  
  methods: {
    async connectRealtime() {
      // Connect to Xano realtime
      this.realtimeConnection = await wwLib.realtime.connect({
        endpoint: wwLib.globalData.xanoRealtimeUrl,
        auth: wwLib.auth.getToken()
      });
      
      // Subscribe to channels
      await this.subscribeToChannels();
      
      // Set up event handlers
      this.setupEventHandlers();
    },
    
    async subscribeToChannels() {
      const channels = [
        `user-${this.currentUser.id}`,
        'global-notifications',
        'live-updates'
      ];
      
      for (const channel of channels) {
        await this.realtimeConnection.subscribe(channel);
      }
    },
    
    setupEventHandlers() {
      // Handle new messages
      this.realtimeConnection.on('new_message', (data) => {
        this.messages.push({
          id: data.id,
          user: data.user,
          content: data.content,
          timestamp: new Date(data.timestamp)
        });
        
        // Auto-scroll to bottom
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      });
      
      // Handle user presence
      this.realtimeConnection.on('presence_update', (data) => {
        this.updateUserPresence(data.user_id, data.status);
      });
      
      // Handle live data updates
      this.realtimeConnection.on('data_update', (data) => {
        this.updateLocalData(data.table, data.record);
      });
    },
    
    // Send realtime message
    async sendMessage(content) {
      const response = await wwLib.executeWorkflow('send-realtime-message', {
        channel: this.currentChannel,
        message: content,
        user_id: this.currentUser.id
      });
      
      if (!response.success) {
        this.showError('Failed to send message');
      }
    },
    
    // Update presence status
    async updatePresence(status) {
      await wwLib.executeWorkflow('update-presence', {
        channel: this.currentChannel,
        user_id: this.currentUser.id,
        status: status,
        timestamp: new Date()
      });
    }
  }
};
```

### Collaborative Features
```javascript
// Real-time collaboration component
const collaborationFeatures = {
  // Document synchronization
  syncDocument: {
    // Track cursor positions
    trackCursor(position) {
      this.realtimeConnection.broadcast('cursor_update', {
        user_id: this.currentUser.id,
        position: position,
        timestamp: Date.now()
      });
    },
    
    // Handle text changes
    onTextChange(changes) {
      const operation = {
        type: 'text_change',
        changes: changes,
        user_id: this.currentUser.id,
        version: this.documentVersion++
      };
      
      // Apply operational transformation
      const transformedOp = this.transformOperation(operation);
      
      // Broadcast to other users
      this.realtimeConnection.broadcast('document_change', transformedOp);
      
      // Update local state
      this.applyOperation(transformedOp);
    },
    
    // Conflict resolution
    transformOperation(operation) {
      // Implement operational transformation algorithm
      const pendingOps = this.getPendingOperations();
      
      return pendingOps.reduce((op, pendingOp) => {
        return this.operationalTransform(op, pendingOp);
      }, operation);
    }
  },
  
  // Live comments
  liveComments: {
    addComment(text, position) {
      const comment = {
        id: this.generateId(),
        text: text,
        position: position,
        user: this.currentUser,
        timestamp: new Date(),
        resolved: false
      };
      
      // Broadcast to channel
      this.realtimeConnection.broadcast('comment_added', comment);
      
      // Save to database
      wwLib.executeWorkflow('save-comment', comment);
    },
    
    resolveComment(commentId) {
      this.realtimeConnection.broadcast('comment_resolved', {
        comment_id: commentId,
        resolved_by: this.currentUser.id,
        timestamp: new Date()
      });
    }
  }
};
```

## Performance Optimization

### Connection Management
```javascript
// Optimized connection handling
const connectionManager = {
  // Connection pooling
  connections: new Map(),
  
  async getConnection(userId) {
    if (!this.connections.has(userId)) {
      const connection = await this.createConnection(userId);
      this.connections.set(userId, connection);
      
      // Clean up inactive connections
      setTimeout(() => {
        if (connection.inactive) {
          this.closeConnection(userId);
        }
      }, 300000); // 5 minutes
    }
    
    return this.connections.get(userId);
  },
  
  // Message batching
  messageBatch: [],
  batchTimeout: null,
  
  queueMessage(message) {
    this.messageBatch.push(message);
    
    if (!this.batchTimeout) {
      this.batchTimeout = setTimeout(() => {
        this.flushMessageBatch();
      }, 50); // Batch messages every 50ms
    }
  },
  
  flushMessageBatch() {
    if (this.messageBatch.length > 0) {
      this.processBatch(this.messageBatch);
      this.messageBatch = [];
    }
    this.batchTimeout = null;
  }
};
```

## Try This: Build a Realtime Chat

1. **Enable Realtime in Instance**
   - Configure WebSocket settings
   - Set up channel limits and retention
   - Test basic connectivity

2. **Create Chat Channels**
   - Design public and private channels
   - Implement permission checking
   - Add presence tracking

3. **Build Frontend Integration**
   - Connect WeWeb to realtime endpoints
   - Implement message display
   - Add typing indicators

4. **Add Advanced Features**
   - File sharing in chat
   - Message reactions and threading
   - User mentions and notifications

## Common Mistakes to Avoid

- **Not implementing proper authentication** - Always verify user permissions for channels
- **Missing connection cleanup** - Clean up WebSocket connections on user disconnect
- **Overloading channels** - Limit message frequency and implement batching
- **Poor error handling** - Handle connection drops and reconnection gracefully
- **No presence management** - Track user online/offline status accurately

## Pro Tips

💡 **Use channel namespacing** - Organize channels by feature and access level

💡 **Implement message persistence** - Store important messages for offline users

💡 **Add connection health checks** - Monitor and restart failed connections

💡 **Optimize for mobile** - Handle network changes and background states

💡 **Consider scalability early** - Plan for horizontal scaling and load balancing