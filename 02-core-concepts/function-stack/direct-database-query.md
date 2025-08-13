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
            
            -   [Swagger (OpenAPI Documentation)](../../building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../../building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../../building-with-visual-development/background-tasks.html)
        -   [Triggers](../../building-with-visual-development/triggers.html)
        -   [Middleware](../../building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../../building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../../building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](../ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](query-all-records/external-filtering-examples.html)
                            -   [Get Record](get-record.html)
            -   [Add Record](add-record.html)
            -   [Edit Record](edit-record.html)
            -   [Add or Edit Record](add-or-edit-record.html)
            -   [Patch Record](patch-record.html)
            -   [Delete Record](delete-record.html)
            -   [Bulk Operations](bulk-operations.html)
            -   [Database Transaction](database-transaction.html)
            -   [External Database Query](external-database-query.html)
            -   [Direct Database Query](direct-database-query.html)
            -   [Get Database Schema](get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../data-manipulation/create-variable.html)
            -   [Update Variable](../data-manipulation/update-variable.html)
            -   [Conditional](../data-manipulation/conditional.html)
            -   [Switch](../data-manipulation/switch.html)
            -   [Loops](../data-manipulation/loops.html)
            -   [Math](../data-manipulation/math.html)
            -   [Arrays](../data-manipulation/arrays.html)
            -   [Objects](../data-manipulation/objects.html)
            -   [Text](../data-manipulation/text.html)
                    -   [Security](../security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../data-caching-redis.html)
        -   [Custom Functions](../custom-functions.html)
        -   [Utility Functions](../utility-functions.html)
        -   [File Storage](../file-storage.html)
        -   [Cloud Services](../cloud-services.html)
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
    
    [Finding your database identifier](#finding-your-database-identifier)

-   [Using Custom Aliases](#using-custom-aliases)

-   [Test Data](#test-data)

-   [Statement Arguments](#statement-arguments)

-   [SQL Query Wizard](#sql-query-wizard)

-   [What\'s the difference between Direct Database Query and Direct Database Access?](#whats-the-difference-between-direct-database-query-and-direct-database-access)

-   [Using the AI SQL Assistant](#using-the-ai-sql-assistant)

Was this helpful?

Copy


2.  Functions
3.  [Database Requests](../database-requests.html)

Direct Database Query 
=====================

The Direct Database Query function is available starting on the **upgraded** (non-Legacy) Launch or Scale plans. If you have any questions, please reach out to support.

To access the Direct Database Query function, add a new function to your function stack, choose Database Operations, and then Direct Database Query.

![](../../../_gitbook/image58d0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FvfQa1zdzvGIXXdahGSgU%252FCleanShot%25202023-05-22%2520at%252012.32.13.png%3Falt%3Dmedia%26token%3D0b3299e0-c97a-4c23-8c87-70d0597060fd&width=768&dpr=4&quality=100&sign=f60fcfc2&sv=2)

From the Direct Database Query panel, you can provide the following:

-   
    
        
    
    **Code** - This is the query you would like to perform
    
-   
    
        
    
    [**Statement Args**](direct-database-query.html#statement-arguments) - If you specify arguments using **?** in your code, you can use this section to sequentially fill in those arguments with other data, such as variables or inputs previously defined in your function stack
    
-   
    
        
    
    **Response Type** - Return either a single item, or a list of items
    
-   
    
        
    
    **Output Variable** - The name of the variable that will contain the result of the query
    

![](../../../_gitbook/image8e9a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FLhZcFGEANCxSgloEsmY4%252FCleanShot%25202023-05-22%2520at%252012.34.45.png%3Falt%3Dmedia%26token%3Df0719c9b-d7c8-4b13-9169-d001cceaba8f&width=768&dpr=4&quality=100&sign=5b2fdf93&sv=2)

###  

Finding your database identifier

The database identifier can be found by combining the workspace ID and database table ID with \'mvpw\'.

For example:
If workspace ID = 1 and ID = 3: `mvpw1_3`
If workspace ID = 500 and table ID = 3913: `mvpw500_3913`

Using the mvpw selector will return two columns: id and xdo, with xdo containing each record\'s content. For SELECT statements where you want to return specific columns, use \'x\' instead.

You can also use an **x identifier**, such as x1\_3, to return a more readable view of the data. Please note, however, that these views do not always have function parity with working with the mvpw\_ version of your tables (such as when performing inserts).

Using **x\_** is typically best when just performing queries.

![](../../../_gitbook/image31b8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FxTX0kAyuuBbK5hRcvRgd%252FCleanShot%25202023-05-25%2520at%252017.16.45.png%3Falt%3Dmedia%26token%3Dfe01fd92-2d97-4355-880e-acce135ee106&width=768&dpr=4&quality=100&sign=dbb1275d&sv=2)

Where to find your table ID and workspace ID

Direct Database Query allows you to query tables across your Instance. For example, if you are in workspace 2, you can query a table from workspace 1 using the above syntax. Please do so carefully to not misuse sensitive data in a query.

###  

Using Custom Aliases

You can leverage custom view aliases to make direct database queries easier to write, and more readable, based on exactly the data that you need.

Head to your database table, and create a [custom view](../../../the-database/database-basics/database-views.html). When creating your custom view, you can provide a **Database View Alias**, which you can use in your Direct Database Query statement.

In the screenshot below, we\'ve created a database view to filter people named David in our people table. When saving the view, we\'re providing an alias called \'david\'.

![](../../../_gitbook/imageb107.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FnxtTzJ3Wvoe5CAhkKQcT%252FCleanShot%25202024-03-18%2520at%252014.45.42.png%3Falt%3Dmedia%26token%3D7b9816f5-39dc-47c2-bbf3-3be39069f38b&width=768&dpr=4&quality=100&sign=8a7689ad&sv=2)

Once this view is saved, we can utilize it in a Direct Database Query function to retrieve the data from that view. The view is listed when using the Direct Query wizard, or you can type it manually if you are writing a query from scratch as `SELECT * from "view_name";`

![](../../../_gitbook/image8371.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FxFBJcETFC2wyXEY8U2JW%252FCleanShot%25202024-03-18%2520at%252014.47.47.png%3Falt%3Dmedia%26token%3D9ee2a63c-e4bc-42b3-a52e-70ed2f252d80&width=768&dpr=4&quality=100&sign=18bcb835&sv=2)

###  

Test Data

Assuming our data source is named \'test\', mvpw599\_2377 would become mvpw599\_test\_2377. You can replace \'test\' in this example with the name of your data source.

Direct Database Query does not respond to the selection of your data source in Xano or the data source specified in any external requests. You need to specifically state the test data source in the function. It is not possible at this time to dynamically modify the table selector.

###  

Statement Arguments

Statement arguments enable dynamic values in your queries. Statement arguments are designed to come from variables, inputs, or environment variables. A `?` in the query will identify where a statement argument should be placed; they will be placed in sequential order.

Statement arguments are escaped with single quotes by default.
In situations where you want to escape the argument value with double quotes, use `?:alias`.
To insert an argument value with no quotes, such as a table name, use `?:raw`.

Argument Type

Query Syntax

Result

Default

`?`

\'example\'

Alias

`?:alias`

\"example\"

Raw

`?:raw`

example

####  

Example:

In the following query, there are two statement arguments. The input `search` will be placed at the first `?` and the variable `var_1` will be placed at the second `?`.

![](../../../_gitbook/image741a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8fjb1DoTLfDW6KLrQ91p%252FCleanShot%25202023-06-19%2520at%252015.56.27.png%3Falt%3Dmedia%26token%3Dd248c17f-e7e1-4259-a733-3e4b3826505c&width=768&dpr=4&quality=100&sign=38db69ab&sv=2)

Arguments can not, at this time, be anything other than single values. Arguments can not also replace functions; they can only serve as query values at this time.

 

PREVENTING SQL INJECTION ATTACKS

Xano offers some filters to help ensure that any dynamic / user input is not parsed in a way that might harm your database or cause other unintended consequences.

Make sure to process your inputs **before** they are used in any SQL queries with the appropriate filter.

These filters are [sql\_alias and sql\_esc](../../filters/text.html#sql_alias)

###  

SQL Query Wizard

The SQL Query Wizard generates simple SQL queries. **It is not designed to support complex statements or joins but basic statements** to help get you started.

![](../../../_gitbook/image51b8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F32Ts3rad99ToNvU8fnh5%252FCleanShot%25202023-06-15%2520at%252017.10.04.png%3Falt%3Dmedia%26token%3D72bcb166-b128-4f1a-93e8-b6080fe540c0&width=768&dpr=4&quality=100&sign=319e791f&sv=2)

Open the Wizard Panel

####  

Step 1: Choose the Database Table to Query

![](../../../_gitbook/image4387.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FUcm30liawN6gmZNKNVdf%252FCleanShot%25202023-06-19%2520at%252010.10.42.png%3Falt%3Dmedia%26token%3Dc5eb9e69-a3bd-457f-94ef-0e63df27f417&width=768&dpr=4&quality=100&sign=7baf8b7c&sv=2)

####  

Step 2: Choose the field

![](../../../_gitbook/imagebd09.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FhOtxGV5wiU5gx9VE3yi3%252FCleanShot%25202023-06-19%2520at%252010.11.17.png%3Falt%3Dmedia%26token%3Db4b6a2c6-2334-4a0a-9ff9-0da07742e7e3&width=768&dpr=4&quality=100&sign=4d82a8df&sv=2)

####  

Step 3: Choose an operator and value.

![](../../../_gitbook/imagecae0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FRRuJmAIt96rd6lbbl6uB%252FCleanShot%25202023-06-19%2520at%252011.11.46.png%3Falt%3Dmedia%26token%3De1e9a640-2c57-4fb0-83f6-134f91b47a6d&width=768&dpr=4&quality=100&sign=af2b058e&sv=2)

Choose an operator for the query and add a value. Optionally include multiple conditions with AND or OR statements.

####  

Step 4: Select the columns to include in the query response.

![](../../../_gitbook/imagef036.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FsI7m2Uo98MKn30G1wlMT%252FCleanShot%25202023-06-19%2520at%252011.20.39.png%3Falt%3Dmedia%26token%3D266954b2-edb5-4c19-8dc4-ec6eec06253d&width=768&dpr=4&quality=100&sign=fbab9a62&sv=2)

The Wizard will process the settings and generate a SQL query in the code editor.

![](../../../_gitbook/image8f8c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FM3mnFRczIpDwUqoLvnQR%252FCleanShot%25202023-06-19%2520at%252011.21.25.png%3Falt%3Dmedia%26token%3D71251232-8052-4b1e-9c61-7d210552179f&width=768&dpr=4&quality=100&sign=a72c2c1&sv=2)

The result returns a list from merchant where desc = Pizza.

![](../../../_gitbook/image252d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FgaocicwGRzgw671WvXfE%252FCleanShot%25202023-06-19%2520at%252015.50.37.png%3Falt%3Dmedia%26token%3D5c04c01d-c8fd-4651-9ffc-8ee1c2e126e4&width=768&dpr=4&quality=100&sign=bf259b06&sv=2)

###  

What\'s the difference between Direct Database Query and Direct Database Access?

Direct Database Access is a premium add-on that allows you to connect directly to your Xano PostgreSQL database using an external tool. If you would like to leverage something outside of Xano to manage your database, direct database access is the feature you\'re looking for.

The Direct Database Query function in Xano is available if you want to simply run SQL queries from inside Xano.

 

Using the AI SQL Assistant

<div>

1

###  

When using the [Direct Database Query](direct-database-query.html) function, click [![](../../../_gitbook/image8fd5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fq2fTM69Ceqv2kvxBXNAe%252FCleanShot%25202025-02-26%2520at%252015.57.11%25402x.png%3Falt%3Dmedia%26token%3Dd1fc633c-743b-43ff-b183-4170708662bf&width=300&dpr=4&quality=100&sign=11e09b20&sv=2)] to access the AI SQL assistant.

The assistant can help you write queries against your Xano database.

2

###  

Provide the assistant with the query you would like it to build.

![](../../../_gitbook/imagec690.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FDArwNKh96mkjrtFG41u3%252FCleanShot%25202025-02-26%2520at%252016.02.55%25402x.png%3Falt%3Dmedia%26token%3D48f9a6f5-5deb-4f86-9d28-c634012d0241&width=768&dpr=4&quality=100&sign=2231b2af&sv=2)

3

###  

Once complete, the assistant will present you with the query, along with an explanation of how it works and some records that satisfy the query.

![](../../../_gitbook/image79ef.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FPvNThYNoZwRNi57UrdbM%252FCleanShot%25202025-02-26%2520at%252016.04.37%25402x.png%3Falt%3Dmedia%26token%3D9c3fa1cf-12f7-4a3b-a6bf-9f795b5df311&width=768&dpr=4&quality=100&sign=7c5ee8e0&sv=2)

4

###  

If the query returns the expected results, click [Update SQL]. Otherwise, you can ask the assistant to make any desired modifications or fixes.

You can also make your own modifications to the query, such as adding ? characters to represent dynamic values.

</div>

Last updated 4 months ago

Was this helpful?