---
title: "User Data Separation in Xano - Complete Multi-Tenant Security Guide"
description: "Master data isolation and multi-tenant architecture in Xano with comprehensive patterns, security controls, and privacy compliance for scalable applications"
category: authentication
tags:
  - Data Separation
  - Multi-Tenant
  - Data Isolation
  - Privacy
  - User Data
  - Security
  - Tenant Isolation
  - Data Privacy
difficulty: intermediate
reading_time: 14 minutes
last_updated: '2025-01-23'
prerequisites:
  - Understanding of user authentication
  - Knowledge of database relationships
  - Xano function stack experience
  - Basic security concepts
---

# User Data Separation in Xano

## 📋 **Quick Summary**

**What it does:** User data separation ensures that users can only access data that belongs to them, creating secure multi-tenant environments where data is logically isolated even when stored in shared database tables.

**Why it matters:** Data separation provides:
- **Privacy protection** - Users can't see each other's sensitive information
- **Compliance readiness** - Meet GDPR, HIPAA, and other privacy regulations
- **Multi-tenant architecture** - Support multiple customers on the same platform
- **Security boundaries** - Prevent data leakage and unauthorized access
- **Scalable architecture** - Build SaaS applications with proper tenant isolation

**Time to implement:** 30-60 minutes for basic separation, 2-4 hours for comprehensive multi-tenant setup

---

## What You'll Learn

- Understanding data separation vs access control concepts
- Database schema design for secure multi-tenancy
- Implementation patterns for user data isolation
- Advanced security techniques and preconditions
- Multi-level tenant separation strategies
- Privacy compliance and data protection methods

## Understanding Data Separation Concepts

Think of data separation like apartment buildings - even though multiple tenants live in the same building, each has their own private unit with locked doors. Similarly, users share database tables, but proper separation ensures they only see their own data.

### 🎯 **Data Separation vs Access Control**

| Aspect | Data Separation | Access Control (RBAC) |
|--------|-----------------|----------------------|
| **Purpose** | Isolate user data | Control what actions users can perform |
| **Scope** | Horizontal data filtering | Vertical permission management |
| **Security Model** | Tenant-based isolation | Role-based permissions |
| **Compliance Focus** | Data privacy (GDPR, HIPAA) | Operational security (SOX, SOC2) |
| **Example** | User A sees only their orders | Manager can approve, Staff can view |

### 🔐 **Multi-Tenancy Models**

**Single-Tenant (Dedicated):**
- Each customer has separate database/instance
- Maximum isolation but higher costs
- Best for: Enterprise clients with strict requirements

**Multi-Tenant Shared Database:**
- All customers share tables with tenant ID filtering
- Cost-efficient but requires careful implementation
- Best for: SaaS applications with many smaller clients

**Multi-Tenant Shared Schema:**
- Separate schemas per tenant in same database
- Balance between isolation and efficiency
- Best for: Medium-scale B2B applications

## Database Schema Design for Data Separation

### Basic User Data Separation

```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- User-owned data with foreign key relationship
CREATE TABLE user_items (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) NOT NULL,
  title VARCHAR(255) NOT NULL,
  content TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  
  -- Index for efficient filtering
  INDEX idx_user_items_user_id (user_id)
);

-- Sample data showing separation
INSERT INTO users (id, email, name) VALUES 
(1, 'alice@example.com', 'Alice'),
(2, 'bob@example.com', 'Bob'),
(3, 'carol@example.com', 'Carol');

INSERT INTO user_items (user_id, title, content) VALUES 
(1, 'Alice Item 1', 'Private content for Alice'),
(1, 'Alice Item 2', 'Another Alice item'),
(2, 'Bob Item 1', 'Bob private content'),
(3, 'Carol Item 1', 'Carol private data');
```

### Multi-Level Tenant Architecture

