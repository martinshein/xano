---
title: "External API Request - Connect to Any Service"
description: "Call external APIs and web services from your Xano backend"
category: function-stack
subcategory: integrations
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- api
- external
- integration
- webhooks
- rest
---

# External API Request - Connect to Any Service



## Quick Summary

> **What it is:** Function to call any external API or web service from your backend
> 
> **When to use:** Integrating with third-party services like OpenAI, Stripe, SendGrid, or any REST API
> 
> **Key benefit:** Connect your backend to thousands of services without writing code
> 
> **Perfect for:** Non-developers building integrations with external tools and services

## What You'll Learn

- Setting up API requests
- Using the AI Assistant
- Authentication methods
- Handling responses
- Error management

## Quick Start with AI Assistant

### Step 1: Add External API Function
1. Click + in function stack
2. Select "APIs & Lambdas"
3. Choose "External API Request"

### Step 2: Use AI Assistant
1. Click "AI Assistant" button
2. Describe what you want:
   - "Call OpenAI to generate text"
   - "Send email with SendGrid"
   - "Get weather from OpenWeatherMap"
3. AI builds the request for you!

### Step 3: Add Your Credentials
```javascript
// AI creates structure, you add keys
API_KEY: env.OPENAI_API_KEY
```

## Manual Configuration

### Basic Request Structure
```javascript
External_API_Request {
  url: "https://api.example.com/endpoint",
  method: "POST",
  headers: {
    "Authorization": "Bearer " + env.API_KEY,
    "Content-Type": "application/json"
  },
  params: {
    data: Input.data,
    option: "value"
  }
}
```

## Integration Examples

### With n8n - Webhook to API
```javascript
// n8n sends webhook data
webhook_data = Input

// Call external API
response = External_API_Request {
  url: "https://api.service.com/process",
  method: "POST",
  headers: {
    "API-Key": env.SERVICE_API_KEY
  },
  params: webhook_data
}

// Return to n8n
return response.result
```

### With WeWeb - AI Integration
```javascript
// WeWeb sends user prompt
prompt = Input.message

// Call OpenAI
ai_response = External_API_Request {
  url: "https://api.openai.com/v1/chat/completions",
  method: "POST",
  headers: {
    "Authorization": "Bearer " + env.OPENAI_KEY,
    "Content-Type": "application/json"
  },
  params: {
    model: "gpt-3.5-turbo",
    messages: [
      {role: "user", content: prompt}
    ]
  }
}

return ai_response.choices[0].message.content
```

## Common API Patterns

### GET Request - Fetch Data
```javascript
// Weather API
weather = External_API_Request {
  url: "https://api.openweathermap.org/data/2.5/weather",
  method: "GET",
  params: {
    q: "London",
    appid: env.WEATHER_API_KEY,
    units: "metric"
  }
}

temperature = weather.main.temp
```

### POST Request - Send Data
```javascript
// Send email via SendGrid
email_result = External_API_Request {
  url: "https://api.sendgrid.com/v3/mail/send",
  method: "POST",
  headers: {
    "Authorization": "Bearer " + env.SENDGRID_KEY,
    "Content-Type": "application/json"
  },
  params: {
    personalizations: [{
      to: [{email: Input.recipient}]
    }],
    from: {email: "noreply@company.com"},
    subject: Input.subject,
    content: [{
      type: "text/html",
      value: Input.message
    }]
  }
}
```

### PUT Request - Update Data
```javascript
// Update CRM record
update = External_API_Request {
  url: "https://api.crm.com/contacts/" + Input.contact_id,
  method: "PUT",
  headers: {
    "API-Key": env.CRM_KEY
  },
  params: {
    name: Input.name,
    email: Input.email,
    updated: timestamp()
  }
}
```

### DELETE Request
```javascript
// Delete resource
deleted = External_API_Request {
  url: "https://api.service.com/items/" + Input.item_id,
  method: "DELETE",
  headers: {
    "Authorization": "Token " + env.API_TOKEN
  }
}
```

## Authentication Methods

### Bearer Token
```javascript
headers: {
  "Authorization": "Bearer " + env.TOKEN
}
```

### API Key Header
```javascript
headers: {
  "X-API-Key": env.API_KEY
}
```

### Basic Auth
```javascript
// Encode credentials
credentials = base64_encode(username + ":" + password)

headers: {
  "Authorization": "Basic " + credentials
}
```

