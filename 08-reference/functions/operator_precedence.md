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
title: Operator Precedence
---

# Operator Precedence

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
    Using the Expression Editor & Playground
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Data Types
Expression 
==========
Expressions are a flexible data type that Xano parses in real-time to support an inline syntax to expressing data with mathematical expressions. Anything you can do with Xano filters, can also be done inline within an expression.
When building expressions, make sure you have the \'expression\' data type selected. You can also click Use Expression under any value box to quickly switch.
Expression building in Xano leverages auto-complete, which will auto-populate references to inputs and variables, filters, and other common notation.
<div>
</div>
Using the Expression Editor & Playground
When using the Expression data type, you will be presented with an Expression Editor & Playground to enable easier editing and testing of your expression.
To get the most value out of the expression editor and playground, make sure to add any variable contents you\'d like to use in the Context panel, and make sure to Run & Debug your function stack to enable auto-complete.
**Expression Editor**
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Build and edit your expression here with easy auto-complete
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Test your expression in the playground or apply the changes
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Get quick context for variables accessible by your expression and their data types
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Search the library of transformers (filters) available to use, and see examples of how they work
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    Take a quick Expressions tutorial
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    Enable new variables to be set to Expression type by default
    :::
**Playground**
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Edit your expression here
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Run and test your expression
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    The result of the last execution
    :::
