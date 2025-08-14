---
title: "Database Views - Save and Share Custom Data Views"
description: "Learn how to create, save, and share customized database views with filters, sorting, and column selection. Perfect for organizing data and team collaboration."
category: database
subcategory: organization
tags:
  - Database Views
  - Filters
  - Sorting
  - Data Organization
  - Collaboration
  - Search
  - Productivity
difficulty: beginner
reading_time: 7 minutes
last_updated: '2025-01-23'
prerequisites:
  - Xano workspace with data
  - Basic understanding of filtering
---

# Database Views - Save and Share Custom Data Views

## 📋 **Quick Summary**

**What it does:** Database Views save your custom combinations of filters, sorting, searches, and column visibility so you can instantly return to specific data views without recreating them every time.

**Why it matters:** Views enable you to:
- Save time by not recreating complex filters
- Share specific data perspectives with team members
- Organize data for different use cases
- Create role-specific data access
- Export filtered data consistently

**Time to implement:** 2 minutes to create a view

---

## What You'll Learn

- Understanding database views vs. tables
- Creating and managing custom views
- Applying filters and sorting
- Sharing views with team members
- Best practices for view organization
- Common view patterns for different use cases

## Understanding Database Views

### 🔍 **What are Database Views?**

Think of database views like saved searches or bookmarks for your data. Just as you might bookmark a filtered product search on Amazon, database views save your exact data configuration.

**Real-world analogy:**
```
Your Email Inbox:
├── All Mail (full table)
├── Unread (filtered view)
├── Important (filtered view)
├── From Boss (filtered view)
└── This Week (filtered view)
```

### 💡 **What This Means for You**

- **No more repetitive filtering:** Save complex filters once, use forever
- **Team consistency:** Everyone sees the same filtered data
- **Quick switching:** Jump between perspectives instantly
- **Safe exploration:** Views don't modify actual data
- **Export ready:** Export the exact view you need

## Views vs. Tables

### 📊 **Key Differences**

| Aspect | Table | View |
|--------|-------|------|
| **What it is** | Actual data storage | Saved filter/sort settings |
| **Data** | Contains real records | Shows filtered table data |
| **Modification** | Changes affect data | Changes affect display only |
| **Storage** | Takes database space | Just saves settings |
| **Purpose** | Store information | Organize information |
| **Sharing** | Shares all data | Shares specific perspective |

### 🎯 **When to Use Views**

**Use Views for:**
- Frequently accessed filters
- Team-specific data subsets
- Report generation
- Data validation workflows
- Client-specific data

**Don't Use Views for:**
- Permanent data separation (use tables)
- Security (use proper permissions)
- Data backup (use exports)

## Creating Database Views

### 🛠️ **Step-by-Step Process**

#### Step 1: Apply Your Filters

1. **Open your table**
2. **Add filters:**
   ```
   status = "active"
   created_at >= "2024-01-01"
   amount > 100
   ```

3. **Set sorting:**
   ```
   Sort by: created_at (Newest first)
   ```

4. **Hide columns:**
   - Uncheck internal fields
   - Show only relevant data

5. **Search if needed:**
   ```
   Search: "premium"
   ```

#### Step 2: Save as View

1. **Click "Save View" button**
2. **Name your view clearly:**
   ```
   Good names:
   - "Active Premium Customers"
   - "January 2024 Orders"
   - "Pending Approvals"
   - "High-Value Transactions"
   
   Bad names:
   - "View 1"
   - "Test"
   - "John's View"
   ```

3. **Add description (optional):**
   ```
   "Shows all active premium customers 
   who joined after Jan 1, 2024"
   ```

4. **Click "Create View"**

### 🎨 **View Configuration Options**

**Filters:**
- Multiple conditions (AND/OR)
- Comparison operators
- Date ranges
- Text searches
- Null checks

**Sorting:**
- Single or multiple columns
- Ascending/descending
- Custom sort orders

**Column Visibility:**
- Show/hide specific fields
- Reorder columns
- Adjust column widths

**Search:**
- Full-text search
- Specific field search
- Case sensitivity options

## Managing Views

### 📁 **View Organization**

**Naming Convention:**
```
[Status/Type] - [Criteria] - [Purpose]

Examples:
"Active - Premium Users - Marketing"
"Pending - Orders > $1000 - Review"
"Archive - 2023 Q4 - Reporting"
```

**Categorization:**
```
Operations Views:
├── Daily - New Signups
├── Daily - Pending Orders
└── Daily - Support Tickets

Reporting Views:
├── Monthly - Revenue Report
├── Monthly - User Growth
└── Monthly - Churn Analysis

Client Views:
├── Client A - All Data
├── Client B - All Data
└── Client C - All Data
```

### ✏️ **Editing Views**

1. **Load the view**
2. **Modify filters/sorting**
3. **Click "Update View"**
4. **Or "Save as New" for variation**

### 🗑️ **Deleting Views**

1. **Select view from dropdown**
2. **Click view options (⋮)**
3. **Select "Delete View"**
4. **Confirm deletion**

