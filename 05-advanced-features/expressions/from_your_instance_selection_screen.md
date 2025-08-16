---
title: "Backup and Restore in Xano"
description: "Learn how to create, restore, and manage backups of your Xano instance data for disaster recovery and development workflows"
category: expressions
has_code_examples: false
last_updated: '2025-01-16'
tags:
  - backup
  - restore
  - instance-management
  - data-protection
  - disaster-recovery
---

# Backup and Restore in Xano

## 📋 **Quick Summary**

Xano provides automated and manual backup capabilities for paid plans, allowing you to protect your data and restore to earlier points in time. This is essential for disaster recovery, testing scenarios, and maintaining multiple environment states.

## What You'll Learn

- How Xano's automatic backup system works
- Step-by-step manual backup creation process
- Restore procedures and best practices
- Backup policy customization options
- When to include media storage in backups
- Integration strategies for development workflows

## Understanding Xano Backups

Xano maintains different backup capabilities based on your plan:

**Free Plans:**
- No backup functionality available
- Recommend upgrading for production use

**Paid Plans:**
- Automatic rolling 3-day backups
- Manual backup creation
- Custom backup scheduling
- Media storage inclusion options

**What's Included in Backups:**
- Complete database schema and data
- API configurations and endpoints
- Custom functions and workflows
- Workspace settings and permissions
- Optional: Media files and attachments

## Creating Manual Backups

Manual backups give you control over when to preserve your instance state, perfect for before major changes or deployments.

### Step-by-Step Process

1. **Access Instance Settings**
   - Navigate to your instance selection screen
   - Click the settings icon (⚙️) next to your target instance

2. **Open Database Backup Panel**
   - In the settings panel, choose "Database Backup"

3. **Start Manual Backup**
   - Click "Manual Backup" button

4. **Configure Media Storage (Optional)**
   - Check the option to include media storage if needed
   - **Warning**: Media backups significantly increase backup size and time

5. **Execute Backup**
   - Click the backup button to start the process
   - Wait for completion confirmation

## Try This: Pre-Deployment Backup

Create a backup before making significant changes:

```markdown
# Pre-Deployment Checklist

1. Navigate to instance settings
2. Access Database Backup panel
3. Create manual backup with timestamp naming
4. Document what changes you're about to make
5. Proceed with deployment
6. Test thoroughly
7. Keep backup available for 24 hours post-deployment
```

## Restoring from Backups

Restoration allows you to revert your instance to a previous state, useful for recovering from issues or testing scenarios.

### Before You Restore

**⚠️ CRITICAL WARNING**: Always create a current backup before restoring another backup. This creates a safety net if you need to revert the restoration.

### Restoration Process

1. **Create Safety Backup**
   - Follow manual backup steps above
   - Wait for completion before proceeding

2. **Access Restore Interface**
   - Go to instance settings (⚙️ icon)
   - Choose "Database Backup" panel

3. **Select Restore Option**
   - Click "Download and Restore"

4. **Choose Backup**
   - Select the backup you want to restore from the list
   - Click the restore button to proceed

5. **Confirm and Wait**
   - Confirm the restoration action
   - Monitor progress until completion

## Custom Backup Policies

Customize when automatic backups occur to align with your workflow and minimize performance impact.

### Setting Custom Schedule

1. **Access Backup Policy**
   - Navigate to instance settings
   - Open "Database Backup" panel

2. **Configure Policy**
   - Click "Policy" option

3. **Set Time Window**
   - Choose your preferred backup time window
   - Default: Early morning PST hours
   - Customize to match your low-traffic periods

### Best Practice Timing

- **Low Traffic Hours**: Schedule during minimal user activity
- **Pre-Change Windows**: Before regular development cycles
- **Geographic Considerations**: Account for your user base timezone
- **Frequency Balance**: More frequent for active development, less for stable production

## Integration with Development Workflows

### Staging Environment Strategy

Use backups to maintain consistent staging environments:

1. **Production Backup**: Create backup of production data
2. **Staging Restore**: Restore backup to staging instance
3. **Testing Phase**: Run tests against production-like data
4. **Development**: Make changes in safe environment

### Version Control Integration

Coordinate backups with code deployments:

```markdown
# Deployment Workflow with Backups

## Pre-Deployment
1. Create manual backup with version tag
2. Document current feature state
3. Prepare rollback plan

## Deployment
1. Deploy code changes
2. Test functionality
3. Monitor for issues

## Post-Deployment
1. Create post-deployment backup if successful
2. Keep pre-deployment backup for 48 hours
3. Document any issues or rollback needs
```

### Team Collaboration

Establish backup protocols for team environments:

- **Daily Backups**: For active development phases
- **Feature Backups**: Before starting major features
- **Release Backups**: Before and after each release
- **Emergency Backups**: When debugging production issues

## Integration with No-Code Platforms

### n8n Backup Automation

Create automated backup workflows:

1. **Schedule Node**: Daily/weekly backup triggers
2. **Webhook Node**: Manual backup endpoints
3. **Notification Node**: Backup completion alerts
4. **File Storage**: Archive backups to cloud storage

### Make.com Scenarios

Build backup monitoring scenarios:

1. **Time Trigger**: Scheduled backup checks
2. **HTTP Module**: Verify backup completion
3. **Slack Module**: Team notifications
4. **Google Drive**: Backup status tracking

### WeWeb Backup Dashboard

Create backup management interfaces:

1. **Backup Status**: Show last backup time
2. **Manual Triggers**: Buttons for immediate backups
3. **Restore Interface**: Guided restoration process
4. **Schedule Management**: Backup policy configuration

## Common Mistakes to Avoid

1. **Forgetting Safety Backups**: Always backup current state before restoring
2. **Media Storage Oversights**: Consider backup size and time implications
3. **Schedule Conflicts**: Avoid backup times during high traffic
4. **Documentation Gaps**: Keep records of what each backup contains
5. **Testing Neglect**: Regularly test your restore process

## Pro Tips

1. **Naming Conventions**: Use descriptive names with timestamps and version info
2. **Regular Testing**: Practice restore procedures in development
3. **Storage Planning**: Monitor backup storage usage and retention
4. **Team Communication**: Notify team members of backup/restore activities
5. **Automation Balance**: Mix automatic and manual backups for optimal coverage
6. **Performance Monitoring**: Track backup completion times and optimize schedules

## Backup Size Considerations

### Database-Only Backups
- Fastest backup and restore times
- Smallest file sizes
- Recommended for frequent backups
- Ideal for development workflows

### Media-Inclusive Backups
- Significantly larger file sizes
- Longer backup and restore times
- Essential for complete disaster recovery
- Use sparingly and strategically

## Troubleshooting Common Issues

### Backup Failures
- Check instance storage limits
- Verify backup permissions
- Monitor during low-activity periods
- Contact support for large workspaces

### Restore Problems
- Ensure sufficient storage space
- Verify backup file integrity
- Check restoration permissions
- Allow adequate time for completion

### Performance Impact
- Schedule during off-peak hours
- Monitor server performance during backups
- Consider splitting large backups
- Optimize media storage inclusion

Xano's backup and restore system provides robust data protection capabilities essential for production applications. By implementing proper backup strategies and procedures, you can maintain data integrity while supporting agile development and deployment workflows.