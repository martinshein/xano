---
title: Xano Backup and Restore - Complete Data Protection Guide
description: Master comprehensive backup and restore strategies for your Xano instances, including automated backups, manual snapshots, and disaster recovery planning
category: functions
difficulty: advanced
last_updated: '2025-08-17'
related_docs: []
subcategory: 08-reference/functions
tags:
  - backup-restore
  - data-protection
  - disaster-recovery
  - instance-management
  - data-security
  - business-continuity
  - automated-backup
  - recovery-planning
---

# Xano Backup and Restore - Complete Data Protection Guide

## 📋 **Quick Summary**

Xano's backup and restore system provides comprehensive data protection with automated rolling backups on paid plans, manual backup creation, custom scheduling, and full instance restoration capabilities for business continuity and disaster recovery.

## What You'll Learn

- **Automated Backup Management**: Understand Xano's automatic 3-day rolling backup system
- **Manual Backup Creation**: Create on-demand backups for critical milestones and deployments
- **Custom Backup Policies**: Configure backup timing and frequency for your specific needs
- **Media Storage Handling**: Decide when to include file storage in your backup strategy
- **Restore Operations**: Safely restore instances from backups with proper precautions
- **Disaster Recovery Planning**: Implement comprehensive backup strategies for business continuity

## Understanding Xano Backup System

### Automatic Rolling Backups
On all paid plans, Xano automatically maintains a **3-day rolling backup** of your entire instance:
- **Frequency**: Daily automatic backups
- **Retention**: 3 days of backup history
- **Coverage**: Complete instance including database, function stacks, and API configurations
- **Accessibility**: Available for restoration at any time during the retention period

### Plan-Based Backup Availability
| Plan Type | Backup Features |
|-----------|----------------|
| Free | ❌ No backups available |
| Launch/Starter/Scale | ✅ 3-day rolling backups + Manual backups |
| Pro/Enterprise | ✅ 3-day rolling backups + Manual backups + Custom policies |

## Creating Manual Backups

### Step-by-Step Manual Backup Process

**Step 1: Access Instance Settings**
From your instance selection screen, click the settings icon (⚙️) next to the instance you want to backup.

**Step 2: Navigate to Database Backup**
In the settings panel, choose "Database Backup" from the available options.

**Step 3: Create Manual Backup**
Click "Manual Backup" to start the backup creation process.

**Step 4: Configure Backup Options**
- **Database Backup**: Always included by default
- **Media Storage**: Check the option to include file storage if needed
  - ⚠️ **Important**: Media storage significantly increases backup size and duration
  - Only include media storage when absolutely necessary

**Step 5: Execute Backup**
Click "Create Backup" to start the backup process. The system will:
- Create a complete snapshot of your instance
- Include all database tables and data
- Package function stacks and API configurations
- Optionally include media storage files

### Best Practices for Manual Backups

```javascript
// Recommended backup timing strategy
const backupStrategy = {
  // Before major deployments
  preDeployment: {
    timing: "Immediately before releasing new features",
    includes: ["database", "functions", "apis"],
    excludeMedia: "Unless media changes are part of deployment"
  },
  
  // Weekly development milestones
  weeklySnapshots: {
    timing: "End of each development sprint",
    includes: ["complete_instance"],
    retention: "Keep for 30 days minimum"
  },
  
  // Before schema changes
  schemaUpdates: {
    timing: "Before any database structure modifications",
    critical: true,
    includes: ["database", "relationships", "indexes"]
  }
};
```

## Restoring from Backups

### Critical Pre-Restoration Steps

⚠️ **STRONGLY ADVISED**: Always create a current backup before restoring from an older one. This allows rollback if the restoration doesn't meet expectations.

### Restoration Process

**Step 1: Access Backup Management**
From your instance selection screen, click the settings icon next to the target instance.

**Step 2: Open Database Backup Panel**
Select "Database Backup" from the settings menu.

**Step 3: Choose Restoration Option**
Click "Download and Restore" to view available backup options.

**Step 4: Select Backup Version**
- Review available backups with timestamps
- Choose the specific backup point for restoration
- Verify backup contents and creation date

