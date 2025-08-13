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
title: Click
---

# Click

[🛠️]The Visual Builder
    :::
        ::: 
            ::: 
            -   Swagger (OpenAPI
                Documentation)
            :::
            ::: 
            -   Async
                Functions
            :::
        -   Background Tasks
        -   Triggers
        -   Middleware
        -   Configuring
            Expressions
        -   Working with Data
        :::
        ::: 
        -   AI Tools
            ::: 
                ::: 
                -   External Filtering
                    Examples
                :::
            -   Get
                Record
            -   Add
                Record
            -   Edit
                Record
            -   Add or Edit
                Record
            -   Patch
                Record
            -   Delete
                Record
            -   Bulk
                Operations
            -   Database
                Transaction
            -   External Database
                Query
            -   Direct Database
                Query
            -   Get Database
                Schema
            :::
            ::: 
            -   Create
                Variable
            -   Update
                Variable
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
            -   Realtime
                Functions
            -   External API
                Request
            -   Lambda
                Functions
            :::
        -   Data Caching
            (Redis)
        -   Custom
            Functions
        -   Utility
            Functions
        -   File
            Storage
        -   Cloud
            Services
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
        -   Response
            Caching
        :::
-   ::: 
    Testing and Debugging
    :::
-   ::: 
    The Database
    :::
        ::: 
        -   Using the Xano
            Database
        -   Field
            Types
        -   Relationships
        -   Database
            Views
        -   Export and
            Sharing
        -   Data
            Sources
        :::
        ::: 
        -   Airtable to
            Xano
        -   Supabase to
            Xano
        -   CSV Import &
            Export
        :::
        ::: 
        -   Storage
        -   Indexing
        -   Maintenance
        -   Schema
            Versioning
        :::
-   ::: 
    Build For AI
    :::
        ::: 
        -   Templates
        :::
        ::: 
        -   Connecting
            Clients
        -   MCP
            Functions
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
        -   Separating User
            Data
        -   Restricting Access
            (RBAC)
        -   OAuth
            (SSO)
        :::
-   ::: 
    Xano Features
    :::
        ::: 
        -   Release Track
            Preferences
        -   Static IP
            (Outgoing)
        -   Change Server
            Region
        -   Direct Database
            Connector
        -   Backup and
            Restore
        -   Security
            Policy
        :::
        ::: 
        -   Audit
            Logs
        :::
        ::: 
        -   Xano
            Link
        -   Developer API
            (Deprecated)
        :::
        ::: 
        -   Master Metadata
            API
        -   Tables and
            Schema
        -   Content
        -   Search
        -   File
        -   Request
            History
        -   Workspace Import and
            Export
        -   Token Scopes
            Reference
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
        -   Agency
            Dashboard
        -   Client
            Invite
        -   Transfer
            Ownership
        -   Agency
            Profile
        -   Commission
        -   Private
            Marketplace
        :::
-   ::: 
    Custom Plans (Enterprise)
    :::
        ::: 
            ::: 
                ::: 
                -   Choosing a
                    Model
                :::
            :::
        -   Tenant
            Center
        -   Compliance
            Center
        -   Security
            Policy
        -   Instance
            Activity
        -   Deployment
        -   RBAC (Role-based Access
            Control)
        -   Xano
            Link
        -   Resource
            Management
        :::
-   ::: 
    Your Xano Account
    :::
-   ::: 
    Troubleshooting & Support
    :::
        ::: 
        -   When a single workflow feels
            slow
        -   When everything feels
            slow
        -   RAM
            Usage
        -   Function Stack
            Performance
        :::
        ::: 
        -   Granting
            Access
        -   Community Code of
            Conduct
        -   Community Content Modification
            Policy
        -   Reporting Potential Bugs and
            Issues
        :::
-   ::: 
    Special Pricing
    :::
-   ::: 
    Security
    :::
-   ::: 
    :::
    Building and Using Background
    Tasks
-   Click in the left-hand menu to access your background
    tasks.
-   Click to create a new background
    task.
Was this helpful?
Copy
1.  [[🛠️]The Visual
    Builder](../building-with-visual-development.html)
2.  Building with Visual Development
Background Tasks 
================
Build and run workflows on a set schedule
Quick Summary
Background tasks, or sometimes referred to as \"cron jobs\" are
workflows that run on a set schedule. Background tasks are great for
things like sending out marketing emails, report generation, analytics,
and large data processing jobs.
Background Tasks are available on our **Starter plan** and higher.
Building and Using Background Tasks
<div>
1
###  
Click
[] in the left-hand menu to access your
background tasks.
2
###  
Click
[] to create a new background task.
Fill in your desired options, such as **name**, **description**,
**tags**, **request
history**, and the preferred **data
source**.
3
###  
Build your background task.
Background tasks are a little different from APIs and custom functions,
in that they do not have inputs or deliver a response. Tasks have two
sections that require your attention.
###  
🔄 Function stack
This is where all of the magic happens. All of the business logic that
is performed lives here.
As you add functions to your function stack, it will suggest next steps
based on most popular user activity.
####  
📅 Schedule
The schedule determines when your background task runs, and how often.
If a new run is scheduled to begin before the previous has completed,
the currently due run will be skipped.
4
###  
Set your task to active.
Once you have built your function stack and your task schedule, click
Enable Task to set it as active, and publish your changes.
</div>
Last updated 1 month ago
Was this helpful?