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
            
            -   [Swagger (OpenAPI Documentation)](swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../custom-functions/async-functions.html)
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
    
    [Accessing the Documentation](#accessing-the-documentation)

-   [Using the Documentation](#using-the-documentation)

-   [Review the API information shown.](#review-the-api-information-shown)

-   [Sending Authenticated Requests](#sending-authenticated-requests)

-   [Click to send a request to that API.](#click-to-send-a-request-to-that-api)

-   [Fill in any request body values or parameters necessary.](#fill-in-any-request-body-values-or-parameters-necessary)

-   [Click to send the test request.](#click-to-send-the-test-request)

-   [Additional Features](#additional-features)

-   [Defining Sample Inputs and Responses](#defining-sample-inputs-and-responses)

-   [Copy / Copy as cURL](#copy-copy-as-curl)

-   [JSON OpenAPI Spec](#json-openapi-spec)

Was this helpful?

Copy


2.  Building with Visual Development
3.  [APIs](../apis.html)

Swagger (OpenAPI Documentation) 
===============================

**Quick Summary**

Swagger documentation provides a standardized way to describe and visualize APIs, showing what requests they accept and what responses they return - like a detailed menu that shows all available options. It allows developers to understand, test, and integrate with APIs without needing to read through pages of technical documentation.

Xano automatically generates documentation for your APIs using [Swagger](https://swagger.io/docs/), which provides the information in a standardized format called [OpenAPI](https://www.openapis.org/). The documentation contains information like the API name, description, inputs, and expected response.

Using these standardized methods allows for easy import of your API information into other platforms, such as your frontend of choice, as well as AI chatbots and large-language models for development assistance. In addition, it provides you an easy way to send API specifications to other developers you might be working with, without giving them access to the rest of your Xano workspace.

 

Accessing the Documentation

Documentation is generated for each API group. At the top of the API group page, just click [![](../../../_gitbook/image9c6c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F59ByIuvkGigkOdT2dMnN%252FCleanShot%25202024-12-26%2520at%252009.16.30.png%3Falt%3Dmedia%26token%3Da7ae0bec-09b6-4154-aa16-acf1ebe4fef6&width=300&dpr=4&quality=100&sign=bada1070&sv=2)] to access the auto-generated documentation for that group.

![](../../../_gitbook/image25c6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FOooccxZDZOKwYoxsLXL1%252FCleanShot%25202024-12-26%2520at%252009.17.13.png%3Falt%3Dmedia%26token%3Dd1e844c4-b675-4ae4-9ee2-7311bf97bddb&width=768&dpr=4&quality=100&sign=ec8f1340&sv=2)

Locating the Swagger documentation

 

Using the Documentation

<div>

1

###  

Review the API information shown.

Each API will show you the method, the API name, and the description on the left side.
[![](../../../_gitbook/image8187.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FYCUesLHvHvWNxQOmyvFl%252FCleanShot%25202024-12-26%2520at%252011.48.54.png%3Falt%3Dmedia%26token%3Ddb296d1d-75cd-4d4c-96fe-4f535a31c965&width=300&dpr=4&quality=100&sign=3280a385&sv=2)]

On the right, you\'ll see a [🔓] icon if that API requires authentication.
[![](../../../_gitbook/image1338.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FxGfbK42rgIiAbWWfQfX6%252FCleanShot%25202024-12-26%2520at%252011.48.20.png%3Falt%3Dmedia%26token%3Da515eada-b94c-4b28-a228-2075ea1e5e41&width=300&dpr=4&quality=100&sign=e29c554f&sv=2)]

Click the `V` to interact with your API of choice.

2

###  

Sending Authenticated Requests

If any of the API(s) you want to interact with require authentication, click [![](../../../_gitbook/imageebbb.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FbQzPqI5VbA4ZvnpvrnwC%252FCleanShot%25202024-12-26%2520at%252011.51.24.png%3Falt%3Dmedia%26token%3Dbb09ea01-8c54-445f-8511-bad65197d8d2&width=300&dpr=4&quality=100&sign=7c147aaf&sv=2)]at the top of the page to supply an authentication token.

3

###  

Click [![](../../../_gitbook/imagee0ef.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FXMeRlhr99BitRjhiqHIz%252FCleanShot%25202024-12-26%2520at%252011.52.33.png%3Falt%3Dmedia%26token%3Dd42703ae-6b5a-4e1f-8a3d-ee7628efa510&width=300&dpr=4&quality=100&sign=3bc46eff&sv=2)]to send a request to that API.

4

###  

Fill in any request body values or parameters necessary.

![](../../../_gitbook/imagececa.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FA1YuPdLYjy26E1cpVjEq%252FCleanShot%25202024-12-26%2520at%252011.53.57.png%3Falt%3Dmedia%26token%3D5547aca5-a596-4a3b-8811-de5ea2871c0d&width=768&dpr=4&quality=100&sign=ff199607&sv=2)

5

###  

Click [![](../../../_gitbook/image139b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FUTiEUEtfOr4gsizVarsP%252FCleanShot%25202024-12-26%2520at%252011.54.39.png%3Falt%3Dmedia%26token%3Ddc341123-4722-4c22-8dd8-1fa60cbb7ec4&width=300&dpr=4&quality=100&sign=f2422238&sv=2)] to send the test request.

You can review the response given below.

![](../../../_gitbook/imagecfb4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FNKybpyECMhByhaQOkOnU%252FCleanShot%25202024-12-26%2520at%252011.55.32.png%3Falt%3Dmedia%26token%3De7302fa5-668d-4f8e-a58f-8801acce7e15&width=768&dpr=4&quality=100&sign=d4c62616&sv=2)

</div>

 

Additional Features

###  

Defining Sample Inputs and Responses

 

Note

We\'re currently rolling out this feature to all users as part of our next release. If you don\'t have it yet, you will soon! Hang tight.

When [testing your function stacks](../../../testing-debugging/testing-and-debugging-function-stacks.html) in Xano, you can define sample input and output examples for your Swagger documentation.

It is important that you do this to ensure that your documentation is as effective as possible, as well as for helping AI models understand what\'s expected when interacting with your APIs.

<div>

1

###  

In the \'response\' section of the Run panel, click [ Set As Example ]

![](../../../_gitbook/imagedbda.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FnwZdxVOKgC8rPEQEzsHo%252FCleanShot%25202025-04-21%2520at%252009.37.02.png%3Falt%3Dmedia%26token%3D17104cdc-1f4a-452a-87c8-bafe28b44c02&width=768&dpr=4&quality=100&sign=15e1131d&sv=2)

2

###  

Review the sample input and response, and make any necessary adjustments

Make sure these do not include any sensitive information.

![](../../../_gitbook/image000f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fx1S8lS4BSQRqv4LxyRqb%252FCleanShot%25202025-04-21%2520at%252009.38.01.png%3Falt%3Dmedia%26token%3Db4ff490a-9897-4a64-aece-be73ad23e1aa&width=768&dpr=4&quality=100&sign=b3730b6e&sv=2)

3

###  

Click [ Save ] and you will see these defined in your Swagger documentation.

![](../../../_gitbook/image9940.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fy1DxEup0oYhPLr7GAg0k%252FCleanShot%25202025-04-21%2520at%252009.43.22.png%3Falt%3Dmedia%26token%3D168242e3-98b6-4b02-9889-58d4a1ec2c8f&width=768&dpr=4&quality=100&sign=d50b4e35&sv=2)

If you need to make adjustments later, you can do so from the settings menu.

![](../../../_gitbook/image1d86.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F0neNgATxiv1nHsfbVj0q%252FCleanShot%25202025-04-21%2520at%252009.42.32.png%3Falt%3Dmedia%26token%3D41107822-d29c-4b44-8b2b-976a1131a91c&width=768&dpr=4&quality=100&sign=ee46b0c5&sv=2)

</div>

###  

Copy / Copy as cURL

Throughout the documentation, you\'ll see [![](../../../_gitbook/image95e8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FRR4MVMKt7guBmuZziHPP%252FCleanShot%25202024-12-26%2520at%252011.56.34.png%3Falt%3Dmedia%26token%3De202fe35-d942-48b3-8717-21aa0c8344e0&width=300&dpr=4&quality=100&sign=31897b1f&sv=2)] icons. These will let you quickly copy the contents of that element, and in the presence of a cURL command, copy that command to quickly paste into a terminal or other API / testing platform of choice, such as [Postman](https://www.postman.com/).

###  

JSON OpenAPI Spec

![](../../../_gitbook/imagedc6f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FTbo2kVp55TtXS3GFj0bZ%252FCleanShot%25202024-12-26%2520at%252011.58.03.png%3Falt%3Dmedia%26token%3D77626bd2-a982-4300-a8ce-c31703d88ea4&width=768&dpr=4&quality=100&sign=e57cf2db&sv=2)

You can click the link at the top of the page to access a JSON-formatted version of your API spec. This is useful for other external platforms that rely on this type of standardized information about your APIs or providing to AI chatbots / LLMs.

Last updated 3 months ago

Was this helpful?