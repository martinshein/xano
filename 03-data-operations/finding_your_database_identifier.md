---
category: 03-data-operations
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Finding your database identifier
---

# Finding your database identifier

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
    Finding your database identifier
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Functions
3.  Database Requests
Direct Database Query 
=====================
The Direct Database Query function is available starting on the **upgraded** (non-Legacy) Launch or Scale plans. If you have any questions, please reach out to support.
To access the Direct Database Query function, add a new function to your function stack, choose Database Operations, and then Direct Database Query.
From the Direct Database Query panel, you can provide the following:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Code** - This is the query you would like to perform
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Statement Args** - If you specify arguments using **?** in your code, you can use this section to sequentially fill in those arguments with other data, such as variables or inputs previously defined in your function stack
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Response Type** - Return either a single item, or a list of items
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Output Variable** - The name of the variable that will contain the result of the query
    :::
###  
Finding your database identifier
The database identifier can be found by combining the workspace ID and database table ID with \'mvpw\'.
For example:
If workspace ID = 1 and ID = 3: `mvpw1_3`
If workspace ID = 500 and table ID = 3913: `mvpw500_3913`
Using the mvpw selector will return two columns: id and xdo, with xdo containing each record\'s content. For SELECT statements where you want to return specific columns, use \'x\' instead.
You can also use an **x identifier**, such as x1\_3, to return a more readable view of the data. Please note, however, that these views do not always have function parity with working with the mvpw\_ version of your tables (such as when performing inserts).
Using **x\_** is typically best when just performing queries.
Where to find your table ID and workspace ID
Direct Database Query allows you to query tables across your Instance. For example, if you are in workspace 2, you can query a table from workspace 1 using the above syntax. Please do so carefully to not misuse sensitive data in a query.
###  
Using Custom Aliases
You can leverage custom view aliases to make direct database queries easier to write, and more readable, based on exactly the data that you need.
Head to your database table, and create a custom view. When creating your custom view, you can provide a **Database View Alias**, which you can use in your Direct Database Query statement.
In the screenshot below, we\'ve created a database view to filter people named David in our people table. When saving the view, we\'re providing an alias called \'david\'.
Once this view is saved, we can utilize it in a Direct Database Query function to retrieve the data from that view. The view is listed when using the Direct Query wizard, or you can type it manually if you are writing a query from scratch as `SELECT * from "view_name";`
###  
Test Data
Assuming our data source is named \'test\', mvpw599\_2377 would become mvpw599\_test\_2377. You can replace \'test\' in this example with the name of your data source.
Direct Database Query does not respond to the selection of your data source in Xano or the data source specified in any external requests. You need to specifically state the test data source in the function. It is not possible at this time to dynamically modify the table selector.
###  
Statement Arguments
Statement arguments enable dynamic values in your queries. Statement arguments are designed to come from variables, inputs, or environment variables. A `?` in the query will identify where a statement argument should be placed; they will be placed in sequential order.
Statement arguments are escaped with single quotes by default.
In situations where you want to escape the argument value with double quotes, use `?:alias`.
To insert an argument value with no quotes, such as a table name, use `?:raw`.
Argument Type
Query Syntax
Result
Default
`?`
\'example\'
Alias
`?:alias`
\"example\"
Raw
`?:raw`
example
####  
Example:
In the following query, there are two statement arguments. The input `search` will be placed at the first `?` and the variable `var_1` will be placed at the second `?`.
Arguments can not, at this time, be anything other than single values. Arguments can not also replace functions; they can only serve as query values at this time.
PREVENTING SQL INJECTION ATTACKS
Xano offers some filters to help ensure that any dynamic / user input is not parsed in a way that might harm your database or cause other unintended consequences.
Make sure to process your inputs **before** they are used in any SQL queries with the appropriate filter.
These filters are sql\_alias and sql\_esc
###  
SQL Query Wizard
The SQL Query Wizard generates simple SQL queries. **It is not designed to support complex statements or joins but basic statements** to help get you started.
Open the Wizard Panel
####  
Step 1: Choose the Database Table to Query
####  
Step 2: Choose the field
####  
Step 3: Choose an operator and value.
Choose an operator for the query and add a value. Optionally include multiple conditions with AND or OR statements.
####  
Step 4: Select the columns to include in the query response.
The Wizard will process the settings and generate a SQL query in the code editor.
The result returns a list from merchant where desc = Pizza.
###  
What\'s the difference between Direct Database Query and Direct Database Access?
Direct Database Access is a premium add-on that allows you to connect directly to your Xano PostgreSQL database using an external tool. If you would like to leverage something outside of Xano to manage your database, direct database access is the feature you\'re looking for.
The Direct Database Query function in Xano is available if you want to simply run SQL queries from inside Xano.
Using the AI SQL Assistant
<div>
1
###  
When using the Direct Database Query function, click [] to access the AI SQL assistant.
The assistant can help you write queries against your Xano database.
2
###  
Provide the assistant with the query you would like it to build.
3
###  
Once complete, the assistant will present you with the query, along with an explanation of how it works and some records that satisfy the query.
4
###  
If the query returns the expected results, click [Update SQL]. Otherwise, you can ask the assistant to make any desired modifications or fixes.
You can also make your own modifications to the query, such as adding ? characters to represent dynamic values.
</div>
Last updated 4 months ago
Was this helpful?