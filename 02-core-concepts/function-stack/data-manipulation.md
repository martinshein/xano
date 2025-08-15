---
title: "Data Manipulation - Transform and Process Data"
description: "Master Xano's data manipulation functions for transforming, processing, and organizing data efficiently in function stacks"
category: function-stack
tags:
  - Data Manipulation
  - Variables
  - Conditionals
  - Loops
  - Data Processing
  - Logic Functions
difficulty: intermediate
reading_time: 10 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of function stacks
  - Basic knowledge of data types
  - Familiarity with programming logic
---

# Data Manipulation - Transform and Process Data

## 📋 **Quick Summary**

**What it does:** Data manipulation functions provide essential tools for transforming, processing, and organizing data within your function stacks using variables, conditionals, loops, and logical operations.

**Why it matters:** Data manipulation enables you to:
- **Control program flow** with conditionals and switches
- **Store and update values** with variables
- **Process collections** with loops and iterations
- **Implement business logic** with complex decision trees
- **Transform data structures** efficiently

**Time to implement:** 5-10 minutes for basic operations, 30+ minutes for complex logic workflows

---

## What You'll Learn

- Core data manipulation functions
- Variable management techniques
- Conditional logic patterns
- Loop operations for data processing
- Best practices for efficient data manipulation

## Core Functions

### 📦 **Variables**

Store and manage data throughout your function stack.

```javascript
// Create and update variables
let userCount = 0;
let processedItems = [];
let currentUser = null;

// Variable operations
function createVariable(name, value) {
  // Initialize variable
  return { [name]: value };
}

function updateVariable(variables, name, value) {
  // Update existing variable
  return { ...variables, [name]: value };
}
```

### 🔀 **Conditionals**

Implement decision logic with if/else statements.

```javascript
// Basic conditional logic
function processUserBasedOnRole(user) {
  if (user.role === 'admin') {
    return {
      access_level: 'full',
      permissions: ['read', 'write', 'delete', 'admin']
    };
  } else if (user.role === 'editor') {
    return {
      access_level: 'limited',
      permissions: ['read', 'write']
    };
  } else {
    return {
      access_level: 'basic',
      permissions: ['read']
    };
  }
}
```

### 🔄 **Switch Statements**

Handle multiple conditions efficiently.

```javascript
// Switch-based logic
function getResponseByStatus(status) {
  switch (status) {
    case 'pending':
      return { message: 'Request is being processed', color: 'yellow' };
    case 'approved':
      return { message: 'Request approved', color: 'green' };
    case 'rejected':
      return { message: 'Request rejected', color: 'red' };
    case 'cancelled':
      return { message: 'Request cancelled', color: 'gray' };
    default:
      return { message: 'Unknown status', color: 'black' };
  }
}
```

### 🔁 **Loops**

Iterate through collections and process data.

```javascript
// For each loop processing
function processUserArray(users) {
  const processed = [];
  
  for (const user of users) {
    processed.push({
      id: user.id,
      full_name: `${user.first_name} ${user.last_name}`,
      email_domain: user.email.split('@')[1],
      is_active: user.status === 'active'
    });
  }
  
  return processed;
}

// While loop for specific conditions
function processUntilCondition(items, maxProcessed = 100) {
  const results = [];
  let index = 0;
  
  while (index < items.length && results.length < maxProcessed) {
    const item = items[index];
    
    if (item.status === 'ready') {
      results.push({
        ...item,
        processed_at: new Date().toISOString()
      });
    }
    
    index++;
  }
  
  return results;
}
```

## Real-World Applications

### User Permission System

