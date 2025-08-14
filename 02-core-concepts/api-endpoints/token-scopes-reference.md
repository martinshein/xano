---
title: "Metadata API Token Scopes Reference - Security Guide"
description: "Complete guide to Xano Metadata API token scopes and permissions - secure your API access for n8n, WeWeb, and Make integrations with proper authorization"
category: api-endpoints
tags:
  - API Security
  - Token Scopes
  - Access Control
  - Permissions
  - Authentication
  - Authorization
difficulty: advanced
reading_time: 10 minutes
last_updated: '2025-01-23'
prerequisites:
  - Understanding of API authentication
  - Knowledge of security principles
  - Metadata API setup experience
---

# Metadata API Token Scopes Reference

## 📋 **Quick Summary**

**What it does:** Token scopes control precisely what permissions a Metadata API access token has across your Xano workspace, enabling secure, granular access control for external integrations.

**Why it matters:** Proper scope configuration:
- Protects your data with least-privilege access
- Prevents security breaches from over-permissioned tokens
- Enables secure third-party integrations
- Ensures compliance with security best practices

**Time to implement:** 5-10 minutes to configure, critical for security

---

## What You'll Learn

- Understanding the principle of least privilege
- Complete scope reference with permissions (CRUD)
- Security best practices for token management
- Common scope configurations for popular tools
- Real-world access control scenarios
- Token lifecycle management strategies

## Understanding Token Scopes

Think of token scopes like giving someone keys to specific rooms in your house - you want to give access only to the areas they need, not the master key to everything.

### 🎯 **Core Security Principles:**
- **Least Privilege**: Grant minimal permissions necessary
- **Scope Isolation**: Separate concerns by limiting access
- **Time-Limited Access**: Rotate tokens regularly
- **Audit Trail**: Monitor token usage and access patterns

## ⚠️ **Critical Security Warning**

**Metadata API tokens grant access to ALL workspaces in your instance.**

This means:
- A single token can access multiple workspaces
- Scope permissions apply across all accessible workspaces
- Extra caution is required for multi-workspace instances
- Consider separate instances for different security contexts

## CRUD Permissions Explained

Each scope supports four permission levels:

| Permission | Symbol | Description | Security Impact |
|------------|--------|-------------|-----------------|
| **Create** | C | Add new data | Can create records, files, schemas |
| **Read** | R | View existing data | Can access sensitive information |
| **Update** | U | Modify existing data | Can alter existing records |
| **Delete** | D | Remove data | Can permanently destroy data |

### 💡 **Permission Strategy**

```yaml
Read-Only Integrations:
- Analytics dashboards: R only
- Monitoring tools: R only
- Reporting systems: R only

Data Entry Systems:
- Forms and surveys: C, R
- Import tools: C, R
- Bulk processors: C, R, U

Admin Interfaces:
- Management dashboards: C, R, U, D
- Data cleanup tools: R, U, D
- Full admin panels: C, R, U, D
```

## Complete Scope Reference

### 1. Workspace Database
**Purpose:** Access to database tables, records, and schema information

**Includes:**
- All table data across data sources
- Schema information and structure
- Database relationships and constraints
- Field definitions and types

**Use Cases:**
```yaml
Read (R):
- Data export tools
- Analytics dashboards
- Reporting systems

Create (C):
- Data import tools
- Form submissions
- API data ingestion

Update (U):
- Data synchronization
- Record updates
- Bulk edit operations

Delete (D):
- Data cleanup scripts
- Admin panels
- Bulk delete operations
```

**⚠️ Security Considerations:**
- Contains all customer/business data
- Most sensitive scope for data privacy
- Consider field-level access controls

### 2. Workspace Content
**Purpose:** Workspace-wide settings and administrative information

**Includes:**
- Data sources configuration
- Branch management
- Basic workspace information
- Import/export functionality
- Workspace metadata

**Use Cases:**
```yaml
Read (R):
- Environment discovery
- Configuration reporting
- Workspace inventory

Create (C):
- Branch creation
- Data source setup
- Workspace initialization

Update (U):
- Configuration changes
- Workspace settings
- Branch management

Delete (D):
- Cleanup operations
- Branch deletion
- Configuration removal
```

**💡 Common Integrations:**
- DevOps tools for environment management
- Backup systems for configuration export
- Development tools for branch operations

### 3. Workspace Live Data Source
**Purpose:** Specific access to production data source

**Includes:**
- Production database access
- Live data operations
- Real-time data queries

