---
title: "Xano API Token Scopes Guide"
description: "Understand and configure Xano API token scopes for secure access control and integration with third-party platforms like WeWeb, Make.com, and monitoring tools"
category: expressions
has_code_examples: false
last_updated: '2025-01-16'
tags:
  - api-scopes
  - security
  - access-control
  - authentication
  - integrations
---

# Xano API Token Scopes Guide
## 📋 **Quick Summary**

Xano API token scopes provide granular access control for third-party integrations and external tools. Understanding and properly configuring scopes ensures secure integration with platforms like WeWeb, Make.com, n8n, and monitoring tools while following the principle of least privilege.

## What You'll Learn

- Understanding CRUD permissions for each scope
- Complete reference of all available scopes
- Recommended scope configurations for common integrations
- Security best practices for token management
- Examples for WeWeb, monitoring, and automation platforms

## Understanding CRUD Permissions

Each scope in Xano follows the CRUD (Create, Read, Update, Delete) permission model, allowing fine-grained access control:

**C (Create)**: Create new data within the scope
**R (Read)**: Read existing data within the scope  
**U (Update)**: Update existing data within the scope
**D (Delete)**: Delete data within the scope

**Permission Management Tips:**
- Hover over permission checkboxes to see + or - options
- Use bulk selection for efficient configuration
- Follow principle of least privilege
- Regular review and rotation of permissions

## Complete Scope Reference

### Workspace Database
**Description**: Database access including table data and schema across all data sources

**What This Includes:**
- Database table content (records)
- Table schemas and structures
- All connected data sources
- Field definitions and relationships

**Use Cases:**
- Admin dashboards requiring full database access
- Data migration and backup tools
- Analytics and reporting platforms
- Complete database management interfaces

**Security Consideration**: Most powerful scope - grant carefully

### Workspace Content
**Description**: Workspace-wide information including datasources, branches, and import/export

**What This Includes:**
- Datasource configurations
- Branch information and management
- Basic workspace metadata
- Import/export operations
- Workspace cloning and migration

**Use Cases:**
- DevOps and deployment tools
- Workspace management interfaces
- Branch synchronization tools
- Backup and migration systems

### Workspace Live Data Source
**Description**: Specific access to the live (production) data source

**What This Includes:**
- Production data source only
- Live branch database access
- Production-specific configurations

**Use Cases:**
- Production monitoring tools
- Live data analytics
- Production-only integrations
- Customer-facing applications

**Security Priority**: Critical for production access

### Workspace API Groups
**Description**: Access to APIs and API group configurations

**What This Includes:**
- API endpoint definitions
- API group organizations
- Endpoint configurations and settings
- API metadata and documentation

**Use Cases:**
- API documentation tools
- Endpoint monitoring systems
- API management platforms
- Development tools requiring API access

### Workspace Functions
**Description**: Access to custom functions and logic

**What This Includes:**
- Custom function definitions
- Function code and logic
- Function metadata and configurations
- Dependency relationships

**Use Cases:**
- Code deployment tools
- Function monitoring systems
- Development environments
- Logic backup and versioning

### Workspace Addons
**Description**: Access to workspace addons and extensions

**What This Includes:**
- Addon configurations
- Extension settings
- Third-party integrations
- Addon metadata

**Use Cases:**
- Addon management tools
- Integration monitoring
- Extension deployment systems
- Configuration backup tools

### Workspace Tasks
**Description**: Access to background tasks and job management

**What This Includes:**
- Task definitions and configurations
- Job queue management
- Task execution history
- Scheduled task settings

**Use Cases:**
- Task monitoring systems
- Job queue management tools
- Automation platforms
- Performance monitoring

### Workspace Files
**Description**: Access to public and private file storage

**What This Includes:**
- File upload and download
- File metadata and organization
- Storage quota management
- File access permissions

**Use Cases:**
- File management interfaces
- Backup and archival systems
- Content management platforms
- Media processing tools

### Workspace Request History
**Description**: Access to API request logs and history

**What This Includes:**
- API request logs
- Performance metrics
- Error tracking data
- Usage analytics

**Use Cases:**
- Monitoring and alerting systems
- Performance analysis tools
- Debug and troubleshooting
- Usage analytics platforms
## Common Integration Scenarios

### WeWeb Integration

For WeWeb's Xano plugins to function properly:

| Scope | C | R | U | D | Purpose |
|-------|---|---|---|---|----------|
| **Workspace API Groups** | ✗ | ✓ | ✗ | ✗ | Read API group information and available endpoints |
| **Workspace Content** | ✗ | ✓ | ✗ | ✗ | Access workspace metadata and configurations |

**Why These Scopes:**
- WeWeb needs to discover available APIs for data binding
- Workspace content access enables proper configuration
- Read-only access maintains security while enabling functionality

**Configuration Tips:**
- Create dedicated tokens for WeWeb integration
- Rotate tokens regularly for security
- Monitor token usage through request history

### Monitoring and Logging Tools

For comprehensive monitoring and logging systems:

| Scope | C | R | U | D | Purpose |
|-------|---|---|---|---|----------|
| **Workspace API Groups** | ✗ | ✓ | ✗ | ✗ | Monitor specific API endpoints and performance |
| **Workspace Content** | ✗ | ✓ | ✗ | ✗ | General workspace information and metadata |
| **Workspace Request History** | ✗ | ✓ | ✗ | ✗ | Access request logs for analysis and alerting |

**Why These Scopes:**
- API Groups: Monitor endpoint health and availability
- Content: Understand workspace configuration context
- Request History: Access detailed performance and error data

**Advanced Monitoring Setup:**
- Use separate tokens for different monitoring tools
- Implement rate limiting to avoid overwhelming APIs
- Set up automated alerting based on request history patterns

