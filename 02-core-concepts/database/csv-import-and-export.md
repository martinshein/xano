---
title: "CSV Import & Export - Bulk Data Management Made Easy"
description: "Import and export CSV files in Xano with automatic schema detection, field mapping, and support for millions of records. Perfect for spreadsheet migrations and data backups."
category: database
subcategory: migration
tags:
  - CSV
  - Import Data
  - Export Data
  - Spreadsheets
  - Data Migration
  - Bulk Operations
  - Excel
difficulty: beginner
reading_time: 8 minutes
last_updated: '2025-01-23'
prerequisites:
  - Xano workspace access
  - CSV file or data to export
  - Basic spreadsheet knowledge
---

# CSV Import & Export - Bulk Data Management Made Easy

## 📋 **Quick Summary**

**What it does:** Import spreadsheet data into Xano databases or export your data to CSV format - handling millions of records with automatic field type detection and mapping.

**Why it matters:** CSV import/export enables you to:
- Migrate from spreadsheets to a real database
- Bulk update thousands of records at once
- Create backups of your data
- Share data with non-technical users
- Import data from any system that exports CSV

**Time to implement:** 5-15 minutes for most imports

---

## What You'll Learn

- Importing CSV files to create new tables
- Adding CSV data to existing tables
- Bulk editing records via CSV
- Exporting data with filters and views
- Handling large files (millions of records)
- Common formatting issues and solutions

## Understanding CSV in Xano

Think of CSV import/export as a bridge between spreadsheets and your database. It's like moving from sticky notes to a filing system - same information, better organization.

### 💡 **What This Means for You**

