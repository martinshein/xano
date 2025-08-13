---
category: filters
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: format\_timestamp
---

# format\_timestamp

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
    add\_ms\_to\_timestamp
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Filters
Timestamp 
=========
NOTE
When a filter below refers to the **parent value**, we\'re talking about the value box that lives immediately above the filter.
[]
For information on how Xano stores, reads, and formats timestamps, visit the Timestamp page.
add\_ms\_to\_timestamp
Add milliseconds to a timestamp. (negative values are ok)
The add\_ms\_to\_timestamp filter is useful when you need to make precise time adjustments at the millisecond level, such as in high-frequency data processing, animation timing, performance measurements, or working with time-sensitive operations like financial transactions.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The original timestamp (epoch in milliseconds)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    milliseconds: The number of milliseconds to add (can be negative)
    :::
Primary Value (timestamp)
Other Value (milliseconds)
Output (timestamp)
1698710400000
500
1698710400500
1698710400000
-250
1698710399750
1698710400000
1500
1698710401500
add\_secs\_to\_timestamp
Add seconds to a timestamp. (negative values are ok)
The add\_secs\_to\_timestamp filter is valuable when you need to adjust time values by seconds, such as calculating expiration times, scheduling events, determining time windows, or adjusting timestamps for different time zones.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The original timestamp (epoch in milliseconds)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    seconds: The number of seconds to add (can be negative)
    :::
Primary Value (timestamp)
Other Value (seconds)
Output (timestamp)
1698710400000
30
1698710430000
1698710400000
-60
1698710340000
1698710400000
3600
1698714000000
###  
format\_timestamp
Converts a timestamp into a human-readable formatted date based on the supplied format.
**This format follows the** **PHP DateTime::format syntax****. Please refer to the official PHP documentation for the full list of formatting characters.**
Timezone regions are listed here.
The `format_timestamp` filter is essential when displaying dates and times in user interfaces, reports, or any output where timestamps need to be presented in a human-readable format.
**Inputs:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `primary value`: The timestamp to format (epoch in milliseconds, typically UTC).
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `format`: The PHP DateTime::format string specifying how the timestamp should be displayed (e.g., `"Y-m-d H:i:s"`).
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `timezone`: The target timezone for the outputted formatted date (e.g., \"America/New\_York\").
    :::
Primary Value (timestamp)
Format String
Output (formatted string)
`1698710400000`
`"Y-m-d"`
`"2023-10-31"`
`1698710400000`
`"M j, Y h:i A"`
`"Oct 31, 2023 12:00 AM"`
`1698710400000`
`"l, F j, Y"`
`"Tuesday, October 31, 2023"`
------------------------------------------------------------------------
###  
parse\_timestamp
Parses a date/time string from various formats into an epoch millisecond timestamp (UTC).
The `parse_timestamp` filter is valuable when working with dates and times from different string sources. It allows you to convert human-readable date strings into the standard epoch millisecond timestamp format used throughout Xano for storage or further processing.
**Inputs:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `primary value`: The date/time string to parse (e.g., `"2023-10-31 14:30:00"`).
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `format`: A string specifying the format of the input date/time string, adhering to PHP\'s DateTime::createFromFormat() syntax.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `timezone`: The timezone that the input `primary value` (date/time string) should be interpreted in, especially if the string itself does not contain timezone offset information (e.g., `"America/New_York"`).
    :::
Primary Value (date string)
Format String
Output (timestamp, UTC)
`"10/31/2023"`
`m/d/Y`
`1698777018000`
`"October 31, 2023 2:30 PM"`
`F j, Y g:i A`
`1698762600000`
`"2023-10-31 14:30:15"`
`Y-m-d H:i:s`
`1698762615000`
------------------------------------------------------------------------
transform\_timestamp
Takes a timestamp and applies a relative transformation to it. Ex. -7 days, last Monday, first day of this month
The transform\_timestamp filter is useful for generating relative dates based on a reference timestamp, such as calculating \"last Monday,\" \"beginning of the month,\" or \"7 days ago\" for reporting periods, scheduling, or any scenario requiring date navigation relative to a reference point.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The reference timestamp (epoch in milliseconds)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    format: A string describing the relative transformation to apply
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    timezone: The timezone to provide the formatted timestamp in
    :::
Primary Value (timestamp)
Other Value (transformation)
Output (timestamp)
1698710400000
\"-7 days\"
1698105600000
Last updated 2 months ago
Was this helpful?