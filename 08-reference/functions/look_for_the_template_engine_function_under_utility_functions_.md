---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Look for the Template Engine function under Utility Functions.
---

# Look for the Template Engine function under Utility Functions.

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'template-engine'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Template Engine \| Xano Documentation'
viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---
[](../index.html)
Xano Documentation
[Ctrl][K]
-   ::: 
    Before You Begin
    :::
-   ::: 
    [🛠️]The Visual Builder
    :::
        ::: 
            ::: 
            -   Swagger (OpenAPI Documentation)
            :::
            ::: 
            -   Async Functions
            :::
        -   Background Tasks
        -   Triggers
        -   Middleware
        -   Configuring Expressions
        -   Working with Data
        :::
        ::: 
        -   AI Tools
            ::: 
                ::: 
                -   External Filtering Examples
                :::
            -   Get Record
            -   Add Record
            -   Edit Record
            -   Add or Edit Record
            -   Patch Record
            -   Delete Record
            -   Bulk Operations
            -   Database Transaction
            -   External Database Query
            -   Direct Database Query
            -   Get Database Schema
            :::
            ::: 
            -   Create Variable
            -   Update Variable
            -   Conditional
            -   Switch
            -   Loops
            -   Math
            -   Arrays
            -   Objects
            -   Text
            :::
        -   Security
            ::: 
            -   Realtime Functions
            -   External API Request
            -   Lambda Functions
            :::
        -   Data Caching (Redis)
        -   Custom Functions
        -   Utility Functions
        -   File Storage
        -   Cloud Services
        :::
        ::: 
        -   Manipulation
        -   Math
        -   Timestamp
        -   Text
        -   Array
        -   Transform
        -   Conversion
        -   Comparison
        -   Security
        :::
        ::: 
        -   Text
        -   Expression
        -   Array
        -   Object
        -   Integer
        -   Decimal
        -   Boolean
        -   Timestamp
        -   Null
        :::
        ::: 
        -   Response Caching
        :::
-   ::: 
    Testing and Debugging
    :::
-   ::: 
    The Database
    :::
        ::: 
        -   Using the Xano Database
        -   Field Types
        -   Relationships
        -   Database Views
        -   Export and Sharing
        -   Data Sources
        :::
        ::: 
        -   Airtable to Xano
        -   Supabase to Xano
        -   CSV Import & Export
        :::
        ::: 
        -   Storage
        -   Indexing
        -   Maintenance
        -   Schema Versioning
        :::
-   ::: 
    Build For AI
    :::
        ::: 
        -   Templates
        :::
        ::: 
        -   Connecting Clients
        -   MCP Functions
        :::
-   ::: 
    Build With AI
    :::
-   ::: 
    File Storage
    :::
-   ::: 
    Realtime
    :::
-   ::: 
    Maintenance, Monitoring, and Logging
    :::
        ::: 
        :::
-   ::: 
    Building Backend Features
    :::
        ::: 
        -   Separating User Data
        -   Restricting Access (RBAC)
        -   OAuth (SSO)
        :::
-   ::: 
    Xano Features
    :::
        ::: 
        -   Release Track Preferences
        -   Static IP (Outgoing)
        -   Change Server Region
        -   Direct Database Connector
        -   Backup and Restore
        -   Security Policy
        :::
        ::: 
        -   Audit Logs
        :::
        ::: 
        -   Xano Link
        -   Developer API (Deprecated)
        :::
        ::: 
        -   Master Metadata API
        -   Tables and Schema
        -   Content
        -   Search
        -   File
        -   Request History
        -   Workspace Import and Export
        -   Token Scopes Reference
        :::
-   ::: 
    Xano Transform
    :::
-   ::: 
    Xano Actions
    :::
-   ::: 
    Team Collaboration
    :::
-   ::: 
    Agencies
    :::
        ::: 
        -   Agency Dashboard
        -   Client Invite
        -   Transfer Ownership
        -   Agency Profile
        -   Commission
        -   Private Marketplace
        :::
