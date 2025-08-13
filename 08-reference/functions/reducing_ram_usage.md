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
title: Reducing RAM Usage
---

# Reducing RAM Usage

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'memory-usage'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Memory Usage \| Xano Documentation'
viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---
[](../../index.html)
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
In this screenshot, we can see that this instance\'s Lambda RAM isn\'t showing steady utilization \-- there are significant peaks, valleys, and spikes. This tells us that there is sporadic intense load with Lambda functions we are using, and it will likely cause problems such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Temporary system restarts and downtime
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Slow performance
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Failed requests
    :::
This is something that should be investigated further.
####  
Reducing RAM Usage
If you are finding yourself in a situation where you are experiencing symptoms of RAM exhaustion, there are a few things you can to do try and mitigate the situation.CommentIt\'s important to note that in some cases, when mitigation is not possible, that may signal it\'s time to upgrade your Xano subscription tier to increase your available RAM. You can always reach out to Xano Support for further clarification.C
**Database RAM**
Spikes in Database RAM can be caused by one or more of the following:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Tables that contain fields with large amounts of data, such as JSON payloads or sizable text content
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Try moving these large fields to a separate table or determining if you can reduce the amount of data stored.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Depending on how often the data needs to be accessed, you can also store the large data in text files and store the file path in the table instead.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Table references to other tables with a high number of fields
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Use the Auto Complete setting on the referenced table to reduce the amount of data loaded when viewing the table
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Running queries with joins on large tables
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Make sure you are using proper indexing on large tables
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Use pagination on your base query
        :::
    :::
**API RAM**
Spikes in API RAM can be caused by one or more of the following:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Function stacks that process large volumes of data
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Clear the contents of variables as they become unnecessary by updating them to blank values
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Move large data processing jobs to background tasks​
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Use post processing to execute any functions that aren\'t necessary to deliver a response
        :::
    :::
**Lambda RAM**
Please note that when using Lambda functions, the contents of **all variables** are loaded into Lambda memory. This is most often the cause of memory issues when using Lambda functions.
Spikes in Lambda RAM can be caused by one or more of the following:Comment
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Contents of other variables are too large for the Lambda to handle during processing
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Using file resources in conjunction with Lambdas
    :::
To mitigate issues with Lambda RAM, try using expressions instead.
**Redis RAM**
Spikes in Redis RAM can be caused by one or more of the following:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Heavy and/or inappropriate reliance on data caching functions
    :::
If you are not using data caching functions and still experiencing spikes in Redis RAM, please reach out to support.
**Tasks RAM**
Spikes in task RAM should be handled as you would handle spikes in API RAM.
Last updated 6 months ago
Was this helpful?