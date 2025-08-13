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
title: What is a database?
---

# What is a database?

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
description: 'In this section, you\''ll learn about the basic concepts of what a database is, and how it works.'
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'database-basics'
twitter:card: summary\_large\_image
twitter:description: 'In this section, you\''ll learn about the basic concepts of what a database is, and how it works.'
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Database Basics \| Xano Documentation'
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
    What is a database?
Was this helpful?
Copy
1.  The Database
Database Basics 
===============
In this section, you\'ll learn about the basic concepts of what a database is, and how it works.
**Quick Definition**
A database is a structured collection of information that\'s organized so you can easily access, manage, and update it - like a super-powered digital filing cabinet that can instantly find and sort your data.
###  
What is a database?
Think of your database like a digital version of a filing cabinet that holds every piece of data your backend needs to run. Just as you organize papers in folders and drawers, a database organizes digital information in an organized way. This can include anything you need, such as\...
-   ::: 
    ::: 
    :::
    :::
    ::: 
    User account information (names, emails, passwords)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Product information (names, prices, descriptions)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Complex data structures, such as AI vectors, images/videos, and more
    :::
Your **database** is comprised of a few different components, detailed below.
###  
Database Tables
A table can be thought of like a drawer in your filing cabinet that is only meant to hold a certain type of information. You could have a separate drawer for users, products, and stores. Each table in Xano is comprised of a collection of **database records**.
###  
Database Records
Each table is comprised of \'records\', which you can think of as individual folders inside of that drawer. Each folder contains all of the relevant data for that record. If we were looking at a drawer that held our user data, each folder might contain information like their name, email address, password, or physical location. These separate pieces of data are our **database fields**.
###  
Database Fields
Each record will have pieces of data separated into fields, or columns (the terms can be used interchangeably). A database field has at least a name to signal what is contained in that field, and a data type associated with it that dictates what can be stored in that field.
Xano offers several different data types that you can use, and you can review those here, but for now, we\'ll focus on some of the more basic ones to get you started.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **text** - Can hold any form of text, sometimes referred to as a string
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **integer** - Any number that does not include a decimal point
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **boolean** - A true or false value
    :::
[[Field Types]]
###  
How is data added to a database table?
Typically, your data comes from one of the following sources:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Manually entering data in the database view
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    User submitted data that is sent to your Xano APIs from your frontend
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    A third party service, sending data to or being called from your Xano function stacks
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Imports from CSV files, other database platforms, or a direct database connection
    :::
Last updated 3 months ago
Was this helpful?