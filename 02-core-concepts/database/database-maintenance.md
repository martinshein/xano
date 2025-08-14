---
title: "Database Maintenance - Optimize Performance with ANALYZE and VACUUM"
description: "Learn how to maintain optimal database performance in Xano using ANALYZE and VACUUM commands. Understand automatic maintenance and when to run manual optimization."
category: database
subcategory: performance
tags:
  - Database Maintenance
  - Performance
  - ANALYZE
  - VACUUM
  - Optimization
  - PostgreSQL
  - Best Practices
difficulty: intermediate
reading_time: 8 minutes
last_updated: '2025-01-23'
prerequisites:
  - Xano workspace with data
  - Basic understanding of databases
  - Tables with significant data volume
---

# Database Maintenance - Optimize Performance with ANALYZE and VACUUM

## 📋 **Quick Summary**

**What it does:** Database maintenance tools (ANALYZE and VACUUM) keep your database running efficiently by updating statistics and reclaiming storage space from deleted records.

**Why it matters:** Proper maintenance ensures:
- Faster query performance (up to 10x improvement)
- Efficient storage usage (reclaim wasted space)
- Accurate query planning
- Prevention of database bloat
- Consistent application performance

**Time to implement:** 5-30 minutes depending on database size

---

## What You'll Learn

- Understanding ANALYZE and VACUUM operations
- When automatic maintenance runs
- How to run manual maintenance
- Identifying when maintenance is needed
- Best practices for database optimization
- Integration impact and timing

## Understanding Database Maintenance

Think of your database like a library. Over time, books get moved around, some get removed, and the card catalog needs updating. Database maintenance is like reorganizing the library and updating the catalog system.

### 💡 **What This Means for You**

- **Automatic daily maintenance:** Xano handles most maintenance for you
- **Manual control available:** Run maintenance when you need it
- **No downtime required:** Maintenance runs while your app stays online
- **Performance improvements:** Queries run faster after maintenance
- **Space recovery:** Deleted data space gets reclaimed

## Automatic Maintenance

### 🤖 **What Xano Does Automatically**

Xano runs maintenance tasks daily during low-traffic periods:

**Daily Operations:**
- ANALYZE on frequently modified tables
- Light VACUUM on active tables
- Statistics updates for query optimization
- Transaction log cleanup

**When it runs:**
- Typically between 2-4 AM (server timezone)
- During lowest traffic periods
- Automatically adjusts to your usage patterns

**What's covered:**
- All active tables
- Indexes
- System catalogs
- Temporary data cleanup

## Manual Maintenance Tools

### 📊 **ANALYZE Operation**

**What ANALYZE does:**
- Gathers statistics about data distribution
- Updates the query planner's knowledge
- Improves query execution plans
- Optimizes index usage

**Think of it like:** Taking inventory in a warehouse - you're counting what's where so you can find things faster.

#### When to Run ANALYZE Manually:

1. **After bulk data imports**
   ```
   Imported 100,000+ records? Run ANALYZE
   ```

2. **After major data changes**
   ```
   Deleted 50% of your data? Run ANALYZE
   ```

3. **Query performance degrades**
   ```
   Queries suddenly slower? Run ANALYZE
   ```

4. **Before launching features**
   ```
   New feature with complex queries? Run ANALYZE
   ```

### 🧹 **VACUUM Operation**

**What VACUUM does:**
- Reclaims storage from deleted rows
- Removes dead tuples (deleted data)
- Prevents table bloat
- Frees up disk space
- Updates visibility map

**Think of it like:** Emptying the recycling bin on your computer - the files are gone but space isn't freed until you empty the bin.

#### Types of VACUUM:

**1. Standard VACUUM**
- Reclaims space within tables
- Doesn't lock tables
- Safe to run anytime
- Takes 5-30 minutes typically

**2. VACUUM FULL**
- Completely rewrites tables
- Reclaims all wasted space
- Requires brief table locks
- Use sparingly (monthly/quarterly)

#### When to Run VACUUM Manually:

1. **After mass deletions**
   ```
   Deleted old records? Run VACUUM
   ```

2. **Table bloat detected**
   ```
   Table size not shrinking after deletes? Run VACUUM
   ```

3. **Disk space concerns**
   ```
   Running low on storage? Run VACUUM
   ```

4. **Performance issues**
   ```
   Slow inserts/updates? Run VACUUM
   ```

## How to Run Manual Maintenance

### 📍 **Accessing Maintenance Panel**

1. Navigate to your Instance Settings
2. Find "Instance Maintenance" section
3. Select maintenance operation
4. Choose tables (or all)
5. Execute maintenance

### 🎯 **Step-by-Step Process**

#### Running ANALYZE:

1. **Open Instance Maintenance**
2. **Select "ANALYZE"**
3. **Choose scope:**
   - All tables
   - Specific tables
   - Most active tables
