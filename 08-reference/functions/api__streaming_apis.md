---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
- Streaming
- Real-time
- n8n
- WeWeb
- AI Integration
- Performance
title: 'Streaming APIs & Real-Time Data Delivery'
---

# Streaming APIs & Real-Time Data Delivery

## 📋 **Quick Summary**
Master Xano's streaming APIs to deliver real-time data progressively, perfect for AI chatbot responses, live content updates, and large dataset processing. Enable responsive applications that provide immediate feedback and seamless user experiences through efficient streaming data delivery.

## 🎯 **Core Concepts**

### What are Streaming APIs?
Streaming APIs enable real-time data delivery by sending data in chunks as it becomes available, rather than waiting for complete processing before responding. This creates more responsive user experiences with immediate feedback.

### Key Benefits
- **Immediate Response**: First content appears within 100ms
- **Progressive Loading**: Users see data as it's processed
- **Better UX**: No long loading periods or timeout issues
- **Scalability**: Handle large responses efficiently
- **Interactivity**: Users can interrupt or modify requests

## 🛠️ **Implementation Guide**

### Creating Streaming Responses

#### Step 1: Configure API Endpoint
```javascript
// Xano API endpoint configuration for streaming
{
  "endpoint_settings": {
    "method": "POST",
    "path": "/api/stream-chat",
    "response_type": "streaming", // Critical setting for streaming
    "headers": {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive"
    }
  },
  "input_parameters": {
    "message": {
      "type": "text", 
      "required": true,
      "description": "Content to stream back to client"
    },
    "options": {
      "type": "object",
      "properties": {
        "chunk_size": "Words per streaming chunk",
        "delay": "Milliseconds between chunks"
      }
    }
  }
}
```

#### Step 2: Function Stack Implementation
```javascript
// Complete streaming function stack
{
  "function_stack": [
    {
      "step": 1,
      "function": "Create Variable",
      "name": "content_chunks",
      "value": [
        "Welcome to our streaming API!",
        "This content appears progressively.",
        "Each chunk streams immediately.",
        "Providing real-time user feedback.",
        "Stream complete - thank you!"
      ]
    },
    {
      "step": 2,
      "function": "For Each",
      "input": "{{content_chunks}}",
      "inner_functions": [
        {
          "function": "Streaming API Response",
          "content": "{{item}}",
          "metadata": {
            "chunk_index": "{{loop_index}}",
            "total_chunks": "{{array_length}}",
            "timestamp": "{{now}}"
          }
        }
      ]
    },
    {
      "step": 3,
      "function": "Streaming API Response",
      "content": "[DONE]",
      "purpose": "Signal stream completion"
    }
  ]
}
```

### AI Chatbot Streaming
```javascript
// AI-powered streaming chatbot implementation
{
  "ai_chatbot_streaming": {
    "endpoint": "/api/ai-chat-stream",
    "authentication": "JWT token required",
    "function_stack": [
      {
        "step": "Input Validation",
        "function": "Validate JWT + sanitize input",
        "security": "Prevent prompt injection attacks"
      },
      {
        "step": "AI Integration", 
        "function": "External API Request (Streaming)",
        "provider": "OpenAI/Anthropic/Google AI",
        "configuration": {
          "url": "https://api.openai.com/v1/chat/completions",
          "method": "POST",
          "headers": {
            "Authorization": "Bearer {{env.OPENAI_API_KEY}}",
            "Content-Type": "application/json"
          },
          "body": {
            "model": "gpt-4",
            "messages": "{{conversation_history}}",
            "stream": true,
            "max_tokens": 1000
          }
        }
      },
      {
        "step": "Stream Processing",
        "function": "For Each (AI Response Chunks)",
        "processing": [
          "Extract content from each streaming chunk",
          "Handle special tokens (start, stop, error)",
          "Add timing and progress metadata",
          "Forward chunks to client immediately"
        ]
      }
    ]
  }
}
```

## 🔗 **n8n Integration Patterns**

### Consuming Xano Streaming APIs
```javascript
// n8n workflow for handling Xano streams
{
  "n8n_streaming_workflow": {
    "trigger": {
      "node": "Webhook",
      "purpose": "Receive streaming request from frontend"
    },
    "processing": [
      {
        "node": "HTTP Request",
        "method": "POST",
        "url": "{{xano_instance}}/api/stream-chat",
        "headers": {
          "Authorization": "Bearer {{jwt_token}}",
          "Accept": "text/event-stream"
        },
        "body": {
          "message": "{{user_input}}",
          "options": {
            "chunk_size": 10,
            "include_metadata": true
          }
        },
        "streaming": true
      },
      {
        "node": "Split In Batches",
        "purpose": "Process each streaming chunk separately"
      },
      {
        "node": "WebSocket",
        "purpose": "Forward chunks to frontend in real-time",
        "configuration": {
          "connection": "Persistent WebSocket to client",
          "message_format": "JSON with chunk content and metadata"
        }
      }
    ]
  }
}
```

