---
category: function-stack
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'Function: Custom Functions'
---

# Function: Custom Functions

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
    What are custom functions?
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Functions
Custom Functions 
================
What are custom functions?
Custom functions are pieces of reusable logic that you can insert into other function stacks. This is most useful when you have a set of steps that remain the same, but need to be executed in multiple places. Placing those steps inside of a custom function allows you to quickly use those steps in other function stacks, while only needing to maintain them in one place.
###  
Using Custom Functions
<div>
1
###  
From the left-side navigation, click [] to access the Library section, and choose Functions from the submenu that appears.
2
###  
To create a custom function, click []
Building a custom function is just like building an API. Refer to that documentation for specific instructions on building the function stack.
3
###  
[] your changes
You can Publish the custom function to ensure that every place it is called uses the same version.
**Hint**
When using Run & Debug, you have the option of running draft versions of functions as well, so you don\'t have to publish changes until you are ready.
4
###  
Insert the custom function any place you need to use it.
In the functions panel, you\'ll see an option labeled Custom Functions, shown below. Just click it to see a list of your custom functions and add them to other function stacks.
5
###  
When you make changes to the custom function, the changes populate across everywhere it is used.
</div>
------------------------------------------------------------------------
Async Execution
Once you\'ve built your custom function and added it to another function stack, you have the option of running the function **asynchronously**. This just means that the functions will be queued for execution, and the rest of your function stack will continue to execute right away.
<div>
</div>
Asynchronous functions will utilize your background task resources (unless you are on an Enterprise plan), so it\'s important to manage expectations when it comes to execution speed. It would be most appropriate to use asynchronous functions when you need to trigger an operation as part of a larger function stack, but do not need to reference the output in the same stack.
To enable asynchronous execution, right-click on the custom function in your function stack, and choose **Async Settings**.
[]
In the panel that opens, choose your desired execution type.
[]
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Synchronous** means that the function stack will wait for the custom function to execute before continuing. The custom function will output the result to the defined variable. This is the standard behavior that has always existed for custom functions.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Async** means that the functions will be queued for execution using your background task resources. The function\'s output variable will be populated with a unique identifier for the queued excecution.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Async (dedicated)** is available for Enterprise plans and gives you a method of specificity around the resources used to execute the custom function.
    :::
When using async functions, the function request history will still populate, so you can review the requests once they have finished executing. Each request will be labeled with the execution method.
[]
####  
Async Function Await
In scenarios where you want to use the output of your async functions later in the function stack, you can utilize the **Async Function Await** function, which accepts the UUIDs returned when an async function is executed.
You can provide an array of IDs to get the output of, and specify how long you\'d like to wait for those functions to finish executing in seconds using the timeout parameter.
[]
Last updated 7 months ago
Was this helpful?