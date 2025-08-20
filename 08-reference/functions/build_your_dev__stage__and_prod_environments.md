---
category: functions
description: Complete CI/CD workflow guide for Xano with development environments, testing strategies, deployment pipelines, and team collaboration patterns
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - ci-cd.md
  - unit-tests.md
  - backup-and-restore.md
  - managing-team-members.md
subcategory: 08-reference/functions
tags:
  - ci-cd
  - deployment
  - testing
  - environments
  - collaboration
  - automation
title: Build your Dev, Stage, and Prod Environments
---

# Build your Dev, Stage, and Prod Environments

## 📋 **Quick Summary**
Learn how to set up proper development, staging, and production environments in Xano for seamless CI/CD workflows. This guide covers environment configuration, testing strategies, deployment pipelines, and team collaboration patterns for reliable software delivery.

## What You'll Learn
- How to set up development, staging, and production environments
- Environment configuration strategies for different Xano plans
- Testing and deployment workflows
- Team collaboration and access control
- Environment variable management
- Automated deployment strategies

## Understanding CI/CD in Xano

**CI/CD (Continuous Integration/Continuous Delivery)** streamlines software development by automating testing and deployment processes. In Xano, your function stacks serve as your codebase, with branching, testing, and deployment features enabling professional development workflows.

### Key Benefits
- **Faster Development**: Regular small updates with automated testing
- **Reduced Errors**: Catch issues early through systematic testing
- **Reliable Deployments**: Consistent, predictable release process
- **Team Collaboration**: Multiple developers working safely on the same project

## Environment Setup Strategies

### 1. Three-Tier Architecture

**Development Environment**
- Build new features and updates
- Experiment with database changes
- Test integration patterns
- No impact on live users

**Staging Environment**
- Mirror production setup
- Run comprehensive tests
- Validate feature completeness
- Performance testing

**Production Environment**
- Live user-facing application
- Stable, tested code only
- Monitoring and alerting
- Backup and recovery systems

### 2. Plan-Specific Implementation

**Launch/Self-Serve Plans: Branching Strategy**
```javascript
// Branch structure
├── main (production)
├── staging
└── development

// Deployment flow
dev → staging → production
```

**Scale/Enterprise Plans: Workspace Separation**
```javascript
// Workspace structure
├── myapp-production
├── myapp-staging  
└── myapp-development

// Deploy with Xano Link
XanoLink.deploy({
  source: 'myapp-staging',
  target: 'myapp-production',
  environment: 'prod'
});
```

**Enterprise Plans: Tenant Center**
```javascript
// Tenant structure
├── prod-tenant
├── staging-tenant
└── dev-tenant

// Environment management
TenantCenter.deploy({
  fromTenant: 'staging-tenant',
  toTenant: 'prod-tenant',
  validateTests: true
});
```
## Testing Strategy

### Unit Tests: Single Function Validation
```javascript
// Example: User registration test
{
  "name": "User Registration Test",
  "endpoint": "/auth/register",
  "method": "POST",
  "payload": {
    "email": "test@example.com",
    "password": "SecurePass123!"
  },
  "expectations": {
    "status": 201,
    "response": {
      "user_id": "number",
      "email": "test@example.com",
      "created_at": "timestamp"
    }
  },
  "errorTests": [
    {
      "case": "Duplicate email",
      "expectStatus": 409
    },
    {
      "case": "Invalid email format",
      "expectStatus": 400
    }
  ]
}
```

### Test Suites: End-to-End Workflows
```javascript
// Example: E-commerce workflow test
{
  "name": "Complete Purchase Flow",
  "steps": [
    {
      "name": "User Registration",
      "endpoint": "/auth/register",
      "storeResponse": "user_data"
    },
    {
      "name": "Add Product to Cart",
      "endpoint": "/cart/add",
      "useAuth": "user_data.token",
      "payload": {
        "product_id": 123,
        "quantity": 2
      }
    },
    {
      "name": "Process Payment",
      "endpoint": "/orders/create",
      "expectEmail": "confirmation"
    }
  ]
}
```

## Deployment Workflow

### 1. Development Phase
- Create feature branch
- Implement functionality
- Write comprehensive tests
- Local validation

### 2. Staging Deployment
```javascript
// Automated deployment script
function deployToStaging() {
  // Deploy code
  XanoDeploy.branch('development', 'staging');
  
  // Run tests
  const testResults = XanoTest.runSuite('staging');
  
  if (testResults.failures > 0) {
    throw new Error('Tests failed - blocking deployment');
  }
  
  // Notify team
  Slack.notify('Staging deployment successful ✅');
}
```

### 3. Production Release
```javascript
// Production deployment with safeguards
function deployToProduction() {
  // Pre-deployment checks
  const checks = {
    testsPass: XanoTest.validate('staging'),
    backupExists: XanoBackup.verify(),
    approvalReceived: TeamApproval.check()
  };
  
  if (!Object.values(checks).every(Boolean)) {
    throw new Error('Pre-deployment checks failed');
  }
  
  // Deploy with rollback capability
  XanoDeploy.production({
    source: 'staging',
    enableRollback: true,
    healthCheck: '/health'
  });
}
```
## Database Testing Considerations

