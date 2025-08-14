---
title: "APIs and Lambda Functions in Xano"
description: "Master the creation and management of APIs and serverless Lambda functions in Xano for your no-code workflows"
category: api-endpoints
tags:
  - APIs
  - Lambda Functions
  - Serverless
  - Backend Logic
  - No-Code Integration
difficulty: intermediate
reading_time: 8 minutes
last_updated: '2025-01-23'
prerequisites:
  - Basic understanding of APIs
  - Xano workspace setup
  - Function Stack basics
---

# APIs and Lambda Functions in Xano

## 📋 **Quick Summary**

**What it does:** APIs and Lambda functions are the core building blocks of your Xano backend. APIs expose your data and logic to external applications, while Lambda functions provide serverless computing for complex operations.

**Why it matters:** These components enable you to:
- Connect Xano to n8n workflows, WeWeb frontends, and Make automations
- Process data without managing servers
- Scale automatically based on demand
- Execute complex business logic visually

**Time to implement:** 15-30 minutes for basic API, 30-60 minutes for Lambda functions

---

## Understanding APIs in Xano

### What Are APIs?

APIs (Application Programming Interfaces) are the communication channels between your Xano backend and your no-code tools. Think of them as secure doorways that allow specific actions with your data.

### 💡 **What This Means for You**

In n8n, APIs become HTTP Request nodes. In WeWeb, they're data sources. In Make, they're HTTP modules. Every API you create in Xano can be instantly used in these tools.

## Creating Your First API

### Step-by-Step Process

1. **Navigate to API Section**
   - Click "API" in your Xano workspace
   - Select "Add API Endpoint"
   - Choose your method (GET, POST, PUT, DELETE, PATCH)

2. **Configure the Endpoint**
   ```
   Name: get_customer_data
   Path: /customers/{customer_id}
   Method: GET
   Authentication: Required (or Public for testing)
   ```

3. **Build the Function Stack**
   - Add "Query All Records" from database
   - Add filters based on customer_id
   - Add response formatting

### 🔗 **n8n Connection Example**

```json
{
  "method": "GET",
  "url": "https://your-instance.xano.io/api:ABC123/customers/{{$node.CustomerID.json.id}}",
  "authentication": {
    "type": "apiKey",
    "apiKey": "{{$credentials.xanoApi.apiKey}}"
  }
}
```

### 🌐 **WeWeb Setup**

1. Add Xano data source
2. Enter your API base URL
3. Configure authentication
4. Test connection with your endpoint

## Lambda Functions Explained

### What Are Lambda Functions?

Lambda functions are serverless code blocks that run on-demand. Unlike traditional APIs that wait for requests, Lambda functions can:
- Process data in the background
- Run scheduled tasks
- Handle complex calculations
- Integrate with external services

### When to Use Lambda Functions

| Use Case | Why Lambda? | Example |
|----------|-------------|---------|
| Data Processing | Runs without timeout limits | Bulk CSV import |
| Scheduled Tasks | Executes automatically | Daily report generation |
| Heavy Computations | Doesn't block API responses | Image processing |
| External Integrations | Handles long-running requests | Syncing with CRM |

## Creating Lambda Functions

### Basic Lambda Structure

1. **Create New Lambda**
   ```
   Name: process_daily_orders
   Trigger: Scheduled (Daily at 2 AM)
   Timeout: 300 seconds
   ```

2. **Add Function Logic**
   - Query yesterday's orders
   - Calculate totals
   - Generate report
   - Send via email

### Advanced Lambda Features

#### Using Deno Runtime

Lambda functions in Xano use Deno, a secure JavaScript runtime. This enables:
- File system access
- External API calls
- Complex data transformations
- Custom business logic

```javascript
// Example Lambda code
const orders = await db.query('orders', {
  created_at: { $gte: yesterday }
});

const report = orders.map(order => ({
  id: order.id,
  total: order.items.reduce((sum, item) => sum + item.price, 0)
}));

return { success: true, report };
```

