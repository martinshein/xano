---
category: functions
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
            -   Swagger (OpenAPI
                Documentation)
            :::
            ::: 
            -   Async
                Functions
            :::
        -   Background Tasks
        -   Triggers
        -   Middleware
        -   Configuring
            Expressions
        -   Working with Data
        :::
        ::: 
        -   AI Tools
            ::: 
                ::: 
                -   External Filtering
                    Examples
                :::
            -   Get
                Record
            -   Add
                Record
            -   Edit
                Record
            -   Add or Edit
                Record
            -   Patch
                Record
            -   Delete
                Record
            -   Bulk
                Operations
            -   Database
                Transaction
            -   External Database
                Query
            -   Direct Database
                Query
            -   Get Database
                Schema
            :::
            ::: 
            -   Create
                Variable
            -   Update
                Variable
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
            -   Realtime
                Functions
            -   External API
                Request
            -   Lambda
                Functions
            :::
        -   Data Caching
            (Redis)
        -   Custom
            Functions
        -   Utility
            Functions
        -   File
            Storage
        -   Cloud
            Services
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
        -   Response
            Caching
        :::
-   ::: 
    Testing and Debugging
    :::
-   ::: 
    The Database
    :::
        ::: 
        -   Using the Xano
            Database
        -   Field
            Types
        -   Relationships
        -   Database
            Views
        -   Export and
            Sharing
        -   Data
            Sources
        :::
        ::: 
        -   Airtable to
            Xano
        -   Supabase to
            Xano
        -   CSV Import &
            Export
        :::
        ::: 
        -   Storage
        -   Indexing
        -   Maintenance
        -   Schema
            Versioning
        :::
-   ::: 
    Build For AI
    :::
        ::: 
        -   Templates
        :::
        ::: 
        -   Connecting
            Clients
        -   MCP
            Functions
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
        -   Separating User
            Data
        -   Restricting Access
            (RBAC)
        -   OAuth
            (SSO)
        :::
-   ::: 
    Xano Features
    :::
        ::: 
        -   Release Track
            Preferences
        -   Static IP
            (Outgoing)
        -   Change Server
            Region
        -   Direct Database
            Connector
        -   Backup and
            Restore
        -   Security
            Policy
        :::
        ::: 
        -   Audit
            Logs
        :::
        ::: 
        -   Xano
            Link
        -   Developer API
            (Deprecated)
        :::
        ::: 
        -   Master Metadata
            API
        -   Tables and
            Schema
        -   Content
        -   Search
        -   File
        -   Request
            History
        -   Workspace Import and
            Export
        -   Token Scopes
            Reference
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
        -   Agency
            Dashboard
        -   Client
            Invite
        -   Transfer
            Ownership
        -   Agency
            Profile
        -   Commission
        -   Private
            Marketplace
        :::
-   ::: 
    Custom Plans (Enterprise)
    :::
        ::: 
            ::: 
                ::: 
                -   Choosing a
                    Model
                :::
            :::
        -   Tenant
            Center
        -   Compliance
            Center
        -   Security
            Policy
        -   Instance
            Activity
        -   Deployment
        -   RBAC (Role-based Access
            Control)
        -   Xano
            Link
        -   Resource
            Management
        :::
-   ::: 
    Your Xano Account
    :::
-   ::: 
    Troubleshooting & Support
    :::
        ::: 
        -   When a single workflow feels
            slow
        -   When everything feels
            slow
        -   RAM
            Usage
        -   Function Stack
            Performance
        :::
        ::: 
        -   Granting
            Access
        -   Community Code of
            Conduct
        -   Community Content Modification
            Policy
        -   Reporting Potential Bugs and
            Issues
        :::
-   ::: 
    Special Pricing
    :::
-   ::: 
    Security
    :::
-   ::: 
    :::
    What is a custom function?
-   Building and Using Custom
    Functions
-   Access your custom functions from the left-hand
    menu.
-   Click + Add Function to create a new custom
    function.
-   Insert your new custom function into other function
    stacks.
-   Creating Custom Functions from Existing Function
    Stacks
-   Select individual steps to convert to a
    function
