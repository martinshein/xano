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
title: Using the Testing Suite
---

# Using the Testing Suite

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'unit-tests'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Unit Tests \| Xano Documentation'
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
    Building a Unit Test
Was this helpful?
Copy
1.  Testing and Debugging
Unit Tests 
==========
Quick Summary
Unit Tests allow you to store the responses of your function stacks as a \'test\' and quickly use them to ensure that your function stacks continue to operate properly as you make changes.
Building a Unit Test
The fastest way to create a unit test is by using Run & Debug. Once you are achieving the desired result by running your function stack, you can click **Create Unit Test** under the result.
[]
You can also create a test manually at any time from the API settings menu.
[]
Give your unit test a name, a description, and the data source that it should use to run the test if different from your live data source.
[]
Unit tests are defined by your **input** and **expects**.
[]
In this example, we are providing an input of 2 and expect a response of 2.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Inputs** align with the inputs that your function stack expects. You can fill out any desired values here that you would like to use to run the test. If you used the **Create Unit Test** option in Run & Debug, this should already be populated for you.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Expects** are the statements that are used to validate your test. These could be anything from a simple equals statement, or use more complex operators based on your needs.
    :::
Your unit test can have multiple expect statements, which can be added by clicking the **+ Add an expect statement** option.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Use the ✏️ button to delete expect statements.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Use the ⏩ button to check all expect statements, or you can run them selectively with the ▶️ button.
    :::
**Unit Tests and Authentication**
When creating a unit test on a function stack that requires authentication, you can provide an auth token and extras just like you would during Run & Debug.
To avoid having to recycle the auth token upon expiration, we have added the ability to ignore auth token expiration when running your unit tests.
####  
Using the Testing Suite
Once you have your unit tests built, you can always run them individually from that API\'s testing panel. If you want to run all of your tests at once, you can use the testing suite.
[]
In the left-hand navigation menu, find your Library and click Unit Tests.
[]
Once inside the testing suite, you can perform the following actions:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Review where your application has and is missing coverage.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Run all tests at once.
    :::
For complex applications with a significant number of objects, you have the ability to dial down further into checking coverage and tests for functions, APIs, and middleware separately. You can also filter your tests by tested / untested only, or failed only, to quickly understand where your attention should be to ensure 100% coverage and success.
Mocking Responses
For each of the functions in your function stack, you can add *mock responses* to assist in the consistency of your unit tests.
<div>
1
###  
Right-click on a function and choose Mock Test Response
2
###  
In the panel that opens on the right, you can add mock data for this function that will be used during your unit test.
You can specify different pieces of data for each individual unit test you\'ve built for this function stack.
</div>
Last updated 1 month ago
Was this helpful?