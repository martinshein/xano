---
category: database
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/database
tags:
- authentication
- api
- webhook
- trigger
- query
- filter
- middleware
- expression
- realtime
- transaction
- function
- background-task
- custom-function
- rest
- database
title: 'apple-mobile-web-app-status-bar-style: black'
---

---
apple-mobile-web-app-status-bar-style: black

color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'designing-your-database'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'

viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---

[![](../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)![](../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)](../index.html)















-   

    
    -   Using These Docs
    -   Where should I start?
    -   Set Up a Free Xano Account
    -   Key Concepts
    -   The Development Life Cycle
    -   Navigating Xano
    -   Plans & Pricing

-   

    
    -   Building with Visual Development
        
        -   APIs
            
            -   [Swagger (OpenAPI Documentation)](../the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../the-function-stack/building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../the-function-stack/building-with-visual-development/background-tasks.html)
        -   [Triggers](../the-function-stack/building-with-visual-development/triggers.html)
        -   [Middleware](../the-function-stack/building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../the-function-stack/building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../the-function-stack/building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](../the-function-stack/functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](../the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../the-function-stack/functions/database-requests/get-record.html)
            -   [Add Record](../the-function-stack/functions/database-requests/add-record.html)
            -   [Edit Record](../the-function-stack/functions/database-requests/edit-record.html)
            -   [Add or Edit Record](../the-function-stack/functions/database-requests/add-or-edit-record.html)
            -   [Patch Record](../the-function-stack/functions/database-requests/patch-record.html)
            -   [Delete Record](../the-function-stack/functions/database-requests/delete-record.html)
            -   [Bulk Operations](../the-function-stack/functions/database-requests/bulk-operations.html)
            -   [Database Transaction](../the-function-stack/functions/database-requests/database-transaction.html)
            -   [External Database Query](../the-function-stack/functions/database-requests/external-database-query.html)
            -   [Direct Database Query](../the-function-stack/functions/database-requests/direct-database-query.html)
            -   [Get Database Schema](../the-function-stack/functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../the-function-stack/functions/data-manipulation/create-variable.html)
            -   [Update Variable](../the-function-stack/functions/data-manipulation/update-variable.html)
            -   [Conditional](../the-function-stack/functions/data-manipulation/conditional.html)
            -   [Switch](../the-function-stack/functions/data-manipulation/switch.html)
            -   [Loops](../the-function-stack/functions/data-manipulation/loops.html)
            -   [Math](../the-function-stack/functions/data-manipulation/math.html)
            -   [Arrays](../the-function-stack/functions/data-manipulation/arrays.html)
            -   [Objects](../the-function-stack/functions/data-manipulation/objects.html)
            -   [Text](../the-function-stack/functions/data-manipulation/text.html)
                    -   [Security](../the-function-stack/functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../the-function-stack/functions/apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../the-function-stack/functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../the-function-stack/functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../the-function-stack/functions/data-caching-redis.html)
        -   [Custom Functions](../the-function-stack/functions/custom-functions.html)
        -   [Utility Functions](../the-function-stack/functions/utility-functions.html)
        -   [File Storage](../the-function-stack/functions/file-storage.html)
        -   [Cloud Services](../the-function-stack/functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](../the-function-stack/filters/manipulation.html)
        -   [Math](../the-function-stack/filters/math.html)
        -   [Timestamp](../the-function-stack/filters/timestamp.html)
        -   [Text](../the-function-stack/filters/text.html)
        -   [Array](../the-function-stack/filters/array.html)
        -   [Transform](../the-function-stack/filters/transform.html)
        -   [Conversion](../the-function-stack/filters/conversion.html)
        -   [Comparison](../the-function-stack/filters/comparison.html)
        -   [Security](../the-function-stack/filters/security.html)
            -   Data Types
        
        -   [Text](../the-function-stack/data-types/text.html)
        -   [Expression](../the-function-stack/data-types/expression.html)
        -   [Array](../the-function-stack/data-types/array.html)
        -   [Object](../the-function-stack/data-types/object.html)
        -   [Integer](../the-function-stack/data-types/integer.html)
        -   [Decimal](../the-function-stack/data-types/decimal.html)
        -   [Boolean](../the-function-stack/data-types/boolean.html)
        -   [Timestamp](../the-function-stack/data-types/timestamp.html)
        -   [Null](../the-function-stack/data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](../the-function-stack/additional-features/response-caching.html)
        