-   Creating New Folders with Existing
    Functions
-   Moving Existing Functions into
    Folders
Was this helpful?
Copy
1.  [[🛠️]The Visual
    Builder](../building-with-visual-development.html)
2.  Building with Visual Development
Custom Functions 
================
Build business logic once and reuse it in multiple places
**Quick Summary**
Custom functions are very similar to your APIs --- they have inputs, a
function stack, and a response. However, they can not be called
externally. Instead, custom functions allow you to build something and
use it in other places, while maintaining it in a centralized location.
What is a custom function?
Custom functions can be thought of as a building block for the rest of
your backend. You can build a custom function just like an API endpoint,
and insert that custom function into other function stacks, giving you
easily reusable logic while only having to maintain it in one place.
When you make a change inside of a custom function, that change is
automatically in effect everywhere you have chosen to use the custom
function.
------------------------------------------------------------------------
Building and Using Custom Functions
<div>
1
###  
Access your custom functions from the left-hand menu.
2
###  
Click [ + Add Function ] to create a new custom function.
Give your custom function a **name**, **description**, **tags**, and
choose your Request
History settings.
You can also choose to store your custom functions inside of a folder.
If the folder already exists, just start typing the name and select it
from the auto-complete. If the folder doesn\'t exist, you can create a
new one from here.
[] When you\'re done, click [ Save
].
3
###  
Build your custom function
A custom function has three sections --- the same as an API endpoint.
###  
⬇️ Inputs
The inputs are anything that a function stack needs to run. For example,
a function stack that logs in a user probably needs a username or email
and a password; these would be the inputs.
###  
🔄 Function stack
This is where all of the magic happens. All of the business logic that
is performed lives here.
As you add functions to your function stack, it will suggest next steps
based on most popular user activity.
###  
⬆️ Response
Once the function stack has done its job, it needs to know what to
return. This lives in the Response section.
4
###  
Insert your new custom function into other function stacks.
When you\'re ready to use your new custom function in other function
stacks, click
[], choose **Custom Functions** from the
panel that opens, and select your custom function.
You\'ll be able to supply data for any inputs the custom function is
expecting here.
</div>
------------------------------------------------------------------------
###  
Creating Custom Functions from Existing Function Stacks
If you have a function stack that you\'d like to convert into a custom
function, you can do so in one of the following ways.
<div>
1
###  
Convert the entire stack
Click the three dots in the upper-right corner and choose Convert To
Function
2
###  
Select individual steps to convert to a function
You can select a group of steps and click
[]to convert those steps into a custom
function.
</div>
------------------------------------------------------------------------
Custom Function Settings
###  
From the Settings panel
Name
Purpose
Name
The name of the custom function.
Description
An internal description, just for you.
Tags
Use tags to organize objects throughout your Xano workspace and find
them later
Request History
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Inherit Settings
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Use whatever is set in your workspace branch defaults
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Other
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Set specific request history settings for this function
        :::
    :::
[📖] **Learn more about request
history**
Response caching
Cache the response and redeliver it during future runs [📖]
**Learn more about response
caching**
------------------------------------------------------------------------
Custom Function Folders
You can organize your custom functions into folders for better
organization.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Folders are not required if you prefer not to use them. You can
    store all of your functions in folders, or use a combination of
    folders and no folders.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    A folder requires having at least one function inside of it ---
    empty folders are not supported.
    :::
<div>
1
###  
Creating New Functions
When creating a new function, you\'ll be given the option to store it in
a folder.
Just start typing the name of the folder. If it exists, select it from
the auto-complete dropdown. If it doesn\'t exist, it will be created for
you.
2
###  
Creating New Folders with Existing Functions
Click the [ Add Folder ] button to create a new folder
for your existing functions.
Give your new folder a name, and use the autocomplete to select at least
one function to add to it.
3
###  
Moving Existing Functions into Folders
Select the functions to move by using the checkboxes on the left-hand
side, and click [ Move ]
Type a new folder name, or add them to an existing folder. When you\'re
ready, click [ Save ]
</div>
Last updated 2 months ago
Was this helpful?