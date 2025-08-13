---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'Function: Async Functions'
---

# Function: Async Functions

[](../../../index.html)
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
            -   Swagger (OpenAPI
                Documentation)
            :::
            ::: 
            -   Async Functions
            :::
        -   Background Tasks
        -   Triggers
        -   Middleware
        -   Configuring
            Expressions
        -   Working with
            Data
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
    What are async functions?
-   When should I use async
    functions?
-   Insert a custom function into your function
    stack.
-   Click on the function to change the execution
    mode.
-   If necessary, retrieve the output of the async
    function.
Was this helpful?
Copy
1.  [[🛠️]The Visual
    Builder](../../building-with-visual-development.html)
2.  Building with Visual Development
3.  Custom
    Functions
Async Functions 
===============
Use async functions to ensure that your custom functions execute exactly
as you intend
What are async functions?
When working with custom functions in Xano, you can choose to have them
execute asynchronously. An async function works like a background
task, allowing your main process to continue without waiting
for the custom function to finish.
When should I use async functions?
Asynchronous execution can be particularly beneficial in scenarios where
you don\'t want certain tasks to hold up the entire process. For
instance, if you\'re running a complex data fetch or a time-consuming
operation, doing it asynchronously means your main application or
interface remains responsive to user inputs while the background
operation continues independently. This can enhance user experience by
reducing wait times.
Here are a few examples of when to use async functions:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Loading Data:** When fetching data from a server, such as pulling
    in user information or loading a list of products, async functions
    allow the page to display its initial content quickly without
    waiting for the entire data request to complete.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **File Uploads:** Starting a file upload process without freezing
    the interface lets users continue interacting with the application
    while the file is being processed.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Notification Systems:** Sending notifications through email or
    messaging services asynchronously ensures that users continue their
    tasks without interruption while the messages are sent in the
    background.
    :::
Enabling Async Execution
<div>
1
###  
Insert a custom function into your function stack.
If you haven\'t built any custom functions yet, you can review our
documentation on them
here.
2
###  
Click
[]on the function to change the execution
mode.
3
###  
If necessary, retrieve the output of the async function.
If a function is set to async, it will return an ID that represents that
execution, similar to the value shown below.
Copy
``` 
6f10cc09-d3e0-4ead-9a98-a0bc66bbe673
```
You can use the **Async Function Await** function to retrieve the output
of the function once execution completes. Just provide it with an array
of the ID(s) returned when the function runs.
</div>
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
6f10cc09-d3e0-4ead-9a98-a0bc66bbe673

```

