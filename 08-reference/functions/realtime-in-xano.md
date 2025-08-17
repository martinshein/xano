---
title: Real-time Functions Reference
description: Complete guide to implementing real-time features in Xano - WebSockets, channels, live updates, and real-time data synchronization for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- realtime
- websockets
- channels
- live-updates
- push-notifications
- data-synchronization
- pubsub
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 02-core-concepts/function-stack/realtime.md
- 08-reference/functions/triggers.md
- 08-reference/functions/webhooks.md
---

## 📋 **Quick Summary**

Real-time functionality in Xano enables live data updates, instant notifications, and synchronized experiences across connected clients using WebSockets, channels, and publish-subscribe patterns for no-code applications.

## What You'll Learn

- How to implement real-time channels and messaging
- WebSocket connection management and authentication
- Live data synchronization patterns
- Channel permissions and access control
- Real-time integration with no-code platforms
- Performance optimization for real-time features
- Advanced real-time scenarios and troubleshooting

## Understanding Real-time in Xano

### Real-time Architecture

**WebSocket Connections:**
- Persistent bidirectional communication
- Low-latency message delivery
- Connection lifecycle management
- Automatic reconnection handling

**Channel System:**
- Topic-based message routing
- User and group channels
- Private and public channels
- Channel permissions and access control

**Publish-Subscribe Pattern:**
- Event-driven messaging
- Message broadcasting
- Selective message delivery
- Real-time data synchronization

### Real-time Use Cases

```javascript
// Common real-time scenarios
{
  "chat_messaging": {
    "channel": "chat_room_{{room_id}}",
    "events": ["message_sent", "user_joined", "user_left", "typing_start", "typing_stop"]
  },
  "live_dashboard": {
    "channel": "dashboard_{{user_id}}",
    "events": ["metrics_updated", "alert_triggered", "data_refreshed"]
  },
  "collaborative_editing": {
    "channel": "document_{{doc_id}}",
    "events": ["content_changed", "cursor_moved", "user_connected", "user_disconnected"]
  },
  "live_notifications": {
    "channel": "user_{{user_id}}_notifications",
    "events": ["notification_received", "notification_read", "notification_deleted"]
  }
}
```

## Basic Real-time Implementation

### 1. Channel Creation and Management

```javascript
// Create and configure real-time channels
{
  "function": "create_realtime_channel",
  "channel_name": "user_{{auth.user.id}}_updates",
  "permissions": {
    "subscribe": ["user:{{auth.user.id}}", "admin"],
    "publish": ["system", "admin"],
    "presence": true
  },
  "options": {
    "persistent": false,
    "max_connections": 100,
    "message_history": 50
  }
}

// Join user to specific channels
{
  "function": "subscribe_to_channel",
  "channels": [
    "user_{{auth.user.id}}_notifications",
    "team_{{auth.user.team_id}}_updates",
    "global_announcements"
  ],
  "connection_id": "{{websocket.connection_id}}"
}
```

### 2. Publishing Real-time Messages

```javascript
// Publish message to channel
{
  "function": "publish_realtime_message",
  "channel": "chat_room_{{room_id}}",
  "event": "message_sent",
  "data": {
    "message_id": "{{new_message.id}}",
    "content": "{{new_message.content}}",
    "sender": {
      "id": "{{auth.user.id}}",
      "name": "{{auth.user.name}}",
      "avatar": "{{auth.user.avatar_url}}"
    },
    "timestamp": "{{now()}}",
    "room_id": "{{room_id}}"
  },
  "exclude_sender": true
}

// Broadcast system notification
{
  "function": "broadcast_to_all_users",
  "event": "system_maintenance",
  "data": {
    "message": "System maintenance will begin in 10 minutes",
    "scheduled_time": "{{maintenance_time}}",
    "duration": "30 minutes",
    "type": "warning"
  },
  "filter": {
    "user_status": "active"
  }
}
```

### 3. Real-time Data Synchronization

