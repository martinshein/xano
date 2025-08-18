---
title: Xano Audit Logs - Complete Workspace Activity Tracking
description: Master audit logs for comprehensive workspace monitoring, security compliance, and team collaboration tracking in your Xano backend applications
category: functions
difficulty: advanced
last_updated: '2025-08-17'
related_docs: []
subcategory: 08-reference/functions
tags:
  - audit-logs
  - workspace-security
  - compliance
  - team-collaboration
  - activity-tracking
  - security-monitoring
  - RBAC
  - workspace-management
---

# Xano Audit Logs - Complete Workspace Activity Tracking

## 📋 **Quick Summary**

Audit Logs provide detailed and searchable information about any changes or activity inside of a Xano workspace, offering comprehensive tracking for security compliance, team collaboration, and operational monitoring.

## What You'll Learn

- **Comprehensive Activity Tracking**: Monitor all workspace changes including database, API, and user activities
- **Security and Compliance**: Implement audit trails for regulatory compliance and security monitoring
- **Team Collaboration Insights**: Track team member actions and workspace modifications
- **Search and Export**: Filter, search, and export audit data for analysis and reporting
- **Retention Management**: Understand audit log retention policies across different plans
- **API Integration**: Access audit logs programmatically via Metadata API endpoints

## Core Audit Log Categories

### Workspace Management
Track fundamental workspace operations:
- **Create Workspace**: New workspace creation events
- **Update Workspace**: Workspace setting modifications  
- **Reset Workspace**: Workspace reset to default state operations
- **Read Workspace**: Workspace information access events
- **Delete Workspace**: Workspace removal activities

### Database Activity Monitoring
Monitor all database-related changes:
- **Table Operations**: Create, update, delete, and restore table actions
- **Data Modifications**: Record creation, updates, and deletions
- **Schema Changes**: Field additions, modifications, and relationship updates
- **Database Queries**: Track query execution and performance

### API and Function Stack Tracking
Keep tabs on your backend logic:
- **API Group Management**: API endpoint group creation, updates, and deletions
- **Function Operations**: Custom function creation, modifications, and executions
- **Query Activities**: API endpoint creation, updates, and execution tracking
- **Add-on Management**: Add-on installations, updates, and usage

### Authentication and Security Events
Monitor security-critical activities:
- **User Actions**: Authentication events and user activity tracking
- **Permission Changes**: RBAC permission modifications
- **Token Management**: JWT token generation and validation events
- **Security Policy Updates**: Security setting modifications

## Audit Log Retention by Plan

| Plan Type | Retention Period |
|-----------|------------------|
| Free/Build | 24 hours |
| Launch, Starter, Starter+ | 7 days |
| Scale, Pro, Pro+ | 28 days |
| Enterprise/Custom | Unlimited |

## Accessing and Managing Audit Logs

### Via Xano Interface

**Step 1: Navigate to Audit Logs**
From your workspace dashboard, click the three dots (⋯) in the top-right corner and choose "Audit Logs".

**Step 2: View Log Details**
Browse through the chronological list of activities. Click any log entry to view detailed information including:
- Event timestamp and description
- User responsible for the action
- Affected workspace/branch
- JSON payload with complete event data
- Quick navigation to related resources (when available)

**Step 3: Search and Filter**
Use the search panel to filter logs by:
- **Event Type**: Filter by specific activity categories
- **User**: View actions by specific team members
- **Time Range**: Focus on specific date ranges
- **Labels**: Filter by custom event labels

### Programmatic Access via Metadata API

Access audit logs through dedicated API endpoints:

#### Browse All Audit Logs
```javascript
// GET /api:meta/audit_log
const response = await fetch('https://your-instance.xano.io/api:meta/audit_log', {
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN',
    'Content-Type': 'application/json'
  },
  params: {
    page: 1,
    per_page: 50,
    include_data: true
  }
});
```

#### Advanced Search with Filtering
```javascript
// POST /api:meta/audit_log/search
const searchQuery = await fetch('https://your-instance.xano.io/api:meta/audit_log/search', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    page: 1,
    per_page: 50,
    sort: { id: "desc" },
    search: [
      { field: "type", operator: "eq", value: "Create Table" },
      { field: "user.email", operator: "like", value: "@yourcompany.com" }
    ]
  })
});
```

## Integration with n8n, WeWeb, and Make.com

### n8n Audit Log Monitoring
```javascript
// n8n HTTP Request Node for audit log monitoring
{
  "method": "GET",
  "url": "https://your-instance.xano.io/api:meta/audit_log",
  "authentication": "genericCredentialType",
  "headers": {
    "Authorization": "Bearer {{$credentials.xano.authToken}}"
  },
  "qs": {
    "per_page": 100,
    "include_data": true
  }
}

// Set up webhook for real-time audit notifications
// Trigger: Schedule (every 5 minutes)
// Filter: New audit entries since last check
// Action: Send Slack notification for critical events
```

### WeWeb Audit Dashboard
```javascript
// WeWeb Formula for audit log display
// Create dynamic table showing recent activities
const auditData = await xano.get('/api:meta/audit_log', {
  per_page: 20,
  page: context.currentPage
});

// Format for dashboard display
return auditData.items.map(log => ({
  timestamp: new Date(log.created_at).toLocaleString(),
  action: log.type,
  user: log.user?.email || 'System',
  description: log.msg,
  workspace: log.workspace?.name
}));
```

