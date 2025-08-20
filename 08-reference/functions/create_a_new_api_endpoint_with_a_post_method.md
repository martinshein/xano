---
category: functions
description: Complete guide to creating POST API endpoints and webhooks in Xano with security implementation, data processing patterns, and integration examples
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - webhooks.md
  - middleware.md
  - external-api-request.md
  - triggers.md
subcategory: 08-reference/functions
tags:
  - api
  - webhooks
  - post-method
  - security
  - integration
  - automation
title: Create a new API endpoint with a POST method
---

# Create a new API endpoint with a POST method

## 📋 **Quick Summary**
Learn to build secure POST API endpoints and webhooks in Xano for receiving data from external services, processing form submissions, and handling automated system integrations with proper validation and security measures.

## What You'll Learn
- How to create POST endpoints for data submission
- Webhook implementation with signature verification
- Data processing patterns for dynamic payloads
- Security best practices for public endpoints
- Integration patterns with n8n, WeWeb, and external services
- Error handling and response formatting

## Understanding POST Endpoints vs Webhooks

### POST API Endpoints
**User-initiated requests** where clients send data to your server:
- Form submissions
- Data creation requests
- File uploads
- Authentication requests

### Webhooks
**System-initiated requests** where external services push data to your endpoints:
- Payment notifications (Stripe, PayPal)
- User actions (Slack, Discord)
- System events (GitHub, Zapier)
- Real-time updates (WebSockets fallback)

```javascript
// Comparison
const requestTypes = {
  "POST Endpoint": {
    initiator: "User/Frontend",
    purpose: "Submit data",
    examples: ["form submission", "create user", "upload file"]
  },
  "Webhook": {
    initiator: "External Service", 
    purpose: "Receive notifications",
    examples: ["payment completed", "user mentioned", "deployment finished"]
  }
};
```

## Creating POST Endpoints

### Step 1: Create the Endpoint
```javascript
// Endpoint configuration
{
  "method": "POST",
  "path": "/api/users/create",
  "authentication": "required", // or "optional" for webhooks
  "inputs": {
    "name": {
      "type": "text",
      "required": true,
      "validation": "min:2,max:50"
    },
    "email": {
      "type": "text", 
      "required": true,
      "validation": "email,unique:users"
    },
    "password": {
      "type": "text",
      "required": true,
      "validation": "min:8,secure"
    }
  }
}
```

### Step 2: Build Function Stack
```javascript
// Function stack for user creation
[
  {
    "function": "Input Validation",
    "logic": `
      if (!inputs.email || !isValidEmail(inputs.email)) {
        return error(400, "Invalid email format");
      }
      if (inputs.password.length < 8) {
        return error(400, "Password must be at least 8 characters");
      }
    `
  },
  {
    "function": "Check Existing User",
    "query": "SELECT id FROM users WHERE email = ?",
    "params": ["inputs.email"]
  },
  {
    "function": "Hash Password",
    "filter": "hash_password",
    "input": "inputs.password"
  },
  {
    "function": "Create User",
    "action": "add_record",
    "table": "users",
    "data": {
      "name": "inputs.name",
      "email": "inputs.email", 
      "password": "hashed_password",
      "created_at": "now()"
    }
  },
  {
    "function": "Generate JWT",
    "filter": "create_jwt",
    "payload": {
      "user_id": "new_user.id",
      "email": "new_user.email"
    }
  },
  {
    "function": "Return Response",
    "response": {
      "success": true,
      "user": {
        "id": "new_user.id",
        "name": "new_user.name",
        "email": "new_user.email"
      },
      "token": "jwt_token"
    }
  }
]
```

### n8n Integration Example
```javascript
// n8n workflow: User registration with email verification
{
  "name": "User Registration Flow",
  "trigger": {
    "type": "webhook",
    "method": "POST",
    "path": "/register-user"
  },
  "nodes": [
    {
      "name": "Validate Input",
      "type": "javascript",
      "code": `
        const { name, email, password } = $json;
        
        // Validation
        if (!email.includes('@')) {
          throw new Error('Invalid email format');
        }
        
        if (password.length < 8) {
          throw new Error('Password too short');
        }
        
        return { name, email, password, validated: true };
      `
    },
    {
      "name": "Create User in Xano",
      "type": "http-request",
      "url": "https://app.xano.com/api/users/create",
      "method": "POST",
      "body": {
        "name": "{{ $json.name }}",
        "email": "{{ $json.email }}",
        "password": "{{ $json.password }}"
      }
    },
    {
      "name": "Send Welcome Email",
      "type": "email",
      "to": "{{ $json.email }}",
      "subject": "Welcome to Our Platform!",
      "template": "welcome-user"
    },
    {
      "name": "Add to CRM",
      "type": "http-request",
      "url": "https://api.hubspot.com/contacts",
      "body": {
        "email": "{{ $json.email }}",
        "name": "{{ $json.name }}",
        "source": "website-registration"
      }
    }
  ]
}
```

