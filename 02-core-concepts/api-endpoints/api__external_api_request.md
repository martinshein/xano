---
title: "External API Requests in Xano"
description: "Connect Xano to any external service or API - perfect for integrating payment gateways, email services, AI tools, and more"
category: api-endpoints
tags:
  - External APIs
  - Integration
  - HTTP Requests
  - Webhooks
  - Third-party Services
difficulty: intermediate
reading_time: 10 minutes
last_updated: '2025-01-23'
prerequisites:
  - Basic understanding of APIs
  - Xano Function Stack knowledge
  - API authentication concepts
---

# External API Requests in Xano

## 📋 **Quick Summary**

**What it does:** External API Requests allow Xano to communicate with any third-party service, making it the bridge between your backend and external tools like Stripe, SendGrid, OpenAI, or any REST API.

**Why it matters:** This function enables you to:
- Integrate payment processing without storing sensitive data
- Send emails through professional services
- Connect to AI/ML services
- Sync data with CRMs and ERPs
- Chain multiple services in your workflows

**Time to implement:** 10-30 minutes per integration

---

## Understanding External API Requests

### What Are External API Requests?

Think of External API Requests as Xano making a phone call to another service. Just like n8n's HTTP Request node or Make's HTTP module, this function lets Xano reach out to any service with an API.

### 💡 **What This Means for You**

- **In n8n:** Similar to HTTP Request nodes, but running on your backend
- **In WeWeb:** Handle sensitive API calls server-side instead of exposing keys
- **In Make:** Complement your scenarios with secure backend processing

## Getting Started Quickly

### Three Ways to Create External API Requests

#### 1. 🤖 **AI Assistant Method** (Fastest)
1. Add External API Request function
2. Click the AI Assistant button
3. Describe what you want: "Connect to Stripe to create a customer"
4. Review and apply the generated configuration

#### 2. 📋 **cURL Import Method** (Most Accurate)
1. Copy cURL command from API documentation
2. Click "Import cURL" button in Xano
3. Paste the command
4. Xano auto-configures everything

#### 3. 🔧 **Manual Configuration** (Most Control)
Build your request piece by piece with full customization

## Essential Configuration

### Basic Request Structure

```yaml
URL: https://api.service.com/endpoint
Method: GET | POST | PUT | DELETE | PATCH
Headers:
  Authorization: Bearer YOUR_API_KEY
  Content-Type: application/json
Body:
  key: value
  nested:
    data: here
```

### 🔗 **n8n Integration Pattern**

When n8n calls Xano, which then calls external API:
```javascript
// n8n → Xano → External Service → n8n
1. n8n triggers Xano endpoint
2. Xano calls external API securely
3. Xano processes response
4. Xano returns clean data to n8n
```

### 🌐 **WeWeb Security Pattern**

Keep API keys safe by routing through Xano:
```javascript
// WeWeb → Xano → Stripe
// Never: WeWeb → Stripe (exposes keys)
// Always: WeWeb → Xano (with auth) → Stripe
```

## Common Integration Examples

### Example 1: Stripe Payment Processing

```json
{
  "url": "https://api.stripe.com/v1/customers",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer sk_live_...",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "params": {
    "email": "{customer_email}",
    "name": "{customer_name}"
  }
}
```

**💡 Pro Tip:** Store Stripe keys in Environment Variables, not hardcoded

### Example 2: SendGrid Email

```json
{
  "url": "https://api.sendgrid.com/v3/mail/send",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer SG...",
    "Content-Type": "application/json"
  },
  "params": {
    "personalizations": [{
      "to": [{"email": "{recipient}"}]
    }],
    "from": {"email": "noreply@company.com"},
    "subject": "Welcome!",
    "content": [{
      "type": "text/html",
      "value": "{email_body}"
    }]
  }
}
```

### Example 3: OpenAI GPT Integration

```json
{
  "url": "https://api.openai.com/v1/chat/completions",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer sk-...",
    "Content-Type": "application/json"
  },
  "params": {
    "model": "gpt-4",
    "messages": [
      {"role": "user", "content": "{user_prompt}"}
    ],
    "temperature": 0.7
  }
}
```

## Authentication Methods

### 1. API Key Authentication

Most common for services like SendGrid, Stripe:
```yaml
Headers:
  X-API-Key: your-key-here
  # or
  Authorization: Bearer your-key-here
```

### 2. OAuth 2.0 Flow

For services like Google, Microsoft:
1. Get authorization code
2. Exchange for access token
3. Use token in requests
4. Refresh when expired

### 3. Basic Authentication

For older APIs:
```yaml
Headers:
  Authorization: Basic base64(username:password)
```

### 🔧 **Make/Integromat Tip**

