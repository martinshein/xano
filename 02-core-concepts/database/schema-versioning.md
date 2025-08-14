---
title: "Schema Versioning - Track and Rollback Database Changes"
description: "Master Xano's schema versioning to track database changes, compare versions, and rollback mistakes. Essential for safe development and team collaboration."
category: database
subcategory: management
tags:
  - Schema Versioning
  - Version Control
  - Rollback
  - Database History
  - Team Collaboration
  - Change Tracking
  - Backup
difficulty: intermediate
reading_time: 8 minutes
last_updated: '2025-01-23'
prerequisites:
  - Starter plan or higher
  - Database tables created
  - Basic understanding of schemas
---

# Schema Versioning - Track and Rollback Database Changes

## 📋 **Quick Summary**

**What it does:** Schema versioning automatically saves snapshots of your database structure and API configurations every time you make changes, allowing you to view history, compare versions, and rollback mistakes instantly.

**Why it matters:** Version control provides:
- Instant rollback when something breaks
- See who changed what and when
- Compare differences between versions
- Test changes safely knowing you can revert
- Team accountability and transparency

**Time to implement:** Automatic - no setup required!

---

## What You'll Learn

- How schema versioning works in Xano
- Tracking database and API changes
- Comparing version differences
- Rolling back to previous versions
- Best practices for team collaboration
- Version management strategies

## Understanding Schema Versioning

### 🔄 **What Gets Versioned?**

Xano automatically versions these elements:

```yaml
Database:
- Table structure (fields, types)
- Indexes
- Views
- Relationships

APIs:
- Endpoint configurations
- Function stacks
- Input/output definitions
- Authentication settings

Other Elements:
- Background tasks
- Custom functions
- Addons
- Scheduled tasks
```

### 💡 **Real-World Scenarios**

**Without versioning (risky):**
```
Monday: Add new field to users table
Tuesday: Field breaks production
Wednesday: Manually recreate old structure
Thursday: Still fixing related issues
Result: 3 days of downtime
```

**With versioning (safe):**
```
Monday: Add new field to users table
Tuesday: Field breaks production
Tuesday (5 min later): Rollback to previous version
Result: 5 minutes of issues, instantly fixed
```

## Accessing Version History

### 📂 **Step 1: Open Version History**

For any versioned element:

1. **Click the menu icon (⋮)**
2. **Select "Versions"**
3. **Version panel opens**

```yaml
Version Panel Shows:
- Active version (current)
- Previous versions list
- Timestamp of each change
- Who made the change
- Version notes (if added)
```

### 👁️ **Step 2: View Version Details**

Each version displays:

```yaml
Database Tables:
- Number of fields
- Index count
- View configuration

API Endpoints:
- Input count
- Function count
- Output structure

Background Tasks:
- Function count
- Schedule settings
```

## Comparing Versions

### 🔍 **Visual Comparison**

Click any previous version to see differences:

```yaml
Comparison View:
Left Side: Selected old version
Right Side: Current active version

Color Coding:
🟢 Green: Added in current version
🔴 Red: Removed from old version
🟡 Yellow: Modified between versions
⚪ Gray: Unchanged elements
```

### 📊 **Database Comparisons**

See what changed in your tables:

**Schema Changes:**
```diff
Version #2 (Old):
- id: integer
- name: text
- email: text

Version #4 (Current):
- id: integer
- name: text
- email: text
+ phone: text (Added)
+ status: enum (Added)
- temp_field: text (Removed)
```

**Index Changes:**
```diff
Version #2:
- idx_email

Version #4:
- idx_email
+ idx_status (Added)
+ idx_phone (Added)
```

### 🔧 **API Comparisons**

Track function stack evolution:

**Function Changes:**
```diff
Version #1:
1. Get Record
2. Return

Version #3:
1. Get Record
+ 2. Validate Permissions (Added)
+ 3. Log Activity (Added)
4. Return
```

## Rolling Back Changes

### ⏮️ **Rollback Process**

1. **Select target version** from history
2. **Review differences** carefully
3. **Click "Revert to this version"**
4. **Confirm rollback**
5. **Version restored instantly**

### ⚠️ **Important Considerations**

**Before rolling back:**
```yaml
Check for:
- Dependent APIs using changed fields
- Active integrations (n8n, WeWeb)
- Data that uses new fields
- Team members' work affected
```

**Data preservation:**
- Structure changes revert
- Existing data remains
- New fields become inaccessible
- Old fields restore (structure only)

## Team Collaboration

### 👥 **Tracking Team Changes**

Version history shows:
```yaml
Change Log Entry:
- Version: #5
- Date: Jan 15, 2024 3:45 PM
- Author: john@company.com
- Changes: Added 2 fields, 1 index
- Note: "Added phone verification fields"
```

### 📝 **Adding Version Notes**

Best practice for team clarity:

```yaml
Good Notes:
✅ "Added user preferences table for settings feature"
✅ "Fixed email field type - was integer, now text"
✅ "Temporary debug fields - remove after testing"

Bad Notes:
❌ "Changed stuff"
❌ "Test"
❌ (No note)
```

