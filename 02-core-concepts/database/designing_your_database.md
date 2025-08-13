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
title: Designing Your Database
---

# Designing Your Database

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'designing-your-database'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Designing your Database \| Xano Documentation'
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
    Table Relationships
Was this helpful?
Copy
1.  The Database
Designing your Database 
=======================
**Quick Summary**
Good database design starts with organizing your information into logical groups, like putting customer details in one table and order history in another. These groups are then connected through common identifiers using a table reference field - like a customer ID that links a person to all their orders - which helps maintain accuracy and avoid duplicating information.
Think of designing a database like organizing your home. Before you buy storage containers or rearrange your furniture, you need a plan. The same goes for databases - careful planning prevents headaches later.
[**Hint**]
Use a tool like **Excalidraw** to help you when designing your database.
Start by listing everything you need to store. If you\'re building a bookstore database, you\'ll need to track books, authors, customers, and sales. Just like you wouldn\'t store your kitchen items in your bathroom, each type of information needs its own logical home in the database.
Using Excalidraw to begin the database design process.
Let\'s draw these to look like individual items --- these will represent the tables that we\'ll create.
Table Relationships
To illustrate multiple examples, we\'ve added a **Publishers** table to our visualization.
Consider how these pieces connect. A book has one or more authors, and an author can write multiple books. A customer can buy many books, and a book can be bought by many customers. These relationships are crucial - they\'re like the hallways connecting rooms in your house, allowing you to move naturally between related information.
**One-to-One**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Each thing on one side matches exactly one thing on the other side. Like a person and their social security number: one person has one number, and each number belongs to one person
    :::
**One-to-Many**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    One thing on one side can connect to multiple things on the other side, but those multiple things each only connect back to one thing. Like a mother and her children: one mother can have many children, but each child has only one mother
    :::
**Many-to-Many**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Things on both sides can connect to multiple things on the other side. Like students and classes: one student takes many classes, and each class has many students
    :::
For our book store example, let\'s visualize the relationships between our tables.
Database Fields
**Think about the essential characteristics that describe each thing**. Just like how a person\'s profile might include their name, birthday, and contact info, each table should contain the core pieces of information that defines that thing. When referring to all of the fields in a database table as a whole, we\'ll call this **schema**.
Let\'s use our bookstore example:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    For Books: You\'ll want the ISBN (like a book\'s fingerprint), title, publication date, current price, and maybe format (hardcover/paperback). You don\'t need to store the author\'s name here - that\'s what the connection to the Authors table is for.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    For Authors: You\'ll store their name, perhaps birth date, nationality, and a brief biography. You don\'t need to store a list of their books - the relationship between tables handles that.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    For Customers: You\'ll want their name, contact information, shipping addresses, and maybe their preferences or a membership status. You don\'t need to store their purchase history here - that\'s tracked through the Sales table.
    :::
**\"Does this information describe the core thing I\'m tracking, or is it really about something else?\"**
If you find yourself wanting to store a list of things (like \"all books by this author\" or \"all orders from this customer\"), that\'s usually a sign you need a relationship between tables rather than storing that data directly.
**Consider whether the information might change over time**.
For example, book prices change frequently, so you might want both a \"currentPrice\" in the Books table and a \"salePrice\" in the Sales Items table. This lets you track both what a book costs now and what customers actually paid for it in the past.
**Watch out for duplicate information.**
If you\'re storing an author\'s contact details, store them once and reference them when needed, rather than copying them into every book record. This is like having one toolbox in your garage instead of keeping duplicate tools in every room. In Xano, this is accomplished with table reference fields.
**How many fields is \'too many\'?**
This is not a black-and-white question to answer. Some tables can have a significant number of fields, but the dataset is small --- this is usually okay. If you expect this table to grow in size over time, it\'s always better to split data types into separate tables --- for example, if users have companies attached, you should probably store those companies in a separate table and use relationships.
Planning for the Future
**Think about what information you\'ll need to find quickly.**
Just as you might keep frequently used items in easily accessible drawers, consider what data you\'ll search for most often. This helps you decide how to organize and[ ][index][ ]your information.
**Think about how information might expand in the future.**
Initially, you might only need basic book formats (hardcover and paperback). But what happens when you want to add audiobooks? You\'ll need new fields like runtime, narrator, and audio format. Instead of hard-coding format types, you could create a separate formats table, and use a table reference in your books table that lets you add new types without changing your core structure.
Suppose you create a database table for storing book formats directly within the books table:
**Books Table**
BookID
Title
Author
Hardcover
Paperback
Audiobook
This design is inflexible because each time you introduce a new format, you must alter the table structure. Instead, use a separate formats table and establish a relationship with the books table.
**Books Table**
BookID
Title
Author
**Formats Table**
FormatID
FormatType
**BookFormats Table**
BookID
FormatID
This flexible table design allows you to add new formats easily without changing the core structure.
**Finally, remember that simple is usually better.**
Like a well-organized home where everything has its place, a good database design should feel natural and intuitive. If you find yourself creating complicated structures to store simple information, step back and reconsider your approach.
Remember: **A well-designed database makes everything else easier.**
Last updated 3 months ago
Was this helpful?