### AI Content Generation Workflow
```javascript
// Complete AI content generation with streaming
{
  "content_generation_workflow": {
    "trigger": "Content request webhook",
    "nodes": [
      {
        "node": "Validate Input",
        "validation": [
          "Check content topic and requirements",
          "Verify user permissions",
          "Sanitize input parameters"
        ]
      },
      {
        "node": "Xano Streaming API",
        "endpoint": "/api/generate-content-stream",
        "streaming": true,
        "processing": "Real-time AI content generation"
      },
      {
        "node": "Content Processing",
        "actions": [
          "Format chunks for display",
          "Add SEO metadata",
          "Check content quality"
        ]
      },
      {
        "node": "Multi-Output",
        "destinations": [
          "WebSocket for real-time preview",
          "Database for content storage", 
          "CMS for publishing"
        ]
      }
    ]
  }
}
```

## 🌐 **WeWeb Integration**

### Frontend Streaming Client
```javascript
// WeWeb streaming implementation
{
  "weweb_streaming_client": {
    "component": "Custom JavaScript Component",
    "implementation": `
// WeWeb streaming API client
const StreamingClient = {
  async startStream(message, apiEndpoint) {
    const response = await fetch(apiEndpoint, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + this.getJWTToken(),
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 
        message,
        options: { chunk_size: 10, delay: 50 }
      })
    });

    if (!response.ok) {
      throw new Error('Streaming request failed');
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      
      if (done) {
        this.onStreamComplete();
        break;
      }

      const chunk = decoder.decode(value);
      buffer += chunk;
      
      // Process complete chunks (separated by newlines)
      const lines = buffer.split('\\n');
      buffer = lines.pop(); // Keep incomplete line in buffer
      
      lines.forEach(line => {
        if (line.trim()) {
          this.onChunkReceived(line);
        }
      });
    }
  },

  onChunkReceived(chunk) {
    // Update UI with new chunk
    this.appendToMessage(chunk);
    this.updateProgress();
    this.scrollToBottom();
  },

  onStreamComplete() {
    // Stream finished
    this.enableInput();
    this.saveConversation();
    this.showCompletionMessage();
  }
};`,
    
    "ui_components": {
      "chat_interface": {
        "message_display": "Scrollable container with real-time updates",
        "typing_indicator": "Show streaming progress",
        "input_field": "User message input with send button",
        "error_handling": "Display connection issues and retry options"
      },
      
      "progress_display": {
        "progress_bar": "Visual streaming progress",
        "chunk_counter": "Display chunks received",
        "status_text": "Current processing status"
      }
    }
  }
}
```

### Real-Time Dashboard
```javascript
// WeWeb dashboard with streaming metrics
{
  "real_time_dashboard": {
    "components": [
      {
        "component": "Metric Cards",
        "data_source": "Xano streaming analytics API",
        "update_frequency": "Real-time via streaming",
        "metrics": [
          "Active users",
          "API requests per minute", 
          "Response times",
          "Error rates"
        ]
      },
      {
        "component": "Live Charts",
        "library": "Chart.js with streaming plugin",
        "chart_types": [
          "Line charts for trends",
          "Bar charts for comparisons",
          "Gauge charts for current values"
        ]
      },
      {
        "component": "Activity Feed",
        "display": "Live user activity updates",
        "source": "Streaming event data from Xano"
      }
    ],
    
    "streaming_logic": {
      "initialization": "Connect to Xano streaming endpoints on page load",
      "data_handling": "Process incoming metric chunks and update charts",
      "error_recovery": "Automatic reconnection on connection loss",
      "performance": "Efficient DOM updates to prevent lag"
    }
  }
}
```

## 📊 **Large Dataset Streaming**

