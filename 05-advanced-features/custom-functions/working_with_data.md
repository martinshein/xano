---
category: custom-functions
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Working With Data
---

# Working With Data

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
    Understanding Working with Data
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Building with Visual Development
Working with Data 
=================
Understanding Working with Data
When we talk about working with data in Xano, we are referring to anything that touches a piece of data in your workflows --- whether it is an API, custom function, task, or anything else. Data will typically always be passing through these workflows, and it\'s important to understand the various ways you can access and interact with this data.
Database vs Variables
The **database** is used to store information that you will need to recall again later, and across workflows, such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    User accounts
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Product and order information
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Blog posts or comments
    :::
**Variables** are used inside of individual workflows to store information temporarily that you only need to finish the set of functions being executed, such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The current date / time
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Data from a database that needs temporary manipulation or transformation, such as combining a first and last name or calculating a discount
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The output of individual functions in a function stack, like getting a record from a database table
    :::
Data in Functions
Most functions that you can add to a function stack will have some kind of output available. The output of these functions are stored in a **variable**.
In the screenshot shown below, we are using a get record function to retrieve a record from our `author` table. On the right side of that function, take note of return as [**author1**]. This is the variable that the record we retrieve is stored in, and what we will use to get that data in subsequent functions.
When we add another function, we can reference [**author1**] as shown below.
Data in Filters
Filters are like mini-functions that can ride alongside other functions in your function stack. They are used to perform a wide array of tasks against a piece of data.
Our current function stack does nothing but retrieve a record from our `author` table.
Let\'s transform this data by changing the author\'s name to uppercase. The simplest of data transformation happens in an **Update Variable** function. Try it for yourself below.
Changing Variable Names
As you build your function stacks, you\'ll want to ensure you are naming variables appropriately, so you can understand what they contain.
When adding a function, you\'ll usually have the option to set the variable name.
If you need to change the variable name after you\'ve already referenced the data elsewhere, Xano will ask you if you want to update the references to that variable. In the below screenshot, after changing the [**author1**] variable name, Xano lets us know that the variable is already referenced in an **Update Variable** step, and in our response. Click []to automatically change all of these to reflect the new variable, or click [Skip] to leave them the same. If you aren\'t sure which option to choose, more often than not, you\'ll want to update the references.
Last updated 6 months ago
Was this helpful?