### Make.com and n8n Automation

For automation platforms requiring broader access:

| Scope | C | R | U | D | Purpose |
|-------|---|---|---|---|----------|
| **Workspace Database** | ✓ | ✓ | ✓ | ✓ | Full database operations for automation workflows |
| **Workspace Files** | ✓ | ✓ | ✓ | ✗ | File upload/download for document processing |
| **Workspace Tasks** | ✓ | ✓ | ✓ | ✗ | Trigger and monitor background tasks |

**Security Considerations:**
- Use environment-specific tokens (dev/staging/prod)
- Implement IP restrictions where possible
- Regular audit of automation access patterns

### Admin Dashboard Applications

For comprehensive admin interfaces:

| Scope | C | R | U | D | Purpose |
|-------|---|---|---|---|----------|
| **Workspace Database** | ✓ | ✓ | ✓ | ✓ | Complete data management capabilities |
| **Workspace API Groups** | ✗ | ✓ | ✗ | ✗ | Monitor and display API status |
| **Workspace Files** | ✓ | ✓ | ✓ | ✓ | File management interface |
| **Workspace Request History** | ✗ | ✓ | ✗ | ✗ | Performance monitoring and debugging |

### Analytics and Reporting Tools

For read-only analytics and reporting:

| Scope | C | R | U | D | Purpose |
|-------|---|---|---|---|----------|
| **Workspace Database** | ✗ | ✓ | ✗ | ✗ | Read data for analysis and reporting |
| **Workspace Request History** | ✗ | ✓ | ✗ | ✗ | Usage analytics and performance metrics |
| **Workspace Content** | ✗ | ✓ | ✗ | ✗ | Workspace metadata for context |

## Try This: Scope Configuration Worksheet

Use this worksheet to determine appropriate scopes for your integration:

```markdown
# Scope Configuration Worksheet

## Integration Details
- Platform: ________________
- Use Case: _______________
- Environment: ____________
- Security Level: __________

## Required Operations
- [ ] Read database content
- [ ] Create database records
- [ ] Update database records
- [ ] Delete database records
- [ ] Access file storage
- [ ] Monitor API performance
- [ ] Manage background tasks
- [ ] Access workspace metadata

## Recommended Scopes
Based on requirements above:
- [ ] Workspace Database: __ C __ R __ U __ D
- [ ] Workspace API Groups: __ C __ R __ U __ D
- [ ] Workspace Files: __ C __ R __ U __ D
- [ ] Workspace Request History: __ C __ R __ U __ D
- [ ] Other: _______________

## Security Checklist
- [ ] Minimum required permissions selected
- [ ] Token rotation schedule established
- [ ] IP restrictions configured (if applicable)
- [ ] Monitoring and alerting set up
- [ ] Documentation updated
```

## Security Best Practices

### Token Management

1. **Principle of Least Privilege**: Grant only necessary permissions
2. **Regular Rotation**: Rotate tokens on a schedule (monthly/quarterly)
3. **Environment Separation**: Use different tokens for dev/staging/production
4. **Monitoring**: Track token usage through request history
5. **Documentation**: Maintain clear records of token purposes and scopes

### Access Control Strategies

**Development Environment:**
```markdown
# Development Token Configuration
- Broader permissions for testing
- Shorter rotation cycles
- Enhanced monitoring and logging
- Clear expiration dates
```

**Production Environment:**
```markdown
# Production Token Configuration
- Minimal required permissions only
- Longer rotation cycles for stability
- IP restrictions where possible
- Comprehensive audit logging
```

### Audit and Compliance

1. **Regular Reviews**: Quarterly scope and permission audits
2. **Usage Monitoring**: Track API usage patterns and anomalies
3. **Access Logging**: Maintain detailed logs of token usage
4. **Incident Response**: Procedures for token compromise
5. **Compliance Documentation**: Maintain compliance with security policies

## Common Mistakes to Avoid

1. **Over-Permissioning**: Granting more access than necessary
2. **Token Sharing**: Using same token across multiple integrations
3. **Indefinite Tokens**: Not implementing rotation schedules
4. **Insufficient Monitoring**: Not tracking token usage patterns
5. **Documentation Neglect**: Not maintaining clear scope documentation

## Pro Tips

1. **Start Minimal**: Begin with read-only access and add permissions as needed
2. **Test Thoroughly**: Validate integrations work with minimal scopes
3. **Use Descriptive Names**: Name tokens clearly for their intended purpose
4. **Implement Alerts**: Set up monitoring for unusual token usage
5. **Regular Cleanup**: Remove unused or expired tokens
6. **Team Training**: Ensure team understands scope implications

## Troubleshooting Common Issues

### Access Denied Errors
- **Check Scope Configuration**: Verify required permissions are granted
- **Token Validity**: Ensure token hasn't expired
- **IP Restrictions**: Confirm requests originate from allowed IPs
- **Rate Limiting**: Check if requests are being throttled

### Integration Failures
- **Permission Mismatch**: Compare required vs. granted permissions
- **Token Format**: Verify correct token format and headers
- **Endpoint Access**: Confirm endpoints are accessible with current scopes
- **Network Issues**: Check connectivity and firewall settings

### Performance Issues
- **Over-Scoping**: Too broad permissions may impact performance
- **Rate Limits**: Monitor request frequency and implement backoff
- **Token Overhead**: Multiple tokens may create unnecessary overhead
- **Caching**: Implement appropriate caching strategies

By carefully selecting appropriate scopes for each integration, you can maintain security while enabling powerful third-party functionality. Regular review and optimization of scope configurations ensures your Xano integrations remain secure, efficient, and compliant with your organization's security policies.