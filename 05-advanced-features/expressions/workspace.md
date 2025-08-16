---
title: "Xano Audit Logs: Complete Activity Tracking"
description: "Learn how to use Xano's audit logs for comprehensive workspace activity monitoring, compliance, and troubleshooting across all development operations"
category: expressions
has_code_examples: true
last_updated: '2025-01-16'
tags:
  - audit-logs
  - monitoring
  - compliance
  - workspace-activity
  - troubleshooting
---

# Xano Audit Logs: Complete Activity Tracking

## 📋 **Quick Summary**

Xano Audit Logs provide comprehensive tracking and searchable logging of all workspace changes and activities. Essential for compliance, debugging, and team collaboration, audit logs capture everything from database modifications to API deployments with detailed timestamps and user attribution.

## What You'll Learn

- Complete overview of audit log capabilities and coverage
- How to access and navigate audit logs interface
- Advanced searching and filtering techniques
- Export options for compliance and analysis
- API access for automated monitoring
- Retention policies and data management
- Integration patterns for compliance workflows

## Understanding Audit Logs

Audit logs provide a complete record of workspace activity with detailed tracking of:

**User Actions**: Who performed each action with full user attribution
**Timestamps**: Precise timing of all changes and operations
**Change Details**: Comprehensive before/after state information
**Context Information**: Branch, environment, and dependency information
**System Events**: Automated processes and system-triggered changes

**Key Benefits:**
- **Compliance**: Meet regulatory requirements for change tracking
- **Debugging**: Trace issues back to specific changes
- **Team Coordination**: Understand team member activities
- **Security**: Monitor for unauthorized or suspicious activities
- **Performance**: Identify performance-impacting changes

## What's Included in Audit Logs

### Workspace Management
- **Create Workspace**: New workspace creation
- **Update Workspace**: Workspace setting modifications
- **Reset Workspace**: Workspace reset operations
- **Read Workspace**: Workspace access and viewing
- **Delete Workspace**: Workspace removal operations

### Data Source Operations
- **Create Data Source**: New data connection setup
- **Update Data Source**: Data source configuration changes
- **Delete Data Source**: Data source removal

### Branch Management
- **Create Branch**: Development branch creation
- **Update Branch**: Branch configuration changes
- **Delete Branch**: Branch removal
- **Merge Branch**: Branch merge operations
- **Set Live Branch**: Production branch designation

### Environment Variables
- **Read/Create/Update/Delete Environment Variable**: Standard variable management
- **Read/Create/Update/Delete Tenant Environment Variable**: Tenant-specific variables

### Tenant Management
- **Create/Update/Delete Tenant**: Tenant lifecycle management
- **Read/Update Tenant License**: Licensing operations
- **Impersonate Tenant**: Administrative access operations

### Backup and Restore
- **Create Tenant Backup**: Backup generation
- **Restore Tenant Backup**: Restore operations

### Release Management
- **Create/Update Release**: Release lifecycle tracking

### Database Operations
- **Create/Update/Delete/Restore Table**: Table lifecycle management
- **Truncate Table**: Data clearing operations

### API Management
- **Create/Update/Delete/Restore API Group**: API group lifecycle
- **Create/Update/Delete/Restore Query**: Individual API operations
- **Run Query**: API execution tracking

### Function Operations
- **Create/Update/Delete/Restore Function**: Custom function management

### Add-on Management
- **Create/Update/Delete/Restore Add-on**: Add-on lifecycle
- **Run Add-on**: Add-on execution tracking

### Task Operations
- **Create/Update/Delete/Restore Task**: Background task management
- **Run Task**: Task execution tracking

## Accessing Audit Logs

### From Workspace Dashboard

1. **Open Workspace Menu**
   - Navigate to your target workspace
   - Click the three dots (⋮) in the top-right corner

2. **Select Audit Logs**
   - Choose "Audit Logs" from the dropdown menu
   - Access the comprehensive logging interface

### From Instance Settings

For instance-wide audit logs across all workspaces:

1. **Go to Instance Selection**
   - Navigate to your instance selection screen
   - Access settings from the main instance panel

2. **Instance-Level Logging**
   - View consolidated logs across all workspaces
   - Useful for administrators managing multiple workspaces

### Permission Requirements

**RBAC Consideration**: Users need **Workspace Logs** permission when RBAC is enabled
- Configure permissions through workspace settings
- Ensure team members have appropriate access levels
- Consider read-only access for most team members

## Advanced Search and Filtering

### Search Functionality

**Current Limitation**: Search functionality targets event summary titles only
- Search terms match against event descriptions
- Use specific keywords related to actions (create, update, delete)
- Include resource names for more targeted results

**Search Examples:**
```markdown
# Effective Search Terms
- "Create Table users"
- "Update API login"
- "Delete Function validate"
- "Merge Branch feature"
- "Set Live Branch"
```

### Filtering Options

**Event Types**: Filter by specific operation categories
- Database operations
- API changes
- Function modifications
- Branch operations
- User management

