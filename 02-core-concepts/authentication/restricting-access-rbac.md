---
title: "Role-Based Access Control (RBAC) in Xano - Complete Implementation Guide"
description: "Master RBAC implementation in Xano with comprehensive role management, permission systems, and security patterns for no-code applications"
category: authentication
tags:
  - RBAC
  - Role-Based Access Control
  - Authorization
  - Permissions
  - User Roles
  - Access Control
  - Security
  - Authentication
difficulty: intermediate
reading_time: 18 minutes
last_updated: '2025-01-23'
prerequisites:
  - Understanding of user authentication
  - Knowledge of Xano function stacks
  - Database schema design experience
  - JWT token concepts
---

# Role-Based Access Control (RBAC) in Xano

## 📋 **Quick Summary**

**What it does:** RBAC (Role-Based Access Control) restricts access to your application's features and data based on user roles and permissions, ensuring users only access what they're authorized to see and do.

**Why it matters:** RBAC provides:
- **Enhanced security** - Prevent unauthorized access to sensitive data and operations
- **Scalable permissions** - Manage access for thousands of users with role-based groups
- **Compliance readiness** - Meet regulatory requirements for data access controls
- **Reduced admin burden** - Assign roles instead of individual permissions
- **Clear access policies** - Define who can do what in your application

**Time to implement:** 1-2 hours for basic RBAC, 4-8 hours for enterprise-grade permission systems

---

## What You'll Learn

- RBAC concepts and security principles
- Database schema design for roles and permissions
- Multiple RBAC implementation patterns in Xano
- Advanced permission systems with hierarchical roles
- Frontend integration for role-based UI controls
- Best practices for enterprise security compliance

## Understanding RBAC Concepts

Think of RBAC like a company's organizational structure - instead of giving each employee individual keys to every room, you create role-based keycards. Marketing team members get access to marketing areas, IT gets access to server rooms, and executives get broader access.

### 🎯 **Core RBAC Components**

| Component | Description | Example |
|-----------|-------------|---------|
| **User** | Individual person using the system | john@company.com |
| **Role** | Job function or responsibility | Admin, Manager, Staff |
| **Permission** | Specific action or access right | Create User, View Reports |
| **Resource** | Protected data or functionality | User Records, Financial Data |

### 🔐 **RBAC vs Other Access Control Models**

**RBAC (Role-Based Access Control)**:
- Users assigned to roles, roles have permissions
- Scalable for large organizations
- Easy to audit and manage

**ABAC (Attribute-Based Access Control)**:
- Dynamic permissions based on user/resource attributes
- More flexible but complex to implement

**DAC (Discretionary Access Control)**:
- Resource owners control access
- Simple but doesn't scale well

## Database Schema Design for RBAC

### Basic RBAC Schema

```sql
-- Users table with role reference
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  role_id INTEGER REFERENCES roles(id),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Roles table
CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  description TEXT,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Sample roles
INSERT INTO roles (name, description) VALUES 
('admin', 'Full system access'),
('manager', 'Department management access'),
('staff', 'Basic user access'),
('viewer', 'Read-only access');
```

### Advanced RBAC with Permissions

```sql
-- Permissions table
CREATE TABLE permissions (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  description TEXT,
  resource VARCHAR(100) NOT NULL,
  action VARCHAR(50) NOT NULL
);

-- Role-Permission junction table (many-to-many)
CREATE TABLE role_permissions (
  id SERIAL PRIMARY KEY,
  role_id INTEGER REFERENCES roles(id),
  permission_id INTEGER REFERENCES permissions(id),
  UNIQUE(role_id, permission_id)
);

-- Sample permissions
INSERT INTO permissions (name, description, resource, action) VALUES 
('users_create', 'Create new users', 'users', 'create'),
('users_read', 'View user information', 'users', 'read'),
('users_update', 'Update user information', 'users', 'update'),
('users_delete', 'Delete users', 'users', 'delete'),
('reports_read', 'View reports', 'reports', 'read'),
('settings_update', 'Modify system settings', 'settings', 'update');
```

### Hierarchical Roles Schema

