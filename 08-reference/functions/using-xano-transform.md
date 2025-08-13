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
title: 'apple-mobile-web-app-status-bar-style: black'
---

---
apple-mobile-web-app-status-bar-style: black

color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'using-xano-transform'
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
    
    [What is Xano Transform?](#what-is-xano-transform)

-   [Why Xano Transform?](#why-xano-transform)

-   [How do I use Xano Transform?](#how-do-i-use-xano-transform)

-   [The \$\$ special variable](#double-dollar-sign)

-   [Retrieval with GET](#retrieval-with-get)

-   [Array Retrieval](#array-retrieval)

-   [Conditional Retrieval](#conditional-retrieval)

-   [Automatic Anchoring](#automatic-anchoring)

-   [Transformation with SET](#transformation-with-set)

-   [Expression Data Type](#expression-data-type)

-   [Expression Filters](#expression-filters)

-   [as](#as)

-   [transform](#transform)

-   [to\_expr](#to_expr)

-   [get](#get)

-   [set](#set)

-   [Higher Order Filters](#higher-order-filters)

-   [map](#map)

-   [some](#some)

-   [every](#every)

-   [find](#find)

-   [findIndex](#findindex)

-   [filter](#filter)

-   [reduce](#reduce)

-   [Use Cases & Examples](#use-cases-and-examples)

-   [Troubleshooting](#troubleshooting)

-   [Text vs Expression](#text-vs-expression)

Was this helpful?

Copy

1.  [Xano Transform](using-xano-transform.html)

Using Xano Transform 
====================

[](using-xano-transform.html#what-is-xano-transform)

❓ [**What?**]

Get a quick overview of what Xano Transform can do

[](using-xano-transform.html#why-xano-transform)

🤔 [**Why?**]

Explaining the need for something like Xano Transform

[](using-xano-transform.html#how-do-i-use-xano-transform)

🔍 [**How?**]

The basics of how to utilize Xano Transform

[](../the-function-stack/data-types/expression.html)

[♾️ ][**Expression Data Type**]

Use the Expression data type to quickly build complex expressions

[](using-xano-transform.html#retrieval-with-get)

📖 [**GET Filter**]

Xano Transform\'s GET Filter syntax and examples

[](using-xano-transform.html#transformation-with-set)

[🖌️][ **SET Filter**]

Xano Transform\'s SET Filter syntax and examples

[](using-xano-transform.html#examples)

💡 [**Examples**]

Real-world examples of Xano Transform in action, with comparisons to other methods

 

What is Xano Transform?

The Xano Transform Engine is a new technology built by Xano that takes the traditional dot notation syntax and upgrades it to support data manipulation. This syntax is friendly to objects and arrays and supports conditional filtering using the new [Expression data type](../the-function-stack/data-types/expression.html).

Xano Transform encompasses some updates to our GET and SET filters, allowing you to use a powerful and expansive new type of filtering syntax to parse, return, and transform your data in exactly the way you need. Consider it an alternative to chaining several filters and functions together to accomplish a specific result.

------------------------------------------------------------------------

 

Why Xano Transform?

Xano is, and will always remain, a No-Code first platform. That doesn\'t mean that we don\'t want to offer you more ways to accomplish your goals in the fastest way possible. While this may feel like a leap to \"traditional development\" methods, at its core, Xano Transform is here to provide both traditional developers a more familiar way to work with their data, and empower the no-code audience to work faster with a specific set of easy to learn syntax.

Xano Transform also offers you an easy way to share solutions with other Xano users by just copying and pasting an expression to them. This is an incredibly helpful tool while we work behind the scenes to offer other methods of function stack portability.

------------------------------------------------------------------------

 

How do I use Xano Transform?

Xano Transform has two different operating \'modes\', as an extension of our GET filter, and a separate [*expression* data type](../the-function-stack/data-types/expression.html), which all work from utilizing a standardized syntax, outlined in this documentation.

Please note that you can use standard mathematical operators to compare values in areas where they would normally be accepted, such as \>, \<, ==, !=, etc\...

------------------------------------------------------------------------

 

The \$\$ special variable

Throughout this documentation, there will be repeated mentions of the `$$` special variable. This is our version of the standard `this` variable, which is commonly used in various programming languages and Lambda filters. This concept is used to represent the context that is being referenced within a function/filter.

In this example, \$\$ represents the expression`1+2+3`

Copy

``` 
(1+2+3)|transform:$$+1                   // 7
```

One common problem with the `$$/this` variable concept, is what happens when you need to reference 2 or more different versions of it?

Copy

``` 
(1+2+3)|transform:$$+(1|transform:$$+1)
```

What if I wanted to reference the first `$$` in the second transform? There isn\'t a way to do this because the existence of the second transform has taken over the previous value of the \$\$ variable. The solution tends to involve manually creating new variables and assigning them to different copies of the \$\$ variable.

Xano gets around this by having `$$` represent more than just a value - it represents the top most value of anything binded to it.

All \$\$ variables are available via the following syntax. \$0, \$1, \$2 - or \$\[0\], \$\[1\], \$\[2\], etc. This number keeps increasing as values are bounded to it. This means that the above example could also be written as the following:

Copy

``` 
(1+2+3)|transform:$0+(1|transform:$1+1)
```

Therefore, if we needed to access the first \$\$ within the 2nd transform, we could do so by referencing \$\[0\].

Copy

``` 
(1+2+3)|transform:$$+(1|transform:$$+$0)
```

Sometimes, it is easier to reference items from the top instead of the bottom. Since Xano supports [negative indexes], the second item from the top is represented as `-2`. Therefore, we could also use the following syntax using the array notation:

Copy

``` 
(1+2+3)|transform:$$+(1|transform:$$+$[-2])
```

 

Retrieval with GET

<div>

</div>

####  

Example Data Payload

Copy

``` 
{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
     {"tag":"test","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
      ]
    }
  ]
}
```

Syntax

Result

v

Copy

``` 
10
```

items

Copy

``` 
[
    {
      "id": 1,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
     {"tag":"test","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
      ]
    }
  ]
```

items\[0\]

Copy

``` 
{
  "id": 1,
  "name": "s1",
  "score": 100,
  "tags": [
    {"tag":"beta","weight":5},
    {"tag":"test","weight":50}
  ]
}
```

items\[0\].id

Copy

``` 
1
```

items\[0\].tags\[0\]

Copy

``` 
{"tag":"beta","weight":5}
```

items\[0\].tags\[0\].tag

Copy

``` 
"beta"
```

###  

Array Retrieval

Syntax

Result

items.id

Copy

``` 
[1,2]
```

items.tags

Copy

``` 
[
  {"tag":"beta","weight":5},
  {"tag":"test","weight":50},
  {"tag":"abc","weight":10},
  {"tag":"def","weight":90}
]
```

items.tags.tag

Copy

``` 
["beta","test","abc","def"]
```

###  

Conditional Retrieval

Conditional retrieval is made possible by using the expression syntax within the array brackets of an item.

The `$$` special variable is used to represent the current context of the iterated item of the array.

As seen below, this syntax is supported across multiple levels for deeply nested arrays.

Syntax

Result

items\[\$\$.id \> 1\]

Copy

``` 
[{
  "id": 2,
  "name": "x9",
  "score": 87,
  "tags": [
    {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
  ]
}]
```

items\[\$\$.id \> 1\].id

Copy

``` 
[2]
```

items\[\$\$.id \> 1\].tags.tag

Copy

``` 
["abc","def"]
```

items\[\$\$.id \> 1\].tags\[\$\$.weight\>=90\].tag

Copy

``` 
["def"]
```

###  

Automatic Anchoring

Sometimes you may need to reference something outside of the `$$` special variable. For example, you may want to conditionally select something based on a value that is located in the original root of the object.

This type of reference is supported through automatic anchoring. Each item element of the breadcrumb hierarchy is numerically indexed through `$0`, `$1`, `$2`, `$N` variables.

####  

Example: items\[\$\$.id \> 1\].tags\[\$\$.weight\>=90\].tag

\$2 and \$4 have multiple values since they represent an array iteration. The example below is just showing the snapshot of one iteration of their value.

Special Variable

Result

\$0

Copy

``` 
{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
     {"tag":"test","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
      ]
    }
  ]
}
```

\$1

Copy

``` 
[
  {
    "id": 1,
    "name": "s1",
    "score": 100,
    "tags": [
      {"tag":"beta","weight":5},
      {"tag":"test","weight":50}
    ]
  },
  {
    "id": 2,
    "name": "x9",
    "score": 87,
    "tags": [
      {"tag":"abc","weight":10},
      {"tag":"def","weight":90}
    ]
  }
]
```

\$2

Copy

``` 
{
  "id": 2,
  "name": "x9",
  "score": 87,
  "tags": [
    {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
  ]
}
```

\$3

Copy

``` 
[
  {"tag":"abc","weight":10},,
  {"tag":"def","weight":90}
]
```

\$4

Copy

``` 
{"tag":"def","weight":90}
```

\$5

Copy

``` 
"def"
```

The \$\$ special variable is available to be used as a convenience. It always represents the top most numerically indexed special variable that is available within its context.

Syntax

Result

items\[\$\$.id \> 1\].tags\[\$\$.weight\>=90\].tag

Copy

``` 
["def"]
```

items\[\$2.id \> 1\].tags\[\$\$.weight\>=90\].tag

Copy

``` 
["def"]
```

items\[\$\$.id \> 1\].tags\[\$4.weight\>=90\].tag

Copy

``` 
["def"]
```

items\[\$2.id \> 1\].tags\[\$4.weight\>=90\].tag

Copy

``` 
["def"]
```

####  

Advanced Examples

Syntax

Result

items\[\$\$.id \> 1\].tags\[\$\$.weight\>=\$0.v\].tag

Copy

``` 
["abc","def"]
```

items\[\$\$.id \> (\[\$0.v,2,3\]\|max)\].id

Copy

``` 
[]
```

items\[\$\$.id \> (\[\$0.v,2,3\]\|min) \|\| \$\$.id == 1\].id

Copy

``` 
[1,3]
```

------------------------------------------------------------------------

 

Transformation with SET

In addition to the syntax above for data retrieval, SET supports new syntax for data transformation.

The SET filter leverages the targeting mechanism of the GET filter and allows you to transform the data that is retrieved. It is important to note that after the transformation, the complete object (not just what got changed) is returned. By doing so, it allows for this process to be repeated as many times as you need to complete your transformations.

Below are some examples combining the above syntax with the SET filter.

<div>

</div>

Multiple SET filters may be required for each transformation.

Syntax

Result

*Change the value of \"v\"*

**Path**: v
**Value**: 50

Copy

``` 

{
  "v": 10,
  "items": [
    {
      "id": 99,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
     {"tag":"test","weight":50}
      ]
    },
    {
      "id": 99,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
      ]
    }
  ]
}
```

*Add 1 to all item IDs*

**Path**: items.id
**Value**: \$\$+1

Copy

``` 
{
  "v": 10,
  "items": [
    {
      "id": 2,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
     {"tag":"test","weight":50}
      ]
    },
    {
      "id": 3,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
      ]
    }
  ]
}
```

*Uppercase all item tags*

**Path**: items.tags.tag
**Value**: \$\$\|to\_upper

Copy

``` 
{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "S1",
      "score": 100,
      "tags": [
         {"tag":"BETA","weight":5},
     {"tag":"TEST","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "X9",
      "score": 87,
      "tags": [
        {"tag":"ABC","weight":10},
    {"tag":"DEF","weight":90}
      ]
    }
  ]
}
```

*Add the value of an input to each tag weight*

**Path**: items.tags.weight
**Value**: \$input.add+\$\$
**Input**: 500

Copy

``` 
{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "S1",
      "score": 100,
      "tags": [
         {"tag":"BETA","weight":505},
     {"tag":"TEST","weight":550}
      ]
    },
    {
      "id": 2,
      "name": "X9",
      "score": 87,
      "tags": [
        {"tag":"ABC","weight":510},
    {"tag":"DEF","weight":590}
      ]
    }
  ]
}
```

*Add a new total\_weight key for each item that contains the sum of all tag weights*

**Path**: items.total\_weight
**Value**: \$1.tags.weight\|sum

Copy

``` 
{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "S1",
      "score": 100,
      "tags": [
         {"tag":"BETA","weight":5},
     {"tag":"TEST","weight":50}
      ],
      "total_weight": 55
    },
    {
      "id": 2,
      "name": "X9",
      "score": 87,
      "tags": [
        {"tag":"ABC","weight":10},
    {"tag":"DEF","weight":90}
      ],
      "total_weight": 100
    }
  ]
}
```

------------------------------------------------------------------------

 

Expression Data Type

The expression data type can be applied to any value input and allows you to perform certain operations on your data when establishing new values. You can also reference other variables and inputs in your expressions which allows for faster data manipulation.

<div>

</div>

Please see our full, in-depth documentation on the Expression data type [here](../the-function-stack/data-types/expression.html).

------------------------------------------------------------------------

 

Expression Filters

The Xano Transform Engine provides several filters to assist in making transformation easier using the expression syntax. It also includes custom implementations of the [higher order filters](using-xano-transform.html#higher-order-filters).

###  

as

The `as` filter provides a way to dynamically assign a variable to an expression while chaining together filters. This is useful for long or dynamic expressions that need to be referenced more than once.

Arguments

-   
    
        
    
    name - the new variable name
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
####  

Examples

Copy

``` 
// initial data
$obj.really.long.ref.company             // foobar, inc https://foo.bar

// without as
$obj.really.long.ref.company|substr:0:($obj.really.long.ref.company|index:http)|trim
// foobar, inc

// with as
$obj.really.long.ref.company|as:C|substr:0:($C|index:http)|trim
// foobar, inc
```

###  

transform

This filter is similar to the map filter, except it can bind to all data - not just an array.

The `transform` filter is universal way to transform data. It works with arrays, objects, and scalar values.

Arguments

-   
    
        
    
    expression - the expression being used to transform `$$`.
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
####  

Examples

Copy

``` 
[1,2,3]|transform:($$|count)          // 3
[1,2,3]|transform:($$|count)+($$|sum) // 9

{first:Alpha,last:Beta}|transform:$$.first~" "~$$.last
// Alpha Beta
```

###  

to\_expr

It is very important to sanitize your data, if you are using this with user generated expressions. This filter provides a way to dynamically reference your variables and use the filters within Xano.

The `to_expr` filter is introduces the possibility of dynamic programming. It converts text into an expression.

Arguments (none)

Context Variables (none)

####  

Examples

Copy

``` 
"1+2+3"|to_expr                      // 6

$input.score = 10
"1+2+3+$input.score"|to_expr         // 16
```

###  

get

See above for a detailed walkthrough of the improvements to the [get filter](using-xano-transform.html#retrieval-with-get).

###  

set

See above for a detailed walkthrough of the improvements to the [set filter](using-xano-transform.html#transformation-with-set).

 

Higher Order Filters

These filters resemble their Lambda counterparts, but if used within an Expression, they have a simplified syntax along with their own high performance implementation. All of these have the requirement of binding to an array. There is also a subtle change where the Lambda `$this` variable is represented as the Expression `$$` variable.

###  

map

This filter binds to an array. If you need to transform an object or scalar value, try the transform filter.

The `map` filter is used to do transformations on array elements.

Arguments

-   
    
        
    
    expression - the expression being applied to each iteration of the array
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
-   
    
        
    
    **\$index** - the context variable that represents the numerical index of the element of the array being processed
    
-   
    
        
    
    **\$parent** - the context variable that represents the entire array with all of its elements.
    
####  

Examples

Copy

``` 
[1,2,3]|map:$$+1                      // [2,3,4]
[1,2,3]|map:$$+1+$index               // [2,4,6]
[1,2,3]|map:$$+1+($parent|count)      // [5,6,7]

[{name:foo},{name:bar}]|map:$$.name   // [foo,bar]
```

###  

some

The `some` filter (also called **has** or **has any element**) returns true, if the conditional expression matches any of the array elements - otherwise, false is returned.

Arguments

-   
    
        
    
    expression - the expression being applied to each iteration of the array
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
-   
    
        
    
    **\$index** - the context variable that represents the numerical index of the element of the array being processed.
    
-   
    
        
    
    **\$parent** - the context variable that represents the entire array with all of its elements.
    
####  

Examples

Copy

``` 
[1,2,3]|some:$$==2                    // true
[1,2,3]|some:$$>10                    // false
```

###  

every

The `every` filter (also called **find every element**) returns true if the conditional expression matches all of the array elements - otherwise, false is returned.

Arguments

-   
    
        
    
    expression - the expression being applied to each iteration of the array
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
-   
    
        
    
    **\$index** - the context variable that represents the numerical index of the element of the array being processed.
    
-   
    
        
    
    **\$parent** - the context variable that represents the entire array with all of its elements.
    
####  

Examples

Copy

``` 
[1,2,3]|every:$$>=1 && $$<=3          // true
[1,2,3]|every:$$>10                   // false
```

###  

find

The `find` filter (also called **find first element**) returns the array item, that first matches the conditional expression - otherwise, null is returned.

Arguments

-   
    
        
    
    expression - the expression being applied to each iteration of the array
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
-   
    
        
    
    **\$index** - the context variable that represents the numerical index of the element of the array being processed.
    
-   
    
        
    
    **\$parent** - the context variable that represents the entire array with all of its elements.
    
Examples

Copy

``` 
[1,2,3]|find:$$==2                    // 2
[1,2,3]|find:$$>1                     // 2

[{name:foo},{name:bar}]|find:($$.name|starts_with:b)
// {name:bar}
```

###  

findIndex

The `findIndex` filter (also called **find first element index**) returns the index of the array item, that first matches the conditional expression - otherwise, null is returned.

Arguments

-   
    
        
    
    expression - the expression being applied to each iteration of the array
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
-   
    
        
    
    **\$index** - the context variable that represents the numerical index of the element of the array being processed.
    
-   
    
        
    
    **\$parent** - the context variable that represents the entire array with all of its elements.
    
Examples

Copy

``` 
[1,2,3]|findIndex:$$==2               // 1
[1,2,3]|findIndex:$$>1                // 1

[{name:foo},{name:bar}]|findIndex:($$.name|starts_with:b)
// 1
```

###  

filter

The `filter` filter (also called **find all elements**) returns a new array of items that match the conditional expression.

Arguments

-   
    
        
    
    expression - the expression being applied to each iteration of the array
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
-   
    
        
    
    **\$index** - the context variable that represents the numerical index of the element of the array being processed.
    
-   
    
        
    
    **\$parent** - the context variable that represents the entire array with all of its elements.
    
Examples

Copy

``` 
[1,2,3]|filter:$$==2                  // [2]
[1,2,3]|filter:$$>1                   // [2,3]
```

###  

reduce

This also has an optional 2nd argument that represents the initial value. If not specified, it defaults to 0.

The reduce filter is a bit more complicated than the other because it has state that changes through each iteration of the array elements. The purpose of this filter is to perform some calculation based on all of the array items. A common example would be summing a list of numbers together one after another.

Arguments

-   
    
        
    
    expression - the expression being applied to each iteration of the array
    
-   
    
        
    
    initialValue - (optional) the initial value for `$result`. This defaults to 0, if not specified.
    
Context Variables

-   
    
        
    
    **\$\$** - the context variable that represents the element of the array being processed.
    
-   
    
        
    
    **\$index** - the context variable that represents the numerical index of the element of the array being processed.
    
-   
    
        
    
    **\$parent** - the context variable that represents the entire array with all of its elements.
    
-   
    
        
    
    **\$result** - the context variable that is used to represent the result of the previous iteration or the initial value on the first iteration.
    
Examples

Copy

``` 
[1,2,3]|reduce:$$+$result             // 6
[1,2,3]|reduce:$$+$result:10          // 16
```

 

Use Cases & Examples

Xano Transform is almost limitless. Some of the most common use cases for Transform are as follows. Please note that this is not an extensive list, and we recommend reading on for more information and examples.

For the sake of these examples, assume we are working with the following data set. You can download the full list of products as CSV or JSON below as well if you want to try these yourself.

[](../../3699875497-files.gitbook.io/_/files/v0/b/gitbook-x-prod.appspot.com/o/spaces/2tWsL4o1vHmDGb2UAUDD/uploads/nLUFXuOhwfaKSRDCoXd4/products-example-json2dd9.txt?alt=media&token=2eed77f8-4311-4354-b514-30a35bcf092d)

<div>

</div>

83KB

<div>

products-example-json.txt

</div>

[](https://3699875497-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tWsL4o1vHmDGb2UAUDD%2Fuploads%2FXo6saDjAHPD6UEnExqUs%2Fproducts-example.csv?alt=media&token=efc341a0-0dc7-4214-a223-81a19dc08a2e)

<div>

</div>

215KB

<div>

products-example.csv

</div>

Copy

``` 
,
                ,
            ...]
}
```

Using Xano Transform, we could use one or more of the following:

-   
    
        
    
    Find me all of the products with a price greater than \$700
    
-   
    
        
    
    Find me all of the smartphones that have a rating of at least 4.5 and are less than \$300
    
-   
    
        
    
    Find me all of the iPhones that have a total price of their returned price + 7.5% to account for tax
    
These are just a few examples of what Xano Transform could accomplish.

####  

Find all products with a price greater than \$700

Xano Transform (GET Filter)

No-Code

High Order Filters

Javascript

![](../_gitbook/image168d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FxaCQC1wfB4lorvAswo9L%252Fimage.png%3Falt%3Dmedia%26token%3Da4ff2e56-09c0-4b48-ac46-0b2398e5efbd&width=768&dpr=4&quality=100&sign=9bbdb708&sv=2)

Copy

``` 
result[$$.price>700]
```

-   
    
        
    
    **result (*****Find all products)***

    -   
        
                
        
        Selects something in the JSON, in this case the \'list\' key
            
-   
    
        
    
    **\[\]**

    -   
        
                
        
        Indicates that we want to apply a condition to the selection
            
-   
    
        
    
    **\$\$.price** (with a price)

    -   
        
                
        
        Use the value of \'price\' as part of the expression
            
-   
    
        
    
    **\>700** (greater than 700)

    -   
        
                
        
        The expression used to define the data we want returned
            

![](../_gitbook/imagecd4b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FSgwU4bkYi1utfXqoAS6w%252Fimage.png%3Falt%3Dmedia%26token%3Dd41080af-451e-4b76-85a0-71575c9c7541&width=768&dpr=4&quality=100&sign=744268f1&sv=2)

-   
    
        
    
    **Create Variable**

    -   
        
                
        
        Create a variable to hold our list of qualifying results
            
-   
    
        
    
    **For Each Loop**

    -   
        
                
        
        Use a For Each Loop to begin to iterate through the list of data we are working with
        
    -   
        
                
        
        **Conditional**

        -   
            
                        
            
            Check to see if the item we are currently iterating through has a price greater than \$700
            
        -   
            
                        
            
            **Then**

            -   
                
                                
                
                If the item qualifies, add it to the variable created before the loop began
                            
        -   
            
                        
            
            **Else**

            -   
                
                                
                
                Go to the next iteration of the loop
                                        

![](../_gitbook/image8f14.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FChCPdulVTzQ6CmG2pzk0%252Fimage.png%3Falt%3Dmedia%26token%3D6f0edf36-9b13-4905-b654-b45822be4835&width=768&dpr=4&quality=100&sign=744d42be&sv=2)

Using the higher order filter called \'filter\', apply the following code:

Copy

``` 
return $this.price > 700;
```

Copy

``` 
return $var.products.filter(product => product.price > 700);
```

####  

Find all products with a price greater than \$700 and a rating greater than 4.5

Xano Transform (GET Filter)

No-Code

High Order Filters

Javascript

![](../_gitbook/imagead09.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F7VkPQVtqkcqRkrrbOTPw%252Fimage.png%3Falt%3Dmedia%26token%3Dbeb66da4-54f3-4d5d-9151-b40a4178f00b&width=768&dpr=4&quality=100&sign=e684b626&sv=2)

Copy

``` 
result[$$.price>700 && $$.rating>4.5]
```

-   
    
        
    
    **result (*****Find all products)***

    -   
        
                
        
        Selects something in the JSON, in this case the \'list\' key
            
-   
    
        
    
    **\[\]**

    -   
        
                
        
        Indicates that we want to apply a condition to the selection
            
-   
    
        
    
    **\$\$.price** (with a price)

    -   
        
                
        
        Use the value of \'price\' as part of the expression
            
-   
    
        
    
    **\>700** (greater than 700)

    -   
        
                
        
        The first part of the expression used to define the data we want returned
            
-   
    
        
    
    **&&** (and)

    -   
        
                
        
        Indicate that this expression contains multiple conditions
            
-   
    
        
    
    **\$\$.rating** (a rating)

    -   
        
                
        
        Select the \'rating\' value as a part of this condition
            
-   
    
        
    
    **\>4.5** (greater than 4.5)

    -   
        
                
        
        The second part of the expression used to define the data we want returned
            

![](../_gitbook/image467b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fz6hkrfI87thRnUxT7u6f%252Fimage.png%3Falt%3Dmedia%26token%3D05db2522-a463-4888-babd-f59c84ae023c&width=768&dpr=4&quality=100&sign=8f5d4d62&sv=2)

-   
    
        
    
    **Create Variable**

    -   
        
                
        
        Create a variable to hold our list of qualifying results
            
-   
    
        
    
    **For Each Loop**

    -   
        
                
        
        Use a For Each Loop to begin to iterate through the list of data we are working with
        
    -   
        
                
        
        **Conditional**

        -   
            
                        
            
            Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5
            
        -   
            
                        
            
            **Then**

            -   
                
                                
                
                If the item qualifies, add it to the variable created before the loop began
                            
        -   
            
                        
            
            **Else**

            -   
                
                                
                
                Go to the next iteration of the loop
                                        

![](../_gitbook/imaged7f4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FPf6kcScGlaRV5rPrgkVU%252Fimage.png%3Falt%3Dmedia%26token%3Dd4a93fd1-a3de-4cc6-bf8b-3ab5097c1ce6&width=768&dpr=4&quality=100&sign=3205c612&sv=2)

Using the higher order filter called \'filter\', apply the following code:

Copy

``` 
return $this.price > 700 && $this.rating > 4.5;
```

Copy

``` 
return $var.products.filter(product => product.price > 700 && product.rating > 4.5);
```

####  

Find all products with a price greater than \$700 and a rating greater than 4.5, that are in stock

Xano Transform (GET Filter)

No-Code

High Order Filters

Javascript

![](../_gitbook/imageeff2.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8Zq5EdUrk8FycIxBaS9V%252Fimage.png%3Falt%3Dmedia%26token%3D8514cfa9-e805-43d4-b9d8-3a6cda5d55c9&width=768&dpr=4&quality=100&sign=488772c5&sv=2)

Copy

``` 
result[$$.price>700 && $$.rating>4.5 && $$.stock>0]
```

-   
    
        
    
    **result (*****Find all products)***

    -   
        
                
        
        Selects something in the JSON, in this case the \'list\' key
            
-   
    
        
    
    **\[\]**

    -   
        
                
        
        Indicates that we want to apply a condition to the selection
            
-   
    
        
    
    **\$\$.price** (with a price)

    -   
        
                
        
        Use the value of \'price\' as part of the expression
            
-   
    
        
    
    **\>700** (greater than 700)

    -   
        
                
        
        The first part of the expression used to define the data we want returned
            
-   
    
        
    
    **&&** (and)

    -   
        
                
        
        Indicate that this expression contains multiple conditions
            
-   
    
        
    
    **\$\$.rating** (a rating)

    -   
        
                
        
        Select the \'rating\' value as a part of this condition
            
-   
    
        
    
    **\>4.5** (greater than 4.5)

    -   
        
                
        
        The second part of the expression used to define the data we want returned
            
-   
    
        
    
    **&&** (and)

    -   
        
                
        
        Indicate that this expression contains multiple conditions
            
-   
    
        
    
    **\$\$.stock\>0** (that are currently in stock)

    -   
        
                
        
        The third part of the expression used to define the data we want returned
            

![](../_gitbook/imageb04e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FuDGHDDOSCMwv1x6y2k99%252Fimage.png%3Falt%3Dmedia%26token%3D74a0cd6e-a548-4767-8e98-88c248ca818c&width=768&dpr=4&quality=100&sign=409d18b5&sv=2)

-   
    
        
    
    **Create Variable**

    -   
        
                
        
        Create a variable to hold our list of qualifying results
            
-   
    
        
    
    **For Each Loop**

    -   
        
                
        
        Use a For Each Loop to begin to iterate through the list of data we are working with
        
    -   
        
                
        
        **Conditional**

        -   
            
                        
            
            Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5, that also have a stock count greater than 0
            
        -   
            
                        
            
            **Then**

            -   
                
                                
                
                If the item qualifies, add it to the variable created before the loop began
                            
        -   
            
                        
            
            **Else**

            -   
                
                                
                
                Go to the next iteration of the loop
                                        

![](../_gitbook/image7f00.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FZH1dXesRr5pmOJsF3QsS%252Fimage.png%3Falt%3Dmedia%26token%3D06680b2b-b6a5-480e-914a-1d318e1a9d2c&width=768&dpr=4&quality=100&sign=8fd6d451&sv=2)

Using the higher order filter called \'filter\', apply the following code:

Copy

``` 
return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
```

Copy

``` 
return $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);
```

####  

Take the returned list of products and capitalize all product names

Xano Transform (SET Filter)

No-Code

High Order Filters

Javascript

![](../_gitbook/imagee78f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FLJV6XS6t3ux3GtfrH517%252FCleanShot%25202023-12-21%2520at%252014.27.47.png%3Falt%3Dmedia%26token%3Dc0b30678-9751-42b3-b2d9-d30890c552f8&width=768&dpr=4&quality=100&sign=b57bf606&sv=2)

Copy

``` 
Path: name
Value: $$|to_upper
```

-   
    
        
    
    **Path: name**

    -   
        
                
        
        Set the \'path\' option to *name* to indicate this is the key to update
            
-   
    
        
    
    **Value: \$\$\|to\_upper**

    -   
        
                
        
        **\$\$**

        -   
            
                        
            
            Select the current name
                    
    -   
        
                
        
        **\|to\_upper**

        -   
            
                        
            
            Apply the to\_upper filter
                        

![](../_gitbook/image6c73.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FYdWxpXIPwqJtrb9M6BLq%252FCleanShot%25202023-12-21%2520at%252014.29.32.png%3Falt%3Dmedia%26token%3Da687422a-c424-478b-8efa-76b6fda0ce82&width=768&dpr=4&quality=100&sign=b152f303&sv=2)

-   
    
        
    
    **Create Variable**

    -   
        
                
        
        Create a variable to hold our list of qualifying results
            
-   
    
        
    
    **For Each Loop**

    -   
        
                
        
        Use a For Each Loop to begin to iterate through the list of data we are working with
        
    -   
        
                
        
        **Conditional**

        -   
            
                        
            
            Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5, that also have a stock count greater than 0
            
        -   
            
                        
            
            **Then**

            -   
                
                                
                
                Update the product\'s name by applying a to\_upper filter
                
            -   
                
                                
                
                If the item qualifies, add it to the variable created before the loop began
                            
        -   
            
                        
            
            **Else**

            -   
                
                                
                
                Go to the next iteration of the loop
                                        

![](../_gitbook/image5092.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FqYsw3QY1gYParv9VGak7%252FCleanShot%25202023-12-21%2520at%252014.30.19.png%3Falt%3Dmedia%26token%3D3722a323-8417-42a0-8675-1d978df30f1e&width=768&dpr=4&quality=100&sign=ed15b621&sv=2)

Using the filter **filter**, apply the following code:

Copy

``` 
return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
```

Using the filter **map**, apply the following code:

Copy

``` 
return ;
```

Copy

``` 
let filteredProducts = $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);
let modifiedProducts = filteredProducts.map(product => ;
});
return modifiedProducts;
```

####  

Take the returned list of products, capitalize all product names, and conditionally update the price based on the stock value while applying proper price formatting

Xano Transform (GET Filter)

No-Code

High Order Filters

Javascript

![](../_gitbook/image20af.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FXbM81q4i5UVbDTo9Kn6F%252FCleanShot%25202023-12-21%2520at%252014.37.11.png%3Falt%3Dmedia%26token%3D2f6aa710-1203-45cd-99a6-ad368b624b81&width=768&dpr=4&quality=100&sign=4b3018fd&sv=2)

*To complete this example, you\'ll want to apply the SET filter for name as described in the previous example.*

Copy

``` 
Path: price
Value: $1.stock>50 ? ("$"~($$*0.9|number_format:2:.:,)) : ("$"~($$*1.3|number_format:2:.:,))
```

-   
    
        
    
    **Path: price**

    -   
        
                
        
        Set the path option to \'price\' to indicate this is the key to update
            
-   
    
        
    
    **Value: \$1.stock\>50 ? (\"\$\"\~(\$\$\*0.9\|number\_format:2:.:,)) : (\"\$\"\~(\$\$\*1.3\|number\_format:2:.:,))**

    -   
        
                
        
        **\$1.stock\>50**

        -   
            
                        
            
            Use anchored selection to get the stock count and check to see if it is greater than 50
                    
    -   
        
                
        
        **?**

        -   
            
                        
            
            Apply a condition based on what the previous portion of the expression returns
                    
    -   
        
                
        
        **If the stock \> 50**

        -   
            
                        
            
            **(\"\$\"\~**

            -   
                
                                
                
                Begin the value with a \$ character
                            
        -   
            
                        
            
            **(\$\$\*0.9**

            -   
                
                                
                
                Multiply the price by 0.9
                            
        -   
            
                        
            
            **\|number\_format:2:.:,))**

            -   
                
                                
                
                Apply the number\_format filter to format the number as a standard price (2 decimal points, a . decimal separator, and a , thousands seperator)
                                    
    -   
        
                
        
        **If the stock \< 50**

        -   
            
                        
            
            **(\"\$\"\~**

            -   
                
                                
                
                Begin the value with a \$ character
                            
        -   
            
                        
            
            **(\$\$\*1.3**

            -   
                
                                
                
                Multiply the price by 1.3
                            
        -   
            
                        
            
            **\|number\_format:2:.:,))**

            -   
                
                                
                
                Apply the number\_format filter to format the number as a standard price (2 decimal points, a . decimal separator, and a , thousands seperator)
                                        

![](../_gitbook/image654a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fs5vHBs0mwGTGn9sog78U%252FCleanShot%25202023-12-21%2520at%252014.48.23.png%3Falt%3Dmedia%26token%3Df4b3c201-eda0-4600-851e-36a2fc785358&width=768&dpr=4&quality=100&sign=9a2bb23d&sv=2)

-   
    
        
    
    **Create Variable**

    -   
        
                
        
        Create a variable to hold our list of qualifying results
            
-   
    
        
    
    **For Each Loop**

    -   
        
                
        
        Use a For Each Loop to begin to iterate through the list of data we are working with
        
    -   
        
                
        
        **Conditional**

        -   
            
                        
            
            Check to see if the item we are currently iterating through has a price greater than \$700 and a rating greater than 4.5, that also have a stock count greater than 0
            
        -   
            
                        
            
            **Then**

            -   
                
                                
                
                Update the product\'s name by applying a to\_upper filter
                
            -   
                
                                
                
                **Conditional**

                -   
                    
                                        
                    
                    Check to see if the product stock is greater than 50

                    -   
                        
                                                
                        
                        **Then**

                        -   
                            
                                                        
                            
                            Update the product price, multiplying it by 0.9
                                                    
                    -   
                        
                                                
                        
                        **Else**

                        -   
                            
                                                        
                            
                            Update the product price, multiplying it by 1.3
                                                                                        
            -   
                
                                
                
                Update the product\'s price and apply the number\_format filter
                            
        -   
            
                        
            
            **Else**

            -   
                
                                
                
                Go to the next iteration of the loop
                                        

![](../_gitbook/image00a8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FoPZ4uoOQfjvVURNwdIXb%252FCleanShot%25202023-12-21%2520at%252015.10.13.png%3Falt%3Dmedia%26token%3D469eb22a-62a6-4731-af0f-6f9b73e65252&width=768&dpr=4&quality=100&sign=aaf9422c&sv=2)

Using the filter **filter**, apply the following code:

Copy

``` 
return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
```

Using the filter **map**, apply the following code:

Copy

``` 
return )+(?!\d))/g, ",") 
           : ($this.price * 1.3).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
};
```

Copy

``` 
let filteredProducts = $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);

let modifiedProducts = filteredProducts.map(product => )+(?!\d))/g, ",")
    };
});

return modifiedProducts;
```

 

Troubleshooting

###  

Text vs Expression

The get and set filters parse the path argument using the [Xano expression](../the-function-stack/data-types/expression.html) syntax. If you have a path that looks like an expression, but needs to be interpreted as text, then wrap it with brackets and quotes.

Some 3rd party APIs (like Stripe) rely on dot notation arguments being sent as text and then interpreted on their side. In this scenario, it is important to wrap them with the bracket syntax below using double quotation marks.

The [Import cURL](../the-function-stack/functions/apis-and-lambdas/external-api-request.html) feature has been updated to properly escape all arguments.

AS ARRAY

AS TEXT

expand\[0\]

\[\"expand\[0\]\"\]

line\_item\[0\]\[data\]

\[\"line\_item\[0\]\[data\]\"\]

Last updated 6 months ago

Was this helpful?