-   ::: 
    Custom Plans (Enterprise)
    :::
        ::: 
            ::: 
                ::: 
                -   Choosing a Model
                :::
            :::
        -   Tenant Center
        -   Compliance Center
        -   Security Policy
        -   Instance Activity
        -   Deployment
        -   RBAC (Role-based Access Control)
        -   Xano Link
        -   Resource Management
        :::
-   ::: 
    Your Xano Account
    :::
-   ::: 
    Troubleshooting & Support
    :::
        ::: 
        -   When a single workflow feels slow
        -   When everything feels slow
        -   RAM Usage
        -   Function Stack Performance
        :::
        ::: 
        -   Granting Access
        -   Community Code of Conduct
        -   Community Content Modification Policy
        -   Reporting Potential Bugs and Issues
        :::
-   ::: 
    Special Pricing
    :::
-   ::: 
    Security
    :::
-   ::: 
    :::
    Sample Templates
Was this helpful?
Copy
1.  Build With AI
Template Engine 
===============
Quick Summary
The Template Engine, powered by Twig, is used to manipulate and dynamically generate large blocks of text or code with your own data, such as records from your Xano database, or from inputs sent to your APIs.
It\'s great for helping generate things like AI prompts, HTML, and other more large-format data without messing around with a bulk of separate functions to do so.
<div>
</div>
What is the Template Engine?
At its core, think of the Template Engine as text replacement and manipulation of the future. It is designed to give you a simple syntax to quickly manipulate large text strings with dynamic data, such as\...
-   ::: 
    ::: 
    :::
    :::
    ::: 
    AI Prompts
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    HTML
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    JSON
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    SQL queries
    :::
The template engine is powered by Twig, which you can learn more about here.
When should I use the Template Engine instead of other text filters?
You should stick with filters like replace or sprintf if you\'re manipulating short strings of text, such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Replacing a name inside of a string like \"Hello, \[first\_name\] \[last\_name\]\"
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Dynamically providing a price for a single product
    :::
The Template Engine, however, is useful for content templates where:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The template will be edited by non-developers
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The data structure is complex with nested objects
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You need to include conditional sections
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Data formatting (like dates) needs to be consistent
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Templates might be reused with different data sources
    :::
If you\'re doing dynamic replacement over a longer block of text, such as the example below, Template Engine will make this much easier for you.
Copy
``` 
Write a personalized email to {} {} about their recent {} purchase.
Include:
Sign off with the name of their account manager: {}
```
Using the Template Engine
<div>
1
###  
Look for the Template Engine function under Utility Functions.
2
###  
Once you add the Template Engine to your function stack, click the [✏️] button in the panel to open the editor, or use the AI assistant to help write a template for you
3
###  
Take a tour of the editor and begin building your template.
</div>
Template Syntax
###  
Variables
Variables are wrapped in {}, like this, and begin with a \$ character. In the below example, we\'re getting the `name` from an object stored in the `user1` variable.
Copy
``` 
Hi, {}
```
Reference items in an array by using the item index.
Copy
``` 
Hi, {}
```
###  
Conditionals
Conditionals are helpful if you want to dynamically determine what the end result of your template looks like outside of the actual data. For example, maybe you want VIP users to have a different greeting than regular users.
Conditionals are wrapped in  and have support for `else` and `else if`
Copy
``` 
  Hey, {}! Thanks for being a part of our VIP program.
  Hey, {}! Thanks for reading.
```
> In the above example, for this user:
>
> ::: 
> ::: 
> :::
>
> Copy
>
> ``` 
> 
> ```
> :::
>
> \...the result would be:
>
> ::: 
> ::: 
> :::
>
> Copy
>
> ``` 
> Hey, Chris! Thanks for being a part of our VIP program.
> ```
> :::
Copy
``` 
  Your grade is an A
  Your grade is a B
  Your grade is a C
  Your grade is an F
```
> In the above example, for this score:
>
> ::: 
> ::: 
> :::
>
> Copy
>
> ``` 
> score = 85
> ```
> :::
>
> \...the result would be:
>
> ::: 
> ::: 
> :::
>
> Copy
>
> ``` 
> Your grade is a B
> ```
> :::
###  
Loops
You can use loops to populate lists of data without having to write out separate lines for each item, or knowing how many items you\'ll need to populate.
Copy
``` 
  - {}x {} at ${} each
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
-   ::: 
    ::: 
    :::
    :::
    ::: 
    2x Blue T-shirt at \$19.99 each
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    1x Denim Jeans at \$59.99 each
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    3x Cotton Socks at \$4.99 each
    :::
You can also use an Else statement at the end of your For loop to determine what action to take if no items are found. In the next example, if `$list` contains no items, the template will return `No items found.`
Copy
``` 
  {}
  No items found.
