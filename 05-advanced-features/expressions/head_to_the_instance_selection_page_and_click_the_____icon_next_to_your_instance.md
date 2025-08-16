---
title: "Xano Instance Settings and Configuration"
description: "Learn how to configure custom domains, database connectors, and instance upgrades through Xano's instance settings panel"
category: expressions
has_code_examples: false
last_updated: '2025-01-16'
tags:
  - instance-settings
  - custom-domain
  - database-connector
  - instance-upgrade
  - configuration
---

# Xano Instance Settings and Configuration

## 📋 **Quick Summary**

Xano's instance settings provide powerful configuration options including custom domain setup, direct database access, and instance upgrades. These settings help you customize your Xano environment for production use, development workflows, and advanced integrations.

## What You'll Learn

- How to access and navigate instance settings
- Custom domain configuration and DNS setup
- Database Connector setup for direct access
- Instance upgrade process and considerations
- API URL changes and migration strategies
- Best practices for production environments

## Accessing Instance Settings

All instance-level configurations are accessed through the main settings panel:

1. **Navigate to Instance Selection**
   - Go to your Xano instance selection screen
   - Locate your target instance

2. **Open Settings Panel**
   - Click the settings icon (⚙️) next to your instance name
   - This opens the comprehensive settings panel

3. **Available Settings Categories**
   - Custom Domain configuration
   - Database Connector setup  
   - Release Track preferences
   - Backup and Restore options
   - Instance upgrade tools

## Custom Domain Configuration

Custom domains allow you to use your own domain for API endpoints instead of Xano's default URLs.

### Requirements
- Available on all paid Xano plans
- Access to your domain's DNS settings
- Basic understanding of DNS record management

### Setup Process

1. **Access Custom Domain Settings**
   - Click the ⚙️ icon next to your instance
   - Choose "Custom Domain" from the settings panel

2. **DNS Configuration**
   - Update DNS records with your domain registrar
   - Add the required CNAME or A records as specified
   - Common registrars have specific documentation:
     - GoDaddy, Namecheap, Cloudflare
     - Squarespace (formerly Google Domains)
     - Hover, Network Solutions, Bluehost

3. **Verify DNS Propagation**
   - Check propagation status at whatismydns.net
   - Look for green checkmarks indicating successful propagation
   - More checkmarks = better global availability

4. **Configure in Xano**
   - Add your custom domain to the configuration panel
   - Save changes to apply immediately
   - Your APIs become available at the new domain

### Example Domain Setup

```markdown
# Custom Domain Configuration Example

## Before
API Base URL: https://x1b2-c3d4-e5f6.dev.xano.io/

## After Custom Domain
API Base URL: https://api.yourcompany.com/

## Required DNS Changes
Type: CNAME
Name: api
Value: x1b2-c3d4-e5f6.dev.xano.io
TTL: 300 (or as low as possible)
```

### Connecting Via Original Domain

Sometimes you need to access your instance through the original Xano domain:

1. **Access Alternative Connection**
   - Go to instance selection screen
   - Hover over your instance
   - Click the three dots menu
   - Choose "Connect Via Xano Domain"

2. **Use Cases**
   - Troubleshooting domain issues
   - DNS propagation testing
   - Backup access during domain changes

## Database Connector

The Database Connector enables direct PostgreSQL access to your Xano database for advanced use cases.

### Availability
- **Starter Plan**: Available as add-on
- **Pro Plan**: Included
- **All Plans**: Requires careful configuration

### Important Warnings

**⚠️ PROCEED WITH CAUTION**: Direct database access bypasses Xano's built-in protections:
- No automatic data validation
- Risk of data corruption if used incorrectly
- Potential for breaking Xano functionality
- Advanced feature requiring database expertise

### Setup Process

1. **Access Database Connector**
   - Click ⚙️ icon next to your instance
   - Choose "Database Connector" from panel

2. **Review Connection Details**
   - **Details Tab**: Get connection information
     - Database public IP address
     - Full-access and read-only credentials
     - Connection parameters

3. **Configure IP Allow List**
   - **Settings Tab**: Manage access restrictions
   - Add specific IP addresses for security
   - Limit connections to trusted sources only

4. **Get Connection Credentials**
   - Click "Get your database's public IP"
   - Click "Get your database credentials"
   - Securely store connection information

### Security Best Practices

1. **IP Restrictions**: Always use the allow list feature
2. **Read-Only Access**: Use read-only credentials when possible
3. **Credential Management**: Regularly rotate database credentials
4. **Monitor Access**: Track who connects and when
5. **Test Environment**: Practice in development before production

### Example Connection (Using Navicat)

```markdown
# Database Connection Setup

1. Open your database client (Navicat, pgAdmin, etc.)
2. Create new PostgreSQL connection
3. Configure connection parameters:
   - Host: [IP from Xano]
   - Port: 5432
   - Database: [Database name from Xano]
   - Username: [From Xano credentials]
   - Password: [From Xano credentials]
4. Test connection
5. Save configuration for future use
```

## Instance Upgrades