```sql
-- Roles with hierarchy support
CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  parent_role_id INTEGER REFERENCES roles(id),
  level INTEGER DEFAULT 0,
  description TEXT
);

-- Department-based access
CREATE TABLE departments (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  parent_id INTEGER REFERENCES departments(id)
);

-- User-Department-Role assignments
CREATE TABLE user_role_assignments (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  role_id INTEGER REFERENCES roles(id),
  department_id INTEGER REFERENCES departments(id),
  granted_at TIMESTAMP DEFAULT NOW(),
  granted_by INTEGER REFERENCES users(id)
);
```

## RBAC Implementation Patterns

### Pattern 1: Simple Role-Based Access (Database Lookup)

**Best for:** Basic applications with simple role requirements

```javascript
// Function Stack: Check User Role via Database
// Step 1: Get user record with role information
const userRecord = await getRecord({
  table: 'users',
  id: auth.user.id,
  include: ['role']
});

// Step 2: Precondition to check role
if (userRecord.role.name !== 'admin') {
  throw new Error('Access denied: Admin role required', 403);
}

// Step 3: Continue with protected operation
return await queryAllRecords({
  table: 'users'
});
```

**Xano Function Stack Setup:**
1. **Get Record** from `users` table using `auth.user.id`
2. **Precondition** with expression: `requester.role == "admin"`
3. **Query All Records** (or other protected operation)

### Pattern 2: Token-Based Access (JWT Extras)

**Best for:** High-performance applications requiring fast role checks

```javascript
// During login/signup, include role in JWT extras
function createAuthToken(user) {
  return generateJWT({
    user_id: user.id,
    extras: {
      role: user.role.name,
      permissions: user.role.permissions,
      department_id: user.department_id
    }
  });
}

// In protected endpoints, use extras for role checking
function checkAdminAccess() {
  // Precondition expression: auth.extras.role == "admin"
  if (auth.extras.role !== 'admin') {
    throw new Error('Admin access required', 403);
  }
}
```

### Pattern 3: Permission-Based Access Control

**Best for:** Complex applications with granular permissions

```javascript
// Advanced permission checking system
class PermissionChecker {
  static async hasPermission(userId, resource, action) {
    // Query user's permissions through roles
    const userPermissions = await queryRecords({
      table: 'user_role_assignments',
      filters: { user_id: userId },
      include: ['role.permissions']
    });
    
    // Check if user has required permission
    const hasPermission = userPermissions.some(assignment =>
      assignment.role.permissions.some(permission =>
        permission.resource === resource && 
        permission.action === action
      )
    );
    
    if (!hasPermission) {
      throw new Error(`Permission denied: ${resource}:${action}`, 403);
    }
    
    return true;
  }
  
  static async checkMultiplePermissions(userId, requirements) {
    for (const { resource, action } of requirements) {
      await this.hasPermission(userId, resource, action);
    }
    return true;
  }
}

// Usage in function stack
await PermissionChecker.hasPermission(
  auth.user.id, 
  'users', 
  'create'
);
```

### Pattern 4: Department-Based Access Control

**Best for:** Organizations with departmental data separation

```javascript
// Multi-tenant style access control
class DepartmentAccessControl {
  static async enforceDataAccess(userId, requestedData) {
    // Get user's department access
    const userAccess = await getRecord({
      table: 'users',
      id: userId,
      include: ['department', 'role']
    });
    
    // Check if user can access requested department data
    if (requestedData.department_id) {
      const hasAccess = await this.canAccessDepartment(
        userAccess,
        requestedData.department_id
      );
      
      if (!hasAccess) {
        throw new Error('Department access denied', 403);
      }
    }
    
    return userAccess;
  }
  
  static async canAccessDepartment(userAccess, targetDepartmentId) {
    // Admin can access all departments
    if (userAccess.role.name === 'admin') {
      return true;
    }
    
    // Users can access their own department
    if (userAccess.department_id === targetDepartmentId) {
      return true;
    }
    
    // Managers can access child departments
    if (userAccess.role.name === 'manager') {
      return await this.isChildDepartment(
        userAccess.department_id,
        targetDepartmentId
      );
    }
    
    return false;
  }
}
```

