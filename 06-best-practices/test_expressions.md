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
title: Test Expressions
---

# Test Expressions

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'test-suites'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Test Suites \| Xano Documentation'
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
    What is Workflow Testing?
Was this helpful?
Copy
1.  Testing and Debugging
Test Suites 
===========
Workflow Testing allows you to create sets of different tests to validate user flows are working as expected.
What is Workflow Testing?
Workflow Testing in Xano allows you to quickly build sets of tests that you can use to make sure a specific flow is working as expected. You can think of a \'flow\' as a set of separate actions, such as multiple APIs that a user might hit when utilizing your application, or data processing across multiple function stacks.
Workflow Testing allows you to validate these sets or flows with a single click and get instant visibility into your backend functionality.
How do I build workflow tests?
From the left-hand navigation menu, choose **Library** \> **Workflow Tests** []
Choose **Add Workflow Test** in the top-right corner. In the panel that opens, you can give your test a name, description, and add tags for easy access later.
[]
Click the [] button to add a step to your Workflow Test. We\'ve introduced some new functions to assist you in building your tests.
**Run Stacks**
Run stacks are functions you can add to your workflow tests to run other function stacks, such as APIs, custom functions, and middleware.
Function Name
Use Case
Run API Endpoint
Sends a request to one of your API endpoints and returns the result
Run Addon
Runs an addon
Run Function
Runs a custom function and returns the result
Run Middleware
Runs a middleware and returns the result
Run Trigger
Runs a trigger and returns the result
Run Task
Runs a background task and returns the result
####  
Test Expressions
Test Expressions are functions used typically in conjunction with a Run Stack to determine if the output of a Run Stack is valid.
Function Name
Use Case
Expect a variable to be defined
Expect a variable to not be defined
Checks to see if a variable has been defined.
**Example**:
You have an API that returns a `user` object with a name key inside of it. You can use this to check if `user.name` is defined.
Expect variable to be empty
Checks to see if a variable exists, but is empty.
**Example:**
You are calling an external API that is used to process data. If the API call is successful, you know that `response.result` is empty because the API just returns a status code informing you that the job is being processed.
Expect variable to be false
Expect variable to be true
Checks to see if a variable with a boolean data type is returning `false` or `true`
Expect variable to be greater than
Expect variable to be less than
Expect variable to equal
Expect a variable to not equal
Expect variable to be within
Checks to see if a variable matches the specific condition, such as \>, \<, =, or is within a certain range.
Expect variable to be null
Checks to see if a variable contains a `null` value
Expect variable to start with
Expect variable to end with
Checks to see if the value inside of a variable starts or ends with a specific value
Expect function to throw
Checks a function to see if it throws an error
Expect function to match
Checks to see if the output of a variable matches a regular expression
###  
Using Workflow Tests
In this example, we\'ve built a workflow test to make sure our login flow works as expected.
[]
We\'ve added a **Run Stack** function to run our auth/login endpoint, and provided it with a username and password.
After that, our **Test Expression** checks to make sure that the login function is returning an authToken, which is what our login endpoint returns if a valid username and password is provided. When we click [] we can see that our test passes!
[]
If we modify our **Run API Endpoint** run stack to provide an invalid password, we can see that by running our test again, we get an error. This test has failed because an authToken was not returned.
[]
From the main **Workflow Tests** page, we can run each of our tests by clicking the individual []buttons, or we can click []to run all of our workflow tests at once.
We can see by running all of our workflow tests the following information:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    We have **38% coverage**. This means that out of all of the function stacks that exist across our backend, 3/8 of them are used in our tests.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    We have **50% success**. This means that out of all of our workflow tests, half of them are successful.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    To run all of our tests takes less than a second.
    :::
[]
####  
Additional Information
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Click the [] icon next to a workflow test to clone or delete it.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    When adding a Run Stack, you can click the [] icon to open that function stack being tested in a new window or tab and quickly make changes.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    When you test a function stack that currently is in draft mode, your workflow test will run the drafted version.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You can change the data source that all of your workflow test\'s functions run against by clicking the [] button at the top of the workflow test function stack.
    :::
Databases in Workflow Tests
Selecting a Data Source for a Workflow Test
When you select a data source for your Workflow Test, it\'s important to note that a **copy** of the database is generated to ensure that no live data is impacted. This usually means that selecting your live database is not recommended --- if your database is large in size, this can cause complications during testing.
It is recommended to use separate Data Sources for running tests.
Last updated 3 months ago
Was this helpful?