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
    
    [Add to End of Array](#add-to-end-of-array)

-   [Add to Beginning of Array](#add-to-beginning-of-array)

-   [Remove from End of Array](#remove-from-end-of-array)

-   [Remove from Beginning of Array](#remove-from-beginning-of-array)

-   [Merge](#merge)

-   [Find First Element](#find-first-element)

-   [Find First Element Index](#find-first-element-index)

-   [Has Any Element](#has-any-element)

-   [Has Every Element](#has-every-element)

-   [Find All Elements](#find-all-elements)

-   [Get Element Count](#get-element-count)

-   [Array: Map](#array-map)

-   [Array: Partition](#array-partition)

-   [Array: Group By](#array-group-by)

-   [Array: Difference](#array-difference)

-   [Array: Intersection](#array-intersection)

-   [Array: Union](#array-union)

-   [Using the Expression Builder](#using-the-expression-builder)

Was this helpful?

Copy


2.  Functions
3.  [Data Manipulation](../data-manipulation.html)

Arrays 
======

An array, or list, may contain a single item or many items. Arrays behave differently than other data types; you will typically iterate through them to transform data. These iterations can be performed with loops, or you can perform more wide-sweeping changes using [expressions](../../../xano-transform/using-xano-transform.html).

We have several array functions that you can use to extract and manipulate the array quickly.

Before you dive in, let\'s review a key concept specific to arrays: index

The **index** is the number that corresponds to the item in the list, starting at 0. You won\'t see this reflected in your data, but it\'s how arrays keep track of their defined order of items.

 

Add to End of Array

Adds an item to the end of an array

 

Add to Beginning of Array

Adds an item to the beginning of an array

 

Remove from End of Array

Removes the item at the end of the array

 

Remove from Beginning of Array

Removes the item at the beginning of the array

 

Merge

Merges two arrays together

 

Find First Element

Uses the expression builder to find the first matched element of an array

 

Find First Element Index

Uses the expression builder to find the index of the first matched element of an array

 

Has Any Element

Returns a true or false based on if the array has any elements that meet the conditions outlined in the expression builder

 

Has Every Element

Returns a true or false based on if the array has **all** elements that meet the conditions outlined in the expression builder

 

Find All Elements

Uses the expression builder to find all matching elements in the array

 

Get Element Count

Uses the expression builder to find the count of all matching elements in the array

 

Array: Map

####  

What it does

**Array: Map** transforms each element in a collection using a mapping rule and returns a new array of the transformed values. Use it for formatting, calculations, or reshaping array data.

####  

Example --- Format numbers as USD currency

**Before**

Copy

``` 
[11124.12, 235632.12, 393938.52]
```

**After**

Copy

``` 
["$11,124.12", "$235,632.12", "$393,938.52"]
```

**How it works:** For each number (`$this`):

1.  
    
        
    
    `number_format($this, 2, ".", ",")` produces a string with two decimals, `.` as decimal separator, and `,` as the thousands separator.
    
2.  
    
        
    
    `concat("$", …)` prefixes the dollar sign.
    

UI Field

Example value

Notes

**Collection**

`json_decode('[11124.12,235632.12,393938.52]')`

If you already have an array variable, reference it instead.

**Output type**

`Array of Values`

We output strings such as `"$11,124.12"`.

**Mapping function → Value**

`concat("$", number_format($this, 2, ".", ","))`

`$this` is the current element.

**Result as**

`x1`

Variable name to store the mapped array.

![](../../../_gitbook/imageac40.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F7NciaxhqSQZMnRt8qHuk%252FCleanShot%25202025-08-08%2520at%252009.34.22%25402x.png%3Falt%3Dmedia%26token%3Db947899c-2997-407a-9d3d-499896f6613a&width=768&dpr=4&quality=100&sign=5e20524b&sv=2)

------------------------------------------------------------------------

 

Array: Partition

####  

What it does

**Array: Partition** splits a list into two buckets based on a boolean expression you define. Items where the expression returns **true** go under the `true` key; the rest go under `false`.

####  

Example --- Separate an array that contains different data types, such as text and n

**Before**

Copy

``` 
[1,2,"hello",3,4,"goodbye"]
```

**After**

Copy

``` 
{
    "true": ["hello","goodbye"],
    "false":[1,2,3,4]
}
```

**How it works:** For each number (`$this`), evaluate `$this`.is a text string.

UI Field

Example value

Notes

**Array**

`[1,2,3,4,5]`

Your input list.

**Expression**

`$this|is_text=true  `

Any expression that returns boolean.

**Result as**

`variable_name`

Stores an object with `true` and `false` arrays.

![](../../../_gitbook/image2a34.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fvqk65HjrEVvhythKBtEN%252FCleanShot%25202025-08-08%2520at%252009.32.55%25402x.png%3Falt%3Dmedia%26token%3Db488f6ec-da85-40f6-b502-b43babc32ec0&width=768&dpr=4&quality=100&sign=bdd60c46&sv=2)

------------------------------------------------------------------------

 

Array: Group By

####  

What it does

**Array: Group By** organizes items into an object keyed by a value you compute from each item. Each key maps to an array of items that share that key.

####  

Example --- Group people by age

**Before**

Copy

``` 
[
  {"name":"Alice","age":25},
  {"name":"Bob","age":30},
  {"name":"Eve","age":25}
]
```

**After**

Copy

``` 
{
  "25": [
    {"name":"Alice","age":25},
    {"name":"Eve","age":25}
  ],
  "30": [
    {"name":"Bob","age":30}
  ]
}
```

**How it works:** For each person (`$this`), the grouping key is `$this.age`.

UI Field

Example value

Notes

**Collection**

`[{"name":"Alice","age":25},{"name":"Bob","age":30},{"name":"Eve","age":25}]`

Your array of objects.

**Mapping function → Value**

`$this.age`

Determines the group key for each item.

**Result as**

`grouped_people`

Stores an object keyed by age; values are arrays of matching items.

![](../../../_gitbook/image84e5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FZcYZq1o8iCvoGCSlMZfb%252FCleanShot%25202025-08-08%2520at%252009.35.18%25402x.png%3Falt%3Dmedia%26token%3D23f4944c-dca0-4744-93d7-613156565aa0&width=768&dpr=4&quality=100&sign=1ce19b95&sv=2)

------------------------------------------------------------------------

 

Array: Difference

####  

What it does

**Array: Difference** returns elements that are present in the **first** array but **not** in the **second**, comparing items by an optional mapping function.

####  

Example --- Students who didn't submit homework

**Before**

-   
    
        
    
    First array: `["Amy", "Bob", "Eve"]`
    
-   
    
        
    
    Second array: `["Amy", "Eve"]`
    
**After**

Copy

``` 
["Bob"]
```

**How it works:** Map each item to a comparable value (here, just the item itself via `$this`). Return only items from the first array whose mapped value does not appear in the second array.

UI Field

Example value

Notes

**Collections → First**

`["Amy","Bob","Eve"]`

The "source" list.

**Collections → Second**

`["Amy","Eve"]`

Items to exclude.

**Mapping function → Value**

`$this`

Compare on the item itself. For objects, use something like `$this.id`.

**Result as**

`missing_students`

Array of elements found only in the first array.

![](../../../_gitbook/image04da.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FnHHRp1hRxEVbrOyouUvE%252FCleanShot%25202025-08-08%2520at%252009.36.34%25402x.png%3Falt%3Dmedia%26token%3D10951b92-41c0-4946-bf80-0b82181b06e8&width=768&dpr=4&quality=100&sign=f400ff76&sv=2)

------------------------------------------------------------------------

 

Array: Intersection

####  

What it does

**Array: Intersection** returns elements that are present in **both** arrays, comparing by an optional mapping function.

####  

Example --- Customers who bought both products

**Before**

-   
    
        
    
    Buyers of A: `["Alice","Bob","Eve"]`
    
-   
    
        
    
    Buyers of B: `["Eve","Charlie","Bob"]`
    
**After**

Copy

``` 
["Bob", "Eve"]
```

**How it works:** Map each item to a comparable value (here, the item itself with `$this`). Keep only values that appear in both arrays.

UI Field

Example value

Notes

**Collections → First**

`["Alice","Bob","Eve"]`

First list.

**Collections → Second**

`["Eve","Charlie","Bob"]`

Second list.

**Mapping function → Value**

`$this`

For objects, use a key like `$this.email` or `$this.id`.

**Result as**

`shared_customers`

Array of common elements.

![](../../../_gitbook/imagec73c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FC13bEcZy2iy7lfgYMC8J%252FCleanShot%25202025-08-08%2520at%252009.37.28%25402x.png%3Falt%3Dmedia%26token%3Dc4ac05ce-7c2b-4569-a8fe-de485418c00b&width=768&dpr=4&quality=100&sign=76437c0e&sv=2)

------------------------------------------------------------------------

 

Array: Union

####  

What it does

**Array: Union** merges two arrays and returns an array of **unique** elements from both, comparing by an optional mapping function.

####  

Example --- Merge mailing lists without duplicates

**Before**

-   
    
        
    
    List 1: `["Alice","Bob"]`
    
-   
    
        
    
    List 2: `["Bob","Charlie"]`
    
**After**

Copy

``` 
["Alice", "Bob", "Charlie"]
```

**How it works:** Combine both arrays, then deduplicate based on the mapped value (here using `$this` to compare raw values).

UI Field

Example value

Notes

**Collections → First**

`["Alice","Bob"]`

First list.

**Collections → Second**

`["Bob","Charlie"]`

Second list.

**Mapping function → Value**

`$this`

For objects, use a stable key like `$this.id`.

**Result as**

`all_unique_contacts`

Array of unique values from both inputs.

![](../../../_gitbook/image89cd.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FHr78mB3EhZXJ36HwEaxO%252FCleanShot%25202025-08-08%2520at%252009.38.14%25402x.png%3Falt%3Dmedia%26token%3D2c179cbc-4385-4ce9-ab63-08a23228b6eb&width=768&dpr=4&quality=100&sign=ff170ce2&sv=2)

 

Using the Expression Builder

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

Last updated 4 days ago

Was this helpful?