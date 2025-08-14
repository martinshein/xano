---
title: "Direct Database Connector - Access Your PostgreSQL Database"
description: "Connect external tools directly to your Xano PostgreSQL database for analytics, backups, and advanced data operations. Learn setup, security, and table format options."
category: database
subcategory: advanced
tags:
  - PostgreSQL
  - Database Connection
  - External Access
  - SQL
  - JSONB
  - Analytics
  - Backup
difficulty: advanced
reading_time: 12 minutes
last_updated: '2025-01-23'
prerequisites:
  - Pro plan or Starter with add-on
  - Understanding of PostgreSQL
  - External database tool
---

# Direct Database Connector - Access Your PostgreSQL Database

## 📋 **Quick Summary**

**What it does:** Direct Database Connector provides secure access to your Xano instance's underlying PostgreSQL database, allowing external tools to connect for analytics, backups, and custom operations.

**Why it matters:** Direct access enables:
- Advanced analytics with tools like Tableau or PowerBI
- Custom backup and restore solutions
- Complex SQL queries beyond Xano's interface
- Integration with specialized database tools
- Real-time data synchronization

**Time to implement:** 15 minutes to set up connection

⚠️ **Important:** Direct access bypasses Xano's data validation. Use with caution!

---

## What You'll Learn

- Setting up direct database connections
- Managing connection credentials
- Choosing between JSONB and Standard SQL formats
- Implementing IP allowlists for security
- Converting table formats
- Custom SQL table naming
- Best practices for external access

## Understanding Direct Database Access

### 🔌 **What is Direct Database Connector?**

Think of it like having two ways into your house:
- **Front door (Xano API):** Security system, doorbell, visitor log
- **Back door (Direct DB):** Direct access, no security checks

**Real-world analogy:**
```
Xano API Access:
├── Authentication required
├── Data validation enforced
├── Rate limiting applied
├── Audit trails maintained
└── Business logic executed

Direct Database Access:
├── Raw PostgreSQL connection
├── No validation checks
├── Full SQL capabilities
├── Bypasses all middleware
└── Direct table manipulation
```

### 💡 **When to Use Direct Access**

**Perfect for:**
- Business intelligence tools (Tableau, PowerBI, Looker)
- Custom backup solutions
- Data migration projects
- Complex analytical queries
- Real-time replication
- Database administration

**Not recommended for:**
- Regular application operations
- User-facing features
- Data entry workflows
- Untrusted environments

## Plan Requirements

### 💰 **Availability**

| Plan | Direct DB Access | Notes |
|------|-----------------|-------|
| **Free** | ❌ Not available | Use API endpoints |
| **Starter** | 💵 Paid add-on | Additional monthly fee |
| **Pro** | ✅ Included | Full access |
| **Scale** | ✅ Included | Full access |
| **Enterprise** | ✅ Included | Custom configurations |

## Setting Up Database Connection

### 🛠️ **Step 1: Access Connection Settings**

1. **From Instance Dashboard:**
   - Click settings icon (⚙️)
   - Select "Database Connector"

2. **Connection Panel Opens:**
   ```
   Database Connector
   ├── Details Tab
   │   ├── Database IP
   │   ├── Full Access Credentials
   │   └── Read-Only Credentials
   └── Settings Tab
       └── IP Allowlist Configuration
   ```

### 🔑 **Step 2: Retrieve Credentials**

Click "Get Database IP" and "Get Credentials":

```yaml
Connection Details:
  Host: 123.45.67.89
  Port: 5432
  Database: xano_db_12345
  
Full Access:
  Username: xano_full_abc123
  Password: [secure_password_here]
  Permissions: Read, Write, Delete
  
Read-Only Access:
  Username: xano_read_xyz789
  Password: [secure_password_here]
  Permissions: Read only
```

**Security tip:** Use read-only credentials for analytics tools!

### 🔒 **Step 3: Configure IP Allowlist**

Restrict access to specific IP addresses:

1. **Enable Allowlist:**
   ```
   Settings → Enable IP Allowlist ✓
   ```

2. **Add Allowed IPs:**
   ```
   Your Office: 203.0.113.0
   Analytics Server: 198.51.100.42
   Backup Service: 192.0.2.1
   ```