- **No size limits:** Import millions of records without issues
- **Automatic schema:** Xano detects field types automatically
- **Dedicated resources:** Imports run on separate servers (won't slow your app)
- **Smart matching:** Updates existing records or adds new ones
- **Format flexibility:** Works with Excel, Google Sheets, and any CSV source

## Importing CSV Files

### 🚀 **Three Import Options**

1. **Create New Table** - Start fresh with your CSV data
2. **Add to Existing Table** - Append new records
3. **Edit Existing Records** - Update records using ID matching

### 📝 **Method 1: Create New Table from CSV**

Perfect for migrating spreadsheet data to Xano.

#### Step-by-Step Process:

1. **Navigate to Database**
2. **Click "Add Table"**
3. **Select "Import Data"**
4. **Choose "CSV" option**
5. **Upload your file:**
   - Drag and drop, or
   - Browse and select file

#### What Happens Next:

Xano automatically:
- Analyzes first 100 rows
- Detects field types (text, number, date, etc.)
- Suggests table name from filename
- Shows preview for verification

#### Preview Screen Options:

```
Table Name: [customers]  ← Edit if needed

Field Mappings:
name        → Text
email       → Email
age         → Integer
joined_date → Date
is_active   → Boolean
price       → Decimal
```

**🎯 Pro Tips:**
- Review field types carefully
- Set primary key (usually auto-generated ID)
- Rename fields to follow conventions
- Choose appropriate data types for calculations

### 📥 **Method 2: Add Records to Existing Table**

Use when you have new data for an existing table.

#### Process:

1. **Open existing table**
2. **Click options menu (⋮)**
3. **Select "Import CSV"**
4. **Map CSV columns to table fields:**

```
CSV Column    →    Table Field
-----------        -----------
customer_name  →   name
cust_email     →   email
phone_number   →   phone
[Skip]         →   created_at (auto-generated)
```

#### Mapping Rules:

- **Matched fields:** Automatically mapped by name
- **Unmatched fields:** Manually select mapping
- **Extra CSV columns:** Can skip or create new fields
- **Missing CSV columns:** Leave as NULL or set default

### ✏️ **Method 3: Edit Existing Records**

Update multiple records at once using CSV.

#### Requirements:

Your CSV **MUST** include an `id` column that matches existing record IDs.

#### Example CSV for Updates:

```csv
id,name,email,status
1,John Smith,john.smith@email.com,active
2,Jane Doe,jane.doe@email.com,inactive
3,Bob Wilson,bob.wilson@email.com,active
```

#### Process:

1. Export current data (to get IDs)
2. Modify in spreadsheet
3. Keep `id` column intact
4. Import with "Edit Records" option
5. Xano updates matching records

**⚠️ Important:** Records without matching IDs are skipped, not added.

## Exporting Data to CSV

### 📤 **Export Options**

#### Basic Export:

1. **Open any table**
2. **Click options menu (⋮)**
3. **Select "Export CSV"**
4. **Choose options:**
   - All records
   - Current view only
   - With or without filters

#### Export with Views:

If you have a filtered view:
```
☑️ Export current view only
   - Applies all filters
   - Respects sort order
   - Includes only visible columns
```

### 🎨 **Export Scenarios**

**Backup Everything:**
```
Table: Customers
View: All
Filters: None
Result: Complete backup
```

**Export Active Users:**
```
Table: Users
View: Active Users
Filters: status = "active"
Result: Only active user records
```

**Monthly Report:**
```
Table: Orders
Filters: 
  - created_at >= "2024-01-01"
  - created_at <= "2024-01-31"
Result: January orders only
```

## CSV Format Requirements

### ✅ **Valid CSV Format**

**Required characteristics:**
- **Separator:** Comma (,) only
- **Encoding:** UTF-8
- **Line endings:** LF or CRLF
- **Headers:** First row contains field names

**Example of valid CSV:**
```csv
name,email,age,joined_date
"John Smith","john@example.com",28,2024-01-15
"Jane Doe","jane@example.com",32,2024-01-16
"Bob Wilson, Jr.","bob@example.com",45,2024-01-17
```

### 🔧 **Common Format Issues**

| Problem | Solution |
|---------|----------|
| **Semicolon separator** | Replace with commas |
| **Wrong encoding** | Save as UTF-8 |
| **Special characters** | Use UTF-8 encoding |
| **Commas in data** | Wrap in quotes |
| **Line breaks in cells** | Wrap in quotes |

### 📊 **Preparing CSV in Popular Tools**

#### Excel (Windows/Mac):
1. File → Save As
2. Choose "CSV UTF-8 (Comma delimited)"
3. Click Save

#### Google Sheets:
1. File → Download
2. Select "Comma Separated Values (.csv)"
3. Automatically UTF-8 encoded

#### Numbers (Mac):
1. File → Export To → CSV
2. Text Encoding: Unicode (UTF-8)
3. Click Next → Save

## Handling Large Files

### 🚀 **Performance Characteristics**

| File Size | Records | Import Time | Notes |
|-----------|---------|-------------|-------|
| < 1 MB | ~5,000 | < 30 seconds | Instant |
| 10 MB | ~50,000 | 1-2 minutes | Quick |
| 100 MB | ~500,000 | 5-10 minutes | Coffee break |
| 1 GB | ~5 million | 30-60 minutes | Lunch time |

### 💡 **Large File Best Practices**

1. **Test with sample first**
   - Import 100 rows
   - Verify field mapping
   - Check data types

2. **Clean data beforehand**
   - Remove duplicates
   - Fix formatting issues
   - Validate required fields

3. **Import during off-hours**
   - Less server load
   - Faster processing
   - No user impact

4. **Split massive files**
   - Break into 500K record chunks
   - Import sequentially
   - Easier error recovery

## Integration Examples

### 🔧 **n8n Automation**

Create automated CSV exports:

```javascript
// n8n HTTP Request node
{
  "method": "GET",
  "url": "{{$env.XANO_URL}}/customers",
  "responseFormat": "file",
  "options": {
    "response": {
      "response": {
        "responseFormat": "file",
        "outputPropertyName": "data"
      }
    }
  }
}
// Then use Spreadsheet node to process
```

### 🌐 **WeWeb Integration**

Add CSV export button:

```javascript
// WeWeb workflow
1. Create button "Export to CSV"
2. On click → Call Xano API
3. Convert JSON response to CSV
4. Trigger browser download
```

## Common Use Cases

### 📦 **E-Commerce Inventory**

```csv
sku,product_name,quantity,price,category
SKU001,"Widget Pro",150,29.99,Electronics
SKU002,"Widget Mini",275,19.99,Electronics
```

### 👥 **User Migration**

```csv
email,first_name,last_name,role,created_date
john@example.com,John,Smith,admin,2024-01-15
jane@example.com,Jane,Doe,user,2024-01-16
```

### 📊 **Analytics Data**

```csv
date,page_views,unique_visitors,bounce_rate,avg_time
2024-01-15,5234,1823,0.45,00:03:25
2024-01-16,5512,1934,0.42,00:03:45
```

## Try This: Quick Import Exercise

1. **Create sample CSV:**
```csv
product_name,price,in_stock,category
"Laptop Pro",1299.99,true,Electronics
"Desk Chair",249.99,true,Furniture
"Notebook Set",19.99,false,Stationery
```

2. **Save as `products.csv`**

3. **Import to Xano:**
   - Create new table
   - Upload file
   - Review field types
   - Complete import

4. **Verify in database**

5. **Export with filter:**
   - Filter: in_stock = true
   - Export CSV
   - Check results

## ⚠️ **Common Mistakes to Avoid**

1. **Wrong separator character**
   - Must use commas, not semicolons
   - Check in text editor if unsure

2. **Missing ID for updates**
   - Edit operations need ID column
   - Export first to get IDs

3. **Mismatched field names**
   - Headers must match exactly
   - Case-sensitive matching

4. **Date format issues**
   - Use ISO format: YYYY-MM-DD
   - Or configure during import

5. **Special characters**
   - Save as UTF-8
   - Test with sample first

## Troubleshooting

### "Import fails immediately"
- Check CSV format (commas, UTF-8)
- Verify file isn't corrupted
- Try with smaller sample

### "Data looks wrong after import"
- Review field type detection
- Check for special characters
- Verify encoding is UTF-8

### "Missing records after import"
- Check for duplicate IDs
- Look for format errors in CSV
- Review import logs

### "Can't map fields"
- Ensure header row exists
- Check for typos in headers
- Remove special characters

## Best Practices

### 🎯 **Do's**

1. **Always backup before bulk edits**
2. **Test with small sample first**
3. **Validate data before import**
4. **Use consistent date formats**
5. **Document field mappings**

### ❌ **Don'ts**

1. **Don't import without reviewing preview**
2. **Don't skip field type verification**
3. **Don't import sensitive data without encryption**
4. **Don't use Excel-specific formulas**
5. **Don't forget to check encoding**

## Next Steps

After mastering CSV import/export:
1. Set up automated imports via API
2. Create scheduled exports
3. Build data validation workflows
4. Integrate with n8n for processing
5. Implement backup strategies

## Related Documentation

- [Database Basics](./database-basics.md)
- [Airtable Migration](./airtable-to-xano.md)
- [Bulk Operations](../function-stack/bulk-operations.md)
- [Data Sources](./data-sources-management.md)