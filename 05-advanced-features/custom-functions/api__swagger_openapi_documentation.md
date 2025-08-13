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
title: 'API: Swagger Openapi Documentation'
---

# API: Swagger Openapi Documentation

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
    Accessing the Documentation
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Building with Visual Development
3.  APIs
Swagger (OpenAPI Documentation) 
===============================
**Quick Summary**
Swagger documentation provides a standardized way to describe and visualize APIs, showing what requests they accept and what responses they return - like a detailed menu that shows all available options. It allows developers to understand, test, and integrate with APIs without needing to read through pages of technical documentation.
Xano automatically generates documentation for your APIs using Swagger, which provides the information in a standardized format called OpenAPI. The documentation contains information like the API name, description, inputs, and expected response.
Using these standardized methods allows for easy import of your API information into other platforms, such as your frontend of choice, as well as AI chatbots and large-language models for development assistance. In addition, it provides you an easy way to send API specifications to other developers you might be working with, without giving them access to the rest of your Xano workspace.
Accessing the Documentation
Documentation is generated for each API group. At the top of the API group page, just click [] to access the auto-generated documentation for that group.
Locating the Swagger documentation
Using the Documentation
<div>
1
###  
Review the API information shown.
Each API will show you the method, the API name, and the description on the left side.
[]
On the right, you\'ll see a [🔓] icon if that API requires authentication.
[]
Click the `V` to interact with your API of choice.
2
###  
Sending Authenticated Requests
If any of the API(s) you want to interact with require authentication, click []at the top of the page to supply an authentication token.
3
###  
Click []to send a request to that API.
4
###  
Fill in any request body values or parameters necessary.
5
###  
Click [] to send the test request.
You can review the response given below.
</div>
Additional Features
###  
Defining Sample Inputs and Responses
Note
We\'re currently rolling out this feature to all users as part of our next release. If you don\'t have it yet, you will soon! Hang tight.
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
###  
Copy / Copy as cURL
Throughout the documentation, you\'ll see [] icons. These will let you quickly copy the contents of that element, and in the presence of a cURL command, copy that command to quickly paste into a terminal or other API / testing platform of choice, such as Postman.
###  
JSON OpenAPI Spec
You can click the link at the top of the page to access a JSON-formatted version of your API spec. This is useful for other external platforms that rely on this type of standardized information about your APIs or providing to AI chatbots / LLMs.
Last updated 3 months ago
Was this helpful?