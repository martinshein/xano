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
                
                -   [External Filtering Examples](../database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../database-requests/get-record.html)
            -   [Add Record](../database-requests/add-record.html)
            -   [Edit Record](../database-requests/edit-record.html)
            -   [Add or Edit Record](../database-requests/add-or-edit-record.html)
            -   [Patch Record](../database-requests/patch-record.html)
            -   [Delete Record](../database-requests/delete-record.html)
            -   [Bulk Operations](../database-requests/bulk-operations.html)
            -   [Database Transaction](../database-requests/database-transaction.html)
            -   [External Database Query](../database-requests/external-database-query.html)
            -   [Direct Database Query](../database-requests/direct-database-query.html)
            -   [Get Database Schema](../database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](create-variable.html)
            -   [Update Variable](update-variable.html)
            -   [Conditional](conditional.html)
            -   [Switch](switch.html)
            -   [Loops](loops.html)
            -   [Math](math.html)
            -   [Arrays](arrays.html)
            -   [Objects](objects.html)
            -   [Text](text.html)
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
    
    [For Each Loop](#for-each-loop)

-   [Add a For Each loop function.](#add-a-for-each-loop-function)

-   [Specify the list that the loop will iterate through.](#specify-the-list-that-the-loop-will-iterate-through)

-   [Define the variable that will hold each item as the loop runs.](#define-the-variable-that-will-hold-each-item-as-the-loop-runs)

-   [Add functions inside of your loop.](#add-functions-inside-of-your-loop)

-   [For Loop](#for-loop)

-   [While Loop](#while-loop)

-   [Additional Loop Functions](#additional-loop-functions)

-   [Loop: Break](#loop-break)

-   [Loop: Continue](#loop-continue)

-   [For Each Loop: Remove Entry](#for-each-loop-remove-entry)

Was this helpful?

Copy


2.  Functions
3.  [Data Manipulation](../data-manipulation.html)

Loops 
=====

Loops are used to iterate over a set of items, or run a set of steps a certain number of times.

There are a few different kinds of loops that you can use in Xano.

 

For Each Loop

A For Each loop is designed to iterate over a list of items, such as all records returned by a database query, or items returned from an external API request.

If you are iterating through a list of database records, set the return type in the query to **stream** to enable super memory-efficient looping. This is especially helpful the larger the list is.

<div>

1

###  

Add a For Each loop function.

2

###  

Specify the list that the loop will iterate through.

Select the variable that contains your list of items.
[![](../../../_gitbook/imagecb59.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F2rAeav0PwytKYmDr0zdS%252FCleanShot%25202025-01-13%2520at%252010.19.49.png%3Falt%3Dmedia%26token%3Dc3e096cb-0092-4539-b7eb-9679dc86370a&width=300&dpr=4&quality=100&sign=98c989bd&sv=2)]

3

###  

Define the variable that will hold each item as the loop runs.

By default, this is called [**item**], but you can name it whatever you\'d like. Use this variable inside of your loop.
[![](../../../_gitbook/image88b4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fu9Oz3y3QCtuWkoibnGlX%252FCleanShot%25202025-01-13%2520at%252010.20.37.png%3Falt%3Dmedia%26token%3D8b05c0ee-4884-4609-9a6b-87fff6070a1a&width=300&dpr=4&quality=100&sign=34d59df&sv=2)]

4

###  

Add functions inside of your loop.

Make sure these steps target the right variable.
[![](../../../_gitbook/image7a6a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fy4jEBd1rMhTTIB1Z39bR%252FCleanShot%25202025-01-13%2520at%252010.21.15.png%3Falt%3Dmedia%26token%3Dfa6da30c-9f56-4e35-b90c-3df8b12512d4&width=300&dpr=4&quality=100&sign=cfb527bb&sv=2)]

</div>

 

For Loop

A For loop is used to repeat a stack of steps a certain number of times.

Refer to the For Each loop instructions to see how it works. The only difference between a For and a For Each loop is\...

-   
    
        
    
    In a For loop, you need to specify the number of times the loop runs.
    [![](../../../_gitbook/image910b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVt8sf8E8a2FTwixIdPIg%252FCleanShot%25202025-01-13%2520at%252010.11.19.png%3Falt%3Dmedia%26token%3Db3e449bf-e411-46c8-a028-24680d09ad51&width=300&dpr=4&quality=100&sign=f1c1edf5&sv=2)]
    
-   
    
        
    
    Because we aren\'t building the loop against a list of items directly, we don\'t have a variable that houses the individual item. Instead, Xano keeps track of which iteration is running inside of an **index variable**, which you can set here.
    [![](../../../_gitbook/image230e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F40QmrafVexdB3MOSYzy3%252FCleanShot%25202025-01-13%2520at%252010.16.47.png%3Falt%3Dmedia%26token%3D181f8c37-c4b0-449f-9334-fb13428fe348&width=300&dpr=4&quality=100&sign=7e1a9a10&sv=2)]
    
 

While Loop

A While loop is used to repeat a set of steps infinitely as long as the condition(s) defined evaluate as true.

Proceed with caution when using While loops, as they can not be easily stopped once started.

To ensure that your loop works as intended, make sure to **stop the loop with a Break statement** while testing and debugging.

If you are concerned that you have entered an infinite loop and want to break it, learn how to restart your instance [here](../../../xano-features/instance-settings.html#maintenance).

You\'ll use the expression builder to define the conditions that tell the loop whether or not it should continue.

###  

Using the Expression Builder

Each conditional has four different components.

**Conditional Type**

The conditional type determines how this condition is weighted in the final return. You can choose between **AND** and **OR. AND** conditionals require the present conditional and any others before it to be satisfied, such as \"where the date is before today **AND** the user is an admin\". **OR** conditionals do not require any other conditionals to be satisfied, such as \"if the user is an admin **OR** if the user is a manager\".

**Left Value**

This is the first value you\'re using in the conditional. In a database query, this is usually going to be a column that you want to check against.

**Operators**

Please note that operators may differ based on where you are building the expression. Database queries will have different operators available than regular conditional statements. Learn More

-   
    
        
    
    **Equals (==)** - an exact match
    
-   
    
        
    
    **Not Equals (!=)** - does not equal
    
-   
    
        
    
    **Equals with type matching (===)** - an exact value match and an exact type match

    -   
        
                
        
        Ex. Variable **var\_1** has a value of 123, with a type of text. You set up a conditional statement to check if **var\_1 === 123**, but your value in the conditional statement is of type integer. This would return false, because the types do not match.
            
-   
    
        
    
    **Not equals with type matching (!==)** - does not equal value or type, similar to ===
    
-   
    
        
    
    **Greater than (\>)** - the value on the left is greater than the value on the right
    
-   
    
        
    
    **Greater than or equals (≥)** - the value on the left is greater than or equals to the value on the right.
    
-   
    
        
    
    **Less than (\<)** - the value on the left is less than the value on the right.
    
-   
    
        
    
    **Less than or equals (≤)** - the value on the left is less than or equals to the value on the right.
    
-   
    
        
    
    **LIKE** - Used for comparing text. Like is case-insensitive and compares if a text string is like another text string. It can be thought of as equals for text but upper case and lower case does not matter.
    
-   
    
        
    
    **NOT LIKE** - Used for comparing text. Not Like is case-insensitive and compares if a text string is not like another. It is like not equals for text but upper case and lower case does not matter.
    
-   
    
        
    
    **INCLUDES** - Used for comparing text. Includes is a flexible operator and is case-insensitive. It is able to determine if there is a partial match in a text string.
    
-   
    
        
    
    **DOES NOT INCLUDE** - Used for comparing text. Does not include determines if a text string is not included in another text string.
    
-   
    
        
    
    **IN** - If a single value is found in an array (list). Start with the single value on the left side and the right side should contain the array.
    
-   
    
        
    
    **NOT IN** - If a single value is not found in an array (list). The single value should be on the left side and the array on the right side.
    
-   
    
        
    
    **REGEX MATCHES** - [Regular Expression](https://regex101.com/) used for finding patterns in text.
    
-   
    
        
    
    **REGEX DOES NOT MATCH** - [Regular Expression](https://regex101.com/) used for finding a pattern that does not match in text.
    
-   
    
        
    
    **OVERLAPS** - Used for comparing two arrays. Overlaps determines if any values in one array are present in the second array.
    
-   
    
        
    
    **DOES NOT OVERLAP** - Used for comparing two arrays. Does not overlaps determines if no values in the first array are present in the second array.
    
-   
    
        
    
    **CONTAINS** - Contains is an advanced filter used for JSON and arrays. It looks for an exact schema match.
    
-   
    
        
    
    **DOES NOT CONTAIN** - Does not contain is the opposite of contains. It determines if there is not an exact schema match.
    
####  

Right Value

The right value is whatever you are checking against the left value. This could be a hardcoded value, a variable, or even a database field from the same record.

 

Additional Loop Functions

###  

Loop: Break

Breaks the currently running loop, meaning the loop is exited and the next function will run.

###  

Loop: Continue

Immediately begins executing the next iteration of the loop. This is very useful for conditionals inside of loops that determine what happens to the item being iterated through.

###  

For Each Loop: Remove Entry

This will remove the item being iterated through from the parent list.

Last updated 5 months ago

Was this helpful?