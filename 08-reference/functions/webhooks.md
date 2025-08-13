---
category: functions
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 08-reference/functions
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
description: Webhooks are specialized API endpoints designed to be triggered based on other events
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: webhooks
twitter:card: summary\_large\_image
twitter:description: Webhooks are specialized API endpoints designed to be triggered based on other events
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
        
        -   [Using the Xano Database](../the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](../the-database/database-basics/field-types.html)
        -   [Relationships](../the-database/database-basics/relationships.html)
        -   [Database Views](../the-database/database-basics/database-views.html)
        -   [Export and Sharing](../the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](../the-database/database-performance-and-maintenance/schema-versioning.html)
        
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
        
        -   [Separating User Data](user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](user-authentication-and-user-data/oauth-sso.html)
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
    
    [Building Webhooks](#building-webhooks)

-   [Create a new API endpoint with a POST method](#create-a-new-api-endpoint-with-a-post-method)

-   [Add a Get All Raw Input function](#add-a-get-all-raw-input-function)

-   [Process the output of Get All Raw Input as needed](#process-the-output-of-get-all-raw-input-as-needed)

-   [Securing your Webhooks](#securing-your-webhooks)

-   [Signature Verification (recommended)](#signature-verification-recommended)

-   [Check a static token provided in the headers](#check-a-static-token-provided-in-the-headers)

Was this helpful?

Copy

1.  [Building Backend Features](user-authentication-and-user-data.html)

Webhooks 
========

Webhooks are specialized API endpoints designed to be triggered based on other events

 

Quick Summary

Webhooks are API endpoints specifically designed for one system to **automatically push** information to another when a specific **event** happens. For example, Slack provides you with a webhook URL. This URL is ready and listening, much like your own API endpoint.

But here's the key difference:

1.  
    
        
    
    Something like a **form submission endpoint** receives data because the *user initiated* the request (e.g., they clicked \'Submit\').
    
2.  
    
        
    
    The **Slack webhook** receives data because *your server*, after processing the form (the **event**), *initiated* a new request, automatically pushing the form details *to* Slack\'s URL. Slack didn\'t ask for it; your system sent it because something happened.
    
You\'d build webhooks in Xano typically to ingest information ***pushed*** from other places --- like if a user pays for something via Stripe, or they perform an action in your app that you want to log.

<div>

</div>

 

Building Webhooks

<div>

1

###  

Create a new API endpoint with a POST method

1.  
    
        
    
    Click [ + Add API Endpoint ] from inside one of your API groups.
    
2.  
    
        
    
    Choose **Custom API Endpoint** and fill in the details. Make sure to select **POST** as the verb.
    [![](../_gitbook/imagee24d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FMVUpXcTDZfjqIROkctUJ%252FCleanShot%25202025-04-30%2520at%252011.18.57.png%3Falt%3Dmedia%26token%3D643b6771-b675-44fe-a7ce-51d11de0c92f&width=300&dpr=4&quality=100&sign=e797c4c&sv=2)]
    

2

###  

Add a Get All Raw Input function

Typically, webhooks need to be able to dynamically process data that might look a little different between requests. So, we use [Get All Raw Input](../the-function-stack/functions/utility-functions.html#get-all-raw-input) to make sure that we aren\'t confined to just the inputs that are defined in the inputs section.

You\'ll need to choose the encoding, or the format, of the data being sent to this endpoint. This will more often than not be JSON.

While Get All Raw Input offers flexibility, always check the documentation of the service *sending* the webhook. They will specify the structure (schema) of the data payload you should expect.

3

###  

Process the output of Get All Raw Input as needed

From here, the process is completely unique to whatever data is being sent to the webhook, and what you need to do with it.

**Examples:**

-   
    
        
    
    Store the data in a database table using [Add Record](../the-function-stack/functions/database-requests/add-record.html)
    
-   
    
        
    
    If the webhook is receiving a list of items, loop against them using [For Each Loop](../the-function-stack/functions/data-manipulation/loops.html#for-each-loop)
    
-   
    
        
    
    Transform or manipulate the data using [Filters](../the-function-stack/filters.html) or an [Expression](../the-function-stack/data-types/expression.html)
    
-   
    
        
    
    Send the data to another service, such as an analytics platform, using an [External API Request](../the-function-stack/functions/apis-and-lambdas/external-api-request.html)
    
-   
    
        
    
    Begin a more in-depth process using a combination of the above to perform multiple actions, such as transforming data, storing it, and sending [Emails](emails.html)
    
</div>

 

Securing your Webhooks

Just like any other API endpoint you\'re building, it\'s important to ensure that they are built securely. Webhooks have some more specific-to-them ways that they are usually kept locked up.

<div>

1

###  

Signature Verification (recommended)

The service you\'re accepting requests from may offer signature verification. At a high level, this means that you would cross-check the signature they sent with your own calculated signature, using a private key that only you and the service are aware of, and ensure that they match.

**If they match**: The request is verified and you can proceed.

**If they don\'t match**: you should deny the request

In general, this process follows a typical flow:

-   
    
        
    
    Extract the signature provided in the request headers
    
-   
    
        
    
    Ensure you have a raw, unaltered copy of the request body (which you do using Get All Raw Input)
    
-   
    
        
    
    Use the proper [Security](../the-function-stack/filters/security.html) filter (such as [hmac\_sha256 / hmac384 / hmac512](../the-function-stack/filters/security.html#hmac_sha256-hmac384-hmac512)) to encode your own signature, and ensure that it matches with the one you extracted from the request.
    

2

###  

Check a static token provided in the headers

Similar to how standard [User Authentication & User Data](user-authentication-and-user-data.html) works, some services may just send an API key or bearer token as part of the request header. You\'ll want to compare this against your own stored key and ensure that they match.

It\'s also good practice to rotate this token on a regular basis to ensure that it is not compromised.

</div>

 

Tip

Use [Middleware](../the-function-stack/building-with-visual-development/middleware.html) or [Custom Functions](../the-function-stack/building-with-visual-development/custom-functions.html) to build your webhook verification and quickly deploy it across multiple function stacks.

Last updated 3 months ago

Was this helpful?