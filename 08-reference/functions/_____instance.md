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
title: "[\U0001F5A5\uFE0F] Instance"
---

# [🖥️] Instance

[🛠️]The Visual Builder
    :::
        ::: 
            ::: 
            -   Swagger (OpenAPI
                Documentation)
            :::
            ::: 
            -   Async
                Functions
            :::
        -   Background
            Tasks
        -   Triggers
        -   Middleware
        -   Configuring
            Expressions
        -   Working with
            Data
        :::
        ::: 
        -   AI
            Tools
            ::: 
                ::: 
                -   External Filtering
                    Examples
                :::
            -   Get
                Record
            -   Add
                Record
            -   Edit
                Record
            -   Add or Edit
                Record
            -   Patch
                Record
            -   Delete
                Record
            -   Bulk
                Operations
            -   Database
                Transaction
            -   External Database
                Query
            -   Direct Database
                Query
            -   Get Database
                Schema
            :::
            ::: 
            -   Create
                Variable
            -   Update
                Variable
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
            -   Realtime
                Functions
            -   External API
                Request
            -   Lambda
                Functions
            :::
        -   Data Caching
            (Redis)
        -   Custom
            Functions
        -   Utility
            Functions
        -   File
            Storage
        -   Cloud
            Services
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
        -   Response
            Caching
        :::
-   ::: 
    Testing and Debugging
    :::
-   ::: 
    The Database
    :::
        ::: 
        -   Using the Xano
            Database
        -   Field
            Types
        -   Relationships
        -   Database
            Views
        -   Export and
            Sharing
        -   Data
            Sources
        :::
        ::: 
        -   Airtable to
            Xano
        -   Supabase to
            Xano
        -   CSV Import &
            Export
        :::
        ::: 
        -   Storage
        -   Indexing
        -   Maintenance
        -   Schema
            Versioning
        :::
-   ::: 
    Build For AI
    :::
        ::: 
        -   Templates
        :::
        ::: 
        -   Connecting
            Clients
        -   MCP
            Functions
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
        -   Separating User
            Data
        -   Restricting Access
            (RBAC)
        -   OAuth
            (SSO)
        :::
-   ::: 
    Xano Features
    :::
        ::: 
        -   Release Track
            Preferences
        -   Static IP
            (Outgoing)
        -   Change Server
            Region
        -   Direct Database
            Connector
        -   Backup and
            Restore
        -   Security
            Policy
        :::
        ::: 
        -   Audit
            Logs
        :::
        ::: 
        -   Xano
            Link
        -   Developer API
            (Deprecated)
        :::
        ::: 
        -   Master Metadata
            API
        -   Tables and
            Schema
        -   Content
        -   Search
        -   File
        -   Request
            History
        -   Workspace Import and
            Export
        -   Token Scopes
            Reference
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
        -   Agency
            Dashboard
        -   Client
            Invite
        -   Transfer
            Ownership
        -   Agency
            Profile
        -   Commission
        -   Private
            Marketplace
        :::
-   ::: 
    Custom Plans (Enterprise)
    :::
        ::: 
            ::: 
                ::: 
                -   Choosing a
                    Model
                :::
            :::
        -   Tenant
            Center
        -   Compliance
            Center
        -   Security
            Policy
        -   Instance
            Activity
        -   Deployment
        -   RBAC (Role-based Access
            Control)
        -   Xano
            Link
        -   Resource
            Management
        :::
-   ::: 
    Your Xano Account
    :::
-   ::: 
    Troubleshooting & Support
    :::
        ::: 
        -   When a single workflow feels
            slow
        -   When everything feels
            slow
        -   RAM
            Usage
        -   Function Stack
            Performance
        :::
        ::: 
        -   Granting
            Access
        -   Community Code of
            Conduct
        -   Community Content Modification
            Policy
        -   Reporting Potential Bugs and
            Issues
        :::
-   ::: 
    Special Pricing
    :::
-   ::: 
    Security
    :::
-   ::: 
    :::
     Instance
Was this helpful?
Copy
1.  Before You
    Begin