-   
    Testing and Debugging
    
    -   Testing and Debugging Function Stacks
    -   Unit Tests
    -   Test Suites

-   
    The Database
    
    -   Getting Started Shortcuts
    -   Designing your Database
    -   Database Basics
        
        -   [Using the Xano Database](database-basics/using-the-xano-database.html)
        -   [Field Types](database-basics/field-types.html)
        -   [Relationships](database-basics/relationships.html)
        -   [Database Views](database-basics/database-views.html)
        -   [Export and Sharing](database-basics/export-and-sharing.html)
        -   [Data Sources](database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](database-performance-and-maintenance/storage.html)
        -   [Indexing](database-performance-and-maintenance/indexing.html)
        -   [Maintenance](database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](../ai-tools/mcp-builder/mcp-functions.html)
            -   Xano MCP Server

-   
    Build With AI
    
    -   Using AI Builders with Xano
    -   Building a Backend Using AI
    -   Get Started Assistant
    -   AI Database Assistant
    -   AI Lambda Assistant
    -   AI SQL Assistant
    -   API Request Assistant
    -   Template Engine
    -   Streaming APIs

-   
    File Storage
    
    -   File Storage in Xano
    -   Private File Storage

-   
    Realtime
    
    -   Realtime in Xano
    -   Channel Permissions
    -   Realtime in Webflow

-   
    Maintenance, Monitoring, and Logging
    
    -   Statement Explorer
    -   Request History
    -   Instance Dashboard
        
        -   Memory Usage
        
