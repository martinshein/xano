---
title: Webhooks Functions Reference
description: Complete guide to implementing webhooks in Xano - receive real-time event notifications from external services for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- webhooks
- events
- external-integrations
- real-time
- automation
- security
- signature-verification
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 02-core-concepts/function-stack/external-api-request.md
- 08-reference/functions/triggers.md
- 08-reference/functions/middleware.md
---

## 📋 **Quick Summary**

Webhooks are specialized API endpoints designed to receive automatic event notifications from external services. Unlike regular API endpoints triggered by user actions, webhooks are triggered when external systems push data to your Xano backend in real-time.

## What You'll Learn

- How to create secure webhook endpoints in Xano
- Processing webhook data with Get All Raw Input
- Implementing webhook security and signature verification
- Webhook integration patterns for n8n, WeWeb, and Make.com
- Best practices for webhook reliability and error handling
- Common webhook use cases and implementations

## Understanding Webhooks

### Webhooks vs Regular API Endpoints

**Regular API Endpoint:**
- User initiates request (e.g., form submission)
- Your system responds to user action
- Synchronous, request-response pattern

**Webhook Endpoint:**
- External service initiates request automatically
- Your system receives event notifications
- Asynchronous, event-driven pattern

### Common Webhook Use Cases

```javascript
// Payment processing (Stripe)
{
  "event": "payment_intent.succeeded",
  "data": {
    "object": {
      "amount": 2000,
      "currency": "usd",
      "customer": "cus_123",
      "status": "succeeded"
    }
  }
}

// User actions (GitHub)
{
  "action": "opened",
  "pull_request": {
    "id": 123,
    "title": "Add new feature",
    "user": {
      "login": "username"
    }
  }
}

// E-commerce orders (Shopify)
{
  "id": 450789469,
  "email": "customer@example.com",
  "created_at": "2025-01-17T10:00:00Z",
  "total_price": "199.00",
  "line_items": [...]
}
```

## Creating Webhook Endpoints

### Step 1: Create POST API Endpoint

```javascript
// Webhook endpoint configuration
{
  "method": "POST",
  "path": "/webhooks/stripe",
  "authentication": "none", // Handle security in function stack
  "function_stack": [
    "get_all_raw_input",
    "verify_webhook_signature",
    "process_webhook_data"
  ]
}
```

### Step 2: Get All Raw Input Function

The `Get All Raw Input` function captures the complete webhook payload without predefined input constraints.

```javascript
// Get All Raw Input configuration
{
  "function": "get_all_raw_input",
  "encoding": "json", // Most common for webhooks
  "output_variable": "webhook_payload"
}

// Alternative encodings
{
  "encoding": "form_data", // For form-encoded webhooks
  "encoding": "xml",       // For XML-based services
  "encoding": "raw"        // For binary or custom formats
}
```

### Step 3: Process Webhook Data

```javascript
// Processing webhook data
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "event_type",
      "value": "{{webhook_payload.type}}"
    },
    {
      "function": "conditional",
      "condition": "{{event_type}} == 'payment.succeeded'",
      "true_stack": [
        {
          "function": "add_record",
          "table": "payments",
          "data": {
            "stripe_id": "{{webhook_payload.data.object.id}}",
            "amount": "{{webhook_payload.data.object.amount}}",
            "status": "completed",
            "customer_id": "{{webhook_payload.data.object.customer}}"
          }
        }
      ]
    }
  ]
}
```

## Webhook Security Implementation

### 1. Signature Verification (Recommended)

Most secure method using cryptographic signatures.

#### Stripe Signature Verification
```javascript
// Stripe webhook signature verification
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "stripe_signature",
      "value": "{{request.headers['stripe-signature']}}"
    },
    {
      "function": "create_variable", 
      "name": "webhook_secret",
      "value": "{{env.STRIPE_WEBHOOK_SECRET}}"
    },
    {
      "function": "create_variable",
      "name": "calculated_signature",
      "value": "{{hmac_sha256(webhook_payload_raw, webhook_secret)}}"
    },
    {
      "function": "conditional",
      "condition": "{{stripe_signature}} == {{calculated_signature}}",
      "false_stack": [
        {
          "function": "return_response",
          "status": 401,
          "body": {"error": "Invalid signature"}
        }
      ]
    }
  ]
}
```

