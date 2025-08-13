---
category: custom-functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: "\u2B07\uFE0F Inputs"
---

# ⬇️ Inputs

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
    The Anatomy of the Visual Builder
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](building-with-visual-development.html)
Building with Visual Development 
================================
<div>
</div>
The Anatomy of the Visual Builder
The builder will be comprised of **up to** three different sections --- **inputs**, the **function stack**, and the **response**. Different function stack types may not contain all of the available sections listed below.
###  
⬇️ Inputs
The inputs are anything that a function stack needs to run. For example, a function stack that logs in a user probably needs a username or email and a password; these would be the inputs.
###  
🔄 Function stack
This is where all of the magic happens. All of the business logic that is performed lives here.
As you add functions to your function stack, it will suggest next steps based on most popular user activity.
###  
⬆️ Response
Once the function stack has done its job, it needs to know what to return. This lives in the Response section.
------------------------------------------------------------------------
What can I build?
###  
APIs
An API is a piece of logic or a workflow that can be called to run from external sources. Think about when you tap a button or link anywhere in an application; there are API calls happening behind the scenes to make sure those taps perform the expected action.
[](building-with-visual-development.html#apis) 📖 **Learn more about APIs**
###  
Custom Functions
A custom function is similar to an API, but it is reusable logic that you can insert into any other function stack. These are useful if you are implementing similar logic in multiple places, and allows you to build and maintain that logic in a single location.
[](building-with-visual-development.html#custom-functions) 📖 **Learn more about custom functions**
###  
Background Tasks
A background task is a workflow that runs automatically based on a schedule that you define.
[](building-with-visual-development.html#background-tasks) 📖 **Learn more about background tasks**
###  
Triggers
A trigger is a workflow that runs every time something else happens. Xano supports two different kinds of triggers: **database triggers** and **realtime triggers**. Database triggers run every time a certain change is made in a database table, and realtime triggers run based on events in a realtime channel.
[](building-with-visual-development.html#triggers) 📖 **Learn more about triggers**
###  
Middleware
Think of middleware as an extra security guard at the entrance and exit of your other function stacks. You can build and deploy middleware to run either before a function stack, or right before it delivers a response. This is useful for things like input or output sanitization, custom error logging, security, and more.
[](building-with-visual-development.html#middleware) 📖 **Learn more about middleware**
------------------------------------------------------------------------
Using the Visual Builder
You can use both mouse and keyboard navigation when working in the builder.
###  
Adding Functions
Click to add functions to your function stack. You can search for, choose, and favorite functions in the panel that appears on the right.
You can also hover over an existing function and click the **+** sign to add a new function directly under it.
Not sure where to start?
Xano can auto-generate basic endpoints for you based on your tables.
###  
Creating a Draft
Once you start editing your API, a draft will automatically be created. Drafts keep track of each micro-change you (or your team members) make to a Function Stack called Revertible Changes, which you can easily roll back.
###  
Revertible Changes
Revertible changes show each micro-change, when they were made, what the change was, and who made it.
To revert a change, select the change you wish to revert back to. You can also revert all changes to revert all changes in the draft and return to the original version of the Function Stack.
###  
Compare Differences
Before reverting a change, you are able to see a difference comparison snapshot of the previous draft version. This provides context in the differences of the previous version compared to the current draft you are on.
Comparing differences of a previous version to the current draft.
Comparing versions in function stacks using Lambda Functions or Template Engine will show your specific code changes in a specialized format for easy readability.
Once you\'re ready to revert, select **Restore this version**.
###  
Testing a Draft
Testing the API with Run & Debug will use the draft you are editing while calling the API from the front-end will use the live (published version) of the API.
If you have other drafts across your workspace that may interact with the current API or Function Stack you are editing, you can include the relevant drafts while testing in Run & Debug.
Optionally include relevant drafts during Run & Debug.
Publishing
Once you\'re ready to publish the changes, you can simply select publish.
You can include a description of the changes you are publishing. Additionally, you have the option to publish other active drafts in your workspace. This might be useful if you are working with multiple workspace objects that interact or depend on one another and need to be certain everything works harmoniously before publishing.
Optionally include a description of the published changes. Also, you may publish other drafts in the workspace at the same time.
Once a draft is published, the changes will become live. Meaning if the API endpoint is called from a front-end, the changes will be reflected. Publishing a draft will create a new version of the API Endpoint, which allows you to roll back to previously published versions.
**How do I know if I have drafts to publish?**
You can see drafts available for testing and publish via the Publish dialog on any of your function stacks, or in a notification on the dashboard. If you find that you have made changes but are not seeing the expected results via your front-end, ensure that you have published these changes.
------------------------------------------------------------------------
Working with Data
###  
Filters
Filters are additional functions that can be applied directly to other pieces of data in Xano. For example, a filter could be used for a mathematical operation, adjust text formatting, create new datasets from existing data, and more.
To apply a filter, just hover over a value box and click **Add Filter.**
To learn more about the available filters in Xano, head to the Filters section here.
###  
Dot Notation
Dot Notation is used to navigate inside of variables and target specific pieces of data.
Let\'s use the following object as an example. This object is contained in a variable called [**author**].
Copy
``` 
```
Notice how the name field is not capitalized properly. When we edit this variable, we can use **dot notation** to target that name field specifically, like this:
Copy
``` 
author.name
```
This will tell Xano to keep the rest of the object the same, and only update the `name` field with whatever our adjustments are.
###  
Auto-Complete / Subpath
Note
We\'re currently rolling out this feature to all users as part of our next release. If you don\'t have it yet, you will soon! Hang tight.
Xano keeps an understanding of the contents inside of your variables, which makes targeting data inside them easy.
In this example, we have a customer variable that contains data from our database. If you want to target a specific piece of information inside of that variable, such as the customer\'s email or name, you can click \"x properties\" next to the variable name.
Once you do that, you\'ll be able to select the data you\'re looking for.
------------------------------------------------------------------------
Copy and Paste
You can copy and paste function stacks in Xano, enabling speedy development across environments.
Copy and paste works inside of your own function stacks, as well as copying and pasting between workspaces and instances.
**Hint**
If you need to reuse logic in more than one place, it is recommended to utilize Custom Functions.
###  
Selecting Functions
You can hold **Shift** and click on individual functions to select them.
Alternatively, you can also hold **Shift** and click + drag to select multiple functions.
Click your desired option [] or use keyboard shortcuts for your operating system of choice. **Crtl+C / Crtl+X** on Windows, or **Cmd+C / Cmd+X** on Mac.
When you\'re ready to paste, you can do so with the same standard keyboard shortcut: **Crtl+V / Cmd+V**.
------------------------------------------------------------------------
Keyboard Navigation
Section
Key
Action
Function Stack
↑ ↓
Navigate Function Stack rows inputs and response values
Function Stack
Shift ↑ ↓
Select multiple rows
Function Stack
A
Add row below highlighted row or inside highlighted empty row
Function Stack
Delete
Delete highlighted row or selection of rows
Function Stack
Enter
Edit the highlighted row
Function Stack
D
Edit the description of highlighted row
Function Stack
Cmd/Ctrl C
Copy the highlighted row or selection
Function Stack
Cmd/Ctrl X
Cut the highlighted row or selection
Function Stack
Cmd/Ctrl V
Paste function stack clipboard contents below currently highlighted row
Function Stack
Cmd/Ctrl Z
Undo last change
Function Stack
Cmd/Ctrl /
Disable/enable highlighted row
Function Stack
F
Convert a selection of rows into a function
Function Stack
G
Group a selection of rows
Function Stack
C
Clone highlighted row
Function Stack
Option/Alt ↑ ↓
Move highlighted row
Inputs and Response
Enter
Edit highlighted input/response
Inputs and Response
Delete
Delete highlighted input/response
Inputs and Response
C
Clone highlighted response
Page Actions
Cmd/Ctrl Z
Undo last action
Page Actions
Cmd/Ctrl Enter
Open the Run & Debug panel
Page Actions
Cmd/Ctrl P
Open the Publish panel\`;
Last updated 3 months ago
Was this helpful?

## Code Examples

```
 

```

```
 
author.name

```

