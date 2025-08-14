---
title: "Workspace Import & Export with Metadata API - Complete Guide"
description: "Master Xano workspace backup, migration, and deployment with the Metadata API - essential for agencies, DevOps, and multi-environment workflows"
category: api-endpoints
tags:
  - Workspace Management
  - Backup & Restore
  - Data Migration
  - DevOps
  - CI/CD
  - Environment Management
difficulty: advanced
reading_time: 15 minutes
last_updated: '2025-01-23'
prerequisites:
  - Paid Xano plan (required for import/export)
  - Metadata API access with proper scopes
  - Understanding of branching concepts
  - File handling knowledge
---

# Workspace Import & Export with Metadata API

## 📋 **Quick Summary**

**What it does:** The Metadata API's import/export features provide programmatic workspace backup, migration, and deployment capabilities for advanced DevOps workflows.

**Why it matters:** This enables you to:
- Create automated backup systems for workspace protection
- Migrate workspaces between instances and environments
- Implement CI/CD pipelines with database schema versioning
- Clone production environments for testing and development
- Build agency workflow tools for client workspace management

**Time to implement:** 15-30 minutes for basic backup, hours for advanced CI/CD pipelines

---

## What You'll Learn

- Export strategies: schema-only vs. full workspace
- Import operations with branch management
- Password protection and encryption workflows
- Multi-environment deployment patterns
- Agency and enterprise workflow automation
- Error handling and recovery procedures

## Understanding Workspace Import/Export

Think of workspace import/export as Git for your entire backend - you can create snapshots, deploy changes, and manage different versions of your workspace across environments.

### 🎯 **Perfect For:**
- **Agencies:** Client workspace templates and migrations
- **DevOps:** Automated deployment and backup systems
- **Development:** Staging/production environment synchronization
- **Enterprise:** Multi-tenant workspace management
- **Backup:** Disaster recovery and data protection

## ⚠️ **Critical Requirements & Limitations**

### Plan Requirements
```yaml
Required: 
  - Paid Xano plan (Pro, Scale, or Enterprise)
  - Cannot be used on free plans

Limitations:
  - Large workspaces may fail via API (contact support)
  - Exports only include one branch (defaults to live)
  - Draft changes are not exported
  - Imports completely overwrite destination workspace
```

### API Scope Requirements
```yaml
For Export Operations:
  - Workspace Content: Read permission

For Import Operations:
  - Workspace Content: Update permission
```

## Export Operations

### Schema-Only Export

Export just the database structure and configuration without data:

```javascript
POST /api:metadata/workspace/{workspace_id}/export-schema
```

**Request Body:**
```json
{
  "branch": "main",        // Optional: defaults to live branch
  "password": "secure123"  // Optional: encrypt export file
}
```

### Full Workspace Export

Export complete workspace including all data:

```javascript
POST /api:metadata/workspace/{workspace_id}/export
```

**Request Body:**
```json
{
  "branch": "development", // Optional: specify branch
  "password": "backup2024" // Optional: password protection
}
```

### 📝 **Export Response Format**

```json
{
  "download_url": "https://exports.xano.io/file/abc123.xano",
  "expires_at": "2025-01-24T12:00:00Z",
  "size_bytes": 15728640,
  "encrypted": true,
  "branch_exported": "main",
  "export_type": "full_workspace"
}
```

## Import Operations

### Schema Import with Branch Creation

Import schema into a new branch:

```javascript
POST /api:metadata/workspace/{workspace_id}/import-schema
Content-Type: multipart/form-data
```

**Form Data:**
```javascript
{
  "file": [binary file data],
  "newbranch": "imported-schema-v2",
  "setlive": false,           // Optional: make branch live
  "password": "secure123"     // Required if file is encrypted
}
```

### Full Workspace Import

Replace entire workspace with imported content:

```javascript
POST /api:metadata/workspace/{workspace_id}/import
Content-Type: multipart/form-data
```