### Test Database Strategy
**Test Suites create temporary database copies** for isolated testing. For large databases, consider:

- **Data Sources**: External database connections for testing
- **Empty Database Tests**: For logic-only validation
- **Seed Data**: Minimal test datasets
- **Mock Data**: Simulated responses for external services

```javascript
// Test configuration examples
{
  "testConfig": {
    "database": "empty",    // No database needed
    "mockResponses": {
      "stripe": {
        "charge": { "status": "succeeded" }
      }
    }
  }
}
```

## Environment Variable Management

### Branching/Merging Approach
```javascript
// Environment-aware variable retrieval
function getEnvironmentConfig() {
  const allVars = GetEnvironmentVariables();
  const branch = GetCurrentBranch();
  
  return {
    apiKey: allVars[`STRIPE_KEY_${branch.toUpperCase()}`],
    dbUrl: allVars[`DB_URL_${branch.toUpperCase()}`],
    webhookSecret: allVars[`WEBHOOK_SECRET_${branch.toUpperCase()}`]
  };
}
```

### Workspace/Tenant Separation
```javascript
// Environment-specific configurations
// Development Workspace
{
  "STRIPE_KEY": "sk_test_...",
  "DB_URL": "dev-database-url",
  "DEBUG_MODE": "true"
}

// Production Workspace  
{
  "STRIPE_KEY": "sk_live_...",
  "DB_URL": "prod-database-url",
  "DEBUG_MODE": "false"
}
```
## Team Collaboration

### Feature-Based Development
```javascript
// Team organization structure
{
  "teams": {
    "auth-team": ["user-registration", "login", "password-reset"],
    "payment-team": ["stripe-integration", "subscription", "invoicing"],
    "api-team": ["external-integrations", "webhooks", "rate-limiting"]
  },
  "collaboration": {
    "shared-functions": ["email-service", "logging", "validation"],
    "merge-approval": ["team-lead", "senior-dev"]
  }
}
```

### RBAC Access Control
```javascript
// Permission matrix
{
  "roles": {
    "developer": {
      "development": ["read", "write"],
      "staging": ["read"],
      "production": ["read"]
    },
    "team-lead": {
      "development": ["read", "write"],
      "staging": ["read", "write", "deploy"],
      "production": ["read"]
    },
    "devops": {
      "development": ["read", "write"],
      "staging": ["read", "write", "deploy"],
      "production": ["read", "write", "deploy"]
    }
  }
}
```

### Mock-Driven Development
```javascript
// Mock external API responses
{
  "mocks": {
    "stripe-payment": {
      "success": {
        "id": "ch_1234567890",
        "status": "succeeded",
        "amount": 2000
      },
      "failure": {
        "error": "card_declined",
        "decline_code": "insufficient_funds"
      }
    },
    "email-service": {
      "sent": { "message_id": "msg_123", "status": "queued" },
      "failed": { "error": "invalid_email", "code": 400 }
    }
  }
}
```

## n8n Integration Patterns

### Automated Deployment Webhook
```javascript
// n8n workflow: Auto-deploy on git push
{
  "trigger": "webhook",
  "nodes": [
    {
      "name": "Git Webhook",
      "type": "webhook",
      "filter": "branch === 'staging'"
    },
    {
      "name": "Run Tests",
      "type": "http-request",
      "url": "https://app.xano.com/api/test-suite/run"
    },
    {
      "name": "Deploy if Tests Pass",
      "type": "if",
      "condition": "{{ $json.tests_passed }}"
    },
    {
      "name": "Notify Team",
      "type": "slack",
      "message": "Deployment complete ✅"
    }
  ]
}
```

## WeWeb Environment Connection

```javascript
// Environment-aware API configuration
const apiConfig = {
  development: {
    baseURL: 'https://dev-api.yourapp.com',
    authHeader: 'Bearer dev-token'
  },
  staging: {
    baseURL: 'https://staging-api.yourapp.com', 
    authHeader: 'Bearer staging-token'
  },
  production: {
    baseURL: 'https://api.yourapp.com',
    authHeader: 'Bearer prod-token'
  }
};

// WeWeb variable binding
const currentEnv = wwLib.getFrontendContext().environment;
const config = apiConfig[currentEnv];
```

## Try This: Setup Your CI/CD Pipeline

1. **Create Three Environments**
   - Set up dev/staging/production branches or workspaces
   - Configure environment variables for each
   - Test database connectivity

2. **Build Test Suite**
   - Create unit tests for critical functions
   - Add workflow tests for user journeys
   - Include error handling validation

3. **Implement Deployment Pipeline**
   - Automate staging deployments
   - Require test passage before production
   - Set up team notifications

## Common Mistakes to Avoid

- **Skipping staging environment** - Always test changes before production
- **Insufficient test coverage** - Test both success and error scenarios  
- **Manual deployments** - Automate to reduce human error
- **Poor access control** - Limit production access to essential personnel
- **Missing rollback plan** - Always have a way to revert changes

## Pro Tips

💡 **Use feature flags** to control new functionality rollout

💡 **Implement health checks** for automated deployment validation

💡 **Monitor deployment metrics** to identify performance impacts

💡 **Automate database migrations** with version control

💡 **Create deployment checklists** for consistent process execution