```javascript
// Sync data changes in real-time
{
  "trigger": "after_update",
  "table": "projects",
  "function_stack": [
    {
      "function": "publish_realtime_message",
      "channel": "project_{{new_record.id}}",
      "event": "project_updated",
      "data": {
        "project_id": "{{new_record.id}}",
        "changes": "{{diff(old_record, new_record)}}",
        "updated_by": "{{auth.user.id}}",
        "timestamp": "{{now()}}"
      }
    },
    {
      "function": "publish_realtime_message",
      "channel": "user_{{new_record.owner_id}}_notifications",
      "event": "project_notification",
      "data": {
        "type": "project_updated",
        "project_name": "{{new_record.name}}",
        "message": "Project {{new_record.name}} has been updated"
      }
    }
  ]
}
```

## Advanced Real-time Patterns

### 1. Presence and User Status

```javascript
// User presence management
{
  "websocket_events": {
    "connection_established": [
      {
        "function": "update_user_status",
        "user_id": "{{auth.user.id}}",
        "status": "online",
        "last_seen": "{{now()}}",
        "connection_id": "{{websocket.connection_id}}"
      },
      {
        "function": "publish_realtime_message",
        "channel": "team_{{auth.user.team_id}}_presence",
        "event": "user_online",
        "data": {
          "user_id": "{{auth.user.id}}",
          "name": "{{auth.user.name}}",
          "status": "online"
        }
      }
    ],
    "connection_closed": [
      {
        "function": "update_user_status",
        "user_id": "{{auth.user.id}}",
        "status": "offline",
        "last_seen": "{{now()}}"
      },
      {
        "function": "publish_realtime_message",
        "channel": "team_{{auth.user.team_id}}_presence",
        "event": "user_offline",
        "data": {
          "user_id": "{{auth.user.id}}",
          "name": "{{auth.user.name}}",
          "status": "offline",
          "last_seen": "{{now()}}"
        }
      }
    ]
  }
}

// Typing indicators
{
  "function": "handle_typing_indicator",
  "channel": "chat_room_{{room_id}}",
  "user_id": "{{auth.user.id}}",
  "typing": true,
  "function_stack": [
    {
      "function": "publish_realtime_message",
      "channel": "chat_room_{{room_id}}",
      "event": "typing_start",
      "data": {
        "user_id": "{{auth.user.id}}",
        "user_name": "{{auth.user.name}}"
      },
      "exclude_sender": true
    },
    {
      "function": "background_task",
      "task": "clear_typing_indicator",
      "delay": 3,
      "data": {
        "channel": "chat_room_{{room_id}}",
        "user_id": "{{auth.user.id}}"
      }
    }
  ]
}
```

### 2. Private Messaging and Direct Messages

```javascript
// Private messaging system
{
  "function": "send_private_message",
  "from_user": "{{auth.user.id}}",
  "to_user": "{{recipient_id}}",
  "message": "{{message_content}}",
  "function_stack": [
    {
      "function": "add_record",
      "table": "private_messages",
      "data": {
        "from_user_id": "{{auth.user.id}}",
        "to_user_id": "{{recipient_id}}",
        "content": "{{message_content}}",
        "sent_at": "{{now()}}",
        "status": "sent"
      }
    },
    {
      "function": "publish_realtime_message",
      "channel": "user_{{recipient_id}}_messages",
      "event": "private_message_received",
      "data": {
        "message_id": "{{private_messages.id}}",
        "from_user": {
          "id": "{{auth.user.id}}",
          "name": "{{auth.user.name}}",
          "avatar": "{{auth.user.avatar_url}}"
        },
        "content": "{{message_content}}",
        "sent_at": "{{now()}}"
      }
    },
    {
      "function": "publish_realtime_message",
      "channel": "user_{{auth.user.id}}_messages",
      "event": "private_message_sent",
      "data": {
        "message_id": "{{private_messages.id}}",
        "to_user": {
          "id": "{{recipient_id}}",
          "name": "{{recipient.name}}"
        },
        "content": "{{message_content}}",
        "sent_at": "{{now()}}"
      }
    }
  ]
}
```

### 3. Real-time Notifications System

