---
title: "Swagger OpenAPI Documentation"
description: "Generate and manage API documentation using OpenAPI/Swagger standards in Xano"
category: function-stack
difficulty: intermediate
tags:
  - swagger
  - openapi
  - documentation
  - api-docs
  - specifications
related_docs:
  - apis
  - endpoints
  - api-testing
  - metadata
last_updated: '2025-01-23'
---

# Swagger OpenAPI Documentation

## Quick Summary
Swagger/OpenAPI documentation provides standardized API specifications that make your Xano APIs easy to understand, test, and integrate with external systems. Xano automatically generates interactive API documentation that developers can use to explore and test your endpoints.

## What You'll Learn
- How to access and customize your API documentation
- Understanding OpenAPI specification format
- Configuring endpoint descriptions and parameters
- Using interactive testing features
- Sharing documentation with external developers
- Best practices for API documentation

## Understanding Swagger Documentation

Xano automatically generates OpenAPI 3.0 compliant documentation for all your API endpoints. This documentation includes:

### Core Features
- **Interactive Testing**: Test endpoints directly in the browser
- **Parameter Documentation**: Detailed input/output specifications
- **Response Examples**: Sample data for each endpoint
- **Authentication Requirements**: Security scheme documentation
- **Schema Definitions**: Data model specifications

### Accessing Your Documentation
```
https://[your-instance].xano.io/swagger
```

## Configuration and Customization

### Endpoint Documentation
Configure each endpoint with detailed descriptions:

```yaml
# Endpoint Configuration Example
title: "Get User Profile"
summary: "Retrieve user profile information"
description: "Returns detailed user profile including preferences and settings"
tags: ["Users", "Profiles"]
```

### Parameter Documentation
Define clear parameter descriptions:

```json
{
  "name": "user_id",
  "in": "path",
  "required": true,
  "description": "Unique identifier for the user",
  "schema": {
    "type": "integer",
    "minimum": 1
  }
}
```

### Response Schema Examples
Document expected responses:

```json
{
  "200": {
    "description": "User profile retrieved successfully",
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string", "format": "email"}
          }
        }
      }
    }
  }
}
```

## Integration Patterns

### For n8n Users
Use Swagger documentation to configure HTTP Request nodes:

```javascript
// n8n HTTP Request Configuration
{
  "method": "GET",
  "url": "https://your-instance.xano.io/api:endpoint",
  "headers": {
    "Authorization": "Bearer {{$node['Auth'].json['token']}}"
  }
}
```

### For WeWeb Users
Import API specifications directly:

1. Copy Swagger JSON URL from Xano
2. Import into WeWeb API connections
3. Auto-configure data sources and actions

### For External Developers
Share documentation URL for easy integration:

```bash
# Download OpenAPI specification
curl https://your-instance.xano.io/swagger.json > api-spec.json

# Generate client libraries
swagger-codegen generate -i api-spec.json -l javascript
```

## Advanced Documentation Features

### Custom Tags and Grouping
Organize endpoints with tags:

```yaml
tags:
  - name: "Authentication"
    description: "User authentication endpoints"
  - name: "Data Management"
    description: "CRUD operations for data"
```

### Security Scheme Documentation
Document authentication requirements:

```yaml
securitySchemes:
  BearerAuth:
    type: http
    scheme: bearer
    bearerFormat: JWT
```

### Example Requests and Responses
Provide comprehensive examples:

```json
{
  "example": {
    "user": {
      "name": "John Doe",
      "email": "john@example.com",
      "preferences": {
        "notifications": true,
        "theme": "dark"
      }
    }
  }
}
```

## Try This
1. **Access Your Documentation**: Visit your Xano Swagger URL
2. **Test an Endpoint**: Use the "Try it out" feature
3. **Download Specification**: Export OpenAPI JSON
4. **Share with Team**: Send documentation URL to developers

## Common Mistakes to Avoid

❌ **Don't:**
- Leave endpoint descriptions empty
- Forget to document required parameters
- Ignore response schema definitions
- Skip authentication documentation

✅ **Do:**
- Write clear, descriptive endpoint summaries
- Document all parameters with examples
- Include response schemas and examples
- Specify authentication requirements clearly

## Pro Tips

💡 **Documentation Best Practices:**
- Use consistent naming conventions
- Include realistic example data
- Document error responses (400, 401, 500)
- Add descriptions for complex business logic

🚀 **Integration Efficiency:**
- Export specifications for version control
- Use tags to organize related endpoints
- Include rate limiting information
- Document pagination patterns

⚡ **Developer Experience:**
- Test all examples before sharing
- Include common use case scenarios
- Provide client library generation instructions
- Update documentation with API changes

## Performance Considerations

### Documentation Generation
- Swagger documentation is generated automatically
- No performance impact on API execution
- Updates reflect immediately when endpoints change

### Client Code Generation
- Use OpenAPI generators for consistent client libraries
- Validate generated code against live endpoints
- Version client libraries with API changes

## Integration with External Tools

### Postman Integration
Import OpenAPI specification directly into Postman:

```bash
# Import process
1. Copy Swagger JSON URL
2. File > Import in Postman
3. Paste URL to auto-generate collection
```

### API Gateway Integration
Use documentation for gateway configuration:

```yaml
# Kong/AWS API Gateway
swagger: "3.0.0"
paths:
  /users/{id}:
    get:
      x-kong-plugin-rate-limiting:
        minute: 100
```

Your Swagger documentation serves as the single source of truth for API specifications, making integration with external systems seamless and reducing developer onboarding time.