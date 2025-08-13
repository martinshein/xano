---
category: database
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/database
tags:
- authentication
- api
- webhook
- trigger
- query
- filter
- middleware
- expression
- realtime
- transaction
- function
- background-task
- custom-function
- rest
- database
title: 'apple-mobile-web-app-status-bar-style: black'
---

---
apple-mobile-web-app-status-bar-style: black

color-scheme: dark light
description: 'Establish a direct connection to your instance\''s PostgreSQL database'
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'direct-database-connector'
twitter:card: summary\_large\_image
twitter:description: 'Establish a direct connection to your instance\''s PostgreSQL database'
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'

viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---

[![](../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)![](../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)](../../index.html)















-   

    
    -   Using These Docs
    -   Where should I start?
    -   Set Up a Free Xano Account
    -   Key Concepts
    -   The Development Life Cycle
    -   Navigating Xano
    -   Plans & Pricing

-   

    
    -   Building with Visual Development
        
        -   APIs
            
            -   [Swagger (OpenAPI Documentation)](../../the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../../the-function-stack/building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../../the-function-stack/building-with-visual-development/background-tasks.html)
        -   [Triggers](../../the-function-stack/building-with-visual-development/triggers.html)
        -   [Middleware](../../the-function-stack/building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../../the-function-stack/building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../../the-function-stack/building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](../../the-function-stack/functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](../../the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../../the-function-stack/functions/database-requests/get-record.html)
            -   [Add Record](../../the-function-stack/functions/database-requests/add-record.html)
            -   [Edit Record](../../the-function-stack/functions/database-requests/edit-record.html)
            -   [Add or Edit Record](../../the-function-stack/functions/database-requests/add-or-edit-record.html)
            -   [Patch Record](../../the-function-stack/functions/database-requests/patch-record.html)
            -   [Delete Record](../../the-function-stack/functions/database-requests/delete-record.html)
            -   [Bulk Operations](../../the-function-stack/functions/database-requests/bulk-operations.html)
            -   [Database Transaction](../../the-function-stack/functions/database-requests/database-transaction.html)
            -   [External Database Query](../../the-function-stack/functions/database-requests/external-database-query.html)
            -   [Direct Database Query](../../the-function-stack/functions/database-requests/direct-database-query.html)
            -   [Get Database Schema](../../the-function-stack/functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../../the-function-stack/functions/data-manipulation/create-variable.html)
            -   [Update Variable](../../the-function-stack/functions/data-manipulation/update-variable.html)
            -   [Conditional](../../the-function-stack/functions/data-manipulation/conditional.html)
            -   [Switch](../../the-function-stack/functions/data-manipulation/switch.html)
            -   [Loops](../../the-function-stack/functions/data-manipulation/loops.html)
            -   [Math](../../the-function-stack/functions/data-manipulation/math.html)
            -   [Arrays](../../the-function-stack/functions/data-manipulation/arrays.html)
            -   [Objects](../../the-function-stack/functions/data-manipulation/objects.html)
            -   [Text](../../the-function-stack/functions/data-manipulation/text.html)
                    -   [Security](../../the-function-stack/functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../../the-function-stack/functions/apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../../the-function-stack/functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../../the-function-stack/functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../../the-function-stack/functions/data-caching-redis.html)
        -   [Custom Functions](../../the-function-stack/functions/custom-functions.html)
        -   [Utility Functions](../../the-function-stack/functions/utility-functions.html)
        -   [File Storage](../../the-function-stack/functions/file-storage.html)
        -   [Cloud Services](../../the-function-stack/functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](../../the-function-stack/filters/manipulation.html)
        -   [Math](../../the-function-stack/filters/math.html)
        -   [Timestamp](../../the-function-stack/filters/timestamp.html)
        -   [Text](../../the-function-stack/filters/text.html)
        -   [Array](../../the-function-stack/filters/array.html)
        -   [Transform](../../the-function-stack/filters/transform.html)
        -   [Conversion](../../the-function-stack/filters/conversion.html)
        -   [Comparison](../../the-function-stack/filters/comparison.html)
        -   [Security](../../the-function-stack/filters/security.html)
            -   Data Types
        
        -   [Text](../../the-function-stack/data-types/text.html)
        -   [Expression](../../the-function-stack/data-types/expression.html)
        -   [Array](../../the-function-stack/data-types/array.html)
        -   [Object](../../the-function-stack/data-types/object.html)
        -   [Integer](../../the-function-stack/data-types/integer.html)
        -   [Decimal](../../the-function-stack/data-types/decimal.html)
        -   [Boolean](../../the-function-stack/data-types/boolean.html)
        -   [Timestamp](../../the-function-stack/data-types/timestamp.html)
        -   [Null](../../the-function-stack/data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](../../the-function-stack/additional-features/response-caching.html)
        
