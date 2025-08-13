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
title: Timestamps
---

# Timestamps

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: timestamp
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Timestamp \| Xano Documentation'
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
    Timestamps
-   
    What are my options for inputting a timestamp into Xano through the API?
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Data Types
Timestamp 
=========
###  
Timestamps
<div>
</div>
Xano stores timestamps as a **unix timestamp in milliseconds**. Unix timestamp is a way to track time as a running total of seconds. This count starts at the Unix Epoch on January 1st, 1970 at UTC.
For example:
1604959474 seconds since Jan 01 1970. (UTC).
This epoch translates to 11/09/2020 @ 10:04pm (UTC).
Since Xano uses milliseconds, the timestamp would be **1604959474000**.
There is **no timezone in a timestamp** because it is the number of milliseconds from the unix epoch - Jan 1, 1970.
###  
**What is the difference between a timezone region, a timezone abbreviation, and a timezone offset?**
A **timezone region** handles daylight savings time for you. For example:
America/Los\_Angeles will automatically be PST or PDT depending on the actual timestamp. It handles this behind the scenes so you always have the right timezone offset.
Timezone regions are listed here.
A **timezone abbreviation** is the shortened 3 letter abbreviation (PST, PDT, etc.).
This represents a **timezone offset**:
PST is -0800 and PDT is -0700. These values are always the same.
It is recommended to use the timezone region mentioned above so you don't need to keep changing the abbreviation selection with daylight savings time changes.
###  
**When I choose a time from the database table viewer, what timezone is used there?**
The database table view is using the unix timestamp internally but transforming it in the spreadsheet view to the timezone of your browser. This means that if someone else was looking at it from a different timezone, they would see the time that is local to themselves. However, you can change the browser default settings to your preferences for the date & time format and timezone offset that is shown in your database on the account page.
###  
**What are my options for inputting a timestamp into Xano through the API?**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Raw timestamp** in milliseconds (this would not need any timezone information). For example:
    1604959474000
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **ISO 8601** format, which is Year-Month-Day then a "T" and then 24hour-minute-second then "the timezone offset in hours and minutes":
    2004-02-12T15:19:21+00:00
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Postgres** database format, which is similar to the ISO 8601 format:
    2020-11-09 14:13:18-0800
    (Note: a space is used to separate the date from the time instead of the "T" character in ISO 8601. Also, the offset does not include the colon.)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Relative time**. Xano uses relative time formats from php.net. For example:
    now, last Monday, +7 days, etc.
    (Relative times normally don't have any timezone information, so it will often be important to reference the timezone in any type of filter.)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Parse Timestamp** the parse\_timestamp filter allows you to take a human-readable time format and parse it into a Unix timestamp in milliseconds to be stored in the Xano database. The characters used are the same as formatting date and time and can be found here from php.net.
    :::
###  
**What are my options with formatting date and time?**
There are lots of options available. A full list is available here from php.net.
Here are a just few examples:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    c = 2004-02-12T15:19:21+00:00
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    r = Thu, 21 Dec 2000 16:01:07 +0200
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Y-m-d H:i:s = 2000-01-01 00:00:00
    :::
See the Timestamp Filters page to see how to use timestamp filters in Xano.
Last updated 6 months ago
Was this helpful?