### Pagination + Streaming Approach
```javascript
// Streaming large datasets efficiently
{
  "large_dataset_streaming": {
    "scenario": "Stream 50,000+ records to client",
    "approach": "Combine pagination with streaming for optimal performance",
    
    "implementation": {
      "batch_size": 100,
      "max_batches": 500,
      "function_stack": [
        {
          "step": "Initialize Variables",
          "variables": {
            "offset": 0,
            "batch_size": 100,
            "has_more": true,
            "total_processed": 0
          }
        },
        {
          "step": "Streaming Loop",
          "function": "While Loop",
          "condition": "{{has_more}} === true",
          "inner_logic": [
            {
              "function": "Get Records",
              "table": "{{target_table}}",
              "limit": "{{batch_size}}",
              "offset": "{{offset}}",
              "order": "id ASC"
            },
            {
              "function": "Streaming API Response",
              "content": "{{records}}",
              "metadata": {
                "batch_number": "{{current_batch}}",
                "records_in_batch": "{{records.length}}",
                "total_processed": "{{total_processed}}",
                "progress_percentage": "{{(total_processed / estimated_total) * 100}}"
              }
            },
            {
              "function": "Update Variables",
              "updates": {
                "offset": "{{offset + batch_size}}",
                "total_processed": "{{total_processed + records.length}}",
                "has_more": "{{records.length === batch_size}}"
              }
            }
          ]
        },
        {
          "step": "Completion Signal",
          "function": "Streaming API Response",
          "content": "[COMPLETE]",
          "final_metadata": {
            "total_records": "{{total_processed}}",
            "processing_time": "{{elapsed_time}}",
            "status": "success"
          }
        }
      ]
    }
  }
}
```

## 🧪 **Testing Streaming APIs**

### Postman Testing
```javascript
// Comprehensive Postman testing approach
{
  "postman_streaming_tests": {
    "setup": {
      "request_type": "HTTP POST",
      "url": "{{xano_instance}}/api/stream-endpoint",
      "headers": {
        "Authorization": "Bearer {{jwt_token}}",
        "Content-Type": "application/json"
      }
    },
    
    "test_scenarios": [
      {
        "name": "Basic Streaming Test",
        "body": {
          "message": "Test streaming response",
          "options": { "chunk_size": 5, "delay": 100 }
        },
        "validation": [
          "Response starts within 200ms",
          "Chunks arrive with consistent timing",
          "Stream completes with [DONE] signal",
          "No errors or connection drops"
        ]
      },
      {
        "name": "Large Content Test",
        "body": {
          "message": "Test with large content that requires multiple chunks",
          "options": { "chunk_size": 10, "delay": 50 }
        },
        "validation": [
          "Handles large content gracefully",
          "Memory usage remains stable",
          "No timeout errors"
        ]
      },
      {
        "name": "Error Handling Test",
        "body": {
          "message": "Invalid request to test error handling"
        },
        "validation": [
          "Returns appropriate error messages",
          "Fails gracefully without hanging",
          "Error information is streamed back"
        ]
      }
    ]
  }
}
```

### Node.js Test Client
```javascript
// Custom Node.js streaming test client
const testStreamingAPI = () => {
  const https = require('https');
  
  const requestData = JSON.stringify({
    message: "Test streaming API",
    options: { 
      chunk_size: 10,
      delay: 100,
      include_metadata: true 
    }
  });

  const options = {
    hostname: 'your-instance.xano.io',
    path: '/api/stream-endpoint',
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.JWT_TOKEN}`,
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(requestData)
    }
  };

  console.log('Starting streaming test...');
  const startTime = Date.now();

  const req = https.request(options, (res) => {
    console.log(`Status: ${res.statusCode}`);
    console.log(`Headers:`, res.headers);
    
    let chunkCount = 0;
    let totalData = '';

    res.on('data', (chunk) => {
      chunkCount++;
      const chunkString = chunk.toString();
      totalData += chunkString;
      
      console.log(`Chunk ${chunkCount}: ${chunkString.substring(0, 50)}...`);
      console.log(`Time since start: ${Date.now() - startTime}ms`);
    });

    res.on('end', () => {
      console.log('\\n=== Stream Completed ===');
      console.log(`Total chunks received: ${chunkCount}`);
      console.log(`Total data length: ${totalData.length}`);
      console.log(`Total time: ${Date.now() - startTime}ms`);
      console.log(`Average chunk time: ${(Date.now() - startTime) / chunkCount}ms`);
    });

    res.on('error', (error) => {
      console.error('Stream error:', error);
    });
  });

  req.on('error', (error) => {
    console.error('Request error:', error);
  });

  req.write(requestData);
  req.end();
};

