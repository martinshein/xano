---
category: function-stack
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'Function: Utility Functions'
---

# Function: Utility Functions

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
    Return
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Functions
Utility Functions 
=================
Return
Halts execution and returns the defined result immediately. Return is useful when used in combination with conditional statements where you want to change the return based on the result of the condition.
Try/Catch
<div>
</div>
Try/catch enables you to catch any errors that may occur in a specific stack of functions and execute additional logic based on that result. This function essentially enables fully custom error handling in Xano.
**Try** - Try these functions first
**Catch** - Execute these functions if the Try statements return an error
**Finally** - Execute these functions regardless of the result
In the below example, we are starting with a Delete File function, and trying to delete a file that does not exist.
[]
Deleting a file that does not exist returns ERROR\_CODE\_NOT\_FOUND and halts execution.
Normally, when an error occurs in the function stack, execution is halted entirely. If we wanted to deploy some customized error handling to change this behavior, we can do so by placing this function inside of a Try/Catch statement.
In the below iteration, we\'ve moved Delete File into the Try portion of a Try/Catch statement. Now, when we run the endpoint again, the function itself is still failing, but the API itself still returns a success response.
[]
We can then use the Catch portion to read the error, using three variables only available via Try/Catch.
[]
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **code** is the error code
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **message** is the error message
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **result** will be any accompanying data. Most functions will not output a result, and only return data in **code** and **message**
    :::
When we run this again and output those variables as part of our response, you\'ll see that the API still returns a \'Success\' result, but we can view the error message returned by our function in our Try statement.
[]
You can then use the Finally section to determine the behavior based on the result of your Try/Catch. In the below example, we\'re using a conditional statement to check if the try/catch **code** variable is empty. If it is empty, we return a success message. If it is not empty (which means there was an error in our Try statements), we return an error message.
[]
**Practical Example of using Try/Catch**
<div>
</div>
Throw Error
Throw Error allows you to halt execution with a custom error message. This is different from a Precondition step because it does not restrict you to specific error codes. It can be used in combination with Try/Catch or on its own.
Post Process
Post process allows you to execute additional logic after your API has provided a response. This can be useful if you want to see a response on your front-end without waiting for any additional processing to occur, but a background task does not meet your needs.
**Example**
[]
In this function stack, we are setting **var\_1** with a value of \"Hello\" and calling an external API to send the contents of this variable.
Afterwards, we have added Post Process to update **var\_1** and send a new request to the same external API.
The function stack is set to respond with the contents of **var\_1.**
[]
This means that the following will happen in sequence:
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set **var\_1** to \"Hello!\"
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Send **var\_1** to external API
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    The Xano API responds with \"Hello!\"
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set **var\_1** to \"Goodbye!\"
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    Send **var\_1** to external API
    :::
Below is a video of this example in action. Note how the external API recieves both \'Hello\' and \'Goodbye\', but the Xano API just responds with \'Hello\'. *Note: the video does not contain any audio.*
Post Process will use the state of variables where it is defined. This means that while Post Process executes at the end of the function stack, the placement is still important to ensure that any variables it uses retain the appropriate content.
Post Process also enables the use of some special variables: **body, headers,** and **status\_code**. These are only available during post process, and can be used to transmit any of the corresponding data back to a database table, or to an external API, to record the results of post process.
[]
Debug Log
Debug Log allows you to output specific information in a new debug logging section of the Debugger. This is similar to how a console log statement in Javascript would behave. These steps will not run outside of Run & Debug.
<div>
</div>
This can be especially helpful for debugging data errors with loops or otherwise just giving you a quick view of a variable\'s contents during execution. You can insert whatever data you\'d like into Debug Logs; they will accept any data type, and can also have filters applied.
[]
In the below example, we\'re looping through results from a Query All Records statement, and outputting a specific value from each item to the new Debug Log.
[]
And the result is available in the new Debug Log section of the debugger
Precondition
A precondition is a statement that says \"this condition must evaluate as true, or we halt execution and return an error message.\"
<div>
1
###  
Preconditions use the expression builder to define the conditions it checks. Click []to define your conditions.
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
2
###  
Define what happens if the conditions do [not] evaluate as true.
You can provide a custom error message, choose an error type, and supply a payload to return, such as the values being checked in your conditions.
</div>
Stop & Debug
Halts execution and returns a value. Useful to ensure that specific pieces of your function stack are running as expected while building.
[]
Group
Groups functions together. This is an organizational tool for you as you build your function stacks and does not impact any part of the actual execution.
Sleep
Waits for a defined number of seconds before proceeding to the next step.
CSV Stream
CSV Stream is a powerful function allowing you to \'stream\' chunks of a CSV file in sequence to your function stack, allowing for processing of large CSV files.
<div>
</div>
A successful CSV stream function stack includes three essential parts.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    a **file resource** to ingest the CSV file This can come from either a File Resource input, or a file delivered by an external API, with a Create File Resource step applied
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    a **CSV stream** function to stream the CSV data This function initiates the streaming of CSV data, and provides an output variable. This output variable is meant for use with a For Each loop
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    a **For Each** loop to run through the individual CSV rows The loop is responsible for performing any functions you\'d like on your CSV, such as adding each row to one of your database tables.
    :::