## Advanced RBAC Features

### Conditional Permissions

```javascript
// Time-based access control
class ConditionalRBAC {
  static checkBusinessHoursAccess(userRole) {
    const currentHour = new Date().getHours();
    const isBusinessHours = currentHour >= 9 && currentHour <= 17;
    
    // Non-admin users restricted to business hours
    if (userRole !== 'admin' && !isBusinessHours) {
      throw new Error('Access restricted to business hours', 403);
    }
    
    return true;
  }
  
  static checkLocationBasedAccess(userLocation, requiredLocation) {
    // Geographic access restrictions
    if (requiredLocation && userLocation !== requiredLocation) {
      throw new Error('Location-based access denied', 403);
    }
    
    return true;
  }
  
  static checkResourceOwnership(userId, resourceOwnerId, userRole) {
    // Users can access their own data, admins can access all
    if (userId === resourceOwnerId || userRole === 'admin') {
      return true;
    }
    
    throw new Error('Resource ownership access denied', 403);
  }
}
```

### Dynamic Role Assignment

```javascript
// Temporary role elevation
class DynamicRoleAssignment {
  static async grantTemporaryRole(userId, roleId, duration) {
    const expiresAt = new Date(Date.now() + duration);
    
    return await addRecord({
      table: 'temporary_role_assignments',
      data: {
        user_id: userId,
        role_id: roleId,
        expires_at: expiresAt,
        granted_by: auth.user.id
      }
    });
  }
  
  static async getUserActiveRoles(userId) {
    // Get permanent roles
    const permanentRoles = await queryRecords({
      table: 'user_role_assignments',
      filters: { user_id: userId },
      include: ['role']
    });
    
    // Get active temporary roles
    const temporaryRoles = await queryRecords({
      table: 'temporary_role_assignments',
      filters: {
        user_id: userId,
        'expires_at|>': new Date().toISOString()
      },
      include: ['role']
    });
    
    return [...permanentRoles, ...temporaryRoles];
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n RBAC Workflow**

```yaml
RBAC Check Workflow:
1. HTTP Request (Incoming API call)
2. Function Node (Extract auth token)
3. HTTP Request (Get user role from Xano)
4. Switch Node (Route based on role)
5. Different paths for different roles
6. HTTP Response (Return appropriate data)
```

**n8n Role Checking Function:**
```javascript
// Extract and validate user role
const authToken = $input.headers.authorization;
if (!authToken) {
  return { error: 'Authentication required' };
}

// Decode JWT to get user info
const decoded = jwt.decode(authToken.replace('Bearer ', ''));
const userRole = decoded.extras?.role;

// Route based on role
switch (userRole) {
  case 'admin':
    return { route: 'admin_data', permissions: ['read', 'write', 'delete'] };
  case 'manager':
    return { route: 'manager_data', permissions: ['read', 'write'] };
  case 'staff':
    return { route: 'staff_data', permissions: ['read'] };
  default:
    return { error: 'Invalid role' };
}
```

### 🌐 **WeWeb Role-Based UI Control**

```javascript
// WeWeb RBAC integration
class WeWebRBAC {
  constructor() {
    this.userRole = wwLib.auth.getUserRole();
    this.permissions = wwLib.auth.getUserPermissions();
  }
  
  // Check if user has specific permission
  hasPermission(resource, action) {
    return this.permissions.some(permission =>
      permission.resource === resource && permission.action === action
    );
  }
  
  // Check if user has any of the specified roles
  hasAnyRole(roles) {
    return roles.includes(this.userRole);
  }
  
  // Show/hide UI elements based on permissions
  setupUIPermissions() {
    // Hide admin panel for non-admins
    if (!this.hasAnyRole(['admin'])) {
      wwLib.hideElement('admin-panel');
    }
    
    // Disable delete buttons for users without delete permission
    if (!this.hasPermission('users', 'delete')) {
      wwLib.disableElements('.delete-button');
    }
    
    // Show manager features for managers and admins
    if (this.hasAnyRole(['admin', 'manager'])) {
      wwLib.showElement('manager-features');
    }
  }
  
