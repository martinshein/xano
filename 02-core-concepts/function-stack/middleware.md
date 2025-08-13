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
- validation
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
            
            -   [Swagger (OpenAPI Documentation)](apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](custom-functions/async-functions.html)
                    -   [Background Tasks](background-tasks.html)
        -   [Triggers](triggers.html)
        -   [Middleware](middleware.html)
        -   [Configuring Expressions](configuring-expressions.html)
        -   [Working with Data](working-with-data.html)
            -   Functions
        
        -   [AI Tools](../functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](../functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../functions/database-requests/get-record.html)
            -   [Add Record](../functions/database-requests/add-record.html)
            -   [Edit Record](../functions/database-requests/edit-record.html)
            -   [Add or Edit Record](../functions/database-requests/add-or-edit-record.html)
            -   [Patch Record](../functions/database-requests/patch-record.html)
            -   [Delete Record](../functions/database-requests/delete-record.html)
            -   [Bulk Operations](../functions/database-requests/bulk-operations.html)
            -   [Database Transaction](../functions/database-requests/database-transaction.html)
            -   [External Database Query](../functions/database-requests/external-database-query.html)
            -   [Direct Database Query](../functions/database-requests/direct-database-query.html)
            -   [Get Database Schema](../functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../functions/data-manipulation/create-variable.html)
            -   [Update Variable](../functions/data-manipulation/update-variable.html)
            -   [Conditional](../functions/data-manipulation/conditional.html)
            -   [Switch](../functions/data-manipulation/switch.html)
            -   [Loops](../functions/data-manipulation/loops.html)
            -   [Math](../functions/data-manipulation/math.html)
            -   [Arrays](../functions/data-manipulation/arrays.html)
            -   [Objects](../functions/data-manipulation/objects.html)
            -   [Text](../functions/data-manipulation/text.html)
                    -   [Security](../functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../functions/apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../functions/data-caching-redis.html)
        -   [Custom Functions](../functions/custom-functions.html)
        -   [Utility Functions](../functions/utility-functions.html)
        -   [File Storage](../functions/file-storage.html)
        -   [Cloud Services](../functions/cloud-services.html)
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
        
        -   [Response Caching](../additional-features/response-caching.html)
        
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
    
    [What is middleware?](#what-is-middleware)

-   [Middleware Availability](#middleware-availability)

-   [How does middleware work?](#how-does-middleware-work)

-   [Types of Middleware](#types-of-middleware)

-   [Building Middleware](#building-middleware)

-   [Applying Middleware](#applying-middleware)

-   [Applying Middleware to your Entire Workspace](#applying-middleware-to-your-entire-workspace)

-   [From your workspace dashboard, click the icon to access the settings, and choose Middleware.](#from-your-workspace-dashboard-click-the-icon-to-access-the-settings-and-choose-middleware)

-   [Select the workflow type to apply the middleware to.](#select-the-workflow-type-to-apply-the-middleware-to)

-   [Apply PRE or POST middleware.](#apply-pre-or-post-middleware)

-   [Save your changes to apply the settings to the entire workspace by clicking ](#save-your-changes-to-apply-the-settings-to-the-entire-workspace-by-clicking)

-   [Applying Middleware to an API Group or Single API](#applying-middleware-to-an-api-group-or-single-api)

-   [Why use Middleware?](#why-use-middleware)

-   [Flexibility](#flexibility)

-   [Build Efficiency](#build-efficiency)

Was this helpful?

Copy


2.  Building with Visual Development

Middleware 
==========

 

Quick Summary

Middleware are separate pieces of logic that can run before something is executed, or just before it delivers a response (if applicable). It\'s designed for things like input validation, custom security or authentication implementations, logging, and output customization.

Middleware requires a **Starter plan** or higher.

 

What is middleware?

Middleware are separate pieces of logic that you build in Xano that can run before your API executes (even before input validation) or after your function stack is finished executing but before your API delivers its response.

Middleware can be applied at an API, API group, or workspace level. This means that you can apply the same middleware functionality to multiple API endpoints, or even your entire application, in one swing. You also have the ability to customize the middleware application at an API or API group level, meaning that if you want to apply your middleware to your entire application *except* a certain API or group, you can do that too.

Middleware offers the same functionality that any other function stack can utilize.

------------------------------------------------------------------------

 

Middleware Availability

Middleware is available in both **free** and **paid** versions.

**Free Version**

All of our paid plans can utilize the free version of Middleware. In the free version, you can create one Middleware function stack to assign as you see fit across your workspace.

**Paid Version**

The paid version of Middleware is included with our Scale plan. The premium version allows for unlimited creation and assignment of Middleware on APIs, functions, MCP tools, or tasks. Additional defaults are supported at the API group level, which can either be customized or inherited from workspace defaults.

If your plan includes the Compliance Center, you\'ll also be able to access reporting on middleware usage from there.

------------------------------------------------------------------------

 

How does middleware work?

###  

Types of Middleware

**Pre-Middleware**

Pre-middleware executes before any input validation takes place. For example, if you have one of your inputs built in such a way that it requires a minimum string length, your pre-middleware won\'t be aware of this.

 

Note

Pre-middleware will only surface **defined** inputs from the API it is attached to. This means for endpoints where the payload is unpredictable, you will need to ensure that all inputs are defined in the API.

**Post-Middleware**

Post-middleware executes after the function stack ends, but before the API delivers a response. The output of the middleware can be merged into the response your API generates, or replace it entirely.

![](../../_gitbook/imagef82b.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FcZUDXtitU6fdYDPw1H9c%252FCleanShot%25202024-01-16%2520at%252014.16.08.png%3Falt%3Dmedia%26token%3D7c722660-ff78-4839-b26b-dd33a1bb43b9&width=768&dpr=4&quality=100&sign=11bfee1a&sv=2)

A visual representation of middleware workflows

 

Building Middleware

From the left-side navigation, click [![](../../_gitbook/image5493.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FL5aYb8G7VdSMTJ3ZQhKC%252FCleanShot%25202025-01-03%2520at%252009.54.15.png%3Falt%3Dmedia%26token%3D7e12e0a1-bed0-41ba-af77-4d3e1dfc75b9&width=300&dpr=4&quality=100&sign=2bab6a13&sv=2)]and choose [![](../../_gitbook/imagedf49.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FoJ1MzfjOPI0EpFq0bCUt%252FCleanShot%25202025-01-03%2520at%252009.54.40.png%3Falt%3Dmedia%26token%3D39dfa7e1-b87d-4c0e-bcd5-2e37084a3b3b&width=300&dpr=4&quality=100&sign=1940e89b&sv=2)]to access your middleware.

Click the [![](../../_gitbook/imageae28.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FXN4UU2Ozxw10M0ns68hp%252FCleanShot%25202025-01-03%2520at%252009.55.03.png%3Falt%3Dmedia%26token%3D0b231a57-1a5a-474f-8e22-0d2f8f303ad0&width=300&dpr=4&quality=100&sign=96058c32&sv=2)] button in the top-right corner to add new middleware to your workspace. Give your Middleware a name, a description, and any tags you\'d like to apply, and proceed.

Once you\'ve added your middleware, you can begin building your logic, just like any other function stack. There are a couple of key differences to be aware of, however.

-   
    
        
    
    **Inputs**

    -   
        
                
        
        Middleware inputs are static and can not be changed. They will automatically contain the variables coming from the parent object. This means that for pre-middleware, the parent object will provide the inputs contained in the API request. For post-middleware, this will be your API response.
        
    -   
        
                
        
        When referencing those inputs, you will do so from inside the `vars` variable. So, if you send an input labeled `text`, you\'d reference this inside a middleware stack using `vars.text`
        
    -   
        
                
        
        The type contains whether this is running as pre or post middleware, and can not be changed.
            
-   
    
        
    
    **Response**

    -   
        
                
        
        Middleware responses have the option to either merge or replace the response in the parent object.

        -   
            
                        
            
            **Merge** means that middleware will generate its response and merge it with the response of the parent object. For example, if my API contains an input called `text` and my pre-middleware generates a variable called number, and my response type is set to **merge**, we could use a Get All Input function to retrieve those additional inputs. **Merge** also means that any items in the response that have the same name as your inputs will be replaced in the process, as you can not have two keys in a JSON object of the same name.
            
        -   
            
                        
            
            **Replace** means that your middleware will essentially ignore all of the inputs given to it **when it generates a response**. For example, if I am building pre-middleware, and I send it an input called \'text\', and it does not deliver that in the response, that \'text\' input will no longer be available in the API\'s function stack.
                        
-   
    
        
    
    **Exception Preferences**

    -   
        
                
        
        **Silent** ignores errors thrown in middleware and allows the API to return the response without returning the error encountered
        
    -   
        
                
        
        **Rethrow** allows post-middleware to execute for the purposes of error logging in your pre-middleware
        
    -   
        
                
        
        **Critical** halts all execution if an error occurs
            
For this example, we\'ll be using the following middleware:

![](../../_gitbook/image6d1d.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fzd811YXnKhJlsjk65Mdr%252FCleanShot%25202024-01-15%2520at%252015.56.53.png%3Falt%3Dmedia%26token%3D4810a3a5-39f0-49cc-83be-3053f96a394b&width=768&dpr=4&quality=100&sign=e5f74320&sv=2)

\...with the following API:

![](../../_gitbook/image2a5c.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FUVPDV6c7HWdN5ayilcFV%252FCleanShot%25202024-01-15%2520at%252015.57.43.png%3Falt%3Dmedia%26token%3D76766938-7dd4-4dd1-b0b3-f7408a220883&width=768&dpr=4&quality=100&sign=535302dc&sv=2)

The middleware is responsible for checking the \'text\' API to determine if it has a value of \"Hello\" before allowing access.

After you\'ve built your middleware, you\'re ready to apply it.

 

Applying Middleware

###  

**Applying Middleware to your Entire Workspace**

<div>

1

###  

From your workspace dashboard, click the [⚙️] icon to access the settings, and choose Middleware.

2

###  

Select the workflow type to apply the middleware to.

You can choose from APIs, Functions, or Tasks.

3

###  

Apply PRE or POST middleware.

Click [![](../../_gitbook/image8c53.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fb7OZTMNQ0wFpbc9BvUe9%252FCleanShot%25202025-01-03%2520at%252010.14.11.png%3Falt%3Dmedia%26token%3D24227df7-7bfb-416b-95ea-3e8be2aaaff7&width=300&dpr=4&quality=100&sign=1eba3fc8&sv=2)] or [![](../../_gitbook/imagea176.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fe1lNBoTBEIz7POy65X0Y%252FCleanShot%25202025-01-03%2520at%252010.14.35.png%3Falt%3Dmedia%26token%3Df0af0295-c353-438b-bfa4-f28a2fc2f5d6&width=300&dpr=4&quality=100&sign=69838997&sv=2)]to choose a middleware to apply, based on your needs.

4

###  

Save your changes to apply the settings to the entire workspace by clicking [![](../../_gitbook/image0f96.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F9Tz3iA4Xr9kcYfxKmRaG%252FCleanShot%25202025-01-03%2520at%252010.15.07.png%3Falt%3Dmedia%26token%3D0bc62848-2c41-4484-a709-7afad2588f1a&width=300&dpr=4&quality=100&sign=108bf79&sv=2)]

</div>

###  

**Applying Middleware to an API Group or Single API**

Middleware applications are inherited from their parent object. This means that any middleware you apply at a workspace level will be populated down to each API group and API. You do have the ability to customize the middleware on API groups and individual APIs for more granular control over the middleware that applies to that workflow.

Just click the settings icon inside of an API group or API, choose Middleware, and check the Customize box to update the middleware for that specific group or API.

![](../../_gitbook/image4692.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fsc9bWAGub0hcR75yNUg5%252FCleanShot%25202025-01-03%2520at%252010.16.43.png%3Falt%3Dmedia%26token%3De3ba3636-2688-41bb-8331-58f827dd50d0&width=768&dpr=4&quality=100&sign=b44cf824&sv=2)

 

Why use Middleware?

###  

Flexibility

Middleware can be much more flexible in certain scenarios, such as input validation. While Xano currently offers several basic filters for input validation, such as enforcing a certain number of characters, middleware offers the power of an entire function stack to not only validate those inputs in new ways, but even transform and manipulate them, should the need arise.

###  

Build Efficiency

One of the key benefits to using middleware, as opposed to using a custom function for example, is the methods at which middleware can be applied. Having the ability to insert both PRE and POST middleware in your function stacks offers more versatile and controlled execution of the logic contained within them.

Not only that, Middleware can also be applied at a workspace or API group level, giving you a one-swing approach to applying middleware to all of your API endpoints at once, instead of having to go through each API one at a time to apply a custom function.

Last updated 1 month ago

Was this helpful?