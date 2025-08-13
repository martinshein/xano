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
    
    [What are triggers?](#what-are-triggers)

-   [Accessing and Creating Triggers](#accessing-and-creating-triggers)

-   [Database Triggers](#database-triggers)

-   [Realtime Triggers](#realtime-triggers)

-   [Workspace Triggers](#workspace-triggers)

-   [MCP Triggers](#mcp)

-   [AI Agent Triggers](#ai-agent-triggers)

Was this helpful?

Copy


2.  Building with Visual Development

Triggers 
========

**Quick Summary**

Triggers are workflows that can run based on other events that happen in your workspace. Xano offers triggers for:

-   
    
        
    
    Database operations (adds, edits, deletes)
    
-   
    
        
    
    Realtime events
    
-   
    
        
    
    Workspace events (currently limited to branching operations)
    
-   
    
        
    
    MCP Server connections
    
Triggers are available on our **Starter plan** and higher.

 

What are triggers?

Triggers in Xano are workflows that will run only when triggered by another event. You can build triggers for the following events.

Event Type

Event

**Database**

New records

Record edits

Record deletes

Table truncate (deleting all records)

**Realtime**

Channel events

**Workspace**

New branch

Branch merge

Live branch change

**MCP Server**

Client Connect

 

Accessing and Creating Triggers

<div>

1

###  

Database Triggers

You can find database triggers on each table by clicking the settings icon in the top-right corner.

Click [ + Add Database Trigger ] to create a new database trigger.

You can specify what [Data Sources](../../the-database/database-basics/data-sources.html) the trigger will execute on. If no data source is set, then it will execute on all data sources.

Select the **actions** that will activate this trigger.

**Inserts**
Any time a record is added to the table

**Updates**
Any time a record is edited

**Deletes**
Any time a record is deleted

**Truncates**
When the content of the database table is cleared

Finally, you can set up custom filters so that the trigger only runs if the record matches certain conditions. For example, if you only want the trigger to run if a new order is created for a user, or a new user is created with a certain role.

------------------------------------------------------------------------

Database triggers have predefined inputs that contain all of the information you\'ll need to build a workflow based on the database event.

`new`
This is the contents of the new record --- if you\'re adding a record, this will contain the contents of the new record, and if you\'re updating a record, this will contain the contents of the updated record. On deletes and truncates, this will be empty.

`old`
This is the contents of the old record --- if you\'re deleting or editing a record, this will contain the contents of the record before the change. On inserts and truncates, this will be empty.

`action`
The action that activated the trigger. Valid options are `insert` `update` `delete` `truncate`

`data source`
The datasource this trigger has been executed against

------------------------------------------------------------------------

2

###  

Realtime Triggers

Realtime triggers are created for each channel. Once you\'ve created a realtime channel, click the [ + Add Channel Trigger ] button to create a new channel trigger.

Select the **actions** that will activate the trigger.

**Message**
Any time a new message is sent to the channel

**Join**
Any time a new connection is made to the channel

------------------------------------------------------------------------

Realtime triggers have predefined inputs that contain all of the information you\'ll need to build a workflow based on the realtime event.

`Action` and ~~**Command**~~
This will be either \'join\' or \'message\' depending on what was responsible for executing the trigger.

***Action*** *and* ***Command*** *currently have the same values, but behind the scenes, the values do not come from the same source. We maintain two separate inputs for the purpose of expanding this functionality in the future.*

`Channel`
The channel that this command or message is being sent to

`commandOptions`
Any options that are provided with the command being sent to the channel

`payload`
The contents of the command, such as the message body

`client`
An internal client ID

------------------------------------------------------------------------

3

###  

Workspace Triggers

Workspace triggers can be created to execute workflows based on certain workspace-wide events. Currently, these are limited to branch changes.

You can find workspace triggers by clicking the settings icon in the top-right corner of your workspace dashboard.

Click [ + Add Workspace Trigger ] to create a new workspace trigger.

Select the **action(s)** that will execute this trigger.

**Branch Live**
Any time a branch status is set to live

**Branch Merge**
When a branch is merged

**Branch New**
When a new branch is created

4

###  

MCP Triggers

MCP triggers can be created to run any time a client connects to the MCP server. This is useful for functions like:

-   
    
        
    
    Logging connections to the MCP server
    
-   
    
        
    
    Dynamically adjusting server instructions based on other data, such as the user who is connecting
    
-   
    
        
    
    Restricting tools per connection
    
You can find MCP triggers by clicking the settings icon in the top-right corner of your MCP server.

Click [ + Add MCP Server Trigger ] to create a new MCP server trigger.

MCP Server triggers offer the following inputs:

`toolset`
Contains the server information, such as the name and instructions.

`tools[]`
An array that contains each tool.

5

###  

AI Agent Triggers

Agent triggers are similar to MCP triggers. They can be used when an agent is called to perform tasks such as:

-   
    
        
    
    Logging connections
    
-   
    
        
    
    Dynamically adjusting available functions and tools
    
-   
    
        
    
    Adjusting the system prompt based on user or other data
    
You can find Agent Triggers in the settings for your Agent.

`toolset`
Contains the server information, such as the name and instructions.

`tools[]`
An array that contains each tool.

</div>

Last updated 5 days ago

Was this helpful?