The playground also retains access to the transformers (filters) library and the tutorial. You\'ll need to edit your variable context here if testing with variable data. Just copy and paste the contents into the context panel.
Mathematical Operators
Operator
Function
Example
Result
\+
addition
100 + 101
201
\-
subtraction
100 - 101
-1
\*
multiplication
100 \* 101
10101
/
division
100 / 10
10
###  
Operator Precedence
For the most part expressions are evaluated left to right. Using parentheses to illustrate a point, the following would be the same assuming all operators were being evaluated left to right.
Copy
``` 
1 + 2 + 3     == 6
1 + (2 + 3)   == 6
```
However, there are a few operators which get special priority and get evaluated first. These operators are the multiplication and divide operators.
Copy
``` 
1 + 2 * 3    == 7          // if left to right, then 9 (which is incorrect)
1 + (2 * 3)  == 7
1 + 4 / 2    == 3          // if left to right, 2.5 (which is incorrect)
1 + (4 / 2)  == 3
```
Text Operators
Operator
Function
Example
Result
\~
concatenation
a \~ b
ab
To add separation when concatenating, add an empty string between the values: ​`a~" "~b`
Array Operators
Operator
Function
Example
Result
\...
spread items within an array
\[1,2,3, \...\[4,5,6\],7\]
\[1,2,3,4,5,6,7\]
..
range operator
1..10
\[1,2,3,4,5,6,7,8,9,10\]
Array Indexes
Expressions have the ability to reference array elements using all integer values (0, positive numbers, and negative numbers). Using a negative number represents starting from the top of the list rather the beginning of the list.
Expression
Result
\[a,b,c,d,e\]\[0\]
a
\[a,b,c,d,e\]\[1\]
b
\[a,b,c,d,e\]\[-1\]
e
\[a,b,c,d,e\]\[-2\]
d
Object Operators
Operator
Function
Example
Result
\...
spread items within an object
{a:1, b:2, \..., d: 4}
Comparison Operators
Operator
Function
Example
Result
==
equals (type conversion)
1 == \"1\"
true
===
strict equals
1 === \"1\"
false
!=
not equals (type conversion)
1 != \"1\"
false
!==
strict not equals
1 !== \"1\"
true
\>
greater than
1 \> 2
false
\>=
greater than or equals
1 \>= 2
false
\<
less than
1 \< 2
true
\<=
less than or equals
1 \<= 2
true
Logical Operators
Operator
Function
Example
Result
!
not
!true
false
\|\|
or
1 \< 2 \|\| 1 != 1
true
&&
and
1 \< 2 && 1 != 1
false
All of these operators evaluate their expressions as truthy statements. This means that a comparison operator is not required. For example: 0 \|\| 1 would evaluate to true since 1 evaluates as true.
Conditional Operators
Operator
Function
Example
Result
a ? b : c
ternary (if/else)
1 \< 2 ? 3 : 4
3
a ?: b
shorthand ternary (this/that)
1 ?: 2
1
a ?? b
null coalescing
null ?? 10
10
The ternary operator has 2 forms - the traditional if/else based on expression and the shorthand (this/that). The shorthand version will use either the left (this) or the right (that) based on which one evaluates to a truthy statement first going from left to right.
The null coalescing operator is very similar to the shorthand ternary, except that instead of relying on a truthy statement, it only checks for the null value.
Variable Syntax
Variables can be referenced using the same syntax that is available within Lambdas.
###  
Variables
Variables within the function stack are accessible through `$var` root variable.
###  
Inputs
Inputs are accessible through the `$input` root variable.
###  
Authentication
Authentication values are accessible through the `$auth` root variable.
###  
Environment Variables
Environment variables are accessible through the `$env` root variable. This includes both system variables (\$remote\_ip, \$datasource, etc.) as well as workspace environment variables.
###  
Auto-Complete
When building expressions, you\'ll see autocomplete suggestions as you type. This works for variables, inputs, and environment variables, as well as filters.
For variables with nested data, such as objects, you\'ll also be presented with an auto-complete of the fields inside of that object. In this example, we\'re targeting a variable called `log`and are presented with the fields inside of that variable by the expression builder, as well as a description of each.
Data Types
The Xano expression engine supports a more relaxed syntax for its data types to make it easier to reference text and variables without the strict requirements of using quotation marks.
Expression
Type
Result
abc
text
\"abc\"
123
integer
123
\$var.score
integer
123
\"\$var.score\"
text
\"\$var.score\"
\"\\\"\"
text with escaped character
\"
true
boolean
true
false
boolean
false
\"true\"
text
\"true\"
null
null
null
\"null\"
text
\"null\"
\"123\"
text
\"123\"
\[1,2,3\]
array of integers
\[1,2,3\]
\[\"1\",\"2\",\"3\"\]
array of text
\[\"1\",\"2\",\"3\"\]
\[a,b,c\]
array of text
\[\"a\",\"b\",\"c\"\]
\[\"a\",\"b\",\"c\"\]
array of text
\[\"a\",\"b\",\"c\"\]
object
object
object
Dot Notation
The same relaxed syntax used for data types also applies to dot notation.
Dot Notation
JSON Equivalent
\$var.items
\$var.items
\$var.items\[1\]
\$var.items\[1\]
\$var.items\[\"1\"\]
\$var.items\[\"1\"\]
\$var.items\[a\]
\$var.items\[\"a\"\]
\$var.items\[a\~b\~c\]
\$var.items\[\"abc\"\]
\$var.items\[\"a\~b\~c\"\]
\$var.items\[\"a\~b\~c\"\]
Filters
All of the Xano filters are available within the expression syntax. To use these, you need to follow the pipe expression syntax.
Copy
``` 
variable | pipe : arg1 : arg2 : argN
```
For example, to uppercase text using the upper filter, you would do the following.
Copy
``` 
"xano"|upper
// result = XANO
```
Here is another example using a filter with an argument.
Copy
``` 
1 + 2 + (3|add:1)
// result = 7
```
This particular example is using both a mathematical \"+\" and an add filter to illustrate how they can be mixed together.
You can also chain filters together.
Copy
``` 
1 + 2 + (3|add:1|mul:2)
// result = 11
```
Importing Expressions
When importing cURL or pasting JSON into Xano, Xano can automatically detect the Expression data type, provided the expression begins with a \$ character.
As an example, the following JSON\...
Copy
``` 
```
\...will import as:
Advanced Examples
As showcased above, the Xano expression engine is very powerful. Here we can look into some more advanced use cases that bring everything together.
###  
Conditional
####  
Sample Data
Copy
``` 
$input = 
$var = 
```
Expression
Copy
``` 
($input.scores|max) > ($var.numbers|min)
// result = false
```
###  
Null coalescing
####  
Sample Data
Copy
``` 
$input = 
$var = 
```
####  
Expression
Copy
``` 
(($input.scores|merge:[100,101,102])|max)+($var.bad_syntax ?? 100)
// result = 202
```
###  
Ternary
####  
Sample Data
Copy
``` 
$input = 
$var = 
```
####  
Expression
Copy
``` 
($input.scores[2] == 3 ? 10 : 100) + (($var.numbers|min) ?: $var.numbers|max))
// result = 16
```
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
1 + 2 + 3     == 6
1 + (2 + 3)   == 6

```

```
 
1 + 2 * 3    == 7          // if left to right, then 9 (which is incorrect)
1 + (2 * 3)  == 7
1 + 4 / 2    == 3          // if left to right, 2.5 (which is incorrect)
1 + (4 / 2)  == 3

```

```
 
variable | pipe : arg1 : arg2 : argN

```

```
 
"xano"|upper
// result = XANO

```

```
 
1 + 2 + (3|add:1)
// result = 7

```

```
 
1 + 2 + (3|add:1|mul:2)
// result = 11

```

```
 

```

```
 
$input = 
$var = 

```

```
 
($input.scores|max) > ($var.numbers|min)
// result = false

```

```
 
$input = 
$var = 

```

```
 
(($input.scores|merge:[100,101,102])|max)+($var.bad_syntax ?? 100)
// result = 202

```

```
 
$input = 
$var = 

```

```
 
($input.scores[2] == 3 ? 10 : 100) + (($var.numbers|min) ?: $var.numbers|max))
// result = 16

```