```javascript
// Complex permission logic
class PermissionProcessor {
  static determineUserAccess(user, resource) {
    let permissions = [];
    
    // Role-based permissions
    switch (user.role) {
      case 'super_admin':
        permissions = ['create', 'read', 'update', 'delete', 'admin'];
        break;
      case 'admin':
        permissions = ['create', 'read', 'update', 'delete'];
        break;
      case 'editor':
        permissions = ['create', 'read', 'update'];
        break;
      case 'viewer':
        permissions = ['read'];
        break;
      default:
        permissions = [];
    }
    
    // Resource-specific restrictions
    if (resource.type === 'sensitive' && user.role !== 'super_admin') {
      permissions = permissions.filter(p => p !== 'delete');
    }
    
    // User-specific overrides
    if (user.permissions_override) {
      for (const override of user.permissions_override) {
        if (override.action === 'grant') {
          permissions.push(override.permission);
        } else if (override.action === 'revoke') {
          permissions = permissions.filter(p => p !== override.permission);
        }
      }
    }
    
    return {
      user_id: user.id,
      resource_id: resource.id,
      permissions: [...new Set(permissions)],
      access_granted: permissions.length > 0
    };
  }
}
```

### E-commerce Order Processing

```javascript
// Order processing workflow
class OrderProcessor {
  static processOrder(order) {
    let processingSteps = [];
    let orderStatus = 'pending';
    let totalAmount = 0;
    
    // Calculate total amount
    for (const item of order.items) {
      const itemTotal = item.quantity * item.price;
      
      if (item.discount_percentage > 0) {
        const discount = itemTotal * (item.discount_percentage / 100);
        totalAmount += itemTotal - discount;
      } else {
        totalAmount += itemTotal;
      }
    }
    
    // Apply taxes
    const taxAmount = totalAmount * (order.tax_rate || 0.08);
    totalAmount += taxAmount;
    
    // Validate inventory
    let inventoryValid = true;
    for (const item of order.items) {
      if (item.stock_quantity < item.quantity) {
        inventoryValid = false;
        processingSteps.push({
          step: 'inventory_check',
          status: 'failed',
          message: `Insufficient stock for ${item.name}`
        });
      }
    }
    
    if (!inventoryValid) {
      orderStatus = 'inventory_failed';
    } else {
      processingSteps.push({
        step: 'inventory_check',
        status: 'passed',
        message: 'All items in stock'
      });
      
      // Process payment
      if (order.payment_method === 'credit_card') {
        if (this.validateCreditCard(order.payment_details)) {
          orderStatus = 'payment_processed';
          processingSteps.push({
            step: 'payment',
            status: 'completed',
            message: 'Payment successful'
          });
        } else {
          orderStatus = 'payment_failed';
          processingSteps.push({
            step: 'payment',
            status: 'failed',
            message: 'Credit card validation failed'
          });
        }
      }
    }
    
    return {
      order_id: order.id,
      status: orderStatus,
      total_amount: totalAmount,
      tax_amount: taxAmount,
      processing_steps: processingSteps,
      processed_at: new Date().toISOString()
    };
  }
  
  static validateCreditCard(cardDetails) {
    // Simplified validation
    return cardDetails.number && 
           cardDetails.expiry && 
           cardDetails.cvv && 
           cardDetails.number.length >= 13;
  }
}
```

## No-Code Integration Examples

### 🔗 **n8n Data Processing**

```javascript
// n8n function for data manipulation
function processWebhookData($input) {
  const data = $input.body;
  let results = [];
  
  // Process each item
  for (const item of data.items) {
    let processedItem = {
      id: item.id,
      processed: false,
      errors: []
    };
    
    // Validation logic
    if (!item.email) {
      processedItem.errors.push('Email required');
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(item.email)) {
      processedItem.errors.push('Invalid email format');
    }
    
    if (!item.name || item.name.length < 2) {
      processedItem.errors.push('Name must be at least 2 characters');
    }
    
    // Set processing status
    if (processedItem.errors.length === 0) {
      processedItem.processed = true;
      processedItem.formatted_name = item.name.trim().toLowerCase()
        .replace(/\b\w/g, l => l.toUpperCase());
    }
    
    results.push(processedItem);
  }
  
  return {
    total_items: data.items.length,
    processed_items: results.filter(r => r.processed).length,
    failed_items: results.filter(r => !r.processed).length,
    results: results
  };
}
```

### 🌐 **WeWeb Logic Implementation**