```javascript
// Comprehensive notification system
{
  "notification_types": {
    "order_status": {
      "channels": ["user_{{user_id}}_notifications"],
      "template": "Your order #{{order_id}} status changed to {{status}}"
    },
    "team_invite": {
      "channels": ["user_{{user_id}}_notifications", "user_{{user_id}}_team"],
      "template": "You've been invited to join {{team_name}}"
    },
    "system_alert": {
      "channels": ["all_users"],
      "template": "{{message}}"
    }
  },
  "send_notification": [
    {
      "function": "add_record",
      "table": "notifications",
      "data": {
        "user_id": "{{user_id}}",
        "type": "{{notification_type}}",
        "title": "{{title}}",
        "message": "{{message}}",
        "data": "{{notification_data}}",
        "read": false,
        "created_at": "{{now()}}"
      }
    },
    {
      "function": "publish_realtime_message",
      "channel": "user_{{user_id}}_notifications",
      "event": "notification_received",
      "data": {
        "notification_id": "{{notifications.id}}",
        "type": "{{notification_type}}",
        "title": "{{title}}",
        "message": "{{message}}",
        "data": "{{notification_data}}",
        "created_at": "{{now()}}"
      }
    }
  ]
}
```

## No-Code Platform Integration

### n8n Real-time Workflows
```javascript
// Real-time n8n integration
{
  "realtime_n8n_trigger": {
    "channel": "n8n_workflow_updates",
    "webhook_endpoint": "https://hooks.n8n.cloud/webhook/realtime-updates",
    "function_stack": [
      {
        "function": "publish_realtime_message",
        "channel": "workflow_{{workflow_id}}",
        "event": "workflow_status_changed",
        "data": {
          "workflow_id": "{{workflow_id}}",
          "status": "{{new_status}}",
          "execution_id": "{{execution_id}}",
          "timestamp": "{{now()}}"
        }
      },
      {
        "function": "external_api_request",
        "url": "{{webhook_endpoint}}",
        "method": "POST",
        "data": {
          "event": "xano_realtime_update",
          "workflow_id": "{{workflow_id}}",
          "data": "{{event_data}}"
        }
      }
    ]
  }
}
```

### WeWeb Live Components
```javascript
// WeWeb real-time component updates
{
  "weweb_realtime_binding": {
    "component": "live_dashboard",
    "data_source": "realtime_metrics",
    "update_patterns": [
      {
        "channel": "dashboard_metrics",
        "event": "metrics_updated",
        "action": "update_component_data",
        "mapping": {
          "sales_count": "{{data.total_sales}}",
          "revenue": "{{data.total_revenue}}",
          "active_users": "{{data.active_users}}"
        }
      },
      {
        "channel": "dashboard_alerts",
        "event": "alert_triggered",
        "action": "show_notification",
        "mapping": {
          "type": "{{data.alert_type}}",
          "message": "{{data.message}}",
          "severity": "{{data.severity}}"
        }
      }
    ]
  }
}

// WeWeb chat component integration
{
  "weweb_chat_component": {
    "channel": "chat_room_{{room_id}}",
    "events": {
      "message_sent": {
        "action": "append_message",
        "data": "{{event_data}}"
      },
      "user_joined": {
        "action": "update_user_list",
        "data": "{{event_data.user}}"
      },
      "typing_start": {
        "action": "show_typing_indicator",
        "data": "{{event_data.user_name}}"
      }
    }
  }
}
```

### Make.com Real-time Scenarios
```javascript
// Make.com real-time scenario triggers
{
  "make_realtime_integration": {
    "scenario_webhook": "https://hook.us1.make.com/realtime-trigger",
    "channel_mappings": [
      {
        "channel": "order_updates",
        "events": ["order_created", "order_shipped", "order_delivered"],
        "webhook_data": {
          "source": "xano_realtime",
          "channel": "{{channel}}",
          "event": "{{event}}",
          "data": "{{event_data}}",
          "timestamp": "{{now()}}"
        }
      },
      {
        "channel": "inventory_alerts",
        "events": ["low_stock", "out_of_stock"],
        "webhook_data": {
          "alert_type": "inventory",
          "product_id": "{{event_data.product_id}}",
          "current_stock": "{{event_data.stock_level}}",
          "threshold": "{{event_data.threshold}}"
        }
      }
    ]
  }
}
```

