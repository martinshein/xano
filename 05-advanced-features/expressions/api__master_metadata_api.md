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
title: 'API: Master Metadata Api'
---

# API: Master Metadata Api

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'master-metadata-api'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Master Metadata API \| Xano Documentation'
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
The master Metadata API Swagger documentation can be accessed by the following URL:
**https://app.xano.com/api:meta**
###  
Instance
####  
GET /instance/ - Get Single Instance
The GET request will provide details of a specific instance when provided the instance name
###  
get instance
get
[https://app.xano.com/api:meta]/instance/[]
get instance
Authentication: required
Authorizations
Path parameters
[[name][string][Required]]
Responses
[200]
Success!
application/json
[[Response][object]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
get
/instance/[]
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
GET /api:meta/instance/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```
Test it
[[200][]]
Success!
Copy
``` 
```
####  
GET /instance - Browse Instances
The GET request will provide a list of Instances associated with an account.
###  
browse instances
get
[https://app.xano.com/api:meta]/instance
browse instances
Authentication: required
Authorizations
Responses
[200]
Success!
application/json
[[Response][object\[\]]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
get
/instance
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
GET /api:meta/instance HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```
Test it
[[200][]]
Success!
Copy
``` 
[
]
```
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The response provides both the Xano domain and the custom domain (if applicable).
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The meta\_api value will provide access to the Metadata API for the given Instance.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The JSON of the Metadata API Swagger for the Instance is also provided.
    :::
###  
Snippet / Token
These endpoints provide functionality for managing private snippet access tokens.
For reference, the **canonical ID** of your snippet is found at the end of the URL.
Copy
``` 
https://www.xano.com/snippet/abC123Zx/
```
In this example URL, **abC123Zx** is our canonical.
####  
POST /snippet//token/{token\]
Use this endpoint to update a token\'s allowed number of installations.
###  
updates a snippet token
post
[https://app.xano.com/api:meta]/snippet/[]/token/[]
updates a snippet token
Authentication: required
Authorizations
Path parameters
[[canonical][string][Required]]
[[token][string][Required]]
Body
[application/json]
application/jsonmultipart/form-data
[[max\_installs][integer · int64][Required]]
[[current\_installs][integer · int64][Required]]
Responses
[200]
Success!
application/json
[[Response][object]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
post
/snippet/[]/token/[]
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
POST /api:meta/snippet//token/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 39
```
[application/json]
application/jsonmultipart/form-data
Test it
[[200][]]
Success!
Copy
``` 
```
####  
DELETE /snippet//token/
Use this endpoint to delete an access token from a snippet.
###  
deletes a snippet token
delete
[https://app.xano.com/api:meta]/snippet/[]/token/[]
deletes a snippet token
Authentication: required
Authorizations
Path parameters
[[canonical][string][Required]]
[[token][string][Required]]
Responses
[200]
Success!
application/json
[[Response][object]]
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
delete
/snippet/[]/token/[]
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
DELETE /api:meta/snippet//token/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```
Test it
[[200][]]
Success!
Copy
``` 
```
####  
GET /snippet//token
Use this endpoint to get a list of tokens for a snippet.
###  
returns a list of tokens for a snippet
get
[https://app.xano.com/api:meta]/snippet/[]/token
returns a list of tokens for a snippet
Authentication: required
Authorizations
Path parameters
[[canonical][string][Required]]
Responses
[200]
Success!
application/json
[[Response][object\[\]]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
get
/snippet/[]/token
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
GET /api:meta/snippet//token HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```
Test it
[[200][]]
Success!
Copy
``` 
[
]
```
####  
POST /snippet//token
Use this endpoint to create a new token for a snippet.
###  
creates a new install token on the snippet
post
[https://app.xano.com/api:meta]/snippet/[]/token
creates a new install token on the snippet
Authentication: required
Authorizations
Path parameters
[[canonical][string][Required]]
Body
[application/json]
application/jsonmultipart/form-data
[[max\_installs][integer · int64][Required]]
Responses
[200]
Success!
application/json
[[Response][object]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
post
/snippet/[]/token
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
POST /api:meta/snippet//token HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 18
```
[application/json]
application/jsonmultipart/form-data
Test it
[[200][]]
Success!
Copy
``` 
```
###  
Snippets
####  
GET /snippet/
Retrieve a specific snippet by its canonical ID
###  
get a specific snippet by ID
get
[https://app.xano.com/api:meta]/snippet/[]
get a specific snippet by ID
Authentication: required
Authorizations
Path parameters
[[canonical][string][Required]]
Responses
[200]
Success!
application/json
[[Response][object]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
get
/snippet/[]
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
GET /api:meta/snippet/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```
Test it
[[200][]]
Success!
Copy
``` 
```
####  
POST /snippet/
Update settings on the snippet, such as the access method and access description.
###  
update settings on the snippet
post
[https://app.xano.com/api:meta]/snippet/[]
update settings on the snippet
Authentication: required
Authorizations
Path parameters
[[canonical][string][Required]]
Body
[application/json]
application/jsonmultipart/form-data
[[install\_access][string · enum][Required]]Possible values:
`public`
`link`
`token`
[[install\_access\_description][string][Required]]
Responses
[200]
Success!
application/json
[[Response][object]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
post
/snippet/[]
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
POST /api:meta/snippet/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 63
```
[application/json]
application/jsonmultipart/form-data
Test it
[[200][]]
Success!
Copy
``` 
```
####  
GET /snippet
List all snippets owned by the authenticated user.
###  
list snippets owned by the authenticated user
get
[https://app.xano.com/api:meta]/snippet
list snippets owned by the authenticated user
Authentication: required
Authorizations
Query parameters
[[page][integer · int64][Optional]]
Responses
[200]
Success!
application/json
[[Response][object]]
Show properties
[400]
Input Error. Check the request payload for issues.
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
get
/snippet
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
GET /api:meta/snippet HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```
Test it
[[200][]]
Success!
Copy
``` 
{
  "curPage": 1,
  "nextPage": 1,
  "prevPage": 1,
  "items": [
  ]
}
```
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
GET /api:meta/instance/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*

```

```
 

```

```
 
GET /api:meta/instance HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*

```

```
 
[
]

```

```
 
https://www.xano.com/snippet/abC123Zx/

```

```
 
POST /api:meta/snippet//token/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 39

```

```
 

```

```
 
DELETE /api:meta/snippet//token/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*

```

```
 

```

```
 
GET /api:meta/snippet//token HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*

```

```
 
[
]

```

```
 
POST /api:meta/snippet//token HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 18

```

```
 

```

```
 
GET /api:meta/snippet/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*

```

```
 

```

```
 
POST /api:meta/snippet/ HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 63

```

```
 

```

```
 
GET /api:meta/snippet HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*

```

```javascript
 
{
  "curPage": 1,
  "nextPage": 1,
  "prevPage": 1,
  "items": [
  ]
}

```

