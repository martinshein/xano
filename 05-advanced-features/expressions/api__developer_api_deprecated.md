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
title: 'API: Developer Api Deprecated'
---

# API: Developer Api Deprecated

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'developer-api-deprecated'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Developer API (Deprecated) \| Xano Documentation'
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
    Step 1: Generate your Developer API Key
Was this helpful?
Copy
1.  Xano Features
2.  Advanced Back-end Features
Developer API (Deprecated) 
==========================
The Developer API is deprecated. Please see the Metadata API (beta) for the newest solution.
<div>
</div>
The Xano Developer API allows you to interact with your account in an automated fashion.
The primary use case is the ability to authenticate and then retrieve Swagger/OpenAPI documentation for each of your API groups on each of your Xano instances. More functionality will be coming soon.
Since Xano supports a single tenant infrastructure on each of its premium instances, it is important to understand that different authentication is required for different aspects of this API.
Authentication starts with your Developer API Key, which allows you to authenticate your account with the master service. This master service is responsible for managing your account, subscriptions, and instances.
By listing each instance you have access to, you will then be able to re-authenticate with each individual instance to view the Developer API for that instance. Then you will have access to list workspaces and the API groups within each workspace, which then gives you access to the appropriate Swagger documentation for each API group.
###  
Step 1: Generate your Developer API Key
This is available on the Account page. Every account has the ability to have a single Developer API Key. **Once this is generated, it is no longer possible to view the key**, so it is very important to write this down in a safe place, so it isn\'t forgotten. If it is forgotten, then you need to revoke the current one and generate a new key.
Generate a Developer API key from the Account page.
###  
Step 2: Xano Master Service Documentation
Now that you have your API Key, you can start authenticating against the API endpoints for the Xano master service. The API documentation is detailed at <https://app.xano.com/api:developer>.
Currently, there is only support to list your Xano instances, but more functionality will be fleshed out over the next several releases.
Authentication is handled using the Authorization HTTP header along with the Bearer token specification.
If you are viewing the Swagger documentation, then you can click the \"Authorize\" button and paste in your Developer API key. Then you can click on the Instances endpoint and click the \"Try Out\" button to execute the API endpoint.
If you are using the API directly via your front-end or the CURL command line utility, then you would need to include your Developer API key as follows.
In the CURL example below you would replace the text YOUR\_DEVELOPER\_API\_KEY with your actual Developer API Key.
Copy
``` 
curl -X 'GET' \
  'https://app.xano.com/api:developer/instance' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOUR_DEVELOPER_API_KEY'
```
The following would be an example response to expect, if your account had access to two instances.
Copy
``` 
[
  ,
]
```
###  
Step 3: Fetch the tokenUrl for your instance
The tokenUrl for each instance has an authenticated token parameter to give you access to the Authorization token required to call the API for that specific instance.
In the above example, if we fetch the tokenUrl, then the following example response would be expected.
Copy
``` 
```
The authToken key will be used to authenticate to any endpoints listed within the API or swaggerspec links.
**The API key** is a link to the Swagger documentation for the Developer APIs for this specific instance.
**The swaggerspec key** is a link to the json spec for the Swagger documentation in case you want to programmatically parse the endpoints available within the documentation.
**The origin key** is useful for knowing the desired http origin of any requests sent to the instance. This is normally Xano URL, but can change if a custom domain is enabled.
###  
Step 4: Call the APIs of your Instance
Now that we have the authToken from Step 3, we can call the endpoints available within the API link above.
Any endpoints within this instance that require authentication, must use this authToken and not your API Developer Key. The API Developer Key is only intended for the Xano master service.
Copy
``` 
curl -X 'GET' \
  'https://x8d0-doy0-xx99.n0.xano.io/api:developer/workspace' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJ...'
```
Below is an example response to the workspace endpoint listed above.
Copy
``` 
[
  {
    "id": 2,
    "name": "Book Marketplace",
    "description": "This is an example workspace.",
    "apigroups": [
      ,
    ]
  }
]
```
From this response, you can see there is one workspace with two API Groups. Each API Group has its own api and swaggerspec key. The difference here is that these APIs are the ones built by you in your own instance. This also means that these will require their own Authentication.
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
curl -X 'GET' \
  'https://app.xano.com/api:developer/instance' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOUR_DEVELOPER_API_KEY'

```

```
 
[
  ,
]

```

```
 

```

```
 
curl -X 'GET' \
  'https://x8d0-doy0-xx99.n0.xano.io/api:developer/workspace' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJ...'

```

```javascript
 
[
  {
    "id": 2,
    "name": "Book Marketplace",
    "description": "This is an example workspace.",
    "apigroups": [
      ,
    ]
  }
]

```