**Form Data:**
```javascript
{
  "file": [binary file data],
  "password": "backup2024"    // Required if file is encrypted
}
```

## No-Code Platform Integrations

### 🔗 **n8n Backup Automation**

```yaml
Automated Backup Workflow:
1. Schedule Trigger (Daily at 2 AM)
2. HTTP Request (Export workspace)
3. Wait (For export completion)
4. HTTP Request (Download export file)
5. FTP Upload (Store in backup location)
6. Email (Notify backup completion)
```

**n8n Export Configuration:**
```javascript
// Export workspace with encryption
const exportRequest = {
  method: 'POST',
  url: `https://[instance].xano.io/api:metadata/workspace/${workspaceId}/export`,
  headers: {
    'Authorization': `Bearer ${metadataToken}`,
    'Content-Type': 'application/json'
  },
  body: {
    branch: '',  // Live branch
    password: $env.BACKUP_PASSWORD
  }
};
```

### 🌐 **WeWeb Deployment Dashboard**

```javascript
// WeWeb action for workspace deployment
async function deployToProduction(sourceWorkspaceId, targetWorkspaceId) {
  try {
    // 1. Export from staging
    const exportResponse = await wwLib.api.post({
      url: `${wwLib.envVars.XANO_METADATA_API}/workspace/${sourceWorkspaceId}/export-schema`,
      data: {
        branch: 'staging',
        password: wwLib.envVars.DEPLOYMENT_PASSWORD
      },
      headers: {
        'Authorization': 'Bearer ' + wwLib.envVars.METADATA_TOKEN
      }
    });
    
    // 2. Download export file
    const fileResponse = await fetch(exportResponse.data.download_url);
    const fileBlob = await fileResponse.blob();
    
    // 3. Import to production
    const formData = new FormData();
    formData.append('file', fileBlob);
    formData.append('newbranch', `deploy-${Date.now()}`);
    formData.append('setlive', 'true');
    formData.append('password', wwLib.envVars.DEPLOYMENT_PASSWORD);
    
    const importResponse = await wwLib.api.post({
      url: `${wwLib.envVars.XANO_METADATA_API}/workspace/${targetWorkspaceId}/import-schema`,
      data: formData,
      headers: {
        'Authorization': 'Bearer ' + wwLib.envVars.METADATA_TOKEN
      }
    });
    
    return {
      success: true,
      deploymentId: importResponse.data.branch.id,
      message: 'Deployment completed successfully'
    };
    
  } catch (error) {
    console.error('Deployment failed:', error);
    return {
      success: false,
      error: error.message
    };
  }
}
```

### 🔧 **Make CI/CD Pipeline**

```yaml
Deployment Scenario:
1. GitHub Webhook (Code changes detected)
2. HTTP Request (Export staging workspace)
3. Iterator (Process deployment steps)
4. HTTP Request (Import to production)
5. Slack Notification (Deployment status)
6. Error Handler (Rollback on failure)
```

## Advanced Patterns & Use Cases

### Pattern 1: Multi-Environment Deployment

```javascript
class WorkspaceDeploymentManager {
  constructor(metadataToken) {
    this.token = metadataToken;
    this.baseUrl = 'https://[instance].xano.io/api:metadata';
  }
  
  async deployToEnvironment(sourceWorkspaceId, targetWorkspaceId, options = {}) {
    const deploymentId = `deploy-${Date.now()}`;
    
    try {
      // 1. Create deployment branch in target
      const exportResponse = await this.exportWorkspace(sourceWorkspaceId, {
        branch: options.sourceBranch || 'main',
        password: options.password
      });
      
      // 2. Download and validate export
      const exportFile = await this.downloadExport(exportResponse.download_url);
      this.validateExport(exportFile);
      
      // 3. Import to target workspace
      const importResponse = await this.importSchema(targetWorkspaceId, exportFile, {
        newbranch: deploymentId,
        setlive: options.setLive || false,
        password: options.password
      });
      
      // 4. Run post-deployment validation
      if (options.validate) {
        await this.validateDeployment(targetWorkspaceId, deploymentId);
      }
      
      return {
        success: true,
        deploymentId,
        branchId: importResponse.branch.id,
        timestamp: new Date().toISOString()
      };
      
    } catch (error) {
      // Rollback on failure
      if (options.rollbackOnError) {
        await this.rollbackDeployment(targetWorkspaceId, deploymentId);
      }
      
      throw new Error(`Deployment failed: ${error.message}`);
    }
  }
  