**Users**: Filter by team member who performed actions
- Individual user tracking
- Team activity analysis
- Accountability and attribution

**Labels**: Use category-based filtering
- System events vs. user actions
- Production vs. development changes
- Automated vs. manual operations

**Time Ranges**: Focus on specific periods
- Recent changes for debugging
- Historical analysis for compliance
- Incident investigation timeframes

## Try This: Debugging Workflow

Use audit logs to trace a production issue:

```markdown
# Debugging with Audit Logs

## Step 1: Identify Issue Timeline
1. Note when issue was first reported
2. Search logs for events around that time
3. Filter by production branch activities

## Step 2: Trace Recent Changes
1. Filter by event types: API, Function, Database
2. Look for changes in the hours before issue
3. Identify potential culprit modifications

## Step 3: Analyze Change Details
1. Click on suspicious events for details
2. Review before/after state information
3. Use "Go To" buttons to examine current state

## Step 4: Correlate with Performance
1. Cross-reference with monitoring data
2. Check request history for performance impact
3. Identify specific changes causing issues

## Step 5: Plan Resolution
1. Document findings from audit trail
2. Plan rollback or fix strategy
3. Communicate timeline to stakeholders
```

## Audit Log Retention Policies

Retention varies by plan level to balance storage costs with compliance needs:

### Free and Build Plans
**Retention**: 24 hours
- Basic change tracking for immediate debugging
- Suitable for development and learning environments
- Upgrade recommended for production use

### Launch, Starter, Starter+ Plans
**Retention**: 7 days
- Short-term change tracking and debugging
- Basic compliance requirements
- Good for small team environments

### Scale, Pro, Pro+ Plans
**Retention**: 28 days
- Extended debugging and analysis capabilities
- Monthly compliance reporting
- Suitable for production environments

### Enterprise and Custom Plans
**Retention**: Unlimited
- Complete historical record maintenance
- Full compliance and regulatory requirements
- Enterprise-grade audit capabilities

## Exporting Audit Logs

### CSV Export

For spreadsheet analysis and reporting:

1. **Access Export Options**
   - Click three dots (⋮) in top-right of audit log interface
   - Choose "Export CSV" option

2. **Export Scope**
   - Exports current batch of filtered logs
   - Apply filters before export for targeted data
   - Include time range selections for specific periods

3. **Use Cases**
   - Compliance reporting to stakeholders
   - Detailed analysis in spreadsheet applications
   - Integration with business intelligence tools
   - Historical record keeping

### Metadata API Access

For automated monitoring and integration:

#### Browse All Audit Logs

```http
GET /api:meta/audit_log
```

**Query Parameters:**
- `page`: Page number for pagination
- `per_page`: Items per page (default: 50)
- `include_data`: Include detailed change data

**Example Request:**
```javascript
const response = await fetch('/api:meta/audit_log?page=1&per_page=100&include_data=true', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN',
    'Accept': 'application/json'
  }
});

const auditData = await response.json();
```

#### Advanced Search API

```http
POST /api:meta/audit_log/search
```