-   
    Building Backend Features
    
    -   User Authentication & User Data
        
        -   [Separating User Data](../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
            -   Webhooks
    -   Messaging
    -   Emails
    -   Custom Report Generation
    -   Fuzzy Search
    -   Chatbots

-   
    Xano Features
    
    -   Snippets
    -   Instance Settings
        
        -   [Release Track Preferences](../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../xano-features/metadata-api/content.html)
        -   [Search](../xano-features/metadata-api/search.html)
        -   [File](../xano-features/metadata-api/file.html)
        -   [Request History](../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../xano-features/metadata-api/token-scopes-reference.html)
        
-   
    Xano Transform
    
    -   Using Xano Transform

-   
    Xano Actions
    
    -   What are Actions?
    -   Browse Actions

-   
    Team Collaboration
    
    -   Realtime Collaboration
    -   Managing Team Members
    -   Branching & Merging
    -   Role-based Access Control (RBAC)

-   
    Agencies
    
    -   Xano for Agencies
    -   Agency Features
        
        -   [Agency Dashboard](../agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](../agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](../agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](../agencies/agency-features/agency-profile.html)
        -   [Commission](../agencies/agency-features/commission.html)
        -   [Private Marketplace](../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](../enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](../enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](../enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
-   
    Special Pricing
    
    -   Students & Education
    -   Non-Profits

-   
    Security
    
    -   Best Practices

[Powered by GitBook]

On this page

-   
    
    [Table Relationships](#table-relationships)

-   [Database Fields](#database-fields)

-   [Planning for the Future](#planning-for-the-future)

Was this helpful?

Copy

1.  [The Database](getting-started-shortcuts.html)

Designing your Database 
=======================

**Quick Summary**

Good database design starts with organizing your information into logical groups, like putting customer details in one table and order history in another. These groups are then connected through common identifiers using a table reference field - like a customer ID that links a person to all their orders - which helps maintain accuracy and avoid duplicating information.

Think of designing a database like organizing your home. Before you buy storage containers or rearrange your furniture, you need a plan. The same goes for databases - careful planning prevents headaches later.

[**Hint**]

Use a tool like [**Excalidraw**](https://excalidraw.com/) to help you when designing your database.

Start by listing everything you need to store. If you\'re building a bookstore database, you\'ll need to track books, authors, customers, and sales. Just like you wouldn\'t store your kitchen items in your bathroom, each type of information needs its own logical home in the database.

![](../_gitbook/image4cc7.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FbYkpMp4eDyBJsYcIJ9x6%252FCleanShot%25202024-12-14%2520at%252012.56.18.png%3Falt%3Dmedia%26token%3Dd07aa586-87c8-4823-8316-760ba6bbf85a&width=768&dpr=4&quality=100&sign=92488c32&sv=2)

Using Excalidraw to begin the database design process.

Let\'s draw these to look like individual items --- these will represent the tables that we\'ll create.

![](../_gitbook/image66c9.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8TS57szni2Svwd9G4CZ6%252FCleanShot%25202024-12-14%2520at%252012.57.04.png%3Falt%3Dmedia%26token%3D24371295-06ab-450b-b4fc-05c7308ee61f&width=768&dpr=4&quality=100&sign=8bd639ba&sv=2)

 

Table Relationships

To illustrate multiple examples, we\'ve added a **Publishers** table to our visualization.

Consider how these pieces connect. A book has one or more authors, and an author can write multiple books. A customer can buy many books, and a book can be bought by many customers. These relationships are crucial - they\'re like the hallways connecting rooms in your house, allowing you to move naturally between related information.

**One-to-One**

-   
    
        
    
    Each thing on one side matches exactly one thing on the other side. Like a person and their social security number: one person has one number, and each number belongs to one person
    
**One-to-Many**

-   
    
        
    
    One thing on one side can connect to multiple things on the other side, but those multiple things each only connect back to one thing. Like a mother and her children: one mother can have many children, but each child has only one mother
    
**Many-to-Many**

-   
    
        
    
    Things on both sides can connect to multiple things on the other side. Like students and classes: one student takes many classes, and each class has many students
    
For our book store example, let\'s visualize the relationships between our tables.

 

Database Fields

**Think about the essential characteristics that describe each thing**. Just like how a person\'s profile might include their name, birthday, and contact info, each table should contain the core pieces of information that defines that thing. When referring to all of the fields in a database table as a whole, we\'ll call this **schema**.

Let\'s use our bookstore example:

-   
    
        
    
    For Books: You\'ll want the ISBN (like a book\'s fingerprint), title, publication date, current price, and maybe format (hardcover/paperback). You don\'t need to store the author\'s name here - that\'s what the connection to the Authors table is for.
    
-   
    
        
    
    For Authors: You\'ll store their name, perhaps birth date, nationality, and a brief biography. You don\'t need to store a list of their books - the relationship between tables handles that.
    
-   
    
        
    
    For Customers: You\'ll want their name, contact information, shipping addresses, and maybe their preferences or a membership status. You don\'t need to store their purchase history here - that\'s tracked through the Sales table.
    
**\"Does this information describe the core thing I\'m tracking, or is it really about something else?\"**
If you find yourself wanting to store a list of things (like \"all books by this author\" or \"all orders from this customer\"), that\'s usually a sign you need a relationship between tables rather than storing that data directly.

**Consider whether the information might change over time**.
For example, book prices change frequently, so you might want both a \"currentPrice\" in the Books table and a \"salePrice\" in the Sales Items table. This lets you track both what a book costs now and what customers actually paid for it in the past.

**Watch out for duplicate information.**
If you\'re storing an author\'s contact details, store them once and reference them when needed, rather than copying them into every book record. This is like having one toolbox in your garage instead of keeping duplicate tools in every room. In Xano, this is accomplished with [table reference fields](database-basics/field-types.html#table-reference).

**How many fields is \'too many\'?**
This is not a black-and-white question to answer. Some tables can have a significant number of fields, but the dataset is small --- this is usually okay. If you expect this table to grow in size over time, it\'s always better to split data types into separate tables --- for example, if users have companies attached, you should probably store those companies in a separate table and use [relationships](designing-your-database.html#table-relationships).

 

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