  // Filter data based on user permissions
  filterDataByPermissions(data, resourceType) {
    if (this.userRole === 'admin') {
      return data; // Admins see everything
    }
    
    // Filter based on user's department or ownership
    return data.filter(item => {
      if (item.created_by === wwLib.auth.getUserId()) {
        return true; // Users can see their own data
      }
      
      if (this.userRole === 'manager' && 
          item.department_id === wwLib.auth.getUserDepartment()) {
        return true; // Managers see department data
      }
      
      return false;
    });
  }
}

// Initialize RBAC on page load
const rbac = new WeWebRBAC();
rbac.setupUIPermissions();

// Use in data binding
function loadUserData() {
  const data = wwLib.data.getAllUsers();
  return rbac.filterDataByPermissions(data, 'users');
}
```

### 🔧 **Make RBAC Automation**

```yaml
RBAC Validation Scenario:
1. Webhook (Receive request with auth token)
2. HTTP Request (Validate token with Xano)
3. JSON Parser (Extract user role and permissions)
4. Router (Branch based on role)
   - Admin path: Full access operations
   - Manager path: Limited management operations  
   - Staff path: Basic read operations
5. Error Handler (Handle access denied scenarios)
```

## Security Best Practices

### 1. Principle of Least Privilege

```javascript
// Always grant minimum required permissions
class LeastPrivilegeRBAC {
  static async assignRoleWithReview(userId, roleId, assignedBy) {
    // Log role assignment for audit trail
    await addRecord({
      table: 'role_assignment_log',
      data: {
        user_id: userId,
        role_id: roleId,
        assigned_by: assignedBy,
        assigned_at: new Date().toISOString(),
        reason: 'Initial assignment'
      }
    });
    
    // Set automatic review date
    const reviewDate = new Date();
    reviewDate.setMonth(reviewDate.getMonth() + 6);
    
    return await addRecord({
      table: 'user_role_assignments',
      data: {
        user_id: userId,
        role_id: roleId,
        review_due: reviewDate.toISOString()
      }
    });
  }
  
  static async reviewOverPrivilegedUsers() {
    // Find users with admin or high-privilege roles
    const highPrivilegeUsers = await queryRecords({
      table: 'user_role_assignments',
      filters: {
        'role.level|>=': 8 // High privilege level
      },
      include: ['user', 'role']
    });
    
    return highPrivilegeUsers.map(assignment => ({
      user: assignment.user.email,
      role: assignment.role.name,
      assigned_date: assignment.created_at,
      review_recommended: true
    }));
  }
}
```

### 2. Role Separation and Validation

```javascript
// Prevent role escalation attacks
class RoleValidation {
  static validateRoleAssignment(assignerRole, targetRole) {
    const roleHierarchy = {
      'viewer': 1,
      'staff': 2,
      'manager': 3,
      'admin': 4,
      'superadmin': 5
    };
    
    const assignerLevel = roleHierarchy[assignerRole];
    const targetLevel = roleHierarchy[targetRole];
    
    // Prevent privilege escalation
    if (targetLevel >= assignerLevel) {
      throw new Error('Cannot assign role equal or higher than your own', 403);
    }
    
    return true;
  }
  
  static validateSensitiveOperation(userRole, operation) {
    const sensitiveOperations = {
      'delete_all_users': ['superadmin'],
      'modify_permissions': ['admin', 'superadmin'],
      'view_audit_logs': ['admin', 'superadmin'],
      'system_settings': ['superadmin']
    };
    
    const allowedRoles = sensitiveOperations[operation] || [];
    
    if (!allowedRoles.includes(userRole)) {
      throw new Error(`Operation ${operation} not permitted for role ${userRole}`, 403);
    }
    
    return true;
  }
}
```

### 3. Audit Logging for RBAC

```javascript
// Comprehensive audit logging
class RBACAuditLogger {
  static async logAccessAttempt(userId, resource, action, success, details = {}) {
    return await addRecord({
      table: 'access_log',
      data: {
        user_id: userId,
        resource: resource,
        action: action,
        success: success,
        timestamp: new Date().toISOString(),
        ip_address: details.ip_address,
        user_agent: details.user_agent,
        details: JSON.stringify(details)
      }
    });
  }
  