-   
    Testing and Debugging
    
    -   Testing and Debugging Function Stacks
    -   Unit Tests
    -   Test Suites

-   
    The Database
    
    -   Getting Started Shortcuts
    -   Designing your Database
    -   Database Basics
        
        -   [Using the Xano Database](../../the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](../../the-database/database-basics/field-types.html)
        -   [Relationships](../../the-database/database-basics/relationships.html)
        -   [Database Views](../../the-database/database-basics/database-views.html)
        -   [Export and Sharing](../../the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](../../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](../../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](../../ai-tools/mcp-builder/mcp-functions.html)
            -   Xano MCP Server

-   
    Build With AI
    
    -   Using AI Builders with Xano
    -   Building a Backend Using AI
    -   Get Started Assistant
    -   AI Database Assistant
    -   AI Lambda Assistant
    -   AI SQL Assistant
    -   API Request Assistant
    -   Template Engine
    -   Streaming APIs

-   
    File Storage
    
    -   File Storage in Xano
    -   Private File Storage

-   
    Realtime
    
    -   Realtime in Xano
    -   Channel Permissions
    -   Realtime in Webflow

-   
    Maintenance, Monitoring, and Logging
    
    -   Statement Explorer
    -   Request History
    -   Instance Dashboard
        
        -   Memory Usage
        