## Channel Permissions and Security

### 1. Role-Based Channel Access

```javascript
// Channel permission system
{
  "channel_permissions": {
    "user_private": {
      "pattern": "user_{{user_id}}_*",
      "subscribe": ["user:{{user_id}}", "admin"],
      "publish": ["system", "admin", "user:{{user_id}}"],
      "presence": false
    },
    "team_channels": {
      "pattern": "team_{{team_id}}_*",
      "subscribe": ["team:{{team_id}}", "admin"],
      "publish": ["team_member:{{team_id}}", "admin"],
      "presence": true
    },
    "public_channels": {
      "pattern": "public_*",
      "subscribe": ["authenticated"],
      "publish": ["admin", "moderator"],
      "presence": true
    },
    "admin_channels": {
      "pattern": "admin_*",
      "subscribe": ["admin"],
      "publish": ["admin"],
      "presence": true
    }
  },
  "permission_validation": [
    {
      "function": "validate_channel_access",
      "channel": "{{requested_channel}}",
      "user_id": "{{auth.user.id}}",
      "action": "{{action}}" // subscribe, publish, presence
    }
  ]
}
```

### 2. Dynamic Channel Creation

```javascript
// Dynamic channel management
{
  "create_private_chat": [
    {
      "function": "create_variable",
      "name": "channel_id",
      "value": "chat_{{generate_uuid()}}"
    },
    {
      "function": "add_record",
      "table": "chat_channels",
      "data": {
        "channel_id": "{{channel_id}}",
        "type": "private",
        "participants": "{{participant_ids}}",
        "created_by": "{{auth.user.id}}",
        "created_at": "{{now()}}"
      }
    },
    {
      "function": "for_each_loop",
      "array": "{{participant_ids}}",
      "function_stack": [
        {
          "function": "grant_channel_access",
          "channel": "{{channel_id}}",
          "user_id": "{{loop_item}}",
          "permissions": ["subscribe", "publish"]
        },
        {
          "function": "publish_realtime_message",
          "channel": "user_{{loop_item}}_notifications",
          "event": "chat_invitation",
          "data": {
            "channel_id": "{{channel_id}}",
            "invited_by": "{{auth.user.name}}",
            "participants": "{{participant_ids}}"
          }
        }
      ]
    }
  ]
}
```

## Performance Optimization

### 1. Message Batching and Throttling

```javascript
// Message batching for high-frequency updates
{
  "batch_realtime_updates": {
    "batch_size": 10,
    "batch_timeout": 100, // milliseconds
    "channels": ["high_frequency_*"],
    "function_stack": [
      {
        "function": "collect_messages",
        "timeout": "{{batch_timeout}}",
        "max_messages": "{{batch_size}}"
      },
      {
        "function": "publish_batched_messages",
        "messages": "{{collected_messages}}",
        "format": "batch_update"
      }
    ]
  }
}

// Rate limiting for real-time messages
{
  "rate_limiting": {
    "user_messages": {
      "limit": 60, // messages per minute
      "window": 60,
      "channels": ["chat_*", "user_*_messages"]
    },
    "system_notifications": {
      "limit": 10, // per minute per user
      "window": 60,
      "channels": ["*_notifications"]
    }
  }
}
```

### 2. Connection Management

```javascript
// WebSocket connection optimization
{
  "connection_management": {
    "max_connections_per_user": 5,
    "connection_timeout": 300000, // 5 minutes
    "heartbeat_interval": 30000,  // 30 seconds
    "reconnection_attempts": 3,
    "connection_cleanup": [
      {
        "function": "cleanup_stale_connections",
        "schedule": "*/5 * * * *", // every 5 minutes
        "criteria": {
          "last_heartbeat": "{{subtract_minutes(now(), 10)}}"
        }
      }
    ]
  }
}
```

