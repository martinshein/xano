---
category: database
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: How can I check my CSV file format?
---

# How can I check my CSV file format?

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'csv-import-and-export'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'CSV Import & Export \| Xano Documentation'
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
    :::
    :::
    ::: 
    The first row must contain the column names - not the file name or any other data.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The second row begins the values. They should be in the same order as the columns they belong to.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Each row should have the same amount of values as there are columns.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Enclosure characters** are required when working with text strings that contain quotation marks. This is because if a quotation mark is detected, this is typically something that would mark the beginning or end of a value. You can use a **double quote (\"\")** to dictate if a value should contain this quotation mark somewhere inside the value.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    CSV files should be UTF-8 encoded. If you\'re having trouble importing your CSV properly in Xano and have determined you are using both the proper separator and enclosure characters, please make sure your file us UTF-8 encoded. This ensures that there are no special characters that might not be supported in Xano.
    :::
UTF-8 Encoding in Notepad (Windows)
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Open your file in Notepad.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click File \> Save As\...
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click \"Save As Type\", and choose All Files.
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click \"UTF-8\" in the Encoding dropdown.
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    Save the file.
    :::
**UTF-8 Encoding in Google Sheets (All platforms)**
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Open your file in Google Sheets
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click File \> Download \> Comma separated values (CSV)
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    The file will be downloaded in CSV format using UTF-8 encoding.
    :::
UTF-8 Encoding in Numbers (Mac)
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Open your file in Numbers
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click File \> Export To\... \> CSV
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    In the \"Text Encoding\" dropdown, choose UTF-8
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Save the file.
    :::
<div>
</div>
160B
<div>
Xano-Sample-CSV.csv
</div>
**Here is a sample CSV file demonstrating both the proper separator and enclosure characters.**
####  
How can I check my CSV file format?
You can review the format of your CSV file format in a number of ways. Open the file in Text Editor, Visual Studio Code, or another code editor. You can also do an online search for CSV file format validators and use an online service.
**How can I edit my CSV file format?**
Tools like Text Editor, Visual Studio Code, and other code editors allow you to make any necessary edits to your file and save the changes. When opening the file from your computer, right click and choose open with to choose from the different options available on your computer.
Last updated 1 month ago
Was this helpful?