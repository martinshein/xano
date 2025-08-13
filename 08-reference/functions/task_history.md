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
title: Task History
---

# Task History

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'request-history'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Request History \| Xano Documentation'
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
    API Request History
Was this helpful?
Copy
1.  Maintenance, Monitoring, and Logging
Request History 
===============
API Request History
From the dashboard, easily view the high-level statistics of the API request history from your entire Workspace. You can toggle between your database and top API requests to see which of your API endpoints are being hit the most. To the right, visualize your API request history with a graph displaying the statistics of the past 24 hours. Select \'View Request Details\' to see a detailed view and history of each API call made in your Workspace.
You can expand each individual call to review detailed information including inputs, response and request headers, and the output. You can even drill-down on a per-user basis to see the activity of each user in your application. Furthermore, you can view failed API calls here in order to help debug what went wrong. Finally, you can use these details to understand Webhook payloads to make it easier to build API endpoints that receive Webhooks.
You can also choose whether to see the request history for the specific branch you have active, or all branches, and download your request history as a CSV. If you would like to access your request history via API, you can do so using our Metadata API.
The Request History panel allows you to filter by the following metrics:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Time** - when the request was received
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Duration** - how long the request took
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Status** - if there was a standard code returned, filter by that status
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Input / Output Size** - how much data was sent to or sent from the request
    :::
API and Custom Function request history panels will also show the average runtime of all of your requests, giving you quick visibility into the state of your application.
It doesn\'t stop at the entire Workspace level. From each API group, you can see the detailed history of the entire group. And from each API endpoint, you can see the history of the individual endpoint.
Function Request History
Custom Functions are similar to API endpoints in Xano, in the sense that they have the same No-Code API builder UI. However, custom functions can only be called by other internal function stacks in Xano whether that\'s an API, other function, or background task.
Functions also have a request history for any time a function is part of a live API request.
First, open the request history of a function from the top right menu icon.
Open request history for a function
Once opened, you can see all the requests from the past 24 hours.
At the top, you can filter the requests by the time they occurred up until and by the duration of the how long the function took to run.
The duration filter can be useful for identifying potential performance issues.
You can click on any of the requests to see the specific details of the inputs, output (response), and the function stack run time information.
Granular information on the function request.
###  
Task History
Task history behaves a little differently than APIs and functions. Tasks maintain a history over 7 days instead of 24 hours. Tasks also do not deliver responses, so no response data will be recorded, but you will still be able to review the statement log, execution status, and the timing details.
###  
Middleware History
Middleware history will behave the same as API and function history.
###  
Triggers History
Request history for triggers behaves most similar to a task, as there is no output returned with a trigger. You can, however, review the inputs (new, old, action, datasource) and the timing details for each step.
Managing Request History
Branch Defaults
> These are default settings related to what is logged in your Request History
In your workspace settings, you can manage the request history for your entire workspace in the Branch Defaults panel.
From this panel, we can define the request history defaults for each object type (query, function, task, middleware, trigger) that maintains history.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Enable / Disable** - Performs the selected action on the object type
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Function Statement Limit** - The number of statements to record for each object type. You can choose between:
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        No statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        100 statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        1,000 statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        10,000 statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Store all statements
        :::
    :::
Please note that request history utilizes your Database (SSD) storage. It is important to consider this when determining how many statements can be stored, or if they need to be stored at all.
####  
Inheriting Settings
In each individual API, function, task, middleware, or trigger\'s settings, you can also control the request history for that object specifically.
By default, these will be set to **inherit**, which means it will obey the branch defaults. Otherwise, you can adjust this for specific objects as necessary.
Clearing Request History
From your Instance settings, you have the option to manually clear your request history at any time.
From this panel, we have two options: **database storage** and **cache storage**.
###  
Database Storage for Request History
This is the actual database table that contains all of your request history, and counts against your available database storage in your instance. You can click on this option to delete one portion or all of your request history at any time.
Use the **Force** option to halt any running processes to ensure the data can be cleared \-- please note however that this may result in a little bit of downtime as the server halts running processes.
###  
Cache Storage for Request History
As requests are logged, they are not immediately saved to the database. For a short period of time, they are held in a cache, and dumped into the database at fast, regular intervals. In some cases, such as during excessive traffic spikes, you may find that clearing the request cache before the items are added to the database can help the recovery process.
Please note that when items are cleared from the cache, they will not be logged in the history database.
Last updated 3 months ago
Was this helpful?