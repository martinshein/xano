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
title: Types of Relationships
---

# Types of Relationships

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
description: Database Relationships are used to define related data between one or more tables.
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: relationships
twitter:card: summary\_large\_image
twitter:description: Database Relationships are used to define related data between one or more tables.
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Relationships \| Xano Documentation'
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
    What are database relationships?
Was this helpful?
Copy
1.  The Database
2.  Database Basics
Relationships 
=============
Database Relationships are used to define related data between one or more tables.
**Quick Definition**
Database relationships show how different tables of data connect to each other - like how a customer\'s ID links their personal information to their complete order history. These relationships can be one-to-one (one person, one social security number), one-to-many (one customer, many orders), or many-to-many (many students can take many classes).
What are database relationships?
Database relationships are crucial connections that link pieces of data across different tables in a database. Imagine it like a web of information where each piece is connected in a logical way.
For example, consider a library: each book has one unique ISBN, which is similar to a one-to-one relationship. Many books can belong to one category, which reflects a one-to-many relationship. Finally, readers may borrow many books, and many copies of a book can be borrowed by different readers, representing a many-to-many relationship. These connections help in organizing data efficiently, allowing more straightforward retrieval and management of the information stored.
Typically, when discussing database relationships, you\'ll see two terms that are important to remember:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Primary Key -** The primary key inside of a database table is the key that\'s used to maintain uniqueness between records --- a value that\'s always different for each record. Usually, this is an `id` field.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Foreign Key** - The foreign key inside of a database table refers to a field that references a primary key inside of another table. For example, a table of `books` might have a field that contains foreign keys from an `authors` table.
    :::
###  
Types of Relationships
In Xano, there are three primary ways tables can be related:
####  
1\. One-to-One
This is like a person and their unique passport. Each data entry in one table relates to exactly one entry in another table.
####  
2\. One-to-Many
Think of a parent and their children. A single entry in one table can relate to multiple entries in another. For example, one teacher can teach many students.
####  
3\. Many-to-Many
Similar to students enrolling in various courses, any entry in one table can relate to multiple entries in another.
------------------------------------------------------------------------
Why Use Relationships?
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Data Consistency**: Ensures all references are valid.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Reduced Redundancy**: Minimizes repeated data.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Efficient Data Retrieval**: Makes it easier to access related data.
    :::
Understanding these basic concepts can simplify how you view databases and highlight why tools like Xano are powerful for managing data.
------------------------------------------------------------------------
Using the Table Reference Field Type
When you add a table reference field to a database table, that field simply stores the IDs of the record(s) being referenced; the data is not actually duplicated. To access the actual data is typically done via an add-on as part of a function stack.
###  
Auto-Complete
Auto-Complete allows you to configure how the referenced records look inside of other tables.
For this example, we have two tables: `user` and `userRole`
<div>
1
###  
Navigate to the table you are referencing data from to adjust the Auto-Complete settings.
2
###  
Click the three dots in the top right and choose Auto-Complete
3
###  
Click \'Customize\' if this is your first time enabling Auto-Complete customization on this table.
4
###  
Click \'Add Column\' to add a new field that will appear on tables that reference this one.
</div>
------------------------------------------------------------------------
Relationship View
You can quickly observe all of your table relationships (that utilize the table reference field to contain the foreign keys of other records) by selecting the \"Show table relationships\" option when viewing your database tables.
From this view, you can visualize all of your table relationships, and click/drag the tables to organize the view based on your preferences.
^*Please\ note\ that\ customization\ in\ this\ view\ are\ not\ saved.*^
Last updated 1 month ago
Was this helpful?