#### GitHub Signature Verification
```javascript
// GitHub webhook signature verification
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "github_signature",
      "value": "{{request.headers['x-hub-signature-256']}}"
    },
    {
      "function": "create_variable",
      "name": "expected_signature", 
      "value": "sha256={{hmac_sha256(webhook_payload_raw, env.GITHUB_WEBHOOK_SECRET)}}"
    },
    {
      "function": "conditional",
      "condition": "{{github_signature}} == {{expected_signature}}",
      "false_stack": [
        {
          "function": "return_response",
          "status": 401,
          "body": {"error": "Unauthorized"}
        }
      ]
    }
  ]
}
```

### 2. Token-Based Authentication

Simpler approach using API keys or bearer tokens.

```javascript
// Token verification
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "webhook_token",
      "value": "{{request.headers['authorization']}}"
    },
    {
      "function": "create_variable",
      "name": "expected_token",
      "value": "Bearer {{env.WEBHOOK_SECRET_TOKEN}}"
    },
    {
      "function": "conditional",
      "condition": "{{webhook_token}} == {{expected_token}}",
      "false_stack": [
        {
          "function": "return_response", 
          "status": 403,
          "body": {"error": "Invalid token"}
        }
      ]
    }
  ]
}
```

### 3. IP Allowlisting

Additional security layer for known service IP ranges.

```javascript
// IP allowlist verification
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "client_ip",
      "value": "{{request.ip}}"
    },
    {
      "function": "create_variable",
      "name": "allowed_ips",
      "value": ["192.168.1.0/24", "10.0.0.0/8"]
    },
    {
      "function": "conditional",
      "condition": "{{client_ip in allowed_ips}}",
      "false_stack": [
        {
          "function": "return_response",
          "status": 403,
          "body": {"error": "IP not allowed"}
        }
      ]
    }
  ]
}
```

## No-Code Platform Integration

### n8n Webhook Triggers
```javascript
// Xano webhook to n8n workflow
{
  "webhook_url": "https://hooks.n8n.cloud/webhook/your-webhook-id",
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "{{webhook_url}}",
      "method": "POST",
      "data": {
        "source": "xano",
        "event": "{{webhook_payload.type}}",
        "payload": "{{webhook_payload}}",
        "timestamp": "{{now()}}"
      }
    }
  ]
}
```

### WeWeb Real-time Updates
```javascript
// WeWeb component updates via webhooks
{
  "function_stack": [
    {
      "function": "add_record",
      "table": "events", 
      "data": "{{webhook_payload}}"
    },
    {
      "function": "realtime_publish",
      "channel": "user_{{webhook_payload.user_id}}",
      "event": "webhook_received",
      "data": {
        "type": "{{webhook_payload.type}}",
        "timestamp": "{{now()}}"
      }
    }
  ]
}
```

### Make.com Scenario Triggers
```javascript
// Make.com integration
{
  "make_webhook": "https://hook.us1.make.com/your-webhook-url",
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "{{make_webhook}}",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json"
      },
      "data": {
        "webhook_source": "{{request.headers['user-agent']}}",
        "event_data": "{{webhook_payload}}",
        "processed_at": "{{now()}}"
      }
    }
  ]
}
```

## Advanced Webhook Patterns

### 1. Webhook Queue Processing
```javascript
// Queue webhooks for background processing
{
  "function_stack": [
    {
      "function": "add_record",
      "table": "webhook_queue",
      "data": {
        "payload": "{{webhook_payload}}",
        "status": "pending",
        "source": "{{request.headers['user-agent']}}",
        "received_at": "{{now()}}"
      }
    },
    {
      "function": "background_task",
      "task": "process_webhook_queue",
      "delay": 5
    }
  ]
}
```