**Step 5: Execute Restoration**
Click "Restore" to begin the restoration process. The system will:
- Replace current instance data with backup data
- Restore database structure and content
- Recover function stacks and API configurations
- Apply backup-specific settings and configurations

### Post-Restoration Verification
```javascript
// Post-restoration checklist
const restorationVerification = {
  dataIntegrity: [
    "Verify critical tables have expected record counts",
    "Check data relationships are intact",
    "Validate recent data changes are as expected"
  ],
  
  functionalityTests: [
    "Test critical API endpoints",
    "Verify authentication systems",
    "Check third-party integrations",
    "Validate file upload/download features"
  ],
  
  configurationReview: [
    "Confirm environment variables",
    "Check team member permissions",
    "Verify instance settings",
    "Review custom function configurations"
  ]
};
```

## Custom Backup Policies

### Advanced Backup Scheduling

**Access Policy Settings**
1. Navigate to instance settings (⚙️ icon)
2. Choose "Database Backup"
3. Click "Policy" to access custom scheduling options

**Configure Backup Windows**
- **Default**: Early morning PST hours
- **Custom Options**: Select optimal backup windows based on:
  - Low traffic periods
  - Development team schedules
  - Business operation hours
  - Geographic considerations

```javascript
// Example custom backup policy configuration
const customBackupPolicy = {
  // Configure for global team with EU/US presence
  backupWindow: {
    timezone: "UTC",
    startHour: 2,  // 2 AM UTC (low traffic)
    duration: 2,   // 2-hour window
    frequency: "daily"
  },
  
  // Special policies for different environments
  environments: {
    production: {
      frequency: "daily",
      retention: "7_days",
      includeMedia: false,
      priority: "high"
    },
    
    staging: {
      frequency: "weekly", 
      retention: "3_days",
      includeMedia: true,
      priority: "normal"
    }
  }
};
```

## Integration with n8n, WeWeb, and Make.com

### n8n Automated Backup Management
```javascript
// n8n workflow for backup monitoring and management
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.cron",
      "parameters": {
        "expression": "0 0 * * 0"  // Weekly on Sunday
      }
    },
    {
      "name": "Create Xano Backup",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "POST",
        "url": "https://your-instance.xano.io/api:meta/backup/create",
        "authentication": "genericCredentialType",
        "headers": {
          "Authorization": "Bearer {{$credentials.xano.authToken}}"
        },
        "body": {
          "include_media": false,
          "backup_type": "scheduled"
        }
      }
    },
    {
      "name": "Backup Notification",
      "type": "n8n-nodes-base.slack",
      "parameters": {
        "channel": "#devops-alerts",
        "text": "✅ Weekly Xano backup completed successfully"
      }
    }
  ]
}
```

### WeWeb Backup Dashboard
```javascript
// WeWeb backup management interface
const backupDashboard = {
  // Display recent backups
  getBackupHistory: async () => {
    const backups = await xano.get('/api:meta/backups', {
      limit: 10,
      sort: 'created_at:desc'
    });
    
    return backups.map(backup => ({
      id: backup.id,
      created: new Date(backup.created_at).toLocaleDateString(),
      size: formatBytes(backup.size_bytes),
      type: backup.includes_media ? 'Complete' : 'Database Only',
      status: backup.status
    }));
  },
  
  // Backup creation interface
  createBackup: async (includeMedia = false) => {
    const response = await xano.post('/api:meta/backup/create', {
      include_media: includeMedia,
      description: `Manual backup - ${new Date().toISOString()}`
    });
    
    // Show progress notification
    showNotification('Backup creation started', 'success');
    return response;
  }
};
```

### Make.com Disaster Recovery Automation
```javascript
// Make.com scenario for automated disaster recovery
{
  "scenario": {
    "name": "Xano Disaster Recovery Monitor",
    "modules": [
      {
        "id": 1,
        "module": "http:ActionSendData",
        "parameters": {
          "url": "https://your-instance.xano.io/api:health",
          "method": "GET"
        }
      },
      {
        "id": 2,
        "module": "builtin:BasicRouter",
        "filter": {
          "conditions": [
            {
              "field": "{{1.statusCode}}",
              "operator": "notEqual",
              "value": "200"
            }
          ]
        }
      },
      {
        "id": 3,
        "module": "http:ActionSendData",
        "parameters": {
          "url": "https://your-instance.xano.io/api:meta/backup/restore",
          "method": "POST",
          "body": {
            "backup_id": "{{last_known_good_backup_id}}",
            "notify_team": true
          }
        }
      }
    ]
  }
}
```