### OAuth 2.0
```javascript
// First get token
token_response = External_API_Request {
  url: "https://oauth.provider.com/token",
  method: "POST",
  params: {
    grant_type: "client_credentials",
    client_id: env.CLIENT_ID,
    client_secret: env.CLIENT_SECRET
  }
}

// Then use token
access_token = token_response.access_token

// Make authenticated request
data = External_API_Request {
  url: "https://api.provider.com/data",
  headers: {
    "Authorization": "Bearer " + access_token
  }
}
```

## Handling Responses

### Success Handling
```javascript
response = External_API_Request(...)

if (response.status == "success") {
  // Process data
  return {
    success: true,
    data: response.data
  }
}
```

### Error Handling
```javascript
Try {
  response = External_API_Request(...)
  return response.data
} Catch (error) {
  // Log error
  Add_Log({
    type: "api_error",
    service: "external_api",
    error: error.message
  })
  
  // Return friendly error
  return {
    success: false,
    error: "Service temporarily unavailable"
  }
}
```

### Retry Logic
```javascript
max_retries = 3
retry_count = 0
success = false

While (retry_count < max_retries AND !success) {
  Try {
    response = External_API_Request(...)
    success = true
  } Catch {
    retry_count += 1
    Wait(1000 * retry_count)  // Exponential backoff
  }
}
```

## Working with cURL

### Import from Documentation
1. Copy cURL command from API docs
2. Click "Import cURL" button
3. Xano converts to request automatically!

Example cURL:
```bash
curl -X POST https://api.example.com/data \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

## Advanced Options

### Timeout Settings
```javascript
External_API_Request {
  url: "https://slow-api.com/endpoint",
  timeout: 30000,  // 30 seconds
  method: "GET"
}
```

### Follow Redirects
```javascript
External_API_Request {
  url: "https://redirect.example.com",
  follow_location: true,  // Follow 301/302 redirects
  max_redirects: 5
}
```

### Custom Response Type
```javascript
// For binary data
file_data = External_API_Request {
  url: "https://api.example.com/download",
  response_type: "binary"
}
```

## Common Integrations

### OpenAI/ChatGPT
```javascript
External_API_Request {
  url: "https://api.openai.com/v1/chat/completions",
  method: "POST",
  headers: {
    "Authorization": "Bearer " + env.OPENAI_KEY
  },
  params: {
    model: "gpt-3.5-turbo",
    messages: messages
  }
}
```

### Stripe Payments
```javascript
External_API_Request {
  url: "https://api.stripe.com/v1/charges",
  method: "POST",
  headers: {
    "Authorization": "Bearer " + env.STRIPE_SECRET
  },
  params: {
    amount: 2000,  // $20.00
    currency: "usd",
    source: token
  }
}
```

### Twilio SMS
```javascript
External_API_Request {
  url: "https://api.twilio.com/2010-04-01/Accounts/" + 
       env.TWILIO_ACCOUNT + "/Messages.json",
  method: "POST",
  headers: {
    "Authorization": "Basic " + base64_encode(
      env.TWILIO_ACCOUNT + ":" + env.TWILIO_AUTH
    )
  },
  params: {
    From: env.TWILIO_PHONE,
    To: recipient_phone,
    Body: message
  }
}
```

## Try This

Create your first API integration:
1. Add External API Request
2. Use AI Assistant to configure
3. Add environment variables for keys
4. Test with sample data
5. Handle errors gracefully

## Pro Tips

💡 **Use Environment Variables:** Never hardcode API keys

💡 **Test in Playground:** Use Run & Debug before going live

💡 **Add Timeouts:** Prevent hanging requests

💡 **Log Failures:** Track API errors for debugging

💡 **Cache Responses:** Use Redis for expensive API calls

## Common Gotchas

### Content-Type Headers
```javascript
// JSON requests need header
headers: {
  "Content-Type": "application/json"
}

// Form data different header
headers: {
  "Content-Type": "application/x-www-form-urlencoded"
}
```

### URL Encoding
```javascript
// Problem: Spaces in URL
url: "https://api.com/search?q=hello world"  // Breaks!

// Solution: Encode parameters
query = url_encode("hello world")
url: "https://api.com/search?q=" + query
```

### Rate Limiting
```javascript
// Add delays between requests
For Each item {
  Call_API(item)
  Wait(1000)  // 1 second delay
}
```

## Next Steps

1. Identify APIs to integrate
2. Get API credentials
3. Test with AI Assistant
4. Add error handling
5. Monitor usage and limits

Remember: External APIs open infinite possibilities - connect your backend to any service on the internet!