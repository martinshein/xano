---
category: expressions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Search where ID = 10
---

# Search where ID = 10

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: search
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Search \| Xano Documentation'
viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---
[](../../index.html)
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
    Browse Content
Was this helpful?
Copy
1.  Xano Features
2.  Metadata API
Search 
======
This section is broken down into Browse Content and Search. Browse Content is a simple method of getting or reading the content of a database table. It can be optionally combined with paging.
Search is an advanced method of filtering, sorting, and paging database content. It is flexible and powerful and enables you to return content based on the parameters you define.
Please note that the Metadata APIs for browsing content do not react to API Access settings. All fields will be returned regardless of this setting.
Browse Content
Browse table content is a simple method of getting content (database records) in a database table. It requires a workspace ID and table ID, while paging is optional.
Example response body:
Copy
``` 
{
  "items": [
    ,
    ,
    ,
  ],
  "itemsReceived": 4,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 4,
  "pageTotal": 1
}
```
Search
Search via the Metadata API is powerful and flexible to return the exact database content you are searching for.
####  
Search where ID = 10
In this example, we will search the Items table where ID = 10
Search can be done as a single object or array if there is only one search parameter. If there are multiple parameters then it must be an array.
You can pass just what you want in the request body. For example, if all we want to do is search then we just need to pass search to the body.
With paging, sort, and search as an array.
Copy
``` 
{
  "page": 1,
  "per_page": 50,
  "sort": ,
  "search": []
}
```
With paging, sort, and search as a single object.
Copy
``` 
{
  "page": 1,
  "per_page": 50,
  "sort": ,
  "search": 
}
```
With just search, as an array.
Copy
``` 
{
  "search": []
}
```
With just search, as a single object.
Copy
``` 
{
  "search": 
}
```
For this example, all of the above are acceptable for the request body.
Example response body:
Copy
``` 
{
  "items": [
  ],
  "itemsReceived": 1,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 1,
  "pageTotal": 1
}
```
####  
Search where Price \> 30 and Price \< 70
In this example, we are searching for content where price is \> 30 and price is \< 70.
Example request body:
Copy
``` 
{
  "search": [,
]
}
```
Example response body:
Copy
``` 
{
  "items": [
    ,
    ,
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}
```
####  
Search where Price \< 30 or Price \> 70
In this example, we will search for where the price is \< 30 or the price is \> 70
Example request body:
Copy
``` 
{
  "search": [
,
]
}
```
Notice how the or is formatted after the Price is \> 70 expression.
Example response body:
Copy
``` 
{
  "items": [
    ,
    ,
    ,
    ,
    ,
  ],
  "itemsReceived": 6,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 6,
  "pageTotal": 1
}
```
####  
In and Not In
The IN and NOT IN operators are great for working with lists and can also be thought of as another version of \"or\" operators. In the first example, we will search where the ID is IN \[2,3,7\].
Example request body:
Copy
``` 
{
  "search": 
}
```
Example response body:
Copy
``` 
{
  "items": [
    ,
    ,
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}
```
In the second example, we will search where ID is NOT IN \[1,2,3,4,6,7,8,9\]
Example request body:
Copy
``` 
{
  "search": 
}
```
Example response body:
Copy
``` 
{
  "items": [
    ,
  ],
  "itemsReceived": 2,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 2,
  "pageTotal": 1
}
```
###  
Sort
Sort is flexible, like search, in the sense that it accepts a single object or an array for a single sort parameter. It also supports multiple sorts, which require an array format.
####  
Single Sort
In this example, we will sort the category table by the name in ascending order.
Example request body:
Copy
``` 
{
  "sort": 
}
```
Also acceptable:
Copy
``` 
{
  "sort": []
}
```
Example response body:
Copy
``` 
{
  "items": [
    ,
    ,
    ,
    ,
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}
```
####  
Multi-Sort
In this example, we will first sort the content by rating in descending order, then the name in ascending order.
Example request body:
Copy
``` 
{
  "sort": [,
]
}
```
Example response body:
Copy
``` 
{
  "items": [
    ,
    ,
    ,
    ,
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}
```
Last updated 6 months ago
Was this helpful?

## Code Examples

```javascript
 
{
  "items": [
    ,
    ,
    ,
  ],
  "itemsReceived": 4,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 4,
  "pageTotal": 1
}

```

```javascript
 
{
  "page": 1,
  "per_page": 50,
  "sort": ,
  "search": []
}

```

```javascript
 
{
  "page": 1,
  "per_page": 50,
  "sort": ,
  "search": 
}

```

```javascript
 
{
  "search": []
}

```

```javascript
 
{
  "search": 
}

```

```javascript
 
{
  "items": [
  ],
  "itemsReceived": 1,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 1,
  "pageTotal": 1
}

```

```javascript
 
{
  "search": [,
]
}

```

```javascript
 
{
  "items": [
    ,
    ,
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}

```

```javascript
 
{
  "search": [
,
]
}

```

```javascript
 
{
  "items": [
    ,
    ,
    ,
    ,
    ,
  ],
  "itemsReceived": 6,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 6,
  "pageTotal": 1
}

```

```javascript
 
{
  "search": 
}

```

```javascript
 
{
  "items": [
    ,
    ,
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}

```

```javascript
 
{
  "search": 
}

```

```javascript
 
{
  "items": [
    ,
  ],
  "itemsReceived": 2,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 2,
  "pageTotal": 1
}

```

```javascript
 
{
  "sort": 
}

```

```javascript
 
{
  "sort": []
}

```

```javascript
 
{
  "items": [
    ,
    ,
    ,
    ,
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}

```

```javascript
 
{
  "sort": [,
]
}

```

```javascript
 
{
  "items": [
    ,
    ,
    ,
    ,
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}

```