```sql
-- Organizations (top-level tenants)
CREATE TABLE organizations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  subdomain VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Teams within organizations
CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  organization_id INTEGER REFERENCES organizations(id) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  
  INDEX idx_teams_org_id (organization_id)
);

-- Users belong to teams and organizations
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  organization_id INTEGER REFERENCES organizations(id) NOT NULL,
  team_id INTEGER REFERENCES teams(id),
  name VARCHAR(255) NOT NULL,
  
  INDEX idx_users_org_id (organization_id),
  INDEX idx_users_team_id (team_id)
);

-- Multi-level data separation
CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  organization_id INTEGER REFERENCES organizations(id) NOT NULL,
  team_id INTEGER REFERENCES teams(id),
  owner_id INTEGER REFERENCES users(id) NOT NULL,
  title VARCHAR(255) NOT NULL,
  
  -- Multiple indexes for different access patterns
  INDEX idx_projects_org_id (organization_id),
  INDEX idx_projects_team_id (team_id),
  INDEX idx_projects_owner_id (owner_id)
);
```

### Privacy-First Schema Design

```sql
-- User profiles with privacy controls
CREATE TABLE user_profiles (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) NOT NULL,
  visibility VARCHAR(20) DEFAULT 'private', -- private, team, public
  profile_data JSONB,
  
  INDEX idx_user_profiles_user_id (user_id),
  INDEX idx_user_profiles_visibility (visibility)
);

-- Audit log for data access
CREATE TABLE data_access_log (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) NOT NULL,
  accessed_user_id INTEGER REFERENCES users(id),
  resource_type VARCHAR(100) NOT NULL,
  resource_id INTEGER NOT NULL,
  action VARCHAR(50) NOT NULL,
  timestamp TIMESTAMP DEFAULT NOW(),
  
  INDEX idx_access_log_user_id (user_id),
  INDEX idx_access_log_timestamp (timestamp)
);
```

## Implementation Patterns in Xano

### Pattern 1: Basic User Data Filtering

**Scenario:** Users can only see their own items

```javascript
// Xano Function Stack Implementation
// 1. Require Authentication on the endpoint
// 2. Query All Records with user filtering

// In Query All Records function:
// Custom Query Expression:
WHERE items.user_id = auth.user.id

// This ensures only items belonging to the authenticated user are returned
```

**Complete Function Stack:**
1. **Authentication Required** ✓
2. **Query All Records** from `user_items` table
   - Filter: `user_id = auth.user.id`
   - This automatically filters results to current user only

### Pattern 2: Enhanced Security with Preconditions

**Scenario:** Additional validation before data operations

```javascript
// Enhanced security pattern for data operations
// Function Stack for "Get User Items":

// 1. Get Record (user validation)
const userRecord = await getRecord({
  table: 'users',
  id: auth.user.id
});

// 2. Precondition (security check)
// Expression: auth.user.id == userRecord.id
if (auth.user.id !== userRecord.id) {
  throw new Error('User validation failed', 403);
}

// 3. Query All Records (filtered data)
// Expression: user_id = auth.user.id
const userItems = await queryAllRecords({
  table: 'user_items',
  filter: { user_id: auth.user.id }
});

return userItems;
```

### Pattern 3: Multi-Level Tenant Filtering

**Scenario:** Organization → Team → User hierarchy

```javascript
// Multi-level tenant separation
class MultiTenantDataAccess {
  static async getUserAccessibleProjects(userId) {
    // 1. Get user's organizational context
    const user = await getRecord({
      table: 'users',
      id: userId,
      include: ['organization', 'team']
    });
    
    // 2. Build hierarchical filters
    const filters = {
      organization_id: user.organization_id
    };
    
    // 3. Apply team-level filtering if user has team
    if (user.team_id) {
      filters.team_id = user.team_id;
    }
    
    // 4. Get projects with proper filtering
    return await queryRecords({
      table: 'projects',
      filters: filters,
      sort: { created_at: 'desc' }
    });
  }
  
  static async validateUserProjectAccess(userId, projectId) {
    // Get user's organizational context
    const user = await getRecord({
      table: 'users', 
      id: userId,
      include: ['organization']
    });
    
    // Get project with organizational data
    const project = await getRecord({
      table: 'projects',
      id: projectId
    });
    
    // Validate organizational access
    if (project.organization_id !== user.organization_id) {
      throw new Error('Cross-organization access denied', 403);
    }
    
    // Validate team access if applicable
    if (project.team_id && project.team_id !== user.team_id) {
      throw new Error('Team access denied', 403);
    }
    
    return true;
  }
}
```

