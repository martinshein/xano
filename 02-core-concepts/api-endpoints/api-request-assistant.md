---
title: "API Request Assistant - AI-Powered Integration Helper"
description: "Use Xano's AI Assistant to automatically configure external API requests - perfect for no-code users connecting to third-party services"
category: api-endpoints
tags:
  - AI Assistant
  - External APIs
  - Automation
  - No-Code Tools
  - Integration Helper
difficulty: beginner
reading_time: 5 minutes
last_updated: '2025-01-23'
prerequisites:
  - Xano workspace access
  - Basic understanding of APIs
---

# API Request Assistant - AI-Powered Integration Helper

## 📋 **Quick Summary**

**What it does:** The API Request Assistant uses AI to automatically configure external API connections for you. Just describe what you want to do, and it generates the complete request configuration.

**Why it matters:** This tool enables you to:
- Connect to any API without reading complex documentation
- Avoid common configuration mistakes
- Save hours of trial and error
- Get working integrations in minutes, not hours

**Time to implement:** 2-5 minutes per API connection

---

## What is the API Request Assistant?

### Your AI Integration Expert

Think of the API Request Assistant as having an expert developer sitting next to you who knows how to connect to thousands of APIs. You describe what you want in plain English, and it writes the technical configuration for you.

### 💡 **What This Means for You**

- **No more reading API docs:** Just tell the AI what service you want to connect to
- **No more debugging headers:** The AI knows what each API needs
- **No more format confusion:** It handles JSON, XML, form-data automatically
- **Perfect for non-developers:** Speak naturally, get technical results

## How to Use the API Request Assistant

### Step 1: Add External API Request

1. Open your Function Stack in Xano
2. Click the **+** button to add a function
3. Navigate to **APIs & Lambdas** category
4. Select **External API Request**

### Step 2: Launch the AI Assistant

Click the **AI Assistant** button (magic wand icon) in the External API Request panel.

### Step 3: Describe Your Request

Tell the AI what you want in plain English:

#### 🔗 **Example Prompts for n8n Users**

```text
"I need to send data to Slack when my n8n workflow triggers this endpoint"

"Connect to Airtable and create a new record in my Customers table"

"Get the latest exchange rates from a currency API"
```

#### 🌐 **Example Prompts for WeWeb Users**

```text
"Set up Stripe to create a new customer with email and name"

"Connect to SendGrid to send a welcome email"

"Fetch user profile data from Auth0"
```

#### 🔧 **Example Prompts for Make/Integromat Users**

```text
"Connect to Google Sheets and append a new row"

"Send an SMS through Twilio with a verification code"

"Create a new contact in HubSpot CRM"
```

### Step 4: Review and Apply

The AI will generate:
- Complete URL with proper formatting
- Correct HTTP method (GET, POST, etc.)
- Required headers
- Properly formatted request body
- Authentication setup

Review the configuration and click **Apply** to use it.

### Step 5: Add Sensitive Information

For security, manually add:
- API keys
- Passwords
- Secret tokens
- Client secrets

**💡 Pro Tip:** Store these in Environment Variables instead of hardcoding

## Real-World Examples

### Example 1: Connecting to OpenAI

**Your prompt:**
```text
"Connect to OpenAI GPT-4 to analyze customer feedback sentiment"
```

**AI generates:**
```json
{
  "url": "https://api.openai.com/v1/chat/completions",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer [ADD_YOUR_API_KEY]",
    "Content-Type": "application/json"
  },
  "params": {
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": "Analyze the sentiment of the following feedback"
      },
      {
        "role": "user",
        "content": "{feedback_text}"
      }
    ]
  }
}
```

### Example 2: Stripe Payment Processing

**Your prompt:**
```text
"Create a Stripe customer and charge them $49.99 for a subscription"
```

**AI generates:**
```json
{
  "url": "https://api.stripe.com/v1/customers",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer [ADD_YOUR_SECRET_KEY]",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "params": {
    "email": "{customer_email}",
    "source": "{payment_token}",
    "metadata[subscription]": "premium"
  }
}
```

### Example 3: Sending Emails via SendGrid

**Your prompt:**
```text
"Send a password reset email using SendGrid"
```

