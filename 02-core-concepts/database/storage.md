---
title: "Database Storage - Monitor and Manage Your Data Space"
description: "Understand database storage limits, monitoring, and optimization in Xano. Learn to manage storage efficiently across different plans and scale your application."
category: database
subcategory: management
tags:
  - Storage
  - Database Size
  - Limits
  - Optimization
  - Monitoring
  - Performance
  - Scaling
difficulty: intermediate
reading_time: 10 minutes
last_updated: '2025-01-23'
prerequisites:
  - Active Xano workspace
  - Database with data
  - Understanding of plans
---

# Database Storage - Monitor and Manage Your Data Space

## 📋 **Quick Summary**

**What it does:** Database storage management helps you monitor how much space your data uses, understand your plan limits, and optimize storage to prevent hitting capacity limits.

**Why it matters:** Proper storage management ensures:
- Your app doesn't hit storage limits unexpectedly
- Performance remains optimal as data grows
- Costs stay predictable and manageable
- You can plan for scaling needs
- Data is stored efficiently

**Time to implement:** 15 minutes to audit, ongoing monitoring

---

## What You'll Learn

- Understanding storage limits by plan
- Monitoring current usage
- Calculating storage needs
- Optimization strategies
- Managing file storage
- Planning for growth
- Troubleshooting storage issues

## Storage Limits by Plan

### 💾 **Plan Comparison**

| Plan | Database Storage | File Storage | API Requests/mo |
|------|-----------------|--------------|-----------------|
| **Free** | 100 MB | 1 GB | 50,000 |
| **Starter** | 5 GB | 10 GB | 250,000 |
| **Launch** | 15 GB | 50 GB | 1,000,000 |
| **Scale** | 50 GB | 200 GB | 5,000,000 |
| **Enterprise** | Custom | Custom | Custom |

### 📊 **What Counts Toward Storage?**

**Database Storage includes:**
```yaml
Counted:
- All table data
- Indexes (10-30% overhead)
- System metadata
- Deleted records (until purged)
- Version history
- Cached query results

Not Counted:
- API code/logic
- Function definitions
- Backups (separate)
- Logs (separate)
```

**File Storage includes:**
```yaml
Counted:
- Uploaded images
- Documents (PDFs, etc.)
- Videos
- User avatars
- Generated files
- Temporary files (until cleaned)

Not Counted:
- External file URLs
- CDN cached files
- Deleted files (after purge)
```

## Monitoring Storage Usage

### 📈 **Check Current Usage**

1. **Access Instance Dashboard:**
   ```
   Settings → Instance → Storage
   ```

2. **View metrics:**
   ```yaml
   Database Usage:
   - Current: 2.3 GB
   - Limit: 5 GB
   - Percentage: 46%
   
   File Storage:
   - Current: 4.7 GB
   - Limit: 10 GB
   - Percentage: 47%
   ```

3. **Set up alerts:**
   ```yaml
   Alert Thresholds:
   - 75% - Warning email
   - 90% - Critical alert
   - 95% - Urgent notification
   ```

### 🔍 **Table-Level Analysis**

Identify storage hogs:

```sql
-- Largest tables query
SELECT 
  table_name,
  row_count,
  total_size_mb,
  index_size_mb
FROM table_statistics
ORDER BY total_size_mb DESC
LIMIT 10;
```

**Common large tables:**
```yaml
Audit Logs: Often largest
- Solution: Archive old logs
- Retention: 30-90 days

User Sessions: Grows quickly
- Solution: Clean expired
- Retention: 7-30 days

Activity Tracking: High volume
- Solution: Aggregate data
- Retention: As needed
```

## Calculating Storage Needs

### 📐 **Storage Calculator**

Estimate your requirements:

```yaml
Per Record Calculation:
1. Average text field: 50 bytes
2. Integer field: 4 bytes
3. Timestamp: 8 bytes
4. Boolean: 1 byte
5. JSON object: 100-1000 bytes
6. File reference: 100 bytes

Example User Table:
- id: 4 bytes
- email: 50 bytes
- name: 50 bytes
- created_at: 8 bytes
- profile_data: 500 bytes
- avatar_url: 100 bytes
Total per user: ~712 bytes

For 10,000 users:
712 × 10,000 = 7.12 MB
+ 30% index overhead = 9.25 MB
```

### 📊 **Growth Projection**

Plan for the future:

```yaml
Monthly Growth Rate: 20%
Current Size: 1 GB

Month 1: 1.2 GB
Month 3: 1.73 GB
Month 6: 3.0 GB
Month 12: 8.9 GB

Action Points:
- Month 4: Review optimization
- Month 8: Consider plan upgrade
- Month 10: Implement archiving
```

## Storage Optimization Strategies

### 🗜️ **Database Optimization**

1. **Remove unnecessary fields:**
   ```yaml
   Before:
   - full_response: JSON (2KB average)
   - debug_data: Text (1KB average)
   - temp_field: Various
   
   After:
   - Remove debug fields in production
   - Archive full_response after 30 days
   - Clean temp fields regularly
   
   Savings: 40-60% reduction
   ```

2. **Use appropriate field types:**
   ```yaml
   Wrong:
   - age: Text ("25") - 2-3 bytes
   - status: Text ("active") - 6 bytes
   - count: Text ("1000") - 4 bytes
   
   Right:
   - age: Integer (25) - 1 byte
   - status: Enum - 1 byte
   - count: Integer - 2 bytes
   
   Savings: 70% reduction
   ```

3. **Archive old data:**
   ```javascript
   // Archive strategy
   1. Identify old records:
      - Orders > 1 year
      - Logs > 90 days
      - Sessions > 30 days
   
   2. Export to CSV/backup
   3. Delete from main table
   4. Store backup externally
   ```