### Pattern 4: Dynamic Privacy Controls

**Scenario:** User-controlled visibility settings

```javascript
// Privacy-aware data access
class PrivacyAwareAccess {
  static async getVisibleProfiles(viewerId) {
    // Get viewer's context
    const viewer = await getRecord({
      table: 'users',
      id: viewerId,
      include: ['organization', 'team']
    });
    
    // Build visibility query based on privacy settings
    const visibilityQuery = [
      // Public profiles
      { visibility: 'public' },
      
      // Team profiles (if viewer has team)
      ...(viewer.team_id ? [
        {
          visibility: 'team',
          'user.team_id': viewer.team_id
        }
      ] : []),
      
      // Organization profiles
      {
        visibility: 'organization',
        'user.organization_id': viewer.organization_id
      },
      
      // User's own profile
      {
        user_id: viewerId
      }
    ];
    
    return await searchRecords({
      table: 'user_profiles',
      search: visibilityQuery,
      operator: 'OR'
    });
  }
  
  static async logDataAccess(userId, accessedResource, action) {
    return await addRecord({
      table: 'data_access_log',
      data: {
        user_id: userId,
        accessed_user_id: accessedResource.user_id,
        resource_type: accessedResource.type,
        resource_id: accessedResource.id,
        action: action,
        timestamp: new Date().toISOString()
      }
    });
  }
}
```

## Advanced Security Techniques

### 1. Row-Level Security with Custom Functions

```javascript
// Create reusable security functions
async function validateDataOwnership(userId, tableName, recordId, ownerField = 'user_id') {
  const record = await getRecord({
    table: tableName,
    id: recordId
  });
  
  if (!record) {
    throw new Error('Record not found', 404);
  }
  
  if (record[ownerField] !== userId) {
    throw new Error('Access denied: Not the owner', 403);
  }
  
  return record;
}

// Usage in function stacks
const validateOwnership = await validateDataOwnership(
  auth.user.id,
  'user_items',
  input.itemId
);
```

### 2. Secure Data Editing Patterns

```javascript
// Secure edit operation with ownership validation
class SecureDataEditor {
  static async editUserItem(userId, itemId, updates) {
    // 1. Get and validate ownership
    const item = await getRecord({
      table: 'user_items',
      id: itemId
    });
    
    // 2. Ownership precondition
    if (item.user_id !== userId) {
      throw new Error('Cannot edit items owned by other users', 403);
    }
    
    // 3. Validate update permissions
    const allowedFields = ['title', 'content', 'status'];
    const sanitizedUpdates = {};
    
    for (const [key, value] of Object.entries(updates)) {
      if (allowedFields.includes(key)) {
        sanitizedUpdates[key] = value;
      }
    }
    
    // 4. Perform update with additional security
    sanitizedUpdates.updated_at = new Date().toISOString();
    sanitizedUpdates.updated_by = userId;
    
    return await editRecord({
      table: 'user_items',
      id: itemId,
      fields: sanitizedUpdates
    });
  }
}
```

### 3. Bulk Operations with Security

