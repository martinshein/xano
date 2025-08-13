---
category: ai-services
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
Last updated 5 days ago
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

