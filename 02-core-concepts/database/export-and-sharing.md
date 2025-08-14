---
title: "Export and Sharing - Share Database Views Securely"
description: "Learn how to export data and share database views with external users using secure authentication modes. Perfect for client reporting and data collaboration."
category: database
subcategory: sharing
tags:
  - Export
  - Sharing
  - CSV Export
  - Data Collaboration
  - Authentication
  - Security
  - Reporting
difficulty: intermediate
reading_time: 7 minutes
last_updated: '2025-01-23'
prerequisites:
  - Xano workspace with data
  - Understanding of database views
  - Users to share with
---

# Export and Sharing - Share Database Views Securely

## 📋 **Quick Summary**

**What it does:** Export your data to CSV or create secure shareable links to database views, allowing external users to access specific data without Xano accounts.

**Why it matters:** Data sharing enables you to:
- Share reports with clients without giving database access
- Export data for analysis in other tools
- Collaborate with stakeholders securely
- Create read-only data portals
- Automate report distribution

**Time to implement:** 5 minutes to set up sharing

---

## What You'll Learn

- Exporting data to CSV format
- Creating shareable database views
- Setting up authentication modes
- Managing share permissions
- Best practices for secure sharing
- Integration with reporting tools

## Understanding Export and Sharing

Think of sharing as creating a window into your database - you control exactly what people can see, who can see it, and how they access it. It's like giving someone a guest pass to specific rooms in your building.

### 💡 **What This Means for You**

- **No account needed:** Share data with people outside your team
- **Granular control:** Share specific views, not entire tables
- **Multiple security levels:** Choose appropriate authentication
- **Real-time data:** Shared views show live data
- **Export flexibility:** Download data in standard formats

## Exporting Data

### 📤 **Quick CSV Export**

The fastest way to get data out of Xano.

#### Process:

1. **Open any table or view**
2. **Click the options menu (⋮)**
3. **Select "Export CSV"**
4. **Choose export options:**
   - Current view with filters
   - All records in table
   - Specific data source

#### Export Options:

```
☑️ Export current view only
   - Applies active filters
   - Maintains sort order
   - Includes only visible columns

☐ Include all records
   - Ignores current filters
   - Exports entire table
   - All columns included
```

### 🎯 **Advanced Export Scenarios**

**Monthly Report Export:**
```
View: Sales Report
Filters: 
  - date >= "2024-01-01"
  - date <= "2024-01-31"
  - status = "completed"
Sort: date DESC
Export: Current view only
```

**Customer List for Marketing:**
```
View: Active Customers
Filters:
  - subscribed = true
  - email_verified = true
Columns: name, email, signup_date
Export: Selected columns only
```

## Creating Shareable Views

### 🔗 **Setting Up a Share**

Transform any database view into a shareable link.

#### Step-by-Step Process:

1. **Create or select a database view**
   - Apply filters
   - Choose columns
   - Set sort order

2. **Click "Share View" button**

3. **Configure share settings:**
   - Name the share
   - Select data source
   - Choose authentication mode
   - Set permissions

4. **Generate share link**

5. **Distribute to users**

### 🔐 **Authentication Modes**

Three levels of security for shared views:

#### 1. Public Access (No Authentication)
```
Security Level: ⚠️ Low
Use Case: Public data, marketing stats
Setup: Just share the link
Access: Anyone with link can view
```

**When to use:**
- Public dashboards
- Marketing metrics
- Non-sensitive data
- Embedded reports

#### 2. Password Protected
```
Security Level: 🔒 Medium
Use Case: Client reports, partner data
Setup: Set a password
Access: Link + password required
```

**When to use:**
- Client-specific reports
- Partner portals
- Team reports
- Semi-sensitive data

**Password best practices:**
- Use strong passwords (12+ characters)
- Different password per share
- Rotate passwords regularly
- Share password separately from link

#### 3. Two-Factor Authentication
```
Security Level: 🔐 High
Use Case: Financial data, PII
Setup: Require email verification
Access: Link + email confirmation
```

**When to use:**
- Financial reports
- Personal information
- Compliance requirements
- Highly sensitive data

**How it works:**
1. User clicks share link
2. Enters their email
3. Receives verification email
4. Clicks verification link
5. Accesses the data

## Managing Shared Views

### 📊 **Share Configuration Options**

**Basic Settings:**
```yaml
Name: "Q1 Sales Report"
Description: "Quarterly sales data for stakeholders"
View: "Sales Q1 2024"
Data Source: "production"
```

**Column Selection:**
```yaml
Visible Columns:
  - order_date
  - customer_name
  - product
  - quantity
  - total
Hidden Columns:
  - cost
  - profit_margin
  - internal_notes
```

**Access Controls:**
```yaml
Authentication: "password"
Password: "SecurePass123!"
Expiration: "2024-12-31"
Max Views: 1000
Allow Download: true
```

### 🎨 **Customizing Shared Views**

