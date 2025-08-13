---
category: 06-best-practices
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'Function: Testing And Debugging Function Stacks'
---

# Function: Testing And Debugging Function Stacks

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'testing-and-debugging-function-stacks'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Testing and Debugging Function Stacks \| Xano Documentation'
viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---
[](../index.html)
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
    Testing a Function Stack
Was this helpful?
Copy
1.  Testing and Debugging
Testing and Debugging Function Stacks 
=====================================
Testing a Function Stack
<div>
1
###  
Click [] at the top of your workflow to execute it.
Clicking this button opens the Run panel.
2
###  
Populate any necessary inputs.
This information will be used to test your workflow. If you\'re copying and pasting JSON from another source, you can use the Format button to quickly turn it into a readable structure if necessary, although this will not impact the functionality of your test run.
3
###  
Click []to execute the workflow.
Hint - Running in Safe Mode
If you\'re running into memory issues when running large function stacks or working with large data sets, you can run with Safe Mode by clicking the arrow next to the Run button and choosing **Safe Mode**.
[]
Safe Mode runs the function stack without retaining any context in memory, which can be very helpful when looping over a significant amount of data and you\'re experiencing crashes. *No context* just means that things like autocomplete won\'t work, and the output of debugging information will be limited.
Any questions, please reach out to our support team!
4
###  
Review the response and timing, if desired.
####  
Response
The response block will show you what the workflow has returned, if applicable, once execution has completed.
You can see the amount of time the request took to complete, and perform several actions from inside this block.
Click [] to copy the contents of the response
Click [] to copy the request as a cURL command to be used outside of Xano
Click [] to create a unit test based on this run.
Click [] to activate the debugger --- more on this below.
####  
Timing
You can further review more information for each step that executed during this run in the Timing block.
This block will provide individual timings for each step, allowing you to quickly pinpoint any points of delay that could be improved. You can also click the **\>** icon next to each step to review that step\'s output for further investigation.
5
###  
What\'s next?
Run it again by clicking [ Run Again ], reset everything back to the initial state by clicking [ Reset ] , or activate the debugger with [ Activate Debugger ] .
You can also use this opportunity to define sample inputs and responses for your Swagger (OpenAPI Documentation).
When testing your function stacks in Xano, you can define sample input and output examples for your Swagger documentation.
It is important that you do this to ensure that your documentation is as effective as possible, as well as for helping AI models understand what\'s expected when interacting with your APIs.
<div>
1
###  
In the \'response\' section of the Run panel, click [ Set As Example ]
2
###  
Review the sample input and response, and make any necessary adjustments
Make sure these do not include any sensitive information.
3
###  
Click [ Save ] and you will see these defined in your Swagger documentation.
If you need to make adjustments later, you can do so from the settings menu.
</div>
</div>
------------------------------------------------------------------------
Using the Debugger
The Debugger is used to review each step of execution, one at a time, to pinpoint the cause of any issues that might arise during that run.
Please note that each step is not actually individually being executed; the full run has completed prior to the debugger being available.
###  
Simple Mode
[] Stop Debugging
[] Restart the Debugger
[] Move to the next step
As you move through each step, the current will be highlighted as shown below.
Completed steps will be highlighted in green.
As you progress through each step, the **Variables** panel will update with current data.
Clicking different steps in your function stack will bring the debugger to that point.
###  
Advanced Options
Click []to enable the advanced debugging options.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Step Over** - When working with nested function stacks (custom functions or middleware), if you don\'t need to debug those, just step right over them and continue with the next function in your function stack
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Step Into / Step Out** - Step into or out of a nested function (custom function or middleware) and continue the debugging experience seamlessly
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Continue** - Continue with execution of your function stack
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Enable Breakpoints** - Enable or disable breakpoints as a whole
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Step Forwards / Step Backwards** - Toggle forward or reverse execution of your function stack
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Result** - View the result of your completed execution
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Watches** - Use custom Javascript expressions for more complex data monitoring or calculation as your function stack executes
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Variables** - View the current contents of your variables as the function stack executes
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Copy** 📄 **/ Add Watch** 👁️ - Copies the variable\'s current contents, or adds a variable to your Watches list
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Breakpoints** - Hover over the icon on the left side of each function to establish a breakpoint. Breakpoints will cause the debugger to pause at that step.
    :::
Unknown Errors and Debugger Errors
**Unknown Error**
**The debugger encountered an error**
If you see these messages, they could indicate one of the following:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    An unhandled exception in your logic
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        This means that you\'ve likely ran across a rare error that we don\'t yet have specific messaging for. Please let us know about this so we can make an adjustment.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Server resource issues
    :::
You can also try running your function stack in Safe Mode.
Hint - Running in Safe Mode
If you\'re running into memory issues when running large function stacks or working with large data sets, you can run with Safe Mode by clicking the arrow next to the Run button and choosing **Safe Mode**.
[]
Safe Mode runs the function stack without retaining any context in memory, which can be very helpful when looping over a significant amount of data and you\'re experiencing crashes. *No context* just means that things like autocomplete won\'t work, and the output of debugging information will be limited.
Any questions, please reach out to our support team!
For assistance with either of these errors, please reach out to our support team. You can also review our documentation on memory usage to narrow down the cause.
Last updated 3 months ago
Was this helpful?