```javascript
// WeWeb conditional display logic
class WeWebLogicHelper {
  static showElementBasedOnConditions(element, conditions) {
    let shouldShow = true;
    
    // Check user role
    if (conditions.requiredRole) {
      const userRole = wwLib.auth.getUserRole();
      shouldShow = shouldShow && (userRole === conditions.requiredRole);
    }
    
    // Check subscription status
    if (conditions.requiresSubscription) {
      const hasSubscription = wwLib.user.hasActiveSubscription();
      shouldShow = shouldShow && hasSubscription;
    }
    
    // Check custom conditions
    if (conditions.customLogic) {
      shouldShow = shouldShow && conditions.customLogic();
    }
    
    // Apply visibility
    if (element) {
      element.style.display = shouldShow ? 'block' : 'none';
    }
    
    return shouldShow;
  }
  
  static processFormData(formData, validationRules) {
    const processed = {
      valid: true,
      errors: [],
      data: {}
    };
    
    for (const [field, value] of Object.entries(formData)) {
      const rules = validationRules[field];
      
      if (rules) {
        // Required field check
        if (rules.required && (!value || value.trim() === '')) {
          processed.errors.push(`${field} is required`);
          processed.valid = false;
          continue;
        }
        
        // Length validation
        if (rules.minLength && value.length < rules.minLength) {
          processed.errors.push(`${field} must be at least ${rules.minLength} characters`);
          processed.valid = false;
        }
        
        // Pattern validation
        if (rules.pattern && !new RegExp(rules.pattern).test(value)) {
          processed.errors.push(`${field} format is invalid`);
          processed.valid = false;
        }
      }
      
      // Store processed value
      processed.data[field] = value ? value.trim() : value;
    }
    
    return processed;
  }
}
```

## Best Practices

1. **Keep logic simple** - Break complex operations into smaller functions
2. **Validate inputs** - Always check data before processing
3. **Handle errors gracefully** - Provide meaningful error messages
4. **Use appropriate data structures** - Choose the right approach for each task
5. **Optimize loops** - Avoid unnecessary iterations

## Next Steps

