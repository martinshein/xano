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
title: 'apple-mobile-web-app-status-bar-style: black'
---

---
apple-mobile-web-app-status-bar-style: black

color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'testing-and-debugging-function-stacks'
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
    
    [Testing a Function Stack](#testing-a-function-stack)

-   [Click at the top of your workflow to execute it.](#click-at-the-top-of-your-workflow-to-execute-it)

-   [Populate any necessary inputs.](#populate-any-necessary-inputs)

-   [Click to execute the workflow.](#click-to-execute-the-workflow)

-   [Review the response and timing, if desired.](#review-the-response-and-timing-if-desired)

-   [What\'s next?](#whats-next)

-   [Using the Debugger](#using-the-debugger)

-   [Simple Mode](#simple-mode)

-   [Advanced Options](#advanced-options)

-   [Unknown Errors and Debugger Errors](#unknown-errors-and-debugger-errors)

Was this helpful?

Copy

1.  [Testing and Debugging](testing-and-debugging-function-stacks.html)

Testing and Debugging Function Stacks 
=====================================

 

Testing a Function Stack

<div>

1

###  

Click [![](../_gitbook/image9f06.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FtEjVTFcKePG8peCHxgd0%252FCleanShot%25202025-01-03%2520at%252010.47.02.png%3Falt%3Dmedia%26token%3Dcf429cdd-bfdb-4086-bef4-18f27d2dae26&width=300&dpr=4&quality=100&sign=b583bb8f&sv=2)] at the top of your workflow to execute it.

Clicking this button opens the Run panel.

2

###  

Populate any necessary inputs.

This information will be used to test your workflow. If you\'re copying and pasting JSON from another source, you can use the Format button to quickly turn it into a readable structure if necessary, although this will not impact the functionality of your test run.

![](../_gitbook/image2e9b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FYslHliTj8F5dn53kz3WE%252FCleanShot%25202025-01-03%2520at%252010.56.54.png%3Falt%3Dmedia%26token%3D822be772-6760-406c-9709-d87b1078495a&width=768&dpr=4&quality=100&sign=4361c368&sv=2)

3

###  

Click [![](../_gitbook/imagece7b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F9O8OHSqGuBtFNAk27YFy%252FCleanShot%25202025-01-03%2520at%252010.57.23.png%3Falt%3Dmedia%26token%3D0d6d7ec3-5040-4169-b33e-0fdc559a3485&width=300&dpr=4&quality=100&sign=8df78d44&sv=2)]to execute the workflow.

 

Hint - Running in Safe Mode

If you\'re running into memory issues when running large function stacks or working with large data sets, you can run with Safe Mode by clicking the arrow next to the Run button and choosing **Safe Mode**.

[![](../_gitbook/image52c4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FgzwHyhqTX59WcORNY9PQ%252FCleanShot%25202025-04-15%2520at%252016.27.26.png%3Falt%3Dmedia%26token%3D984b1afe-94e8-4de3-adef-2fabe76dd611&width=300&dpr=4&quality=100&sign=a4975538&sv=2)]

Safe Mode runs the function stack without retaining any context in memory, which can be very helpful when looping over a significant amount of data and you\'re experiencing crashes. *No context* just means that things like autocomplete won\'t work, and the output of debugging information will be limited.

Any questions, please reach out to our support team!

4

###  

Review the response and timing, if desired.

####  

Response

The response block will show you what the workflow has returned, if applicable, once execution has completed.

![](../_gitbook/imageaa37.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FgWUIsAJq392Df2IDalHj%252FCleanShot%25202025-01-03%2520at%252010.58.33.png%3Falt%3Dmedia%26token%3D56faec77-6f0a-4f2e-96d2-de6daf3e660e&width=768&dpr=4&quality=100&sign=d6c4d0&sv=2)

You can see the amount of time the request took to complete, and perform several actions from inside this block.

Click [![](../_gitbook/imaged81d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FR1YMl4sexvJxBpc757RH%252FCleanShot%25202025-01-03%2520at%252010.59.29.png%3Falt%3Dmedia%26token%3D835bd4a2-c6af-4fd6-8502-33af9c037386&width=300&dpr=4&quality=100&sign=d6223d12&sv=2)] to copy the contents of the response

Click [![](../_gitbook/imageb5ba.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FztdIDyuDNprAtJmThI03%252FCleanShot%25202025-01-03%2520at%252010.59.56.png%3Falt%3Dmedia%26token%3D13399ca9-50b0-4f17-834b-70213a9988b1&width=300&dpr=4&quality=100&sign=a3e5a8eb&sv=2)] to copy the request as a cURL command to be used outside of Xano

Click [![](../_gitbook/image2037.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FrBC0fmrNSwil04OcndSw%252FCleanShot%25202025-01-03%2520at%252011.03.04.png%3Falt%3Dmedia%26token%3D15f3d4e9-4275-49f0-b2d6-14eaede53266&width=300&dpr=4&quality=100&sign=1a32a24a&sv=2)] to create a [unit test](unit-tests.html) based on this run.

Click [![](../_gitbook/image7baa.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FKI3MCRjtTUv05l7ro369%252FCleanShot%25202025-01-03%2520at%252011.04.33.png%3Falt%3Dmedia%26token%3De40d3c80-993a-49d1-ba5d-b4a1ab4fa2c2&width=300&dpr=4&quality=100&sign=6757aa42&sv=2)] to activate the debugger --- more on this below.

####  

Timing

You can further review more information for each step that executed during this run in the Timing block.

![](../_gitbook/imagec908.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVRrWamiQCKzaNjgJUDSo%252FCleanShot%25202025-01-03%2520at%252011.05.33.png%3Falt%3Dmedia%26token%3D0fa36ba8-1b62-4ab5-9f55-6d821cd22d32&width=768&dpr=4&quality=100&sign=eb896476&sv=2)

This block will provide individual timings for each step, allowing you to quickly pinpoint any points of delay that could be improved. You can also click the **\>** icon next to each step to review that step\'s output for further investigation.

5

###  

What\'s next?

Run it again by clicking [ Run Again ], reset everything back to the initial state by clicking [ Reset ] , or activate the debugger with [ Activate Debugger ] .

You can also use this opportunity to define sample inputs and responses for your [Swagger (OpenAPI Documentation)](../the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html).

When [testing your function stacks](testing-and-debugging-function-stacks.html) in Xano, you can define sample input and output examples for your Swagger documentation.

It is important that you do this to ensure that your documentation is as effective as possible, as well as for helping AI models understand what\'s expected when interacting with your APIs.

<div>

1

###  

In the \'response\' section of the Run panel, click [ Set As Example ]

![](../_gitbook/imagedbda.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FnwZdxVOKgC8rPEQEzsHo%252FCleanShot%25202025-04-21%2520at%252009.37.02.png%3Falt%3Dmedia%26token%3D17104cdc-1f4a-452a-87c8-bafe28b44c02&width=768&dpr=4&quality=100&sign=15e1131d&sv=2)

2

###  

Review the sample input and response, and make any necessary adjustments

Make sure these do not include any sensitive information.

![](../_gitbook/image000f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fx1S8lS4BSQRqv4LxyRqb%252FCleanShot%25202025-04-21%2520at%252009.38.01.png%3Falt%3Dmedia%26token%3Db4ff490a-9897-4a64-aece-be73ad23e1aa&width=768&dpr=4&quality=100&sign=b3730b6e&sv=2)

3

###  

Click [ Save ] and you will see these defined in your Swagger documentation.

![](../_gitbook/image9940.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fy1DxEup0oYhPLr7GAg0k%252FCleanShot%25202025-04-21%2520at%252009.43.22.png%3Falt%3Dmedia%26token%3D168242e3-98b6-4b02-9889-58d4a1ec2c8f&width=768&dpr=4&quality=100&sign=d50b4e35&sv=2)

If you need to make adjustments later, you can do so from the settings menu.

![](../_gitbook/image1d86.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F0neNgATxiv1nHsfbVj0q%252FCleanShot%25202025-04-21%2520at%252009.42.32.png%3Falt%3Dmedia%26token%3D41107822-d29c-4b44-8b2b-976a1131a91c&width=768&dpr=4&quality=100&sign=ee46b0c5&sv=2)

</div>

</div>

------------------------------------------------------------------------

 

Using the Debugger

The Debugger is used to review each step of execution, one at a time, to pinpoint the cause of any issues that might arise during that run.

Please note that each step is not actually individually being executed; the full run has completed prior to the debugger being available.

###  

Simple Mode

[![](../_gitbook/imagedacc.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FS1FIPerThylUcjD1EuQM%252FCleanShot%25202025-01-03%2520at%252011.17.38.png%3Falt%3Dmedia%26token%3D79e7d939-78e4-4203-879a-a4f0f4d2e515&width=300&dpr=4&quality=100&sign=bba4cffc&sv=2)] Stop Debugging

[![](../_gitbook/image8975.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FWk9w3d87hmaOtaG7OEsm%252FCleanShot%25202025-01-03%2520at%252011.19.12.png%3Falt%3Dmedia%26token%3D3adb98dd-466c-484b-b744-6f8bfff82dd1&width=300&dpr=4&quality=100&sign=12e97a0&sv=2)] Restart the Debugger

[![](../_gitbook/imagebe3b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FilMsCt69QUaOfAQI3MDg%252FCleanShot%25202025-01-03%2520at%252011.19.29.png%3Falt%3Dmedia%26token%3D2bde3f3b-dc68-4fa2-89a7-1687267afc3b&width=300&dpr=4&quality=100&sign=652a8e5d&sv=2)] Move to the next step

As you move through each step, the current will be highlighted as shown below.

![](../_gitbook/image0e96.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FdyhvShdStGgzm7fO39TX%252FCleanShot%25202025-01-03%2520at%252011.20.02.png%3Falt%3Dmedia%26token%3D4119124c-f065-4988-8a8c-3f60eb65d1e2&width=768&dpr=4&quality=100&sign=98ec7b53&sv=2)

Completed steps will be highlighted in green.

![](../_gitbook/image04e9.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FmuNk7uufvEoimx8VsXi2%252FCleanShot%25202025-01-03%2520at%252011.20.51.png%3Falt%3Dmedia%26token%3D863d512d-e1db-41ee-b2e6-4ca0e3a9a630&width=768&dpr=4&quality=100&sign=d9ffa20c&sv=2)

As you progress through each step, the **Variables** panel will update with current data.

![](../_gitbook/imagec093.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fd8XM6R2EmXJghtoiopK0%252FCleanShot%25202025-01-03%2520at%252011.21.43.png%3Falt%3Dmedia%26token%3D1936bebb-c4c7-4ac9-adb6-aed71d388b6e&width=768&dpr=4&quality=100&sign=da0a8902&sv=2)

Clicking different steps in your function stack will bring the debugger to that point.

![](../_gitbook/imaged0d4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8jaRt3GfglnW2EXAAAuT%252FCleanShot%25202025-01-03%2520at%252011.23.02.gif%3Falt%3Dmedia%26token%3D61ed4907-ce99-402e-87f3-183cbc5b0687&width=768&dpr=4&quality=100&sign=29e2020a&sv=2)

###  

Advanced Options

Click [![](../_gitbook/image956a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FcvFYGpE35p4huqN3AvV3%252FCleanShot%25202025-01-03%2520at%252011.25.43.png%3Falt%3Dmedia%26token%3D978d1cd4-728f-4779-9f62-c90f5401d3b2&width=300&dpr=4&quality=100&sign=7061cd26&sv=2)]to enable the advanced debugging options.

-   
    
        
    
    **Step Over** - When working with nested function stacks (custom functions or middleware), if you don\'t need to debug those, just step right over them and continue with the next function in your function stack
    
-   
    
        
    
    **Step Into / Step Out** - Step into or out of a nested function (custom function or middleware) and continue the debugging experience seamlessly
    
-   
    
        
    
    **Continue** - Continue with execution of your function stack
    
-   
    
        
    
    **Enable Breakpoints** - Enable or disable breakpoints as a whole
    
-   
    
        
    
    **Step Forwards / Step Backwards** - Toggle forward or reverse execution of your function stack
    
-   
    
        
    
    **Result** - View the result of your completed execution
    
-   
    
        
    
    **Watches** - Use custom Javascript expressions for more complex data monitoring or calculation as your function stack executes
    
-   
    
        
    
    **Variables** - View the current contents of your variables as the function stack executes
    
-   
    
        
    
    **Copy** 📄 **/ Add Watch** 👁️ - Copies the variable\'s current contents, or adds a variable to your Watches list
    
-   
    
        
    
    **Breakpoints** - Hover over the icon on the left side of each function to establish a breakpoint. Breakpoints will cause the debugger to pause at that step.
    
 

Unknown Errors and Debugger Errors

**Unknown Error**

**The debugger encountered an error**

If you see these messages, they could indicate one of the following:

-   
    
        
    
    An unhandled exception in your logic

    -   
        
                
        
        This means that you\'ve likely ran across a rare error that we don\'t yet have specific messaging for. Please let us know about this so we can make an adjustment.
            
-   
    
        
    
    Server resource issues
    
You can also try running your function stack in Safe Mode.

 

Hint - Running in Safe Mode

If you\'re running into memory issues when running large function stacks or working with large data sets, you can run with Safe Mode by clicking the arrow next to the Run button and choosing **Safe Mode**.

[![](../_gitbook/image52c4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FgzwHyhqTX59WcORNY9PQ%252FCleanShot%25202025-04-15%2520at%252016.27.26.png%3Falt%3Dmedia%26token%3D984b1afe-94e8-4de3-adef-2fabe76dd611&width=300&dpr=4&quality=100&sign=a4975538&sv=2)]

Safe Mode runs the function stack without retaining any context in memory, which can be very helpful when looping over a significant amount of data and you\'re experiencing crashes. *No context* just means that things like autocomplete won\'t work, and the output of debugging information will be limited.

Any questions, please reach out to our support team!

For assistance with either of these errors, please reach out to our support team. You can also review our documentation on [memory usage](../troubleshooting-and-support/troubleshooting-performance/ram-usage.html) to narrow down the cause.

Last updated 3 months ago

Was this helpful?