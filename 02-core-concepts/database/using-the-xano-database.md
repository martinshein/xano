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
- crud
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
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'using-the-xano-database'
twitter:card: summary\_large\_image
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
    
    [ Create a Database Table](#create-a-database-table)

-   [Head to the database](#head-to-the-database)

-   [Add a new table](#add-a-new-table)

-   [Give your table a name and a description.](#give-your-table-a-name-and-a-description)

-   [Choose your primary key type.](#choose-your-primary-key-type)

-   [Add some tags.](#add-some-tags)

-   [Choose to add basic CRUD endpoints.](#choose-to-add-basic-crud-endpoints)

-   [Confirm your choices.](#confirm-your-choices)

-   [ Navigating the Table View](#navigating-the-table-view)

-   [ Adding a new field](#adding-a-new-field)

-   [ Field Options](#field-options)

-   [ Adding Data](#adding-data)

-   [Generate Test Data](#generate-test-data)

-   [Adding Data Manually](#adding-data-manually)

-   [ Additional Table Settings](#additional-table-settings)

Was this helpful?

Copy

1.  [The Database](../getting-started-shortcuts.html)
2.  Database Basics

Using the Xano Database 
=======================

**Hint**

Use the [✨][**AI Database Assistant**](../../xano-ai/ai-database-assistant.html) to create and update tables for you!

 

[👨‍🏭] Create a Database Table

<div>

1

###  

Head to the database

Click [![](../../_gitbook/imageaeef.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FOnBNb2bfrMwZ922KTxsH%252FCleanShot%25202024-12-14%2520at%252012.19.51.png%3Falt%3Dmedia%26token%3D5a96e263-c5cd-46dd-80d4-aef2f3d5ea03&width=300&dpr=4&quality=100&sign=eb38e7bc&sv=2)]in the left hand menu.

2

###  

Add a new table

Click [![](../../_gitbook/image4eca.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FHe5zLVBAhuO4jnw1eRge%252FCleanShot%25202024-12-14%2520at%252012.20.52.png%3Falt%3Dmedia%26token%3D652f4f8c-fec9-4a9e-a26a-faa4a6e0a3a7&width=300&dpr=4&quality=100&sign=23475cf2&sv=2)]in the top right corner.

Choose **Import Data** to [import data from a CSV file](../migrating-your-data/csv-import-and-export.html), or **Enter Data Manually** to start with an empty table where you can add your own data later, or generate sample data automatically.

If you\'re just starting out, we\'d recommend choosing **Enter Data Manually** and using the sample data generator. You can always import data later.

In the panel that opens, give your table a name and a description

3

###  

Give your table a name and a description.

When naming your table, it\'s considered best practice to use camelCase for multiple words, and to not use plurals in the table name. For example, a table of dog breeds would be named `dogBreed`

The description is just for you to make notes on what this table will contain, notable data constraints, or any other information you\'d like to store.

4

###  

Choose your primary key type.

The primary key is the ID of each record. Xano offers two types of primary keys to choose from.

 

When should you use Sequential, and when should you use UUID?

When designing your database structure in Xano, choosing the right identifier type is an important decision. Here\'s a straightforward guide to help you decide:

**Sequential IDs are best for:**

-   
    
        
    
    Performance-sensitive operations - they\'re faster to index and query
    
-   
    
        
    
    Human-friendly references - easier to communicate (\"Please check record \#42\")
    
-   
    
        
    
    Storage efficiency - they consume less space in your database
    
-   
    
        
    
    When chronological order matters - the sequence reveals creation order
    
-   
    
        
    
    Single-database applications where centralized ID generation works well
    
-   
    
        
    
    Systems that benefit from predictable numbering patterns
    
**Common use cases:** Customer IDs, order numbers, ticket systems, invoice numbers, internal record tracking

**UUIDs are best for:**

-   
    
        
    
    Distributed systems where multiple services create records independently
    
-   
    
        
    
    Data synchronization across different databases or systems
    
-   
    
        
    
    Preventing ID guessing or enumeration attacks
    
-   
    
        
    
    Frontend-first workflows where IDs need to be generated before server contact
    
-   
    
        
    
    Multi-region deployments with separate databases
    
-   
    
        
    
    When you don\'t want to expose information about record counts
    
-   
    
        
    
    Scenarios where data privacy is paramount
    
**Common use cases:** User accounts in modern applications, cross-system record tracking, session management, event logging in distributed architectures

Please note that there is **no support** for converting tables to / from different primary key types. However, this can be done with a manual migration to a new table.

Sequential (1, 2, 3\...)

A sequential identifier is just a sequence of whole numbers (1, 2, 3, etc\...).

Think of sequential IDs like numbered tickets at a deli counter. They start at 1 and count up one by one (2, 3, 4\...). Just like how the first customer gets ticket \#1, the first row in your database gets ID \#1. This system is straightforward but requires coordination - just as you can\'t have two deli counters giving out the same numbers (it would confuse customers), you need to ensure you\'re not creating duplicate IDs across different parts of your system.

UUID

A UUID is like the serial number on your electronics - something like \"550e8400-e29b-41d4-a716-446655440000\". It\'s longer and looks random, similar to how no two iPhone serial numbers are alike, even if they were made in different factories. This makes UUIDs particularly useful when you have data coming from multiple sources or need to merge databases - you don\'t have to worry about ID conflicts, just like how Apple doesn\'t need to check with Samsung about what serial numbers they\'re using.

Some users feel that using UUIDs is also more secure. UUIDs do provide some security benefits through obscurity - you can\'t easily guess other valid IDs by simply incrementing a number. If a website shows you order \#1234, you might guess that order \#1235 exists. But if you see order 550e8400-e29b-41d4-a716-446655440000, you can\'t easily guess other valid orders.

However, it\'s crucial to understand that using UUIDs is not a replacement for proper security measures. You should never rely on the difficulty of guessing IDs as your only security mechanism. Proper authentication and authorization should be in place regardless of ID type.

5

###  

Add some tags.

Tags in Xano can be applied to any object (tables, APIs, functions, etc\...) and are used to easily find related objects when searching your workspace.

6

###  

Choose to add basic CRUD endpoints.

Xano can provide you with some standard pre-built APIs for basic operations against this table. If you choose this option, you\'ll also want to supply an **API Group** for those endpoints to live in. You can always choose to generate these endpoints later, too.

7

###  

Confirm your choices.

Once you\'ve confirmed all of your settings are as you want them to be, click **Add Table**.

</div>

------------------------------------------------------------------------

 

[ℹ️] Navigating the Table View

Let\'s start with the top control bar.

![](../../_gitbook/imageabc9.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F806NJxSJjLBaHdAMtihT%252FCleanShot%25202024-12-14%2520at%252022.02.58.png%3Falt%3Dmedia%26token%3D9fc223f1-a7fa-4c9c-818b-e6626521b68f&width=768&dpr=4&quality=100&sign=4dcc1fc&sv=2)

[🧭] Navigation Controls

[![](../../_gitbook/imagecbf1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FucEQQ5SYZEPPXHC6pbhS%252FCleanShot%25202024-12-14%2520at%252022.03.27.png%3Falt%3Dmedia%26token%3Dc2cc78aa-6e42-4980-a516-7fd9e9234bc7&width=300&dpr=4&quality=100&sign=9d8b3389&sv=2)]Table name, ID, description, and tags

[![](../../_gitbook/image3446.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FwCOCni4b0RYLiEZuyVs6%252FCleanShot%25202024-12-14%2520at%252022.05.07.png%3Falt%3Dmedia%26token%3Ddfa0577c-0443-426a-9f4b-3c6545989cd3&width=300&dpr=4&quality=100&sign=62153761&sv=2)] Go back to your list of database tables.

[![](../../_gitbook/image137b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F7Y8jTvsDicjEE3Qm6mPu%252FCleanShot%25202024-12-14%2520at%252022.04.35.png%3Falt%3Dmedia%26token%3Db60586a2-bb58-49bb-b12b-8e6b4500bbc9&width=300&dpr=4&quality=100&sign=5f0a70c5&sv=2)] Refresh the list of records

[![](../../_gitbook/image85e6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F5Zoi2JA9OB901lgfsPR1%252FCleanShot%25202024-12-14%2520at%252022.06.50.png%3Falt%3Dmedia%26token%3D5fed8fa9-eb59-40b2-800b-4597af52e063&width=300&dpr=4&quality=100&sign=fd75baf8&sv=2)] Change the database view

[🔎] Searching, Filtering, and Sorting

[![](../../_gitbook/imageb61d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FatzxIQFe0VAI295SAdue%252FCleanShot%25202024-12-14%2520at%252022.09.18.png%3Falt%3Dmedia%26token%3D33bacad8-21c7-4346-b3ba-0cec0a10a827&width=300&dpr=4&quality=100&sign=25506e7c&sv=2)] Search for specific records

[![](../../_gitbook/image5057.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FMmvW6H42J6bc3v7egHjY%252FCleanShot%25202024-12-14%2520at%252022.09.43.png%3Falt%3Dmedia%26token%3D3f5a6bc7-3fc5-46f9-9ab4-a63c778b2ae6&width=300&dpr=4&quality=100&sign=c215115&sv=2)] Filter your records by certain conditions, such as \"all records with an ID greater than 100\"

[![](../../_gitbook/image5f7d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FPk7ww9YUFcKVSJQmrgVs%252FCleanShot%25202024-12-14%2520at%252022.10.38.png%3Falt%3Dmedia%26token%3D0ebf1856-fa97-429d-93a8-4b65e0175868&width=300&dpr=4&quality=100&sign=a1cb0d3d&sv=2)] Sort your database records

[![](../../_gitbook/imagede86.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FTT8QQwJS4kI8WJgKLGFX%252FCleanShot%25202024-12-14%2520at%252022.11.07.png%3Falt%3Dmedia%26token%3Dd4e32dee-6e46-42e4-bc69-3034277bf974&width=300&dpr=4&quality=100&sign=50464053&sv=2)] Hide database fields from view

[🧰] Tools and Advanced Controls

[![](../../_gitbook/image5ec5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FGb2T69aJBBKDG04IJol6%252FCleanShot%25202024-12-14%2520at%252022.14.59.png%3Falt%3Dmedia%26token%3D7b94fc79-1092-489b-bc48-e42910067070&width=300&dpr=4&quality=100&sign=676cb2b8&sv=2)] Cut, Copy, Paste, Undo, and Redo

[![](../../_gitbook/imageb13e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FgtcibtKkdWuJaXmXGP0P%252FCleanShot%25202024-12-14%2520at%252022.15.31.png%3Falt%3Dmedia%26token%3D665fe9bc-3a3e-4403-8876-5c0bb6040c50&width=300&dpr=4&quality=100&sign=c5ee1d76&sv=2)] Show Schema

[![](../../_gitbook/image74c1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FXBuic6AEs9V4rnd2qHOC%252FCleanShot%25202024-12-14%2520at%252022.16.43.png%3Falt%3Dmedia%26token%3Da2695cf7-fa29-4d65-8d26-f9400ce5d400&width=300&dpr=4&quality=100&sign=82ffdc82&sv=2)] Show References

[![](../../_gitbook/image2f8c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FQYOUtHQuGlK4L68QDh73%252FCleanShot%25202024-12-14%2520at%252022.17.36.png%3Falt%3Dmedia%26token%3Dde4b0133-1b59-4bd4-bb59-0eb88e4ac943&width=300&dpr=4&quality=100&sign=a6588579&sv=2)] Indexes

[![](../../_gitbook/image1def.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FCpwl9lZdVbS0T3A8dljb%252FCleanShot%25202024-12-14%2520at%252022.19.05.png%3Falt%3Dmedia%26token%3D68aeaa1f-12ad-48e8-a7f8-8205d9fc7e63&width=300&dpr=4&quality=100&sign=c3311d93&sv=2)] Review available keyboard shortcuts for the database view

Just below the control bar, you\'ll see your database records.

![](../../_gitbook/image2861.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FnZt0oHZj8BbIXIOynyAF%252FCleanShot%25202024-12-14%2520at%252022.32.26.png%3Falt%3Dmedia%26token%3D857b8373-e71b-4abb-b74c-cb4812a281c1&width=768&dpr=4&quality=100&sign=5c41d3cd&sv=2)

Use your mouse or arrow keys to navigate between records and individual cells.

![](../../_gitbook/imageb9fe.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Ff8GPL2uj7nVmqWDJGlx5%252FCleanShot%25202024-12-14%2520at%252022.34.26.gif%3Falt%3Dmedia%26token%3D54c00457-7a89-437e-90e4-0cb7854b2619&width=768&dpr=4&quality=100&sign=7b8517e7&sv=2)

To modify data, just select the cell and make your desired changes. They will be saved automatically.

![](../../_gitbook/imageba9d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fjrtz15dQctPga0c7Je6Z%252FCleanShot%25202024-12-14%2520at%252022.35.42.gif%3Falt%3Dmedia%26token%3D289cf1e9-6c9e-4040-b430-aef56f54fb60&width=768&dpr=4&quality=100&sign=5df1f8c9&sv=2)

[![](../../_gitbook/imagec27c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fp3OAUr0yxOn9s1omB3kx%252FCleanShot%25202024-12-14%2520at%252022.37.07.png%3Falt%3Dmedia%26token%3D50fda62d-ce59-4269-baff-a282969d135a&width=300&dpr=4&quality=100&sign=686402bb&sv=2)] Select one or more records by checking these boxes

[![](../../_gitbook/imageb796.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FfXe2Q4MccBMTTC4somPT%252FCleanShot%25202024-12-14%2520at%252022.38.28.png%3Falt%3Dmedia%26token%3D0eb48ea2-5858-4c7e-a662-0332dd186a96&width=300&dpr=4&quality=100&sign=64b1f69d&sv=2)] Open a card view of the selected record

[![](../../_gitbook/image3414.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FORGn2Jt0HdgQa8TtsW5D%252FCleanShot%25202024-12-14%2520at%252022.39.20.png%3Falt%3Dmedia%26token%3D72b6ea0a-0a9f-4461-808c-efd67ce99867&width=300&dpr=4&quality=100&sign=ac2cabab&sv=2)] Add a new field

------------------------------------------------------------------------

 

[➕] Adding a new field

 

When Working in Large Tables



Click the [![](../../_gitbook/image57c1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fcz1QOPP46cg6eyc87W9J%252FCleanShot%25202024-12-14%2520at%252022.57.46.png%3Falt%3Dmedia%26token%3D49c57df6-b4cc-48cd-bec5-4df1a21a98f3&width=300&dpr=4&quality=100&sign=10499f92&sv=2)] to add a new field, and choose the [type of field](field-types.html) you want to add from the panel that opens.

After you\'ve selected your desired field type, you will be presented with a number of options. You can review each one of them and what they mean below.

Setting

Required?

Description

Name

The name of the field you are creating

Description

Add additional details here

Data Structure

**Single** - Each record will only store one value in this field. This is the more common selection.
**List** - Each record can hold multiple values in this field. For example, if this was a table of authors, we might have a field that can store multiple books for each author.

Allow Nullable Values

A `null` value is similar to an empty value in that it represents \"nothing is here\", but it\'s still an actual value written to the record. Useful if you need to specifically check whether or not that field has data stored.

Format

For some field types, you can specify a format. This does not change the actual data being stored and is only used to enable easier viewing and editing for you inside of the table view.

Default Value

When adding new records, you can automatically populate a default value
^**Note:**^ ^If\ your\ field\ allows\ nullable\ values,\ they\ will\ auto-apply\ null\ to\ new\ records\ as\ a\ default\ value.\ Adding\ \'null\'\ to\ the\ default\ value\ field\ manually\ will\ be\ processed\ as\ text\ and\ have\ unintended\ results.^

**Note**

The settings listed below only impact your API endpoints that utilize the database link feature. This means that it is possible to make changes that break these rules via the database table view.

Setting

Required?

Description

Required

Determines whether or not this field is required when adding a record

Sensitive Data

Hide the contents of this field from certain areas, such as request history

Column Visibility

**Public** - The field will be available as an input
**Private** - This field will not appear in inputs
**Internal** - Hide this field from API inputs and responses

Custom Rules & Filters

See below.

####  

Custom Rules & Filters

For each field, you can apply various rules and filters to ensure that the data is stored in the format that you expect.

Filter Name

Purpose

min

Enforces a minimum number of required characters

max

Enforces a maximum number of required characters

startsWith

Enforces a prefix

endsWith

Enforces a suffix

prevent

Blacklists phrases

lower

Stores the value in all lowercase

upper

Stores the value in all uppercase

alphaOk

Whitelist certain alphanumeric characters

digitOk

Whitelist certain numbers

ok

Whitelist certain characters

pattern

Enforce a regex pattern

------------------------------------------------------------------------

 

[⚙️] Field Options

Right-click on the header of a field to access field-related settings and make adjustments to the options already detailed above, as well as some additional controls.

[![](../../_gitbook/image0bbd.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FB1H3SDGq60frHIaPUim3%252FCleanShot%25202024-12-15%2520at%252011.48.25.png%3Falt%3Dmedia%26token%3D0c865fe5-8e21-45bc-8dd7-77bc42ef9981&width=300&dpr=4&quality=100&sign=efc10769&sv=2)] Rename this field

Please note that renaming a field should be handled with care, as it may impact any function steps that reference that field.

You can click [![](../../_gitbook/image83c6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FWhDyKarFKgmgX39Sqj1E%252FCleanShot%25202025-02-10%2520at%252011.18.05.png%3Falt%3Dmedia%26token%3D17ed9cde-a7a9-41d5-a3ea-c0bb308b6f46&width=300&dpr=4&quality=100&sign=6017ff8e&sv=2)] when viewing a database table to open **Referenced By** and view any database operations that utilize that column first to understand where changes need to be made. In the screenshot below, we know we want to update the name column, so we can use **Referenced By** to find where it\'s used beforehand.

[![](../../_gitbook/imageb50c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FoZwVhJDhcQhh2OOwiAoc%252FCleanShot%25202025-02-10%2520at%252011.24.08.png%3Falt%3Dmedia%26token%3D7c66d6d6-c44c-4342-b978-e7675191ce5f&width=300&dpr=4&quality=100&sign=db0dacb2&sv=2)]

[![](../../_gitbook/image1840.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F0zGCEIEaFRWEDQXeBrKW%252FCleanShot%25202024-12-15%2520at%252011.50.54.png%3Falt%3Dmedia%26token%3Db3ed1075-6f49-45ad-9482-46b096b445fd&width=300&dpr=4&quality=100&sign=ca0500fa&sv=2)] Access field settings (the options detailed earlier in this document)

[![](../../_gitbook/image9ac0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FAZQutfbPAf004HA5w7fq%252FCleanShot%25202024-12-15%2520at%252011.51.29.png%3Falt%3Dmedia%26token%3D4c9369a4-0a89-456d-9929-b1f8c6e5cfa5&width=300&dpr=4&quality=100&sign=af0f2b09&sv=2)] Make a copy of this column

[![](../../_gitbook/image5bec.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FfXKwcrS0oz08Jt22qaqN%252FCleanShot%25202024-12-15%2520at%252011.51.51.png%3Falt%3Dmedia%26token%3D69c707fe-7147-4f77-aae0-7797050d9405&width=300&dpr=4&quality=100&sign=6281786f&sv=2)] Insert a new column directly after the selected column

[![](../../_gitbook/image628b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F2utdHNbHyqYQNXYkAuc2%252FCleanShot%25202025-03-07%2520at%252016.44.57.png%3Falt%3Dmedia%26token%3D7c1d6d67-a504-45af-93c7-2649c54f2dfe&width=300&dpr=4&quality=100&sign=1da854de&sv=2)] Reorder your database fields. This does not impact how the data is returned in your function stacks.

[![](../../_gitbook/image18fa.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fkm4dosvmUh8Nv1DebRlJ%252FCleanShot%25202024-12-15%2520at%252011.52.26.png%3Falt%3Dmedia%26token%3Deed11718-2764-4ae7-a105-d1ef52e972bc&width=300&dpr=4&quality=100&sign=e2109808&sv=2)] Change the data type of the column

Xano will attempt to convert the data in the column to the new data type, but because of potential variations between data types, and the specific data being converted, this may not always be successful. It is **always** recommended to create a new column instead.

[![](../../_gitbook/imaged02f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Ft2sRcf2vvOPpmIhzatgJ%252FCleanShot%25202024-12-15%2520at%252011.53.38.png%3Falt%3Dmedia%26token%3Df40fdd7b-d561-4db0-845f-b93b775763cb&width=300&dpr=4&quality=100&sign=44f4d809&sv=2)] Delete the column

Deleting a column is irreversible. Proceed with caution.

------------------------------------------------------------------------

 

[🔢] Adding Data

###  

Generate Test Data

After you\'ve created your database schema, you can generate some sample data to use right away by clicking [ ][🪄][**Generate Records** ]

This option is located at the **bottom** of your database records --- so, if you have no records, you should see it right at the top.

![](../../_gitbook/image8eb0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fb7pCv87PKoe2FoBjCqti%252FCleanShot%25202025-03-18%2520at%252009.52.47.png%3Falt%3Dmedia%26token%3D3f62d91f-83c8-472f-9c7f-06fe899d671a&width=768&dpr=4&quality=100&sign=9825b2df&sv=2)

The record generation will look at the name and the data type for each of your fields and try to auto-suggest what they should be filled with.

![](../../_gitbook/image2d11.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FtbUhbhsfMb0V3zBka2XI%252FCleanShot%25202025-03-18%2520at%252009.53.20.png%3Falt%3Dmedia%26token%3D3684a788-f5f6-447d-8b05-6c5e2d47bf58&width=768&dpr=4&quality=100&sign=8e867806&sv=2)

You can click on one of those data types to change what that field is populated with, or specific settings related to that data type.

![](../../_gitbook/image5ae7.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FYl8sDrk620HKfpqGc9UU%252FCleanShot%25202025-03-18%2520at%252009.54.50.png%3Falt%3Dmedia%26token%3D541899d5-4cef-4958-96d4-7a650110b2cf&width=768&dpr=4&quality=100&sign=b48b3f0a&sv=2)

In the bottom-right corner, you can change the number of records generated, up to 100 at a time.

When you\'re ready, click \"Generate\" and you should see your new sample data populated. You can always generate more records if you\'d like.

![](../../_gitbook/image5408.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FOCKzjqIRk2qDHVrxJ6pO%252FCleanShot%25202025-03-18%2520at%252009.56.43.png%3Falt%3Dmedia%26token%3D6ab3d3ce-4918-465f-8668-434c8055976d&width=768&dpr=4&quality=100&sign=1bf2a6a2&sv=2)

 

Hint

Want to clear out all of the sample data? There\'s a quick \"Clear All Records\" shortcut in the upper-right settings menu. **This will delete all records in the table in one swing.**

###  

Adding Data Manually

Click [![](../../_gitbook/image40a3.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FxSPCuoUJ621zILcSGMPE%252FCleanShot%25202025-03-18%2520at%252009.58.40.png%3Falt%3Dmedia%26token%3D5e7f14dc-eb61-423b-99cf-bff9f4820e30&width=300&dpr=4&quality=100&sign=7a8d3cd7&sv=2)]at the bottom of your existing records (if any) to add a new record.

The record will be created using any default values you\'ve specified in the field options, and you can click on each cell to fill it in manually.

You can also click [![](../../_gitbook/image366b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FMU8Rw3CrDixqIMw9iQc6%252FCleanShot%25202025-03-18%2520at%252009.59.43.png%3Falt%3Dmedia%26token%3D94c08f63-e995-4314-a362-a746f92019db&width=300&dpr=4&quality=100&sign=eb51883d&sv=2)]to open up the card view and fil in multiple, or all fields at once when creating a new record.

------------------------------------------------------------------------

 

[⚙️] Additional Table Settings

Click [![](../../_gitbook/image64e4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FF8QIn9psy3Vs1YjnDtrX%252FCleanShot%25202024-12-15%2520at%252012.14.22.png%3Falt%3Dmedia%26token%3D7a696d6d-eaa6-4529-8b77-3e86e4379e51&width=300&dpr=4&quality=100&sign=6c8aecb5&sv=2)]to access table settings after creation, including both settings detailed earlier in this document, as well as some additional options.

Setting Name

Description

Authentication

Determines whether or not this table is used for [user authentication](../../building-backend-features/user-authentication-and-user-data.html).

Security

Change the table GUID.

Versions

Xano maintains a version history of your table schema. You can roll back to a previous version of your schema if you\'ve made changes that you want to undo.
**Note**: This does not change the data in your table, only the fields. If you need to restore a backup of your table data, see [this document](../../xano-features/instance-settings/backup-and-restore.html).

Triggers

Access your database triggers.

Auto-complete

Access your auto-complete settings.

Clear all records

Deletes all records in the table. You can also choose to reset the primary ID back to 1 on tables that use a sequential ID.

Clone table

Cloning copies the table schema. Cloning **does not** copy existing data.

Export data

Export your table data using the current view as a CSV

Import data

Import records from a CSV [📖] [**Learn More**](../migrating-your-data/csv-import-and-export.html)

------------------------------------------------------------------------

 

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
            
If you are using the [Direct Database Connector](../../xano-features/instance-settings/direct-database-connector.html), Standard SQL format is usually recommended.

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

------------------------------------------------------------------------

 

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