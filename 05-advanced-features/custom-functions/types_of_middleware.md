---
category: custom-functions
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Types of Middleware
---

# Types of Middleware

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
    What is middleware?
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Building with Visual Development
Middleware 
==========
Quick Summary
Middleware are separate pieces of logic that can run before something is executed, or just before it delivers a response (if applicable). It\'s designed for things like input validation, custom security or authentication implementations, logging, and output customization.
Middleware requires a **Starter plan** or higher.
What is middleware?
Middleware are separate pieces of logic that you build in Xano that can run before your API executes (even before input validation) or after your function stack is finished executing but before your API delivers its response.
Middleware can be applied at an API, API group, or workspace level. This means that you can apply the same middleware functionality to multiple API endpoints, or even your entire application, in one swing. You also have the ability to customize the middleware application at an API or API group level, meaning that if you want to apply your middleware to your entire application *except* a certain API or group, you can do that too.
Middleware offers the same functionality that any other function stack can utilize.
------------------------------------------------------------------------
Middleware Availability
Middleware is available in both **free** and **paid** versions.
**Free Version**
All of our paid plans can utilize the free version of Middleware. In the free version, you can create one Middleware function stack to assign as you see fit across your workspace.
**Paid Version**
The paid version of Middleware is included with our Scale plan. The premium version allows for unlimited creation and assignment of Middleware on APIs, functions, MCP tools, or tasks. Additional defaults are supported at the API group level, which can either be customized or inherited from workspace defaults.
If your plan includes the Compliance Center, you\'ll also be able to access reporting on middleware usage from there.
------------------------------------------------------------------------
How does middleware work?
###  
Types of Middleware
**Pre-Middleware**
Pre-middleware executes before any input validation takes place. For example, if you have one of your inputs built in such a way that it requires a minimum string length, your pre-middleware won\'t be aware of this.
Note
Pre-middleware will only surface **defined** inputs from the API it is attached to. This means for endpoints where the payload is unpredictable, you will need to ensure that all inputs are defined in the API.
**Post-Middleware**
Post-middleware executes after the function stack ends, but before the API delivers a response. The output of the middleware can be merged into the response your API generates, or replace it entirely.
A visual representation of middleware workflows
Building Middleware
From the left-side navigation, click []and choose []to access your middleware.
Click the [] button in the top-right corner to add new middleware to your workspace. Give your Middleware a name, a description, and any tags you\'d like to apply, and proceed.
Once you\'ve added your middleware, you can begin building your logic, just like any other function stack. There are a couple of key differences to be aware of, however.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Inputs**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Middleware inputs are static and can not be changed. They will automatically contain the variables coming from the parent object. This means that for pre-middleware, the parent object will provide the inputs contained in the API request. For post-middleware, this will be your API response.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        When referencing those inputs, you will do so from inside the `vars` variable. So, if you send an input labeled `text`, you\'d reference this inside a middleware stack using `vars.text`
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        The type contains whether this is running as pre or post middleware, and can not be changed.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Response**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Middleware responses have the option to either merge or replace the response in the parent object.
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            **Merge** means that middleware will generate its response and merge it with the response of the parent object. For example, if my API contains an input called `text` and my pre-middleware generates a variable called number, and my response type is set to **merge**, we could use a Get All Input function to retrieve those additional inputs. **Merge** also means that any items in the response that have the same name as your inputs will be replaced in the process, as you can not have two keys in a JSON object of the same name.
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            **Replace** means that your middleware will essentially ignore all of the inputs given to it **when it generates a response**. For example, if I am building pre-middleware, and I send it an input called \'text\', and it does not deliver that in the response, that \'text\' input will no longer be available in the API\'s function stack.
            :::
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Exception Preferences**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Silent** ignores errors thrown in middleware and allows the API to return the response without returning the error encountered
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Rethrow** allows post-middleware to execute for the purposes of error logging in your pre-middleware
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Critical** halts all execution if an error occurs
        :::
    :::
For this example, we\'ll be using the following middleware:
\...with the following API:
The middleware is responsible for checking the \'text\' API to determine if it has a value of \"Hello\" before allowing access.
After you\'ve built your middleware, you\'re ready to apply it.
Applying Middleware
###  
**Applying Middleware to your Entire Workspace**
<div>
1
###  
From your workspace dashboard, click the [⚙️] icon to access the settings, and choose Middleware.
2
###  
Select the workflow type to apply the middleware to.
You can choose from APIs, Functions, or Tasks.
3
###  
Apply PRE or POST middleware.
Click [] or []to choose a middleware to apply, based on your needs.
4
###  
Save your changes to apply the settings to the entire workspace by clicking []
</div>
###  
**Applying Middleware to an API Group or Single API**
Middleware applications are inherited from their parent object. This means that any middleware you apply at a workspace level will be populated down to each API group and API. You do have the ability to customize the middleware on API groups and individual APIs for more granular control over the middleware that applies to that workflow.
Just click the settings icon inside of an API group or API, choose Middleware, and check the Customize box to update the middleware for that specific group or API.
Why use Middleware?
###  
Flexibility
Middleware can be much more flexible in certain scenarios, such as input validation. While Xano currently offers several basic filters for input validation, such as enforcing a certain number of characters, middleware offers the power of an entire function stack to not only validate those inputs in new ways, but even transform and manipulate them, should the need arise.
###  
Build Efficiency
One of the key benefits to using middleware, as opposed to using a custom function for example, is the methods at which middleware can be applied. Having the ability to insert both PRE and POST middleware in your function stacks offers more versatile and controlled execution of the logic contained within them.
Not only that, Middleware can also be applied at a workspace or API group level, giving you a one-swing approach to applying middleware to all of your API endpoints at once, instead of having to go through each API one at a time to apply a custom function.
Last updated 1 month ago
Was this helpful?