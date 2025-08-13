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
title: Example Use Cases
---

# Example Use Cases

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'response-caching'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Response Caching \| Xano Documentation'
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
**Watch a practical example** of Response Caching using the Star Wars API
From the settings of an API Endpoint or Custom Function response caching can be accessed. Response caching is an abstracted caching method to cache the response of an endpoint or function.
[]
You can choose from a number of different settings to determine how to cache the response.
[]
**TTL** - Stands for time to live. This defines how long to cache the response for. Options range from 5 seconds to 7 days. After the TTL expires, the query will run normally and reset the response cache.
**Use inputs for caching signature** - This is defaulted to yes. It will create a response cache for each new or unique set of inputs for the duration of the TTL.
**Use IP address for caching signature** - This is defaulted to no. It can be used if you wish to record a response cache on a per IP address basis.
**HTTP Request Header Names** - This is optional. You are able to cache the HTTP request headers of the response. Add the request header name or names that you wish to cache.
**Environment Variable Names** - This is optional. It allows you to cache any defined environment variable names to the response cache.
**Use Authentication ID for caching signature** - When an API endpoint requires authentication, this option becomes available. This can be turned on to enable a caching on a per user basis for authenticated endpoints.
[]
####  
Example Use Cases
**Use inputs and disable authentication ID for caching signature**
Company statistics for your entire team. If you need to display company statistics for your entire team then you may consider using inputs and disabling authentication ID for caching signature. You API endpoint would require authentication so that only your team can access the API but you would disable the authentication ID for caching. This would make it so the cache response is not on a per user basis. Since it is company statistics you want each user to see the same statistics. Using inputs enables each searched or inputted value gets cached, so if other team members search or input the same values then the response will already be there.
**Use inputs and use authentication ID for caching signature**
Personal statistics. In this scenario you would enable both inputs and authentication ID for caching signature. This would cache responses on a per user basis. For example, you might have each individual sales rep reviewing their own statistics for the quarter. Enabling inputs would cache the response for each inputted value. Additionally, enabling authentication ID for caching signature (with the appropriate business logic) would cache the responses on a per user basis.
**Disable inputs and disable authentication ID for caching signature**
There\'s a movie night event and you want to generate a random movie. Imagine you have an API that inputs a category or genre of movie and based on that, returns a random movie. By disabling both inputs and authentication ID for caching signature, this will allow for the first search on this API to generate a random movie to be played during movie night. It won\'t matter what other people search. So if the first person searched Science-Fiction and the result is Star Wars then all other searches (drama, action, comedy, etc.) will return Star Wars. Now you have your random movie for movie night.
Last updated 6 months ago
Was this helpful?