---
category: functions
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: '**RBAC Example 1: Use Get Record**'
---

# **RBAC Example 1: Use Get Record**

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'restricting-access-rbac'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Restricting Access (RBAC) \| Xano Documentation'
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
In this example, each user has one of two roles: admin or staff.
####  
**RBAC Example 1: Use Get Record**
Now, let\'s set up an API endpoint that GETs all users but only if the user trying to call the endpoint has a role of admin.
Take note of the endpoint below, user authentication is required. Additionally, take note of the Function Stack:
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Get Record from user: This will use the authToken to find the user\'s ID and look up their information.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Precondition: This will enforce that the user\'s role is equal to admin. If it is not, then it will throw and error and stop the endpoint.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Query all records from user: This will only be performed if the user\'s role is an admin by passing the precondition.
    :::
In this example, the API endpoint requires an authenticated user. Then the Function Stack is set up to perform only if the user\'s role is equal to admin.
Get the record of the user who\'s calling the endpoint (requester) with the auth ID.
In this example, we are getting the record of the user based on their authenticated ID.
Next, set a precondition to enforce that the user (called requester in the example) has a role equal to admin.
Click on the pencil icon to open the Expression Builder and set the conditions for the precondition. Additionally, set your error type and message if the conditions are not met.
In this example, the requester.role must be equal to admin in order to pass the precondition.
If the precondition is met, then the user who is the requester will have permission to execute the rest of the Function Stack and complete the API endpoint.
####  
RBAC Example 2: Use Extras
Extras allow you to store data within the authentication token, which you can access and use on authenticated API endpoints.
First, you must set up the sign-up & login to include the user\'s role at the time of authentication.
In this example, we will use the login endpoint to pass the user\'s role into extras of the auth token at the time of authentication.
In this example, we are passing the user\'s role into the authToken at the time of login by utilizing extras.
Now that the user\'s role is passed into the authToken, we can eliminate the Get Record function from the previous example and reference \"extras.role\" in the precondition to enforce the user\'s role.
In this example, we can use the extras of the authenticated user to access the user\'s role and set the precondition equal to admin.
Set extras.role (as defined in the creation of the authentication token) equal to admin.
If the user\'s role is equal to admin then they will pass the precondition and have permission to execute the rest of the Function Stack. **
Last updated 6 months ago
Was this helpful?