```
###  
Filters
You can use Twig\'s built in filters, similar to our own, to transform or manipulate data as part of the template.
The below list is some of the most essential filters used in Twig, but it is not all of them. You can review the entire list here.
Filter
Description
Example
Result
`upper`
Converts string to uppercase
`{}`
*When \$user.name is \"John Smith\"*
\"JOHN SMITH\"
`lower`
Converts string to lowercase
`{}`
*When \$user.name is \"John Smith\"*
\"john smith\"
`trim`
Removes whitespace from the beginning and end of a string
`{}`
*When \$user.input is \" hello \"*
\"hello\"
`join`
Joins array elements into a string with a delimiter
`{}`
*When \$user.tags is \[\"php\", \"twig\", \"web\"\]*
\"php, twig, web\"
`default`
Provides a fallback value if the variable is null, empty, or undefined
`{}`
*When \$user.middleName is null*
\"No middle name\"
`number_format`
Formats numbers with grouped thousands and decimal points
`{}`
*When \$product.price is 1234.56*
\"1,234.56\"
`shuffle`
Randomly shuffles an array
`{}`
*When \$user.items is \[\"a\", \"b\", \"c\"\]*
*Random order like:* \[\"c\", \"a\", \"b\"\]
`date`
Formats dates using PHP\'s date syntax
`{}`
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
{}
Outputs: &lt;script&gt;alert(&quot;XSS&quot;);&lt;/script&gt;
```
####  
JavaScript Escaping
Copy
``` 
{}
```
####  
URL Escaping
Copy
``` 
{}
```
####  
CSS Escaping
Copy
``` 
{}
```
###  
Comments
You can insert comments into your templates by wrapping them in . They won\'t appear in your final template.
Copy
``` 
```
You can check out some examples of the Template Engine in real-world scenarios here: Sample Templates.
Sample Templates
Use these sample templates to get started with templates quickly and understand what real-world use cases might look like.
###  
AI Prompting Template
**Context**: A template for generating structured AI prompts with dynamic instructions, constraints, and example inputs/outputs.
Copy
``` 
You are an AI assistant tasked with {}.
Context:
{}
*No additional context provided*
Instructions:
1. {}
{}. {}
Constraints:
- {}
Output Format:
{}
Example Input:
{}
Example Expected Output:
{}
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
        <title>{}</title>
    </head>
    <body>
        <header>
            <h1>Welcome, {}!</h1>
        </header>
        <nav>
                <a href="/profile">My Profile</a>
                <a href="/logout">Logout</a>
                <a href="/login">Login</a>
                <a href="/register">Register</a>
        </nav>
        <main>
                <div class="product">
                    <h2>{}</h2>
                    <p>Price: ${}</p>
                        <button>Add to Cart</button>
                        <span class="out-of-stock">Out of Stock</span>
                </div>
        </main>
    </body>
</html>
```
Hint
Use an HTML template in combination with our HTTP Header function to serve HTML directly using your APIs by setting the header `Content-Type: text/html; charset=utf-8`
###  
SQL Query Template
**Context**: A flexible database query generator that adapts to user roles and filtering requirements for a multi-tenant application.
PREVENTING SQL INJECTION ATTACKS
Xano offers some filters to help ensure that any dynamic / user input is not parsed in a way that might harm your database or cause other unintended consequences.
Make sure to process your inputs **before** they are used in any SQL queries with the appropriate filter.
These filters are sql\_alias and sql\_esc
Copy
``` 
SELECT 
    id, 
    {} 
FROM {}
WHERE 
        1=1
        organization_id = {}
        AND status = '{}'
ORDER BY 
        {} {}
        created_at DESC
LIMIT {}
```
Hint
Use an SQL template in combination with our Direct Database Query function to dynamically generate and use SQL queries against your Xano database. You can also use our External Database Query functions the same way.
Just type `?:raw` into the query editor and point the statement argument to the output of your Template Engine function.
###  
Markdown Template
**Context**: A Twig template for generating raw Markdown code with dynamic content and metadata.
Copy
``` 
# {}
Author: {}
Date: {}
## Overview
{}
*No summary available*
### Key Points
- {}
## Content
{}
### Tags
`{}`, 
## Footnotes
[^{}]: {}
```
###  
Email Template
**Context**: A flexible email template system that supports personalized messaging, dynamic sections, and optional signatures.
Copy
``` 
# {}
Author: {}
Date: {}
## Overview
{}
*No summary available*
### Key Points
- {}
## Content
{}
### Tags
`{}`, 
## Footnotes
[^{}]: {}
```
Last updated 4 months ago
Was this helpful?

