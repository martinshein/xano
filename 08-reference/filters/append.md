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
title: append
---

# append

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
    append
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Filters
Array 
=====
NOTE
When a filter below refers to the **parent value**, we\'re talking about the value box that lives immediately above the filter.
[]
Copy
``` 
[
    ,
]
```
###  
append
Adds a new element to the end of the array, and return the updated array
Parameter
Purpose
Example
parent value
The original array you\'d like to modify
\[1,2,3,4\]
value
The value to add to the end of the array
5
Example
Result
parent value: `[1, 2, 3, 4]`
value: 5
`[1, 2, 3, 4, 5]`
parent value: `["Think Visually", "Build Confidently"]`
value: \"Deploy Securely\"
`["Think Visually, Build Confidently, "Deploy Securely"]`
parent value:
Copy
``` 
[
    ,
]
```
value:
Copy
``` 
```
Copy
``` 
[
    ,
    ,
]
```
------------------------------------------------------------------------
###  
count
Returns the number of items in an array
Paremeter
Purpose
Example
parent value
The array to count
`[1, 2, 3, 4, 5]`
Copy
``` 
[
    ,
]
```
Example
Output
Copy
``` 
[
    ,
]
```
2
`[1, 2, 3, 4, 5]`
5
------------------------------------------------------------------------
###  
diff / diff\_assoc
###  
intsersect / intersect\_assoc
These filters are used to compare arrays.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **diff** is used to show values from the first array that **are not** in the second array
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **intersect** is used to show values from the first array that **are** in the second array
    :::
