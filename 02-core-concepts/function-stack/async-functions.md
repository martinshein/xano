---
category: function-stack
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/function-stack
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
title: '[![](../../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv'
---

[![](../../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)![](../../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)](../../../index.html)















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
            
            -   [Swagger (OpenAPI Documentation)](../apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](async-functions.html)
                    -   [Background Tasks](../background-tasks.html)
        -   [Triggers](../triggers.html)
        -   [Middleware](../middleware.html)
        -   [Configuring Expressions](../configuring-expressions.html)
        -   [Working with Data](../working-with-data.html)
            -   Functions
        
        -   [AI Tools](../../functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](../../functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../../functions/database-requests/get-record.html)
            -   [Add Record](../../functions/database-requests/add-record.html)
            -   [Edit Record](../../functions/database-requests/edit-record.html)
            -   [Add or Edit Record](../../functions/database-requests/add-or-edit-record.html)
            -   [Patch Record](../../functions/database-requests/patch-record.html)
            -   [Delete Record](../../functions/database-requests/delete-record.html)
            -   [Bulk Operations](../../functions/database-requests/bulk-operations.html)
            -   [Database Transaction](../../functions/database-requests/database-transaction.html)
            -   [External Database Query](../../functions/database-requests/external-database-query.html)
            -   [Direct Database Query](../../functions/database-requests/direct-database-query.html)
            -   [Get Database Schema](../../functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../../functions/data-manipulation/create-variable.html)
            -   [Update Variable](../../functions/data-manipulation/update-variable.html)
            -   [Conditional](../../functions/data-manipulation/conditional.html)
            -   [Switch](../../functions/data-manipulation/switch.html)
            -   [Loops](../../functions/data-manipulation/loops.html)
            -   [Math](../../functions/data-manipulation/math.html)
            -   [Arrays](../../functions/data-manipulation/arrays.html)
            -   [Objects](../../functions/data-manipulation/objects.html)
            -   [Text](../../functions/data-manipulation/text.html)
                    -   [Security](../../functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../../functions/apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../../functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../../functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../../functions/data-caching-redis.html)
        -   [Custom Functions](../../functions/custom-functions.html)
        -   [Utility Functions](../../functions/utility-functions.html)
        -   [File Storage](../../functions/file-storage.html)
        -   [Cloud Services](../../functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](../../filters/manipulation.html)
        -   [Math](../../filters/math.html)
        -   [Timestamp](../../filters/timestamp.html)
        -   [Text](../../filters/text.html)
        -   [Array](../../filters/array.html)
        -   [Transform](../../filters/transform.html)
        -   [Conversion](../../filters/conversion.html)
        -   [Comparison](../../filters/comparison.html)
        -   [Security](../../filters/security.html)
            -   Data Types
        
        -   [Text](../../data-types/text.html)
        -   [Expression](../../data-types/expression.html)
        -   [Array](../../data-types/array.html)
        -   [Object](../../data-types/object.html)
        -   [Integer](../../data-types/integer.html)
        -   [Decimal](../../data-types/decimal.html)
        -   [Boolean](../../data-types/boolean.html)
        -   [Timestamp](../../data-types/timestamp.html)
        -   [Null](../../data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](../../additional-features/response-caching.html)
        
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
        
        -   [Using the Xano Database](../../../the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](../../../the-database/database-basics/field-types.html)
        -   [Relationships](../../../the-database/database-basics/relationships.html)
        -   [Database Views](../../../the-database/database-basics/database-views.html)
        -   [Export and Sharing](../../../the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](../../../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../../../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../../../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../../../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../../../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../../../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../../../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../../../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../../../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](../../../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](../../../ai-tools/mcp-builder/mcp-functions.html)
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
        
        -   [Separating User Data](../../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
        
        -   [Release Track Preferences](../../../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../../../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../../../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](../../../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../../../xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](../../../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../../../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../../../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../../../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../../../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../../../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../../../xano-features/metadata-api/content.html)
        -   [Search](../../../xano-features/metadata-api/search.html)
        -   [File](../../../xano-features/metadata-api/file.html)
        -   [Request History](../../../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](../../../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../../../xano-features/metadata-api/token-scopes-reference.html)
        
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
        
        -   [Agency Dashboard](../../../agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](../../../agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](../../../agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](../../../agencies/agency-features/agency-profile.html)
        -   [Commission](../../../agencies/agency-features/commission.html)
        -   [Private Marketplace](../../../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](../../../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](../../../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](../../../enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](../../../enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](../../../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../../../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](../../../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](../../../enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](../../../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](../../../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](../../../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](../../../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](../../../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](../../../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](../../../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](../../../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](../../../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
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
    
    [What are async functions?](#what-are-async-functions)

-   [When should I use async functions?](#when-should-i-use-async-functions)

-   [Enabling Async Execution](#enabling-async-execution)

-   [Insert a custom function into your function stack.](#insert-a-custom-function-into-your-function-stack)

-   [Click on the function to change the execution mode.](#click-on-the-function-to-change-the-execution-mode)

-   [If necessary, retrieve the output of the async function.](#if-necessary-retrieve-the-output-of-the-async-function)

Was this helpful?

Copy


2.  Building with Visual Development
3.  [Custom Functions](../custom-functions.html)

Async Functions 
===============

Use async functions to ensure that your custom functions execute exactly as you intend

 

What are async functions?

When working with custom functions in Xano, you can choose to have them execute asynchronously. An async function works like a [background task](../background-tasks.html), allowing your main process to continue without waiting for the custom function to finish.

 

When should I use async functions?

Asynchronous execution can be particularly beneficial in scenarios where you don\'t want certain tasks to hold up the entire process. For instance, if you\'re running a complex data fetch or a time-consuming operation, doing it asynchronously means your main application or interface remains responsive to user inputs while the background operation continues independently. This can enhance user experience by reducing wait times.

Here are a few examples of when to use async functions:

-   
    
        
    
    **Loading Data:** When fetching data from a server, such as pulling in user information or loading a list of products, async functions allow the page to display its initial content quickly without waiting for the entire data request to complete.
    
-   
    
        
    
    **File Uploads:** Starting a file upload process without freezing the interface lets users continue interacting with the application while the file is being processed.
    
-   
    
        
    
    **Notification Systems:** Sending notifications through email or messaging services asynchronously ensures that users continue their tasks without interruption while the messages are sent in the background.
    
 

Enabling Async Execution

<div>

1

###  

Insert a custom function into your function stack.

If you haven\'t built any custom functions yet, you can review our documentation on them [here](../../functions/custom-functions.html).

2

###  

Click [![](../../../_gitbook/imaged45f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FcU9uKnM8DP44r4mxwQ4f%252FCleanShot%25202025-02-13%2520at%252008.00.40.png%3Falt%3Dmedia%26token%3D058820b1-1f58-499c-a762-1405480283d7&width=300&dpr=4&quality=100&sign=11951ac7&sv=2)]on the function to change the execution mode.

3

###  

If necessary, retrieve the output of the async function.

If a function is set to async, it will return an ID that represents that execution, similar to the value shown below.

Copy

``` 
6f10cc09-d3e0-4ead-9a98-a0bc66bbe673
```

You can use the **Async Function Await** function to retrieve the output of the function once execution completes. Just provide it with an array of the ID(s) returned when the function runs.

![](../../../_gitbook/image08c1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FQVtuABYIeWtQUQ6sbS0S%252FCleanShot%25202025-02-13%2520at%252008.03.59.png%3Falt%3Dmedia%26token%3Da68aa1b2-3b12-478d-b1ba-8eef7a3cb86f&width=768&dpr=4&quality=100&sign=d0e19e64&sv=2)

</div>

Last updated 6 months ago

Was this helpful?