## Try This: Complete Real-time Chat System

Create a comprehensive real-time chat application:

```javascript
// Complete real-time chat implementation
{
  "chat_system": {
    "join_room": [
      {
        "function": "get_record",
        "table": "chat_rooms",
        "record_id": "{{room_id}}"
      },
      {
        "function": "conditional",
        "condition": "{{!chat_rooms || !has_room_access(auth.user.id, room_id)}}",
        "true_stack": [
          {
            "function": "return_response",
            "status": 403,
            "body": {"error": "Access denied to chat room"}
          }
        ]
      },
      {
        "function": "subscribe_to_channel",
        "channel": "chat_room_{{room_id}}",
        "user_id": "{{auth.user.id}}"
      },
      {
        "function": "publish_realtime_message",
        "channel": "chat_room_{{room_id}}",
        "event": "user_joined",
        "data": {
          "user_id": "{{auth.user.id}}",
          "user_name": "{{auth.user.name}}",
          "joined_at": "{{now()}}"
        }
      }
    ],
    "send_message": [
      {
        "function": "add_record",
        "table": "chat_messages",
        "data": {
          "room_id": "{{room_id}}",
          "user_id": "{{auth.user.id}}",
          "content": "{{message}}",
          "sent_at": "{{now()}}"
        }
      },
      {
        "function": "publish_realtime_message",
        "channel": "chat_room_{{room_id}}",
        "event": "message_sent",
        "data": {
          "message_id": "{{chat_messages.id}}",
          "content": "{{message}}",
          "sender": {
            "id": "{{auth.user.id}}",
            "name": "{{auth.user.name}}",
            "avatar": "{{auth.user.avatar_url}}"
          },
          "sent_at": "{{now()}}"
        }
      }
    ],
    "leave_room": [
      {
        "function": "unsubscribe_from_channel",
        "channel": "chat_room_{{room_id}}",
        "user_id": "{{auth.user.id}}"
      },
      {
        "function": "publish_realtime_message",
        "channel": "chat_room_{{room_id}}",
        "event": "user_left",
        "data": {
          "user_id": "{{auth.user.id}}",
          "user_name": "{{auth.user.name}}",
          "left_at": "{{now()}}"
        }
      }
    ]
  }
}
```

## Common Real-time Mistakes to Avoid

### ❌ Poor Practices
- Not implementing proper authentication for channels
- Sending too many unnecessary real-time updates
- Missing connection cleanup and resource management
- Not handling reconnection scenarios
- Ignoring message ordering and delivery guarantees

### ✅ Best Practices
- Implement proper channel permissions and access control
- Use message batching for high-frequency updates
- Implement connection management and cleanup
- Handle network interruptions gracefully
- Ensure message ordering and delivery

## Pro Tips

### 💡 **Performance Optimization**
- Use channel patterns for efficient message routing
- Implement message batching for high-frequency updates
- Monitor connection counts and resource usage
- Use presence efficiently to avoid unnecessary updates

### 🔒 **Security Considerations**
- Always validate channel access permissions
- Implement rate limiting for message publishing
- Sanitize real-time message content
- Monitor for abuse and implement blocking

### 📊 **Monitoring and Analytics**
- Track real-time message volumes and patterns
- Monitor connection health and stability
- Measure message delivery latency
- Set up alerts for connection issues

### 🔄 **Integration Patterns**
- Design real-time events for easy consumption
- Implement fallback mechanisms for offline scenarios
- Create consistent event schemas
- Use real-time for enhanced user experience

## Troubleshooting Real-time Issues

### Common Problems
1. **Connection drops**: Implement heartbeat and reconnection logic
2. **Message delivery failures**: Add retry mechanisms and acknowledgments
3. **Performance issues**: Optimize message frequency and batching
4. **Permission errors**: Verify channel access and authentication

Real-time functionality in Xano enables powerful live experiences and instant data synchronization. Proper implementation ensures reliable, scalable, and secure real-time features for modern no-code applications.