Use the basic filter for value arrays, and the **\_assoc** version for arrays of objects.
Parameter
Purpose
Example
parent value
The first array to compare
`[1, 2, 3, 4, 5]`
Copy
``` 
[
    ,
]
```
value
The second array to compare
Same as above
Example
Output
Using **diff:**
parent value: `[1,2,3,4,5]`
value: `[3,4,5,6,7]`
`[1, 2]`
Using **diff\_assoc:**
parent value:
Copy
``` 
[
    ,
    ,
]
```
value:
Copy
``` 
[
    ,
]
```
Copy
``` 
[
]
```
Using **intersect:**
parent value: `[1,2,3,4,5]`
value: `[3,4,5,6,7]`
`[3, 4, 5]`
Using **intersect\_assoc:**
parent value:
Copy
``` 
[
    ,
]
```
value:
Copy
``` 
[
    ,
    ,
]
```
Copy
``` 
[
    ,
]
```
------------------------------------------------------------------------
###  
filter\_empty
Returns a new srray with only entries that are not empty.
An **empty** value can be `[]`, ``, `0`, `null`, `""`, or `false`.
Parameter
Purpose
Example
parent value
The array to filter
`[1, 0, 2, 0, 3]`
Copy
``` 
[
    ,
    ,
]
```
path
When filtering arrays of objects, you can specify a path to optionally use a specific key to judge emptiness.
Example
Output
Copy
``` 
[
    ,
    ,
]
```
Copy
``` 
[
    ,
]
```
`[1, 0, 2, 0, 3]`
`[1, 2, 3]`
------------------------------------------------------------------------
###  
first
Get the first entry of an Array.
Parameter
Purpose
Example
parent value
The array to retrieve the first entry from
`[1, 2, 3]`
Copy
``` 
[
    ,
]
```
Example
Output
`[1, 2, 3]`
1
Copy
``` 
[
    ,
]
```
Copy
``` 
```
------------------------------------------------------------------------
###  
filter\_empty\_array
###  
filter\_empty\_object
###  
filter\_empty\_text
###  
filter\_false
###  
filter\_null
###  
filter\_zero
These filters are designed to remove the corresponding values from an object or an array. Useful in scenarios where something is sending data to your APIs that you don\'t have full control over, such as a frontend platform that always sends empty strings or null values.
Parameter
Purpose
parent value
The array or object to target
Example
Output
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
**filter\_empty\_array**
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "data": ,
        "info": null
}
```
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
**filter\_empty\_object**
Copy
``` 
```
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
**filter\_empty\_text**
Copy
``` 
{
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
**filter\_false**
Copy
``` 
{
        "title": "",
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
**filter\_null**
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": 
}
```
Copy
``` 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}
```
**filter\_zero**
Copy
``` 
{
        "title": "",
        "name": false,
        "items": [],
        "data": ,
        "info": null
}
```
------------------------------------------------------------------------
###  
flatten
Flattens a multi-level array into a single-level array.
Parameter
Purpose
Example
parent value
The array to flatten
Copy
``` 
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```
Example
Output
Copy
``` 
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```
Copy
``` 
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Copy
``` 
[
  {
    id: 1,
    name: "John",
    pets: [
      ,
    ]
  },
  {
    id: 2,
    name: "Sarah",
    pets: [
    ]
  }
]]
```
Copy
``` 
[
  ,
  ,
]
```
------------------------------------------------------------------------
###  
join
Converts an array into a text string by *joining* each value and using a separator.
Parameter
Purpose
Example
parent value
The array to join
\[\"a\", \"b\", \"c\"\]
separator ^optional^
The character or characters to place in between each array item
Can be any text value, or even a single empty space
Example
Output
parent value: `["a", "b", "c"]`
separator: \_
`a_b_c`
parent value: \[1, 2, 3, 4, 5\]
separator:
`12345`
------------------------------------------------------------------------
###  
last
Get the last entry of an Array.
Parameter
Purpose
Example
parent value
The array to get the last entry of
\[`1, 2, 3]`
Example
Output
`[1, 2, 3]`
`3`
------------------------------------------------------------------------
###  
merge
###  
merge\_recursive
Merge two arrays or objects together and return the new item.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Use **merge** to merge single level data.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Use **merge\_recursive** to merge multi-level data.
    :::
Parameter
Purpose
Example
parent value
The first array to merge
\[1, 2, 3\]
value
The second array to merge
\[4, 5, 6\]
Example
Output
using **merge**
parent value: `["a", "b", "c"]`
value: `["d", "e", "f"]`
`["a", "b", "c", "d", "e", "f"]`
using **merge\_recursive**
parent value:
Copy
``` 
```
value:
Copy
``` 
```
Copy
``` 
```
------------------------------------------------------------------------
###  
pop
Pops the last element of the Array off and returns it.
Please note that Xano\'s **pop** filter does NOT remove the item from the array.
------------------------------------------------------------------------
###  
prepend
Push an element on to the beginning of an array
------------------------------------------------------------------------
###  
push
Push an element on to the end of an array
------------------------------------------------------------------------
###  
range
Returns array of values between the specified start/stop.
------------------------------------------------------------------------
###  
remove
Remove any elements from the array that match the supplied value and return the new array
Use the **path** option to search inside of objects.
Use the **strict** option to determine how precise the filter is (for example, treating 100 and \"100\" the same)
------------------------------------------------------------------------
###  
safe\_array
Always returns an array. Uses the existing value if it is an array or creates an array of one element.
------------------------------------------------------------------------
###  
shift
Shifts the first element off the Array and returns it.
------------------------------------------------------------------------
###  
shuffle
Returns the array in a randomized order
------------------------------------------------------------------------
###  
slice
Extracts and returns a section of an array
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **offset** - what index should the slice start, starting at 0
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **length** - how many items to slice
    :::
------------------------------------------------------------------------
###  
sort
Sort an Array of elements with an optional path inside the element, sort type, and ascending/descending.
Sort types include:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **text** - case-sensitive sort for text
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **itext** - case-insensitive sort for text
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **number** - to sort numerically
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **natural** - case-sensitive sort that is alphanumerical and natural to humans
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **inatural** - case-insensitive sort that is alphanumerical and natural to humans
    :::
Ascending order is performed with a true boolean. Descending order uses a false boolean.
The example below shows the difference between case-sensitivity sort with text and itext:
The example below shows how to use the number sort type:
The example below shows using the natural sorting option
------------------------------------------------------------------------
###  
unique
Returns unique values of an Array. You can also use this filter with an array of objects by specifying a path to the key you would like to use to judge uniqueness.
------------------------------------------------------------------------
###  
unshift
Push an element to the beginning of an Array and return the new Array.
------------------------------------------------------------------------
###  
pick/unpick
These filters are meant to be used when dealing with Object field types and are particularly useful if you are receiving a large object, from a webhook for example, where only a few of those records are required for your workflows. You can also use them with an array of objects by specifying a path to the key you would like to make changes to.
**Pick**: Identify values you would like to keep and the filter will return a new object containing only the values you have selected.
Example Object
Defining the Keys we want to include in our new object.
Result
**Unpick**: Identify values you would like to exclude and the filter will return a new object containing only the fields that weren't omitted.
Example Object
Defining the Keys we want to exclude from our new object.
Result
Last updated 3 months ago
Was this helpful?

## Code Examples

```
 
[
    ,
]

```

```
 
[
    ,
]

```

```
 

```

```
 
[
    ,
    ,
]

```

```
 
[
    ,
]

```

```
 
[
    ,
]

```

```
 
[
    ,
]

```

```
 
[
    ,
    ,
]

```

```
 
[
    ,
]

```

```
 
[
]

```

```
 
[
    ,
]

```

```
 
[
    ,
    ,
]

```

```
 
[
    ,
]

```

```
 
[
    ,
    ,
]

```

```
 
[
    ,
    ,
]

```

```
 
[
    ,
]

```

```
 
[
    ,
]

```

```
 
[
    ,
]

```

```
 

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "data": ,
        "info": null
}

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```
 

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```javascript
 
{
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```javascript
 
{
        "title": "",
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": 
}

```

```javascript
 
{
        "title": "",
        "name": false,
        "width": 0,
        "items": [],
        "data": ,
        "info": null
}

```

```javascript
 
{
        "title": "",
        "name": false,
        "items": [],
        "data": ,
        "info": null
}

```

```
 
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

```

```
 
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

```

```
 
[1, 2, 3, 4, 5, 6, 7, 8, 9]

```

```javascript
 
[
  {
    id: 1,
    name: "John",
    pets: [
      ,
    ]
  },
  {
    id: 2,
    name: "Sarah",
    pets: [
    ]
  }
]]

```

```
 
[
  ,
  ,
]

```

```
 

```

```
 

```

```
 

```

