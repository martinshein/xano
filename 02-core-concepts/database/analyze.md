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
title: Analyze
---

# Analyze

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: maintenance
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Maintenance \| Xano Documentation'
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
    How do I perform maintenance on my Xano instance?
Was this helpful?
Copy
1.  The Database
2.  Database Performance and Maintenance
Maintenance 
===========
How do I perform maintenance on my Xano instance?
All paid plans include access to the Maintenance panel, accessible via your instance settings. There are different maintenance operations you can perform to help troubleshoot issues you might be having in Xano, or to manage your database storage.
Accessing the Maintenance Panel
Head to your instance settings from your instance selection screen and choose Maintenance.
From the next panel that appears, you can choose between several maintenance options.
**Clear Internal Cache**
This maintenance action clears the internal cache within the instance. This does not affect any drafts or redis storage. You should use this option first if you are experiencing any or multiple of the following symptoms:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Slow loading in Xano or function stacks not loading
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    APIs not responding or responding with strange errors such as \"invalid app\"
    :::
**Database Maintenance**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Analyze**
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Vacuum**
    :::
Database maintenance is automatically done daily but Xano does offer ways to manually run PostgreSQL analyze and vacuum commands through the Instance Maintenance panel.
PostgreSQL\'s VACUUM and ANALYZE functions are essential maintenance tasks for optimizing database performance.
Together, VACUUM and ANALYZE help keep the database running smoothly by managing storage and providing accurate statistics for optimal query planning and execution.
###  
Analyze
ANALYZE gathers statistics about the data distribution in tables, enabling the query optimizer to generate efficient execution plans. It updates the query planner\'s knowledge of the data, improving query performance by enabling better index selection and join strategies.
###  
Vacuum
VACUUM reclaims storage space by removing obsolete or dead data that remains after updates or deletions. It helps prevent performance degradation caused by fragmentation and frees up disk space.
####  
Partial VACUUM
This command analyzes and cleans up the database, but it does not necessarily reclaim all available disk space. It marks the space previously occupied by deleted rows as reusable for future inserts and updates. VACUUM also updates statistics used by the query planner to improve query performance.
####  
Full VACUUM
**Full VACUUM requires at least 50% free storage space before continuing. Proceeding with a Full VACUUM without enough free storage can fail or cause instance downtime.**
This command performs a more thorough cleanup compared to partial. It reclaims all available disk space by rewriting the entire table and indexes from scratch. This process can be more resource-intensive and time-consuming, as it involves copying the data to a new file and rebuilding the indexes. Full VACUUM can significantly improve disk space utilization but **may cause downtime** for larger tables.
Server Maintenance
Your Xano instance is separated into \'pods\' that are all responsible for their own functions. Use the guide here to determine what should be restarted and when. You can also use this panel to view the status of your backend. Use the [] button to check the progress of any restarts performed.
If you aren\'t sure which option to choose, please reach out to support. None of these options are typically destructive in any capacity, but we can provide specific guidance based on the behaviors you are observing.
###  
Backend
This is a full reboot of your Xano instance. A good, quick catch-all for any issues you might be seeing. This option is also appropriate for stopping things like infinite loops.
###  
Database
If you are experiencing issues with your database, or want to halt an ongoing database transaction, such as an import or bulk operation.
###  
Frontend
If you are experiencing issues with the Xano UI, you can try restarting it from here.
###  
Node
This pod is responsible for some backend operations and Lambda functions.
###  
Realtime
This pod is responsible for our realtime functionality
###  
Redis
This pod is responsible for caching both to facilitate Xano functionality, and caching functions inside of your function stacks. Restarting this pod can assist with various issues related to performance and downtime if the cache is full and unable to clear automatically. If you believe you are experiencing issues related to Redis, please reach out to support.
###  
Task
This pod is responsible for running your background tasks. You can restart this pod if you\'d like to halt any ongoing tasks.
Please note that restarting your tasks will not impact the schedule of those tasks --- they will continue to execute as defined. Make sure to disable any tasks either before or after the restart if you want to make sure they do not run again until you are ready.
Async Function Maintenance
If you are utilizing asynchronous functions and are experiencing issues such as your functions not completing execution, you can clear the asynchronous queue from this panel.
Use the [] option to clear any queued functions from memory.
Request History
Use this option to manually clear your request history and free up space in your database.
Request history is typically purged automatically, but you can clear it anytime from here if you find it necessary.
Make sure to define branch defaults for your request history so you\'re only logging what you need.
From this panel, we have two options: **database storage** and **cache storage**.
###  
Database Storage for Request History
This is the actual database table that contains all of your request history, and counts against your available database storage in your instance. You can click on this option to delete one portion or all of your request history at any time.
Use the **Force** option to halt any running processes to ensure the data can be cleared \-- please note however that this may result in a little bit of downtime as the server halts running processes.
###  
Cache Storage for Request History
As requests are logged, they are not immediately saved to the database. For a short period of time, they are held in a cache, and dumped into the database at fast, regular intervals. In some cases, such as during excessive traffic spikes, you may find that clearing the request cache before the items are added to the database can help the recovery process.
Please note that when items are cleared from the cache, they will not be logged in the history database.
Last updated 5 months ago
Was this helpful?