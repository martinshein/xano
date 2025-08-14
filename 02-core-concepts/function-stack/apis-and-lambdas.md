---
title: APIs & Lambdas
description: Connect external services and execute custom code with visual API integrations and serverless Lambda functions
category: function-stack
difficulty: intermediate
last_updated: '2025-01-23'
related_docs:
  - external-api-request
  - lambda-functions
  - realtime-functions
subcategory: 02-core-concepts/function-stack
tags:
  - apis
  - lambda
  - external-integration
  - serverless
  - javascript
  - typescript
---

# APIs & Lambdas

**Quick Summary**
APIs & Lambdas help you connect with external services and run custom code within your visual workflows. Think of them as bridges that let your Xano backend communicate with other tools and execute specialized logic.

## What You'll Learn

- When to use external API requests vs Lambda functions
- How to connect with third-party services
- Building real-time functionality
- Best practices for external integrations

---

## Function Categories

The APIs and Lambda Functions category contains three powerful tools for extending your backend capabilities:

### External API Request
Connect to any web service or API - perfect for integrating with payment processors, email services, or any external platform.

**Common Use Cases:**
- Payment processing (Stripe, PayPal)
- Email services (SendGrid, Mailgun)
- SMS notifications (Twilio)
- Social media APIs
- Weather services
- Third-party data sources

### Lambda Functions  
Execute JavaScript or TypeScript code directly in your function stack - ideal for complex calculations or custom logic that visual functions can't handle.

**Common Use Cases:**
- Complex mathematical calculations
- Custom data transformations
- API response parsing
- Business rule implementations
- Integration with npm packages

### Realtime Functions
Trigger live updates and events across your application - perfect for chat features, live notifications, or collaborative tools.

**Common Use Cases:**
- Live chat systems
- Real-time notifications
- Collaborative editing
- Live dashboards
- Gaming features
- Activity feeds

---

## Try This: Build a Payment Notification System

**Scenario:** Create a system that processes payments and sends real-time notifications.

### Step 1: Process Payment with External API
```javascript
// External API Request to Stripe
POST https://api.stripe.com/v1/charges
Headers: {
  "Authorization": "Bearer sk_test_...",
  "Content-Type": "application/x-www-form-urlencoded"
}
Body: {
  "amount": 2000,
  "currency": "usd", 
  "source": "tok_visa",
  "description": "Order #1234"
}
```

### Step 2: Process Response with Lambda
```javascript
// Lambda Function to handle payment response
const paymentResult = $functions.external_api.response;

if (paymentResult.status === 'succeeded') {
  // Update order status
  const orderUpdate = {
    id: $input.order_id,
    status: 'paid',
    payment_id: paymentResult.id,
    paid_at: new Date()
  };
  
  return {
    success: true,
    order: orderUpdate,
    customer_email: $input.customer_email
  };
} else {
  return {
    success: false,
    error: paymentResult.failure_message
  };
}
```

### Step 3: Send Real-time Update
```javascript
// Realtime Function to notify customer
if ($functions.process_payment.success) {
  // Send to customer's channel
  const notification = {
    type: 'payment_success',
    order_id: $input.order_id,
    message: 'Your payment has been processed successfully!'
  };
  
  // Broadcast to user's channel
  channel: `user_${$auth.user.id}`,
  event: 'payment_notification',
  data: notification
}
```

---

## Integration Patterns for Visual Developers

### WeWeb Integration Pattern
1. **Frontend Action** → WeWeb button click
2. **API Call** → Xano endpoint with External API Request
3. **Lambda Processing** → Custom logic for response handling  
4. **Realtime Update** → Live UI updates in WeWeb

### n8n Automation Pattern
1. **Trigger** → Webhook from external service
2. **Lambda Function** → Process and validate data
3. **External API** → Forward to another service
4. **Realtime Event** → Notify connected users

---

## When to Use Each Tool

### Use External API Request When:
✅ Connecting to existing web services  
✅ Making HTTP requests to third parties  
✅ You need authentication headers/tokens  
✅ Working with REST or GraphQL APIs  

### Use Lambda Functions When:
✅ Complex data transformations needed  
✅ Mathematical calculations required  
✅ Custom business logic implementation  
✅ Need to use JavaScript/TypeScript libraries  
✅ Processing API responses before saving  

### Use Realtime Functions When:
✅ Building chat or messaging features  
✅ Live notifications required  
✅ Collaborative tools development  
✅ Real-time dashboard updates  
✅ Gaming or interactive features  

---

## Common Mistakes to Avoid

❌ **Using Lambda for simple operations**
- Visual functions are often simpler and faster

❌ **Not handling API errors properly** 
- Always check response status and handle failures

❌ **Hardcoding API keys**
- Use environment variables for sensitive data

❌ **Forgetting rate limits**
- Respect third-party API limitations

❌ **Overusing realtime events**
- Only send updates when necessary

---

## Pro Tips

💡 **API Integration Strategy**
- Test external APIs in isolation first
- Use Lambda functions to normalize different API responses
- Implement retry logic for unreliable services

💡 **Performance Optimization**
- Cache API responses when possible
- Use background tasks for non-urgent API calls
- Batch multiple operations when supported

💡 **Error Handling**
- Provide meaningful error messages
- Log API failures for debugging
- Implement fallback behaviors

💡 **Security Best Practices**
- Never expose API keys in frontend code
- Validate all external data before processing
- Use HTTPS for all external API calls

---

## Real-World Examples

### E-commerce Order Flow
1. **Order Creation** → Visual functions create order record
2. **Payment Processing** → External API Request to payment processor
3. **Inventory Update** → Lambda function calculates new stock levels
4. **Customer Notification** → Realtime function sends order confirmation

### Social Media Dashboard
1. **Data Fetching** → External API Requests to social platforms
2. **Data Processing** → Lambda functions normalize different API formats
3. **Analytics Calculation** → Lambda functions compute engagement metrics
4. **Live Updates** → Realtime functions push new data to dashboard

### Customer Support System
1. **Ticket Creation** → Visual functions store support ticket
2. **Auto-Assignment** → Lambda function implements assignment logic
3. **Email Notification** → External API Request to email service
4. **Status Updates** → Realtime functions notify agents and customers

---

**Next Steps:** Ready to dive deeper? Explore [External API Request](/root/xano-knowledge/02-core-concepts/function-stack/external-api-request.md) for detailed API integration or [Lambda Functions](/root/xano-knowledge/02-core-concepts/function-stack/lambda-functions.md) for custom code execution.