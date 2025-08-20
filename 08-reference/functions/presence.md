---
category: functions
description: Complete user presence and status management in Xano with real-time tracking, activity monitoring, and collaborative features
difficulty: intermediate  
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - realtime-in-xano.md
  - enabling_realtime.md
  - websockets.md
  - user-tracking.md
subcategory: 08-reference/functions
tags:
  - presence
  - user-status
  - realtime
  - collaboration
  - activity-tracking
  - websockets
title: Presence
---

# Presence

## 📋 **Quick Summary**
Implement comprehensive user presence and activity tracking in Xano with real-time status updates, collaborative features, and intelligent activity monitoring for engaging user experiences.

## What You'll Learn
- User presence tracking and management
- Real-time status updates and broadcasting
- Activity monitoring and idle detection
- Collaborative presence features
- Performance optimization for presence systems
- Integration patterns with realtime applications

## Presence System Architecture

### Core Concepts
```javascript
// Presence system components
const presenceSystem = {
  "user_status": {
    "online": "User is actively using the application",
    "away": "User is inactive but connected", 
    "busy": "User is online but marked as unavailable",
    "offline": "User is not connected"
  },
  
  "activity_tracking": {
    "last_seen": "Timestamp of last user activity",
    "current_location": "Current page/section user is viewing",
    "active_sessions": "List of active browser/device sessions",
    "interaction_count": "Recent user interactions per minute"
  },
  
  "presence_channels": {
    "global_presence": "Site-wide user status",
    "room_presence": "Users in specific rooms/channels",
    "document_presence": "Collaborative document editing",
    "typing_indicators": "Real-time typing status"
  }
};
```

## Basic Presence Implementation

### User Connection Tracking
```javascript
// Function stack for presence connection
[
  {
    "function": "Initialize Presence",
    "realtime_action": "join_channel",
    "channel": "global_presence",
    "user_data": {
      "user_id": "auth.user.id",
      "name": "auth.user.name",
      "avatar": "auth.user.avatar",
      "status": "online",
      "connected_at": "now()"
    }
  },
  {
    "function": "Update Database Status",
    "action": "upsert_record",
    "table": "user_presence",
    "match_fields": ["user_id"],
    "data": {
      "user_id": "auth.user.id",
      "status": "online",
      "last_seen": "now()",
      "session_id": "generate_session_id()",
      "ip_address": "request.ip_address",
      "user_agent": "request.user_agent"
    }
  },
  {
    "function": "Broadcast Status Update",
    "realtime_action": "broadcast",
    "channel": "global_presence",
    "event": "user_status_changed",
    "data": {
      "user_id": "auth.user.id",
      "status": "online",
      "timestamp": "now()"
    }
  },
  {
    "function": "Get Current Online Users",
    "query": `
      SELECT 
        up.user_id,
        u.name,
        u.avatar,
        up.status,
        up.last_seen
      FROM user_presence up
      JOIN users u ON up.user_id = u.id
      WHERE up.status IN ('online', 'away', 'busy')
        AND up.last_seen > DATE_SUB(NOW(), INTERVAL 5 MINUTE)
      ORDER BY up.last_seen DESC
    `
  }
]
```

### Status Change Management
```javascript
// Advanced status management
const statusManagement = {
  "update_user_status": {
    "function_stack": [
      {
        "function": "Validate Status",
        "logic": `
          const validStatuses = ['online', 'away', 'busy', 'offline'];
          if (!validStatuses.includes(inputs.status)) {
            return error(400, "Invalid status value");
          }
          
          // Check if status change is allowed
          if (inputs.status === 'offline' && !inputs.explicit_logout) {
            return error(400, "Cannot set offline status without explicit logout");
          }
        `
      },
      {
        "function": "Update Presence Record",
        "action": "update_record",
        "table": "user_presence",
        "where": { "user_id": "auth.user.id" },
        "data": {
          "status": "inputs.status",
          "status_message": "inputs.status_message",
          "last_seen": "now()",
          "updated_at": "now()"
        }
      },
      {
        "function": "Broadcast Status Change",
        "realtime_action": "broadcast",
        "channel": "global_presence",
        "event": "user_status_changed",
        "data": {
          "user_id": "auth.user.id",
          "status": "inputs.status",
          "status_message": "inputs.status_message",
          "timestamp": "now()"
        }
      },
      {
        "function": "Log Status Change",
        "action": "add_record",
        "table": "presence_history",
        "data": {
          "user_id": "auth.user.id",
          "previous_status": "previous_status",
          "new_status": "inputs.status",
          "changed_at": "now()",
          "change_reason": "inputs.reason || 'manual'"
        }
      }
    ]
  }
};
```

## Activity Detection and Idle Management

