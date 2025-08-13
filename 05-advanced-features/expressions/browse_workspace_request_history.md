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
title: Browse Workspace Request History
---

# Browse Workspace Request History

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'request-history'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Request History \| Xano Documentation'
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
    Browse Workspace Request History
Was this helpful?
Copy
1.  Xano Features
2.  Metadata API
Request History 
===============
The Metadata API enables you to interact with the API Request History of a given instance.
<div>
</div>
###  
Browse Workspace Request History
Browse is a straightforward approach to getting API Request History. The required parameter is the workspace ID. However, you can drill down further with the branch, API Group, or specific API Endpoint.
**Required Parameters**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Workspace ID (workspace\_id)
    :::
**Optional Parameters**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Branch ID (branch\_id) - Workspace Branch ID.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    API ID (api\_id) - The API Group ID.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Query ID (query\_id) - The ID of a specific API Endpoint.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Page
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Per\_Page - (500 max)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    include\_output - (true or false) - If you want to include the output of each API request.
    :::
###  
Search
Search workspace history allows for granular filtering and sorting of a workspace\'s API Request History.
Request History is similar to content search, except instead of fields for searching and filtering, request history uses the same options from the Xano dashboard.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    duration - duration of an API request, in seconds.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    status - the status code.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    created\_at - the time of execution, as a timestamp in milliseconds.
    :::
####  
Examples:
**Search for requests with a duration of less than 2 seconds. Sort by the longest duration.**
In this example, we are searching for requests with a duration less than 2 seconds and sorting the results by duration in descending order.
Example request body:
Copy
``` 
{
  "page": 1,
  "per_page": 50,
  "branch_id": null,
  "api_id": null,
  "query_id": null,
  "sort": ,
  "search": [
              ]
}
```
**Search for Reqeusts with a status code of 400. Sort the Results by oldest.**
Example Request Body:
Copy
``` 
{
  "page": 1,
  "per_page": 50,
  "branch_id": null,
  "api_id": null,
  "query_id": null,
  "sort": ,
  "search": []
}
```
Last updated 6 months ago
Was this helpful?

## Code Examples

```javascript
 
{
  "page": 1,
  "per_page": 50,
  "branch_id": null,
  "api_id": null,
  "query_id": null,
  "sort": ,
  "search": [
              ]
}

```

```javascript
 
{
  "page": 1,
  "per_page": 50,
  "branch_id": null,
  "api_id": null,
  "query_id": null,
  "sort": ,
  "search": []
}

```

