---
category: function-stack
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/function-stack
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
title: '[![](../../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv'
---

[![](../../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)![](../../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)](../../../index.html)















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
            
            -   [Swagger (OpenAPI Documentation)](../../building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../../building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../../building-with-visual-development/background-tasks.html)
        -   [Triggers](../../building-with-visual-development/triggers.html)
        -   [Middleware](../../building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../../building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../../building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](../ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](query-all-records/external-filtering-examples.html)
                            -   [Get Record](get-record.html)
            -   [Add Record](add-record.html)
            -   [Edit Record](edit-record.html)
            -   [Add or Edit Record](add-or-edit-record.html)
            -   [Patch Record](patch-record.html)
            -   [Delete Record](delete-record.html)
            -   [Bulk Operations](bulk-operations.html)
            -   [Database Transaction](database-transaction.html)
            -   [External Database Query](external-database-query.html)
            -   [Direct Database Query](direct-database-query.html)
            -   [Get Database Schema](get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](../data-manipulation/create-variable.html)
            -   [Update Variable](../data-manipulation/update-variable.html)
            -   [Conditional](../data-manipulation/conditional.html)
            -   [Switch](../data-manipulation/switch.html)
            -   [Loops](../data-manipulation/loops.html)
            -   [Math](../data-manipulation/math.html)
            -   [Arrays](../data-manipulation/arrays.html)
            -   [Objects](../data-manipulation/objects.html)
            -   [Text](../data-manipulation/text.html)
                    -   [Security](../security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](../apis-and-lambdas/realtime-functions.html)
            -   [External API Request](../apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](../apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](../data-caching-redis.html)
        -   [Custom Functions](../custom-functions.html)
        -   [Utility Functions](../utility-functions.html)
        -   [File Storage](../file-storage.html)
        -   [Cloud Services](../cloud-services.html)
            -   Filters
        
        -   [Manipulation](../../filters/manipulation.html)
        -   [Math](../../filters/math.html)
        -   [Timestamp](../../filters/timestamp.html)
        -   [Text](../../filters/text.html)
        -   [Array](../../filters/array.html)
        -   [Transform](../../filters/transform.html)
        -   [Conversion](../../filters/conversion.html)
        -   [Comparison](../../filters/comparison.html)
        -   [Security](../../filters/security.html)
            -   Data Types
        
        -   [Text](../../data-types/text.html)
        -   [Expression](../../data-types/expression.html)
        -   [Array](../../data-types/array.html)
        -   [Object](../../data-types/object.html)
        -   [Integer](../../data-types/integer.html)
        -   [Decimal](../../data-types/decimal.html)
        -   [Boolean](../../data-types/boolean.html)
        -   [Timestamp](../../data-types/timestamp.html)
        -   [Null](../../data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](../../additional-features/response-caching.html)
        
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
        
        -   [Using the Xano Database](../../../the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](../../../the-database/database-basics/field-types.html)
        -   [Relationships](../../../the-database/database-basics/relationships.html)
        -   [Database Views](../../../the-database/database-basics/database-views.html)
        -   [Export and Sharing](../../../the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](../../../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../../../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../../../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../../../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../../../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../../../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../../../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../../../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../../../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](../../../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](../../../ai-tools/mcp-builder/mcp-functions.html)
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
        
        -   [Separating User Data](../../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
        
        -   [Release Track Preferences](../../../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](../../../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](../../../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](../../../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](../../../xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](../../../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](../../../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](../../../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](../../../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](../../../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](../../../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../../../xano-features/metadata-api/content.html)
        -   [Search](../../../xano-features/metadata-api/search.html)
        -   [File](../../../xano-features/metadata-api/file.html)
        -   [Request History](../../../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](../../../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](../../../xano-features/metadata-api/token-scopes-reference.html)
        
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
        
        -   [Agency Dashboard](../../../agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](../../../agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](../../../agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](../../../agencies/agency-features/agency-profile.html)
        -   [Commission](../../../agencies/agency-features/commission.html)
        -   [Private Marketplace](../../../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](../../../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](../../../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](../../../enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](../../../enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](../../../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../../../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](../../../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](../../../enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](../../../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](../../../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](../../../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](../../../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](../../../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](../../../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](../../../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](../../../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](../../../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
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


2.  Functions
3.  [Database Requests](../database-requests.html)

Patch Record 
============

**Patch** is most appropriate when you aren\'t sure what fields will be updated when editing the record.

####  

What\'s the difference between Edit Record and Patch Record?

-   
    
        
    
    **Edit Record** is best used when you have a static expectation for which fields need to be updated when the function is executed. For example, maybe you have an endpoint specifically to allow a user to update their password. Edit Record would make sense here, because you would not be changing any other information.
    
-   
    
        
    
    **Patch Record** is best used when you have an endpoint that can update multiple fields, but may not always need to do so. Something like a user submitting a collection of edits to their user profile would fall under this example.
    
**Patch Record** is a little different than **Edit Record** in the way values are provided to it. While Edit Record gives you the option to address each field individually inside of the function, **Patch** only expects a field name and field value (so it knows which record to patch) and a JSON object representing all of the values to be updated.

In the following example, let\'s say that our record currently looks like this:

Copy

``` 
{
    "id": 1,
    "name": "Chris",
    "email": "[email protected]",
    "city": "Chicago"
    }
```

We want to build an endpoint that allows our users to update one or more of these fields in one swing. This means that we need to construct a JSON object that contains **only** the values to be updated and provide that to our Patch Record statement.

If Chris wants to update only his city, the object we provide to Patch would look like this:

Copy

``` 
{
    "city": "Seattle"
    }
```

And our patch statement might look like this:

![](../../../_gitbook/imagecc45.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F1fBCzAq3Dv0rQLm17QUu%252FCleanShot%25202024-09-10%2520at%252006.07.16.png%3Falt%3Dmedia%26token%3Dfa054734-45f5-4f41-815b-8ad443063ca6&width=768&dpr=4&quality=100&sign=a91272b8&sv=2)

However, using the **set filter** in the scenario where multiple fields **might** be provided is not recommended. This is because if Patch is provided empty or null values, it will write those to the record, and the goal is to only write the fields we want.

**Please be aware that Patch will write every field provided in the JSON object to the record, even blank and null values.
The JSON object used for Patch should only provide the fields you want to update, and nothing more. Providing empty or null values unintentionally can result in data loss.**

Some frontends will always send empty or null values regardless of what data points are actually defined.

To make Patch work as it is normally expected, you\'ll want to leverage filters like:

-   
    
        
    
    `filter_null` to remove null values
    
-   
    
        
    
    `filter_empty_text` to remove empty text strings
    
Using a **Get All Raw Input** function along with **Patch Record** can be a perfect combination.

-   
    
        
    
    **Get All Raw Input** provides a JSON object of all of the input fields passed to the API.
    
-   
    
        
    
    We can then provide the output of this function to **Patch Record**, giving us an easy and fast method of building a flexible endpoint for editing records.
    
Our final endpoint might look something like this:

![](../../../_gitbook/imageaa72.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FHXTDYZW2ddh6hdnQCqN8%252FCleanShot%25202024-09-10%2520at%252006.11.02.png%3Falt%3Dmedia%26token%3Dabd3539c-f609-432d-85e1-afeb58cf30df&width=768&dpr=4&quality=100&sign=60474e69&sv=2)

![](../../../_gitbook/image1897.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F4cu09liemLkCyEllz2D5%252FCleanShot%25202024-09-10%2520at%252006.11.28.png%3Falt%3Dmedia%26token%3D9daf9dfc-ad7c-4e0a-9ee4-58bf888e942f&width=768&dpr=4&quality=100&sign=7b5d8ca8&sv=2)

Last updated 4 months ago

Was this helpful?