## API Authentication & Security

### Authentication Methods

1. **API Key Authentication**
   - Best for: Server-to-server communication
   - Use in: n8n, Make, backend services
   
2. **JWT Authentication**
   - Best for: User-based access
   - Use in: WeWeb, Bubble, frontend apps

3. **OAuth 2.0**
   - Best for: Third-party integrations
   - Use in: Social logins, enterprise SSO

### Setting Up Authentication

```yaml
# For n8n users:
1. Generate API key in Xano
2. Add to n8n credentials
3. Use in HTTP Request node

# For WeWeb users:
1. Enable JWT auth in Xano
2. Configure auth plugin in WeWeb
3. Handle login/logout flows
```

## Rate Limiting & Performance

### Default Limits

- **API Calls:** 100 requests/second per endpoint
- **Lambda Execution:** 300 seconds max
- **Payload Size:** 10MB for requests, 50MB for responses

### 🔧 **Make/Integromat Optimization**

When using Make scenarios:
1. Enable "Sequential Processing" for rate-limited APIs
2. Use "Break" modules to handle errors
3. Implement exponential backoff for retries

## Best Practices for No-Code Users

### 1. Naming Conventions

Use clear, descriptive names:
- ✅ `get_customer_orders`
- ✅ `create_invoice`
- ❌ `api_1`
- ❌ `function_test`

### 2. Version Management

Always version your APIs:
```
/api/v1/customers
/api/v2/customers (with new fields)
```

### 3. Error Handling

Implement user-friendly error messages:
```json
{
  "error": {
    "code": "CUSTOMER_NOT_FOUND",
    "message": "No customer found with ID 123",
    "suggestion": "Please check the customer ID and try again"
  }
}
```

### 4. Testing Strategy

1. **Use Xano's Run & Debug**
   - Test with sample data
   - Check response format
   - Verify error handling

2. **Test in Your No-Code Tool**
   - n8n: Use "Execute Node" button
   - WeWeb: Use preview mode
   - Make: Use "Run once" feature

## Common Integration Patterns

### Pattern 1: CRUD Operations

```yaml
Create: POST /items
Read: GET /items/{id}
Update: PUT /items/{id}
Delete: DELETE /items/{id}
List: GET /items
```

### Pattern 2: Webhook Receiver

For n8n/Make webhooks:
1. Create POST endpoint in Xano
2. Add webhook URL to external service
3. Process incoming data in Function Stack
4. Return success response

### Pattern 3: Batch Processing

For handling multiple records:
```json
POST /batch/customers
{
  "operations": [
    { "action": "create", "data": {...} },
    { "action": "update", "id": 123, "data": {...} }
  ]
}
```

## Monitoring & Debugging

### Using Request History

1. Navigate to "Request History" in Xano
2. Filter by endpoint or status
3. Click to see full request/response
4. Use for debugging integration issues

### Performance Monitoring

Track these metrics:
- Response time (aim for <500ms)
- Error rate (target <1%)
- Throughput (requests/minute)

## 💡 **Pro Tips for No-Code Users**

1. **Start Simple:** Build basic CRUD APIs first, then add complexity
2. **Use Templates:** Xano provides API templates for common patterns
3. **Document Everything:** Add descriptions to your APIs for team members
4. **Test Incrementally:** Test each step in your Function Stack
5. **Monitor Usage:** Check request history weekly to spot issues

## Next Steps

- Learn about [External API Requests](api__external_api_request.md) to connect with other services
- Explore [Real-time Functions](function__realtime_functions.md) for live updates
- Master [API Documentation](swagger-openapi-documentation.md) for team collaboration

## Need Help?

- 📚 Check the [Xano Community](https://community.xano.com)
- 🎥 Watch [Video Tutorials](https://university.xano.com)
- 💬 Join the [Xano Discord](https://discord.gg/xano)