**Branding Options:**
- Custom header text
- Company logo
- Color scheme
- Footer information

**Display Settings:**
- Records per page
- Default sort order
- Column widths
- Date formats

**Interaction Settings:**
- Enable/disable sorting
- Enable/disable filtering
- Allow CSV download
- Show/hide record count

## Security Best Practices

### 🔒 **Protecting Shared Data**

1. **Use appropriate authentication**
   - Match security to data sensitivity
   - Default to higher security when unsure

2. **Limit data exposure**
   - Share views, not tables
   - Apply filters before sharing
   - Hide sensitive columns

3. **Set expiration dates**
   - Time-limited shares for projects
   - Regular review of active shares

4. **Monitor access**
   - Track who accesses shares
   - Review access logs
   - Alert on suspicious activity

5. **Rotate credentials**
   - Change passwords periodically
   - Revoke old shares
   - Update access lists

### ⚠️ **Common Security Mistakes**

1. **Sharing entire tables**
   - Always use filtered views
   - Hide unnecessary columns

2. **Using weak passwords**
   - Minimum 12 characters
   - Mix of character types

3. **Never expiring shares**
   - Set reasonable expiration
   - Review active shares monthly

4. **Sharing production data**
   - Consider using test data source
   - Anonymize sensitive information

## Integration Examples

### 🔧 **n8n Automation**

Automate report distribution:

```javascript
// n8n workflow for weekly reports
{
  "trigger": "Every Monday at 9 AM",
  "actions": [
    {
      "type": "HTTP Request",
      "url": "https://share.xano.io/abc123",
      "auth": {
        "type": "password",
        "password": "{{$env.SHARE_PASSWORD}}"
      }
    },
    {
      "type": "Email",
      "to": "stakeholders@company.com",
      "subject": "Weekly Report Ready",
      "body": "View report: {{shareLink}}"
    }
  ]
}
```

### 🌐 **WeWeb Embedding**

Embed shared view in WeWeb app:

```html
<!-- WeWeb HTML element -->
<iframe 
  src="https://share.xano.io/abc123?embed=true"
  width="100%"
  height="600"
  frameborder="0">
</iframe>
```

### 📊 **Power BI Connection**

Connect Power BI to shared data:

1. Use Web connector
2. Enter share URL
3. Configure authentication
4. Set refresh schedule

## Use Case Examples

### 📈 **Client Dashboard**

```yaml
Share Name: "Client Performance Dashboard"
View: Filtered to client's data only
Authentication: Password
Features:
  - Real-time metrics
  - Download enabled
  - 30-day expiration
  - Custom branding
```

### 📋 **Inventory Report**

```yaml
Share Name: "Weekly Inventory Status"
View: Current stock levels
Authentication: Two-factor
Features:
  - Auto-refresh daily
  - Email notifications
  - Export to Excel
  - Historical comparison
```

### 👥 **Team Analytics**

```yaml
Share Name: "Team Performance Metrics"
View: Aggregated team data
Authentication: Public (internal network only)
Features:
  - Live updates
  - Sortable columns
  - Trend charts
  - KPI highlights
```

## Try This: Create Your First Share

1. **Create a filtered view:**
   - Open a table
   - Apply filters
   - Hide sensitive columns

2. **Set up sharing:**
   - Click "Share View"
   - Name it "Test Share"
   - Choose password authentication
   - Set password: "TestShare123!"

3. **Configure options:**
   - Enable CSV download
   - Set 7-day expiration
   - Limit to your data source

4. **Test the share:**
   - Copy link
   - Open in private browser
   - Enter password
   - Verify correct data shows

5. **Clean up:**
   - Revoke the share
   - Review access logs

## Troubleshooting

### "Share link not working"
- Check expiration date
- Verify authentication settings
- Confirm data source selection
- Check user's email for 2FA

### "Wrong data showing"
- Review view filters
- Check data source
- Verify column selection
- Refresh the share

### "Can't download CSV"
- Enable download in settings
- Check user permissions
- Verify browser compatibility

### "Performance issues"
- Limit number of records
- Reduce column count
- Add pagination
- Use indexed columns

## Best Practices Summary

### 🎯 **Do's**

1. **Always use views, not direct table access**
2. **Set appropriate authentication levels**
3. **Include expiration dates**
4. **Monitor access regularly**
5. **Document what's being shared**

### ❌ **Don'ts**

1. **Don't share sensitive data publicly**
2. **Don't use same password for all shares**
3. **Don't forget to revoke old shares**
4. **Don't share production data for testing**
5. **Don't ignore access logs**

## Next Steps

After mastering sharing:
1. Set up automated report distribution
2. Create client portal with multiple shares
3. Implement share governance policy
4. Build monitoring dashboard
5. Integrate with BI tools

## Related Documentation

- [Database Views](./database-views.md)
- [CSV Export](./csv-import-and-export.md)
- [Data Sources](./data-sources-management.md)
- [Security Best Practices](../authentication/security-policy.md)