Key Concepts 
============
Get a quick primer on the key concepts and terminology that we use
throughout the product and documentation to get you started quickly.
------------------------------------------------------------------------
###  
[🖥️] Instance
<div>
</div>
Your Xano instance is the heart of everything you do in Xano. An
**instance** is a dedicated server that we manage for you and it
contains all of your Xano data, including APIs, databases, user data,
and more.
On all of our paid plans, each instance has its own dedicated resources,
is always available, and completely isolated from other Xano users. This
means that even if, in the rare occurrence that one user experiences an
issue with their own Xano backend, it won\'t impact anybody else.
On our free plan, you are on a shared instance with other Xano users.
------------------------------------------------------------------------
###  
[📂] Workspace
<div>
</div>
In your Xano instance, you can have multiple **workspaces**. Think of a
workspace as a separate container for each project you\'re building in
Xano. Your workspaces are completely isolated from each other, but all
share the same compute resources provided by your instance.
------------------------------------------------------------------------
###  
🧠 Backend
<div>
</div>
Think of the backend as the brains of a website or app. It\'s all the
behind-the-scenes action that users don\'t see. When you\'re browsing an
online store, the backend is figuring out what products to show you,
keeping track of your shopping cart, and making sure your payment goes
through. It\'s like the engine room of a ship - not glamorous, but
absolutely crucial.
------------------------------------------------------------------------
###  
📱 Frontend
<div>
</div>
The frontend is everything you see and interact with on a website or
app. It\'s the pretty face that greets you when you land on a page. This
includes the layout, colors, buttons, and forms you fill out. A good
frontend makes using a website feel smooth and intuitive, like a
well-designed cockpit in an airplane. It\'s all about creating a great
user experience.
------------------------------------------------------------------------
###  
🗄️ Database
<div>
</div>
A database is essentially a digital warehouse for information. It\'s
where websites and apps store all their data in an organized way. Need
to look up a customer\'s order history? That\'s stored in a database.
Want to see all products under \$50? The database has that info too.
It\'s like a super-efficient librarian who can find any piece of
information in milliseconds.
------------------------------------------------------------------------
###  
🔌 API
<div>
</div>
APIs allow different applications to communicate and share data with
each other. When you use Google Maps inside another app, that\'s an API
at work. When you click a Buy Now button on Amazon, APIs are firing at
all cylinders behind the scenes.
APIs don\'t have to only be based on user action, either. For example,
most websites implement some sort of tracking to ensure that the user
experience is as smooth as possible. When you visit these websites,
there are API calls being made as you navigate through their frontend.
APIs set the rules for how different pieces of software can talk to each
other, making it possible for developers to integrate various services
without starting from scratch.
An API has a few main components.
<div>
1
###  
Headers
Headers are the configuration that rides along with an API request. They
contain information like where the request is coming from and what type
of data it contains.
2
###  
Method
The method, also known as the verb, is assigned to an API to typically
dictate the type of operation the API is designed to complete.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **GET**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Retrieve data
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **POST**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Send data
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **PUT / PATCH**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Update data
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **DELETE**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Delete data
        :::
    :::
Please note that when you build APIs in Xano, you can choose the method
to apply, giving you full flexibility in exactly what function that API
serves. While it isn\'t always best practice, a DELETE endpoint could
technically do nothing but add new data, if it makes sense for your use
case.
3
###  
Query parameters / Request body
Query parameters and the request body are kind of the same thing, but
sent in an API request in different ways.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Query parameters** live as part of the request URL. If the API URL
    is `https://myapi.com/getThings` and expects you to send a
    thingId with your request, you would append it to the URL with
    `?thingId=99`, so your full
    request URL would be
    `https://myapi.com/getThings?thingId=99.` You would typically use query
    parameters for GET and DELETE endpoints.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Request Body** is like a set of query parameters, but sent as a
    JSON object. It\'s more flexible when sending complex data types,
    such as lists, nested objects, or files.
    :::
