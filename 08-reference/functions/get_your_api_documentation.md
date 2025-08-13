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
title: Get your API documentation
---

# Get your API documentation

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
description: 'Get the latest on using platforms like Bolt.new, v0, and Cursor with Xano'
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'using-ai-builders-with-xano'
twitter:card: summary\_large\_image
twitter:description: 'Get the latest on using platforms like Bolt.new, v0, and Cursor with Xano'
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Using AI Builders with Xano \| Xano Documentation'
viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---
[](../index.html)
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
    The Key: Auto-documented APIs
Was this helpful?
Copy
1.  Build With AI
Using AI Builders with Xano 
===========================
Get the latest on using platforms like Bolt.new, v0, and Cursor with Xano
[](https://youtu.be/m4YoJXaqdEc?si=-T0O0RXVTL93HHls)
 **Using Xano with Cursor**
 **Using Swagger Docs with ChatGPT**
The Key: Auto-documented APIs
When you\'re building API endpoints in Xano, they\'re auto-documented in the OpenAPI specification using Swagger. This means that without any effort from you, you already have AI-ready documentation that can be used in combination with your favorite AI builder to spin up fully baked applications very quickly.
We have a full section on this functionality here: Swagger (OpenAPI Documentation). For now though, you can get started quickly with the instructions below.
<div>
1
###  
Get your API documentation
Inside your API group(s), you\'ll find a link to the documentation in the top-right, as shown below.
2
###  
On the documentation page that opens, save the JSON version by right-clicking the link at the top and saving it.
You\'ll want to save separate files for each of the API groups that you want to use in the AI builder.
3
###  
Import the documentation into your AI of choice, and start building!
Here\'s a quick demo of us importing some API documentation into ChatGPT, and getting a fully functional app returned.
<div>
</div>
Please note that this video does not contain any audio, and is not intended to be a full tutorial; only a quick demonstration.
</div>
Best Practices and Tips
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Start with a clear objective**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Understand the scope of what you want the end result to look like. Try to keep in mind what a successful MVP (minimum viable product) or version 1 would require, and use that to guide the AI builder.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Use versioning**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Store your app\'s code on Github and use versioning to ensure that you can always roll back, and that it\'s easier to start new conversations if necessary with other AI platforms. Here\'s a great tutorial from FreeCodeCamp.
        :::
    :::
Last updated 2 months ago
Was this helpful?