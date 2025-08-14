---
title: "Data Sources - Separate Test and Production Data Safely"
description: "Learn how to use Xano's data sources to separate test and production data, enabling safe development without risking live data."
category: database
subcategory: core-concepts
tags:
  - Data Sources
  - Test Data
  - Production Data
  - Database Management
  - Development Workflow
  - Data Migration
  - Best Practices
difficulty: intermediate
reading_time: 8 minutes
last_updated: '2025-01-23'
prerequisites:
  - Basic understanding of databases
  - Xano workspace with tables created
---

# Data Sources - Separate Test and Production Data Safely

## 📋 **Quick Summary**

**What it does:** Data sources are separate versions of your database that share the same structure (schema) but contain different data - like having multiple copies of a spreadsheet with the same columns but different rows.

**Why it matters:** Data sources enable you to:
- Test new features without breaking production
- Keep real customer data safe from accidents
- Develop with realistic test data
- Switch between environments instantly
- Migrate data between environments when ready

**Time to implement:** 5 minutes to set up, saves hours of potential disasters

---

## What You'll Learn

- How to create and manage data sources
- Best practices for test vs. production data
- Switching between data sources safely
- Targeting specific data sources in APIs
- Migrating data between environments
- Integration tips for n8n and WeWeb

## Understanding Data Sources

Imagine you're renovating a store. You wouldn't experiment with the layout while customers are shopping - you'd use a model or test location first. Data sources work the same way.

### 💡 **What This Means for You**

- **No more accidental deletions:** Test data stays separate from real data
- **Confident testing:** Break things in test without consequences
- **Realistic development:** Use copy of real data structure for testing
- **Easy deployment:** Switch from test to production instantly
- **Team collaboration:** Each developer can have their own data source

## How Data Sources Work

### The Key Concept

All data sources in your workspace:
- ✅ Share the SAME database structure (tables, fields, relationships)
- ❌ Have DIFFERENT actual data (records, content)

Think of it like this:
- **Structure** = The filing cabinet design (same for all)
- **Data** = The actual files inside (different for each)

## Creating Data Sources

### Step-by-Step Setup

#### 1️⃣ **Access Data Sources**

Click the data source indicator in the left navigation menu (shows current data source name and color).

#### 2️⃣ **Add New Data Source**

Click "+ Add Data Source" in the panel that opens.

#### 3️⃣ **Configure Your Data Source**

**Name it clearly:**
- `production` - Your live data
- `test` - General testing
- `dev_john` - Developer-specific
- `staging` - Pre-production testing

**Choose a distinct color:**
- 🔴 Red for production (danger!)
- 🟢 Green for test (safe)
- 🔵 Blue for development
- 🟡 Yellow for staging

**💡 Pro Tip:** The color appears throughout Xano as a constant reminder of which data source you're using.

#### 4️⃣ **Save and Start Using**

Click "Create" and your new data source is ready!

## Using Data Sources Effectively

### 🔄 **Switching Data Sources**

**How to switch:**
1. Click the data source indicator (left navigation)
2. Select desired data source
3. Color changes throughout interface

**What happens when you switch:**
- All database operations target selected source
- API testing uses selected data
- Function debugging uses selected data
- Your live application is NOT affected

**⚠️ Important:** Switching data sources in Xano does NOT change what your live application uses!

### 🎯 **Setting Active Data Source**

The "active" data source is what your live application uses by default.

**To change active source:**
1. Select data source from panel
2. Click "Set as Active"
3. Confirm the change

**🔴 WARNING:** Changing active data source affects your LIVE application! Only do this when:
- Deploying from staging to production
- Rolling back to previous data
- Performing planned maintenance

### 🎮 **Targeting Specific Data Sources**

Four ways to specify which data source to use:

#### Method 1: Set Data Source Function

In your function stack:
```
1. Add "Set Data Source" function (Utility Functions)
2. Select target data source
3. All subsequent database operations use this source
```

**Use case:** Copying data between sources programmatically

#### Method 2: Request Headers

When calling APIs externally:
```
X-Data-Source: test
```

**🔧 n8n Example:**
```javascript
{
  headers: {
    "X-Data-Source": "test",
    "Authorization": "Bearer YOUR_TOKEN"
  }
}
```

#### Method 3: URL Parameters

When headers aren't available:
```
https://your-instance.xano.io/api:abc123/users?x-data-source=test
```

