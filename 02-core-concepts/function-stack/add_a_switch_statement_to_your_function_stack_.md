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
title: Add a Switch statement to your function stack.
---

# Add a Switch statement to your function stack.

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
    Using Switch Case
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Functions
3.  Data Manipulation
Switch 
======
**Quick Summary**
Switch Case is similar to a conditional statement, but it\'s designed to only check a single value for matches. Where a conditional is great for things like \"If the user joined before 2020 and is also a subscriber\", Switch Case is more efficient and ideal for simple scenarios like \"If the color is red, blue, green, brown, yellow, or orange\", when you want each of those options to have different paths.
Conditional vs Switch --- which one should you use?
When deciding between using an If/Then statement and a Switch statement, it\'s important to consider the complexity and clarity of the logic you\'re implementing. An If/Then statement is ideal for situations where you have several conditions that require different actions. It provides straightforward logic for evaluating true or false scenarios.
On the other hand, a Switch statement is better suited for cases with multiple possible values for a single variable. It makes your function stacks cleaner and more organized by avoiding deep nesting of conditions when the logic involves fixed values. Use If/Then for more advanced conditions and Switch for handling multiple specific scenarios with more concise readability.
Using Switch Case
<div>
1
###  
Add a Switch statement to your function stack.
Switch is located under Data Manipulation.
2
###  
Set the value that Switch should be checking.
You can hard code a value here, or specify a variable or input.
3
###  
Set your \'default\' functions, if desired.
The **Default** section of Switch will run if:
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    No matches are found
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    You chose to not break out of Switch after a match is found
    :::
This is a good spot to insert any \"catch-all\" situations where you want a standard behavior for unaccounted possibilities.
4
###  
Click []to define a behavior based on a specific value.
When adding a new **case**, you\'ll be asked to provide the value that determines if this case will run.
You can also choose to either stop the Switch Case statement after the match is found, or execute the functions under Default after matching.
5
###  
Add functions to your case(s)
Click []under your cases to add functions to them, or drag and drop functions inside of them. Now, when your Switch function detects that case in the value you specified in step 2, it will execute those functions.
</div>
Last updated 5 months ago
Was this helpful?