  async createBackup(workspaceId, backupType = 'full') {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const backupName = `backup-${workspaceId}-${timestamp}`;
    
    const endpoint = backupType === 'schema' ? 'export-schema' : 'export';
    
    const response = await fetch(`${this.baseUrl}/workspace/${workspaceId}/${endpoint}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        password: process.env.BACKUP_PASSWORD
      })
    });
    
    if (!response.ok) {
      throw new Error(`Backup failed: ${response.statusText}`);
    }
    
    const result = await response.json();
    
    return {
      backupName,
      downloadUrl: result.download_url,
      expiresAt: result.expires_at,
      size: result.size_bytes
    };
  }
}
```

### Pattern 2: Agency Client Management

```javascript
class AgencyWorkspaceManager {
  async cloneClientTemplate(templateWorkspaceId, clientWorkspaceId, clientConfig) {
    // 1. Export template workspace
    const template = await this.exportWorkspace(templateWorkspaceId, {
      type: 'schema',
      password: process.env.TEMPLATE_PASSWORD
    });
    
    // 2. Customize for client
    const customizedTemplate = await this.customizeTemplate(template, clientConfig);
    
    // 3. Import to client workspace
    const deployment = await this.importToClient(clientWorkspaceId, customizedTemplate);
    
    // 4. Configure client-specific settings
    await this.applyClientConfiguration(clientWorkspaceId, clientConfig);
    
    return {
      clientId: clientConfig.clientId,
      workspaceId: clientWorkspaceId,
      templateVersion: template.version,
      deploymentId: deployment.id
    };
  }
  
  async migrateClientWorkspace(fromWorkspaceId, toWorkspaceId, migrationPlan) {
    const steps = [];
    
    try {
      // 1. Pre-migration backup
      steps.push('backup');
      const backup = await this.createBackup(fromWorkspaceId, 'full');
      
      // 2. Export source workspace
      steps.push('export');
      const exportData = await this.exportWorkspace(fromWorkspaceId, {
        includeData: migrationPlan.includeData,
        password: migrationPlan.password
      });
      
      // 3. Prepare target workspace
      steps.push('prepare');
      await this.prepareTargetWorkspace(toWorkspaceId, migrationPlan);
      
      // 4. Import to target
      steps.push('import');
      const importResult = await this.importWorkspace(toWorkspaceId, exportData);
      
      // 5. Post-migration validation
      steps.push('validate');
      await this.validateMigration(toWorkspaceId, migrationPlan.validationRules);
      
      // 6. Update client records
      steps.push('finalize');
      await this.updateClientRecords(migrationPlan.clientId, {
        oldWorkspaceId: fromWorkspaceId,
        newWorkspaceId: toWorkspaceId,
        migrationDate: new Date()
      });
      
      return {
        success: true,
        stepsCompleted: steps,
        backupUrl: backup.downloadUrl,
        newWorkspaceId: toWorkspaceId
      };
      
    } catch (error) {
      return {
        success: false,
        failedAtStep: steps[steps.length - 1],
        error: error.message,
        rollbackRequired: true
      };
    }
  }
}
```

### Pattern 3: Enterprise Multi-Tenant Management

```javascript
class EnterpriseWorkspaceOrchestrator {
  async deployToAllTenants(templateWorkspaceId, tenantList, deploymentConfig) {
    const deploymentResults = [];
    const concurrencyLimit = deploymentConfig.maxConcurrent || 3;
    
    // Process tenants in batches
    for (let i = 0; i < tenantList.length; i += concurrencyLimit) {
      const batch = tenantList.slice(i, i + concurrencyLimit);
      
      const batchPromises = batch.map(async (tenant) => {
        try {
          const result = await this.deployToTenant(templateWorkspaceId, tenant, deploymentConfig);
          return { tenant: tenant.id, success: true, result };
        } catch (error) {
          return { tenant: tenant.id, success: false, error: error.message };
        }
      });
      
      const batchResults = await Promise.all(batchPromises);
      deploymentResults.push(...batchResults);
      
      // Progress reporting
      this.reportProgress(deploymentResults.length, tenantList.length);
    }
    
    return {
      totalTenants: tenantList.length,
      successful: deploymentResults.filter(r => r.success).length,
      failed: deploymentResults.filter(r => !r.success).length,
      results: deploymentResults
    };
  }
  
  async synchronizeEnvironments(productionWorkspaceId, environmentMappings) {
    const syncResults = {};
    
    for (const [envName, envWorkspaceId] of Object.entries(environmentMappings)) {
      try {
        // Export from production
        const prodExport = await this.exportWorkspace(productionWorkspaceId, {
          type: 'schema',
          password: process.env.SYNC_PASSWORD
        });
        
        // Import to environment
        const importResult = await this.importSchema(envWorkspaceId, prodExport, {
          newbranch: `sync-${Date.now()}`,
          setlive: true
        });
        
        syncResults[envName] = {
          success: true,
          branchId: importResult.branch.id,
          syncTime: new Date().toISOString()
        };
        
      } catch (error) {
        syncResults[envName] = {
          success: false,
          error: error.message
        };
      }
    }
    
    return syncResults;
  }
}
```

## Security & Best Practices

### Password Protection Strategy

```javascript
// Generate secure passwords for exports
function generateExportPassword(workspaceId, timestamp) {
  const crypto = require('crypto');
  const baseString = `${workspaceId}-${timestamp}-${process.env.SECRET_KEY}`;
  return crypto.createHash('sha256').update(baseString).digest('hex').substring(0, 32);
}

// Secure password storage
class PasswordManager {
  constructor() {
    this.vault = new Map();
  }
  
  storePassword(exportId, password) {
    // Encrypt before storing
    const encrypted = this.encrypt(password);
    this.vault.set(exportId, {
      password: encrypted,
      expiresAt: Date.now() + (24 * 60 * 60 * 1000) // 24 hours
    });
  }
  
  retrievePassword(exportId) {
    const entry = this.vault.get(exportId);
    if (!entry || Date.now() > entry.expiresAt) {
      throw new Error('Password expired or not found');
    }
    return this.decrypt(entry.password);
  }
}
```

### Validation & Error Handling

```javascript
function validateExportFile(fileBuffer) {
  // Basic file validation
  if (!fileBuffer || fileBuffer.length === 0) {
    throw new Error('Export file is empty');
  }
  
  // Check file header for Xano export format
  const header = fileBuffer.slice(0, 10).toString();
  if (!header.includes('XANO')) {
    throw new Error('Invalid Xano export file format');
  }
  
  // Size validation
  const maxSize = 500 * 1024 * 1024; // 500MB
  if (fileBuffer.length > maxSize) {
    throw new Error('Export file too large for API import');
  }
  
  return true;
}

async function safeImport(workspaceId, fileBuffer, options = {}) {
  try {
    // Pre-import validation
    validateExportFile(fileBuffer);
    
    // Create backup before import
    const backup = await createBackup(workspaceId);
    
    // Attempt import
    const importResult = await importWorkspace(workspaceId, fileBuffer, options);
    
    // Post-import validation
    await validateImportResult(workspaceId, importResult);
    
    return {
      success: true,
      importResult,
      backupUrl: backup.downloadUrl
    };
    
  } catch (error) {
    // Rollback on failure
    if (options.autoRollback && backup) {
      await rollbackFromBackup(workspaceId, backup);
    }
    
    throw new Error(`Import failed: ${error.message}`);
  }
}
```

## Performance Optimization

### Large Workspace Handling

```javascript
class LargeWorkspaceManager {
  async exportLargeWorkspace(workspaceId, options = {}) {
    // Check workspace size first
    const workspaceInfo = await this.getWorkspaceInfo(workspaceId);
    
    if (workspaceInfo.estimatedSize > 100 * 1024 * 1024) { // 100MB
      console.warn('Large workspace detected, consider schema-only export');
      
      if (options.forceSchemaOnly) {
        return this.exportSchema(workspaceId, options);
      }
    }
    
    // Use chunked export for very large workspaces
    if (workspaceInfo.estimatedSize > 1024 * 1024 * 1024) { // 1GB
      throw new Error('Workspace too large for API export. Contact Xano support.');
    }
    
    return this.exportWorkspace(workspaceId, options);
  }
  
  async monitorExportProgress(exportId) {
    const maxWaitTime = 30 * 60 * 1000; // 30 minutes
    const pollInterval = 30 * 1000;     // 30 seconds
    const startTime = Date.now();
    
    while (Date.now() - startTime < maxWaitTime) {
      const status = await this.checkExportStatus(exportId);
      
      if (status.completed) {
        return status;
      }
      
      if (status.failed) {
        throw new Error(`Export failed: ${status.error}`);
      }
      
      await new Promise(resolve => setTimeout(resolve, pollInterval));
    }
    
    throw new Error('Export timeout - operation took too long');
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Create a simple backup system that:
1. Exports workspace schema daily
2. Stores backups with timestamps
3. Sends email notifications
4. Retains last 7 backups

### Intermediate Challenge
Build a staging-to-production deployment tool that:
1. Exports staging workspace
2. Creates new branch in production
3. Validates deployment
4. Makes branch live if validation passes

### Advanced Challenge
Design an enterprise multi-tenant system that:
1. Manages workspace templates
2. Deploys to multiple tenants
3. Handles rollbacks and recovery
4. Provides audit trails and reporting

## Common Mistakes to Avoid

1. **Not using paid plans** - Import/export requires paid subscription
2. **Forgetting password protection** - Sensitive data should be encrypted
3. **No backup before import** - Always backup before destructive operations
4. **Ignoring file size limits** - Large workspaces may need support assistance
5. **Missing error handling** - Network issues and timeouts are common

## Troubleshooting

### Common Issues

| Error | Cause | Solution |
|-------|-------|----------|
| 403 Forbidden | Insufficient permissions | Check API token scopes |
| 413 Payload Too Large | Workspace too big | Use schema-only export |
| 500 Server Error | Large workspace/timeout | Contact Xano support |
| Invalid file format | Corrupted export | Re-export workspace |
| Password required | Encrypted file | Provide correct password |

### Recovery Procedures

```javascript
// Emergency rollback procedure
async function emergencyRollback(workspaceId, backupFile) {
  try {
    console.log('Starting emergency rollback...');
    
    // Import backup file
    const rollbackResult = await importWorkspace(workspaceId, backupFile, {
      setlive: true,
      skipValidation: true // Emergency mode
    });
    
    console.log('Rollback completed successfully');
    return rollbackResult;
    
  } catch (error) {
    console.error('Rollback failed:', error.message);
    console.log('Manual intervention required - contact Xano support');
    throw error;
  }
}
```

## Next Steps

- Master [Content Management](content.md) for data operations
- Explore [Token Security](token-scopes-reference.md) for proper access control
- Learn about [Request History](request-history.md) for monitoring deployments
- Understand [Search Operations](search.md) for workspace discovery

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - DevOps and deployment discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Import/export workflows
- 📖 [Branching Docs](../../collaboration/branching-merging.md) - Advanced branch management
- 🔧 [Support](https://xano.com/support) - Large workspace assistance