**Request Body:**
```javascript
{
  "page": 1,
  "per_page": 50,
  "include_data": true,
  "sort": {
    "field": "created_at",
    "direction": "desc"
  },
  "search": [
    {
      "field": "type",
      "operator": "=",
      "value": "Create Table"
    },
    {
      "field": "created_at",
      "operator": ">",
      "value": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### Response Structure

```javascript
{
  "items": [
    {
      "id": 1,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z",
      "type": "Create Table",
      "msg": "Table 'users' created in workspace 'Production'",
      "label": ["database", "table", "creation"],
      "data": {
        /* Detailed change information */
        "table_name": "users",
        "fields": [/* field definitions */],
        "relationships": [/* relationship info */]
      },
      "obj": {
        /* Related object information */
        "table_id": "123",
        "workspace_id": "456"
      },
      "user": {
        /* User who performed action */
        "id": "789",
        "name": "John Developer",
        "email": "john@company.com"
      },
      "workspace": {
        /* Workspace context */
        "id": "456",
        "name": "Production Environment"
      },
      "branch": {
        /* Branch information */
        "id": "branch-123",
        "name": "main",
        "is_live": true
      }
    }
  ],
  "itemsReceived": 1,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "perPage": 50,
  "itemsTotal": 1,
  "pageTotal": 1
}
```

## Integration Patterns

### Compliance Monitoring

Build automated compliance workflows:

```javascript
// Daily compliance report generator
async function generateComplianceReport(startDate, endDate) {
  const searchParams = {
    "page": 1,
    "per_page": 1000,
    "include_data": true,
    "search": [
      {
        "field": "created_at",
        "operator": ">=",
        "value": startDate
      },
      {
        "field": "created_at",
        "operator": "<=",
        "value": endDate
      }
    ]
  };
  
  const response = await fetch('/api:meta/audit_log/search', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + complianceToken,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(searchParams)
  });
  
  const data = await response.json();
  
  // Process for compliance reporting
  const report = {
    period: { start: startDate, end: endDate },
    totalEvents: data.itemsTotal,
    eventsByType: {},
    userActivity: {},
    criticalChanges: []
  };
  
  data.items.forEach(event => {
    // Categorize events
    report.eventsByType[event.type] = (report.eventsByType[event.type] || 0) + 1;
    
    // Track user activity
    const userName = event.user.name;
    report.userActivity[userName] = (report.userActivity[userName] || 0) + 1;
    
    // Flag critical changes
    if (event.type.includes('Delete') || event.type.includes('Live Branch')) {
      report.criticalChanges.push({
        type: event.type,
        user: userName,
        time: event.created_at,
        description: event.msg
      });
    }
  });
  
  return report;
}
```

### Security Monitoring

Implement security alerting:

```javascript
// Security monitoring for unusual activity
async function monitorSecurityEvents() {
  const securityEvents = [
    'Delete Workspace',
    'Delete Table', 
    'Impersonate Tenant',
    'Update Tenant License',
    'Set Live Branch'
  ];
  
  const searches = securityEvents.map(eventType => ({
    "field": "type",
    "operator": "=",
    "value": eventType
  }));
  
  const response = await fetch('/api:meta/audit_log/search', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + securityToken,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "page": 1,
      "per_page": 100,
      "search": [
        {
          "field": "created_at",
          "operator": ">",
          "value": new Date(Date.now() - 24*60*60*1000).toISOString() // Last 24 hours
        }
      ]
    })
  });
  
  const data = await response.json();
  const securityAlerts = data.items.filter(event => 
    securityEvents.includes(event.type)
  );
  
  if (securityAlerts.length > 0) {
    // Send alerts to security team
    await sendSecurityAlert(securityAlerts);
  }
  
  return securityAlerts;
}
```

### Team Activity Dashboard

Create team activity monitoring:

```javascript
// Team activity dashboard data
async function getTeamActivity(timeRange = '7d') {
  const startDate = new Date();
  startDate.setDate(startDate.getDate() - parseInt(timeRange));
  
  const response = await fetch('/api:meta/audit_log/search', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + dashboardToken,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "page": 1,
      "per_page": 1000,
      "search": [
        {
          "field": "created_at",
          "operator": ">",
          "value": startDate.toISOString()
        }
      ]
    })
  });
  
  const data = await response.json();
  
  // Aggregate team activity
  const teamMetrics = {
    totalActivity: data.itemsTotal,
    activeUsers: new Set(),
    activityByDay: {},
    topActions: {},
    recentActivity: data.items.slice(0, 10)
  };
  
  data.items.forEach(event => {
    teamMetrics.activeUsers.add(event.user.name);
    
    const day = event.created_at.split('T')[0];
    teamMetrics.activityByDay[day] = (teamMetrics.activityByDay[day] || 0) + 1;
    
    teamMetrics.topActions[event.type] = (teamMetrics.topActions[event.type] || 0) + 1;
  });
  
  teamMetrics.activeUsers = teamMetrics.activeUsers.size;
  
  return teamMetrics;
}
```

## Best Practices

### Monitoring and Alerting

1. **Regular Review**: Establish periodic audit log review schedules
2. **Automated Monitoring**: Set up automated alerts for critical changes
3. **Compliance Reporting**: Generate regular compliance reports
4. **Performance Correlation**: Cross-reference logs with performance metrics
5. **Security Monitoring**: Monitor for suspicious or unauthorized activities

### Data Management

1. **Export Strategy**: Regular exports for long-term retention
2. **Storage Planning**: Consider storage costs for high-activity workspaces
3. **Access Control**: Limit audit log access to appropriate team members
4. **Retention Awareness**: Understand retention limits for your plan
5. **Backup Integration**: Include audit logs in disaster recovery planning

### Team Collaboration

1. **Change Communication**: Use audit logs to communicate team changes
2. **Training**: Train team members on audit log interpretation
3. **Documentation**: Document critical changes with audit log references
4. **Incident Response**: Establish audit log procedures for incident response
5. **Accountability**: Use logs to maintain development accountability

## Common Use Cases

### Compliance Reporting

Generate monthly compliance reports showing all workspace changes, user activities, and critical operations for regulatory requirements.

### Incident Investigation

Trace production issues back to specific changes using timestamp correlation and detailed change information.

### Performance Analysis

Identify performance-impacting changes by correlating audit log timestamps with performance metrics.

### Security Auditing

Monitor for unauthorized access, suspicious activities, and security-relevant changes across all workspaces.

### Team Coordination

Track team member activities, understand change patterns, and coordinate development efforts.

### Change Management

Maintain detailed records of all changes for change management processes and approval workflows.

Xano Audit Logs provide the foundation for enterprise-grade change management, compliance, and operational excellence. By leveraging both the interface and API capabilities, you can build comprehensive monitoring, reporting, and alerting systems that ensure transparency, accountability, and security across your entire Xano environment.