// Run the test
testStreamingAPI();
```

## 🚀 **Advanced Patterns**

### Multi-Source Data Streaming
```javascript
// Combine multiple data sources into single stream
{
  "multi_source_streaming": {
    "use_case": "Dashboard with multiple data feeds",
    "implementation": [
      {
        "step": "Initialize Streams",
        "function": "Create Variables",
        "variables": {
          "user_metrics": [],
          "system_metrics": [],
          "activity_feed": [],
          "stream_order": ["users", "system", "activity"]
        }
      },
      {
        "step": "For Each Data Source",
        "function": "For Each",
        "input": "{{stream_order}}",
        "processing": [
          {
            "function": "Conditional",
            "condition": "{{item}} === 'users'",
            "true_branch": [
              {
                "function": "Get Records",
                "table": "user_analytics"
              },
              {
                "function": "Streaming API Response",
                "content": "{{records}}",
                "metadata": {
                  "source": "users",
                  "type": "analytics"
                }
              }
            ]
          },
          {
            "function": "Conditional", 
            "condition": "{{item}} === 'system'",
            "true_branch": [
              {
                "function": "External API Request",
                "url": "{{monitoring_api_endpoint}}"
              },
              {
                "function": "Streaming API Response",
                "content": "{{response}}",
                "metadata": {
                  "source": "system",
                  "type": "monitoring"
                }
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### Error Handling and Resilience
```javascript
// Robust error handling for streaming APIs
{
  "error_handling_patterns": {
    "connection_recovery": {
      "client_side": {
        "reconnection_logic": `
// Automatic reconnection with exponential backoff
class StreamingClient {
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;
    this.reconnectDelay = 1000; // Start with 1 second
  }

  async startStream(data) {
    try {
      await this.connectAndStream(data);
      this.reconnectAttempts = 0; // Reset on success
    } catch (error) {
      console.error('Stream error:', error);
      await this.handleReconnection(data);
    }
  }

  async handleReconnection(data) {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      const delay = this.reconnectDelay * Math.pow(2, this.reconnectAttempts - 1);
      
      console.log(\`Reconnecting in \${delay}ms (attempt \${this.reconnectAttempts})\`);
      
      setTimeout(() => {
        this.startStream(data);
      }, delay);
    } else {
      console.error('Max reconnection attempts reached');
      this.onMaxRetriesReached();
    }
  }

  onMaxRetriesReached() {
    // Fall back to non-streaming mode
    this.fallbackToRegularAPI();
  }
}`,
        
        "fallback_strategy": "Switch to traditional API if streaming fails"
      },
      
      "server_side": {
        "error_streaming": [
          {
            "function": "Try/Catch Block",
            "try_block": "Main streaming logic",
            "catch_block": [
              {
                "function": "Streaming API Response",
                "content": "Error occurred: {{error_message}}",
                "metadata": {
                  "type": "error",
                  "recoverable": "{{is_recoverable}}",
                  "retry_after": "{{suggested_retry_delay}}"
                }
              }
            ]
          }
        ]
      }
    }
  }
}
```

## 🎯 **Best Practices**

### Performance Optimization
```javascript
// Streaming performance best practices
{
  "performance_guidelines": {
    "chunk_sizing": {
      "text_streaming": "50-200 characters per chunk",
      "data_streaming": "100-1000 records per chunk", 
      "ai_responses": "1-10 words per chunk for natural flow",
      "testing": "A/B test different sizes for optimal UX"
    },
    
    "timing_strategies": {
      "fixed_interval": "50-200ms between chunks",
      "adaptive_interval": "Adjust based on content complexity",
      "burst_mode": "Send chunks as fast as processed",
      "natural_pacing": "Mimic human-like response timing"
    },
    
    "resource_management": {
      "memory_usage": "Process chunks individually to minimize memory",
      "connection_limits": "Monitor concurrent streaming connections",
      "rate_limiting": "Implement appropriate request limits",
      "timeout_handling": "Set reasonable timeouts for chunk delivery"
    }
  }
}
```

### Security Considerations
```javascript
// Security best practices for streaming APIs
{
  "security_guidelines": {
    "authentication": {
      "jwt_validation": "Validate tokens before starting stream",
      "permission_checks": "Verify user access to requested data",
      "rate_limiting": "Prevent streaming API abuse"
    },
    
    "input_validation": {
      "sanitization": "Clean all input parameters",
      "size_limits": "Limit request payload size",
      "content_filtering": "Block malicious content patterns"
    },
    
    "data_protection": {
      "sensitive_data": "Never stream sensitive data in plain text",
      "encryption": "Use HTTPS for all streaming communications",
      "logging": "Log streaming activities for security audits"
    }
  }
}
```

---

*Streaming APIs revolutionize user experience by providing immediate, progressive feedback. Master these patterns to build responsive applications with AI chatbots, real-time dashboards, and efficient large dataset processing that keeps users engaged throughout the entire interaction.*