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
    
    [What is Query All Records?](#what-is-query-all-records)

-   [Function Options](#function-options)

-   [Using Addons](#using-addons)

-   [Click the button in the Output tab of your Query All Records function.](#click-the-button-in-the-output-tab-of-your-query-all-records-function)

-   [Click to create a new addon.](#click-to-create-a-new-addon)

-   [Select the table you want to add to the response.](#select-the-table-you-want-to-add-to-the-response)

-   [Choose how you want the data returned.](#choose-how-you-want-the-data-returned)

-   [Select the field(s) from the table you are adding that match the data from the original query.](#select-the-field-s-from-the-table-you-are-adding-that-match-the-data-from-the-original-query)

-   [Give your addon a name, and click ](#give-your-addon-a-name-and-click)

-   [Give the data a name, which is the key it will reside in inside of the parent object.](#give-the-data-a-name-which-is-the-key-it-will-reside-in-inside-of-the-parent-object)

Was this helpful?

Copy


2.  Functions
3.  [Database Requests](../database-requests.html)

Query All Records 
=================

 

What is Query All Records?

Query All Records is used to retrieve records from a database table. You can set various filters and other options to determine exactly which records to retrieve.

 

Function Options

Query All Records offers three panels for various settings: **filter**, **output**, and **external**.

Filter

Output

External

The Filter tab is used to determine what records will be returned from the database.

###  

By Custom Query

This is the section you\'ll use to determine what records to return. If you leave it blank, all records will be returned.

Click the [![](../../../_gitbook/imaged0f9.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FMTAb2fiyFHfwu2tk5oLC%252FCleanShot%25202025-01-06%2520at%252012.19.42.png%3Falt%3Dmedia%26token%3D52765992-7842-4d33-a624-12abf9e0ed11&width=300&dpr=4&quality=100&sign=a078be63&sv=2)] icon to edit the custom query, and choose **Add A Conditional** from the panel that opens.

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

###  

By Joins

Joins are an advanced concept that allows you to find matching records between tables. For example, let\'s say you have a table of `orders`, and each of those orders contain products of a specific color. We want to determine how many orders each customer made with products matching their favorite color.

You have two tables with the following data:

`Customers`: Names and their favorite color
`Orders`: Color and price of items sold

When you join these tables using the color as the connection point, you can see which customers bought items matching their favorite color.

There are different ways to combine these lists:

-   
    
        
    
    Inner join: Only shows matches (like customers who bought their favorite color)
    
-   
    
        
    
    Left join: Shows all customers, even if they haven\'t bought anything
    
-   
    
        
    
    Right join: Shows all orders, even if no customer likes that color
    
So if Sarah likes blue and there\'s a blue sweater order, an inner join would connect them. But if Tom likes green and he hasn\'t placed any orders with green items, he\'d only appear in a left join.

Joins are useful because they allow you to consolidate all of this into a single database operation, instead of querying multiple tables and manually matching the data in several additional steps.

###  

Evals

Evals are used to add additional fields from joined tables as part of your response.

In the below example, we have two tables: **sales** and **product**. We\'ve queried the **sales** table and joined it with **product** so we can retrieve product data for each sale. Our eval adds the product name to the response for each sales record returned.

![](../../../_gitbook/image28cc.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FsqJNMPmsHIUPZ5aUhS8y%252FCleanShot%25202025-04-14%2520at%252017.38.50.png%3Falt%3Dmedia%26token%3D06d91dae-8727-4610-8fc4-561a98b8a1bf&width=768&dpr=4&quality=100&sign=e505de74&sv=2)

###  

Null Coalesce

This is a special filter available in a Query All Records statements that allows you to, when looking for values that represent `null` in your database, specify an additional value to look for and treat as `null`.

In real-world use cases, this is useful for things like when you want to find records where a status field is either \'active\' or not set (treating unset as active by default).

For example, in the following table:

[![](../../../_gitbook/image81f6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FFeJBac9z9Mia4DpZCaNJ%252FCleanShot%25202025-06-18%2520at%252016.28.28.png%3Falt%3Dmedia%26token%3Df36a9fd0-305b-4125-9ee8-1015d6f950eb&width=300&dpr=4&quality=100&sign=7dcc71a7&sv=2)]

If we wanted to find all records that are `null`, but know that records with `hello` also mean the same thing as `null` in our application\'s context, we would use the `coalesce` filter to account for this when querying the table.

In the example below on this table, the query returns records with `id: 1 (value='hello')` and `id: 4 (value=null)`, but excludes `id: 2 (value='goodbye')`.

![](../../../_gitbook/image7a79.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F53IlR0CWkL1L675xYO8b%252Fimage.png%3Falt%3Dmedia%26token%3Ddc22f1c0-53d7-4657-b703-45e26aa7a7de&width=768&dpr=4&quality=100&sign=53c585e3&sv=2)

The output tab contains all options related to the return, once the records have been queried. You can change options like determining what fields to show, the sort order, and more.

###  

Customizing the return

Click [![](../../../_gitbook/image4b57.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FvQl01nxlvaoR0EXGwtPv%252FCleanShot%25202025-01-06%2520at%252014.45.09.png%3Falt%3Dmedia%26token%3D396282da-fa99-4cdf-b7e2-888e6b8e6d74&width=300&dpr=4&quality=100&sign=abe763be&sv=2)] to edit the fields returned in the query.

Note that customizing to reduce the fields returned will not have an impact on query speed, but may help with other performance issues in your function stacks. It is always good practice to only return the fields necessary.

###  

Return As

Change the variable name that this function will output to.

If you\'re using conditional steps, you can use the same variable name in multiple steps to make satisfying the conditional or outputting data in the response easier.

For example, if we are sending a specific response based on if a variable is true or false, we can set both of those outputs to the same variable, making building our response easier.

###  

Return Settings

Under Return Settings, you can adjust sorting and pagination settings.

####  

Return Types

**exists** - Returns a true or false based on if records were returned
**count** - Returns the number of records found
**single** - Returns the first record found
**list** - Returns a list of records
**stream** - When used with a For Each Loop, maintains memory efficiency when iterating through large lists of records
**aggregate** - Perform special aggregation functions on the returned records

####  

Sorting

Click [![](../../../_gitbook/imaged7b3.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FYEPGYJmCCZ89pEuNq3kR%252FCleanShot%25202025-01-06%2520at%252014.55.36.png%3Falt%3Dmedia%26token%3D5849dda7-f8ad-469d-8672-2bdf2159488d&width=300&dpr=4&quality=100&sign=551a1f&sv=2)]to apply a sort to the returned records. You can apply multiple sorts for further customization.

####  

Paging

Check [![](../../../_gitbook/imagee814.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FZfTa5HL2R2Fq18AxipwF%252FCleanShot%25202025-01-06%2520at%252014.54.31.png%3Falt%3Dmedia%26token%3D2fc53eac-e503-41d6-9cc3-81636e9cdd52&width=300&dpr=4&quality=100&sign=53ef55b5&sv=2)] to enable pagination for this query. You can specify which page to return, and how many records should be returned for each page.

Check [![](../../../_gitbook/image4f7a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fu5tWiv2gPUIfue3FlQBM%252FCleanShot%25202025-01-06%2520at%252014.54.49.png%3Falt%3Dmedia%26token%3Db2d27b6c-c019-4302-8c61-fd6aabcdc3d3&width=300&dpr=4&quality=100&sign=6d3b213&sv=2)] if you want to include paging metadata, as shown below, in your return. You can also opt to include the total item count, which is the total number of records in the table.

Copy

``` 

Return As

Set the variable name that will contain the result

####  

Lock

When used with a database transaction

The external tab in a Query all Records Function enables external manipulation of your filtering, sorting, and paging. Once you link up the variable, you can pick and choose which options can be configured externally.

The features present in the External tab are essential for any of the following scenarios:

-   
    
        
    
    You need to enable pagination of the results on your front-end
    
-   
    
        
    
    You want your users to have more control over search parameters
    
-   
    
        
    
    You want to otherwise define how the Query All Records function behaves with parameters coming in from your front-end.
    

![](../../../_gitbook/image434d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FqvvngeVvxDH9t16Lzf4m%252FCleanShot%25202025-01-07%2520at%252008.46.03.png%3Falt%3Dmedia%26token%3D04c3a08f-78b4-48d7-a503-d41c30f4c815&width=768&dpr=4&quality=100&sign=ff5c5950&sv=2)

###  

External Query Options

You will notice that as you explore the various options for externally manipulating your query, there are two different modes, **simple** and **classic**.

You should be using **simple** mode for new queries, but we will continue to make classic mode available to ensure that existing queries still continue to function.

####  

External Sorting

External sorting allows you to dynamically provide sorting options, such as if you want to allow your users to choose between ascending or descending order.

To use external sorting, you need a JSON array that defines the sort in the following format. The object can either be constructed by your front-end and provided to Xano via a JSON input, or your front-end can just send the sort parameters and you can construct the array in the function stack with a Create Variable function.

You can copy the JSON below and paste it into the value of a Create Variable step, and then choose \"Import JSON\" on the pop-up that displays to let Xano construct this for you automatically.

Copy

``` 
[
      {
            "orderBy": "",
            "sortBy": ""
      }
]
```

You can define multiple sorts by adding additional objects to the array.

**orderBy** will either be \'asc\' or \'desc\' for ascending or descending order

**sortBy** will contain the table name and the column name to sort by. As an example, if you have a table called \"transactions\" and you want to sort by the column \"amount\", your **sortBy** would be \"*transactions.amount*\"

####  

External Filtering

External filtering allows you to define specific query conditions via an input. To use external filtering, you need to construct a JSON array defining the conditions of the search in the following format. This format is the same as if you were to read a condition you built in Query All Records, from left to right.

Copy

``` 
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": ""
        },
        "op": "==",
        "right": {
          "operand": ""
        }
      }
    }
  ]
}
```

In this example, we are doing a simple search to check if a field contains a specific value. The left, op, and right values match exactly what we would see in the Query All Records expression builder.

Copy

``` 
,
        "op": "==",
        "right": {
          "operand": "1"
        }
      }
    }
  ]
}
```

![](../../../_gitbook/image43c6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FxpUljXnpuqQ2dMcwGF6J%252FCleanShot%25202023-06-12%2520at%252009.53.52.png%3Falt%3Dmedia%26token%3Dbea2281e-e333-4cf8-a100-c2f480bcc204&width=768&dpr=4&quality=100&sign=e0e7abc4&sv=2)

If you want to define multiple search conditions, you can add additional objects to the \"expression\" array.

Operator

Purpose

between

Checks if a value is between one value and another

contains

Checks if a string contains another string

=

Checks if a value equals another value

==

Checks if a value equals another value and has the same type

\>=

Checks if a value is greater than or equal to another value

\<=

Checks if a value is less than or equal to another value

\>

Checks if a value is greater than another value

\<

Checks if a value is less than another value

ilike / includes

Checks if a string matches a certain pattern or similarity to another, such as searching for all names that start with a K. Ignores case sensitivity.

like

Same as ilike, but uses case sensitivity.

not between

Checks if a value is not between two others

not contains

The opposite of contains --- checks if a string does not contain another string

in

Checks to see if a value is inside of an array of values

not in

Checks to see if a value is not inside of an array of values

overlaps

Checks to see if one array has the some of the same values of another array

not overlaps

Checks to see if one array does not have any of the same values of another array

regex

Uses [regular expressions](https://regex101.com/) to check for matching values

not regex

Uses [regular expressions](https://regex101.com/) to check for non-matching values

View additional external filtering examples at the link below.

[[External Filtering Examples]]

####  

External Paging

External paging is essential if you are displaying results in pages on your front-end, as your front-end will typically send the information about what page to display back to Xano so your API knows which page to return.

Using Simple Mode for external paging, you can easily set variables or values for the following options as pertains to paging:

**Page**
The current page of results

**Per Page**
The amount of results per page

**Offset**
Offset is available if you need to manually define an offset for the set of records returned.
The following example, assuming your record IDs start at 1, will return records 1 - 10

> Page: 1
> Per Page: 10
> Offset: 0

The following example, assuming your record IDs start at 1, will return records 2 - 11

> Page: 1
> Per Page: 10
> Offset: 1

<div>

</div>

Video Example of Using External Paging (Simple mode)

To define your external parameters using simple mode, just specify your desired values or variables in the External tab:

![](../../../_gitbook/image5da0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fl7PHBAQ04hBWLhcbvGVM%252FCleanShot%25202023-01-17%2520at%252016.46.54%25402x.png%3Falt%3Dmedia%26token%3Db97a3736-d1e0-423d-a358-72930a03d1e8&width=768&dpr=4&quality=100&sign=ca77f101&sv=2)

 

Using Addons

Addons are a way for you to enrich a query\'s result with related data from other tables, such as getting product information and orders together. This is usually facilitated by using [table reference fields](../../../the-database/database-basics/field-types.html#table-reference).

Please note that addons that are empty (do not retrieve any data) will not be provided in the response.

<div>

1

###  

Click the [![](../../../_gitbook/imageefad.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fsz8cBA6BXO0V1Y0TO0is%252FCleanShot%25202025-01-07%2520at%252008.25.57.png%3Falt%3Dmedia%26token%3Df67a7d4a-b8c6-46c9-a376-5fd7635491ff&width=300&dpr=4&quality=100&sign=3af36687&sv=2)] button in the Output tab of your Query All Records function.

You\'ll see this attached to the base level of the response, table reference fields, and list fields. It\'s important to choose the correct Addon button based on the data you\'re trying to enhance.

In this example, we have an Order table that just contains product IDs, and we want to see actual product information instead.

![](../../../_gitbook/imagea799.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FQf0Q3jXEhY9fnGMKfKBZ%252FCleanShot%25202025-01-07%2520at%252008.26.38.png%3Falt%3Dmedia%26token%3Da4ed94f4-b85c-4470-95fc-6148ec406339&width=768&dpr=4&quality=100&sign=2a6d6fff&sv=2)

2

###  

Click [![](../../../_gitbook/imageee33.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FhjzQ5junXMsWQjPQJJ7t%252FCleanShot%25202025-01-07%2520at%252008.28.28.png%3Falt%3Dmedia%26token%3D1e8bea7b-88f1-48a3-8e66-210d67901689&width=300&dpr=4&quality=100&sign=772924e6&sv=2)] to create a new addon.

You can also select from already created addons from here.

3

###  

Select the table you want to add to the response.

For this example, we\'re adding product data to our orders, so we\'ll choose product.

![](../../../_gitbook/image0af7.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FhIOJ8jtI5z5UNDFYW1uI%252FCleanShot%25202025-01-07%2520at%252008.34.23.png%3Falt%3Dmedia%26token%3Dbabaa554-0878-4f53-b237-e72c15dbe14f&width=768&dpr=4&quality=100&sign=16ae0087&sv=2)

4

###  

Choose how you want the data returned.

Similar to return types on a Query All Records step, you can adjust how the data is returned here.

####  

Return Types

**exists** - Returns a true or false based on if records were returned
**count** - Returns the number of records found
**single** - Returns the first record found
**list** - Returns a list of records
**stream** - When used with a For Each Loop, maintains memory efficiency when iterating through large lists of records
**aggregate** - Perform special aggregation functions on the returned records

For this example, because we are only returning one product per product ID, we\'ll choose **single**.

5

###  

Select the field(s) from the table you are adding that match the data from the original query.

Our orders table contains product IDs in a field called `product_id`, so we\'ll choose that field. Xano will try and make the right choice for you automatically, so you may not have to make any changes here.

![](../../../_gitbook/image1476.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FXolPGJ75zuu8fYB5mPN4%252FCleanShot%25202025-01-07%2520at%252008.38.40.png%3Falt%3Dmedia%26token%3Dde3060bd-f00d-491d-b45c-73c9db7db9ec&width=768&dpr=4&quality=100&sign=bf025707&sv=2)

6

###  

Give your addon a name, and click [![](../../../_gitbook/imagef731.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FqXri3YAF4VnCLXdCgmNn%252FCleanShot%25202025-01-07%2520at%252008.39.17.png%3Falt%3Dmedia%26token%3D057691ea-58fe-4deb-9c19-40fa5e7bbbd5&width=300&dpr=4&quality=100&sign=dd7af170&sv=2)]

This name is just for you, so you can find the addon you\'re creating later.

7

###  

Give the data a name, which is the key it will reside in inside of the parent object.

Our parent object in this case is each product ID. The parent object is just whatever you are adding on to --- think back to a few steps ago when we clicked the Addon button inside of product\_id.

We want each product to be nested under a key called product\_info, so that\'s what we\'ll put here.

![](../../../_gitbook/imageb0bd.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FAtuydobkxnklF69jlC5h%252FCleanShot%25202025-01-07%2520at%252008.40.34.png%3Falt%3Dmedia%26token%3D6dd73122-dab9-44d6-bb58-90b3d49ccf5c&width=768&dpr=4&quality=100&sign=21039d08&sv=2)

You can also click [![](../../../_gitbook/image3e2a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FwId6MEVOTjRiTmT2OPVI%252FCleanShot%25202025-01-07%2520at%252008.42.21.png%3Falt%3Dmedia%26token%3Dbff0f736-0cfb-4e9b-8b3c-cfd8c8e14873&width=300&dpr=4&quality=100&sign=7f12423a&sv=2)] to change the response if you only want certain fields returned.

</div>

Last updated 1 month ago

Was this helpful?