### Make.com Compliance Automation
```javascript
// Make.com scenario for compliance reporting
// Module 1: Xano HTTP Request - Get audit logs
{
  "url": "https://your-instance.xano.io/api:meta/audit_log/search",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{connection.authToken}}",
    "Content-Type": "application/json"
  },
  "body": {
    "search": [
      {
        "field": "type",
        "operator": "in",
        "value": ["Delete Table", "Delete Workspace", "Update Security Policy"]
      }
    ],
    "sort": {"created_at": "desc"}
  }
}

// Module 2: Google Sheets - Create compliance report
// Module 3: Email notification for critical activities
```

## Security and Compliance Implementation

### RBAC Permission Requirements
For audit log access, ensure team members have the **Workspace Logs** permission enabled in your RBAC settings.

### Compliance Best Practices
```javascript
// Example: Automated compliance check
const complianceCheck = {
  // Monitor critical security events
  securityEvents: [
    'Update Security Policy',
    'Create User',
    'Delete User', 
    'Update RBAC Permissions'
  ],
  
  // Check for suspicious patterns
  checkSuspiciousActivity: (logs) => {
    const suspiciousPatterns = [
      'Multiple failed authentications',
      'Unusual delete operations',
      'Off-hours administrative actions'
    ];
    
    return logs.filter(log => 
      suspiciousPatterns.some(pattern => 
        log.description.includes(pattern)
      )
    );
  },
  
  // Generate compliance report
  generateReport: async () => {
    const logs = await xano.get('/api:meta/audit_log/search', {
      search: [
        {field: 'created_at', operator: 'gte', value: last30Days}
      ]
    });
    
    return {
      totalEvents: logs.itemsTotal,
      securityEvents: logs.items.filter(log => 
        complianceCheck.securityEvents.includes(log.type)
      ),
      userActivity: groupBy(logs.items, 'user.email'),
      suspiciousActivity: complianceCheck.checkSuspiciousActivity(logs.items)
    };
  }
};
```

## Advanced Audit Log Analysis

### Custom Event Filtering
```javascript
// Create custom audit log filters for specific needs
const customFilters = {
  // Monitor API endpoint changes
  apiChanges: {
    search: [
      {field: 'type', operator: 'like', value: 'Query'},
      {field: 'type', operator: 'like', value: 'API Group'}
    ]
  },
  
  // Track database modifications
  databaseChanges: {
    search: [
      {field: 'type', operator: 'like', value: 'Table'},
      {field: 'type', operator: 'like', value: 'Record'}
    ]
  },
  
  // Monitor team collaboration
  teamActivity: {
    search: [
      {field: 'type', operator: 'eq', value: 'Create Branch'},
      {field: 'type', operator: 'eq', value: 'Merge Branch'},
      {field: 'type', operator: 'eq', value: 'Update Workspace'}
    ]
  }
};
```

### Export and Backup Strategies
```javascript
// Automated audit log backup
const auditBackup = {
  // Export to CSV for external analysis
  exportToCsv: async (startDate, endDate) => {
    const logs = await xano.post('/api:meta/audit_log/search', {
      search: [
        {field: 'created_at', operator: 'gte', value: startDate},
        {field: 'created_at', operator: 'lte', value: endDate}
      ],
      per_page: 1000
    });
    
    return convertToCSV(logs.items, [
      'created_at', 'type', 'msg', 'user.email', 
      'workspace.name', 'branch.label'
    ]);
  },
  
  // Schedule regular backups
  scheduleBackup: () => {
    // Set up cron job or scheduled task
    // Export weekly audit summaries
    // Store in external system (S3, Google Drive, etc.)
  }
};
```

## 💡 **Pro Tips**

1. **Set Up Monitoring Alerts**: Create automated notifications for critical audit events like security policy changes or bulk delete operations

2. **Regular Compliance Reviews**: Schedule monthly audit log reviews to identify patterns and ensure compliance with your organization's policies

3. **Custom Dashboards**: Build audit dashboards in WeWeb or n8n to visualize workspace activity trends and team productivity

4. **Integration with SIEM**: Connect audit logs to your Security Information and Event Management system for comprehensive security monitoring

5. **Retention Planning**: For Enterprise plans with unlimited retention, implement regular archiving strategies to manage storage costs

## Try This: Audit Log Security Dashboard

Create a real-time security monitoring dashboard:

```javascript
// 1. Set up n8n workflow for audit log monitoring
// 2. Filter for security-critical events
// 3. Create Slack alerts for suspicious activity
// 4. Build WeWeb dashboard showing:
//    - Recent security events
//    - User activity summary
//    - Failed authentication attempts
//    - Database modification trends

const securityDashboard = {
  criticalEvents: ['Delete Workspace', 'Update Security Policy', 'Create User'],
  monitoringInterval: '5 minutes',
  alertThreshold: 'Immediate',
  retentionPolicy: 'Archive monthly for Enterprise compliance'
};
```

## Common Mistakes to Avoid

❌ **Not setting proper RBAC permissions for audit log access**
✅ Configure "Workspace Logs" permission for appropriate team members

❌ **Ignoring audit log retention limits on lower-tier plans**  
✅ Implement regular export procedures for long-term compliance needs

❌ **Not monitoring critical security events in real-time**
✅ Set up automated alerts for high-risk activities

❌ **Using audit logs only reactively after incidents**
✅ Implement proactive monitoring and regular compliance reviews

Audit logs are essential for maintaining security, compliance, and operational visibility in your Xano workspace. Use them proactively to monitor team activities, ensure security best practices, and maintain comprehensive records of all workspace changes.