In the Xano visual builder, these are known as **inputs**. You can add
inputs manually, or add a **Database Link** input to automatically
populate and sync all fields from a database table.
4
###  
Response
The response is whatever the API sends back once it has completed the
logic it is meant to perform. An API doesn\'t necessarily need to
deliver a response, but it is typical.
Think of your frontend sending an API request when a user logs in. That
API request would probably return information about the user logging in,
such as their name, location, or other relevant user data.
A response has a few different pieces, similar to what\'s included in
the request, including **response headers** and a **response body**.
</div>
------------------------------------------------------------------------
🏷️ Variables
Variables are like containers or labels that store information you want
to use later in a workflow. Think of them as named boxes where you can
keep different types of items, such as numbers, words, or lists. You
give each box a name so you can easily find and use the information it
holds whenever you need it in your project. This makes it simple to
update or change the data without needing to rewrite everything.
Variables are temporary and exist only while a workflow is running, used
for storing information you need to access quickly, whereas values in a
database are like records in a filing cabinet, stored permanently until
you decide to update or delete them, accessible across various workflows
and sessions. This makes databases ideal for managing large sets of data
over time, and variables more appropriate for temporary data handling.
------------------------------------------------------------------------
###  
🗃️ JSON
<div>
</div>
JSON is a handy way of formatting data that\'s easy for both humans and
computers to understand. JSON organizes information into simple
key-value pairs, kind of like a really well-structured grocery list.
It\'s lightweight and flexible, which is why developers love using it to
pass data between servers and web applications.
For an example of how JSON can supercharge your data structure, take
this example of a hand-written grocery list compared to a JSON
equivalent.
Handwritten List
JSON
Copy
``` 
[
  ,
  ,
  ,
  ,
  ,
  ,
]
```
JSON follows a structure of `key: value` pairs.
The key typically defines what the value represents, and the value is
the actual value itself.
While it may seem similar, **JSON is not code**. It is just a standard
way to structure data. For a real-world comparison, maybe you have a
favorite news site or blog that you visit daily. You are used to the
format they provide so the information is easily digestible. Now,
imagine if every day, they decided to follow a different, unorganized
structure instead. This is why data standardization is important, and
JSON is a very effective way of achieving this.
####  
📄 Objects
An object represents the whole of a thing, such as a person, place,
vehicle, form submission \-- the possibilities are endless and fully
dependent on what you are building. A JSON object can have multiple keys
and values inside.
Here is an example of a JSON object that represents user data.
Copy
``` 
```
As you can see, we have our **keys**, such as `name`, `age`, and
`city`, as well as our values, which are
the actual data that belongs to this user.
####  
📑 Arrays
JSON can also represent lists of items, like the example below. It looks
almost exactly the same, but now we have multiple people inside of an
**array**, or list, denoted by square brackets.
Copy
``` 
[
  ,
  ,
]
```
####  
🪺 Nested Data
Values don\'t just have to be single items, such as a person\'s name or
email. You can also supply other objects or arrays for your values. In
the below example, we\'ve added an interests key and supplied an array
of text strings for the value.
Copy
``` 
```
###  
ℹ️ JSON Data Types
You may have noticed a few mentions of things like integers or strings
when learning about JSON. It is important to know what types of data are
valid representations inside of a JSON object. One of the most important
things to remember when working with JSON is that quotation marks are
incredibly important and can be the difference between something working
or falling apart.
🔤 **Strings** are surrounded by \"quotation marks\" and are just plain
text.
Copy
``` 
```
🔢 **Integers** are numbers that are not decimals. Notice how we do not
have quotation marks around `1994` in the
example below. If we used `"1994"`
instead, this would become a string.
Copy
``` 
```
🔢 **Decimals** are numbers that contain a decimal point.
Copy
``` 
```
✅ **Booleans** are true or false values.
Copy
``` 
    "exists": true
```
⛔ **Null** is a special data type that represents nothing in situations
where you need to specify that nothing is provided.
Copy
``` 
    "phone": null
```
📑 **Arrays** are lists of things. These could be any other valid JSON
data type. You could even have an array of arrays if you wanted.
Copy
``` 
[
    "red",
    "blue",
    "green"
    ]
```
📄 **Objects** are collections of key-value pairs enclosed in curly
braces. Keys are always strings, but values can be any valid JSON data
type.
Copy
``` 
```
Last updated 5 months ago
Was this helpful?

## Code Examples

```
 
[
  ,
  ,
  ,
  ,
  ,
  ,
]

```

```
 

```

```
 
[
  ,
  ,
]

```

```
 

```

```
 

```

```
 

```

```
 

```

```
 
    "exists": true

```

```
 
    "phone": null

```

```
 
[
    "red",
    "blue",
    "green"
    ]

```

```
 

```