```javascript
// Secure bulk operations
class SecureBulkOperations {
  static async bulkDeleteUserItems(userId, itemIds) {
    // 1. Validate all items belong to user
    const items = await queryRecords({
      table: 'user_items',
      filters: {
        id: { in: itemIds },
        user_id: userId
      }
    });
    
    // 2. Security check - ensure all requested items are owned by user
    if (items.length !== itemIds.length) {
      throw new Error('Some items not found or access denied', 403);
    }
    
    // 3. Perform bulk deletion
    const deleteResults = [];
    for (const item of items) {
      const result = await deleteRecord({
        table: 'user_items',
        id: item.id
      });
      deleteResults.push(result);
    }
    
    return {
      deletedCount: deleteResults.length,
      deletedIds: items.map(item => item.id)
    };
  }
  
  static async bulkUpdateItemStatus(userId, itemIds, newStatus) {
    // Validate ownership first
    const ownedItems = await queryRecords({
      table: 'user_items',
      filters: {
        id: { in: itemIds },
        user_id: userId
      }
    });
    
    // Update only owned items
    const updatePromises = ownedItems.map(item =>
      editRecord({
        table: 'user_items',
        id: item.id,
        fields: {
          status: newStatus,
          updated_at: new Date().toISOString()
        }
      })
    );
    
    return await Promise.all(updatePromises);
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n User Data Separation**

```yaml
Data Separation Workflow:
1. HTTP Request (Incoming user request)
2. Function Node (Extract user ID from auth token)
3. HTTP Request (Call Xano with user filtering)
4. Function Node (Additional data filtering)
5. HTTP Response (Return user-specific data)
```

**n8n User Context Function:**
```javascript
// Extract user context for data filtering
const authToken = $input.headers.authorization;
if (!authToken) {
  return { error: 'Authentication required' };
}

// Decode JWT to get user info
const decoded = jwt.decode(authToken.replace('Bearer ', ''));
const userId = decoded.user_id;
const organizationId = decoded.extras?.organization_id;

// Apply user context to data queries
return {
  userId: userId,
  organizationId: organizationId,
  filters: {
    user_id: userId,
    organization_id: organizationId
  },
  userContext: decoded
};
```

### 🌐 **WeWeb Data Separation**

```javascript
// WeWeb user data filtering
class WeWebDataSeparation {
  constructor() {
    this.currentUser = wwLib.auth.getUser();
    this.userFilters = this.buildUserFilters();
  }
  
  buildUserFilters() {
    return {
      user_id: this.currentUser.id,
      organization_id: this.currentUser.organization_id,
      team_id: this.currentUser.team_id
    };
  }
  
  // Automatically filter all data requests
  async loadUserData(endpoint, additionalFilters = {}) {
    const filters = {
      ...this.userFilters,
      ...additionalFilters
    };
    
    const response = await wwLib.api.post({
      url: `${wwLib.envVars.XANO_API}/${endpoint}`,
      data: { filters },
      headers: {
        'Authorization': 'Bearer ' + wwLib.auth.getAuthToken()
      }
    });
    
    // Additional client-side filtering for extra security
    return this.clientSideFilter(response.data);
  }
  
  clientSideFilter(data) {
    // Double-check data belongs to current user
    if (Array.isArray(data)) {
      return data.filter(item => 
        item.user_id === this.currentUser.id ||
        item.organization_id === this.currentUser.organization_id
      );
    }
    
    return data;
  }
  
  // Secure data operations
  async saveUserData(endpoint, data) {
    // Automatically add user context
    const secureData = {
      ...data,
      user_id: this.currentUser.id,
      organization_id: this.currentUser.organization_id,
      created_by: this.currentUser.id
    };
    
    return await wwLib.api.post({
      url: `${wwLib.envVars.XANO_API}/${endpoint}`,
      data: secureData,
      headers: {
        'Authorization': 'Bearer ' + wwLib.auth.getAuthToken()
      }
    });
  }
}

// Usage in WeWeb
const dataManager = new WeWebDataSeparation();

