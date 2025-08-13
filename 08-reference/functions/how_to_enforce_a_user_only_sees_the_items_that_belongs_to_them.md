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
title: How to enforce a user only sees the items that belongs to them
---

# How to enforce a user only sees the items that belongs to them

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'separating-user-data'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Separating User Data \| Xano Documentation'
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
For this example, we have three users in our user table: Steph, Klay, and Jordan.
There is also an items table. Each item belongs to a user.
####  
How to enforce a user only sees the items that belongs to them
Here we have an API endpoint, which gets all the items from the items table. The first step is to require user authentication on the endpoint.
Require authentication for the API endpoint.
Now that authentication is required, the next step is to open the Query All Records function and add an expression to the by custom query section.
Copy
``` 
WHERE
db: items.user_id = auth id
```
Add an expression to the Query All Records function for items.
Filter the record where the user\_id must be equal to the auth id.
When we go to run the API endpoint in Run&Debug, an auth token is required to run the API. In Xano, we can easily search for a user to use a auth token for testing. In your application, the user will need to authenticate first by logging in or signing up.
Let\'s select user 2, Klay and run the API endpoint:
The result is all the items associated with user id = 2:
Items only belonging to user 2 are returned.
####  
Added layer of security with precondition
We can add an additional layer of security with the use of preconditions.
First, use a Get Record on the user table with a field value of the auth id.
Get the user record with the auth id.
Then use a precondition to enforce the auth ID is equal to the id from the Get Record.
Copy
``` 
WHERE
auth id = var: user.id
```
Set a precondition where the ID of the user record is equal to the auth id.
####  
How to enforce the user can only edit data that belongs to them
When it comes to editing data, the function stack will also use a precondition. The API endpoint will once again require authentication.
First, we need to Get the Record of the item that the user wants to edit.
First, Get the Record that the user is trying to edit.
Getting the existing record allows us to check if it belongs to the user.
Next, use a Precondition to say:
Copy
``` 
WHERE
var: items_1 |GET| "user_id" = auth id
```
The precondition enforces that the record belongs to the user trying to edit it. Using the GET filter makes sure that the record exists - if it doesn\'t the precondition will fail.
Here we use the GET filter with a default value of 0. This helps us account for existence of the record we want to edit. If the record does not exist, the precondition will trigger because a user\_id value of 0 will not match the auth ID.
If the precondition passes, then the function stack will continue to run and edit the data. If it fails, it will throw an error and stop execution.
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
WHERE
db: items.user_id = auth id

```

```
 
WHERE
auth id = var: user.id

```

```
 
WHERE
var: items_1 |GET| "user_id" = auth id

```

