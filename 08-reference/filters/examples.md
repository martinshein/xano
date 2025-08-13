---
category: filters
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Examples
---

# Examples

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
    fill
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Filters
Manipulation 
============
NOTE
When a filter below refers to the **parent value**, we\'re talking about the value box that lives immediately above the filter.
[]
fill
Create an array of a certain size with a default value.
Parameter
Purpose
Example
parent value
The default value to fill
\"default value\"
start
The starting index of the array
0
length
The number of items in the array
10
###  
Examples
Example
Result
[]
Copy
``` 
[
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value"
]
```
------------------------------------------------------------------------
fill\_keys
Creates an object of a certain size with a default value and a list of keys.
Parameter
Purpose
Example
parent value
The default value to fill
\"default value\"
keys
The array of keys to use
Copy
``` 
[
    "key1",
    "key2",
    "key3"
]
```
###  
Examples
Example
Output
[]
Copy
``` 
```
------------------------------------------------------------------------
first\_notempty
Applies the first value that is not **empty** (0, null, \"\", empty string)
Useful if you need to determine a value to apply based on what is provided, such as editing a database record and being uncertain if an input will be provided to replace a value.
Parameter
Purpose
Example
parent value
The value to check if empty
Can contain any value, or no value.
value
The value to use if the parent value is empty
\"default\"
###  
Examples
------------------------------------------------------------------------
first\_notnull
Applies the first value that is not `null`
Useful if you need to determine a value to apply based on what is provided, such as editing a database record and being uncertain if an input will be provided to replace a value.
Hint
Remember, `null` is its own value entirely. It is not the same as \"null\", an empty string, or any other similar empty state.
Parameter
Purpose
Example
parent value
The value to check if `null`
Can be any value
value
The value to use if the parent value is `null`
\"default\"
###  
Examples
------------------------------------------------------------------------
get
Gets a value at the specified path inside of an array or object.
For arrays, the path can be an index, such as `0`, `1,` or `2`, which will get the specific item at that index in the array.
For arrays of objects, you can specify the index + a path, such as `2.name`
For single objects, you can just specify the path, such as `name`.
This filter is useful if you aren\'t sure if the value you need will exist, and need to provide a default value in place of it.
Hint
Are you getting errors in your function stacks because certain values don\'t exist all the time? The **GET** filter can be a great fix for this.
Parameter
Purpose
Example
parent value
The object or array to search for the value
This can be an object, array, a variable, or the result of one of the Get All Input functions [\[1\]](../functions/utility-functions.html#get-all-input) [\[2\]](../functions/utility-functions.html#get-all-raw-input)
path
The path to look for inside of the parent value
For getting a specific array item:
`0`
For getting a specific path inside of an object:
`pathName`
For getting a specific path inside of an array of objects:
`0.pathName`
default value
The value to provide in place of the value that isn\'t found
This value can be whatever you\'d like.
###  
Examples
An age is provided in the input, so it is provided by the GET filter.
No age is provided in the input, so the default value is used instead.
------------------------------------------------------------------------
has
Checks if a value is present (similar to get), but only returns a true or false.
Parameter
Purpose
Example
parent value
The object or array to search for the value
This can be an object, array, a variable, or the result of one of the Get All Input functions [\[1\]](../functions/utility-functions.html#get-all-input) [\[2\]](../functions/utility-functions.html#get-all-raw-input)
path
The path to look for inside of the parent value
For getting a specific array item:
`0`
For getting a specific path inside of an object:
`pathName`
For getting a specific path inside of an array of objects:
`0.pathName`
###  
Examples
An age is provided, so the filter returns **true**
An age is not provided, so the filter returns **false**
------------------------------------------------------------------------
set
Replaces or inserts new data at a specified path.
Parameter
Purpose
parent value
The object or array to target with the set filter
path
The path at which to insert the supplied value
value
The supplied value to use
###  
Examples
Replace a value with another
Set a new key inside of an object
------------------------------------------------------------------------
set\_conditional
Use set\_conditional to set a new value in an object based on whether a condition evaluates as true.
Parameter
Purpose
parent value
The data to insert the result, such as an object
path
The path to insert the result
value
The value to insert at the specified path
conditional
The condition to check. This can either come from an earlier function,or another filter that returns a `true` or `false`
###  
Examples
The age provided is greater than 20, so we return the value set in our set\_conditional filter
------------------------------------------------------------------------
set\_ifnotempty
set\_ifnotnull
Sets a new value in an object if the value provided is not empty. An empty value can be 0, `null`, or an empty string.
set\_ifnotnull works the same, but only checks for `null`
Parameter
Purpose
Example
parent value
Where to set the value
This will usually be an existing object
path
The path to set the value if the checked value exists
\"name\"
\"age\"
\"location\"
value
The value to set if the checked value is not empty (or null)
Any value
###  
Examples
<div>
1
###  
First, we\'re getting an existing record from the database.
In this function stack, we\'re simulating a user submitting changes to their user profile.
2
###  
Then, we use an Update Variable with set\_ifnotempty (or set\_ifnotnull) to determine whether or not the returned record needs to be updated.
3
###  
Finally, we edit the record using the result of step 2 for all of our values.
</div>
------------------------------------------------------------------------
transform
The `transform` filter is universal way to transform data. It works with arrays, objects, and scalar values. It uses the expression data type to specify the transformation.
Hint
This filter is similar to the map filter, except it can bind to all data - not just an array.
You can use the context variable \$\$ to target the parent value.
Parameter
Purpose
Example
parent value
The value to apply the transformation to
Can be any value or variable
expression
The expression to run
Any expression
Read more about expressions and Xano Transform below.
[[Expression]]
[[Xano Transform]]
###  
Examples
Copy
``` 
[1,2,3]|transform:($$|count)                              // returns 3
[1,2,3]|transform:($$|count)+($$|sum)                     // returns 9
|transform:$$.first~" "~$$.last    // returns Alpha Beta
```
------------------------------------------------------------------------
unset
Removes a key from an object
Parameter
Purpose
parent value
The object to target
path
The name of the key to remove from the object
###  
Examples
The user record normally returns a \"name\", but using **unset** has removed it.
------------------------------------------------------------------------
Last updated 4 months ago
Was this helpful?

## Code Examples

```
 
[
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value"
]

```

```
 
[
    "key1",
    "key2",
    "key3"
]

```

```
 

```

```
 
[1,2,3]|transform:($$|count)                              // returns 3
[1,2,3]|transform:($$|count)+($$|sum)                     // returns 9
|transform:$$.first~" "~$$.last    // returns Alpha Beta

```

