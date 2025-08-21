---
title: "User Data Separation & Access Control"
description: "Complete guide to implementing user data separation, RBAC patterns, and secure access control to ensure users only see their own data in Xano applications."
category: security
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-21'
tags:
  - user-data-separation
  - rbac
  - access-control
  - data-security
  - authentication
---

# User Data Separation & Access Control

## 📋 **Quick Summary**
Comprehensive guide to implementing secure user data separation in Xano. Learn how to ensure users only access their own data through proper filtering, authentication checks, and RBAC patterns for multi-tenant applications.

## What You'll Learn
- User data separation fundamentals and security principles
- Database filtering techniques for user-specific data
- Authentication and authorization patterns
- RBAC implementation for different user roles
- Multi-tenant data isolation strategies

## 🚀 Understanding User Data Separation

User data separation ensures that:
- **Users only see their own records** - No unauthorized access to other users' data
- **Role-based permissions** - Different access levels based on user roles
- **Secure API endpoints** - All endpoints properly authenticate and filter data
- **Data isolation** - Multi-tenant applications maintain strict data boundaries

## 🎯 Try This: Basic User Data Filtering

### Simple User-Specific Queries
```javascript
// Get user's own records only
get_user_orders = query_all_records({
  table: "orders",
  filter: [
    {
      field: "user_id",
      operator: "=",
      value: request.user.id  // From JWT authentication
    }
  ]
})

// Alternative using request context
get_user_profile = get_record({
  table: "user_profiles", 
  record_id: request.user.id
})
```

### Authentication-First Approach
```javascript
// Always validate authentication before data access
secure_user_data_access = function_stack([
  // 1. Validate JWT token
  authenticate_user,
  
  // 2. Check user exists and is active
  conditional({
    if: !request.user || request.user.status !== "active",
    then: return_error({
      status: 401,
      message: "Unauthorized access"
    })
  }),
  
  // 3. Filter data by user ID
  query_all_records({
    table: "user_documents",
    filter: [
      {
        field: "owner_id",
        operator: "=", 
        value: request.user.id
      }
    ]
  })
])
```

## 🔗 Integration Examples

### n8n User-Specific Workflows
```javascript
// Trigger n8n workflow with user-specific data
trigger_user_workflow = external_api_request({
  url: process.env.N8N_USER_WEBHOOK,
  method: "POST",
  headers: {
    "Authorization": "Bearer " + process.env.N8N_API_KEY,
    "X-User-ID": request.user.id  // Pass user context
  },
  data: {
    user_id: request.user.id,
    user_email: request.user.email,
    user_role: request.user.role,
    action: "process_user_data",
    data: user_specific_data
  }
})
```

### WeWeb User Context
```javascript
// Return user-specific data for WeWeb frontend
weweb_user_data = {
  user: {
    id: request.user.id,
    name: request.user.name,
    email: request.user.email,
    role: request.user.role
  },
  dashboard_data: query_all_records({
    table: "user_metrics",
    filter: [{ field: "user_id", operator: "=", value: request.user.id }]
  }),
  recent_activity: query_all_records({
    table: "activity_log",
    filter: [
      { field: "user_id", operator: "=", value: request.user.id }
    ],
    limit: 10,
    order_by: "created_at DESC"
  })
}
```

## 🔒 Advanced RBAC Patterns

### Role-Based Data Access
```javascript
// Dynamic data access based on user roles
role_based_data_access = conditional({
  // Admin users see all data
  if: request.user.role === "admin",
  then: query_all_records({ table: "orders" }),
  
  // Managers see their team's data  
  else_if: request.user.role === "manager",
  then: query_all_records({
    table: "orders",
    filter: [
      {
        field: "assigned_team",
        operator: "=",
        value: request.user.team_id
      }
    ]
  }),
  
  // Regular users see only their own data
  else: query_all_records({
    table: "orders", 
    filter: [
      {
        field: "user_id",
        operator: "=",
        value: request.user.id
      }
    ]
  })
})
```