3. **Save Configuration**

**Note:** Only these IPs can connect when enabled!

## Connecting External Tools

### 📊 **Example: Tableau Connection**

```yaml
Connection Settings:
  Server: 123.45.67.89
  Port: 5432
  Database: xano_db_12345
  Authentication: Username/Password
  Username: xano_read_xyz789
  Password: [your_password]
  SSL Mode: Require
```

### 🔧 **Example: pgAdmin Setup**

```yaml
General Tab:
  Name: Xano Production

Connection Tab:
  Host: 123.45.67.89
  Port: 5432
  Database: xano_db_12345
  Username: xano_full_abc123
  Password: [your_password]

SSL Tab:
  SSL Mode: Require
```

### 💻 **Example: Python Connection**

```python
import psycopg2

# Read-only connection for analytics
conn = psycopg2.connect(
    host="123.45.67.89",
    port=5432,
    database="xano_db_12345",
    user="xano_read_xyz789",
    password="your_password",
    sslmode="require"
)

# Execute query
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM users")
user_count = cursor.fetchone()[0]
print(f"Total users: {user_count}")
```

## Table Format Options

### 📋 **Understanding Table Formats**

Xano supports two table storage formats:

#### **1. JSONB Format (Legacy Default)**

```sql
-- Table structure
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    data JSONB
);

-- Sample data
{
  "id": 1,
  "data": {
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-15"
  }
}
```

**Pros:**
- Flexible schema
- Easy field additions
- Good for unstructured data

**Cons:**
- Harder for BI tools
- Complex SQL queries
- Performance overhead

#### **2. Standard SQL Format (Recommended)**

```sql
-- Table structure
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP
);

-- Sample data
| id | name     | email            | created_at          |
|----|----------|------------------|---------------------|
| 1  | John Doe | john@example.com | 2024-01-15 10:30:00 |
```

**Pros:**
- BI tool friendly
- Better performance
- Standard SQL queries
- Clear schema

**Cons:**
- Less flexible
- Schema migrations needed

### 🔄 **Converting Table Format**

#### **When to Convert to Standard SQL:**

✅ **Convert if you:**
- Use Tableau, PowerBI, or similar tools
- Need better query performance
- Frequently add new fields
- Run complex analytics

❌ **Keep JSONB if you:**
- Don't use external connections
- Have highly dynamic schemas
- Are satisfied with current performance

#### **Conversion Process:**

1. **Enable Standard SQL (Workspace Settings):**
   ```
   Settings → Database Preferences
   ☑ Use standard SQL columns for new tables
   ```

2. **Convert Existing Tables:**
   ```
   Settings → Migrate Tables
   Select tables to convert
   Confirm migration
   ```

⚠️ **Warning:** Conversion is PERMANENT!

3. **Migration happens immediately**
   - No downtime
   - Data preserved
   - Indexes maintained

## Custom SQL Table Names

### 🏷️ **Default vs Custom Names**

**Default naming:**
```sql
-- Xano default format
mvpw1_3  -- Hard to understand
mvpw1_7  -- Not descriptive
```

**Custom naming:**
```sql
-- Your custom names
users
orders
products
```

### ⚙️ **Setting Custom Names**

1. **Enable in Workspace:**
   ```
   Settings → Database Preferences
   ☑ Enable Custom SQL Table Names
   ```

2. **Configure per Table:**
   ```
   Table Settings → SQL Table Name → Manage
   Enter: users (or your preferred name)
   ```

3. **Naming Rules:**
   - Must be globally unique
   - Use prefixes for multiple workspaces
   - Test environment adds suffix automatically

**Example setup:**
```yaml
Production:
  users → prod_users
  orders → prod_orders

Development:
  users → dev_users_test
  orders → dev_orders_test
```

## Security Best Practices

### 🔐 **Connection Security**

1. **Always use SSL/TLS:**
   ```sql
   -- Connection string
   postgresql://user:pass@host:5432/db?sslmode=require
   ```

2. **Implement IP allowlisting:**
   - Only allow known IPs
   - Update list regularly
   - Remove unused entries