**Note:** Deleting a view doesn't delete any data!

## Common View Patterns

### 📊 **Status-Based Views**

```yaml
Active Records:
  Filter: status = "active"
  Sort: name ASC
  Use: Daily operations

Pending Review:
  Filter: status = "pending"
  Sort: created_at DESC
  Use: Approval workflows

Archived:
  Filter: status = "archived"
  Sort: archived_at DESC
  Use: Historical reference
```

### 📅 **Time-Based Views**

```yaml
Today's Activity:
  Filter: created_at = TODAY()
  Sort: created_at DESC
  Use: Daily monitoring

This Week:
  Filter: created_at >= WEEK_START()
  Sort: priority DESC
  Use: Weekly planning

Last 30 Days:
  Filter: created_at >= NOW() - 30 days
  Sort: amount DESC
  Use: Recent activity
```

### 💰 **Value-Based Views**

```yaml
High-Value Items:
  Filter: amount > 1000
  Sort: amount DESC
  Use: Priority handling

At-Risk Items:
  Filter: stock < 10
  Sort: stock ASC
  Use: Reorder alerts

Best Performers:
  Filter: rating >= 4.5
  Sort: sales_count DESC
  Use: Feature products
```

## Sharing Views

### 👥 **Team Collaboration**

**How views help teams:**
- Everyone sees same filtered data
- Consistent reporting
- Role-specific perspectives
- Reduced training time

**Sharing strategies:**
1. **Department Views:**
   - Sales - Pipeline View
   - Support - Ticket Queue
   - Finance - Invoice Tracking

2. **Role Views:**
   - Manager - Team Overview
   - Agent - Assigned Tasks
   - Admin - System Status

3. **Project Views:**
   - Project A - All Tasks
   - Project B - Milestones
   - Project C - Issues

### 🔗 **Export and Share**

Views can be:
- Exported to CSV
- Shared via secure links
- Used in API queries
- Embedded in reports

## Best Practices

### ✅ **Do's**

1. **Use descriptive names**
   - Clear purpose
   - Include key filters
   - Date ranges if applicable

2. **Document complex views**
   - Add descriptions
   - Note update frequency
   - Specify use cases

3. **Regular cleanup**
   - Delete unused views
   - Update outdated filters
   - Consolidate similar views

4. **Create view templates**
   - Standard naming
   - Common filter sets
   - Reusable patterns

### ❌ **Don'ts**

1. **Don't create too many views**
   - Causes confusion
   - Hard to maintain
   - Clutters interface

2. **Don't use for security**
   - Views aren't permissions
   - Data still accessible
   - Use proper access control

3. **Don't forget maintenance**
   - Update as schema changes
   - Remove obsolete views
   - Keep filters current

## Integration Tips

### 🔧 **n8n Workflows**

Use views in API calls:
```javascript
// Fetch specific view data
const viewData = await $http.get(
  'https://your-app.xano.io/api:abc/table',
  {
    params: {
      view: 'active_premium_users'
    }
  }
);
```

### 🌐 **WeWeb Collections**

1. Create view in Xano
2. Reference view in collection
3. Auto-filtered data in frontend
4. Real-time updates maintained

## Try This: Create Your First Views

### 📝 **Exercise: Customer Service Views**

Create these three views for a support team:

1. **"Urgent - Unassigned"**
   ```
   Filters:
   - priority = "high"
   - assigned_to = NULL
   - status != "closed"
   Sort: created_at ASC (oldest first)
   ```

2. **"My Open Tickets"**
   ```
   Filters:
   - assigned_to = CURRENT_USER
   - status IN ("open", "pending")
   Sort: priority DESC, created_at ASC
   ```

3. **"Resolved Today"**
   ```
   Filters:
   - resolved_at = TODAY()
   - status = "closed"
   Sort: resolved_at DESC
   ```

## Common Questions

### "How many views should I create?"

Start small:
- 3-5 views per table initially
- Add as patterns emerge
- Consolidate similar views

### "Can views affect performance?"

Views themselves don't impact performance:
- They're just saved settings
- Complex filters might be slow
- Index filtered columns for speed

### "Who can see my views?"

Depends on settings:
- Personal views (just you)
- Team views (workspace members)
- Shared views (link recipients)

## Troubleshooting

### "View shows no data"
- Check filters aren't too restrictive
- Verify data exists matching criteria
- Check date ranges

### "View is slow"
- Simplify complex filters
- Add indexes to filtered columns
- Reduce number of sorted columns

### "Can't find my view"
- Check view dropdown
- Verify correct table
- Check if deleted

## Next Steps

Now that you understand views:
1. Create views for your common filters
2. Share views with your team
3. Set up export workflows
4. Build view-based reports
5. Optimize with proper indexes

## Related Documentation

- [Database Basics](./database-basics.md)
- [Filtering Data](../function-stack/query-all-records.md)
- [Export and Sharing](./export-and-sharing.md)
- [Data Sources](./data-sources-management.md)