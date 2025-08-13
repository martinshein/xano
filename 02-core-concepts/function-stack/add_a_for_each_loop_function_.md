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
title: Add a For Each loop function.
---

# Add a For Each loop function.

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
    For Each Loop
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Functions
3.  Data Manipulation
Loops 
=====
Loops are used to iterate over a set of items, or run a set of steps a certain number of times.
There are a few different kinds of loops that you can use in Xano.
For Each Loop
A For Each loop is designed to iterate over a list of items, such as all records returned by a database query, or items returned from an external API request.
If you are iterating through a list of database records, set the return type in the query to **stream** to enable super memory-efficient looping. This is especially helpful the larger the list is.
<div>
1
###  
Add a For Each loop function.
2
###  
Specify the list that the loop will iterate through.
Select the variable that contains your list of items.
[]
3
###  
Define the variable that will hold each item as the loop runs.
By default, this is called [**item**], but you can name it whatever you\'d like. Use this variable inside of your loop.
[]
4
###  
Add functions inside of your loop.
Make sure these steps target the right variable.
[]
</div>
For Loop
A For loop is used to repeat a stack of steps a certain number of times.
Refer to the For Each loop instructions to see how it works. The only difference between a For and a For Each loop is\...
-   ::: 
    ::: 
    :::
    :::
    ::: 
    In a For loop, you need to specify the number of times the loop runs.
    []
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Because we aren\'t building the loop against a list of items directly, we don\'t have a variable that houses the individual item. Instead, Xano keeps track of which iteration is running inside of an **index variable**, which you can set here.
    []
    :::
While Loop
A While loop is used to repeat a set of steps infinitely as long as the condition(s) defined evaluate as true.
Proceed with caution when using While loops, as they can not be easily stopped once started.
To ensure that your loop works as intended, make sure to **stop the loop with a Break statement** while testing and debugging.
If you are concerned that you have entered an infinite loop and want to break it, learn how to restart your instance here.
You\'ll use the expression builder to define the conditions that tell the loop whether or not it should continue.
###  
Using the Expression Builder
Each conditional has four different components.
**Conditional Type**
The conditional type determines how this condition is weighted in the final return. You can choose between **AND** and **OR. AND** conditionals require the present conditional and any others before it to be satisfied, such as \"where the date is before today **AND** the user is an admin\". **OR** conditionals do not require any other conditionals to be satisfied, such as \"if the user is an admin **OR** if the user is a manager\".
**Left Value**
This is the first value you\'re using in the conditional. In a database query, this is usually going to be a column that you want to check against.
**Operators**
Please note that operators may differ based on where you are building the expression. Database queries will have different operators available than regular conditional statements. Learn More
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Equals (==)** - an exact match
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Not Equals (!=)** - does not equal
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Equals with type matching (===)** - an exact value match and an exact type match
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Ex. Variable **var\_1** has a value of 123, with a type of text. You set up a conditional statement to check if **var\_1 === 123**, but your value in the conditional statement is of type integer. This would return false, because the types do not match.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Not equals with type matching (!==)** - does not equal value or type, similar to ===
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Greater than (\>)** - the value on the left is greater than the value on the right
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Greater than or equals (≥)** - the value on the left is greater than or equals to the value on the right.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Less than (\<)** - the value on the left is less than the value on the right.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Less than or equals (≤)** - the value on the left is less than or equals to the value on the right.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **LIKE** - Used for comparing text. Like is case-insensitive and compares if a text string is like another text string. It can be thought of as equals for text but upper case and lower case does not matter.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **NOT LIKE** - Used for comparing text. Not Like is case-insensitive and compares if a text string is not like another. It is like not equals for text but upper case and lower case does not matter.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **INCLUDES** - Used for comparing text. Includes is a flexible operator and is case-insensitive. It is able to determine if there is a partial match in a text string.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **DOES NOT INCLUDE** - Used for comparing text. Does not include determines if a text string is not included in another text string.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **IN** - If a single value is found in an array (list). Start with the single value on the left side and the right side should contain the array.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **NOT IN** - If a single value is not found in an array (list). The single value should be on the left side and the array on the right side.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **REGEX MATCHES** - Regular Expression used for finding patterns in text.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **REGEX DOES NOT MATCH** - Regular Expression used for finding a pattern that does not match in text.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **OVERLAPS** - Used for comparing two arrays. Overlaps determines if any values in one array are present in the second array.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **DOES NOT OVERLAP** - Used for comparing two arrays. Does not overlaps determines if no values in the first array are present in the second array.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **CONTAINS** - Contains is an advanced filter used for JSON and arrays. It looks for an exact schema match.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **DOES NOT CONTAIN** - Does not contain is the opposite of contains. It determines if there is not an exact schema match.
    :::
####  
Right Value
The right value is whatever you are checking against the left value. This could be a hardcoded value, a variable, or even a database field from the same record.
Additional Loop Functions
###  
Loop: Break
Breaks the currently running loop, meaning the loop is exited and the next function will run.
###  
Loop: Continue
Immediately begins executing the next iteration of the loop. This is very useful for conditionals inside of loops that determine what happens to the item being iterated through.
###  
For Each Loop: Remove Entry
This will remove the item being iterated through from the parent list.
Last updated 5 months ago
Was this helpful?