In the below example, we\'ve added these three key components, and can now process the incoming CSV data.
CSV Stream is a much simpler alternative to the previously established method of array functions and object manipulation to process incoming CSV data.
[][]
JSONL Stream
JSONL Stream is a powerful function allowing you to \'stream\' chunks of JSON in sequence to your function stack, allowing for processing of large data sets, similar to the CSV Stream function above.
HTTP Header
Set a custom HTTP header. This function is useful if you need your responses to deliver specific, custom headers. You can also use this to specify custom API response codes outside of the ones our Precondition function offers.
The **duplicates** parameter lets you decide to either replace headers that already exist with your new header, or allow for duplicate headers to exist.
[]
Examples of Custom HTTP Headers
Please note that each individual header should use its own Set Header function.
**Rate Limiting**
These will not enforce rate limits themselves, but it\'s good information to have in your headers if you are rate limiting your APIs.
Copy
``` 
X-Rate-Limit-Limit: 100
X-Rate-Limit-Remaining: 95
X-Rate-Limit-Reset: 1615560000
```
####  
Serving Content Downloads
If you want your API to directly serve file downloads, use this header:
Copy
``` 
Content-Disposition: attachment; filename="report.pdf"
```
You may also need:
Copy
``` 
Content-Type: text/html
```
####  
Custom HTTP Status
Sometimes, you might need to send an HTTP status that Xano doesn\'t natively offer using preconditions.
Copy
``` 
HTTP/1.1 201 Created
Content-Type: application/json
```
Get All Variables
Returns all of the variables present up to that point in the function stack.
Get All Input
Returns all of the inputs sent to the API in a single object.
Get All Raw Input
Returns all data sent to the API, even if they are not defined inputs. You\'d use this function when building a **Webhook,** or you otherwise aren\'t sure what data will be sent to this endpoint.
Exclude Middleware Modification should be set to `false` if you intend on using the raw data in your function stack **before** it\'s modified by Middleware.
Get Environment Variables
Returns all of your environment variables in a single object.
Calculate Distance
Calculate the distance between two longitude/Latitude points
[]
IP Address Lookup
Takes in an IP address and returns geographical information based on that IP. This product includes GeoLite2 data created by MaxMind, available from https://www.maxmind.com.
[]
Set Data Source
This function allows you to specify which data source that database operations following it target. Remember that the order of operations in a function stack matters, so any database operations that come before your Set Data Source statement will use whatever is used normally.
[]
Async Function Await
Learn about Async functions here
Last updated 2 months ago
Was this helpful?

## Code Examples

```
 
X-Rate-Limit-Limit: 100
X-Rate-Limit-Remaining: 95
X-Rate-Limit-Reset: 1615560000

```

```
 
Content-Disposition: attachment; filename="report.pdf"

```

```
 
Content-Type: text/html

```

```
 
HTTP/1.1 201 Created
Content-Type: application/json

```