## Code Examples

```javascript
 
Write a personalized email to {} {} about their recent {} purchase.
Include:
Sign off with the name of their account manager: {}

```

```javascript
 
Hi, {}

```

```javascript
 
Hi, {}

```

```javascript
 
  Hey, {}! Thanks for being a part of our VIP program.
  Hey, {}! Thanks for reading.

```

```
 
> 
> 
```

```
 
> Hey, Chris! Thanks for being a part of our VIP program.
> 
```

```
 
  Your grade is an A
  Your grade is a B
  Your grade is a C
  Your grade is an F

```

```
 
> score = 85
> 
```

```
 
> Your grade is a B
> 
```

```javascript
 
  - {}x {} at ${} each

```

```
 
[
  ,
  ,
]

```

```javascript
 
  {}
  No items found.

```

```javascript
 
{}
Outputs: &lt;script&gt;alert(&quot;XSS&quot;);&lt;/script&gt;

```

```javascript
 
{}

```

```javascript
 
{}

```

```javascript
 
{}

```

```
 

```

```javascript
 
You are an AI assistant tasked with {}.
Context:
{}
*No additional context provided*
Instructions:
1. {}
{}. {}
Constraints:
- {}
Output Format:
{}
Example Input:
{}
Example Expected Output:
{}

```

```javascript
 
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{}</title>
    </head>
    <body>
        <header>
            <h1>Welcome, {}!</h1>
        </header>
        <nav>
                <a href="/profile">My Profile</a>
                <a href="/logout">Logout</a>
                <a href="/login">Login</a>
                <a href="/register">Register</a>
        </nav>
        <main>
                <div class="product">
                    <h2>{}</h2>
                    <p>Price: ${}</p>
                        <button>Add to Cart</button>
                        <span class="out-of-stock">Out of Stock</span>
                </div>
        </main>
    </body>
</html>

```

```javascript
 
SELECT 
    id, 
    {} 
FROM {}
WHERE 
        1=1
        organization_id = {}
        AND status = '{}'
ORDER BY 
        {} {}
        created_at DESC
LIMIT {}

```

```

###  
Email Template
**Context**: A flexible email template system that supports personalized messaging, dynamic sections, and optional signatures.
Copy

```