// Load user-specific projects
async function loadMyProjects() {
  const projects = await dataManager.loadUserData('projects', {
    status: 'active'
  });
  
  wwLib.collections.userProjects.update(projects);
  return projects;
}
```

### 🔧 **Make Multi-Tenant Operations**

```yaml
Multi-Tenant Scenario:
1. Webhook (User action with tenant context)
2. JSON Parser (Extract user and tenant information)
3. HTTP Request (Query data with tenant filtering)
4. Iterator (Process each tenant-specific record)
5. Router (Different actions based on tenant rules)
6. HTTP Response (Return filtered results)
```

## Privacy Compliance Patterns

### GDPR Compliance Implementation

```javascript
// GDPR-compliant data operations
class GDPRCompliantDataManager {
  async exportUserData(userId) {
    // Collect all user data across tables
    const userData = {
      user_profile: await this.getUserProfile(userId),
      user_items: await this.getUserItems(userId),
      user_activities: await this.getUserActivities(userId),
      user_preferences: await this.getUserPreferences(userId)
    };
    
    // Log data export request
    await this.logDataOperation(userId, 'data_export', 'GDPR request');
    
    return {
      user_id: userId,
      export_date: new Date().toISOString(),
      data: userData,
      format: 'JSON'
    };
  }
  
  async deleteUserData(userId, retainLegal = true) {
    const deletionLog = [];
    
    try {
      // Delete user-owned data
      const itemsDeleted = await this.deleteUserItems(userId);
      deletionLog.push(`Deleted ${itemsDeleted} user items`);
      
      // Anonymize rather than delete for legal requirements
      if (retainLegal) {
        await this.anonymizeUserProfile(userId);
        deletionLog.push('User profile anonymized');
      } else {
        await this.deleteUserProfile(userId);
        deletionLog.push('User profile deleted');
      }
      
      // Log deletion
      await this.logDataOperation(userId, 'data_deletion', 'GDPR request');
      
      return {
        success: true,
        operations: deletionLog,
        timestamp: new Date().toISOString()
      };
      
    } catch (error) {
      await this.logDataOperation(userId, 'data_deletion_failed', error.message);
      throw error;
    }
  }
  
  async anonymizeUserProfile(userId) {
    return await editRecord({
      table: 'users',
      id: userId,
      fields: {
        email: `deleted_user_${userId}@privacy.deleted`,
        name: 'Deleted User',
        profile_data: null,
        gdpr_deleted: true,
        deleted_at: new Date().toISOString()
      }
    });
  }
}
```

### HIPAA-Compliant Data Handling

```javascript
// HIPAA-compliant medical data separation
class HIPAADataManager {
  async getPatientData(userId, requestingUserId, accessReason) {
    // Validate access permissions
    await this.validateHIPAAAccess(userId, requestingUserId, accessReason);
    
    // Log access attempt
    await this.logHIPAAAccess(userId, requestingUserId, accessReason);
    
    // Return limited data based on need-to-know
    const patientData = await this.getFilteredPatientData(userId, requestingUserId);
    
    return {
      patient_id: userId,
      accessed_by: requestingUserId,
      access_time: new Date().toISOString(),
      data: patientData
    };
  }
  
