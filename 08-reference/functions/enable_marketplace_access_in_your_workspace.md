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
title: Enable Marketplace access in your workspace
---

# Enable Marketplace access in your workspace

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'oauth-sso'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'OAuth (SSO) \| Xano Documentation'
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
    OAuth vs JWE Token Authentication
Was this helpful?
Copy
1.  Building Backend Features
2.  User Authentication & User Data
OAuth (SSO) 
===========
**OAuth** is a security framework that allows you to grant websites or applications access to your information without sharing your password. It acts like a permission slip, letting a service access part of your data from another service on your behalf. For example, you might log into a new app using your Google or Facebook account, and OAuth handles the secure sharing of your data between the services.
**OAuth vs JWE Token Authentication**
**OAuth** is like giving a valet key to a friend, allowing them limited access to your car. It lets services share your data safely without sharing your password. You\'re still in control, and you can revoke this access at any time.
**JWE Token Authentication** is more like using a sealed envelope. Your information is encrypted and can only be read by the intended recipient. It ensures data integrity and privacy but doesn\'t manage who has access like OAuth does. It\'s great for situations where secure data transmission is key.
The OAuth Flow
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Client Registration**: The client application registers with the OAuth service provider to obtain a client ID and client secret, which are used to identify the application during the OAuth flow.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **User Authorization**: The client redirects the user to the authorization server where the user logs in and consents to the application\'s data access request. This is where the user would see a Google, Facebook, X, or other sign-in option on your frontend.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Authorization Grant**: Once the user signs in and approves access, the authorization server issues an authorization grant to the client, typically in the form of a code sent via a URL query parameter. This would be one of your APIs in Xano that is designed to ingest that authorization.
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Access Token Request**: Your Xano API sends a request to the authorization server\'s token endpoint, including the authorization grant and credentials (client ID and secret), to obtain an access token. Once we\'ve determined that token is valid, it will be traded for a Xano JWE token to proceed with standard authentication methods.
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Access Token Response**: The authorization server verifies the request and returns an access token, which the client can use to access protected resources on the user\'s behalf.
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Access Resource**: The client uses the access token to make requests to the resource server, accessing the user\'s resources as allowed by the token\'s scope.
    :::
Building OAuth in Xano
<div>
1
###  
Enable Marketplace access in your workspace
If you don\'t see **Marketplace** in your left-hand navigation menu, head to your workspace settings, and click the icon in the top-right corner, and click **Settings**.
Check the box to **Enable Marketplace**
2
###  
Access the Marketplace and browse for your OAuth extension of choice
Xano provides several prebuilt OAuth flows that you can import from here into your workspace.
</div>
Last updated 6 months ago
Was this helpful?