- Learn [Arrays](arrays.md) for collection processing
- Master [Objects](objects.md) for data structures
- Explore [Filters](filters.md) for data transformation
- Understand [Variables](create-variable.md) for state management

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Logic and processing discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Data manipulation guides
- 📖 [Best Practices](../../best-practices/logic-patterns.md) - Efficient processing techniques
- 🔧 [Support](https://xano.com/support) - Complex logic assistance















-   

    
    -   Using These Docs
    -   Where should I start?
    -   Set Up a Free Xano Account
    -   Key Concepts
    -   The Development Life Cycle
    -   Navigating Xano
    -   Plans & Pricing

-   

    
    -   Building with Visual Development
        
        -   APIs
            
            -   [Swagger (OpenAPI Documentation)](../building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../building-with-visual-development/background-tasks.html)
        -   [Triggers](../building-with-visual-development/triggers.html)
        -   [Middleware](../building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](database-requests/get-record.html)
            -   [Add Record](database-requests/add-record.html)
            -   [Edit Record](database-requests/edit-record.html)
            -   [Add or Edit Record](database-requests/add-or-edit-record.html)
            -   [Patch Record](database-requests/patch-record.html)
            -   [Delete Record](database-requests/delete-record.html)
            -   [Bulk Operations](database-requests/bulk-operations.html)
            -   [Database Transaction](database-requests/database-transaction.html)
            -   [External Database Query](database-requests/external-database-query.html)
            -   [Direct Database Query](database-requests/direct-database-query.html)
            -   [Get Database Schema](database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](data-manipulation/create-variable.html)
            -   [Update Variable](data-manipulation/update-variable.html)
            -   [Conditional](data-manipulation/conditional.html)
            -   [Switch](data-manipulation/switch.html)
            -   [Loops](data-manipulation/loops.html)
            -   [Math](data-manipulation/math.html)
            -   [Arrays](data-manipulation/arrays.html)
            -   [Objects](data-manipulation/objects.html)
            -   [Text](data-manipulation/text.html)
                    -   [Security](security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](apis-and-lambdas/realtime-functions.html)
            -   [External API Request](apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](data-caching-redis.html)
        -   [Custom Functions](custom-functions.html)
        -   [Utility Functions](utility-functions.html)
        -   [File Storage](file-storage.html)
        -   [Cloud Services](cloud-services.html)
            -   Filters
        
        -   [Manipulation](../filters/manipulation.html)
        -   [Math](../filters/math.html)
        -   [Timestamp](../filters/timestamp.html)
        -   [Text](../filters/text.html)
        -   [Array](../filters/array.html)
        -   [Transform](../filters/transform.html)
        -   [Conversion](../filters/conversion.html)
        -   [Comparison](../filters/comparison.html)
        -   [Security](../filters/security.html)
            -   Data Types
        
        -   [Text](../data-types/text.html)
        -   [Expression](../data-types/expression.html)
        -   [Array](../data-types/array.html)
        -   [Object](../data-types/object.html)
        -   [Integer](../data-types/integer.html)
        -   [Decimal](../data-types/decimal.html)
        -   [Boolean](../data-types/boolean.html)
        -   [Timestamp](../data-types/timestamp.html)
        -   [Null](../data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](../additional-features/response-caching.html)
        
-   
    Testing and Debugging
    
    -   Testing and Debugging Function Stacks
    -   Unit Tests
    -   Test Suites

-   
    The Database
    
    -   Getting Started Shortcuts
    -   Designing your Database
    -   Database Basics
        
        -   [Using the Xano Database](../../the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](../../the-database/database-basics/field-types.html)
        -   [Relationships](../../the-database/database-basics/relationships.html)
        -   [Database Views](../../the-database/database-basics/database-views.html)
        -   [Export and Sharing](../../the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](../../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](../../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](../../ai-tools/mcp-builder/mcp-functions.html)
            -   Xano MCP Server

-   
    Build With AI
    
    -   Using AI Builders with Xano
    -   Building a Backend Using AI
    -   Get Started Assistant
    -   AI Database Assistant
    -   AI Lambda Assistant
    -   AI SQL Assistant
    -   API Request Assistant
    -   Template Engine
    -   Streaming APIs

-   
    File Storage
    
    -   File Storage in Xano
    -   Private File Storage

-   
    Realtime
    
    -   Realtime in Xano
    -   Channel Permissions
    -   Realtime in Webflow

-   
    Maintenance, Monitoring, and Logging
    
    -   Statement Explorer
    -   Request History
    -   Instance Dashboard
        
        -   Memory Usage
        
-   
    Building Backend Features
    
    -   User Authentication & User Data
        
        -   [Separating User Data](../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
            -   Webhooks
    -   Messaging
    -   Emails
    -   Custom Report Generation
    -   Fuzzy Search
    -   Chatbots

-   
    Xano Features
    
    -   Snippets
    -   Instance Settings
        
        -   [Release Track Preferences](../../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](../../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../../xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](../../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../../xano-features/metadata-api/content.html)
        -   [Search](../../xano-features/metadata-api/search.html)
        -   [File](../../xano-features/metadata-api/file.html)
        -   [Request History](../../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](../../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../../xano-features/metadata-api/token-scopes-reference.html)
        
-   
    Xano Transform
    
    -   Using Xano Transform

-   
    Xano Actions
    
    -   What are Actions?
    -   Browse Actions

-   
    Team Collaboration
    
    -   Realtime Collaboration
    -   Managing Team Members
    -   Branching & Merging
    -   Role-based Access Control (RBAC)

-   
    Agencies
    
    -   Xano for Agencies
    -   Agency Features
        
        -   [Agency Dashboard](../../agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](../../agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](../../agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](../../agencies/agency-features/agency-profile.html)
        -   [Commission](../../agencies/agency-features/commission.html)
        -   [Private Marketplace](../../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](../../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](../../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](../../enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](../../enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](../../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](../../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](../../enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](../../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](../../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](../../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](../../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](../../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](../../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](../../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](../../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](../../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
-   
    Special Pricing
    
    -   Students & Education
    -   Non-Profits

-   
    Security
    
    -   Best Practices

[Powered by GitBook]

On this page

Was this helpful?

Copy


2.  Functions

Data Manipulation 
=================

[[Create Variable]]

[[Update Variable]]

[[Conditional]]

[[Loops]]

[[Math]]

[[Arrays]]

[[Objects]]

[[Text]]

Last updated 6 months ago

Was this helpful?