  async validateHIPAAAccess(patientId, requesterId, reason) {
    const requester = await getRecord({
      table: 'healthcare_providers',
      id: requesterId,
      include: ['role', 'organization']
    });
    
    const patient = await getRecord({
      table: 'patients',
      id: patientId
    });
    
    // Check if requester is in same organization
    if (requester.organization_id !== patient.organization_id) {
      throw new Error('Cross-organization access denied', 403);
    }
    
    // Check role-based access
    const allowedRoles = ['doctor', 'nurse', 'admin'];
    if (!allowedRoles.includes(requester.role.name)) {
      throw new Error('Insufficient privileges for patient data access', 403);
    }
    
    // Require valid reason
    const validReasons = ['treatment', 'consultation', 'emergency', 'administrative'];
    if (!validReasons.includes(reason)) {
      throw new Error('Invalid access reason provided', 400);
    }
    
    return true;
  }
}
```

## Testing Data Separation

### Automated Security Tests

```javascript
// Test suite for data separation
class DataSeparationTests {
  async testUserDataIsolation() {
    const testResults = [];
    
    // Test 1: User can only see own data
    const user1Items = await this.queryUserItems(1);
    const user2Items = await this.queryUserItems(2);
    
    testResults.push({
      test: 'user_data_isolation',
      passed: !this.hasOverlap(user1Items, user2Items),
      description: 'Users should not see each other\'s data'
    });
    
    // Test 2: Cross-user access attempt fails
    try {
      await this.attemptCrossUserAccess(1, 2);
      testResults.push({
        test: 'cross_user_access_prevention',
        passed: false,
        description: 'Cross-user access should be blocked'
      });
    } catch (error) {
      testResults.push({
        test: 'cross_user_access_prevention',
        passed: error.status === 403,
        description: 'Cross-user access properly blocked'
      });
    }
    
    // Test 3: Bulk operations security
    const bulkTestResult = await this.testBulkOperationSecurity();
    testResults.push(bulkTestResult);
    
    return {
      total_tests: testResults.length,
      passed: testResults.filter(t => t.passed).length,
      failed: testResults.filter(t => !t.passed).length,
      results: testResults
    };
  }
  
  async testBulkOperationSecurity() {
    try {
      // Attempt to delete items from multiple users
      const mixedItemIds = [1, 2, 3, 4, 5]; // Items from different users
      await this.bulkDeleteItems(1, mixedItemIds); // User 1 tries to delete all
      
      return {
        test: 'bulk_operation_security',
        passed: false,
        description: 'Bulk operations should only affect owned data'
      };
    } catch (error) {
      return {
        test: 'bulk_operation_security',
        passed: error.message.includes('access denied'),
        description: 'Bulk operations properly secured'
      };
    }
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Implement basic user data separation:
1. Create a user-owned data table (e.g., user_notes)
2. Build an API endpoint with user authentication
3. Add filtering to show only current user's data
4. Test with different user accounts

### Intermediate Challenge
Build multi-level tenant separation:
1. Design organization → team → user hierarchy
2. Implement data filtering at multiple levels
3. Create privacy controls for data visibility
4. Add audit logging for data access

### Advanced Challenge
Create comprehensive privacy system:
1. Implement GDPR-compliant data export/deletion
2. Build role-based data access controls
3. Create automated security testing
4. Design privacy-first multi-tenant architecture

## Common Implementation Mistakes

1. **Forgetting server-side filtering** - Never rely only on client-side data filtering
2. **Missing ownership validation** - Always verify data ownership before operations
3. **Inadequate bulk operation security** - Bulk operations need careful ownership checks
4. **No audit logging** - Track data access for compliance and security
5. **Weak preconditions** - Use robust validation in function stacks

## Data Separation Checklist

```yaml
Authentication & Authorization:
- [ ] User authentication required on all data endpoints
- [ ] Ownership validation in function stacks
- [ ] Proper error handling for access denied scenarios

Database Design:
- [ ] Foreign key relationships properly established
- [ ] Database indexes on filtering columns
- [ ] Audit tables for data access logging

Security Implementation:
- [ ] Server-side data filtering implemented
- [ ] Preconditions for additional security layers
- [ ] Bulk operations properly secured
- [ ] Cross-user access attempts blocked

Compliance & Privacy:
- [ ] Data export functionality for GDPR
- [ ] Data deletion/anonymization procedures
- [ ] Access logging for audit trails
- [ ] Privacy controls for data visibility
```

## Next Steps

- Implement [Role-Based Access Control](restricting-access-rbac.md) for authorization
- Configure [Security Policies](security-policy.md) for enterprise controls
- Set up [OAuth Authentication](oauth-sso.md) for secure user management
- Review [API Security](../api-endpoints/token-scopes-reference.md) best practices

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Data separation discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step implementation guides
- 📖 [Security Documentation](../../security/best-practices.md) - Advanced security patterns
- 🔧 [Support](https://xano.com/support) - Multi-tenant architecture assistance