3. **Use appropriate credentials:**
   ```yaml
   Analytics Tools: Read-only access
   Backup Systems: Full access (carefully managed)
   Development: Separate credentials per developer
   ```

4. **Rotate credentials regularly:**
   - Revoke and regenerate monthly
   - Update all connected systems
   - Document credential usage

### 🚫 **Common Security Mistakes**

**Never do this:**
```javascript
// ❌ Hardcoded credentials in code
const connectionString = "postgresql://user:password@host/db";

// ❌ Using full access for read operations
analyticsConnection.user = "xano_full_access";

// ❌ Disabled SSL
sslmode = "disable";

// ❌ No IP restrictions
allowlist = "*";
```

**Always do this:**
```javascript
// ✅ Environment variables
const connectionString = process.env.DATABASE_URL;

// ✅ Read-only for analytics
analyticsConnection.user = process.env.XANO_READONLY_USER;

// ✅ Require SSL
sslmode = "require";

// ✅ Specific IP allowlist
allowlist = ["203.0.113.0/24"];
```

## Integration Examples

### 🔧 **n8n Database Node**

```javascript
// n8n PostgreSQL node configuration
{
  "credentials": {
    "database": "xano_db_12345",
    "host": "123.45.67.89",
    "port": 5432,
    "user": "{{$credentials.xanoReadUser}}",
    "password": "{{$credentials.xanoReadPassword}}",
    "ssl": true
  },
  "operation": "executeQuery",
  "query": "SELECT * FROM users WHERE created_at > NOW() - INTERVAL '24 hours'"
}
```

### 📊 **PowerBI Direct Query**

1. Get Data → PostgreSQL database
2. Enter connection details
3. Use DirectQuery mode for real-time
4. Build reports on live data

### 🔄 **Backup Script Example**

```bash
#!/bin/bash
# Daily backup script

# Set credentials (from environment)
export PGPASSWORD=$XANO_DB_PASSWORD

# Create backup
pg_dump \
  -h 123.45.67.89 \
  -p 5432 \
  -U xano_full_abc123 \
  -d xano_db_12345 \
  --no-owner \
  --no-privileges \
  -f backup_$(date +%Y%m%d).sql

# Upload to S3
aws s3 cp backup_$(date +%Y%m%d).sql s3://backups/xano/
```

## Troubleshooting

### 🔍 **Connection Issues**

**"Connection refused"**
- Check IP allowlist settings
- Verify credentials are correct
- Ensure port 5432 is open

**"SSL connection required"**
- Add `sslmode=require` to connection
- Update client to support SSL

**"Permission denied"**
- Using read-only for write operations?
- Check credential permissions

### 📊 **Query Performance**

**Slow queries on JSONB tables:**
```sql
-- Instead of:
SELECT data->>'email' FROM users WHERE data->>'status' = 'active';

-- Consider converting to Standard SQL format
```

**Missing indexes:**
```sql
-- Check existing indexes
SELECT * FROM pg_indexes WHERE tablename = 'users';

-- Note: Contact Xano support for index requests
```

## Best Practices Summary

### ✅ **Do's**

1. **Use read-only credentials** for analytics
2. **Enable IP allowlisting** always
3. **Convert to Standard SQL** for BI tools
4. **Monitor query performance** regularly
5. **Document all external connections**
6. **Test in development first**
7. **Keep credentials secure**

### ❌ **Don'ts**

1. **Don't bypass Xano for user operations**
2. **Don't share credentials across services**
3. **Don't disable SSL**
4. **Don't modify schema directly**
5. **Don't skip backups before changes**
6. **Don't hardcode credentials**

## Next Steps

After setting up direct access:

1. **Test connection** with read-only first
2. **Set up monitoring** for queries
3. **Document usage** for team
4. **Create backup strategy**
5. **Plan credential rotation**
6. **Configure BI tools**
7. **Set up alerts** for issues

## Related Documentation

- [Database Basics](./database-basics.md)
- [Database Maintenance](./database-maintenance.md)
- [Backup and Restore](./backup-and-restore.md)
- [Security Best Practices](../authentication/security-policy.md)
- [Performance Optimization](./indexing.md)