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
title: 'tables-and-schema'
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
        
        -   [Release Track Preferences](../instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../instance-settings/change-server-region.html)
        -   [Direct Database Connector](../instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../instance-settings/backup-and-restore.html)
        -   [Security Policy](../instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](master-metadata-api.html)
        -   [Tables and Schema](tables-and-schema.html)
        -   [Content](content.html)
        -   [Search](search.html)
        -   [File](file.html)
        -   [Request History](request-history.html)
        -   [Workspace Import and Export](workspace-import-and-export.html)
        -   [Token Scopes Reference](token-scopes-reference.html)
        
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
    
    [Get Workspaces](#get-workspaces)

-   [Get Tables of a Workspace](#get-tables-of-a-workspace)

-   [Create Table and Add Schema One by One](#create-table-and-add-schema-one-by-one)

-   [Create an Index](#create-an-index)

-   [Create Table with Schema and an Index in One Call](#create-table-with-schema-and-an-index-in-one-call)

-   [Browse Content](#browse-content)

-   [](#undefined)

Was this helpful?

Copy

1.  [Xano Features](../snippets.html)
2.  Metadata API

Tables and Schema 
=================

The following are various examples of how to leverage the Metadata API to create and modify database tables including the schema and indexes included within them.

<div>

</div>

###  

Get Workspaces

Browse the workspaces of the instance. This API endpoint does not require any parameters. Retrieving the workspaces gives you information on the workspace name and ID. The workspace ID is particularly important for use in other Metadata API endpoints.

![](../../_gitbook/imagede47.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FY0gyroYWFpE6WbQofCZk%252FCleanShot%25202023-04-12%2520at%252014.54.55%25402x.png%3Falt%3Dmedia%26token%3D8f3b69ed-c404-4739-823a-60a543d71e6b&width=768&dpr=4&quality=100&sign=7431fe3c&sv=2)

Example response body:

Copy

``` 
[
  {
    "id": 1,
    "name": "my workspace 1",
    "description": ""
  },
  {
    "id": 3,
    "name": "test",
    "description": ""
  },
  {
    "id": 2,
    "name": "to do app",
    "description": "my to do app example"
  }
]
```

###  

Get Tables of a Workspace

Browse workspace tables. This API endpoint requires a workspace ID and will provide various information about each database table in a workspace, including database table ID, which is needed in various Metadata API endpoints.

![](../../_gitbook/image7696.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FTEwSXP5yfgzy1uZsi3sL%252FCleanShot%25202023-04-12%2520at%252015.19.51.png%3Falt%3Dmedia%26token%3D9809a1bb-4f71-4e01-9779-f009cdd9d8e9&width=768&dpr=4&quality=100&sign=f850b82e&sv=2)

Example response body:

Copy

``` 
[
  {
    "id": 7,
    "created_at": "2023-04-12 22:00:38+0000",
    "updated_at": "2023-04-12 22:00:42+0000",
    "name": "category",
    "description": "",
    "guid": "yu2eB8E0dSEtL6MbBPzzJUM06gA",
    "auth": false
  },
  {
    "id": 8,
    "created_at": "2023-04-12 22:00:51+0000",
    "updated_at": "2023-04-12 22:01:07+0000",
    "name": "items",
    "description": "",
    "guid": "eP9O-rD-7sGKpbLOEhdED6YGrmA",
    "auth": false
  },
  {
    "id": 1,
    "created_at": "2022-03-24 20:20:26+0000",
    "updated_at": "2022-03-24 20:20:26+0000",
    "name": "user",
    "description": "",
    "guid": "nTOiqqb31ecz1Te6v_3YMkfp5xc",
    "auth": true
  }
]
```

###  

Create Table and Add Schema One by One

First, create a new table in the desired workspace. The default request values suffice. In this example, first, we will create a table and then add schema individually. The Metadata API is capable of adding schema in bulk but that will be covered in another example.

![](../../_gitbook/image1485.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FRpVsEHJSf3Gg4Rz093zD%252FCleanShot%25202023-04-12%2520at%252015.40.34%25402x.png%3Falt%3Dmedia%26token%3Db617be79-06d2-48b0-8a70-c480da68b9e4&width=768&dpr=4&quality=100&sign=d4e1d507&sv=2)

Example response body:

Copy

``` 
{
  "id": 9
}
```

Taking the newly created database table ID, we can add schema 1 by 1 to the table.

1.  
    
        
    
    A text field called name.
    

![](../../_gitbook/image48fb.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FdPSax8mutQuFG5uQr1NQ%252FCleanShot%25202023-04-12%2520at%252016.05.20%25402x.png%3Falt%3Dmedia%26token%3D8b5fce43-a75b-4c95-b141-3ce2406a0a02&width=768&dpr=4&quality=100&sign=b2634580&sv=2)

Example response body:

Copy

``` 
{
  "name": "name"
}
```

Next, let\'s add an integer field called score with a default value of 30

![](../../_gitbook/image9936.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8GKU7UD2EJX3ThBq9FFh%252FCleanShot%25202023-04-12%2520at%252016.15.51%25402x.png%3Falt%3Dmedia%26token%3D664b80bc-40b9-4520-912d-63c8bff12d33&width=768&dpr=4&quality=100&sign=5b0566f5&sv=2)

As we execute these Metadata API calls, our new table in Xano is being created along with the new schema, one by one.

![](../../_gitbook/image952a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FjBMlF3OCyhr1N3q5KPLM%252FCleanShot%25202023-04-12%2520at%252016.24.07.png%3Falt%3Dmedia%26token%3Db9c29b52-9645-47ce-8ba5-78fc2cc8d467&width=768&dpr=4&quality=100&sign=6b0d8257&sv=2)

###  

Create an Index

The Metadata API gives control over indexes on database tables. In this example, let\'s create a Unique Index on the name field of new table 123.

![](../../_gitbook/image111d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FQaF8FvGmp7npFs8i2FDv%252FCleanShot%25202023-04-12%2520at%252016.27.18.png%3Falt%3Dmedia%26token%3D660b4812-ddb6-4a52-8d50-3680ad49d31e&width=768&dpr=4&quality=100&sign=6b9a6170&sv=2)

Example response body:

Copy

``` 
{
  "id": "baa524c4"
}
```

The API responds with the ID of the index. In Xano, we can see the index has been created:

![](../../_gitbook/image2950.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVFEm9xnlHNwUzGbrDsay%252FCleanShot%25202023-04-12%2520at%252016.27.52.png%3Falt%3Dmedia%26token%3D389f7b4f-0a28-4970-af0e-6b16feec3c82&width=768&dpr=4&quality=100&sign=60a64af0&sv=2)

###  

Create Table with Schema and an Index in One Call

In this example, we will create a new database table along with schema and an index in the same API call. The Metadata API is flexible enough to accommodate this method.

![](../../_gitbook/image6575.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FqI7o1l46LJfH40hYflhC%252FCleanShot%25202023-04-12%2520at%252017.10.58%25402x.png%3Falt%3Dmedia%26token%3D8ef3ab2e-e8b6-4321-bec9-943efe8a8c77&width=768&dpr=4&quality=100&sign=2da76440&sv=2)

Here\'s the example request body:

Copy

``` 
{
  "name": "new stuff",
  "description": "",
  "auth": null,
  "guid": null,
  "schema": [
    {
      "name": "id",
      "type": "int",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    },
    {
      "name": "created_at",
      "type": "timestamp",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    },
    {
      "name": "name",
      "type": "text",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    }
  ],
  "index":[
    {
      "type": "btree",
      "fields": [
        {
          "name": "name",
          "op": "desc"
        }
      ]
    }
  ]
}
```

This creates a new table called \"new stuff\" with three fields: id, created\_at, and name with an index on the name field.

For defining schema, the Metadata API needs a minimum of \"name\" and \"type\" but the other fields aren\'t required. If you are defining schema during table creation, the first field must be the ID field.

For Request body examples of schema and index, check out the PUT examples in Swagger for table/schema and table/index.

###  

Browse Content

Browse table content is a simple method of getting content (database records) in a database table. It requires a workspace ID and table ID, while paging is optional.

![](../../_gitbook/image1ddb.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FR226s9BJbb7tsj76l7Tt%252FCleanShot%25202023-04-12%2520at%252017.29.24.png%3Falt%3Dmedia%26token%3D23fea969-9db4-4f9f-8f46-c0228e20e42a&width=768&dpr=4&quality=100&sign=1ca79470&sv=2)

Example response body:

Copy

``` 
{
  "items": [
    {
      "id": 1,
      "created_at": 1681336868222,
      "name": "Basketball",
      "description": "round ball to shoot hoops",
      "category_id": 1
    },
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2
    },
    {
      "id": 3,
      "created_at": 1681336868658,
      "name": "Bluetooth Speaker",
      "description": "Portable music player",
      "category_id": 3
    },
    {
      "id": 4,
      "created_at": 1681336868931,
      "name": "Camera",
      "description": "Take photos with this",
      "category_id": 3
    }
  ],
  "itemsReceived": 4,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 4,
  "pageTotal": 1
}
```

###  

Last updated 6 months ago

Was this helpful?