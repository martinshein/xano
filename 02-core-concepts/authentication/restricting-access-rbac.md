---
category: authentication
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/authentication
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
title: 'restricting-access-rbac'
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
        
        -   [Using the Xano Database](../../the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](../../the-database/database-basics/field-types.html)
        -   [Relationships](../../the-database/database-basics/relationships.html)
        -   [Database Views](../../the-database/database-basics/database-views.html)
        -   [Export and Sharing](../../the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](../../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../../the-database/database-performance-and-maintenance/schema-versioning.html)
        
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
        
        -   [Separating User Data](separating-user-data.html)
        -   [Restricting Access (RBAC)](restricting-access-rbac.html)
        -   [OAuth (SSO)](oauth-sso.html)
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

1.  [Building Backend Features](../user-authentication-and-user-data.html)
2.  User Authentication & User Data

Restricting Access (RBAC) 
=========================

RBAC (Role-based access control) or role-based permissions is a way to restrict access based on a user\'s defined role. This guide will cover two different methods of enforcing access / RBAC to an API endpoint based on the user\'s role.

<div>

</div>

Let\'s use the following user table for both examples of RBAC. Make note of the role field and the values for each user.

![](../../_gitbook/image36e7.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FDHYZCuUiAlT3bssm3lIM%252Fimage.png%3Falt%3Dmedia%26token%3D31f50f0b-fea6-4163-b139-e9a9b807b685&width=768&dpr=4&quality=100&sign=7c3dbed9&sv=2)

In this example, each user has one of two roles: admin or staff.

####  

**RBAC Example 1: Use Get Record**

Now, let\'s set up an API endpoint that GETs all users but only if the user trying to call the endpoint has a role of admin.

Take note of the endpoint below, user authentication is required. Additionally, take note of the Function Stack:

1.  
    
        
    
    Get Record from user: This will use the authToken to find the user\'s ID and look up their information.
    
2.  
    
        
    
    Precondition: This will enforce that the user\'s role is equal to admin. If it is not, then it will throw and error and stop the endpoint.
    
3.  
    
        
    
    Query all records from user: This will only be performed if the user\'s role is an admin by passing the precondition.
    

![](../../_gitbook/image5d3e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FonKEooRr3Hw1bsh1XcGR%252Fimage.png%3Falt%3Dmedia%26token%3Dac7691ca-5ee1-44a0-a8de-2e452ad0da44&width=768&dpr=4&quality=100&sign=4b78962&sv=2)

In this example, the API endpoint requires an authenticated user. Then the Function Stack is set up to perform only if the user\'s role is equal to admin.

Get the record of the user who\'s calling the endpoint (requester) with the auth ID.

![](../../_gitbook/image664a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FPrldsRrgdeShYlJ8Vixp%252Fimage.png%3Falt%3Dmedia%26token%3D5102ca7b-ae0b-495a-91ef-dcadc22f2822&width=768&dpr=4&quality=100&sign=73e5193c&sv=2)

In this example, we are getting the record of the user based on their authenticated ID.

Next, set a precondition to enforce that the user (called requester in the example) has a role equal to admin.

![](../../_gitbook/image2e03.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FO1PA0ZpCOfjLBbjPWYgP%252Fimage.png%3Falt%3Dmedia%26token%3D400f6024-63d0-46f0-8da2-852f8a16ab6b&width=768&dpr=4&quality=100&sign=54635c46&sv=2)

Click on the pencil icon to open the Expression Builder and set the conditions for the precondition. Additionally, set your error type and message if the conditions are not met.

![](../../_gitbook/imagede5c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FPEPEX4vz84ygHUtmYBGx%252Fimage.png%3Falt%3Dmedia%26token%3D139e36ed-0cef-4cf1-ab17-06325f0ecb97&width=768&dpr=4&quality=100&sign=d9ef8607&sv=2)

In this example, the requester.role must be equal to admin in order to pass the precondition.

If the precondition is met, then the user who is the requester will have permission to execute the rest of the Function Stack and complete the API endpoint.

####  

RBAC Example 2: Use Extras

[Extras](../user-authentication-and-user-data.html#extras) allow you to store data within the authentication token, which you can access and use on authenticated API endpoints.

First, you must set up the [sign-up & login](../user-authentication-and-user-data.html) to include the user\'s role at the time of authentication.

In this example, we will use the login endpoint to pass the user\'s role into extras of the auth token at the time of authentication.

![](../../_gitbook/image30c0.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FHd6ZxJBWCC929qV25rsd%252Fimage.png%3Falt%3Dmedia%26token%3D1cde4ef9-96d6-4133-8d9b-2b84655ff129&width=768&dpr=4&quality=100&sign=61b5fd7c&sv=2)

In this example, we are passing the user\'s role into the authToken at the time of login by utilizing extras.

Now that the user\'s role is passed into the authToken, we can eliminate the Get Record function from the previous example and reference \"extras.role\" in the precondition to enforce the user\'s role.

![](../../_gitbook/image4d04.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FI4ByRi9ttyUp8j87RTxY%252Fimage.png%3Falt%3Dmedia%26token%3D82cc2a0a-e2e0-43ea-a7ca-10ed6daab9c0&width=768&dpr=4&quality=100&sign=dd8ab151&sv=2)

In this example, we can use the extras of the authenticated user to access the user\'s role and set the precondition equal to admin.

![](../../_gitbook/image6db4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVAeju5IjFrt7OPNMw8WK%252Fimage.png%3Falt%3Dmedia%26token%3D0df7ac2e-a276-45a7-be2e-c7946afd29ad&width=768&dpr=4&quality=100&sign=f27ae50e&sv=2)

Set extras.role (as defined in the creation of the authentication token) equal to admin.

If the user\'s role is equal to admin then they will pass the precondition and have permission to execute the rest of the Function Stack. **

Last updated 6 months ago

Was this helpful?