### 2. Webhook Retry Logic
```javascript
// Implement retry mechanism for failed webhooks
{
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{webhook_payload.retry_count}} < 3",
      "true_stack": [
        {
          "function": "try_catch",
          "try_stack": [
            {
              "function": "process_webhook_data"
            }
          ],
          "catch_stack": [
            {
              "function": "external_api_request",
              "url": "{{webhook_payload.retry_url}}",
              "data": {
                "retry_count": "{{webhook_payload.retry_count + 1}}",
                "original_payload": "{{webhook_payload}}"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### 3. Webhook Transformation Pipeline
```javascript
// Transform webhook data before processing
{
  "transformation_pipeline": [
    {
      "function": "create_variable",
      "name": "normalized_data",
      "value": {
        "id": "{{webhook_payload.id || webhook_payload.event_id}}",
        "type": "{{webhook_payload.type || webhook_payload.event_type}}",
        "timestamp": "{{webhook_payload.created_at || webhook_payload.timestamp}}",
        "data": "{{webhook_payload.data || webhook_payload.object}}"
      }
    },
    {
      "function": "add_record",
      "table": "events",
      "data": "{{normalized_data}}"
    }
  ]
}
```

## Try This: Complete Webhook Implementation

Create a payment webhook handler:

```javascript
// Payment webhook complete implementation
{
  "endpoint": "/webhooks/payments",
  "method": "POST",
  "function_stack": [
    {
      "function": "get_all_raw_input",
      "encoding": "json",
      "output": "webhook_data"
    },
    {
      "function": "verify_signature",
      "signature_header": "stripe-signature",
      "secret": "{{env.STRIPE_WEBHOOK_SECRET}}"
    },
    {
      "function": "switch",
      "variable": "{{webhook_data.type}}",
      "cases": {
        "payment_intent.succeeded": [
          {
            "function": "add_record",
            "table": "payments",
            "data": {
              "stripe_id": "{{webhook_data.data.object.id}}",
              "amount": "{{webhook_data.data.object.amount}}",
              "status": "completed",
              "customer_email": "{{webhook_data.data.object.receipt_email}}"
            }
          },
          {
            "function": "external_api_request",
            "url": "{{env.EMAIL_SERVICE_URL}}",
            "data": {
              "to": "{{webhook_data.data.object.receipt_email}}",
              "template": "payment_confirmation",
              "data": {
                "amount": "{{webhook_data.data.object.amount / 100}}",
                "currency": "{{webhook_data.data.object.currency}}"
              }
            }
          }
        ],
        "payment_intent.payment_failed": [
          {
            "function": "add_record",
            "table": "failed_payments",
            "data": {
              "stripe_id": "{{webhook_data.data.object.id}}",
              "failure_reason": "{{webhook_data.data.object.last_payment_error.message}}"
            }
          }
        ]
      }
    },
    {
      "function": "return_response",
      "status": 200,
      "body": {"received": true}
    }
  ]
}
```

## Common Webhook Mistakes to Avoid

### ❌ Poor Practices
- Not verifying webhook signatures
- Processing webhooks synchronously without timeouts
- Not handling duplicate webhook deliveries
- Returning errors for expected webhook types
- Not logging webhook events for debugging

### ✅ Best Practices
- Always verify webhook authenticity
- Process webhooks asynchronously when possible
- Implement idempotency for duplicate handling
- Return success status for valid webhooks
- Log all webhook events with proper context

## Webhook Testing and Debugging

### Testing Tools
```javascript
// Use ngrok for local webhook testing
{
  "local_development": {
    "ngrok_url": "https://abc123.ngrok.io/webhooks/test",
    "webhook_payload": {
      "test": true,
      "event": "test_event",
      "data": {"message": "Hello webhook!"}
    }
  }
}
```

### Debugging Techniques
```javascript
// Webhook debugging
{
  "debug_webhook": [
    {
      "function": "add_record",
      "table": "webhook_logs",
      "data": {
        "headers": "{{request.headers}}",
        "payload": "{{webhook_payload}}",
        "ip": "{{request.ip}}",
        "timestamp": "{{now()}}"
      }
    }
  ]
}
```

## Pro Tips

### 💡 **Performance Optimization**
- Use background tasks for heavy webhook processing
- Implement webhook queues for high-volume scenarios
- Cache frequently accessed webhook configurations
- Set appropriate timeout values for external calls

### 🔒 **Security Best Practices**
- Always verify webhook signatures when available
- Use HTTPS for all webhook endpoints
- Implement rate limiting to prevent abuse
- Rotate webhook secrets regularly

### 📊 **Monitoring and Analytics**
- Track webhook success/failure rates
- Monitor webhook processing times
- Set up alerts for webhook failures
- Log webhook events for audit trails

### 🔄 **Reliability Patterns**
- Implement idempotency keys
- Handle webhook retries gracefully
- Validate webhook payload structure
- Provide clear error responses

## Troubleshooting Webhook Issues

### Common Problems
1. **Webhooks not received**: Check endpoint URL and firewall settings
2. **Signature verification failures**: Verify secret key and signature format
3. **Timeout errors**: Optimize processing time or use background tasks
4. **Duplicate processing**: Implement idempotency checks

Webhooks provide powerful real-time integration capabilities in Xano. Proper implementation with security, error handling, and monitoring ensures reliable event-driven workflows for no-code platforms.