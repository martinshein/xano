---
category: custom-functions
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 05-advanced-features/custom-functions
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
- cache
- transaction
- function
- background-task
- custom-function
- rest
- database
title: '[![](../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2'
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
            
            -   [Swagger (OpenAPI
                Documentation)](apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async
                Functions](custom-functions/async-functions.html)
                    -   [Background Tasks](background-tasks.html)
        -   [Triggers](triggers.html)
        -   [Middleware](middleware.html)
        -   [Configuring
            Expressions](configuring-expressions.html)
        -   [Working with Data](working-with-data.html)
            -   Functions
        
        -   [AI Tools](../functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering
                    Examples](../functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get
                Record](../functions/database-requests/get-record.html)
            -   [Add
                Record](../functions/database-requests/add-record.html)
            -   [Edit
                Record](../functions/database-requests/edit-record.html)
            -   [Add or Edit
                Record](../functions/database-requests/add-or-edit-record.html)
            -   [Patch
                Record](../functions/database-requests/patch-record.html)
            -   [Delete
                Record](../functions/database-requests/delete-record.html)
            -   [Bulk
                Operations](../functions/database-requests/bulk-operations.html)
            -   [Database
                Transaction](../functions/database-requests/database-transaction.html)
            -   [External Database
                Query](../functions/database-requests/external-database-query.html)
            -   [Direct Database
                Query](../functions/database-requests/direct-database-query.html)
            -   [Get Database
                Schema](../functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create
                Variable](../functions/data-manipulation/create-variable.html)
            -   [Update
                Variable](../functions/data-manipulation/update-variable.html)
            -   [Conditional](../functions/data-manipulation/conditional.html)
            -   [Switch](../functions/data-manipulation/switch.html)
            -   [Loops](../functions/data-manipulation/loops.html)
            -   [Math](../functions/data-manipulation/math.html)
            -   [Arrays](../functions/data-manipulation/arrays.html)
            -   [Objects](../functions/data-manipulation/objects.html)
            -   [Text](../functions/data-manipulation/text.html)
                    -   [Security](../functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime
                Functions](../functions/apis-and-lambdas/realtime-functions.html)
            -   [External API
                Request](../functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda
                Functions](../functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching
            (Redis)](../functions/data-caching-redis.html)
        -   [Custom
            Functions](../functions/custom-functions.html)
        -   [Utility
            Functions](../functions/utility-functions.html)
        -   [File
            Storage](../functions/file-storage.html)
        -   [Cloud
            Services](../functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](../filters/manipulation.html)
        -   [Math](../filters/math.html)
        -   [Timestamp](../filters/timestamp.html)
        -   [Text](../filters/text.html)
        -   [Array](../filters/array.html)
        -   [Transform](../filters/transform.html)
        -   [Conversion](../filters/conversion.html)
        -   [Comparison](../filters/comparison.html)
        -   [Security](../filters/security.html)
            -   Data Types
        
        -   [Text](../data-types/text.html)
        -   [Expression](../data-types/expression.html)
        -   [Array](../data-types/array.html)
        -   [Object](../data-types/object.html)
        -   [Integer](../data-types/integer.html)
        -   [Decimal](../data-types/decimal.html)
        -   [Boolean](../data-types/boolean.html)
        -   [Timestamp](../data-types/timestamp.html)
        -   [Null](../data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response
            Caching](../additional-features/response-caching.html)
        
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
        
        -   [Using the Xano
            Database](../../the-database/database-basics/using-the-xano-database.html)
        -   [Field
            Types](../../the-database/database-basics/field-types.html)
        -   [Relationships](../../the-database/database-basics/relationships.html)
        -   [Database
            Views](../../the-database/database-basics/database-views.html)
        -   [Export and
            Sharing](../../the-database/database-basics/export-and-sharing.html)
        -   [Data
            Sources](../../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to
            Xano](../../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to
            Xano](../../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import &
            Export](../../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema
            Versioning](../../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting
            Clients](../../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP
            Functions](../../ai-tools/mcp-builder/mcp-functions.html)
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
        
        -   [Separating User
            Data](../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access
            (RBAC)](../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth
            (SSO)](../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
        
        -   [Release Track
            Preferences](../../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP
            (Outgoing)](../../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server
            Region](../../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database
            Connector](../../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and
            Restore](../../xano-features/instance-settings/backup-and-restore.html)
        -   [Security
            Policy](../../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit
            Logs](../../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano
            Link](../../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API
            (Deprecated)](../../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata
            API](../../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and
            Schema](../../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../../xano-features/metadata-api/content.html)
        -   [Search](../../xano-features/metadata-api/search.html)
        -   [File](../../xano-features/metadata-api/file.html)
        -   [Request
            History](../../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and
            Export](../../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes
            Reference](../../xano-features/metadata-api/token-scopes-reference.html)
        
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
        
        -   [Agency
            Dashboard](../../agencies/agency-features/agency-dashboard.html)
        -   [Client
            Invite](../../agencies/agency-features/client-invite.html)
        -   [Transfer
            Ownership](../../agencies/agency-features/transfer-ownership.html)
        -   [Agency
            Profile](../../agencies/agency-features/agency-profile.html)
        -   [Commission](../../agencies/agency-features/commission.html)
        -   [Private
            Marketplace](../../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a
                    Model](../../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant
            Center](../../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance
            Center](../../enterprise/enterprise-features/compliance-center.html)
        -   [Security
            Policy](../../enterprise/enterprise-features/security-policy.html)
        -   [Instance
            Activity](../../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access
            Control)](../../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano
            Link](../../enterprise/enterprise-features/xano-link.html)
        -   [Resource
            Management](../../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels
            slow](../../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels
            slow](../../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM
            Usage](../../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack
            Performance](../../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting
            Access](../../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of
            Conduct](../../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification
            Policy](../../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and
            Issues](../../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
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
    
    [What is a custom function?](#what-is-a-custom-function)

-   [Building and Using Custom
    Functions](#building-and-using-custom-functions)

-   [Access your custom functions from the left-hand
    menu.](#access-your-custom-functions-from-the-left-hand-menu)

-   [Click + Add Function to create a new custom
    function.](#click--add-function-to-create-a-new-custom-function)

-   [Build your custom function](#build-your-custom-function)

-   [Insert your new custom function into other function
    stacks.](#insert-your-new-custom-function-into-other-function-stacks)

-   [Creating Custom Functions from Existing Function
    Stacks](#creating-custom-functions-from-existing-function-stacks)

-   [Convert the entire stack](#convert-the-entire-stack)

-   [Select individual steps to convert to a
    function](#select-individual-steps-to-convert-to-a-function)

-   [Custom Function Settings](#custom-function-settings)

-   [From the Settings panel](#from-the-settings-panel)

-   [Custom Function Folders](#folders)

-   [Creating New Functions](#creating-new-functions)

-   [Creating New Folders with Existing
    Functions](#creating-new-folders-with-existing-functions)

-   [Moving Existing Functions into
    Folders](#moving-existing-functions-into-folders)

Was this helpful?

Copy

1.  [[🛠️]The Visual
    Builder](../building-with-visual-development.html)
2.  Building with Visual Development

Custom Functions 
================

Build business logic once and reuse it in multiple places

**Quick Summary**

Custom functions are very similar to your APIs --- they have inputs, a
function stack, and a response. However, they can not be called
externally. Instead, custom functions allow you to build something and
use it in other places, while maintaining it in a centralized location.

 

What is a custom function?

Custom functions can be thought of as a building block for the rest of
your backend. You can build a custom function just like an API endpoint,
and insert that custom function into other function stacks, giving you
easily reusable logic while only having to maintain it in one place.
When you make a change inside of a custom function, that change is
automatically in effect everywhere you have chosen to use the custom
function.

------------------------------------------------------------------------

 

Building and Using Custom Functions

<div>

1

###  

Access your custom functions from the left-hand menu.

![](../../_gitbook/image1807.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FgEcfLvgcqWPU227qJiz5%252FCleanShot%25202024-12-27%2520at%252014.31.52.png%3Falt%3Dmedia%26token%3D0f1be08c-18fd-4379-8651-5ef3a30fd2e2&width=768&dpr=4&quality=100&sign=ba41be63&sv=2)

2

###  

Click [ + Add Function ] to create a new custom function.

Give your custom function a **name**, **description**, **tags**, and
choose your [Request
History](../../maintenance-monitoring-and-logging/request-history.html) settings.

You can also choose to store your custom functions inside of a folder.
If the folder already exists, just start typing the name and select it
from the auto-complete. If the folder doesn\'t exist, you can create a
new one from here.

[![](../../_gitbook/imagea283.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVy86sQ4iLQRDhYi8h12c%252FCleanShot%25202025-05-19%2520at%252010.34.21.png%3Falt%3Dmedia%26token%3Df5bef25a-4ead-4416-bca0-459a812cb3b0&width=300&dpr=4&quality=100&sign=901fa413&sv=2)] When you\'re done, click [ Save
].

3

###  

Build your custom function

A custom function has three sections --- the same as an API endpoint.

###  

⬇️ Inputs

The inputs are anything that a function stack needs to run. For example,
a function stack that logs in a user probably needs a username or email
and a password; these would be the inputs.

###  

🔄 Function stack

This is where all of the magic happens. All of the business logic that
is performed lives here.

As you add functions to your function stack, it will suggest next steps
based on most popular user activity.

###  

⬆️ Response

Once the function stack has done its job, it needs to know what to
return. This lives in the Response section.

4

###  

Insert your new custom function into other function stacks.

When you\'re ready to use your new custom function in other function
stacks, click
[![](../../_gitbook/image1483.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8mhRxVQgPC8ALivf1ukI%252FCleanShot%25202024-12-27%2520at%252014.40.23.png%3Falt%3Dmedia%26token%3Da1da8b0f-6a9c-4570-ba2c-0e31af42dba0&width=300&dpr=4&quality=100&sign=ea5d3e13&sv=2)], choose **Custom Functions** from the
panel that opens, and select your custom function.

You\'ll be able to supply data for any inputs the custom function is
expecting here.

![](../../_gitbook/imagec2c0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fv2BRzVhLgbbouzh1GfdH%252FCleanShot%25202024-12-27%2520at%252014.41.28.png%3Falt%3Dmedia%26token%3D4834c0d7-5740-49e5-8aaf-405ce46929b2&width=768&dpr=4&quality=100&sign=9e5e953e&sv=2)

</div>

------------------------------------------------------------------------

###  

Creating Custom Functions from Existing Function Stacks

If you have a function stack that you\'d like to convert into a custom
function, you can do so in one of the following ways.

<div>

1

###  

Convert the entire stack

Click the three dots in the upper-right corner and choose Convert To
Function

![](../../_gitbook/image8fff.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FtP9fFNkK70hkNfxARf6T%252FCleanShot%25202025-02-12%2520at%252012.13.55.png%3Falt%3Dmedia%26token%3Dba6d0b32-02d0-4f3c-8664-923b9f9c8b98&width=768&dpr=4&quality=100&sign=efd53dc5&sv=2)

2

###  

Select individual steps to convert to a function

You can select a group of steps and click
[![](../../_gitbook/image4556.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FHu4cFGVXWjUhp5NbFpVb%252FCleanShot%25202025-02-12%2520at%252012.16.11.png%3Falt%3Dmedia%26token%3Dadbd7f60-f90f-41f8-9b52-992e797612f1&width=300&dpr=4&quality=100&sign=a1513580&sv=2)]to convert those steps into a custom
function.

![](../../_gitbook/imageb455.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FGySMJTCFaZH6Z9s5e1pT%252FCleanShot%25202025-02-12%2520at%252012.14.46.gif%3Falt%3Dmedia%26token%3Db0829b2a-4ccb-4434-8b81-45c127e96403&width=768&dpr=4&quality=100&sign=17f02e63&sv=2)

</div>

------------------------------------------------------------------------

 

Custom Function Settings

###  

From the Settings panel

![](../../_gitbook/image522d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FmjI2kCsucENivoHsthRW%252FCleanShot%25202024-12-23%2520at%252009.56.20.png%3Falt%3Dmedia%26token%3Dc98faeba-9ced-4be2-8397-da89dcd32fc3&width=768&dpr=4&quality=100&sign=88874836&sv=2)

Name

Purpose

Name

The name of the custom function.

Description

An internal description, just for you.

Tags

Use tags to organize objects throughout your Xano workspace and find
them later

Request History

-   
    
        
    
    Inherit Settings

    -   
        
                
        
        Use whatever is set in your workspace branch defaults
            
-   
    
        
    
    Other

    -   
        
                
        
        Set specific request history settings for this function
            
[📖] [**Learn more about request
history**](../../maintenance-monitoring-and-logging/request-history.html)

Response caching

Cache the response and redeliver it during future runs [📖]
[**Learn more about response
caching**](../additional-features/response-caching.html)

------------------------------------------------------------------------

 

Custom Function Folders

You can organize your custom functions into folders for better
organization.

-   
    
        
    
    Folders are not required if you prefer not to use them. You can
    store all of your functions in folders, or use a combination of
    folders and no folders.
    
-   
    
        
    
    A folder requires having at least one function inside of it ---
    empty folders are not supported.
    
<div>

1

###  

Creating New Functions

When creating a new function, you\'ll be given the option to store it in
a folder.

Just start typing the name of the folder. If it exists, select it from
the auto-complete dropdown. If it doesn\'t exist, it will be created for
you.

![](../../_gitbook/image564e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fy1GbYqEQeKGSyR4SKQvD%252FCleanShot%25202025-05-19%2520at%252010.40.00.png%3Falt%3Dmedia%26token%3D5b9b35a9-8779-45d4-9051-60da3b6d2652&width=768&dpr=4&quality=100&sign=1568fc60&sv=2)

2

###  

Creating New Folders with Existing Functions

Click the [ Add Folder ] button to create a new folder
for your existing functions.

![](../../_gitbook/image8d84.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FpubxQSf14BGracAzLnbH%252FCleanShot%25202025-05-19%2520at%252010.41.03.png%3Falt%3Dmedia%26token%3D86141b18-ed79-44af-a7be-12bb0b3d622b&width=768&dpr=4&quality=100&sign=5d529489&sv=2)

Give your new folder a name, and use the autocomplete to select at least
one function to add to it.

![](../../_gitbook/imagefba2.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FrohIQGNNH2jLEwzMZvRs%252FCleanShot%25202025-05-19%2520at%252010.42.01.png%3Falt%3Dmedia%26token%3Ddea0f081-7d50-4463-a8fd-2bc47ecb4c25&width=768&dpr=4&quality=100&sign=ee12f939&sv=2)

3

###  

Moving Existing Functions into Folders

Select the functions to move by using the checkboxes on the left-hand
side, and click [ Move ]

![](../../_gitbook/image19fb.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F5meSDI60XK4p4RxlZfuQ%252FCleanShot%25202025-05-19%2520at%252010.44.42.png%3Falt%3Dmedia%26token%3D79ffd68c-6868-4c35-bad1-4015c3f20a1a&width=768&dpr=4&quality=100&sign=87f346ae&sv=2)

Type a new folder name, or add them to an existing folder. When you\'re
ready, click [ Save ]

![](../../_gitbook/image5366.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FvVEGTfZqVSLkbI0h7gWp%252FCleanShot%25202025-05-19%2520at%252010.45.29.png%3Falt%3Dmedia%26token%3D073d6d34-d093-4793-8bd2-3825e4737a53&width=768&dpr=4&quality=100&sign=e3919837&sv=2)

</div>

Last updated 2 months ago

Was this helpful?