Instance upgrades move your data and logic to more powerful infrastructure.

### Why Upgrade?

**Free Plan Limitations:**
- Shared resources with other customers
- Limited storage and database records
- Reduced processing power
- Suitable for prototyping only

**Paid Plan Benefits:**
- Dedicated or enhanced resources
- Increased storage and performance
- Better scalability options
- Production-ready infrastructure

### Upgrade Process

1. **Plan Selection**
   - **Launch to Scale1x**: 48-hour refund policy available
   - **Scale Tier Trials**: Contact support for higher tier trials
   - **Custom Enterprise**: Tailored solutions available

2. **Pre-Upgrade Checklist**
   - **Backup Creation**: Create current backup before upgrading
   - **API URL Review**: Check if URL changes are required
   - **Frontend Updates**: Prepare for potential API URL changes

3. **When API URL Changes**
   Your API URL will change if:
   - Upgrading from free to paid plan
   - Adding features like Static IP
   - Changing server regions

4. **URL Migration Example**
   ```markdown
   # API URL Change Example
   
   ## Before Upgrade
   https://x1b2-c3d4-e5f6.dev.xano.io/
   
   ## After Upgrade  
   https://x7y8-z9a1-b2c3.dev.xano.io/
   
   ## Full Endpoint Example
   Before: https://x1b2-c3d4-e5f6.dev.xano.io/api:4qSkfrOl/user
   After:  https://x7y8-z9a1-b2c3.dev.xano.io/api:4qSkfrOl/user
   ```

5. **Complete Upgrade**
   - Type "I UNDERSTAND" in confirmation box
   - Click "Start upgrade now"
   - Monitor progress until completion

## Try This: Production Setup Checklist

Prepare your instance for production use:

```markdown
# Production Instance Setup

## 1. Custom Domain
- [ ] Configure custom domain DNS
- [ ] Verify propagation globally
- [ ] Test API endpoints on new domain
- [ ] Update documentation with new URLs

## 2. Instance Upgrade
- [ ] Create comprehensive backup
- [ ] Upgrade to appropriate paid plan
- [ ] Update API URLs in frontend applications
- [ ] Test all functionality post-upgrade

## 3. Security Configuration
- [ ] Set up Database Connector IP restrictions
- [ ] Configure backup policies
- [ ] Review access permissions
- [ ] Document connection credentials securely

## 4. Monitoring Setup
- [ ] Configure release track preferences
- [ ] Set up backup monitoring
- [ ] Establish performance baselines
- [ ] Create incident response procedures
```

## Integration with No-Code Platforms

### WeWeb Configuration

Update WeWeb projects after instance changes:

1. **API Datasource Updates**: Change base URLs in WeWeb's data sources
2. **Authentication Flows**: Update auth endpoint URLs
3. **Custom Headers**: Maintain any custom headers or tokens
4. **Testing**: Validate all data flows work correctly

### Make.com Scenario Updates

Modify Make.com scenarios for new instance settings:

1. **HTTP Module URLs**: Update all Xano API URLs
2. **Webhook URLs**: Reconfigure webhook endpoints if needed
3. **Connection Testing**: Validate all connections work
4. **Error Handling**: Update error handling for new response formats

### n8n Workflow Updates

Adjust n8n workflows for instance changes:

1. **HTTP Request Nodes**: Update base URLs
2. **Credential Management**: Update stored Xano credentials
3. **Workflow Testing**: Execute test runs for all workflows
4. **Documentation**: Update workflow documentation

## Common Mistakes to Avoid

1. **DNS Propagation Rush**: Waiting for full DNS propagation before finalizing
2. **Missing Backups**: Not creating backups before major changes
3. **Frontend Oversight**: Forgetting to update frontend API URLs
4. **Database Access**: Using Database Connector without proper security
5. **Documentation Gaps**: Not updating team documentation after changes

## Pro Tips

1. **Staged Rollouts**: Test domain changes in development first
2. **DNS Monitoring**: Use monitoring tools to track domain health
3. **Backup Automation**: Set up automated backup verification
4. **Team Communication**: Notify team members of instance changes
5. **Rollback Planning**: Always have rollback procedures documented
6. **Performance Testing**: Validate performance after upgrades

## Troubleshooting Common Issues

### Custom Domain Problems
- **DNS Propagation**: Allow 24-48 hours for full propagation
- **SSL Issues**: Ensure proper SSL certificate installation
- **Subdomain Configuration**: Verify correct subdomain setup

### Database Connector Issues
- **Connection Failures**: Check IP allow list configuration
- **Credential Problems**: Verify credentials haven't expired
- **Performance Issues**: Monitor concurrent connection limits

### Upgrade Problems
- **API URL Changes**: Update all frontend references
- **Feature Access**: Verify new plan features are available
- **Performance**: Monitor and optimize after upgrade

Xano's instance settings provide the foundation for production-ready applications. By properly configuring custom domains, database access, and instance capabilities, you can create robust, scalable backend systems that integrate seamlessly with your frontend applications and automation workflows.