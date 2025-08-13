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
            
            -   [Swagger (OpenAPI Documentation)](../building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../building-with-visual-development/background-tasks.html)
        -   [Triggers](../building-with-visual-development/triggers.html)
        -   [Middleware](../building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](database-requests/get-record.html)
            -   [Add Record](database-requests/add-record.html)
            -   [Edit Record](database-requests/edit-record.html)
            -   [Add or Edit Record](database-requests/add-or-edit-record.html)
            -   [Patch Record](database-requests/patch-record.html)
            -   [Delete Record](database-requests/delete-record.html)
            -   [Bulk Operations](database-requests/bulk-operations.html)
            -   [Database Transaction](database-requests/database-transaction.html)
            -   [External Database Query](database-requests/external-database-query.html)
            -   [Direct Database Query](database-requests/direct-database-query.html)
            -   [Get Database Schema](database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](data-manipulation/create-variable.html)
            -   [Update Variable](data-manipulation/update-variable.html)
            -   [Conditional](data-manipulation/conditional.html)
            -   [Switch](data-manipulation/switch.html)
            -   [Loops](data-manipulation/loops.html)
            -   [Math](data-manipulation/math.html)
            -   [Arrays](data-manipulation/arrays.html)
            -   [Objects](data-manipulation/objects.html)
            -   [Text](data-manipulation/text.html)
                    -   [Security](security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](apis-and-lambdas/realtime-functions.html)
            -   [External API Request](apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](data-caching-redis.html)
        -   [Custom Functions](custom-functions.html)
        -   [Utility Functions](utility-functions.html)
        -   [File Storage](file-storage.html)
        -   [Cloud Services](cloud-services.html)
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
    
    [How long can I store data in the Data Cache?](#how-long-can-i-store-data-in-the-data-cache)

-   [Caching Functions](#caching-functions)

-   [Set a Cache Value](#set-a-cache-value)

-   [Get a Cache Value](#get-a-cache-value)

-   [Has a Cache Value](#has-a-cache-value)

-   [Delete Cache Value](#delete-cache-value)

-   [Increment Cache Value](#increment-cache-value)

-   [Decrement Cache Value](#decrement-cache-value)

-   [Get Cache Keys](#get-cache-keys)

-   [Add to Beginning of List](#add-to-beginning-of-list)

-   [Add to End of List](#add-to-end-of-list)

-   [Remove from Beginning of List](#remove-from-beginning-of-list)

-   [Remove from End of List](#remove-from-end-of-list)

-   [Remove from List](#remove-from-list)

-   [Get Length of List](#get-length-of-list)

-   [Get Elements from List](#get-elements-from-list)

-   [Rate Limit](#rate-limit)

Was this helpful?

Copy


2.  Functions

Data Caching (Redis) 
====================

 

Quick Summary

Xano provides a data caching service, powered by Redis, that allows you to temporarily store data in memory for high-performance data retrieval and storage purposes. This is great for storing temporary data that needs to be quickly generated and accessed for a period of time.

If you are retrieving data from a database or an external API, for example, that you know never, or very infrequently, changes, using data caching can be incredibly valuable.

Data Caching functions require a **Starter plan** or higher.

###  

**How long can I store data in the Data Cache?**

Through the cache functions you use, you can manually set how long data gets stored, or you can expect it to naturally get overwritten once it reaches the 100MB limit**.**

**Note**

As mentioned above, **Data Caching is temporary storage** - so never store something that can\'t be recovered - if permanent storage is required, then the database can and should be used.

 

Caching Functions

###  

Set a Cache Value

Redis Cache Values work in key-value pairs. Set a Cache Value function allows you to define a key to reference the cache value in other cache functions. The data input is where you define the data you wish to be cached (the value of the pair). Ttl stands for time to live. Set this, in seconds, to determine how long to cache the data for.

**Key:** define a key name to reference the cache value by.

**Data:** select the value that you wish to cache. This will often be a variable containing data.

**TTL:** define how long, in seconds, for the cache to last. After this time expires, the query will run normally again and reset the data cache value for the specified time. Set this equal to 0 never reset the cache value.

Redis is extremely sensitive to data variation, so you may find it useful to store JSON objects as text strings for easier use of additional caching functions, such as \'removing from list\'.

[![](../../_gitbook/image7235.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FGpW4dbbV2urT7qQSRxtS%252FCleanShot%25202023-01-18%2520at%252010.28.56%25402x.png%3Falt%3Dmedia%26token%3Dbbc0dcf8-9b21-47b5-9641-887ea2e1c1fb&width=768&dpr=4&quality=100&sign=53e06ed8&sv=2)]

###  

Get a Cache Value

Get a Cache Value allows you to retrieve a cache value based on the defined key of a set cache value. Get a Cache Value function also outputs a variable so that you can use the data from the cache value in other functions or in the response.

**Key**: enter in the key of a set cache value that you wish to retrieve.

[![](../../_gitbook/image4f80.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FbnayJiAatBWmLa7GsiOg%252FCleanShot%25202023-01-18%2520at%252010.30.59%25402x.png%3Falt%3Dmedia%26token%3D6f95bb09-0165-4b52-88a5-f83e6a77ff3b&width=768&dpr=4&quality=100&sign=83d7d869&sv=2)]

###  

Has a Cache Value

Has a Cache Value allows you to determine whether or not a cache value exists based on the key. This function will return a boolean of true or false as a variable depending on if the cache value exists.

**Key**: enter a key to find if a cache value exists.

[![](../../_gitbook/image0854.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FHh0G1UvT33OUaKCwEWOF%252FCleanShot%25202023-01-18%2520at%252010.32.12%25402x.png%3Falt%3Dmedia%26token%3Dd441dd6f-8d55-4630-99a2-be3d77c3e5c3&width=768&dpr=4&quality=100&sign=eaa77fd7&sv=2)]

The return variable result will look like this:

[![](../../_gitbook/image3389.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MgCzLyJ23yW9rDCofuf%252F-MgDPeLKfhs45_dfxzco%252FUntitled%2520presentation%2520%2827%29.png%3Falt%3Dmedia%26token%3Db58aee95-7004-4d5d-9c6d-dfca969ac07c&width=768&dpr=4&quality=100&sign=888ae014&sv=2)]

Because the key \"user\_info\" has a cache value, the return variable is true.

###  

Delete Cache Value

Delete cache value will delete a cache value based on the key of the cache value.

**Key**: enter in the key of a set cache value in order to delete it.

[![](../../_gitbook/image63e3.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F3sApXBMV85eQJAVhfh4t%252FCleanShot%25202023-01-18%2520at%252010.33.22%25402x.png%3Falt%3Dmedia%26token%3Dfe9e3460-a413-47de-b28a-946eb96b6ac0&width=768&dpr=4&quality=100&sign=c144633b&sv=2)]

If we try to Get Cache Value for the same key after it is deleted, the response will come back as false.

[![](../../_gitbook/image93e1.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F77VhSIVYnleP3eLR0nXo%252FCleanShot%25202023-01-18%2520at%252010.34.45%25402x.png%3Falt%3Dmedia%26token%3D7b0757b5-286b-478f-a3c9-a6c5041e56ca&width=768&dpr=4&quality=100&sign=c4d26153&sv=2)]

In this example, we are doing a Get Cache Value for the same key that is being deleted in the prior step. We will try to return the return variable of the Get Cache Value.

[![](../../_gitbook/image8de0.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MgDPmj5FfQTTmYUCws-%252F-MgDSBsQxWUDWIZL2Fxl%252FUntitled%2520presentation%2520%2831%29.png%3Falt%3Dmedia%26token%3D002e21c4-6ab4-4226-a1a0-8fd70d531aa3&width=768&dpr=4&quality=100&sign=c50dc1aa&sv=2)]

The Get Cache Value returned a result of false because the cache value was already deleted.

###  

Increment Cache Value

Increment Cache Value allows you create an Incremental Cache Value by choosing a key and choosing the value to increment by. The incremented value is returned in a variable so you can perform logic based on what the count is.

**Key**: set a key name.

**By**: choose the value to increment by.

[![](../../_gitbook/imaged0a1.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FIeHH2hYnwhTa0dXcOfgF%252FCleanShot%25202023-01-18%2520at%252010.45.12%25402x.png%3Falt%3Dmedia%26token%3Dcba3eba3-0067-4899-9627-f3d76eaf2ae4&width=768&dpr=4&quality=100&sign=629ede67&sv=2)]

Increment Cache Value can act as a lightweight counter. The incremental values are stored on temporary memory, so keep in mind, if the server were to ever restart then the count would be reset.

Use case examples include a promotion where something is available or accessible for the first 100 users. Or perhaps, the 100th user wins the promotion.

###  

Decrement Cache Value

Decrement Cache Value allows you to decrement a cache value by choosing a key and a value to decrement it by. The decremented cache value is returned in a variable so you can perform additional logic based on its value.

**Key**: create a key name for the decrement cache value.

**By**: choose the value to decrement by.

[![](../../_gitbook/imaged46f.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FYk252ouGMMNb6kLr4xft%252FCleanShot%25202023-01-18%2520at%252010.45.44%25402x.png%3Falt%3Dmedia%26token%3Defe780fa-dca4-4675-b07b-e45b99e86167&width=768&dpr=4&quality=100&sign=2b44f06e&sv=2)]

Decrement cache value is similar to increment cache value but it decreases the value. You can also use this as a counter stored on temporary memory.

###  

Get Cache Keys

Get Cache Keys allows you to retrieve cache keys that match a searched value. You can use \"\*\" as a wildcard to search. Only putting in \"\*\" will grab all keys but you can combine it with with text string to narrow your search.

**Search**: enter in they name of the keys you are searching for. Use \"\*\" as a wildcard.

[![](../../_gitbook/image86a5.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FyXb6ESTOuHJ80H4TFLSo%252FCleanShot%25202023-01-18%2520at%252010.52.18%25402x.png%3Falt%3Dmedia%26token%3D7c9d45d4-419b-4d3b-9310-1e90d9f1e2c7&width=768&dpr=4&quality=100&sign=1f2c5785&sv=2)][![](../../_gitbook/image8e54.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FZGPl7sT35uqmVcep4O4i%252FCleanShot%25202023-01-18%2520at%252010.53.02%25402x.png%3Falt%3Dmedia%26token%3D51c0b5bc-6d51-41e8-83ae-cd0c4e582091&width=768&dpr=4&quality=100&sign=5d64dbda&sv=2)]

Here\'s an example of combining the wildcard \"\*\" with text to retrieve cache key.

[![](../../_gitbook/imagedbc5.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FzkIjzlAogRffBetzZP6M%252FCleanShot%25202023-01-18%2520at%252010.54.02%25402x.png%3Falt%3Dmedia%26token%3D029c8fed-9724-4ca8-9723-e681ea2c582b&width=768&dpr=4&quality=100&sign=91bcb39e&sv=2)]

###  

Add to Beginning of List

Add to Beginning of List allows you to insert a value at the start of the list stored at a key you specify.

**Key**: set a key name.

**Value**: the value to add to the beginning of the list.

[![](../../_gitbook/image5037.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FAdHjeyVF0NpFwax5htGH%252Fimage.png%3Falt%3Dmedia%26token%3D6839d361-22a8-43d4-8d67-ec7f68549a1b&width=768&dpr=4&quality=100&sign=e788da70&sv=2)]

###  

Add to End of List

Add to End of List allows you to insert a specified value at the tail end of the list, stored at the key you specify.

**Key**: set a key name.

**Value**: the value to add to the end of the list

[![](../../_gitbook/image501a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FIixKTRptIkGnvyCmHtRL%252Fimage.png%3Falt%3Dmedia%26token%3Dceff04f7-b80a-449f-b4a3-33da27414fbe&width=768&dpr=4&quality=100&sign=a5be8e59&sv=2)]

###  

Remove from Beginning of List

Allows you to remove the first element from a list stored at a key you specify.

**Key**: the key that you\'d like to remove the value from

[![](../../_gitbook/image0104.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Ff6O2LJ180H6cltqlhuIK%252Fimage.png%3Falt%3Dmedia%26token%3D522f7e76-dc36-456c-a25d-df610abaf373&width=768&dpr=4&quality=100&sign=31c5e864&sv=2)]

###  

Remove from End of List

Allows you to remove the last element from a list stored at a key you specify.

**Key**: the key that you\'d like to remove the value from

[![](../../_gitbook/image0104.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Ff6O2LJ180H6cltqlhuIK%252Fimage.png%3Falt%3Dmedia%26token%3D522f7e76-dc36-456c-a25d-df610abaf373&width=768&dpr=4&quality=100&sign=31c5e864&sv=2)]

###  

Remove from List

Allows you to remove a specified item from a list. You can choose to remove all specified values, or a maximum amount.

**Key**: the key that you\'d like to remove the value from

**Value**: the value you would like to remove

**Count**: the amount of values you want to remove. The default (0) will remove all, or you can specify a maximum.

[![](../../_gitbook/image176b.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FjIKYdKrozrFe9mXPNTup%252Fimage.png%3Falt%3Dmedia%26token%3De4806920-f85f-4457-8fe6-b0798f271a4b&width=768&dpr=4&quality=100&sign=8b35c133&sv=2)]

###  

Get Length of List

Allows you to return the current length of a list as a variable.

**Key**: specifies the key you would like to reference

[![](../../_gitbook/imagec3c8.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F9MTci4aIK5FWNUkdjcZi%252Fimage.png%3Falt%3Dmedia%26token%3D6269cfa7-f3ac-43b4-b2d7-5be2ba1dce64&width=768&dpr=4&quality=100&sign=ee9f7c5d&sv=2)]

###  

Get Elements from List

Allows you to retrieve a range of values from a list.

**Key**: specify which key you would like to reference.

**Start**: identifies the start of the elements you would like to retrieve.

**Stop**: identifies the end of the elements you would like to retrieve.

You can use negative values to represent the end of the list (ex. -1 is the last element, -2 is the second to last, and so on). The start and stop parameters are also inclusive. This means that the results you are given will include the elements at the positions you start and end with.

[![](../../_gitbook/image6c3d.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FLaIQEfn2KP1D4AD0UFIO%252Fimage.png%3Falt%3Dmedia%26token%3Da87cb43a-cdc7-45ad-9ba7-1bdfa180e94b&width=768&dpr=4&quality=100&sign=1da3dadd&sv=2)]

###  

Rate Limit

Xano allows you to set rate limits on your queries so that you can limit the requests per given time period that an API endpoint can be called.

The Rate Limit function comes with a few settings for configuration.

**Key**: define a key for the rate limit.

**Max**: set the max amount of requests allowed in the given time or TTL.

**TTL**: set the time to live, in seconds, of each cycle.

**Error**: optionally include an error message. If you include an error message, when the Rate Limit is reached it will automatically throw an error and display this message. If you do not, the Rate Limit will output a boolean of false when the Rate Limit is reached. This can be used if you wish to create custom logic for what happens when the Rate Limit is reached.

[![](../../_gitbook/imageca37.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F6Mms2pSXyw300CUgsSKZ%252FCleanShot%25202023-01-18%2520at%252010.55.09%25402x.png%3Falt%3Dmedia%26token%3Da63f82a5-22d2-4421-ba80-9931ab08778c&width=768&dpr=4&quality=100&sign=23fcb0da&sv=2)]

Last updated 1 month ago

Was this helpful?