  static async generateAccessReport(startDate, endDate) {
    const accessLogs = await queryRecords({
      table: 'access_log',
      filters: {
        'timestamp|>=': startDate,
        'timestamp|<=': endDate
      },
      include: ['user']
    });
    
    const report = {
      total_attempts: accessLogs.length,
      successful_attempts: accessLogs.filter(log => log.success).length,
      failed_attempts: accessLogs.filter(log => !log.success).length,
      top_accessed_resources: this.getTopResources(accessLogs),
      suspicious_activity: this.findSuspiciousActivity(accessLogs)
    };
    
    return report;
  }
  
  static findSuspiciousActivity(logs) {
    // Detect multiple failed access attempts
    const failedAttempts = logs.filter(log => !log.success);
    const attemptsByUser = {};
    
    failedAttempts.forEach(log => {
      if (!attemptsByUser[log.user_id]) {
        attemptsByUser[log.user_id] = [];
      }
      attemptsByUser[log.user_id].push(log);
    });
    
    // Flag users with more than 5 failed attempts in the period
    const suspicious = Object.entries(attemptsByUser)
      .filter(([userId, attempts]) => attempts.length > 5)
      .map(([userId, attempts]) => ({
        user_id: userId,
        failed_attempts: attempts.length,
        resources_attempted: [...new Set(attempts.map(a => a.resource))]
      }));
    
    return suspicious;
  }
}
```

## Enterprise RBAC Patterns

### Multi-Tenant RBAC

```javascript
// Tenant-aware role-based access control
class MultiTenantRBAC {
  static async checkTenantAccess(userId, tenantId, resource, action) {
    // Get user's tenant assignments
    const userTenants = await queryRecords({
      table: 'user_tenant_assignments',
      filters: { user_id: userId },
      include: ['tenant', 'role']
    });
    
    // Check if user has access to the specific tenant
    const tenantAccess = userTenants.find(
      assignment => assignment.tenant_id === tenantId
    );
    
    if (!tenantAccess) {
      throw new Error('Tenant access denied', 403);
    }
    
    // Check if user's role in this tenant allows the action
    const hasPermission = await this.checkTenantPermission(
      tenantAccess.role_id,
      resource,
      action
    );
    
    if (!hasPermission) {
      throw new Error(`Permission denied: ${resource}:${action} in tenant ${tenantId}`, 403);
    }
    
    return tenantAccess;
  }
  
  static async getUserTenantContext(userId) {
    const tenantAssignments = await queryRecords({
      table: 'user_tenant_assignments',
      filters: { user_id: userId, is_active: true },
      include: ['tenant', 'role.permissions']
    });
    
    return tenantAssignments.map(assignment => ({
      tenant_id: assignment.tenant_id,
      tenant_name: assignment.tenant.name,
      role: assignment.role.name,
      permissions: assignment.role.permissions.map(p => ({
        resource: p.resource,
        actions: p.actions
      }))
    }));
  }
}
```

### API Rate Limiting by Role

```javascript
// Role-based rate limiting
class RoleBasedRateLimit {
  static getRateLimitForRole(role) {
    const limits = {
      'viewer': { requests: 100, window: 3600 }, // 100/hour
      'staff': { requests: 500, window: 3600 },   // 500/hour
      'manager': { requests: 1000, window: 3600 }, // 1000/hour
      'admin': { requests: 5000, window: 3600 },   // 5000/hour
      'superadmin': null // No limits
    };
    
    return limits[role] || limits['viewer'];
  }
  
