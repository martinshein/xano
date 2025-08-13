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
- integration
- middleware
- expression
- realtime
- transaction
- function
- background-task
- custom-function
- rest
- database
title: Header 1
---

---
apple-mobile-web-app-status-bar-style: black

color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'what-are-actions'
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
    
    [What does zero dependency mean?](#what-does-zero-dependency-mean)

-   [Browsing and Using Actions](#browsing-and-using-actions)

-   [From the left-hand navigation menu, click Actions](#from-the-left-hand-navigation-menu-click-actions)

-   [Browse for and add new actions from here, or at xano.com/actions](#browse-for-and-add-new-actions-from-here-or-at-xano.com-actions)

-   [From any function stack, under the Actions category, you\'ll see your installed actions available for use](#from-any-function-stack-under-the-actions-category-youll-see-your-installed-actions-available-for-us)

-   [Creating an Action](#creating-an-action)

-   [Action Settings](#action-settings)

-   [Action Packages](#action-packages)

-   [Click on the left-hand navigation.](#click-on-the-left-hand-navigation)

-   [Give your package a name, description, and check the other settings in the panel that opens.](#give-your-package-a-name-description-and-check-the-other-settings-in-the-panel-that-opens)

-   [Add Actions to your package by clicking ](#add-actions-to-your-package-by-clicking)

-   [When your Package is ready, click Publish, and once publishing completes, you can add it to your workspace(s).](#when-your-package-is-ready-click-publish-and-once-publishing-completes-you-can-add-it-to-your-worksp)

-   [Publishing](#publishing)

-   [Settings Registry](#settings-registry)

-   [Deleting an Action](#deleting-an-action)

-   [Actions](#actions)

-   [Members](#members)

-   [Settings](#settings)

Was this helpful?

Copy

1.  [Xano Actions](what-are-actions.html)

What are Actions? 
=================

<div>

</div>

A Xano Action is a powerful, zero-dependency function that anyone can create, share, fork (create new versions), and install. Actions can be previewed, tested, and edited in Run mode outside of a Xano instance, meaning they do not require an account for testing and trying them out.

Actions are a lightweight version of the Xano function stack designed for specific processes such as integrations with external APIs or business logic executions. They are similar to custom functions, but without dependencies and shareable to anyone.

Discover Actions on [xano.com/actions](https://www.xano.com/actions). Browse Actions created by the Xano team or other community members. Clicking on an Action allows you to:

-   
    
        
    
    **Run & Debug** the Action.
    
-   
    
        
    
    **Make edits** to the Action.
    
-   
    
        
    
    **Clone**: Make a copy of the Action, change whatever you\'d like, and publish a new (separate) version of the Action.
    
-   
    
        
    
    **Add** the Action into your workspace to be used in any function stack.
    
###  

What does zero dependency mean?

Actions are designed not to contain dependencies to support more seamless integration to existing Xano workspaces and function stacks. Additionally, it promotes easy shareability for anyone, regardless of if they\'re a Xano user, to interact with Actions.

Zero-dependency means Actions do not contain:

-   
    
        
    
    Database request functions or database tables
    
-   
    
        
    
    Middleware
    
-   
    
        
    
    Environment variables\*
    
-   
    
        
    
    Lambdas
    
-   
    
        
    
    Redis caching
    
-   
    
        
    
    Multiple Xano objects
    
-   
    
        
    
    Docker Microservices
    
*\*Settings registry is available for actions for API keys and other sensitive tokens or keys.*

###  

Browsing and Using Actions

<div>

1

###  

From the left-hand navigation menu, click Actions

2

###  

Browse for and add new actions from here, or at xano.com/actions

3

###  

From any function stack, under the Actions category, you\'ll see your installed actions available for use

![](../_gitbook/imageba44.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVcDjbZiCTGqs2n5WDPyi%252FCleanShot%25202025-05-22%2520at%252010.57.31.png%3Falt%3Dmedia%26token%3Dbf6ee00c-b675-412b-a56a-8a2026e43471&width=768&dpr=4&quality=100&sign=7f0878c5&sv=2)

</div>

###  

Creating an Action

![](../_gitbook/image05d5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FhdNkTb2jokj6oDkkeeeH%252FCleanShot%25202024-10-10%2520at%252009.52.49%25402x.png%3Falt%3Dmedia%26token%3D36e47b45-a959-41e6-8db9-72020c98f7e9&width=768&dpr=4&quality=100&sign=50b278c0&sv=2)

Click [**+ Create Action** ]to begin building a new Action.

Building a new Action is very similar to building in a [regular Xano function stack.](../the-function-stack/building-with-visual-development.html#the-anatomy-of-the-visual-builder)

Please note that because Actions are designed to not have dependencies outside of the Action itself, certain functions such as database operations are not available.

###  

Action Settings

Click the three dots in the upper-right corner to access **Action Settings**. From this panel, you can update the following:

**Name** - Give your action a unique name

**Instructions** - You can write documentation to accompany your action here. This field supports markdown for formatting. View the expandable section below for a quick reference.

**Quick Markdown Reference**

Copy

``` 
# Header 1
## Header 2
### Header 3

*Italic* or _Italic_
**Bold** or __Bold__
***Bold and Italic*** or ___Bold and Italic___

- Item 1
- Item 2
  - Subitem 2.1

1. First item
2. Second item
   1. Subitem 2.1

[Link text](https://www.example.com)

[Alt text](image-url.jpg)

`inline code`

```code block```
```

You can also preview your instructions using the **Preview** tab.

**Category** - You must provide a category for your Action before publishing

**Video URL** - You can insert a YouTube or Loom video link here to accompany your action

###  

Action Packages

Packages can be used to bundle and install multiple Actions at once.

<div>

1

###  

Click [![](../_gitbook/imagec0bd.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F86YBkpCmjw0xCLPqbC39%252FCleanShot%25202025-03-20%2520at%252016.07.44.png%3Falt%3Dmedia%26token%3Db4d332a8-6b52-47be-ac35-8ef843d8e39d&width=300&dpr=4&quality=100&sign=aba7f99&sv=2)] on the left-hand navigation.

2

###  

Give your package a name, description, and check the other settings in the panel that opens.

3

###  

Add Actions to your package by clicking [![](../_gitbook/imagece06.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FCL0U3r5I1aJobzvQ4axr%252FCleanShot%25202025-03-20%2520at%252016.08.59.png%3Falt%3Dmedia%26token%3Df0642111-1ebd-4f11-8cc0-a9cb7471f07f&width=300&dpr=4&quality=100&sign=36d808b7&sv=2)]

You can choose to either copy the action into the package, or move it.

You can also create new actions at this time specifically for your package.

4

###  

When your Package is ready, click Publish, and once publishing completes, you can add it to your workspace(s).

</div>

###  

Publishing

When you publish your Action, you\'ll be able to review and make any changes to the documentation and certain Action settings once more before going live.

Make sure to choose the appropriate access level for your Action.

**Public** - This Action will be available for anyone to browse for, install and use.

**Private** - This Action will not be available for distribution. Use this for specific Actions that you only want to use internally.

**Unlisted** - This Action will be available to anyone that has the URL, but will not be found when browsing available Actions.

###  

Settings Registry

Because Actions have no dependencies, each Action contains a Settings Registry, which is used in a similar manner to [environment variables](../the-function-stack/environment-variables.html). You will use the Settings Registry for situations where an Action requires an API key or other sensitive data that you need to ensure users of the Action supply without supplying it yourself.

To add a new value to the Settings Registry, just add a new input to your Action. In the settings for that input, you\'ll see a new option in the **Configuration** section called Settings Registry.

![](../_gitbook/imageecca.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FM2SFknHWLhfd51ekB8UG%252FCleanShot%25202024-10-15%2520at%252022.25.36%25402x.png%3Falt%3Dmedia%26token%3D3814d73d-db16-4d04-9502-7c170961ea54&width=768&dpr=4&quality=100&sign=e6d7b210&sv=2)

Checking this box will mark this input as part of the Settings Registry, enabling you to provide your own data for testing and make sure it is apparent when these values need to be provided for others utilizing the Action you are building.

###  

Deleting an Action

Please note that deleting an action does not impact users who have already imported your action into their workspace.

Click the settings icon in the top-right of your published action, and click Delete Action**.**

![](../_gitbook/image1c99.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FLJGoeiSylOjfnjtFYmDy%252FCleanShot%25202024-10-29%2520at%252013.44.11.png%3Falt%3Dmedia%26token%3D2f5b5bcd-e87c-45bb-a631-90a66c8dade8&width=768&dpr=4&quality=100&sign=4145997&sv=2)

Think of projects as a folder for related actions to reside in. They are necessary for any actions you create, and include a number of helpful features to keep you organized.

###  

Actions

![](../_gitbook/imageb0c8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FssFdKeniB9a2FYTNPlq3%252FCleanShot%25202024-10-10%2520at%252009.50.01%25402x.png%3Falt%3Dmedia%26token%3D57e6f7b5-5b4c-40a5-9515-20f6882a007d&width=768&dpr=4&quality=100&sign=f2f8af9&sv=2)

Your project can have multiple Actions inside of it. You can add new actions to a Project by clicking Create Action inside of the Project.

###  

Members

![](../_gitbook/image1735.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FRUgn592zAWQI9wzv9rWV%252FCleanShot%25202024-10-10%2520at%252009.50.18%25402x.png%3Falt%3Dmedia%26token%3D261534bd-af78-4d72-89da-3339b04c25ea&width=768&dpr=4&quality=100&sign=8e25cbfa&sv=2)

You can invite collaborators to a Project that you own by clicking the **Invite Collaborators** button.

Once you\'ve sent an invite, it will show up on the Members screen, as shown below.

![](../_gitbook/image3130.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8vaTLfZJEiYy4MN3Nc8l%252FCleanShot%25202024-10-04%2520at%252017.35.59.png%3Falt%3Dmedia%26token%3D0532575c-8e04-4c3a-ada9-904c5249adfb&width=768&dpr=4&quality=100&sign=d5d4f571&sv=2)

The invitee will receive an email similar to the one below allowing them to accept the invitation.

![](../_gitbook/imageaa1c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FdYGTKYhoOpOlKoq1GKwc%252FCleanShot%25202024-10-04%2520at%252017.36.47.png%3Falt%3Dmedia%26token%3D2c7b95eb-6fc6-4017-95ab-231c34600fa2&width=768&dpr=4&quality=100&sign=b962c202&sv=2)

###  

Settings

![](../_gitbook/imaged505.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FgTooTO7oeqHxRuNRRzVp%252FCleanShot%25202024-10-10%2520at%252009.50.38%25402x.png%3Falt%3Dmedia%26token%3D45b80bec-c198-4956-b1e3-308304fd5a00&width=768&dpr=4&quality=100&sign=d8b8f6&sv=2)

**Name** - The name of your project

**Custom Project ID** - You can assign a custom ID to your project here. The project ID determines the slug, or portion of the URL, that leads to the project.

**Description** - A description of your project

From this screen, you can also delete your project.

Last updated 2 months ago

Was this helpful?