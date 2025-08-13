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
title: 'apple-mobile-web-app-status-bar-style: black'
---

---
apple-mobile-web-app-status-bar-style: black

color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'response-caching'
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
            
            -   [Swagger (OpenAPI Documentation)](../building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../building-with-visual-development/background-tasks.html)
        -   [Triggers](../building-with-visual-development/triggers.html)
        -   [Middleware](../building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../building-with-visual-development/working-with-data.html)
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
        
        -   [Response Caching](response-caching.html)
        
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

Was this helpful?

Copy


2.  Additional Features

Response Caching 
================

####  

Response Caching

[**Watch a practical example**](https://youtu.be/TTQky7FqRQE) of Response Caching using the [Star Wars API](https://swapi.dev/)

From the settings of an [API Endpoint](../building-with-visual-development/apis.html) or [Custom Function](../functions/custom-functions.html) response caching can be accessed. Response caching is an abstracted caching method to cache the response of an endpoint or function.

[![](../../_gitbook/image2acd.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MfjDlawtMnevbHx45uw%252F-MfjK_cyiFbXxTGORZLt%252Fcaching.png%3Falt%3Dmedia%26token%3D91dea8b1-08ec-4c0e-b820-843a5f31a09d&width=768&dpr=4&quality=100&sign=2f79e768&sv=2)]

You can choose from a number of different settings to determine how to cache the response.

[![](../../_gitbook/image26eb.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MfjDlawtMnevbHx45uw%252F-MfjLdGctLvT-WNeHBMp%252Fcaching%2520%281%29.png%3Falt%3Dmedia%26token%3D3b769e18-6e47-4fbc-9a5e-1cf5cce1b814&width=768&dpr=4&quality=100&sign=11aae88a&sv=2)]

**TTL** - Stands for time to live. This defines how long to cache the response for. Options range from 5 seconds to 7 days. After the TTL expires, the query will run normally and reset the response cache.

**Use inputs for caching signature** - This is defaulted to yes. It will create a response cache for each new or unique set of inputs for the duration of the TTL.

**Use IP address for caching signature** - This is defaulted to no. It can be used if you wish to record a response cache on a per IP address basis.

**HTTP Request Header Names** - This is optional. You are able to cache the HTTP request headers of the response. Add the request header name or names that you wish to cache.

**Environment Variable Names** - This is optional. It allows you to cache any defined [environment variable](../environment-variables.html) names to the response cache.

**Use Authentication ID for caching signature** - When an API endpoint requires [authentication](../../building-backend-features/user-authentication-and-user-data.html), this option becomes available. This can be turned on to enable a caching on a per user basis for authenticated endpoints.

[![](../../_gitbook/image5640.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MfoE9ds9tUfjoofzMUU%252F-MfoFDfB70ntclRxZDPd%252Fcaching%2520%282%29.png%3Falt%3Dmedia%26token%3D55616bd0-c466-4cb8-bb52-15270bac0cbb&width=768&dpr=4&quality=100&sign=b09d4684&sv=2)]

####  

Example Use Cases

**Use inputs and disable authentication ID for caching signature**

Company statistics for your entire team. If you need to display company statistics for your entire team then you may consider using inputs and disabling authentication ID for caching signature. You API endpoint would require authentication so that only your team can access the API but you would disable the authentication ID for caching. This would make it so the cache response is not on a per user basis. Since it is company statistics you want each user to see the same statistics. Using inputs enables each searched or inputted value gets cached, so if other team members search or input the same values then the response will already be there.

**Use inputs and use authentication ID for caching signature**

Personal statistics. In this scenario you would enable both inputs and authentication ID for caching signature. This would cache responses on a per user basis. For example, you might have each individual sales rep reviewing their own statistics for the quarter. Enabling inputs would cache the response for each inputted value. Additionally, enabling authentication ID for caching signature (with the appropriate business logic) would cache the responses on a per user basis.

**Disable inputs and disable authentication ID for caching signature**

There\'s a movie night event and you want to generate a random movie. Imagine you have an API that inputs a category or genre of movie and based on that, returns a random movie. By disabling both inputs and authentication ID for caching signature, this will allow for the first search on this API to generate a random movie to be played during movie night. It won\'t matter what other people search. So if the first person searched Science-Fiction and the result is Star Wars then all other searches (drama, action, comedy, etc.) will return Star Wars. Now you have your random movie for movie night.

Last updated 6 months ago

Was this helpful?