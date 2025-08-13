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
title: Get Workspaces
---

# Get Workspaces

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'tables-and-schema'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Tables and Schema \| Xano Documentation'
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
    Get Workspaces
Was this helpful?
Copy
1.  Xano Features
2.  Metadata API
Tables and Schema 
=================
The following are various examples of how to leverage the Metadata API to create and modify database tables including the schema and indexes included within them.
<div>
</div>
###  
Get Workspaces
Browse the workspaces of the instance. This API endpoint does not require any parameters. Retrieving the workspaces gives you information on the workspace name and ID. The workspace ID is particularly important for use in other Metadata API endpoints.
Example response body:
Copy
``` 
[
  ,
  ,
]
```
###  
Get Tables of a Workspace
Browse workspace tables. This API endpoint requires a workspace ID and will provide various information about each database table in a workspace, including database table ID, which is needed in various Metadata API endpoints.
Example response body:
Copy
``` 
[
  ,
  ,
]
```
###  
Create Table and Add Schema One by One
First, create a new table in the desired workspace. The default request values suffice. In this example, first, we will create a table and then add schema individually. The Metadata API is capable of adding schema in bulk but that will be covered in another example.
Example response body:
Copy
``` 
```
Taking the newly created database table ID, we can add schema 1 by 1 to the table.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    A text field called name.
    :::
Example response body:
Copy
``` 
```
Next, let\'s add an integer field called score with a default value of 30
As we execute these Metadata API calls, our new table in Xano is being created along with the new schema, one by one.
###  
Create an Index
The Metadata API gives control over indexes on database tables. In this example, let\'s create a Unique Index on the name field of new table 123.
Example response body:
Copy
``` 
```
The API responds with the ID of the index. In Xano, we can see the index has been created:
###  
Create Table with Schema and an Index in One Call
In this example, we will create a new database table along with schema and an index in the same API call. The Metadata API is flexible enough to accommodate this method.
Here\'s the example request body:
Copy
``` 
{
  "name": "new stuff",
  "description": "",
  "auth": null,
  "guid": null,
  "schema": [
    ,
    ,
  ],
  "index":[
    {
      "type": "btree",
      "fields": [
      ]
    }
  ]
}
```
This creates a new table called \"new stuff\" with three fields: id, created\_at, and name with an index on the name field.
For defining schema, the Metadata API needs a minimum of \"name\" and \"type\" but the other fields aren\'t required. If you are defining schema during table creation, the first field must be the ID field.
For Request body examples of schema and index, check out the PUT examples in Swagger for table/schema and table/index.
###  
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
###  
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
[
  ,
  ,
]

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

```javascript
 
{
  "name": "new stuff",
  "description": "",
  "auth": null,
  "guid": null,
  "schema": [
    ,
    ,
  ],
  "index":[
    {
      "type": "btree",
      "fields": [
      ]
    }
  ]
}

```

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