  static async checkRateLimit(userId, userRole) {
    const limit = this.getRateLimitForRole(userRole);
    
    if (!limit) return true; // No limits
    
    const windowStart = Math.floor(Date.now() / 1000) - limit.window;
    
    const recentRequests = await queryRecords({
      table: 'api_requests',
      filters: {
        user_id: userId,
        'timestamp|>=': windowStart
      }
    });
    
    if (recentRequests.length >= limit.requests) {
      throw new Error(`Rate limit exceeded: ${limit.requests} requests per ${limit.window} seconds`, 429);
    }
    
    // Log the request
    await addRecord({
      table: 'api_requests',
      data: {
        user_id: userId,
        timestamp: Math.floor(Date.now() / 1000)
      }
    });
    
    return true;
  }
}
```

## Testing RBAC Implementation

### Automated RBAC Testing

```javascript
// Test suite for RBAC functionality
class RBACTestSuite {
  static async runAllTests() {
    const results = [];
    
    // Test basic role assignments
    results.push(await this.testRoleAssignment());
    
    // Test permission checks
    results.push(await this.testPermissionChecks());
    
    // Test privilege escalation prevention
    results.push(await this.testPrivilegeEscalation());
    
    // Test tenant isolation
    results.push(await this.testTenantIsolation());
    
    return {
      total_tests: results.length,
      passed: results.filter(r => r.passed).length,
      failed: results.filter(r => !r.passed).length,
      results: results
    };
  }
  
  static async testRoleAssignment() {
    try {
      // Test admin can assign manager role
      await assignRole(1, 'manager', 'admin'); // Should succeed
      
      // Test staff cannot assign admin role
      try {
        await assignRole(2, 'admin', 'staff'); // Should fail
        return { test: 'role_assignment', passed: false, reason: 'Staff should not assign admin role' };
      } catch (error) {
        // Expected to fail
      }
      
      return { test: 'role_assignment', passed: true };
    } catch (error) {
      return { test: 'role_assignment', passed: false, error: error.message };
    }
  }
  
  static async testPermissionChecks() {
    try {
      // Test admin can access admin endpoints
      const adminAccess = await checkAccess(1, 'users', 'delete', 'admin');
      
      // Test staff cannot access admin endpoints
      try {
        await checkAccess(2, 'users', 'delete', 'staff');
        return { test: 'permission_checks', passed: false, reason: 'Staff should not delete users' };
      } catch (error) {
        // Expected to fail
      }
      
      return { test: 'permission_checks', passed: true };
    } catch (error) {
      return { test: 'permission_checks', passed: false, error: error.message };
    }
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Implement basic RBAC with three roles:
1. Create users, roles, and role_assignments tables
2. Build login endpoint that includes role in JWT
3. Create admin-only endpoint using precondition
4. Test role-based access control

### Intermediate Challenge
Build permission-based access control:
1. Create permissions and role_permissions tables
2. Implement permission checking function
3. Create middleware for automatic permission checks
4. Build admin interface for role management

### Advanced Challenge
Design enterprise multi-tenant RBAC:
1. Add tenant isolation with cross-tenant access controls
2. Implement hierarchical roles and departments
3. Create audit logging and compliance reporting
4. Build role analytics dashboard

## Common Mistakes to Avoid

1. **Client-side only access control** - Always validate permissions server-side
2. **Overly complex role hierarchies** - Keep roles simple and understandable
3. **Missing audit trails** - Log all permission changes and access attempts
4. **Hard-coded permissions** - Use database-driven permission systems
5. **No permission review process** - Regularly audit user permissions

## Security Compliance Checklist

```yaml
Access Control:
- [ ] Principle of least privilege enforced
- [ ] Role separation implemented
- [ ] Administrative access monitored
- [ ] Regular permission reviews scheduled

Audit & Compliance:
- [ ] All access attempts logged
- [ ] Failed access attempts monitored
- [ ] Regular security reports generated
- [ ] Compliance requirements met

Technical Security:
- [ ] Server-side permission validation
- [ ] JWT tokens properly secured
- [ ] Rate limiting by role implemented
- [ ] Privilege escalation prevented
```

## Next Steps

- Explore [User Data Separation](separating-user-data.md) for data isolation
- Learn about [Security Policies](security-policy.md) for advanced protection
- Master [OAuth Integration](oauth-sso.md) for external authentication
- Understand [API Security](../api-endpoints/token-scopes-reference.md)

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - RBAC implementation discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step RBAC setup
- 📖 [Security Documentation](../../security/best-practices.md) - Advanced security patterns
- 🔧 [Support](https://xano.com/support) - Enterprise RBAC assistance