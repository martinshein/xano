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
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'data-sources'
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
    
    [Creating Data Sources](#creating-data-sources)

-   [Access your data sources from the left-side navigation menu](#access-your-data-sources-from-the-left-side-navigation-menu)

-   [Add a new data source from the panel that opens](#add-a-new-data-source-from-the-panel-that-opens)

-   [Customize the new data source](#customize-the-new-data-source)

-   [Using Data Sources](#using-data-sources)

-   [Switching Data Sources](#switching-data-sources)

-   [Setting a Data Source as Active](#setting-a-data-source-as-active)

-   [Targeting Specific Data Sources](#targeting-specific-data-sources)

-   [Use the Set Data Source function](#use-the-set-data-source-function)

-   [Send a data source header in your request](#send-a-data-source-header-in-your-request)

-   [Send a URL argument in your request](#send-a-url-argument-in-your-request)

-   [Change the settings of the function stack](#change-the-settings-of-the-function-stack)

-   [Migrating Data Between Data Sources](#migrating-data-between-data-sources)

-   [Access the Migration panel](#access-the-migration-panel)

-   [Select the source and destination data source.](#select-the-source-and-destination-data-source)

-   [Select the tables to migrate.](#select-the-tables-to-migrate)

-   [Confirm your changes to begin the migration.](#confirm-your-changes-to-begin-the-migration)

Was this helpful?

Copy

1.  [The Database](../getting-started-shortcuts.html)
2.  Database Basics

Data Sources 
============

**Quick Summary**

Data sources are like separate versions of tables that contain different data sets --- typically, they are separated into **live** or **production** data, and **test** data. The advantage to using separate data sources is so when you are building or iterating on your backend functionality, your actual live data stays safe. All data sources share the same database schema. They only differ by allowing different copies of the database records.

In Xano, data sources are essentially different sets of tables within your application\'s database. These data sources are crucial because they provide a way to separate the actual, live data that your business relies on from the data you use for testing or development purposes. This separation is beneficial as it ensures that any changes you make while testing new features do not affect the actual operational data.

Data sources typically have two main variants: **live data** and **test data**. You can have as many data sources as you\'d like if additional separation makes sense for your backend. Live data is what your application uses in real-time---it's the actual data that reflects real-world activities. In contrast, test data is used for experimentation and development, allowing developers to try out new features or changes without risking the integrity of the live data. By keeping these data sources distinct, Xano enables businesses to safely innovate and enhance their backend functionality without compromising the data they depend on every day.

 

Creating Data Sources

<div>

1

###  

Access your data sources from the left-side navigation menu

![](../../_gitbook/image00a9.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fc5Kt1nfmJZ0AbP0sLXkg%252FCleanShot%25202025-01-02%2520at%252008.02.27.png%3Falt%3Dmedia%26token%3D7d0b3574-35ee-4dcc-a0b7-1f301072454a&width=768&dpr=4&quality=100&sign=80bd9518&sv=2)

2

###  

Add a new data source from the panel that opens

[![](../../_gitbook/imageb83d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FiPHbIil5oFS5BX3BbIyn%252FCleanShot%25202025-01-02%2520at%252008.04.38.png%3Falt%3Dmedia%26token%3D8c38498d-6002-430f-8571-d6055e181747&width=300&dpr=4&quality=100&sign=66e57b9d&sv=2)]

3

###  

Customize the new data source

![](../../_gitbook/imageda8e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F2tJfvZg3fM9pk4JNekm0%252FCleanShot%25202025-01-02%2520at%252008.04.38.png%3Falt%3Dmedia%26token%3Dedd2027e-607f-4468-95c3-14395344f530&width=768&dpr=4&quality=100&sign=96203796&sv=2)

Give it a name, and choose a distinct color to assign to the data source. The color assigned is important, as it is used throughout the Xano interface to remind you of the currently selected data source.

When you\'re done, click [![](../../_gitbook/imagec88d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FbaRJCxU3lFRQzn2mo1VI%252FCleanShot%25202025-01-02%2520at%252008.06.46.png%3Falt%3Dmedia%26token%3D44b3b4ef-f6e6-49e7-a7c3-21c0a16b9fc1&width=300&dpr=4&quality=100&sign=117de89c&sv=2)]

</div>

------------------------------------------------------------------------

 

Using Data Sources

###  

Switching Data Sources

When you switch data sources, any action you take in Xano such as running and debugging a function stack will target the selected data source. It is recommended to use a test data source whenever possible to avoid accidentally impacting live application data.

Switch your data source at any time by clicking the data source indicator in the left-side navigation.

This **does not** impact your live application; only the work you are performing inside of Xano.

###  

Setting a Data Source as Active

If you want your backend to use a different data source by default, select it from the data sources panel and choose [![](../../_gitbook/imaged3ff.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FyIGSITeNKe0TUF5ZTvfN%252FCleanShot%25202025-01-02%2520at%252008.16.43.png%3Falt%3Dmedia%26token%3Dbbe4a951-8b43-4e03-bc0c-7e105275bec1&width=300&dpr=4&quality=100&sign=e401e711&sv=2)]. All future activity, unless otherwise specified using one of the alternative methods below, will use the active data source.

Proceed with caution. Changing the active data source can have unintended consequences on your live application. You do not need to change the **active data source** to work with other data sources in Xano.

###  

Targeting Specific Data Sources

When running function stacks in Xano or calling them externally, you can target a specific data source a number of ways. If you do not specify a data source, Xano will use the

<div>

1

###  

Use the Set Data Source function

The **Set Data Source** function, located under **Utility Functions**, allows you to manually set a data source at any time. Any future database operations, such as reads and writes, will use the defined data source.

![](../../_gitbook/image8bc5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FzR1vIb6DAUvTcdNO0Ifh%252FCleanShot%25202025-01-02%2520at%252008.10.14.png%3Falt%3Dmedia%26token%3D83de53d3-b01a-49df-b535-f53ea714f0aa&width=768&dpr=4&quality=100&sign=c8963624&sv=2)

2

###  

Send a data source header in your request

If you\'re calling one of your Xano APIs externally, you can specify the data source to use in the request headers.

The header to send is as follows. Replace \'test\' with the name of the data source you wish to target.

Copy

``` 
X-Data-Source: test
```

3

###  

Send a URL argument in your request

If you don\'t have the ability to modify the request headers but still want to specify the data source in an external request, you can use a URL argument.

Copy

``` 
https://x1xx-abcd-efgh.a1.xano.io/api:x123abc/user?x-data-source=test
```

4

###  

Change the settings of the function stack

In some function stack types, such as background tasks, you can set the data source to target if you would like it to be different from the live data source.

![](../../_gitbook/imagea248.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F7mIHeUIRkpbMnOBstjPU%252FCleanShot%25202025-01-02%2520at%252008.18.59.png%3Falt%3Dmedia%26token%3D575200e9-aca3-448f-8cbd-ac57a3f8a91b&width=768&dpr=4&quality=100&sign=b23cb803&sv=2)

</div>

###  

Migrating Data Between Data Sources

<div>

1

###  

Access the Migration panel

Click the data sources indicator and choose [⚙️] **Manage Data Sources**. In the panel that opens, click Migrate.

2

###  

Select the source and destination data source.

![](../../_gitbook/image7162.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FguCJvhYFGbC6HUls8yUu%252FCleanShot%25202025-01-02%2520at%252008.38.28.png%3Falt%3Dmedia%26token%3D32f6e726-c8a1-48e1-a2e7-6f86f7f7fddd&width=768&dpr=4&quality=100&sign=40278691&sv=2)

3

###  

Select the tables to migrate.

![](../../_gitbook/imagee0c3.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FZSD8OLA0oHEXRNaWNAjF%252FCleanShot%25202025-01-02%2520at%252008.39.10.png%3Falt%3Dmedia%26token%3Dd4ee25d4-d48d-4aa8-b2d1-0a0a67cba9d8&width=768&dpr=4&quality=100&sign=35603817&sv=2)

4

###  

Confirm your changes to begin the migration.

You can check the progress of the migration via the indicator in the left-hand navigation. You\'ll also see a banner at the top of the screen once the migration has completed.

![](../../_gitbook/image33ac.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FufgxvFRR4AJT2K8Q9751%252FCleanShot%25202025-01-02%2520at%252008.40.28.png%3Falt%3Dmedia%26token%3D174b02b3-5937-4364-a95c-185272870815&width=768&dpr=4&quality=100&sign=78f38691&sv=2)

![](../../_gitbook/image5585.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FEDZb3H3GCyHQi9wWviNN%252FCleanShot%25202025-01-02%2520at%252008.40.53.png%3Falt%3Dmedia%26token%3Dc2d492e4-6aba-4ec4-884a-e0f91199d247&width=768&dpr=4&quality=100&sign=277bb489&sv=2)

</div>

Last updated 7 months ago

Was this helpful?