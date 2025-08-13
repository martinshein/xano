---
category: functions
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 08-reference/functions
tags:
- authentication
- api
- webhook
- trigger
- query
- transformation
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
    
    [Understanding Working with
    Data](#understanding-working-with-data)

-   [Database vs Variables](#database-vs-variables)

-   [Data in Functions](#data-in-functions)

-   [Data in Filters](#data-in-filters)

-   [Changing Variable Names](#changing-variable-names)

Was this helpful?

Copy

1.  [[🛠️]The Visual
    Builder](../building-with-visual-development.html)
2.  Building with Visual Development

Working with Data 
=================

 

Understanding Working with Data

When we talk about working with data in Xano, we are referring to
anything that touches a piece of data in your workflows --- whether it
is an API, custom function, task, or anything else. Data will typically
always be passing through these workflows, and it\'s important to
understand the various ways you can access and interact with this data.

 

Database vs Variables

The **database** is used to store information that you will need to
recall again later, and across workflows, such as:

-   
    
        
    
    User accounts
    
-   
    
        
    
    Product and order information
    
-   
    
        
    
    Blog posts or comments
    
**Variables** are used inside of individual workflows to store
information temporarily that you only need to finish the set of
functions being executed, such as:

-   
    
        
    
    The current date / time
    
-   
    
        
    
    Data from a database that needs temporary manipulation or
    transformation, such as combining a first and last name or
    calculating a discount
    
-   
    
        
    
    The output of individual functions in a function stack, like getting
    a record from a database table
    
 

Data in Functions

Most functions that you can add to a function stack will have some kind
of output available. The output of these functions are stored in a
**variable**.

In the screenshot shown below, we are using a get record function to
retrieve a record from our `author` table.
On the right side of that function, take note of return as
[**author1**]. This is the variable that the record we
retrieve is stored in, and what we will use to get that data in
subsequent functions.

![](../../_gitbook/image82da.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVIWWrnsoUKHFOlbNN7Va%252FCleanShot%25202025-02-10%2520at%252009.45.20.png%3Falt%3Dmedia%26token%3Dac5077cc-9c44-4871-95c6-48a34c6e4c7a&width=768&dpr=4&quality=100&sign=e2527c5d&sv=2)

When we add another function, we can reference
[**author1**] as shown below.

![](../../_gitbook/image4482.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FNNEzrYMPb5lUyxWlDn9I%252FCleanShot%25202025-02-10%2520at%252009.49.14.png%3Falt%3Dmedia%26token%3Dd446be26-1e16-46a4-898b-ebb91c2b2056&width=768&dpr=4&quality=100&sign=f3758633&sv=2)

 

Data in Filters

Filters are like mini-functions that can ride alongside other functions
in your function stack. They are used to perform a wide array of tasks
against a piece of data.

Our current function stack does nothing but retrieve a record from our
`author` table.

![](../../_gitbook/image06ea.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FCMenLr59zBjj5vQOnNhM%252FCleanShot%25202025-02-10%2520at%252009.51.30.png%3Falt%3Dmedia%26token%3D20faa2e6-ba57-41bc-b626-75cba16866d8&width=768&dpr=4&quality=100&sign=c2b63adc&sv=2)

Let\'s transform this data by changing the author\'s name to uppercase.
The simplest of data transformation happens in an **Update Variable**
function. Try it for yourself below.

 

Changing Variable Names

As you build your function stacks, you\'ll want to ensure you are naming
variables appropriately, so you can understand what they contain.

When adding a function, you\'ll usually have the option to set the
variable name.

![](../../_gitbook/imagef8b1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FG4B9XnFlBVOveaesEDJl%252FCleanShot%25202025-02-10%2520at%252010.12.32.png%3Falt%3Dmedia%26token%3Df36f1a43-115c-4dd1-8b5a-e989267d8d38&width=768&dpr=4&quality=100&sign=accb913f&sv=2)

If you need to change the variable name after you\'ve already referenced
the data elsewhere, Xano will ask you if you want to update the
references to that variable. In the below screenshot, after changing the
[**author1**] variable name, Xano lets us know that
the variable is already referenced in an **Update Variable** step, and
in our response. Click
[![](../../_gitbook/image8524.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FApE0eEZKCJXq3gKYkeG1%252FCleanShot%25202025-02-10%2520at%252010.15.14.png%3Falt%3Dmedia%26token%3Ddeb8607f-41cb-465c-b23f-c11c9f4429da&width=300&dpr=4&quality=100&sign=a6e9a9&sv=2)]to automatically change all of these to
reflect the new variable, or click [Skip] to leave them
the same. If you aren\'t sure which option to choose, more often than
not, you\'ll want to update the references.

![](../../_gitbook/image698e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FtsNZ2DQb8eqOABm6krlp%252FCleanShot%25202025-02-10%2520at%252010.14.08.png%3Falt%3Dmedia%26token%3D940d5834-4741-4c2d-8dbb-39863da6afb4&width=768&dpr=4&quality=100&sign=405a6473&sv=2)

Last updated 6 months ago

Was this helpful?