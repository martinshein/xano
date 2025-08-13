---
category: api-endpoints
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/api-endpoints
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
title: 'streaming-apis'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'

viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---

[![](../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)![](../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)](../index.html)















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
            
            -   [Swagger (OpenAPI Documentation)](../the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../the-function-stack/building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../the-function-stack/building-with-visual-development/background-tasks.html)
        -   [Triggers](../the-function-stack/building-with-visual-development/triggers.html)
        -   [Middleware](../the-function-stack/building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../the-function-stack/building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../the-function-stack/building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](../the-function-stack/functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](../the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../the-function-stack/functions/database-requests/get-record.html)
            -   [Add Record](../the-function-stack/functions/database-requests/add-record.html)
            -   [Edit Record](../the-function-stack/functions/database-requests/edit-record.html)
            -   [Add or Edit Record](../the-function-stack/functions/database-requests/add-or-edit-record.html)
            -   [Patch Record](../the-function-stack/functions/database-requests/patch-record.html)
            -   [Delete Record](../the-function-stack/functions/database-requests/delete-record.html)
            -   [Bulk Operations](../the-function-stack/functions/database-requests/bulk-operations.html)
            -   [Database Transaction](../the-function-stack/functions/database-requests/database-transaction.html)
            -   [External Database Query](../the-function-stack/functions/database-requests/external-database-query.html)
            -   [Direct Database Query](../the-function-stack/functions/database-requests/direct-database-query.html)
            -   [Get Database Schema](../the-function-stack/functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../the-function-stack/functions/data-manipulation/create-variable.html)
            -   [Update Variable](../the-function-stack/functions/data-manipulation/update-variable.html)
            -   [Conditional](../the-function-stack/functions/data-manipulation/conditional.html)
            -   [Switch](../the-function-stack/functions/data-manipulation/switch.html)
            -   [Loops](../the-function-stack/functions/data-manipulation/loops.html)
            -   [Math](../the-function-stack/functions/data-manipulation/math.html)
            -   [Arrays](../the-function-stack/functions/data-manipulation/arrays.html)
            -   [Objects](../the-function-stack/functions/data-manipulation/objects.html)
            -   [Text](../the-function-stack/functions/data-manipulation/text.html)
                    -   [Security](../the-function-stack/functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../the-function-stack/functions/apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../the-function-stack/functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../the-function-stack/functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../the-function-stack/functions/data-caching-redis.html)
        -   [Custom Functions](../the-function-stack/functions/custom-functions.html)
        -   [Utility Functions](../the-function-stack/functions/utility-functions.html)
        -   [File Storage](../the-function-stack/functions/file-storage.html)
        -   [Cloud Services](../the-function-stack/functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](../the-function-stack/filters/manipulation.html)
        -   [Math](../the-function-stack/filters/math.html)
        -   [Timestamp](../the-function-stack/filters/timestamp.html)
        -   [Text](../the-function-stack/filters/text.html)
        -   [Array](../the-function-stack/filters/array.html)
        -   [Transform](../the-function-stack/filters/transform.html)
        -   [Conversion](../the-function-stack/filters/conversion.html)
        -   [Comparison](../the-function-stack/filters/comparison.html)
        -   [Security](../the-function-stack/filters/security.html)
            -   Data Types
        
        -   [Text](../the-function-stack/data-types/text.html)
        -   [Expression](../the-function-stack/data-types/expression.html)
        -   [Array](../the-function-stack/data-types/array.html)
        -   [Object](../the-function-stack/data-types/object.html)
        -   [Integer](../the-function-stack/data-types/integer.html)
        -   [Decimal](../the-function-stack/data-types/decimal.html)
        -   [Boolean](../the-function-stack/data-types/boolean.html)
        -   [Timestamp](../the-function-stack/data-types/timestamp.html)
        -   [Null](../the-function-stack/data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](../the-function-stack/additional-features/response-caching.html)
        
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
        
        -   [Using the Xano Database](../the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](../the-database/database-basics/field-types.html)
        -   [Relationships](../the-database/database-basics/relationships.html)
        -   [Database Views](../the-database/database-basics/database-views.html)
        -   [Export and Sharing](../the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](../ai-tools/mcp-builder/mcp-functions.html)
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
        
        -   [Separating User Data](../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
        
        -   [Release Track Preferences](../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../xano-features/metadata-api/content.html)
        -   [Search](../xano-features/metadata-api/search.html)
        -   [File](../xano-features/metadata-api/file.html)
        -   [Request History](../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../xano-features/metadata-api/token-scopes-reference.html)
        
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
        
        -   [Agency Dashboard](../agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](../agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](../agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](../agencies/agency-features/agency-profile.html)
        -   [Commission](../agencies/agency-features/commission.html)
        -   [Private Marketplace](../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](../enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](../enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](../enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
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
    
    [Streaming API Request](#streaming-api-request)

-   [Streaming API Response](#streaming-api-response)

-   [Setting up a streaming response](#setting-up-a-streaming-response)

-   [Testing your Streaming Response](#testing-your-streaming-response)

Was this helpful?

Copy

1.  [Build With AI](using-ai-builders-with-xano.html)

Streaming APIs 
==============

###  

Streaming API Request

<div>

</div>

You can use the Streaming External API Request endpoint to call an API that returns a stream in almost exactly the same way as you call normal APIs from your function stacks. The only difference is the structure of data returned, which would typically be an array of items that you would leverage a For Each loop to work with.

###  

Streaming API Response

When delivering certain types of API responses, you may want to \'stream\' this response (similar to your favorite AI-powered chatbots). In Xano, this is possible with a simple combination of a For Each loop and a Streaming API Response function.

<div>

</div>

We\'ll be using a poem in the public domain to demonstrate the streaming response. You can copy the sample below and use it in your own function stacks to test.

Copy

``` 
["Two roads diverged in a yellow wood,","And sorry I could not travel both","And be one traveler, long I stood","And looked down one as far as I could","To where it bent in the undergrowth;","","Then took the other, as just as fair,","And having perhaps the better claim,","Because it was grassy and wanted wear;","Though as for that the passing there","Had worn them really about the same,","","And both that morning equally lay","In leaves no step had trodden black.","Oh, I kept the first for another day!","Yet knowing how way leads on to way,","I doubted if I should ever come back.","","I shall be telling this with a sigh","Somewhere ages and ages hence:","Two roads diverged in a wood, and I—","I took the one less traveled by,","And that has made all the difference."]
```

Data that you use for a streaming response needs to be separated into logical pieces. In this example, each item in the array is a new line in the poem. It would typically make the most sense to build a streaming response against an array just for ease of implementation.

###  

Setting up a streaming response

-   
    
        
    
    Set the API response type to \'streaming\' from the API settings, or choose the streaming option when creating a new API endpoint.
    [![](../_gitbook/image4c95.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FNZOLcN8oyu1L8v4L2x00%252FCleanShot%25202024-07-08%2520at%252007.56.07.png%3Falt%3Dmedia%26token%3D449ce627-314e-4080-a13d-3ade4e785783&width=300&dpr=4&quality=100&sign=70b130de&sv=2)]
    
-   
    
        
    
    In your function stack, once you have the data you want to stream ready to go, use a For Each loop to start looping against each item in your array.
    [![](../_gitbook/image18d0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FlOADi8t0RtajAohfvJ4r%252FCleanShot%25202024-07-08%2520at%252007.59.57.png%3Falt%3Dmedia%26token%3D5dd68489-56e0-4ce3-9850-91fc4a46439d&width=300&dpr=4&quality=100&sign=87ea9cf1&sv=2)]
    
-   
    
        
    
    Inside of the loop, use a **Streaming API Response** function to deliver each item inside of the array as the loop iterates through it.
    [![](../_gitbook/image1f5f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FFbC8C9IjZEC64yzpVNoQ%252FCleanShot%25202024-07-08%2520at%252008.00.51.png%3Falt%3Dmedia%26token%3D126ea6cc-51c4-4800-95d3-a6b4914525e4&width=300&dpr=4&quality=100&sign=4c29365d&sv=2)]
    
-   
    
        
    
    You can now test your streaming API, and should see each item in the array streamed as part of the response.
    

Please note that your front-end must support streaming responses. If it does not, the response can still be delivered traditionally.

Using Run & Debug will not display a stream, and only the entire response once the stream has completed.

###  

Testing your Streaming Response

####  

Testing in Postman

-   
    
        
    
    Create a new request with type HTTP
    
-   
    
        
    
    Paste your API endpoint URL in the URL input, and click Send.
    
-   
    
        
    
    You will see your API response delivered in the result panel.
    

![](../_gitbook/imagee0e6-2.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F7FiNQqHGZg5nLcL9VT7q%252FCleanShot%25202024-07-08%2520at%252008.11.35.gif%3Falt%3Dmedia%26token%3D6023031e-b9c2-452a-94e1-f21276d515b2&width=768&dpr=4&quality=100&sign=9e143f29&sv=2)

####  

Testing in Insomnia

-   
    
        
    
    Create a new request with type Event Stream
    
-   
    
        
    
    Paste your API endpoint URL in the URL input, and click Connect
    
-   
    
        
    
    You will see your API response delivered in the result panel.
    

![](../_gitbook/image861b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FoNYxIg2f7TpEDKgshXQM%252FCleanShot%25202024-07-08%2520at%252008.15.02.gif%3Falt%3Dmedia%26token%3D51819393-7b97-484e-ae06-62ac051cf5bd&width=768&dpr=4&quality=100&sign=d3ec6306&sv=2)

Last updated 6 months ago

Was this helpful?