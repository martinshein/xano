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
        
        -   [Text](text.html)
        -   [Expression](expression.html)
        -   [Array](array.html)
        -   [Object](object.html)
        -   [Integer](integer.html)
        -   [Decimal](decimal.html)
        -   [Boolean](boolean.html)
        -   [Timestamp](timestamp.html)
        -   [Null](null.html)
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
    
    [Using the Expression Editor & Playground](#editor-playground)

-   [Mathematical Operators](#mathematical-operators)

-   [Operator Precedence](#operator-precedence)

-   [Text Operators](#text-operators)

-   [Array Operators](#array-operators)

-   [Array Indexes](#array-indexes)

-   [Object Operators](#object-operators)

-   [Comparison Operators](#comparison-operators)

-   [Logical Operators](#logical-operators)

-   [Conditional Operators](#conditional-operators)

-   [Variable Syntax](#variable-syntax)

-   [Variables](#variables)

-   [Inputs](#inputs)

-   [Authentication](#authentication)

-   [Environment Variables](#environment-variables)

-   [Auto-Complete](#auto-complete)

-   [Data Types](#data-types)

-   [Dot Notation](#dot-notation)

-   [Filters](#filters)

-   [Importing Expressions](#importing-expressions)

-   [Advanced Examples](#advanced-examples)

-   [Conditional](#conditional)

-   [Null coalescing](#null-coalescing)

-   [Ternary](#ternary)

Was this helpful?

Copy


2.  Data Types

Expression 
==========

Expressions are a flexible data type that Xano parses in real-time to support an inline syntax to expressing data with mathematical expressions. Anything you can do with Xano filters, can also be done inline within an expression.

When building expressions, make sure you have the \'expression\' data type selected. You can also click Use Expression under any value box to quickly switch.

Expression building in Xano leverages auto-complete, which will auto-populate references to inputs and variables, filters, and other common notation.

<div>

</div>

 

Using the Expression Editor & Playground

When using the Expression data type, you will be presented with an Expression Editor & Playground to enable easier editing and testing of your expression.

To get the most value out of the expression editor and playground, make sure to add any variable contents you\'d like to use in the Context panel, and make sure to Run & Debug your function stack to enable auto-complete.

**Expression Editor**

[![](../../_gitbook/imaged5e7.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FjhDtlSDBfq9fyCAM8rs8%252FCleanShot%25202024-07-09%2520at%252010.08.39.png%3Falt%3Dmedia%26token%3D9d122271-1425-4f8a-b343-e15e305d24e1&width=300&dpr=4&quality=100&sign=72727c28&sv=2)]

1.  
    
        
    
    Build and edit your expression here with easy auto-complete
    
2.  
    
        
    
    Test your expression in the playground or apply the changes
    
3.  
    
        
    
    Get quick context for variables accessible by your expression and their data types
    
4.  
    
        
    
    Search the library of transformers (filters) available to use, and see examples of how they work
    
5.  
    
        
    
    Take a quick Expressions tutorial
    
6.  
    
        
    
    Enable new variables to be set to Expression type by default
    

**Playground**

[![](../../_gitbook/image55c1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FKptHPCdemM7f31YpwnTs%252FCleanShot%25202024-07-09%2520at%252010.12.13.png%3Falt%3Dmedia%26token%3D137b7fd8-2dc1-4007-837d-38168e1f552d&width=300&dpr=4&quality=100&sign=bba2bd12&sv=2)]

1.  
    
        
    
    Edit your expression here
    
2.  
    
        
    
    Run and test your expression
    
3.  
    
        
    
    The result of the last execution
    
The playground also retains access to the transformers (filters) library and the tutorial. You\'ll need to edit your variable context here if testing with variable data. Just copy and paste the contents into the context panel.

 

Mathematical Operators

Operator

Function

Example

Result

\+

addition

100 + 101

201

\-

subtraction

100 - 101

-1

\*

multiplication

100 \* 101

10101

/

division

100 / 10

10

###  

Operator Precedence

For the most part expressions are evaluated left to right. Using parentheses to illustrate a point, the following would be the same assuming all operators were being evaluated left to right.

Copy

``` 
1 + 2 + 3     == 6
1 + (2 + 3)   == 6
```

However, there are a few operators which get special priority and get evaluated first. These operators are the multiplication and divide operators.

Copy

``` 
1 + 2 * 3    == 7          // if left to right, then 9 (which is incorrect)
1 + (2 * 3)  == 7

1 + 4 / 2    == 3          // if left to right, 2.5 (which is incorrect)
1 + (4 / 2)  == 3
```

 

Text Operators

Operator

Function

Example

Result

\~

concatenation

a \~ b

ab

To add separation when concatenating, add an empty string between the values: ​`a~" "~b`

 

Array Operators

Operator

Function

Example

Result

\...

spread items within an array

\[1,2,3, \...\[4,5,6\],7\]

\[1,2,3,4,5,6,7\]

..

range operator

1..10

\[1,2,3,4,5,6,7,8,9,10\]

 

Array Indexes

Expressions have the ability to reference array elements using all integer values (0, positive numbers, and negative numbers). Using a negative number represents starting from the top of the list rather the beginning of the list.

Expression

Result

\[a,b,c,d,e\]\[0\]

a

\[a,b,c,d,e\]\[1\]

b

\[a,b,c,d,e\]\[-1\]

e

\[a,b,c,d,e\]\[-2\]

d

 

Object Operators

Operator

Function

Example

Result

\...

spread items within an object

, d: 4}

{a:1,b:2,c:3,d:4}

 

Comparison Operators

Operator

Function

Example

Result

==

equals (type conversion)

1 == \"1\"

true

===

strict equals

1 === \"1\"

false

!=

not equals (type conversion)

1 != \"1\"

false

!==

strict not equals

1 !== \"1\"

true

\>

greater than

1 \> 2

false

\>=

greater than or equals

1 \>= 2

false

\<

less than

1 \< 2

true

\<=

less than or equals

1 \<= 2

true

 

Logical Operators

Operator

Function

Example

Result

!

not

!true

false

\|\|

or

1 \< 2 \|\| 1 != 1

true

&&

and

1 \< 2 && 1 != 1

false

All of these operators evaluate their expressions as truthy statements. This means that a comparison operator is not required. For example: 0 \|\| 1 would evaluate to true since 1 evaluates as true.

 

Conditional Operators

Operator

Function

Example

Result

a ? b : c

ternary (if/else)

1 \< 2 ? 3 : 4

3

a ?: b

shorthand ternary (this/that)

1 ?: 2

1

a ?? b

null coalescing

null ?? 10

10

The ternary operator has 2 forms - the traditional if/else based on expression and the shorthand (this/that). The shorthand version will use either the left (this) or the right (that) based on which one evaluates to a truthy statement first going from left to right.

The null coalescing operator is very similar to the shorthand ternary, except that instead of relying on a truthy statement, it only checks for the null value.

 

Variable Syntax

Variables can be referenced using the same [syntax](../functions/apis-and-lambdas/lambda-functions.html#special-variables) that is available within Lambdas.

###  

Variables

Variables within the function stack are accessible through `$var` root variable.

![](../../_gitbook/imaged236.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F9VlcvRWaYtOBe40RoEbe%252FCleanShot%25202023-12-19%2520at%252009.52.50.png%3Falt%3Dmedia%26token%3Ddfabf1fe-420e-477f-a7df-80793370221c&width=768&dpr=4&quality=100&sign=ebfd86de&sv=2)

###  

Inputs

Inputs are accessible through the `$input` root variable.

![](../../_gitbook/imageb48e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FaeQ9FTGRjVcPodeXWn0w%252FCleanShot%25202023-12-19%2520at%252009.54.20.png%3Falt%3Dmedia%26token%3D4bbbc492-851c-40e7-aa73-7096de2c3f6b&width=768&dpr=4&quality=100&sign=241d0d74&sv=2)

###  

Authentication

Authentication values are accessible through the `$auth` root variable.

![](../../_gitbook/image081f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F0O75Ap1j6LNYhuyKfckx%252FCleanShot%25202023-12-19%2520at%252009.54.39.png%3Falt%3Dmedia%26token%3Dbcc123db-e48a-4135-84a2-556dd86d918a&width=768&dpr=4&quality=100&sign=d016d0cc&sv=2)

###  

Environment Variables

Environment variables are accessible through the `$env` root variable. This includes both system variables (\$remote\_ip, \$datasource, etc.) as well as workspace environment variables.

![](../../_gitbook/imaged2d2.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FHZKi5odiN8W1sw5IhKL7%252FCleanShot%25202023-12-19%2520at%252009.55.02.png%3Falt%3Dmedia%26token%3D059603bf-d23d-40f3-8b96-1e432cfe2ab6&width=768&dpr=4&quality=100&sign=7750de66&sv=2)

###  

Auto-Complete

When building expressions, you\'ll see autocomplete suggestions as you type. This works for variables, inputs, and environment variables, as well as filters.

For variables with nested data, such as objects, you\'ll also be presented with an auto-complete of the fields inside of that object. In this example, we\'re targeting a variable called `log`and are presented with the fields inside of that variable by the expression builder, as well as a description of each.

![](../../_gitbook/imageb53e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FC9MoJNfizPdCt1zXRmyw%252FCleanShot%25202024-04-03%2520at%252011.34.22.png%3Falt%3Dmedia%26token%3D49a5cc4d-9754-4989-b99b-3ca6322f7277&width=768&dpr=4&quality=100&sign=9ce0aeaf&sv=2)

 

Data Types

The Xano expression engine supports a more relaxed syntax for its data types to make it easier to reference text and variables without the strict requirements of using quotation marks.

Expression

Type

Result

abc

text

\"abc\"

123

integer

123

\$var.score

integer

123

\"\$var.score\"

text

\"\$var.score\"

\"\\\"\"

text with escaped character

\"

true

boolean

true

false

boolean

false

\"true\"

text

\"true\"

null

null

null

\"null\"

text

\"null\"

\"123\"

text

\"123\"

\[1,2,3\]

array of integers

\[1,2,3\]

\[\"1\",\"2\",\"3\"\]

array of text

\[\"1\",\"2\",\"3\"\]

\[a,b,c\]

array of text

\[\"a\",\"b\",\"c\"\]

\[\"a\",\"b\",\"c\"\]

array of text

\[\"a\",\"b\",\"c\"\]

{a:1}

object

{\"a\":1}

{\"a\":a}

object

{\"a\":\"a\"}

object

{\"a\":123}

 

Dot Notation

The same relaxed syntax used for data types also applies to dot notation.

Dot Notation

JSON Equivalent

\$var.items

\$var.items

\$var.items\[1\]

\$var.items\[1\]

\$var.items\[\"1\"\]

\$var.items\[\"1\"\]

\$var.items\[a\]

\$var.items\[\"a\"\]

\$var.items\[a\~b\~c\]

\$var.items\[\"abc\"\]

\$var.items\[\"a\~b\~c\"\]

\$var.items\[\"a\~b\~c\"\]

 

Filters

All of the Xano filters are available within the expression syntax. To use these, you need to follow the pipe expression syntax.

Copy

``` 
variable | pipe : arg1 : arg2 : argN
```

For example, to uppercase text using the upper filter, you would do the following.

Copy

``` 
"xano"|upper

// result = XANO
```

Here is another example using a filter with an argument.

Copy

``` 
1 + 2 + (3|add:1)

// result = 7
```

This particular example is using both a mathematical \"+\" and an add filter to illustrate how they can be mixed together.

You can also chain filters together.

Copy

``` 
1 + 2 + (3|add:1|mul:2)

// result = 11
```

 

Importing Expressions

When importing cURL or pasting JSON into Xano, Xano can automatically detect the Expression data type, provided the expression begins with a \$ character.

As an example, the following JSON\...

Copy

``` 

```

\...will import as:

![](../../_gitbook/imageb854.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FaNnVJ1zaAjOZlg29egxg%252FCleanShot%25202024-04-09%2520at%252015.02.30.png%3Falt%3Dmedia%26token%3D19c55ee7-5feb-4ee8-9374-3f01f250b197&width=768&dpr=4&quality=100&sign=98fee76f&sv=2)

 

Advanced Examples

As showcased above, the Xano expression engine is very powerful. Here we can look into some more advanced use cases that bring everything together.

###  

Conditional

####  

Sample Data

Copy

``` 
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [4,5,6]
}
```

Expression

Copy

``` 
($input.scores|max) > ($var.numbers|min)

// result = false
```

###  

Null coalescing

####  

Sample Data

Copy

``` 
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [4,5,6]
}
```

####  

Expression

Copy

``` 
(($input.scores|merge:[100,101,102])|max)+($var.bad_syntax ?? 100)

// result = 202
```

###  

Ternary

####  

Sample Data

Copy

``` 
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [0,1,2,3,4,5,6]
}
```

####  

Expression

Copy

``` 
($input.scores[2] == 3 ? 10 : 100) + (($var.numbers|min) ?: $var.numbers|max))

// result = 16
```

Last updated 6 months ago

Was this helpful?