4. **Click "Run ANALYZE"**
5. **Monitor progress**
   - Small tables: Seconds
   - Large tables: Minutes

#### Running VACUUM:

1. **Open Instance Maintenance**
2. **Select "VACUUM"**
3. **Choose type:**
   - Standard VACUUM (recommended)
   - VACUUM FULL (use carefully)
4. **Select tables**
5. **Click "Run VACUUM"**
6. **Wait for completion**

### ⏱️ **Execution Time Estimates**

| Table Size | ANALYZE Time | VACUUM Time | VACUUM FULL Time |
|------------|--------------|-------------|------------------|
| < 1,000 records | < 1 second | < 1 second | < 5 seconds |
| 10,000 records | 1-5 seconds | 5-10 seconds | 30 seconds |
| 100,000 records | 10-30 seconds | 1-2 minutes | 5-10 minutes |
| 1M records | 1-2 minutes | 5-10 minutes | 30-60 minutes |
| 10M+ records | 5-10 minutes | 20-30 minutes | 2+ hours |

## Identifying Maintenance Needs

### 🔍 **Signs You Need ANALYZE**

1. **Query performance degradation**
   - Queries taking longer than usual
   - Different execution plans
   - Index not being used

2. **After significant data changes**
   - Bulk imports/updates
   - Mass deletions
   - Schema modifications

3. **Statistics outdated**
   - Query planner making poor choices
   - Full table scans instead of index scans

### 🔍 **Signs You Need VACUUM**

1. **Table bloat indicators**
   - Table size not decreasing after deletes
   - Slow INSERT performance
   - High disk usage

2. **Dead tuple accumulation**
   - Many UPDATE operations
   - Frequent DELETE operations
   - High transaction volume

3. **Performance symptoms**
   - Slower sequential scans
   - Increased I/O operations
   - Memory usage climbing

## Best Practices

### ✅ **Do's**

1. **Schedule during low traffic**
   ```
   Run maintenance during off-peak hours
   ```

2. **Start with ANALYZE**
   ```
   ANALYZE is faster and often solves issues
   ```

3. **Monitor regularly**
   ```
   Check performance weekly
   ```

4. **Document maintenance**
   ```
   Log when and why you run maintenance
   ```

5. **Test in development first**
   ```
   Try maintenance on test data source
   ```

### ❌ **Don'ts**

1. **Don't run VACUUM FULL frequently**
   ```
   Monthly at most, it locks tables
   ```

2. **Don't ignore automatic maintenance**
   ```
   Daily automation handles most needs
   ```

3. **Don't run during peak hours**
   ```
   Can impact performance temporarily
   ```

4. **Don't panic about minor bloat**
   ```
   Some bloat is normal and acceptable
   ```

## Integration Considerations

### 🔧 **n8n Workflows**

When running maintenance:
```javascript
// Add retry logic for maintenance windows
{
  retryOnFail: true,
  maxRetries: 3,
  waitBetweenRetries: 5000
}
```

### 🌐 **WeWeb Applications**

During maintenance:
- Read operations continue normally
- Brief delays possible on writes
- Add loading states for better UX

## Monitoring and Metrics

### 📊 **Key Metrics to Track**

1. **Query execution time**
   - Before/after maintenance
   - Trending over time

2. **Table sizes**
   - Physical size vs row count
   - Growth patterns

3. **Dead tuple ratio**
   - Dead rows / total rows
   - Should stay below 20%

4. **Index usage**
   - Which indexes are used
   - Scan types (sequential vs index)

## Try This: Maintenance Checklist

**Weekly Tasks:**
- [ ] Check query performance trends
- [ ] Monitor table sizes
- [ ] Review slow query logs

**Monthly Tasks:**
- [ ] Run ANALYZE on all tables
- [ ] VACUUM high-activity tables
- [ ] Review disk usage

**Quarterly Tasks:**
- [ ] Consider VACUUM FULL for bloated tables
- [ ] Review and optimize indexes
- [ ] Audit maintenance schedule

**After Major Changes:**
- [ ] Run ANALYZE immediately
- [ ] VACUUM affected tables
- [ ] Test query performance

## Troubleshooting

### "Queries suddenly slow"
1. Run ANALYZE first
2. Check for missing indexes
3. Run VACUUM if needed

### "Disk space not freed after deletes"
1. Run standard VACUUM
2. If space critical, schedule VACUUM FULL
3. Check for long-running transactions

### "Maintenance taking too long"
1. Run on specific tables, not all
2. Break into smaller batches
3. Schedule during lowest traffic

## Next Steps

After understanding maintenance:
1. Set up monitoring for your tables
2. Create maintenance schedule
3. Document your procedures
4. Train team on when to run maintenance
5. Automate alerts for performance issues

## Related Documentation

- [Database Performance](./database-performance-and-maintenance.md)
- [Indexing Strategy](./indexing.md)
- [Query Optimization](../function-stack/query-all-records.md)
- [Storage Management](./storage.md)