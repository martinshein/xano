---
category: database
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Access your data sources from the left-side navigation menu
---

# Access your data sources from the left-side navigation menu

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'data-sources'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Data Sources \| Xano Documentation'
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
-   ::: 
    :::
    Creating Data Sources
Was this helpful?
Copy
1.  The Database
2.  Database Basics
Data Sources 
============
**Quick Summary**
Data sources are like separate versions of tables that contain different data sets --- typically, they are separated into **live** or **production** data, and **test** data. The advantage to using separate data sources is so when you are building or iterating on your backend functionality, your actual live data stays safe. All data sources share the same database schema. They only differ by allowing different copies of the database records.
In Xano, data sources are essentially different sets of tables within your application\'s database. These data sources are crucial because they provide a way to separate the actual, live data that your business relies on from the data you use for testing or development purposes. This separation is beneficial as it ensures that any changes you make while testing new features do not affect the actual operational data.
Data sources typically have two main variants: **live data** and **test data**. You can have as many data sources as you\'d like if additional separation makes sense for your backend. Live data is what your application uses in real-time---it's the actual data that reflects real-world activities. In contrast, test data is used for experimentation and development, allowing developers to try out new features or changes without risking the integrity of the live data. By keeping these data sources distinct, Xano enables businesses to safely innovate and enhance their backend functionality without compromising the data they depend on every day.
Creating Data Sources
<div>
1
###  
Access your data sources from the left-side navigation menu
2
###  
Add a new data source from the panel that opens
[]
3
###  
Customize the new data source
Give it a name, and choose a distinct color to assign to the data source. The color assigned is important, as it is used throughout the Xano interface to remind you of the currently selected data source.
When you\'re done, click []
</div>
------------------------------------------------------------------------
Using Data Sources
###  
Switching Data Sources
When you switch data sources, any action you take in Xano such as running and debugging a function stack will target the selected data source. It is recommended to use a test data source whenever possible to avoid accidentally impacting live application data.
Switch your data source at any time by clicking the data source indicator in the left-side navigation.
This **does not** impact your live application; only the work you are performing inside of Xano.
###  
Setting a Data Source as Active
If you want your backend to use a different data source by default, select it from the data sources panel and choose []. All future activity, unless otherwise specified using one of the alternative methods below, will use the active data source.
Proceed with caution. Changing the active data source can have unintended consequences on your live application. You do not need to change the **active data source** to work with other data sources in Xano.
###  
Targeting Specific Data Sources
When running function stacks in Xano or calling them externally, you can target a specific data source a number of ways. If you do not specify a data source, Xano will use the
<div>
1
###  
Use the Set Data Source function
The **Set Data Source** function, located under **Utility Functions**, allows you to manually set a data source at any time. Any future database operations, such as reads and writes, will use the defined data source.
2
###  
Send a data source header in your request
If you\'re calling one of your Xano APIs externally, you can specify the data source to use in the request headers.
The header to send is as follows. Replace \'test\' with the name of the data source you wish to target.
Copy
``` 
X-Data-Source: test
```
3
###  
Send a URL argument in your request
If you don\'t have the ability to modify the request headers but still want to specify the data source in an external request, you can use a URL argument.
Copy
``` 
https://x1xx-abcd-efgh.a1.xano.io/api:x123abc/user?x-data-source=test
```
4
###  
Change the settings of the function stack
In some function stack types, such as background tasks, you can set the data source to target if you would like it to be different from the live data source.
</div>
###  
Migrating Data Between Data Sources
<div>
1
###  
Access the Migration panel
Click the data sources indicator and choose [⚙️] **Manage Data Sources**. In the panel that opens, click Migrate.
2
###  
Select the source and destination data source.
3
###  
Select the tables to migrate.
4
###  
Confirm your changes to begin the migration.
You can check the progress of the migration via the indicator in the left-hand navigation. You\'ll also see a banner at the top of the screen once the migration has completed.
</div>
Last updated 7 months ago
Was this helpful?

## Code Examples

```
 
X-Data-Source: test

```

```
 
https://x1xx-abcd-efgh.a1.xano.io/api:x123abc/user?x-data-source=test

```

