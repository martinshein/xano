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
title: Merging Database Tables
---

# Merging Database Tables

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'xano-link'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Xano Link \| Xano Documentation'
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
Xano Link provides the Instance owner an interface where they can publish one source workspace to many client workspaces. Changes or updates can be made to the source workspace and published to many client workspaces. This is a manual process so it requires keeping track of which client workspaces need to be updated. It is recommended to use naming conventions for the workspaces to help keep track (e.g. product\_name:source, product\_name:user\_id).
Xano Link can be accessed from the settings of the source workspace.
Accessing Xano Link
Once inside, you can choose to Link APIs, functions, addons, and database tables. Take note of the **Select All/None** and **Auto include dependencies** options to assist in ensuring that the Link only merges the data you want. You also have the option to include records from the selected database tables, or only merge the schema.
**Select All/None** allows you to quickly bulk select or de-select items.
**Auto include dependencies** will scan and auto-include in the Link any items that are dependent on what you have already selected. For example, if you are choosing API endpoints that include custom functions, the functions will also be merged without you having to select them manually.
###  
Merging Database Tables
Choosing Database Tables and Records
You have the option to choose specific tables and records to merge when using Xano Link. Click on the record count to select specifically which records you want to merge, or select all.
Choosing records to merge
When you use Xano Link to merge database tables, and the destination workspace already has that table created, you will need to change the GUID of the destination table to match, otherwise you will have duplicate tables. The steps below will outline how to change the GUID. Please proceed with caution as you change these advanced settings.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Head to the **source table**, click the three dots in the top-right, and choose Security.
    :::
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click \"Show Advanced Settings\" and copy the GUID that is shown in the box.
    :::
Copying the GUID from the source table
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    After you\'ve copied the GUID, head to the **destination table** in the new workspace, and replace the GUID with the copied value from the source table and save your changes.
    :::
Once you\'re ready to publish an update select which client workspaces the update should be pushed to. You also have the option to merge the newly created branch with whatever branch in the target workspace is set to live, and / or set the newly created branch as the live branch.
**Merge New Branch with existing Live Branch** will merge the newly created branch with the branch in the destination workspace that is currently set to live.
**Set New Branch Live** will set the newly created branch as the live branch immediately.
####  
Customization
Customization on a per-client basis is possible by using **additional** tables or APIs that are independent of the source workspace. Customization to the schema from the source workspace would get overwritten with any new updates.
###  
Compare Differences
Xano Link allows you to view and compare differences before merging a branch from the source workspace into a branch from the destination workspace.
Be sure to select the Merge New Branch option and the destination workspace before selecting \"view.
By selecting view, you can see which items contain differences.
Changed items.
By selecting \"changes\" next to an item, you can see a snapshot of the differences.
In the above example there are six changes:
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Created\_at input deleted
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Name input edited
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Category input edited
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Value input edited
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    API Request function added
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    Create Variable function added
    :::
Last updated 1 month ago
Was this helpful?