### Hierarchical Permission System
```javascript
// Multi-level permission checking
check_data_access_permission = function_stack([
  // 1. Basic authentication
  authenticate_user,
  
  // 2. Get requested resource
  get_record({
    table: request.path_params.table,
    record_id: request.path_params.id
  }),
  
  // 3. Check ownership and permissions
  conditional({
    // Resource owner always has access
    if: response_data.user_id === request.user.id,
    then: create_variable({ name: "access_granted", value: true }),
    
    // Team members can view if shared
    else_if: response_data.shared_with_team && 
             response_data.team_id === request.user.team_id,
    then: create_variable({ name: "access_granted", value: true }),
    
    // Admins have full access
    else_if: request.user.role === "admin",
    then: create_variable({ name: "access_granted", value: true }),
    
    // Everyone else denied
    else: return_error({
      status: 403,
      message: "Access denied to this resource"
    })
  })
])
```

### Organization-Level Separation
```javascript
// Multi-tenant organization data isolation
org_data_isolation = function_stack([
  authenticate_user,
  
  // Validate user belongs to organization
  conditional({
    if: !request.user.organization_id,
    then: return_error({
      status: 400,
      message: "User must belong to an organization"
    })
  }),
  
  // Filter all queries by organization
  query_all_records({
    table: request.query.table || "default_table",
    filter: [
      {
        field: "organization_id",
        operator: "=",
        value: request.user.organization_id
      },
      // Additional user-specific filtering if needed
      {
        field: "user_id", 
        operator: "=",
        value: request.query.user_specific ? request.user.id : null
      }
    ]
  })
])
```

## ⚙️ Database Design for User Separation

### User Reference Patterns
```sql
-- Every user-owned table should have user_id
CREATE TABLE user_documents (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  content TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Multi-tenant organization pattern
CREATE TABLE organization_data (
  id SERIAL PRIMARY KEY,
  organization_id INTEGER NOT NULL REFERENCES organizations(id),
  user_id INTEGER NOT NULL REFERENCES users(id),
  data_type VARCHAR(50),
  data_content JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Team-based sharing pattern
CREATE TABLE team_resources (
  id SERIAL PRIMARY KEY,
  owner_id INTEGER NOT NULL REFERENCES users(id),
  team_id INTEGER REFERENCES teams(id),
  resource_type VARCHAR(50),
  visibility VARCHAR(20) DEFAULT 'private', -- private, team, organization
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Secure Indexes for Performance
```sql
-- Indexes for efficient user data filtering
CREATE INDEX idx_documents_user_id ON user_documents(user_id);
CREATE INDEX idx_documents_user_created ON user_documents(user_id, created_at);
CREATE INDEX idx_org_data_org_user ON organization_data(organization_id, user_id);
CREATE INDEX idx_team_resources_owner ON team_resources(owner_id);
CREATE INDEX idx_team_resources_team ON team_resources(team_id);
```

## 🔧 Middleware for Automatic Filtering

### Global User Data Middleware
```javascript
// Middleware to automatically filter user data
user_data_filter_middleware = function_stack([
  // Extract user ID from JWT
  authenticate_user,
  
  // Add user context to all database operations
  create_variable({
    name: "user_context",
    value: {
      user_id: request.user.id,
      organization_id: request.user.organization_id,
      role: request.user.role,
      team_id: request.user.team_id
    }
  }),
  
  // Auto-apply user filtering to queries
  conditional({
    if: request.query.auto_filter !== "false",
    then: create_variable({
      name: "default_filters",
      value: [
        {
          field: "user_id",
          operator: "=", 
          value: request.user.id
        }
      ]
    })
  })
])
```

### Table-Specific Security Rules
```javascript
// Security rules per table type
table_security_rules = {
  "user_profiles": {
    read: "owner_or_admin",
    write: "owner_only",
    delete: "owner_only"
  },
  "team_documents": {
    read: "team_member_or_admin", 
    write: "team_member",
    delete: "owner_or_team_lead"
  },
  "organization_settings": {
    read: "organization_member",
    write: "organization_admin",
    delete: "organization_owner"
  }
}