### 📁 **File Storage Optimization**

1. **Image optimization:**
   ```yaml
   Before Upload:
   - Resize to max needed dimensions
   - Compress (80% quality often enough)
   - Convert to WebP format
   
   Example Savings:
   Original: 5MB JPEG
   Optimized: 200KB WebP
   Savings: 96% reduction
   ```

2. **File lifecycle management:**
   ```yaml
   Temporary Files:
   - Delete after processing
   - Set TTL (time-to-live)
   - Regular cleanup job
   
   User Files:
   - Limit upload sizes
   - Enforce quotas per user
   - Remove orphaned files
   ```

3. **External storage:**
   ```yaml
   Use External Services for:
   - Large videos → YouTube/Vimeo
   - Documents → Google Drive
   - Images → Cloudinary/S3
   
   Store in Xano:
   - Only URLs/references
   - Metadata
   - Thumbnails
   ```

## Clean-Up Strategies

### 🧹 **Automated Cleanup**

Create background tasks:

```javascript
// Daily cleanup task
1. Delete expired sessions
2. Remove orphaned files
3. Purge old logs
4. Clean temporary tables

// Weekly cleanup
1. Archive old records
2. Optimize tables (VACUUM)
3. Rebuild indexes
4. Generate storage report
```

### 🗑️ **Soft Delete Strategy**

Implement soft deletes wisely:

```yaml
Soft Delete Benefits:
- Data recovery possible
- Audit trail maintained
- Relationships preserved

Storage Impact:
- Records remain in database
- Storage not freed
- Indexes still include them

Best Practice:
1. Soft delete initially
2. Hard delete after 30 days
3. Archive if needed for compliance
```

## Integration Considerations

### 🔧 **n8n Storage Workflows**

Automate storage management:

```javascript
// n8n workflow for storage monitoring
1. Schedule: Daily at 2 AM
2. Xano API: Get storage metrics
3. Condition: If usage > 80%
4. Actions:
   - Run cleanup task
   - Send alert email
   - Log to monitoring system
```

### 🌐 **WeWeb File Handling**

Optimize frontend uploads:

```yaml
WeWeb Upload Settings:
- Max file size: 5MB
- Allowed types: images only
- Client-side compression: enabled
- Progress indicator: show

Before Upload Hook:
- Validate file size
- Check user quota
- Compress if needed
- Generate thumbnail
```

## Monitoring Best Practices

### 📊 **Storage Dashboard**

Create monitoring API:

```javascript
// Storage metrics endpoint
{
  database: {
    used_mb: 2340,
    limit_mb: 5120,
    percentage: 45.7,
    largest_tables: [
      {name: "logs", size_mb: 890},
      {name: "users", size_mb: 456}
    ]
  },
  files: {
    used_gb: 4.7,
    limit_gb: 10,
    percentage: 47,
    file_count: 12453
  },
  trends: {
    daily_growth_mb: 45,
    projected_full_date: "2024-06-15"
  }
}
```

### 🚨 **Alert Thresholds**

Set up progressive alerts:

```yaml
50% Usage:
- Type: Information
- Action: Log only
- Frequency: Weekly

75% Usage:
- Type: Warning
- Action: Email team
- Frequency: Daily

90% Usage:
- Type: Critical
- Action: Page on-call
- Frequency: Hourly

95% Usage:
- Type: Emergency
- Action: Auto-cleanup + escalate
- Frequency: Every 15 min
```

## Scaling Strategies

### 📈 **When to Upgrade**

Signs you need more storage:

```yaml
Indicators:
✓ Consistently above 70% usage
✓ Monthly growth > 10%
✓ Cleanup barely helps
✓ Performance degradation
✓ Feature limitations

Upgrade Timeline:
1. Monitor for 2 weeks
2. Project 3-month growth
3. Plan upgrade if needed
4. Schedule during low traffic
```

### 🎯 **Optimization vs. Upgrade**

Decision matrix:

| Situation | Optimize | Upgrade |
|-----------|----------|---------|
| Old data accumulation | ✅ | ❌ |
| Rapid user growth | ❌ | ✅ |
| Inefficient schemas | ✅ | ❌ |
| Large file uploads | ✅ | ✅ |
| Temporary spike | ✅ | ❌ |
| Consistent growth | ❌ | ✅ |

## Try This: Storage Audit

### 📝 **Exercise: Analyze Your Storage**

1. **Check current usage:**
   ```
   Settings → Instance → Storage
   Note all percentages
   ```

2. **Identify largest tables:**
   ```sql
   Query table sizes
   List top 5 consumers
   ```

3. **Calculate growth rate:**
   ```
   Compare this month vs. last
   Project next 3 months
   ```

4. **Create cleanup plan:**
   ```yaml
   Immediate: Delete obvious waste
   This week: Archive old data
   This month: Optimize schemas
   ```

## Common Issues

### 🔍 **"Storage full" errors**
- Run immediate cleanup
- Archive old data
- Delete unused files
- Contact support if critical

### 🔍 **"Slow queries" with high storage**
- Indexes may be fragmented
- Run VACUUM/ANALYZE
- Consider archiving
- Optimize query patterns

### 🔍 **"Can't delete files"**
- Check for references
- Clear CDN cache
- Verify permissions
- Use force delete if safe

## Next Steps

After optimizing storage:

1. **Set up monitoring** dashboard
2. **Create cleanup** automations
3. **Document retention** policies
4. **Plan scaling** strategy
5. **Optimize uploads** in frontend
6. **Review monthly** usage trends

## Related Documentation

- [Database Maintenance](./database-maintenance.md)
- [File Storage](../../features/file-storage.md)
- [Performance Optimization](./indexing.md)
- [Backup and Restore](../../features/backup-restore.md)
- [Plan Limits](../../pricing/plan-limits.md)