**⚠️ Production Safety:**
```yaml
Recommended Permissions:
- Development tools: R only
- Monitoring systems: R only
- Admin dashboards: C, R, U (avoid D)
- Emergency tools: C, R, U, D (restricted access)
```

**Use Cases:**
- Production monitoring
- Live data analysis
- Real-time integrations
- Production incident response

### 4. Workspace API Groups
**Purpose:** Access to API definitions and configurations

**Includes:**
- API endpoint definitions
- API group organization
- Endpoint configurations
- API metadata and documentation

**Use Cases:**
```yaml
Read (R):
- API documentation generation
- Integration discovery
- Development tools
- API gateway configuration

Create (C):
- API generation tools
- Automated endpoint creation
- Integration setup

Update (U):
- API configuration management
- Endpoint maintenance
- Version management

Delete (D):
- API cleanup
- Deprecated endpoint removal
```

### 5. Workspace Functions
**Purpose:** Access to custom function definitions

**Includes:**
- Custom function code
- Function configurations
- Function metadata
- Execution parameters

**🔧 Developer Tools:**
- Code deployment systems
- Function management interfaces
- Development environments
- CI/CD pipelines

### 6. Workspace Addons
**Purpose:** Access to addon configurations and data

**Includes:**
- Third-party addon settings
- Addon data and configurations
- Integration parameters

**Integration Examples:**
- Payment processor settings
- Email service configurations
- Analytics tool connections

### 7. Workspace Tasks
**Purpose:** Access to background task definitions and execution

**Includes:**
- Background task configurations
- Task execution history
- Scheduled task management
- Task results and logs

**Automation Use Cases:**
- Task monitoring systems
- Automated scheduling tools
- Performance tracking
- System maintenance scripts

### 8. Workspace Files
**Purpose:** Access to file storage (public and private)

**Includes:**
- Public file storage
- Private file storage
- File metadata
- Upload/download operations

**⚠️ File Security:**
```yaml
Public Files:
- Generally safer to access
- Consider bandwidth implications
- Monitor for abuse

Private Files:
- Highly sensitive data
- Strict access controls required
- Audit all access attempts
```

### 9. Workspace Request History
**Purpose:** Access to API request logs and analytics

**Includes:**
- Request/response logs
- Performance metrics
- Usage analytics
- Error tracking data

**📊 Analytics Applications:**
- Performance monitoring
- Usage reporting
- Security audit trails
- API analytics dashboards

## Common Integration Configurations

### 🌐 **WeWeb Integration**

**Required Scopes:**
```yaml
Workspace API Groups: [R]
- Purpose: Discover available APIs
- Security: Read-only for safety

Workspace Content: [R]
- Purpose: Access workspace information
- Security: Read-only for configuration discovery
```

**Optional Scopes (based on features):**
```yaml
Workspace Database: [C, R, U, D]
- Purpose: Direct database operations
- Security: Full permissions for admin panels

Workspace Files: [C, R]
- Purpose: File upload/display features
- Security: Avoid delete permissions
```

### 🔗 **n8n Workflow Automation**

**Basic Data Operations:**
```yaml
Workspace Database: [C, R, U]
- Purpose: Data sync, form processing
- Security: No delete for safety

Workspace Content: [R]
- Purpose: Workspace discovery
- Security: Read-only access
```

**Advanced Automation:**
```yaml
Workspace Tasks: [C, R]
- Purpose: Trigger background tasks
- Security: Create and monitor tasks

Workspace Request History: [R]
- Purpose: Monitor workflow performance
- Security: Read-only for analytics
```

### 🔧 **Make (Integromat) Scenarios**

**Data Processing:**
```yaml
Workspace Database: [C, R, U]
- Purpose: Record manipulation
- Security: Standard CRUD without delete

Workspace Files: [C, R]
- Purpose: File processing workflows
- Security: Upload and read files
```

### 📊 **Analytics & Monitoring Tools**

**Read-Only Analytics:**
```yaml
Workspace Database: [R]
Workspace Request History: [R]
Workspace Content: [R]
- Purpose: Data analysis and reporting
- Security: Strictly read-only access
```

### 🛡️ **Admin & Management Tools**

**Full Administrative Access:**
```yaml
All Scopes: [C, R, U, D]
- Purpose: Complete system management
- Security: Highly restricted, admin-only tokens
```

**Maintenance Tools:**
```yaml
Workspace Database: [R, U, D]
Workspace Files: [R, D]
- Purpose: Data cleanup and maintenance
- Security: No create permissions needed
```

## Security Best Practices

### 1. Token Lifecycle Management