### Automated Activity Tracking
```javascript
// Activity detection system
const activityTracking = {
  "track_user_activity": {
    "function_stack": [
      {
        "function": "Record Activity",
        "action": "add_record",
        "table": "user_activities",
        "data": {
          "user_id": "auth.user.id",
          "activity_type": "inputs.activity_type",
          "page_url": "inputs.page_url",
          "timestamp": "now()",
          "session_id": "inputs.session_id"
        }
      },
      {
        "function": "Update Last Seen",
        "action": "update_record",
        "table": "user_presence", 
        "where": { "user_id": "auth.user.id" },
        "data": {
          "last_seen": "now()",
          "current_page": "inputs.page_url",
          "activity_count": "COALESCE(activity_count, 0) + 1"
        }
      },
      {
        "function": "Check Idle Status",
        "logic": `
          const lastActivity = await queryDatabase(
            "SELECT last_seen, status FROM user_presence WHERE user_id = ?",
            [auth.user.id]
          );
          
          if (lastActivity.length > 0) {
            const timeSinceLastActivity = Date.now() - new Date(lastActivity[0].last_seen).getTime();
            const idleThreshold = 5 * 60 * 1000; // 5 minutes
            
            if (timeSinceLastActivity > idleThreshold && lastActivity[0].status === 'online') {
              // Auto-transition to away status
              await updateRecord("user_presence", { user_id: auth.user.id }, {
                status: 'away',
                auto_away_at: new Date()
              });
              
              await broadcastToChannel("global_presence", "user_status_changed", {
                user_id: auth.user.id,
                status: 'away',
                reason: 'idle_timeout'
              });
            }
          }
        `
      }
    ]
  },
  
  "idle_detection_background_task": {
    "trigger": "schedule",
    "interval": "60", // Run every minute
    "logic": `
      // Find users who should be marked as away
      const idleUsers = await queryDatabase(\`
        SELECT user_id, last_seen 
        FROM user_presence 
        WHERE status = 'online' 
          AND last_seen < DATE_SUB(NOW(), INTERVAL 5 MINUTE)
      \`);
      
      for (const user of idleUsers) {
        await updateRecord("user_presence", { user_id: user.user_id }, {
          status: 'away',
          auto_away_at: new Date()
        });
        
        await broadcastToChannel("global_presence", "user_status_changed", {
          user_id: user.user_id,
          status: 'away',
          reason: 'idle_timeout'
        });
      }
      
      // Mark users as offline after extended inactivity
      const offlineUsers = await queryDatabase(\`
        SELECT user_id 
        FROM user_presence 
        WHERE status IN ('online', 'away') 
          AND last_seen < DATE_SUB(NOW(), INTERVAL 30 MINUTE)
      \`);
      
      for (const user of offlineUsers) {
        await updateRecord("user_presence", { user_id: user.user_id }, {
          status: 'offline',
          went_offline_at: new Date()
        });
        
        await broadcastToChannel("global_presence", "user_status_changed", {
          user_id: user.user_id,
          status: 'offline',
          reason: 'timeout'
        });
      }
    `
  }
};
```

## Collaborative Presence Features

### Document Collaboration
```javascript
// Document presence tracking
const documentPresence = {
  "join_document": [
    {
      "function": "Validate Document Access",
      "logic": `
        const document = await queryDatabase(
          "SELECT id, permissions FROM documents WHERE id = ?",
          [inputs.document_id]
        );
        
        if (!document.length) {
          return error(404, "Document not found");
        }
        
        // Check user permissions
        const hasAccess = await checkDocumentPermissions(
          inputs.document_id, 
          auth.user.id
        );
        
        if (!hasAccess) {
          return error(403, "Access denied to document");
        }
      `
    },
    {
      "function": "Join Document Channel",
      "realtime_action": "join_channel",
      "channel": `document_${inputs.document_id}`,
      "user_data": {
        "user_id": "auth.user.id",
        "name": "auth.user.name",
        "avatar": "auth.user.avatar",
        "cursor_position": "inputs.cursor_position",
        "joined_at": "now()"
      }
    },
    {
      "function": "Record Document Presence",
      "action": "upsert_record",
      "table": "document_presence",
      "match_fields": ["document_id", "user_id"],
      "data": {
        "document_id": "inputs.document_id",
        "user_id": "auth.user.id",
        "joined_at": "now()",
        "last_active": "now()",
        "cursor_position": "inputs.cursor_position",
        "selection_range": "inputs.selection_range"
      }
    },
    {
      "function": "Notify Other Users",
      "realtime_action": "broadcast",
      "channel": `document_${inputs.document_id}`,
      "event": "user_joined",
      "data": {
        "user": {
          "id": "auth.user.id",
          "name": "auth.user.name",
          "avatar": "auth.user.avatar"
        },
        "timestamp": "now()"
      }
    }
  ],
  
  "update_cursor_position": [
    {
      "function": "Update Cursor Data",
      "action": "update_record",
      "table": "document_presence",
      "where": {
        "document_id": "inputs.document_id",
        "user_id": "auth.user.id"
      },
      "data": {
        "cursor_position": "inputs.cursor_position",
        "selection_range": "inputs.selection_range",
        "last_active": "now()"
      }
    },
    {
      "function": "Broadcast Cursor Update",
      "realtime_action": "broadcast",
      "channel": `document_${inputs.document_id}`,
      "event": "cursor_moved",
      "data": {
        "user_id": "auth.user.id",
        "cursor_position": "inputs.cursor_position",
        "selection_range": "inputs.selection_range"
      }
    }
  ]
};
```

### Typing Indicators
```javascript
// Typing indicator system
const typingIndicators = {
  "start_typing": [
    {
      "function": "Set Typing Status",
      "realtime_action": "broadcast",
      "channel": "inputs.channel_id",
      "event": "typing_start",
      "data": {
        "user_id": "auth.user.id",
        "user_name": "auth.user.name",
        "timestamp": "now()"
      }
    },
    {
      "function": "Set Auto-Clear Timer",
      "background_task": "clear_typing_indicator",
      "delay": 3000, // 3 seconds
      "data": {
        "user_id": "auth.user.id",
        "channel_id": "inputs.channel_id"
      }
    }
  ],
  
  "stop_typing": [
    {
      "function": "Clear Typing Status",
      "realtime_action": "broadcast", 
      "channel": "inputs.channel_id",
      "event": "typing_stop",
      "data": {
        "user_id": "auth.user.id",
        "timestamp": "now()"
      }
    }
  ]
};
```

## Integration with Frontend Frameworks

### WeWeb Presence Integration
```javascript
// WeWeb presence component
const wewebPresenceManager = {
  data: {
    currentStatus: 'online',
    onlineUsers: [],
    userActivity: {
      lastActivity: Date.now(),
      activityCount: 0
    }
  },
  
  mounted() {
    this.initializePresence();
    this.setupActivityTracking();
  },
  
  methods: {
    async initializePresence() {
      // Connect to presence system
      const response = await wwLib.executeWorkflow('initialize-presence');
      
      if (response.success) {
        this.currentStatus = response.status;
        this.onlineUsers = response.online_users;
      }
      
      // Set up real-time presence updates
      wwLib.realtime.subscribe('global_presence', {
        onUserStatusChanged: (data) => {
          this.updateUserStatus(data.user_id, data.status);
        },
        onUserJoined: (data) => {
          this.addOnlineUser(data.user);
        },
        onUserLeft: (data) => {
          this.removeOnlineUser(data.user_id);
        }
      });
    },
    
    async updateStatus(newStatus, message = '') {
      const response = await wwLib.executeWorkflow('update-user-status', {
        status: newStatus,
        status_message: message
      });
      
      if (response.success) {
        this.currentStatus = newStatus;
      }
    },
    
    setupActivityTracking() {
      // Track user interactions
      ['click', 'keypress', 'scroll', 'mousemove'].forEach(event => {
        document.addEventListener(event, this.recordActivity, true);
      });
      
      // Set up idle detection
      this.idleTimer = setInterval(() => {
        const timeSinceActivity = Date.now() - this.userActivity.lastActivity;
        
        if (timeSinceActivity > 300000 && this.currentStatus === 'online') { // 5 minutes
          this.updateStatus('away');
        }
      }, 60000); // Check every minute
    },
    
    recordActivity() {
      this.userActivity.lastActivity = Date.now();
      this.userActivity.activityCount++;
      
      // Return to online if user was away due to inactivity
      if (this.currentStatus === 'away') {
        this.updateStatus('online');
      }
      
      // Throttle activity reporting
      if (this.userActivity.activityCount % 10 === 0) {
        wwLib.executeWorkflow('track-user-activity', {
          activity_type: 'interaction',
          page_url: window.location.pathname,
          session_id: wwLib.getSessionId()
        });
      }
    },
    
    updateUserStatus(userId, status) {
      const userIndex = this.onlineUsers.findIndex(u => u.id === userId);
      
      if (userIndex !== -1) {
        if (status === 'offline') {
          this.onlineUsers.splice(userIndex, 1);
        } else {
          this.onlineUsers[userIndex].status = status;
        }
      }
    }
  }
};
```

### n8n Presence Automation
```javascript
// n8n workflow: Presence-based notifications
{
  "name": "Smart Presence Notifications",
  "trigger": {
    "type": "xano-realtime",
    "channel": "global_presence",
    "event": "user_status_changed"
  },
  "nodes": [
    {
      "name": "Analyze Status Change",
      "type": "javascript",
      "code": `
        const { user_id, status, previous_status } = $json;
        
        // Detect important status transitions
        const importantTransitions = {
          'offline_to_online': status === 'online' && previous_status === 'offline',
          'extended_away': status === 'away' && previous_status === 'online',
          'back_from_away': status === 'online' && previous_status === 'away'
        };
        
        return {
          user_id,
          status,
          previous_status,
          transitions: importantTransitions,
          should_notify: Object.values(importantTransitions).some(Boolean)
        };
      `
    },
    {
      "name": "Check Notification Preferences",
      "type": "xano-query",
      "condition": "{{ $json.should_notify }}",
      "query": "SELECT notification_preferences FROM users WHERE id = ?",
      "params": ["{{ $json.user_id }}"]
    },
    {
      "name": "Send Team Notifications",
      "type": "switch",
      "condition": "{{ $json.transitions.offline_to_online }}",
      "nodes": [
        {
          "name": "Notify Team Members",
          "type": "xano-query",
          "query": `
            SELECT DISTINCT tm.user_id, u.email, u.name
            FROM team_members tm
            JOIN users u ON tm.user_id = u.id
            WHERE tm.team_id IN (
              SELECT team_id FROM team_members WHERE user_id = ?
            ) AND tm.user_id != ?
          `,
          "params": ["{{ $json.user_id }}", "{{ $json.user_id }}"]
        },
        {
          "name": "Send Notifications",
          "type": "loop",
          "items": "{{ $json }}",
          "nodes": [
            {
              "name": "Send Email",
              "type": "email",
              "to": "{{ $item.email }}",
              "template": "team-member-online",
              "data": {
                "user_name": "{{ $json.user_name }}",
                "team_member_name": "{{ $item.name }}"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## Performance Optimization

### Efficient Presence Queries
```javascript
// Optimized presence queries
const optimizedQueries = {
  // Batch presence updates
  batchUpdatePresence: `
    INSERT INTO user_presence (user_id, status, last_seen) 
    VALUES ? 
    ON DUPLICATE KEY UPDATE 
      status = VALUES(status),
      last_seen = VALUES(last_seen),
      updated_at = NOW()
  `,
  
  // Efficient online user lookup with caching
  getOnlineUsers: `
    SELECT 
      up.user_id,
      u.name,
      u.avatar,
      up.status,
      up.last_seen,
      up.current_page
    FROM user_presence up
    JOIN users u ON up.user_id = u.id
    WHERE up.status IN ('online', 'away', 'busy')
      AND up.last_seen > DATE_SUB(NOW(), INTERVAL 10 MINUTE)
    ORDER BY 
      CASE up.status 
        WHEN 'online' THEN 1 
        WHEN 'busy' THEN 2 
        WHEN 'away' THEN 3 
      END,
      up.last_seen DESC
    LIMIT 100
  `,
  
  // Channel-specific presence
  getChannelPresence: `
    SELECT 
      cp.user_id,
      u.name,
      u.avatar,
      cp.joined_at,
      cp.last_active
    FROM channel_presence cp
    JOIN users u ON cp.user_id = u.id
    WHERE cp.channel_id = ?
      AND cp.last_active > DATE_SUB(NOW(), INTERVAL 5 MINUTE)
    ORDER BY cp.last_active DESC
  `
};
```

## Try This: Build Presence System

1. **Basic Presence Tracking**
   - Create presence database tables
   - Implement connection/disconnection handlers
   - Set up status broadcasting

2. **Activity Detection**
   - Add idle detection logic
   - Implement automated status transitions
   - Create activity logging

3. **Collaborative Features**
   - Build typing indicators
   - Add cursor position tracking
   - Implement document presence

4. **Frontend Integration**
   - Connect WeWeb to presence system
   - Display online user lists
   - Add status change controls

## Common Mistakes to Avoid

- **Not cleaning up presence data** - Remove stale presence records regularly
- **Excessive broadcasting** - Throttle presence updates to prevent spam
- **Missing idle detection** - Implement proper activity tracking
- **Poor performance** - Optimize queries for large user bases
- **No privacy controls** - Allow users to control presence visibility

## Pro Tips

💡 **Use connection heartbeats** - Regular ping/pong to detect disconnections

💡 **Implement presence levels** - Different visibility levels for different contexts

💡 **Cache presence data** - Use Redis or similar for high-performance lookups

💡 **Batch presence updates** - Group multiple updates for efficiency

💡 **Add presence analytics** - Track usage patterns and engagement metrics