// Apply security rules
apply_table_security = function_stack([
  authenticate_user,
  
  // Get table security rule
  create_variable({
    name: "security_rule",
    value: table_security_rules[request.query.table]
  }),
  
  // Check permissions based on operation
  conditional({
    if: request.method === "GET" && security_rule.read === "owner_only",
    then: [
      query_all_records({
        table: request.query.table,
        filter: [{ field: "user_id", operator: "=", value: request.user.id }]
      })
    ],
    
    else_if: request.method === "POST" && security_rule.write === "team_member",
    then: [
      // Validate team membership before allowing write
      validate_team_membership,
      add_record({
        table: request.query.table,
        data: merge(request.data, { user_id: request.user.id })
      })
    ]
  })
])
```

## 💡 Pro Tips

- **Always Filter by User**: Never trust client-side filtering for security
- **Use Middleware**: Implement consistent security checks across all endpoints
- **Database Indexes**: Index user_id fields for better query performance
- **Audit Logging**: Track who accessed what data and when
- **Test Security**: Regularly test with different user roles and permissions

## 🆘 Common Security Mistakes

- **Client-Side Filtering**: Relying on frontend to filter sensitive data
- **Missing Authentication**: Endpoints that don't verify user identity
- **Role Confusion**: Inconsistent role checking across different endpoints
- **Data Leakage**: Returning more data than necessary in API responses
- **Weak Session Management**: Not properly validating JWT tokens

## 🎯 Try This: Complete Security Implementation

### Secure API Endpoint Pattern
```javascript
// Complete secure endpoint implementation
secure_user_orders_endpoint = function_stack([
  // 1. Authentication middleware
  authenticate_user,
  
  // 2. Validate user is active
  conditional({
    if: request.user.status !== "active",
    then: return_error({ status: 401, message: "Account inactive" })
  }),
  
  // 3. Get user's orders with proper filtering
  query_all_records({
    table: "orders",
    filter: [
      { field: "user_id", operator: "=", value: request.user.id },
      // Optional date filtering
      request.query.from_date ? {
        field: "created_at",
        operator: ">=",
        value: request.query.from_date
      } : null
    ].filter(Boolean),
    limit: request.query.limit || 20,
    offset: request.query.offset || 0,
    order_by: "created_at DESC"
  }),
  
  // 4. Sanitize response data
  create_variable({
    name: "sanitized_orders",
    value: response_data.map(order => ({
      id: order.id,
      total: order.total,
      status: order.status,
      created_at: order.created_at,
      items_count: order.items.length
      // Never expose internal IDs or sensitive data
    }))
  }),
  
  // 5. Log access for audit
  add_record({
    table: "access_log",
    data: {
      user_id: request.user.id,
      action: "view_orders",
      resource_count: response_data.length,
      timestamp: now(),
      ip_address: $remote_ip
    }
  }),
  
  // 6. Return secure response
  {
    success: true,
    data: sanitized_orders,
    pagination: {
      limit: request.query.limit || 20,
      offset: request.query.offset || 0,
      total: sanitized_orders.length
    }
  }
])
```

## 📊 Security Checklist

| Security Layer | Implementation | Status |
|----------------|----------------|--------|
| Authentication | JWT validation on all endpoints | ✅ |
| User Filtering | All queries filter by user_id | ✅ |
| Role-Based Access | Different permissions by role | ✅ |
| Data Sanitization | Remove sensitive fields from responses | ✅ |
| Audit Logging | Track all data access | ✅ |
| Input Validation | Validate all user inputs | ✅ |
| Error Handling | Don't leak information in errors | ✅ |

## 🔄 Testing Your Security

```javascript
// Security test scenarios
security_tests = [
  // Test 1: User can only see their own data
  {
    test: "user_data_isolation",
    user: "user_a",
    expected: "only_user_a_data"
  },
  
  // Test 2: Unauthorized access returns 401  
  {
    test: "unauthorized_access",
    user: "no_token",
    expected: "401_error"
  },
  
  // Test 3: Admin can see all data
  {
    test: "admin_access",
    user: "admin_user", 
    expected: "all_organization_data"
  },
  
  // Test 4: Cross-organization data leakage
  {
    test: "organization_isolation",
    user: "org_a_user",
    expected: "no_org_b_data"
  }
]
```

User data separation is fundamental to building secure, trustworthy applications. Always implement security at the database and API level, never rely on client-side restrictions!