## Building Webhooks

### Step 1: Create Webhook Endpoint
```javascript
// Webhook endpoint configuration
{
  "method": "POST",
  "path": "/webhooks/stripe-payment",
  "authentication": "none", // Webhooks typically don't use standard auth
  "rate_limiting": {
    "requests_per_minute": 100,
    "burst_capacity": 20
  }
}
```

### Step 2: Process Dynamic Data
```javascript
// Function stack for webhook processing
[
  {
    "function": "Get All Raw Input",
    "encoding": "json", // or "form-data", "xml"
    "output": "raw_payload"
  },
  {
    "function": "Extract Headers",
    "headers": [
      "stripe-signature",
      "stripe-webhook-id",
      "content-type"
    ],
    "output": "request_headers"
  },
  {
    "function": "Verify Signature",
    "logic": `
      const signature = request_headers['stripe-signature'];
      const payload = raw_payload;
      const secret = environment_variables.STRIPE_WEBHOOK_SECRET;
      
      const expectedSignature = hmac_sha256(payload, secret);
      
      if (signature !== expectedSignature) {
        return error(401, "Invalid signature");
      }
    `
  },
  {
    "function": "Parse Event Data",
    "logic": `
      const eventData = JSON.parse(raw_payload);
      
      return {
        event_type: eventData.type,
        event_id: eventData.id,
        data: eventData.data.object,
        created: eventData.created
      };
    `
  },
  {
    "function": "Process Event",
    "conditional": "event_type",
    "cases": {
      "payment_intent.succeeded": "process_successful_payment",
      "payment_intent.payment_failed": "process_failed_payment", 
      "customer.subscription.created": "process_new_subscription",
      "invoice.payment_succeeded": "process_invoice_payment"
    }
  }
]
```

### Webhook Security Implementation
```javascript
// Signature verification function
function verifyWebhookSignature(payload, signature, secret) {
  // Extract timestamp and signature from header
  const elements = signature.split(',');
  const timestamp = elements.find(e => e.startsWith('t=')).replace('t=', '');
  const sig = elements.find(e => e.startsWith('v1=')).replace('v1=', '');
  
  // Create expected signature
  const payloadWithTimestamp = timestamp + '.' + payload;
  const expectedSig = hmac_sha256(payloadWithTimestamp, secret);
  
  // Verify signature matches
  if (sig !== expectedSig) {
    throw new Error('Invalid signature');
  }
  
  // Verify timestamp (prevent replay attacks)
  const now = Math.floor(Date.now() / 1000);
  if (now - parseInt(timestamp) > 300) { // 5 minute tolerance
    throw new Error('Timestamp too old');
  }
  
  return true;
}
```

### Advanced Webhook Processing
```javascript
// Multi-service webhook handler
{
  "function_stack": [
    {
      "name": "Identify Source",
      "logic": `
        const userAgent = request_headers['user-agent'] || '';
        const signature = request_headers['x-hub-signature-256'] || 
                         request_headers['stripe-signature'] || 
                         request_headers['paypal-auth-algo'];
        
        if (signature.includes('sha256=')) return 'github';
        if (signature.includes('t=')) return 'stripe';
        if (userAgent.includes('PayPal')) return 'paypal';
        
        return 'unknown';
      `
    },
    {
      "name": "Route to Handler",
      "switch": "webhook_source",
      "cases": {
        "github": {
          "function": "handle_github_webhook",
          "security": "verify_github_signature"
        },
        "stripe": {
          "function": "handle_stripe_webhook", 
          "security": "verify_stripe_signature"
        },
        "paypal": {
          "function": "handle_paypal_webhook",
          "security": "verify_paypal_signature"
        }
      }
    }
  ]
}
```

## WeWeb Integration Patterns

### Form Submission Handler
```javascript
// WeWeb component: Contact form
const contactForm = {
  // Form submission method
  async submitForm() {
    this.loading = true;
    this.errors = {};
    
    try {
      const response = await wwLib.executeWorkflow('xano-contact-form', {
        name: this.formData.name,
        email: this.formData.email,
        message: this.formData.message,
        source: 'website-contact'
      });
      
      if (response.success) {
        this.showSuccess = true;
        this.resetForm();
        
        // Track conversion
        wwLib.executeWorkflow('track-conversion', {
          event: 'contact-form-submitted',
          email: this.formData.email
        });
      }
    } catch (error) {
      this.errors.general = error.message;
    } finally {
      this.loading = false;
    }
  },
  
  // Real-time validation
  validateField(field, value) {
    switch (field) {
      case 'email':
        if (!value.includes('@')) {
          this.errors.email = 'Please enter a valid email';
        } else {
          delete this.errors.email;
        }
        break;
      case 'message':
        if (value.length < 10) {
          this.errors.message = 'Message must be at least 10 characters';
        } else {
          delete this.errors.message;
        }
        break;
    }
  }
};
```

