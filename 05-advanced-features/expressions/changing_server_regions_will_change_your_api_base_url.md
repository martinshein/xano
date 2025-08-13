---
category: expressions
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Changing server regions will change your API base URL
---

# Changing server regions will change your API base URL

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'change-server-region'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Change Server Region \| Xano Documentation'
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
    Before You Proceed
Was this helpful?
Copy
1.  Xano Features
2.  Instance Settings
Change Server Region 
====================
Xano\'s paid plans allows you to choose your server region. At the time of this page was published, server regions include:
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Australia (Sydney)
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Belgium
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Brazil (São Paulo)
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Canada (Montreal)
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    France (Paris)
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    Germany (Frankfurt)
    :::
7.  ::: 
    ::: 
    :::
    :::
    ::: 
    India (Mumbai)
    :::
8.  ::: 
    ::: 
    :::
    :::
    ::: 
    Indonesia (Jakarta)
    :::
9.  ::: 
    ::: 
    :::
    :::
    ::: 
    Japan (Tokyo)
    :::
10. ::: 
    ::: 
    :::
    :::
    ::: 
    Saudi Arabia (Dammam)
    :::
11. ::: 
    ::: 
    :::
    :::
    ::: 
    Singapore
    :::
12. ::: 
    ::: 
    :::
    :::
    ::: 
    South Korea (Seoul)
    :::
13. ::: 
    ::: 
    :::
    :::
    ::: 
    United Kingdom (London)
    :::
14. ::: 
    ::: 
    :::
    :::
    ::: 
    United States (Oregon)
    :::
From the billing section, you are able to select where you would like your server to be located.
Before You Proceed
<div>
1
###  
Changing server regions will change your API base URL
Your instance has a specific URL, such as https://abc1-def2-ghi3.xano.io/ and all of your API endpoints begin with this.
When you change regions, because you are migrating to a new server, your base URL will change.
After selecting your new server region, you will be given an option to beging the migration, so you have time to update anything necessary before proceeding.
**Be sure to update any external connections with the new URL prior to initiating the migration.**
2
###  
Unpublished drafts will NOT be migrated
Make sure to publish anything you want to save before proceeding.
</div>
How to Change Server Region
<div>
1
###  
Click your name []in the lower-left corner and choose Billing
2
###  
Click []
3
###  
Select your existing plan to ensure no billing changes are made. You can also choose to upgrade your plan at this time, if you\'d like.
Changing server regions is **free**, but because your subscription restarts when making this change, you will be billed at checkout for the cost of your plan, minus any unused time on your current subscription period.
4
###  
Scroll down to Server Region and select where you\'d like your server to be hosted.
Use the dropdown to select your region of choice.
5
###  
Proceed through checkout.
6
###  
After checkout, review your new server URL and update any external connections.
7
###  
Once you\'re ready, proceed with the migration by clicking the button shown below.
</div>
Last updated 6 months ago
Was this helpful?