**AI generates:**
```json
{
  "url": "https://api.sendgrid.com/v3/mail/send",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer [ADD_YOUR_API_KEY]",
    "Content-Type": "application/json"
  },
  "params": {
    "personalizations": [{
      "to": [{"email": "{user_email}"}],
      "dynamic_template_data": {
        "reset_link": "{reset_url}",
        "user_name": "{user_name}"
      }
    }],
    "template_id": "d-xxxxxxxxxxxxx",
    "from": {"email": "noreply@yourcompany.com"}
  }
}
```

## Advanced AI Assistant Features

### Iterative Refinement

Don't get it right the first time? Continue the conversation:

```text
You: "Connect to Slack to send a message"
AI: [generates basic configuration]
You: "Add formatting and mention a user"
AI: [updates with rich formatting and @mention syntax]
You: "Also include a button that links to our dashboard"
AI: [adds interactive button component]
```

### Understanding Complex APIs

The AI Assistant understands:
- OAuth flow requirements
- Pagination patterns
- Rate limiting considerations
- Webhook signatures
- Multi-part form data
- GraphQL queries

### API Documentation Import

You can even paste API documentation:

```text
"Here's the curl command from the docs: 
curl -X POST https://api.example.com/v1/data \
  -H 'Authorization: Bearer token' \
  -d '{\"key\":\"value\"}'"
```

The AI will convert it to Xano's format automatically.

## Best Practices

### 1. Be Specific in Your Prompts

❌ **Vague:** "Connect to payment API"
✅ **Specific:** "Connect to Stripe to create a checkout session for $29.99"

### 2. Mention Your Use Case

❌ **Generic:** "Get data from API"
✅ **Contextual:** "Get customer orders from Shopify to display in WeWeb dashboard"

### 3. Include Required Fields

❌ **Incomplete:** "Send email"
✅ **Complete:** "Send email with subject, recipient, and HTML body using SendGrid"

## Common Patterns by Platform

### 🔗 **For n8n Workflows**

When n8n triggers your Xano endpoint, use the AI Assistant to:
- Process webhook data
- Enrich data from multiple sources
- Transform formats between systems

### 🌐 **For WeWeb Apps**

Use the AI Assistant to set up:
- User authentication flows
- Payment processing
- File uploads to cloud storage
- Email notifications

### 🔧 **For Make Scenarios**

Configure integrations for:
- CRM synchronization
- Marketing automation
- Document generation
- Analytics tracking

## Troubleshooting

### Issue: AI Doesn't Understand My API

**Solution:** Provide more context:
- API name and version
- Link to documentation
- Example request from docs

### Issue: Configuration Doesn't Work

**Solution:** Iterate with the AI:
```text
"The request returns 401 error"
AI will suggest: "Check authorization header format..."
```

### Issue: Complex Authentication

**Solution:** Break it down:
```text
"First, I need to get an OAuth token from /auth/token, 
then use it to call /api/data"
```

## Security Considerations

### Never Share Sensitive Data with AI

✅ **Do:** "Add Stripe API key header"
❌ **Don't:** "Use key sk_live_abc123..."

### Use Environment Variables

After AI generates config:
1. Replace `[ADD_YOUR_API_KEY]` with environment variable
2. Store actual keys in Xano's Environment Variables
3. Reference them as `{env.STRIPE_KEY}`

## 💡 **Pro Tips**

1. **Save Common Patterns:** Copy successful configurations for reuse
2. **Test Incrementally:** Start with simple requests, then add complexity
3. **Check Rate Limits:** Ask AI about API rate limits
4. **Version Your APIs:** Ask AI to use specific API versions
5. **Document Purpose:** Add comments explaining what each request does

## Next Steps

- Try the [External API Request](api__external_api_request.md) function manually
- Learn about [API Authentication](../authentication/oauth-sso.md)
- Explore [Webhook](../../08-reference/functions/webhooks.md) configuration
- Master [Background Tasks](../function-stack/background-tasks.md) for long operations

## Need Help?

- 💬 [Xano Community](https://community.xano.com) - Share your AI prompts
- 🎥 [Video Tutorials](https://university.xano.com) - See AI Assistant in action
- 📚 [API Gallery](https://www.xano.com/api-gallery) - Pre-configured integrations