-   
    Building Backend Features
    
    -   User Authentication & User Data
        
        -   [Separating User Data](../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
            -   Webhooks
    -   Messaging
    -   Emails
    -   Custom Report Generation
    -   Fuzzy Search
    -   Chatbots

-   
    Xano Features
    
    -   Snippets
    -   Instance Settings
        
        -   [Release Track Preferences](release-track-preferences.html)
        -   [Static IP (Outgoing)](static-ip-outgoing.html)
        -   [Change Server Region](change-server-region.html)
        -   [Direct Database Connector](direct-database-connector.html)
        -   [Backup and Restore](backup-and-restore.html)
        -   [Security Policy](security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../metadata-api/tables-and-schema.html)
        -   [Content](../metadata-api/content.html)
        -   [Search](../metadata-api/search.html)
        -   [File](../metadata-api/file.html)
        -   [Request History](../metadata-api/request-history.html)
        -   [Workspace Import and Export](../metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../metadata-api/token-scopes-reference.html)
        
-   
    Xano Transform
    
    -   Using Xano Transform

-   
    Xano Actions
    
    -   What are Actions?
    -   Browse Actions

-   
    Team Collaboration
    
    -   Realtime Collaboration
    -   Managing Team Members
    -   Branching & Merging
    -   Role-based Access Control (RBAC)

-   
    Agencies
    
    -   Xano for Agencies
    -   Agency Features
        
        -   [Agency Dashboard](../../agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](../../agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](../../agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](../../agencies/agency-features/agency-profile.html)
        -   [Commission](../../agencies/agency-features/commission.html)
        -   [Private Marketplace](../../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](../../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](../../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](../../enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](../../enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](../../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](../../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](../../enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](../../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](../../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](../../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](../../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](../../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](../../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](../../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](../../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](../../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
-   
    Special Pricing
    
    -   Students & Education
    -   Non-Profits

-   
    Security
    
    -   Best Practices

[Powered by GitBook]

On this page

Was this helpful?

Copy

1.  [Xano Features](../snippets.html)
2.  Instance Settings

Direct Database Connector 
=========================

Establish a direct connection to your instance\'s PostgreSQL database

 

Note

Direct Database Connector is available as a paid add-on for our **Starter** plan or included with our **Pro** plan.

Database Connector is a premium add-on that is available for Launch and Scale plans. Please visit your Billing page for the most up-to-date pricing for this additional feature.

You have the option to connect your Xano instance\'s PostgreSQL database directly with an external application or service. This can be useful if there is a platform for manipulating your database that you prefer to use over the Xano interface, creating custom backup and restore solutions, or even performing data analytics.

Use care when accessing your database directly. This type of connection removes a significant portion of normal checks and balances for data validity that using Xano directly provides.

**Proceed with caution.**

**How to Access the Database Connector**

On your instance selection screen, click the ⚙️ icon, and in the panel that opens, choose Database Connector.

[![](../../_gitbook/imaged532.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fbva4pABZQRkdxaTFgEF8%252FCleanShot%25202023-08-16%2520at%252013.18.14.png%3Falt%3Dmedia%26token%3D3ebffa8a-ac22-48cf-9831-49d37795711e&width=768&dpr=4&quality=100&sign=b56ed3c&sv=2)][![](../../_gitbook/image1e1b.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FLH2VNwWcmVMhISoSzAAt%252FCleanShot%25202023-08-16%2520at%252013.21.19.png%3Falt%3Dmedia%26token%3D6be56cd2-6040-4aa0-b7fe-2dd53702998a&width=768&dpr=4&quality=100&sign=af506598&sv=2)]

The panel that opens is split into two sections, Details and Settings.

[![](../../_gitbook/imagee010.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FAyD90vNwvU2Olvpi9oOA%252FCleanShot%25202023-08-16%2520at%252013.22.58.png%3Falt%3Dmedia%26token%3D3a02f7da-8706-4f69-be55-a097282ffcd7&width=768&dpr=4&quality=100&sign=1659b479&sv=2)]

Details allows you to retrieve the access information for a direct database connection.

Settings allows you to enable and use an allow list, to limit direct database connections to specific IP addresses.

1.  
    
        
    
    Get your database\'s public IP
    
2.  
    
        
    
    Get your database credentials
    
3.  
    
        
    
    Settings Panel
    
4.  
    
        
    
    Add an IP address to your allow list
    
Clicking both of the \"Get\" buttons will provide us with the database IP and two sets of credentials, full-access and read-only.

[![](../../_gitbook/image204f.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FtDJ38RyZjDC9eQiwGROW%252FCleanShot%25202023-08-21%2520at%252007.47.08.png%3Falt%3Dmedia%26token%3Dd1a9a18c-c0cd-4da9-8b84-f0f629b9a90c&width=768&dpr=4&quality=100&sign=f17c368b&sv=2)]

From this panel, you can also **revoke and re-generate** your database credentials, should the need arise.

**Establishing a Database Connection (Example)**

You can use any application you\'d like that is capable of connecting to a PostgreSQL database. In this example, we\'ll be using Navicat.

Select \'Connection\' in the top-left, and fill in your credentials and the IP received from Xano.

[![](../../_gitbook/image8bac.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FFUiRBkNbG1G0TQL97a3C%252FCleanShot%25202023-08-16%2520at%252013.39.09.png%3Falt%3Dmedia%26token%3D65e31cd1-2a78-4034-8486-645a51b3011d&width=768&dpr=4&quality=100&sign=6188df4&sv=2)]

Click \'Save\' to save the connection. We can now navigate the PostgreSQL database from Xano using Navicat. We can even add / update data, run queries, etc\...

[![](../../_gitbook/imageb29a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FVOIm1fX5IgwBKIL7bUtd%252FCleanShot%25202023-08-16%2520at%252013.41.35.gif%3Falt%3Dmedia%26token%3D77716497-f44c-4896-a2f2-3bda1a11f951&width=768&dpr=4&quality=100&sign=782a399b&sv=2)]

 

Table Format

 

Table Formats - Only relevant for direct database connections

As of our **1.68 release (5/27/25)**, all new workspaces will default to the standard SQL column format for tables. For all workspaces created prior to that, read below.

Your tables can be created using one of two formats:

-   
    
        
    
    **JSONB format**

    -   
        
                
        
        This creates your tables with two columns:

        -   
            
                        
            
            `id` - the ID of the record
            
        -   
            
                        
            
            `jsonb` - contains a JSON representation of the entire record
                        
-   
    
        
    
    **Standard SQL format**

    -   
        
                
        
        This creates a more standard table layout. Instead of a jsonb column, each column is written separately.
            
If you are using the [Direct Database Connector](direct-database-connector.html), Standard SQL format is usually recommended.

###  

**When to Convert to Standard SQL Format:**

-   
    
        
    
    You need direct database connections with third-party tools that aren\'t friendly to JSONB format, such as Tableau or PowerBI
    
-   
    
        
    
    You want faster performance for non-indexed queries
    
-   
    
        
    
    You\'re frequently adding new fields (faster column additions)
    
-   
    
        
    
    You plan to use SQL analytics tools or run complex reports directly against your database
    
###  

**When to Keep JSONB Format:**

-   
    
        
    
    You\'re satisfied with current performance
    
-   
    
        
    
    You don\'t need direct database connections
    
###  

Converting Tables from JSONB to standard SQL

This change is **permanent**. Most users will not need to adjust these settings, and they only impact your experience if you are connecting to your database directly via third-party tools.

Using standard SQL does not mean you can\'t use JSONB --- you have the ability to mix and match table types, if you prefer. You can also still use JSON fields on any table type for more complex, dynamic field structure.

<div>

1

###  

From your workspace dashboard, click the settings icon in the upper-right corner, and click Settings.

2

###  

Scroll down to the Database Preferences section, and check the option to \'Use standard SQL columns for new tables\'

![](../../_gitbook/image772d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FDMaRjrbVYNffLkgmrUhu%252FCleanShot%25202025-05-22%2520at%252010.38.36.png%3Falt%3Dmedia%26token%3D3110d09c-e22b-434d-ab89-b73d371d9bba&width=768&dpr=4&quality=100&sign=32a5ed3&sv=2)

This setting must be enabled before you can convert existing tables to the new format.

3

###  

Convert your table(s) from your workspace settings, or the settings of any table.

From the migration panel, select any of the tables you\'d like to convert, and confirm your choices. The migration will begin immediately.

![](../../_gitbook/image4e5f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F74oa7AYUup5PuKSvoqle%252FCleanShot%25202025-05-22%2520at%252010.41.30.png%3Falt%3Dmedia%26token%3De5a64f8a-8449-4b6c-a95f-15479c39ac36&width=768&dpr=4&quality=100&sign=3d472f2f&sv=2)

</div>

 

Custom SQL Table Names

From your Workspace settings, you can enable **Custom SQL Table Names**.

By default, Xano assigns each table a SQL name in the format mvpw\_ (e.g., mvpw1\_3). This identifier works for direct access, but can be difficult to read or use with direct queries and database tools.

You can replace this with a custom SQL name to make queries more intuitive and improve compatibility with external connectors.

If you change a table\'s SQL name, be sure to update any queries that reference the old name to avoid breaking functionality.

Once you\'ve enabled **Custom SQL Table Names**, head to any database table\'s settings, and click Manage next to SQL Table Name.

![](../../_gitbook/imageb0a8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F3OrVjebY1Mt1TBHzARfn%252FCleanShot%25202025-05-22%2520at%252010.46.21.png%3Falt%3Dmedia%26token%3D83a80aa5-8f23-4ad1-8454-b37a011f7ac0&width=768&dpr=4&quality=100&sign=a6af9b63&sv=2)

![](../../_gitbook/image91fc.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FWQfO0O3xnkFxNl7l8bCD%252FCleanShot%25202025-05-22%2520at%252010.48.26.png%3Falt%3Dmedia%26token%3Dd348d638-a9f2-42bc-99a4-c6c596940bb6&width=768&dpr=4&quality=100&sign=ab27b65a&sv=2)

-   
    
        
    
    Leave the SQL Table Name field blank to use Xano's default SQL table name, which follows the format mvpw\<workspaceID\>\_\<tableID\> (e.g., mvpw1\_3).
    
```{=html}
<!-- -->
```
-   
    
        
    
    SQL table names must be globally unique across all workspaces.
    **Hint**: Use the Custom Prefix to ensure uniqueness across workspaces.
    
```{=html}
<!-- -->
```
-   
    
        
    
    Datasources automatically add a suffix based on their environment. For example, **users** becomes **users\_test** in the test datasource.
    
```{=html}
<!-- -->
```
-   
    
        
    
    To reuse the same base name across workspaces, use a workspace-specific prefix (e.g., projA\_users, projB\_users).
    

Last updated 1 month ago

Was this helpful?