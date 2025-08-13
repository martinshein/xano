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
title: '}{% endif %}'
---

---
apple-mobile-web-app-status-bar-style: black

color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'template-engine'
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
    
    [Sample Templates](#sample-templates)

-   [AI Prompting Template](#ai-prompting-template)

-   [HTML Template](#html-template)

-   [SQL Query Template](#sql-query-template)

-   [Markdown Template](#markdown-template)

-   [Email Template](#email-template)

Was this helpful?

Copy

1.  [Build With AI](using-ai-builders-with-xano.html)

Template Engine 
===============

 

Quick Summary

The Template Engine, powered by Twig, is used to manipulate and dynamically generate large blocks of text or code with your own data, such as records from your Xano database, or from inputs sent to your APIs.

It\'s great for helping generate things like AI prompts, HTML, and other more large-format data without messing around with a bulk of separate functions to do so.

<div>

</div>

 

What is the Template Engine?

At its core, think of the Template Engine as text replacement and manipulation of the future. It is designed to give you a simple syntax to quickly manipulate large text strings with dynamic data, such as\...

-   
    
        
    
    AI Prompts
    
-   
    
        
    
    HTML
    
-   
    
        
    
    JSON
    
-   
    
        
    
    SQL queries
    
The template engine is powered by Twig, which you can learn more about [here](https://twig.symfony.com/).

 

When should I use the Template Engine instead of other text filters?

You should stick with filters like [replace](../the-function-stack/filters/text.html#replace) or [sprintf](../the-function-stack/filters/text.html#sprintf) if you\'re manipulating short strings of text, such as:

-   
    
        
    
    Replacing a name inside of a string like \"Hello, \[first\_name\] \[last\_name\]\"
    
-   
    
        
    
    Dynamically providing a price for a single product
    
The Template Engine, however, is useful for content templates where:

-   
    
        
    
    The template will be edited by non-developers
    
-   
    
        
    
    The data structure is complex with nested objects
    
-   
    
        
    
    You need to include conditional sections
    
-   
    
        
    
    Data formatting (like dates) needs to be consistent
    
-   
    
        
    
    Templates might be reused with different data sources
    
If you\'re doing dynamic replacement over a longer block of text, such as the example below, Template Engine will make this much easier for you.

Copy

``` 
Write a personalized email to } } about their recent } purchase.

Include:
- Reference to their purchase history (they've ordered } times)
- Mention that their } will be delivered on }
- If }, offer them a }% discount on their next purchase
- Thank them for being a customer since }

Sign off with the name of their account manager: }
```

 

Using the Template Engine

<div>

1

###  

Look for the Template Engine function under Utility Functions.

![](../_gitbook/image37ab.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FTf5FE3kGjwJFG8WWNy0n%252FCleanShot%25202025-04-02%2520at%252016.29.13.png%3Falt%3Dmedia%26token%3D8bbc4381-82cf-408a-af17-9b3bf0f6c70b&width=768&dpr=4&quality=100&sign=9a1f796f&sv=2)

2

###  

Once you add the Template Engine to your function stack, click the [✏️] button in the panel to open the editor, or use the AI assistant to help write a template for you

3

###  

Take a tour of the editor and begin building your template.

![](../_gitbook/imageb3b4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FO9dhVXAaiLRKmNX5wrJX%252FCleanShot%25202025-04-02%2520at%252016.33.01.png%3Falt%3Dmedia%26token%3D928b4ec3-aee1-4dd1-8b89-3497e5dbd37e&width=768&dpr=4&quality=100&sign=5a4da712&sv=2)

</div>

 

Template Syntax

###  

Variables

Variables are wrapped in {{ curly braces }}, like this, and begin with a \$ character. In the below example, we\'re getting the `name` from an object stored in the `user1` variable.

Copy

``` 
Hi, }
```

Reference items in an array by using the item index.

Copy

``` 
Hi, }
```

###  

Conditionals

Conditionals are helpful if you want to dynamically determine what the end result of your template looks like outside of the actual data. For example, maybe you want VIP users to have a different greeting than regular users.

Conditionals are wrapped in {% and %} and have support for `else` and `else if`

Copy

``` 

  Hey, }! Thanks for being a part of our VIP program.
{% else %}
  Hey, }! Thanks for reading.
{% endif %}
```

> In the above example, for this user:
>
> 
> 
> >
> Copy
>
> ``` 
> {
>     "name" == "Chris",
>     "vip" == true
>     }
> ```
> >
> \...the result would be:
>
> 
> 
> >
> Copy
>
> ``` 
> Hey, Chris! Thanks for being a part of our VIP program.
> ```
> 

Copy

``` 
{% if $score >== 90 %}
  Your grade is an A
{% elseif $score >== 80 %}
  Your grade is a B
{% elseif $score >== 70 %}
  Your grade is a C
{% else %}
  Your grade is an F
{% endif %}
```

> In the above example, for this score:
>
> 
> 
> >
> Copy
>
> ``` 
> score = 85
> ```
> >
> \...the result would be:
>
> 
> 
> >
> Copy
>
> ``` 
> Your grade is a B
> ```
> 
###  

Loops

You can use loops to populate lists of data without having to write out separate lines for each item, or knowing how many items you\'ll need to populate.

Copy

``` 

  - }x } at $} each
{% endfor %}
```

Data

Sample Output

Copy

``` 
[
  ,
  ,
  
]
```

-   
    
        
    
    2x Blue T-shirt at \$19.99 each
    
-   
    
        
    
    1x Denim Jeans at \$59.99 each
    
-   
    
        
    
    3x Cotton Socks at \$4.99 each
    
You can also use an Else statement at the end of your For loop to determine what action to take if no items are found. In the next example, if `$list` contains no items, the template will return `No items found.`

Copy

``` 
{% for item in $list %}
  {{ item }}
{% else %}
  No items found.
{% endfor %}
```

###  

Filters

You can use Twig\'s built in filters, similar to our own, to transform or manipulate data as part of the template.

The below list is some of the most essential filters used in Twig, but it is not all of them. You can review the entire list [here](../../twig.symfony.com/doc/3.x/filters/index.html).

Filter

Description

Example

Result

`upper`

Converts string to uppercase

`}`
*When \$user.name is \"John Smith\"*

\"JOHN SMITH\"

`lower`

Converts string to lowercase

`}`
*When \$user.name is \"John Smith\"*

\"john smith\"

`trim`

Removes whitespace from the beginning and end of a string

`}`
*When \$user.input is \" hello \"*

\"hello\"

`join`

Joins array elements into a string with a delimiter

`}`
*When \$user.tags is \[\"php\", \"twig\", \"web\"\]*

\"php, twig, web\"

`default`

Provides a fallback value if the variable is null, empty, or undefined

`}`
*When \$user.middleName is null*

\"No middle name\"

`number_format`

Formats numbers with grouped thousands and decimal points

`}`
*When \$product.price is 1234.56*

\"1,234.56\"

`shuffle`

Randomly shuffles an array

`}`
*When \$user.items is \[\"a\", \"b\", \"c\"\]*

*Random order like:* \[\"c\", \"a\", \"b\"\]

`date`

Formats dates using PHP\'s date syntax

`}`
*When \$user.createdAt is \"2023-12-25\"*

\"December 25, 2023\"

###  

Escape Filter (e)

The escape filter is used to format text using specifications designated by the destination, such as a URL that only allows certain characters to remain valid.

When you use `e` by itself without specifying a format, it typically defaults to HTML escaping. This means it will convert characters like `<`, `>`, `&`, `"`, and `'` to their HTML-safe equivalents.

When you specify a format (like `e('html')`, `e('js')`, `e('url')`, etc.), you\'re explicitly telling the Template Engine how to escape the content for a specific context, which can provide more precise protection. We\'d recommend always specifying the format, just to be safe.

####  

HTML Escaping

Copy

``` 
{% set $user_input = '<script>alert("XSS");</script>' %}
{{ $user_input|e('html') }}

Outputs: &lt;script&gt;alert(&quot;XSS&quot;);&lt;/script&gt;
```

####  

JavaScript Escaping

Copy

``` 
{% set $js_string = 'Hello "world"! \n New line' %}
{{ $js_string|e('js') }}
{# Outputs: Hello \"world\"! \\n New line #}
```

####  

URL Escaping

Copy

``` 
{% set $search_query = 'hello world & special chars' %}
{{ $search_query|e('url') }}
{# Outputs: hello+world+%26+special+chars #}
```

####  

CSS Escaping

Copy

``` 
{% set $css_value = 'expression(alert("XSS"))' %}
{{ $css_value|e('css') }}
{# Outputs: expression\28 alert\28 "XSS"\29 \29 #}
```

###  

Comments

You can insert comments into your templates by wrapping them in {\# and \#}. They won\'t appear in your final template.

Copy

``` 
{# This is a hidden comment #}
```

You can check out some examples of the Template Engine in real-world scenarios here: [Sample Templates](template-engine.html#sample-templates).

 

Sample Templates

Use these sample templates to get started with templates quickly and understand what real-world use cases might look like.

###  

AI Prompting Template

**Context**: A template for generating structured AI prompts with dynamic instructions, constraints, and example inputs/outputs.

Copy

``` 
You are an AI assistant tasked with }.

Context:
{% if $context %}
{{ $context }}
{% else %}
*No additional context provided*
{% endif %}

Instructions:
1. }

}. {{ $step }}
{% endfor %}

Constraints:

- {{ $constraint }}
{% endfor %}

Output Format:
}

Example Input:
}

Example Expected Output:
}
```

###  

HTML Template

**Context**: A product listing page for an e-commerce website, showing personalized content based on user authentication and product availability.

Copy

``` 
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>}</title>
    </head>
    <body>
        <header>
            <h1>Welcome, }!</h1>
        </header>
        
        <nav>
            
                <a href="/profile">My Profile</a>
                <a href="/logout">Logout</a>
            {% else %}
                <a href="/login">Login</a>
                <a href="/register">Register</a>
            {% endif %}
        </nav>
        
        <main>
            {% for $item in $products %}
                <div class="product">
                    <h2>}</h2>
                    <p>Price: $}</p>
                    
                        <button>Add to Cart</button>
                    {% else %}
                        <span class="out-of-stock">Out of Stock</span>
                    {% endif %}
                </div>
            {% endfor %}
        </main>
    </body>
</html>
```

 

Hint

Use an HTML template in combination with our [HTTP Header](../the-function-stack/functions/utility-functions.html#http-header) function to serve HTML directly using your APIs by setting the header `Content-Type: text/html; charset=utf-8`

###  

SQL Query Template

**Context**: A flexible database query generator that adapts to user roles and filtering requirements for a multi-tenant application.

 

PREVENTING SQL INJECTION ATTACKS

Xano offers some filters to help ensure that any dynamic / user input is not parsed in a way that might harm your database or cause other unintended consequences.

Make sure to process your inputs **before** they are used in any SQL queries with the appropriate filter.

These filters are [sql\_alias and sql\_esc](../the-function-stack/filters/text.html#sql_alias)

Copy

``` 
SELECT 
    id, 
    {{ $select_columns|join(', ') }} 
FROM {{ $table_name }}
WHERE 
    
        1=1
    {% else %}
        organization_id = }
    {% endif %}
    
        AND status = '}'
    {% endif %}
ORDER BY 
    {% if $sort_by %}
        {{ $sort_by }} {{ $sort_direction|default('ASC') }}
    {% else %}
        created_at DESC
    {% endif %}
LIMIT {{ $limit|default(10) }}
```

 

Hint

Use an SQL template in combination with our [Direct Database Query](../the-function-stack/functions/database-requests/direct-database-query.html) function to dynamically generate and use SQL queries against your Xano database. You can also use our [External Database Query](../the-function-stack/functions/database-requests/external-database-query.html) functions the same way.

Just type `?:raw` into the query editor and point the statement argument to the output of your Template Engine function.

###  

Markdown Template

**Context**: A Twig template for generating raw Markdown code with dynamic content and metadata.

Copy

``` 
# }{% endif %}
Author: }{% endif %}
Date: }{% endif %}

## Overview

}
{% else %}
*No summary available*
{% endif %}

### Key Points

- {{ $point }}
{% endfor %}

## Content

}

### Tags

`{{ $tag }}`, {% endif %}
{% endfor %}
{% endif %}

## Footnotes

[^}]: {{ $footnote }}
{% endfor %}
{% endif %}
```

###  

Email Template

**Context**: A flexible email template system that supports personalized messaging, dynamic sections, and optional signatures.

Copy

``` 
# }{% endif %}

Author: }{% endif %}
Date: }{% endif %}

## Overview

}
{% else %}
*No summary available*
{% endif %}

### Key Points

- {{ $point }}
{% endfor %}

## Content

}

### Tags

`{{ $tag }}`, {% endif %}
{% endfor %}
{% endif %}

## Footnotes

[^}]: {{ $footnote }}
{% endfor %}
{% endif %}
```

Last updated 4 months ago

Was this helpful?