Use Xano for OAuth token management:
- Store refresh tokens securely
- Auto-refresh before expiry
- Share tokens across scenarios

## Handling Files and Multipart Data

### Sending Files to External Services

```javascript
// Upload to Cloudinary example
{
  "url": "https://api.cloudinary.com/v1_1/{cloud}/upload",
  "method": "POST",
  "params": {
    "file": file_resource, // From Xano file input
    "upload_preset": "unsigned_preset"
  }
}
```

### Receiving Files from APIs

1. Get file URL from API response
2. Use "Create File Resource" function
3. Store in Xano or pass to frontend

## Error Handling & Retries

### Implementing Smart Retries

```yaml
1. Try external request
2. If status != 200:
   - Wait 1 second
   - Try again (max 3 times)
   - Log error if all fail
3. Return success or error
```

### Common Error Patterns

| Error Code | Meaning | Solution |
|------------|---------|----------|
| 401 | Authentication failed | Check API key |
| 429 | Rate limited | Add delays between requests |
| 500 | Server error | Implement retry logic |
| timeout | Request too slow | Increase timeout setting |

## Security Best Practices

### 1. Never Expose API Keys

```yaml
❌ Bad: Hardcode in function
✅ Good: Use Environment Variables
✅ Better: Use Xano's Vault for secrets
```

### 2. Validate SSL Certificates

```yaml
Host Verification: true (recommended)
Peer Verification: true (recommended)
# Only set false for development
```

### 3. Use IP Whitelisting

For sensitive APIs:
1. Get Xano's static IP (Scale plan)
2. Whitelist in external service
3. Extra security layer

## Performance Optimization

### Timeout Settings

```yaml
Default: 30 seconds
Large files: 60-120 seconds
Quick checks: 5-10 seconds
```

### Caching Responses

For expensive or slow APIs:
1. Check cache first (Redis)
2. If miss, make external request
3. Store response in cache
4. Return cached data

### 🔗 **n8n Optimization**

Chain requests efficiently:
```javascript
// Instead of: n8n → API1, n8n → API2, n8n → API3
// Do: n8n → Xano → [API1, API2, API3] → n8n
// Result: 1 round trip instead of 3
```

## Debugging External Requests

### Using Run & Debug

1. Add External API Request to function
2. Click "Run & Debug"
3. Check:
   - Request details (headers, body)
   - Response status
   - Response body
   - Timing information

### Common Issues & Solutions

| Issue | Cause | Fix |
|-------|-------|-----|
| "Connection refused" | Wrong URL/port | Verify endpoint URL |
| "SSL certificate problem" | Self-signed cert | Disable peer verification (dev only) |
| "Timeout" | Slow API | Increase timeout value |
| "401 Unauthorized" | Bad credentials | Check API key format |

## Advanced Patterns

### Pattern 1: Webhook Relay

```yaml
# Receive webhook → Process → Forward
1. Xano receives webhook
2. Validate and transform data
3. Forward to multiple services
4. Return consolidated response
```

### Pattern 2: API Aggregation

```yaml
# Combine multiple API responses
1. Call Weather API
2. Call Traffic API
3. Call Calendar API
4. Merge data
5. Return unified response
```

### Pattern 3: Circuit Breaker

```yaml
# Prevent cascade failures
1. Track API failures
2. If failures > threshold
3. Stop calling API temporarily
4. Return cached/default data
5. Retry after cooldown
```

## 💡 **Pro Tips for No-Code Users**

1. **Start with Postman:** Test external APIs in Postman first, then import to Xano
2. **Use Request History:** Debug by checking what Xano actually sent
3. **Environment Variables:** Store different keys for dev/staging/production
4. **Mock During Development:** Create fake responses while building
5. **Document Everything:** Add notes about rate limits and requirements

## Real-World Use Cases

### E-commerce Integration
- Process payments (Stripe/PayPal)
- Calculate shipping (FedEx/UPS APIs)
- Send receipts (email service)
- Update inventory (ERP system)

### Marketing Automation
- Sync contacts with CRM
- Trigger email campaigns
- Post to social media
- Track analytics events

### AI-Powered Features
- Generate content (OpenAI)
- Analyze sentiment (AWS Comprehend)
- Translate text (DeepL)
- Process images (Cloudinary)

## Next Steps

- Master [API Authentication](../authentication/oauth-sso.md) for secure integrations
- Learn about [Webhooks](../../08-reference/functions/webhooks.md) for receiving data
- Explore [Background Tasks](../function-stack/background-tasks.md) for long-running operations

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Ask integration questions
- 🎥 [Video Tutorials](https://university.xano.com) - See integrations in action
- 📖 [API Directory](https://rapidapi.com) - Find APIs to integrate