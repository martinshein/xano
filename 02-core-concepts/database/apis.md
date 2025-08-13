---
category: database
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: APIs
---

# APIs

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'schema-versioning'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Schema Versioning \| Xano Documentation'
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
    How to open schema version history
Was this helpful?
Copy
1.  The Database
2.  Database Performance and Maintenance
Schema Versioning 
=================
<div>
</div>
You can leverage versioning to help you solve problems, see differences in your work, test ideas, and easily revert back to previous versions. It also tracks who from your team made a change, and when the change was made.
Schema versioning is for database tables, API groups, API endpoints, functions, Addons, and background tasks. It allows you to easily roll back to a previous version in case you make a mistake.
Schema Versioning is available on our **Starter** plan and higher.
**How to open schema version history**
Open Version History by selecting Versions from the menu icon.
View your active (current) version, select from a previous one to roll-back, and see who made a change and when.
Version History captures which is your active version, a history of previous versions with data on when the change was made and by who, and the ability to select a previous one.
Version history will keep track of changes you make anywhere on a query, whether you make a change to a function or a filter. For API endpoints and functions, version history keeps a count of how many inputs, functions, and results were included in each version.
Counts of each versions\' inputs, functions, and results allow you to determine which version you may wish to roll-back to.
Tasks will show how many functions and schedules there were for each version.
Version history of a background task.
Addons will show a count of how many inputs each version had.
Version history of an Addon.
Compare Differences
When selecting a previous version, you can view a screenshot of the version and the differences compared to the active version. This gives you full context of the different versions to see exactly what changes were made and whether or not you indeed want to revert to the previous version.
###  
APIs
For example, here is the live version of an API endpoint:
Example of a live version of a function stack.
After selecting Version History, we can see the different versions with some metadata and publish notes about each:
The available versions of the API endpoint.
By clicking on a version, in this example we selected version \#2, a modal opens showing the differences present in the current live version \#4 as compared to the state of version \#2.
The difference comparison tells us a few things.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The live version (indicated at the top) and when it was created.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The email of who created the version.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    What differences the live version has compared to the old version selected.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    When the old version was created.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Indications of what\'s been changed from the old version compared to the state of things in the live version.
    :::
Lastly, you can easily navigate through the screenshots of the different old versions.
Navigate through the previous versions.
###  
Database
Difference comparison in schema versioning is also available on the database. In addition to information about the version number, created at time, and creator. Difference comparison on the database will include differences in:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Schema (columns)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Indexes
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    View
    :::
An example of comparing version differences of a database table.
Last updated 1 month ago
Was this helpful?