```yaml
Token Rotation Schedule:
- Development tokens: Monthly
- Production tokens: Quarterly
- Admin tokens: Bi-annually
- Integration tokens: Per vendor requirements
```

### 2. Environment Separation

```yaml
Development Environment:
- Broader permissions acceptable
- Frequent token rotation
- Logging and monitoring

Staging Environment:
- Production-like restrictions
- Limited token distribution
- Testing security policies

Production Environment:
- Strict least-privilege
- Minimal token count
- Comprehensive audit logging
```

### 3. Access Control Matrix

| Integration Type | Database | Content | Files | API Groups | Tasks | History |
|------------------|----------|---------|-------|------------|-------|---------|
| **Analytics Dashboard** | R | R | - | R | - | R |
| **Data Import Tool** | C, R | R | C, R | R | - | - |
| **Admin Panel** | C, R, U, D | R, U | C, R, U, D | R, U | C, R | R |
| **Monitoring System** | R | R | - | R | R | R |
| **Backup Solution** | R | R | R | R | R | R |

### 4. Token Audit Checklist

```yaml
Regular Reviews:
- [ ] List all active tokens
- [ ] Verify each token's purpose
- [ ] Check last usage dates
- [ ] Review assigned permissions
- [ ] Validate integration needs
- [ ] Remove unused tokens
- [ ] Document token purposes
```

### 5. Security Monitoring

```javascript
// Token usage monitoring pattern
const tokenAudit = {
  trackUsage: (tokenId, endpoint, action) => {
    // Log token usage
    console.log(`Token ${tokenId} accessed ${endpoint} with ${action}`);
  },
  
  detectAnomalies: (tokenId, usagePattern) => {
    // Flag unusual usage patterns
    if (usagePattern.frequencySpike > threshold) {
      alert(`Unusual activity detected for token ${tokenId}`);
    }
  },
  
  enforceRateLimit: (tokenId, requestCount, timeWindow) => {
    // Implement rate limiting per token
    if (requestCount > maxRequestsPerHour) {
      blockToken(tokenId, timeWindow);
    }
  }
};
```

## Emergency Procedures

### Token Compromise Response

```yaml
Immediate Actions:
1. Revoke compromised token immediately
2. Generate new token with minimal required scopes
3. Update integration configurations
4. Review access logs for unauthorized activity
5. Document incident for security review

Investigation Steps:
1. Identify scope of potential data access
2. Check for unauthorized data modifications
3. Review related token usage patterns
4. Assess impact on connected systems
5. Implement additional security measures
```

### Recovery Procedures

```yaml
Service Restoration:
1. Create emergency read-only token
2. Test critical integrations
3. Gradually restore full permissions
4. Monitor for unusual activity
5. Complete security assessment

Documentation Updates:
1. Update token inventory
2. Revise security procedures
3. Train team on new protocols
4. Schedule security review
```

## 💡 **Try This**

### Beginner Exercise
Create tokens for different scenarios:
1. Read-only analytics token
2. Data entry form token
3. File upload service token

### Intermediate Challenge
Design a scope matrix for:
1. Multi-tenant SaaS application
2. Agency managing client workspaces
3. Enterprise with multiple departments

### Advanced Project
Implement automated token management:
1. Token rotation system
2. Usage monitoring dashboard
3. Security compliance reporting

## Common Mistakes to Avoid

1. **Over-permissioning tokens** - Granting excessive permissions "just in case"
2. **Never rotating tokens** - Using the same tokens indefinitely
3. **Ignoring unused tokens** - Leaving old tokens active without purpose
4. **No usage monitoring** - Missing security incidents and abuse
5. **Shared tokens** - Using one token across multiple integrations

## Compliance Considerations

### Data Privacy Regulations

```yaml
GDPR Compliance:
- Document data access purposes
- Implement data minimization
- Enable data deletion capabilities
- Maintain audit trails

CCPA Compliance:
- Track data access requests
- Enable consumer data exports
- Support data deletion requests
- Maintain transparency logs
```

### Industry Standards

```yaml
SOC 2 Compliance:
- Regular access reviews
- Privileged access management
- Security monitoring
- Incident response procedures

ISO 27001:
- Access control policies
- Risk assessment procedures
- Security awareness training
- Management reviews
```

## Next Steps

- Master [Content Management](content.md) with appropriate scopes
- Explore [File Operations](file.md) security considerations
- Learn about [Request History](request-history.md) monitoring
- Understand [Search Operations](search.md) access patterns

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Security discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Token management guides
- 📖 [Security Documentation](../../security/best-practices.md) - Advanced security
- 🔧 [Support](https://xano.com/support) - Security assistance