## Version Management Strategies

### 🎯 **Development Workflow**

```yaml
1. Before Major Changes:
   - Note current version number
   - Document what you're changing
   - Alert team members

2. During Development:
   - Make incremental changes
   - Test after each change
   - Version automatically saves

3. If Issues Arise:
   - Check version history
   - Compare with last working version
   - Rollback if needed

4. After Successful Changes:
   - Add descriptive note
   - Notify team of changes
   - Document in project notes
```

### 🔄 **Testing Strategy**

Use versions for safe testing:

```yaml
Safe Testing Pattern:
1. Note current version (#10)
2. Make experimental changes
3. Test thoroughly
4. If successful: Keep changes
5. If failed: Rollback to #10
```

## Integration Considerations

### 🔧 **n8n Workflows**

Before rolling back database changes:

```javascript
// Check n8n workflows using the table
1. List all workflows using the API
2. Check field mappings
3. Test after rollback
4. Update workflows if needed
```

### 🌐 **WeWeb Collections**

Protect your frontend:

```yaml
Before Rollback:
1. Check WeWeb collections using table
2. Note field bindings
3. Prepare update plan

After Rollback:
1. Refresh collections
2. Fix broken bindings
3. Test all features
```

## Best Practices

### ✅ **Do's**

1. **Review changes** before reverting
   ```yaml
   Always:
   - Check differences
   - Understand impact
   - Notify team
   ```

2. **Add meaningful notes**
   ```yaml
   Include:
   - What changed
   - Why it changed
   - Related ticket/issue
   ```

3. **Coordinate with team**
   ```yaml
   Communicate:
   - Before major changes
   - After rollbacks
   - During testing
   ```

4. **Use for testing**
   ```yaml
   Version Control Enables:
   - Safe experimentation
   - Quick recovery
   - A/B testing structures
   ```

### ❌ **Don'ts**

1. **Don't rollback blindly**
   - Check active users first
   - Verify data compatibility
   - Test integrations

2. **Don't skip notes**
   - Future you needs context
   - Team needs understanding
   - Debugging needs history

3. **Don't panic rollback**
   - Assess the issue first
   - Sometimes forward fix is better
   - Consider data implications

## Common Scenarios

### 🔧 **Scenario: Accidental Field Deletion**

```yaml
Problem: Deleted important field
Solution:
1. Open version history
2. Find version before deletion
3. Compare to confirm
4. Rollback
5. Field structure restored
Note: Field data may need separate restoration
```

### 🐛 **Scenario: API Breaking Change**

```yaml
Problem: API change broke mobile app
Solution:
1. Identify when it broke (version #)
2. Compare working vs. broken version
3. Rollback API endpoint only
4. Fix issue in development
5. Reapply when ready
```

### 👥 **Scenario: Team Conflict**

```yaml
Problem: Two developers changed same table
Solution:
1. Review version history
2. See both changes chronologically
3. Discuss best approach
4. Merge changes manually
5. Document decision in notes
```

## Version Limits

### 📊 **Storage Limits by Plan**

| Plan | Version History |
|------|----------------|
| Free | Not available |
| Starter | 30 days |
| Launch | 90 days |
| Scale | 180 days |
| Enterprise | Unlimited |

### 🧹 **Automatic Cleanup**

```yaml
Xano automatically:
- Keeps recent versions based on plan
- Removes old versions after limit
- Preserves current active version
- Maintains smooth performance
```

## Try This: Version Control Exercise

### 📝 **Practice Safe Changes**

1. **Create test table:**
   ```yaml
   Table: version_test
   Fields:
   - id: integer
   - name: text
   ```

2. **Make changes:**
   - Add field: `email: text`
   - Add index on email
   - Save and note version

3. **Make more changes:**
   - Add field: `phone: text`
   - Remove name field
   - Save and note version

4. **Practice rollback:**
   - Open version history
   - Compare versions
   - Rollback to original
   - Verify structure restored

## Troubleshooting

### 🔍 **"Can't see version history"**
- Check you're on Starter plan or higher
- Refresh your browser
- Check permissions if team member

### 🔍 **"Rollback didn't restore my data"**
- Versioning tracks structure, not data
- Use backups for data restoration
- Check deleted_at for soft deletes

### 🔍 **"Version history is missing"**
- Versions older than plan limit are removed
- Current version always preserved
- Upgrade plan for longer history

## Next Steps

With schema versioning mastered:

1. **Establish team protocols** for changes
2. **Document major versions** externally
3. **Create backup strategy** for data
4. **Test rollback procedures** regularly
5. **Train team** on version management
6. **Monitor version** usage patterns

## Related Documentation

- [Database Basics](./database-basics.md)
- [Backup and Restore](../../features/backup-restore.md)
- [Team Collaboration](../../collaboration/team-management.md)
- [Change Management](../../best-practices/change-management.md)
- [API Versioning](../api-endpoints/api-versioning.md)