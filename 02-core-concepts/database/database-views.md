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
description: 'Database Views are used to save filtering, sorting, and search options in your tables so that you can quickly return later.'
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'database-views'
twitter:card: summary\_large\_image
twitter:description: 'Database Views are used to save filtering, sorting, and search options in your tables so that you can quickly return later.'
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
        
        -   [Using the Xano Database](using-the-xano-database.html)
        -   [Field Types](field-types.html)
        -   [Relationships](relationships.html)
        -   [Database Views](database-views.html)
        -   [Export and Sharing](export-and-sharing.html)
        -   [Data Sources](data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../database-performance-and-maintenance/storage.html)
        -   [Indexing](../database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../database-performance-and-maintenance/schema-versioning.html)
        
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
        
        -   [Release Track Preferences](../../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](../../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../../xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](../../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../../xano-features/metadata-api/content.html)
        -   [Search](../../xano-features/metadata-api/search.html)
        -   [File](../../xano-features/metadata-api/file.html)
        -   [Request History](../../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](../../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../../xano-features/metadata-api/token-scopes-reference.html)
        
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

-   
    
    [ What are Database Views?](#what-are-database-views)

-   [ Using Database Views](#using-database-views)

-   [Use the options.](#use-the-options)

-   [Once you\'re ready, click the button.](#once-youre-ready-click-the-button)

-   [Click the View button again to see a list of your views and switch between them.](#click-the-view-button-again-to-see-a-list-of-your-views-and-switch-between-them)

Was this helpful?

Copy

1.  [The Database](../getting-started-shortcuts.html)
2.  Database Basics

Database Views 
==============

Database Views are used to save filtering, sorting, and search options in your tables so that you can quickly return later.

 

[❓] What are Database Views?

In your database, you can search, filter, and sort your records to view exactly the data you\'re looking for. Database Views allow you to save those settings in a view for easy access or sharing.

 

[📷] Using Database Views

<div>

1

###  

Use the [![](../../_gitbook/imagebc30.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FHWCLDZVd6scsfXwgwv0B%252FCleanShot%25202024-12-15%2520at%252019.15.23.png%3Falt%3Dmedia%26token%3D96eaa084-413f-4a32-b3b0-94eda87b20c2&width=300&dpr=4&quality=100&sign=22af70f4&sv=2)] options.

Search, filter, sort, and/or hide fields to get exactly the view you want.

![](../../_gitbook/image36be.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FwkUmSqXtjh1EGOxZSmXP%252FCleanShot%25202024-12-15%2520at%252019.16.16.png%3Falt%3Dmedia%26token%3Ddd928894-61fe-47d6-93fd-7adfd4340941&width=768&dpr=4&quality=100&sign=9fb76fb5&sv=2)

2

###  

Once you\'re ready, click the [![](../../_gitbook/image50b2.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FuwetopAASBEa4CgC8v10%252FCleanShot%25202024-12-15%2520at%252019.16.56.png%3Falt%3Dmedia%26token%3D7e44bc68-3d16-4eae-bac8-ac37ecf8c083&width=300&dpr=4&quality=100&sign=25910512&sv=2)] button.

Give your view a name and, if desired, an alias.

![](../../_gitbook/imagee21f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fme20DbDRikv2I6uITFK7%252FCleanShot%25202024-12-15%2520at%252019.18.05.png%3Falt%3Dmedia%26token%3D26233ebb-ad5f-4db6-aa7f-332647df508a&width=768&dpr=4&quality=100&sign=58d9f5bf&sv=2)

Take note of how the button in the control bar has changed. You\'ll now see the name of your view.

![](../../_gitbook/image2c18.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FiHnduUvRCt5BlxWyW3BM%252FCleanShot%25202024-12-15%2520at%252019.19.13.png%3Falt%3Dmedia%26token%3D9556e953-46e3-4420-8005-52fcf6833185&width=768&dpr=4&quality=100&sign=8176b4d&sv=2)

3

###  

Click the View button again to see a list of your views and switch between them.

![](../../_gitbook/imageba50.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FoTqNTUvJeJNRKUdvrzsN%252FCleanShot%25202024-12-15%2520at%252019.20.00.png%3Falt%3Dmedia%26token%3Dc7722494-2f7a-499d-802d-cfee0878b37a&width=768&dpr=4&quality=100&sign=61f982df&sv=2)

</div>

Some complex data types, like filtering by arrays, is not currently possible. If you\'re trying to filter something and not receiving the expected results, please reach out to support or use a [function stack](../../the-function-stack/functions/database-requests/query-all-records.html) instead.

Last updated 5 months ago

Was this helpful?