**🌐 WeWeb Tip:** Add data source parameter to API calls during development

#### Method 4: Function Stack Settings

For background tasks and triggers:
1. Open function settings
2. Select "Data Source" option
3. Choose target source
4. Save settings

## Data Migration Between Sources

### When to Migrate Data

Common scenarios:
- **Refresh test data:** Copy production → test (anonymized)
- **Deploy features:** Copy staging → production
- **Backup before changes:** Copy production → backup
- **Create demo environment:** Copy production → demo

### 📦 **Migration Process**

#### Step 1: Access Migration Panel
- Click data sources indicator
- Select "⚙️ Manage Data Sources"
- Click "Migrate" button

#### Step 2: Configure Migration
- **Source:** Where data comes FROM
- **Destination:** Where data goes TO
- **Tables:** Select which tables to migrate

#### Step 3: Migration Options
- **Replace:** Delete destination data first
- **Append:** Add to existing data
- **Skip duplicates:** Avoid key conflicts

#### Step 4: Execute Migration
- Review settings carefully
- Click "Start Migration"
- Monitor progress indicator
- Wait for completion banner

**⏱️ Time Estimate:** 
- Small dataset (< 1000 records): Seconds
- Medium dataset (< 10,000 records): Minutes
- Large dataset (> 100,000 records): Could take hours

## Best Practices

### 🎯 **Data Source Strategy**

**Recommended Setup:**
```
production (RED) - Live customer data
staging (YELLOW) - Pre-production testing
test (GREEN) - General development
dev_[name] (BLUE) - Individual developer
```

### 🔐 **Safety Rules**

1. **Always develop in test first**
   - Never experiment in production
   - Test thoroughly before deploying

2. **Use clear naming conventions**
   - Include environment in name
   - Add developer initials for personal sources

3. **Color code consistently**
   - Red = Danger (production)
   - Green = Safe (test)
   - Keep consistent across projects

4. **Regular data refreshes**
   - Weekly: Refresh test from production
   - Before major features: Create fresh copy
   - After deployment: Archive old staging

### ⚠️ **Common Mistakes to Avoid**

1. **Testing in production**
   - Always check color indicator
   - Set up notifications for production changes

2. **Forgetting to switch sources**
   - Check before every session
   - Use workspace bookmarks with source specified

3. **Not refreshing test data**
   - Stale test data hides bugs
   - Schedule regular refreshes

4. **Mixing data source purposes**
   - Keep clear boundaries
   - Don't use staging as test

## Integration Examples

### 🔧 **n8n Workflow Setup**

```javascript
// Development workflow
const headers = {
  "X-Data-Source": process.env.NODE_ENV === 'production' ? 'production' : 'test',
  "Authorization": `Bearer ${API_KEY}`
};

// Make API call with correct source
const response = await fetch(XANO_URL, { headers });
```

### 🌐 **WeWeb Configuration**

In WeWeb, set up environment variables:
```javascript
// Development
XANO_DATA_SOURCE = "test"

// Production
XANO_DATA_SOURCE = "production"

// Use in API calls
`${API_URL}?x-data-source=${XANO_DATA_SOURCE}`
```

## Try This: Quick Exercise

1. **Create a test data source:**
   - Name: "test_learning"
   - Color: Green
   
2. **Switch to test source:**
   - Click indicator
   - Select "test_learning"
   
3. **Add test records:**
   - Go to Database
   - Add sample data
   
4. **Test an API:**
   - Run any API endpoint
   - Verify it uses test data
   
5. **Switch back to live:**
   - Select original source
   - Verify data differs

## Troubleshooting

### "My app is using wrong data"
- Check active data source setting
- Verify API headers/parameters
- Look for Set Data Source functions

### "Migration is taking forever"
- Large datasets take time
- Check for database locks
- Consider off-peak migration

### "Can't see my data source"
- Refresh the page
- Check permissions
- Verify workspace access

## Next Steps

Now that you understand data sources:
1. Set up proper test/production separation
2. Create data migration schedule
3. Document your data source strategy
4. Train team on proper usage

## Related Documentation

- [Database Basics](./database-basics.md)
- [Data Migration Guide](./migrating-your-data.md)
- [Testing Best Practices](../testing-and-debugging-function-stacks.md)
- [Environment Variables](../function-stack/environment-variables.md)