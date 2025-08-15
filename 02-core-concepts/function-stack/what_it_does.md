---
title: "Function Stack Overview"
description: "Understand what function stacks do in Xano and how they power your backend logic and API operations"
category: function-stack
difficulty: beginner
tags:
  - overview
  - concept
  - workflow
  - logic
  - backend
  - api
related_docs:
  - functions
  - building-with-visual-development
  - apis
  - database
last_updated: '2025-01-23'
---

# Function Stack Overview

## Quick Summary
Function stacks are the core of Xano's visual development platform, defining the step-by-step logic that executes when APIs are called or events are triggered. They transform inputs, process data, and generate responses through a sequence of connected functions.

## What You'll Learn
- Function stack fundamentals
- How function stacks execute
- Types of functions available
- Data flow through function stacks
- Best practices for stack design
- Common function stack patterns

Function stacks are the building blocks that transform your business requirements into executable backend logic, making complex operations simple and maintainable.
title: What it does
---

# What it does

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
    Add to End of Array
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Functions
3.  Data Manipulation
Arrays 
======
An array, or list, may contain a single item or many items. Arrays behave differently than other data types; you will typically iterate through them to transform data. These iterations can be performed with loops, or you can perform more wide-sweeping changes using expressions.
We have several array functions that you can use to extract and manipulate the array quickly.
Before you dive in, let\'s review a key concept specific to arrays: index
The **index** is the number that corresponds to the item in the list, starting at 0. You won\'t see this reflected in your data, but it\'s how arrays keep track of their defined order of items.
Add to End of Array
Adds an item to the end of an array
Add to Beginning of Array
Adds an item to the beginning of an array
Remove from End of Array
Removes the item at the end of the array
Remove from Beginning of Array
Removes the item at the beginning of the array
Merge
Merges two arrays together
Find First Element
Uses the expression builder to find the first matched element of an array
Find First Element Index
Uses the expression builder to find the index of the first matched element of an array
Has Any Element
Returns a true or false based on if the array has any elements that meet the conditions outlined in the expression builder
Has Every Element
Returns a true or false based on if the array has **all** elements that meet the conditions outlined in the expression builder
Find All Elements
Uses the expression builder to find all matching elements in the array
Get Element Count
Uses the expression builder to find the count of all matching elements in the array
Array: Map
####  
What it does
**Array: Map** transforms each element in a collection using a mapping rule and returns a new array of the transformed values. Use it for formatting, calculations, or reshaping array data.
####  
Example --- Format numbers as USD currency
**Before**
Copy
``` 
[11124.12, 235632.12, 393938.52]
```
**After**
Copy
``` 
["$11,124.12", "$235,632.12", "$393,938.52"]
```
**How it works:** For each number (`$this`):
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    `number_format($this, 2, ".", ",")` produces a string with two decimals, `.` as decimal separator, and `,` as the thousands separator.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    `concat("$", …)` prefixes the dollar sign.
    :::
