---
title: "Workspace Import and Export API"
description: "Learn how to use Xano's Metadata API to export and import workspace schemas and content for backup, deployment, and collaboration workflows"
category: expressions
has_code_examples: true
last_updated: '2025-01-16'
tags:
  - metadata-api
  - workspace
  - import-export
  - backup
  - deployment
---

# Workspace Import and Export API

## 📋 **Quick Summary**

Xano's Workspace Import and Export API allows you to programmatically backup, migrate, and deploy your workspace configurations including database schemas, API endpoints, and custom functions. This is essential for DevOps workflows, staging environments, and backup strategies.

## What You'll Learn

- How to export workspace schemas and content via API
- Different export options (schema-only vs. full content)
- Import workflows for different deployment scenarios
- Security considerations with password protection
- Best practices for automated backup systems
- Integration patterns with CI/CD pipelines

## Understanding Workspace Exports

Before diving into the API, it's important to understand what gets exported:

**Schema Export includes:**
- Database table structures (without data)
- API endpoint configurations
- Custom function definitions
- Branch configurations

**Full Export includes:**
- Everything from schema export
- Database table content
- File attachments (optional)

**Important Limitations:**
- Only works on paid Xano plans
- Exports only one branch (defaults to live)
- Drafts are not included in exports
- Large workspaces may need manual assistance

## Export Database Schema API

Export only the database structure and API configurations without data content.

### API Endpoint
```http
POST /api:meta/workspace/{workspace_id}/export-schema
```

### Required Parameters
- `workspace_id`: Your workspace identifier
- **API Scope Required**: Instance Workspace: Read

### Optional Parameters
- `branch`: Specific branch to export (leave empty for live branch)
- `password`: Encrypt the export file (recommended for sensitive data)

### Example Request

```javascript
// Export schema with password protection
const response = await fetch('/api:meta/workspace/123/export-schema', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    branch: "", // Empty for live branch
    password: "secure-backup-password"
  })
});

const exportData = await response.json();
```

## Export Full Workspace API

Export complete workspace including data content.

### API Endpoint
```http
POST /api:meta/workspace/{workspace_id}/export
```

### Example Request

```javascript
// Export complete workspace
const response = await fetch('/api:meta/workspace/123/export', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    branch: "development", // Specific branch
    password: "backup-password-2024"
  })
});
```

## Import Schema API

Import a schema export into a new branch with options to merge or set live.

### API Endpoint
```http
POST /api:meta/workspace/{workspace_id}/import-schema
```

### Required Parameters
- `file`: The exported schema file (binary)
- `newbranch`: Name for the new branch to create

### Optional Parameters
- `setlive`: Boolean to immediately set the new branch as live
- `password`: Password if the export was encrypted

### Example Implementation

```javascript
// Import schema to new branch
const formData = new FormData();
formData.append('file', exportFile);
formData.append('newbranch', 'imported-schema-v2');
formData.append('setlive', 'false');
formData.append('password', 'secure-backup-password');

const response = await fetch('/api:meta/workspace/123/import-schema', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
  },
  body: formData
});
```

## Import Full Workspace API

Import a complete workspace export, replacing all content.

### API Endpoint
```http
POST /api:meta/workspace/{workspace_id}/import
```

**⚠️ WARNING**: This completely overwrites the destination workspace content.

### Required Parameters
- `file`: The exported workspace file (binary)

### Optional Parameters
- `password`: Password if the export was encrypted

**API Scope Required**: Instance Workspace: Update

## Try This: Automated Backup Script

Create a Node.js script for automated workspace backups:

```javascript
const fs = require('fs');

async function backupWorkspace(workspaceId, jwtToken) {
  try {
    // Export schema with timestamp
    const timestamp = new Date().toISOString().replace(/:/g, '-');
    const password = `backup-${timestamp}`;
    
    const response = await fetch(`/api:meta/workspace/${workspaceId}/export`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${jwtToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        password: password
      })
    });
    
    if (response.ok) {
      const backup = await response.arrayBuffer();
      const filename = `workspace-${workspaceId}-${timestamp}.xano`;
      fs.writeFileSync(filename, Buffer.from(backup));
      
      console.log(`Backup saved: ${filename}`);
      console.log(`Password: ${password}`);
      
      return { filename, password };
    }
  } catch (error) {
    console.error('Backup failed:', error);
  }
}

// Run daily backup
backupWorkspace('123', 'your-jwt-token');
```

## Integration with No-Code Platforms

### n8n Workflow
Use n8n to create automated backup workflows:

1. **Schedule Trigger**: Set daily/weekly backup schedule
2. **HTTP Request**: Call Xano export API
3. **File Storage**: Save to Google Drive/Dropbox
4. **Notification**: Send backup confirmation via Slack/email

### Make.com Scenario
Create backup scenarios in Make.com:

1. **Webhook Trigger**: Manual or scheduled activation
2. **Xano Module**: Use HTTP module for export API
3. **Cloud Storage**: Automatically upload to cloud storage
4. **Monitoring**: Track backup success/failure

### WeWeb Integration
Build backup management interfaces in WeWeb:

1. **Backup Dashboard**: List recent backups
2. **Export Controls**: Trigger exports with custom parameters
3. **Restore Interface**: Manage import workflows
4. **Status Monitoring**: Track export/import progress

## Common Mistakes to Avoid

1. **Missing Authentication**: Always include proper JWT tokens with required scopes
2. **Forgetting Passwords**: Store export passwords securely - you'll need them for imports
3. **Branch Confusion**: Be explicit about which branch you're exporting
4. **Size Limitations**: Large workspaces may timeout - contact support for assistance
5. **Overwriting Data**: Import operations replace existing content - backup first!

## Pro Tips

1. **Version Control**: Include branch names and timestamps in export filenames
2. **Password Strategy**: Use date-based passwords for easy organization
3. **Staging Workflows**: Export from production, import to staging for testing
4. **Monitoring**: Set up alerts for backup failures in production systems
5. **Documentation**: Keep records of what each export contains
6. **Testing**: Regularly test your import process in development environments

## Response Formats

All export APIs return the workspace data as a binary file. Import APIs return detailed response objects showing the imported workspace structure including:

- Workspace metadata (id, name, description)
- Branch information
- Middleware configurations
- Default settings

## Security Best Practices

1. **Encrypt Exports**: Always use passwords for sensitive workspace data
2. **Secure Storage**: Store backup files in encrypted cloud storage
3. **Access Control**: Limit API tokens to minimum required scopes
4. **Audit Logging**: Track who performs exports/imports and when
5. **Regular Rotation**: Rotate API tokens and backup passwords regularly

The Workspace Import/Export API is essential for maintaining robust DevOps practices with Xano, enabling automated backups, environment management, and deployment workflows that scale with your application needs.