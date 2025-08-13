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
title: 'csv-import-and-export'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'

viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---

[![](../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)![](../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)](../../index.html)















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
            
            -   [Swagger (OpenAPI Documentation)](../../the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../../the-function-stack/building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../../the-function-stack/building-with-visual-development/background-tasks.html)
        -   [Triggers](../../the-function-stack/building-with-visual-development/triggers.html)
        -   [Middleware](../../the-function-stack/building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../../the-function-stack/building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../../the-function-stack/building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](../../the-function-stack/functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](../../the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../../the-function-stack/functions/database-requests/get-record.html)
            -   [Add Record](../../the-function-stack/functions/database-requests/add-record.html)
            -   [Edit Record](../../the-function-stack/functions/database-requests/edit-record.html)
            -   [Add or Edit Record](../../the-function-stack/functions/database-requests/add-or-edit-record.html)
            -   [Patch Record](../../the-function-stack/functions/database-requests/patch-record.html)
            -   [Delete Record](../../the-function-stack/functions/database-requests/delete-record.html)
            -   [Bulk Operations](../../the-function-stack/functions/database-requests/bulk-operations.html)
            -   [Database Transaction](../../the-function-stack/functions/database-requests/database-transaction.html)
            -   [External Database Query](../../the-function-stack/functions/database-requests/external-database-query.html)
            -   [Direct Database Query](../../the-function-stack/functions/database-requests/direct-database-query.html)
            -   [Get Database Schema](../../the-function-stack/functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../../the-function-stack/functions/data-manipulation/create-variable.html)
            -   [Update Variable](../../the-function-stack/functions/data-manipulation/update-variable.html)
            -   [Conditional](../../the-function-stack/functions/data-manipulation/conditional.html)
            -   [Switch](../../the-function-stack/functions/data-manipulation/switch.html)
            -   [Loops](../../the-function-stack/functions/data-manipulation/loops.html)
            -   [Math](../../the-function-stack/functions/data-manipulation/math.html)
            -   [Arrays](../../the-function-stack/functions/data-manipulation/arrays.html)
            -   [Objects](../../the-function-stack/functions/data-manipulation/objects.html)
            -   [Text](../../the-function-stack/functions/data-manipulation/text.html)
                    -   [Security](../../the-function-stack/functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../../the-function-stack/functions/apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../../the-function-stack/functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../../the-function-stack/functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../../the-function-stack/functions/data-caching-redis.html)
        -   [Custom Functions](../../the-function-stack/functions/custom-functions.html)
        -   [Utility Functions](../../the-function-stack/functions/utility-functions.html)
        -   [File Storage](../../the-function-stack/functions/file-storage.html)
        -   [Cloud Services](../../the-function-stack/functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](../../the-function-stack/filters/manipulation.html)
        -   [Math](../../the-function-stack/filters/math.html)
        -   [Timestamp](../../the-function-stack/filters/timestamp.html)
        -   [Text](../../the-function-stack/filters/text.html)
        -   [Array](../../the-function-stack/filters/array.html)
        -   [Transform](../../the-function-stack/filters/transform.html)
        -   [Conversion](../../the-function-stack/filters/conversion.html)
        -   [Comparison](../../the-function-stack/filters/comparison.html)
        -   [Security](../../the-function-stack/filters/security.html)
            -   Data Types
        
        -   [Text](../../the-function-stack/data-types/text.html)
        -   [Expression](../../the-function-stack/data-types/expression.html)
        -   [Array](../../the-function-stack/data-types/array.html)
        -   [Object](../../the-function-stack/data-types/object.html)
        -   [Integer](../../the-function-stack/data-types/integer.html)
        -   [Decimal](../../the-function-stack/data-types/decimal.html)
        -   [Boolean](../../the-function-stack/data-types/boolean.html)
        -   [Timestamp](../../the-function-stack/data-types/timestamp.html)
        -   [Null](../../the-function-stack/data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](../../the-function-stack/additional-features/response-caching.html)
        
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
        
        -   [Using the Xano Database](../database-basics/using-the-xano-database.html)
        -   [Field Types](../database-basics/field-types.html)
        -   [Relationships](../database-basics/relationships.html)
        -   [Database Views](../database-basics/database-views.html)
        -   [Export and Sharing](../database-basics/export-and-sharing.html)
        -   [Data Sources](../database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](airtable-to-xano.html)
        -   [Supabase to Xano](supabase-to-xano.html)
        -   [CSV Import & Export](csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../database-performance-and-maintenance/storage.html)
        -   [Indexing](../database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](../../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](../../ai-tools/mcp-builder/mcp-functions.html)
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
        
        -   [Separating User Data](../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
        
        -   [Release Track Preferences](../../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](../../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../../xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](../../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../../xano-features/metadata-api/content.html)
        -   [Search](../../xano-features/metadata-api/search.html)
        -   [File](../../xano-features/metadata-api/file.html)
        -   [Request History](../../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](../../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../../xano-features/metadata-api/token-scopes-reference.html)
        
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
        
        -   [Agency Dashboard](../../agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](../../agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](../../agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](../../agencies/agency-features/agency-profile.html)
        -   [Commission](../../agencies/agency-features/commission.html)
        -   [Private Marketplace](../../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](../../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](../../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](../../enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](../../enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](../../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](../../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](../../enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](../../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](../../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](../../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](../../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](../../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](../../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](../../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](../../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](../../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
-   
    Special Pricing
    
    -   Students & Education
    -   Non-Profits

-   
    Security
    
    -   Best Practices

[Powered by GitBook]

On this page

Was this helpful?

Copy

1.  [The Database](../getting-started-shortcuts.html)
2.  Migrating your Data

CSV Import & Export 
===================

 

Export a Table or View

Click the [![](../../_gitbook/image9557.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FqVfpMVQjyqO1DS203G58%252FCleanShot%25202024-12-15%2520at%252021.45.01.png%3Falt%3Dmedia%26token%3D74d78e41-455f-43b0-b0e3-7f1c70bb1308&width=300&dpr=4&quality=100&sign=4a6f135e&sv=2)]icon and choose **Export CSV** from the dropdown menu.

Check the [![](../../_gitbook/imagedba8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F5k8gRr2SqGjAhTzi8zwO%252FCleanShot%25202024-12-15%2520at%252021.45.36.png%3Falt%3Dmedia%26token%3D4b0fc88f-71d1-4b67-9ad0-786503dfef87&width=300&dpr=4&quality=100&sign=1afa2d08&sv=2)]option to export only the currently selected [database view](../database-basics/database-views.html).

You will receive an email once your export is complete.

 

Export Specific Records

Check the box next to the records you want to export and click the [![](../../_gitbook/image4897.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252ForpyQPoyyWbRz8DDaf9U%252FCleanShot%25202024-12-15%2520at%252021.50.14.png%3Falt%3Dmedia%26token%3Dbe3f3252-8d2f-40fd-a84a-26f62ad5e421&width=300&dpr=4&quality=100&sign=ff4baf74&sv=2)] button.

![](../../_gitbook/image8bbc.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FXoHefZTNchHxCJCXXAJj%252FCleanShot%25202024-12-15%2520at%252021.49.44.png%3Falt%3Dmedia%26token%3Df1fe83d4-86cf-497f-ad85-6da9d77f200b&width=768&dpr=4&quality=100&sign=f2136c75&sv=2)

Your export may take a few moments depending on the size, but should download automatically.

 

Importing a CSV

Xano\'s CSV file import is ultra-robust. Import your file with confidence, even if you have millions of records. The import process runs on Xano\'s special import service, which has dedicated resources separate from your instance, so it can handle all of your data no matter how large it is.

The CSV file import allows you to create a brand new table from scratch and will generate the schema automatically.

Additionally, you can edit existing records if the file can be mapped to a primary key or append data to an existing table.

Uploads of over 5,000 records will be performed in the background. You can easily monitor the import\'s progress in the settings of your workspace and will be notified on Xano and via email when the import is complete.

###  

Add a New Table

From the database select Add Table.

![](../../_gitbook/image0d96.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F5MmRn9yxCO6VoZzbQsZ5%252FCleanShot%25202021-12-07%2520at%252015.52.56.png%3Falt%3Dmedia%26token%3D35f5a514-a77e-4ef9-a751-dff87aa0bf4a&width=768&dpr=4&quality=100&sign=7164235e&sv=2)

Select Add Table and Select Import Data.

When the right panel opens up, select **Import Data** and choose the **CSV** file option.

![](../../_gitbook/image0512.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FZbwZp2HrDgxcjm1XTBEx%252FCleanShot%25202024-07-12%2520at%252015.56.11.png%3Falt%3Dmedia%26token%3D09b32b57-cb6b-4519-85c8-d25280ea4c51&width=768&dpr=4&quality=100&sign=8e45135&sv=2)

Select import data from CSV.

Next, drag and drop a CSV file onto the uploader or browse the files on your computer for the file you wish to upload.

![](../../_gitbook/image7fba.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FlFGhNg64xvZOYrMOujtL%252FCleanShot%25202025-05-15%2520at%252010.24.16.png%3Falt%3Dmedia%26token%3D8182337e-ed92-409d-abf0-e63b62c41f66&width=768&dpr=4&quality=100&sign=36fd5bf8&sv=2)

Once you select a CSV file, the preview of your CSV will open up. The preview will display the first 100 rows of your file. You can make any final adjustments to the data types, primary key, or table name here before beginning the import.

![](../../_gitbook/image2d5b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FIsZwiEUtiBqnEQnO8FRI%252FCleanShot%25202025-05-15%2520at%252010.26.30.png%3Falt%3Dmedia%26token%3D0fa5683d-d39a-4f19-8c8d-eead966e4d3a&width=768&dpr=4&quality=100&sign=ce34f6ee&sv=2)

Xano will try to automatically detect a primary key field. Currently, only integers are supported for the primary key field. The drop-down will show any fields compatible to be a primary key. If there is no primary key, then Xano will create the primary key automatically.

Once you are ready, click [ Upload ]. If you are uploading over 5,000 records, then your upload will be performed in the background. You can monitor the progress of your upload from the settings page of your workspace. Once your background upload is complete a green banner will appear notifying you to refresh your browser and an email notification will be sent with confirmation of a successful import.

 

Add to an Existing Table

You can import a CSV to an existing table if you\'d like to add records to it. The process is the same as importing to a new table --- just access the import option from inside of the database table you want to add to.
[![](../../_gitbook/image6dd4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F9R9OICb9jw5H7w6XJX0g%252Fimage.png%3Falt%3Dmedia%26token%3D8d4c4c18-ad6f-49d6-bd93-e4644a219b24&width=300&dpr=4&quality=100&sign=433091ee&sv=2)]

During the import, make sure to review the columns and make sure they are mapped to the right columns that already exist in your database table.

[![](../../_gitbook/image99ec.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FTwtuwd95rE1gFJ1rDiPP%252Fimage.png%3Falt%3Dmedia%26token%3Df1e5fa13-5600-4643-8bf0-bf1757f3acf7&width=300&dpr=4&quality=100&sign=9c4dd074&sv=2)]

 

Edit Records in an Existing Table

Just like adding records to an existing table, you can also use a CSV upload to **edit records** in a table.

The only difference between adding a new table or adding to an existing table is that you\'ll need to make sure your CSV contains an `id` field. This is what Xano will use to find the records to apply changes to.

###  

Valid CSV Format

It\'s important that you use a valid CSV file format in order to successfully import your data. If there is an issue with initiating the upload then this could likely be the issue.

####  

What is a valid CSV file format?

A CSV stands for a comma-separate file, which is a delimited text file that uses a **comma** to separate values. The importer does not support other separators, such as semicolons. Each line of the file is a data record. Each record consists of one or more fields, separated by commas.

-   
    
        
    
    The first row must contain the column names - not the file name or any other data.
    
-   
    
        
    
    The second row begins the values. They should be in the same order as the columns they belong to.
    
-   
    
        
    
    Each row should have the same amount of values as there are columns.
    
-   
    
        
    
    **Enclosure characters** are required when working with text strings that contain quotation marks. This is because if a quotation mark is detected, this is typically something that would mark the beginning or end of a value. You can use a **double quote (\"\")** to dictate if a value should contain this quotation mark somewhere inside the value.
    
-   
    
        
    
    CSV files should be UTF-8 encoded. If you\'re having trouble importing your CSV properly in Xano and have determined you are using both the proper separator and enclosure characters, please make sure your file us UTF-8 encoded. This ensures that there are no special characters that might not be supported in Xano.
    
UTF-8 Encoding in Notepad (Windows)

1.  
    
        
    
    Open your file in Notepad.
    
2.  
    
        
    
    Click File \> Save As\...
    
3.  
    
        
    
    Click \"Save As Type\", and choose All Files.
    
4.  
    
        
    
    Click \"UTF-8\" in the Encoding dropdown.
    
5.  
    
        
    
    Save the file.
    
**UTF-8 Encoding in Google Sheets (All platforms)**

1.  
    
        
    
    Open your file in Google Sheets
    
2.  
    
        
    
    Click File \> Download \> Comma separated values (CSV)
    
3.  
    
        
    
    The file will be downloaded in CSV format using UTF-8 encoding.
    
UTF-8 Encoding in Numbers (Mac)

1.  
    
        
    
    Open your file in Numbers
    
2.  
    
        
    
    Click File \> Export To\... \> CSV
    
3.  
    
        
    
    In the \"Text Encoding\" dropdown, choose UTF-8
    
4.  
    
        
    
    Save the file.
    

[](https://3699875497-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tWsL4o1vHmDGb2UAUDD%2Fuploads%2FTcftKcnn1uEplLEXG1qg%2FXano-Sample-CSV.csv?alt=media&token=f037ad45-d0ca-4962-a338-a0b8e0a28776)

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