### Real-time Webhook Processing
```javascript
// WeWeb: Live webhook monitoring
const webhookMonitor = {
  // Connect to real-time updates
  connectToWebhooks() {
    wwLib.realtime.connect('/webhooks/live-feed', {
      onMessage: (data) => {
        this.addWebhookEvent(data);
        this.updateStats(data);
      },
      onError: (error) => {
        console.error('Webhook feed error:', error);
      }
    });
  },
  
  // Process webhook events
  addWebhookEvent(event) {
    this.recentEvents.unshift({
      id: event.id,
      type: event.type,
      source: event.source,
      timestamp: event.timestamp,
      status: event.success ? 'success' : 'failed',
      data: event.data
    });
    
    // Keep only last 100 events
    if (this.recentEvents.length > 100) {
      this.recentEvents = this.recentEvents.slice(0, 100);
    }
  },
  
  // Update dashboard stats
  updateStats(event) {
    this.stats.totalEvents += 1;
    if (event.success) {
      this.stats.successfulEvents += 1;
    } else {
      this.stats.failedEvents += 1;
    }
    
    // Update source stats
    if (!this.stats.sources[event.source]) {
      this.stats.sources[event.source] = 0;
    }
    this.stats.sources[event.source] += 1;
  }
};
```

## Error Handling and Response Formatting

### Standardized Error Responses
```javascript
// Error handling middleware
function handleWebhookError(error, context) {
  const errorResponse = {
    success: false,
    error: {
      code: error.code || 'WEBHOOK_ERROR',
      message: error.message,
      timestamp: new Date().toISOString(),
      webhook_id: context.webhook_id,
      source: context.source
    }
  };
  
  // Log error for monitoring
  logWebhookError({
    error: errorResponse,
    payload: context.raw_payload,
    headers: context.headers
  });
  
  // Return appropriate HTTP status
  const statusCode = getErrorStatusCode(error.code);
  return response(statusCode, errorResponse);
}

function getErrorStatusCode(errorCode) {
  const statusMap = {
    'INVALID_SIGNATURE': 401,
    'MALFORMED_PAYLOAD': 400,
    'RATE_LIMITED': 429,
    'PROCESSING_ERROR': 422,
    'WEBHOOK_ERROR': 500
  };
  
  return statusMap[errorCode] || 500;
}
```

### Success Response Format
```javascript
// Standardized success response
function formatWebhookSuccess(processedData, context) {
  return {
    success: true,
    data: {
      processed_at: new Date().toISOString(),
      webhook_id: context.webhook_id,
      event_type: processedData.event_type,
      actions_taken: processedData.actions || [],
      next_steps: processedData.next_steps || null
    },
    meta: {
      processing_time: Date.now() - context.start_time,
      version: '1.0'
    }
  };
}
```

## Try This: Build Your First Webhook

1. **Create Basic Webhook Endpoint**
   - Set up POST endpoint with no authentication
   - Add "Get All Raw Input" function
   - Test with simple payload

2. **Add Security Verification**
   - Implement signature verification
   - Add timestamp validation
   - Test with real webhook service

3. **Build Processing Logic**
   - Parse webhook payload
   - Add conditional processing
   - Store relevant data in database

4. **Connect to Frontend**
   - Create monitoring dashboard in WeWeb
   - Add real-time event display
   - Implement error notifications

## Common Mistakes to Avoid

- **Missing signature verification** - Always validate webhook authenticity
- **Blocking synchronous processing** - Use background tasks for heavy operations
- **Poor error handling** - Implement comprehensive error responses
- **Ignoring replay attacks** - Validate timestamps and use idempotency keys
- **Insufficient logging** - Log all webhook events for debugging

## Pro Tips

💡 **Use middleware for common webhook patterns** - Create reusable verification logic

💡 **Implement idempotency** - Handle duplicate webhook deliveries gracefully

💡 **Set up monitoring and alerting** - Track webhook failure rates and performance

💡 **Version your webhook endpoints** - Plan for API evolution and backward compatibility

💡 **Test with webhook simulation tools** - Use ngrok, RequestBin, or service-specific testing tools