## Advanced Backup Strategies

### Multi-Environment Backup Management
```javascript
// Comprehensive backup strategy for multiple environments
const enterpriseBackupStrategy = {
  environments: {
    production: {
      frequency: "4_times_daily",
      retention: "30_days",
      includeMedia: true,
      verification: "automated_testing",
      offsite: "s3_backup",
      encryption: "required"
    },
    
    staging: {
      frequency: "daily",
      retention: "7_days", 
      includeMedia: false,
      verification: "basic_checks",
      offsite: "optional"
    },
    
    development: {
      frequency: "weekly",
      retention: "3_days",
      includeMedia: false,
      verification: "none"
    }
  },
  
  // Automated backup verification
  verification: {
    postBackup: [
      "Test critical API endpoints",
      "Verify data integrity checksums",
      "Confirm backup file accessibility",
      "Validate backup metadata"
    ]
  }
};
```

### Backup Size Optimization
```javascript
// Strategies for managing backup storage efficiently
const backupOptimization = {
  // Media storage considerations
  mediaStrategy: {
    include: [
      "Critical user uploads",
      "System configuration files",
      "Essential assets"
    ],
    exclude: [
      "Temporary files", 
      "Cache directories",
      "Log files",
      "Development assets"
    ]
  },
  
  // Database optimization before backup
  preBackupCleanup: [
    "Clear expired sessions",
    "Archive old audit logs", 
    "Remove temporary data",
    "Optimize database indexes"
  ],
  
  // Backup retention strategy
  retention: {
    daily: "7_days",
    weekly: "4_weeks", 
    monthly: "12_months",
    yearly: "permanent"
  }
};
```

## 💡 **Pro Tips**

1. **Backup Before Updates**: Always create a manual backup before major system updates, schema changes, or new feature deployments

2. **Test Restore Procedures**: Periodically test your restore process in a staging environment to ensure backups are viable

3. **Monitor Backup Sizes**: Track backup sizes over time to identify data growth patterns and optimize storage costs

4. **Document Backup Procedures**: Maintain clear documentation of your backup and restore procedures for team members

5. **Consider External Backups**: For critical applications, implement additional backup strategies using external services

## Try This: Comprehensive Backup Automation

Set up an automated backup and monitoring system:

```javascript
// Complete backup automation workflow
const backupAutomation = {
  // Daily production backup
  schedule: {
    production: "0 2 * * *",  // 2 AM daily
    staging: "0 4 * * 0",     // 4 AM weekly
    development: "0 6 1 * *"  // 6 AM monthly
  },
  
  // Backup validation
  validation: async (backupId) => {
    const tests = [
      'database_integrity',
      'api_functionality', 
      'authentication_flow',
      'data_relationships'
    ];
    
    for (const test of tests) {
      const result = await runValidationTest(test, backupId);
      if (!result.success) {
        await notifyTeam(`Backup validation failed: ${test}`);
        return false;
      }
    }
    return true;
  },
  
  // Recovery procedures
  recovery: {
    rto: "15_minutes",  // Recovery Time Objective
    rpo: "1_hour",      // Recovery Point Objective
    steps: [
      "Assess incident scope",
      "Select appropriate backup",
      "Notify stakeholders",
      "Execute restoration",
      "Validate recovery",
      "Resume operations"
    ]
  }
};
```

## Common Mistakes to Avoid

❌ **Forgetting to backup before major changes**
✅ Always create a pre-deployment backup before significant updates

❌ **Including media storage unnecessarily**
✅ Only include media storage when file changes are critical to preserve

❌ **Not testing restore procedures**
✅ Regularly test backup restoration in staging environments

❌ **Relying solely on automatic backups**
✅ Create manual backups at critical development milestones

❌ **Ignoring backup size growth**
✅ Monitor and optimize backup sizes to manage storage costs effectively

Proper backup and restore procedures are essential for maintaining business continuity and protecting your valuable data. Implement comprehensive backup strategies that match your business requirements and regularly test your disaster recovery procedures.