UI Field
Example value
Notes
**Collection**
`json_decode('[11124.12,235632.12,393938.52]')`
If you already have an array variable, reference it instead.
**Output type**
`Array of Values`
We output strings such as `"$11,124.12"`.
**Mapping function → Value**
`concat("$", number_format($this, 2, ".", ","))`
`$this` is the current element.
**Result as**
`x1`
Variable name to store the mapped array.
------------------------------------------------------------------------
Array: Partition
####  
What it does
**Array: Partition** splits a list into two buckets based on a boolean expression you define. Items where the expression returns **true** go under the `true` key; the rest go under `false`.
####  
Example --- Separate an array that contains different data types, such as text and n
**Before**
Copy
``` 
[1,2,"hello",3,4,"goodbye"]
```
**After**
Copy
``` 
```
**How it works:** For each number (`$this`), evaluate `$this`.is a text string.
UI Field
Example value
Notes
**Array**
`[1,2,3,4,5]`
Your input list.
**Expression**
`$this|is_text=true  `
Any expression that returns boolean.
**Result as**
`variable_name`
Stores an object with `true` and `false` arrays.
------------------------------------------------------------------------
Array: Group By
####  
What it does
**Array: Group By** organizes items into an object keyed by a value you compute from each item. Each key maps to an array of items that share that key.
####  
Example --- Group people by age
**Before**
Copy
``` 
[
  ,
  ,
]
```
**After**
Copy
``` 
{
  "25": [
    ,
  ],
  "30": [
  ]
}
```
**How it works:** For each person (`$this`), the grouping key is `$this.age`.
UI Field
Example value
Notes
**Collection**
`[,,]`
Your array of objects.
**Mapping function → Value**
`$this.age`
Determines the group key for each item.
**Result as**
`grouped_people`
Stores an object keyed by age; values are arrays of matching items.
------------------------------------------------------------------------
Array: Difference
####  
What it does
**Array: Difference** returns elements that are present in the **first** array but **not** in the **second**, comparing items by an optional mapping function.
####  
Example --- Students who didn't submit homework
**Before**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    First array: `["Amy", "Bob", "Eve"]`
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Second array: `["Amy", "Eve"]`
    :::
**After**
Copy
``` 
["Bob"]
```
**How it works:** Map each item to a comparable value (here, just the item itself via `$this`). Return only items from the first array whose mapped value does not appear in the second array.
UI Field
Example value
Notes
**Collections → First**
`["Amy","Bob","Eve"]`
The "source" list.
**Collections → Second**
`["Amy","Eve"]`
Items to exclude.
**Mapping function → Value**
`$this`
Compare on the item itself. For objects, use something like `$this.id`.
**Result as**
`missing_students`
Array of elements found only in the first array.
------------------------------------------------------------------------
Array: Intersection
####  
What it does
**Array: Intersection** returns elements that are present in **both** arrays, comparing by an optional mapping function.
####  
Example --- Customers who bought both products
**Before**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Buyers of A: `["Alice","Bob","Eve"]`
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Buyers of B: `["Eve","Charlie","Bob"]`
    :::
**After**
Copy
``` 
["Bob", "Eve"]
```
**How it works:** Map each item to a comparable value (here, the item itself with `$this`). Keep only values that appear in both arrays.
UI Field
Example value
Notes
**Collections → First**
`["Alice","Bob","Eve"]`
First list.
**Collections → Second**
`["Eve","Charlie","Bob"]`
Second list.
**Mapping function → Value**
`$this`
For objects, use a key like `$this.email` or `$this.id`.
**Result as**
`shared_customers`
Array of common elements.
------------------------------------------------------------------------
Array: Union
####  
What it does
**Array: Union** merges two arrays and returns an array of **unique** elements from both, comparing by an optional mapping function.
####  
Example --- Merge mailing lists without duplicates
**Before**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    List 1: `["Alice","Bob"]`
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    List 2: `["Bob","Charlie"]`
    :::
**After**
Copy
``` 
["Alice", "Bob", "Charlie"]
```
**How it works:** Combine both arrays, then deduplicate based on the mapped value (here using `$this` to compare raw values).
UI Field
Example value
Notes
**Collections → First**
`["Alice","Bob"]`
First list.
**Collections → Second**
`["Bob","Charlie"]`
Second list.
**Mapping function → Value**
`$this`
For objects, use a stable key like `$this.id`.
**Result as**
`all_unique_contacts`
Array of unique values from both inputs.
Using the Expression Builder
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
Last updated 4 days ago
Was this helpful?

## Code Examples

```
 
[11124.12, 235632.12, 393938.52]

```

```
 
["$11,124.12", "$235,632.12", "$393,938.52"]

```

```
 
[1,2,"hello",3,4,"goodbye"]

```

```
 

```

```
 
[
  ,
  ,
]

```

```javascript
 
{
  "25": [
    ,
  ],
  "30": [
  ]
}

```

```
 
["Bob"]

```

```
 
["Bob", "Eve"]

```

```
 
["Alice", "Bob", "Charlie"]

```

