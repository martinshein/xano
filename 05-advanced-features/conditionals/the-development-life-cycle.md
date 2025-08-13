---
category: conditionals
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 05-advanced-features/conditionals
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
- crud
- function
- background-task
- custom-function
- rest
- database
title: '[![](../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%'
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
            
            -   [Swagger (OpenAPI
                Documentation)](../the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async
                Functions](../the-function-stack/building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background
            Tasks](../the-function-stack/building-with-visual-development/background-tasks.html)
        -   [Triggers](../the-function-stack/building-with-visual-development/triggers.html)
        -   [Middleware](../the-function-stack/building-with-visual-development/middleware.html)
        -   [Configuring
            Expressions](../the-function-stack/building-with-visual-development/configuring-expressions.html)
        -   [Working with
            Data](../the-function-stack/building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI
            Tools](../the-function-stack/functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering
                    Examples](../the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get
                Record](../the-function-stack/functions/database-requests/get-record.html)
            -   [Add
                Record](../the-function-stack/functions/database-requests/add-record.html)
            -   [Edit
                Record](../the-function-stack/functions/database-requests/edit-record.html)
            -   [Add or Edit
                Record](../the-function-stack/functions/database-requests/add-or-edit-record.html)
            -   [Patch
                Record](../the-function-stack/functions/database-requests/patch-record.html)
            -   [Delete
                Record](../the-function-stack/functions/database-requests/delete-record.html)
            -   [Bulk
                Operations](../the-function-stack/functions/database-requests/bulk-operations.html)
            -   [Database
                Transaction](../the-function-stack/functions/database-requests/database-transaction.html)
            -   [External Database
                Query](../the-function-stack/functions/database-requests/external-database-query.html)
            -   [Direct Database
                Query](../the-function-stack/functions/database-requests/direct-database-query.html)
            -   [Get Database
                Schema](../the-function-stack/functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create
                Variable](../the-function-stack/functions/data-manipulation/create-variable.html)
            -   [Update
                Variable](../the-function-stack/functions/data-manipulation/update-variable.html)
            -   [Conditional](../the-function-stack/functions/data-manipulation/conditional.html)
            -   [Switch](../the-function-stack/functions/data-manipulation/switch.html)
            -   [Loops](../the-function-stack/functions/data-manipulation/loops.html)
            -   [Math](../the-function-stack/functions/data-manipulation/math.html)
            -   [Arrays](../the-function-stack/functions/data-manipulation/arrays.html)
            -   [Objects](../the-function-stack/functions/data-manipulation/objects.html)
            -   [Text](../the-function-stack/functions/data-manipulation/text.html)
                    -   [Security](../the-function-stack/functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime
                Functions](../the-function-stack/functions/apis-and-lambdas/realtime-functions.html)
            -   [External API
                Request](../the-function-stack/functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda
                Functions](../the-function-stack/functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching
            (Redis)](../the-function-stack/functions/data-caching-redis.html)
        -   [Custom
            Functions](../the-function-stack/functions/custom-functions.html)
        -   [Utility
            Functions](../the-function-stack/functions/utility-functions.html)
        -   [File
            Storage](../the-function-stack/functions/file-storage.html)
        -   [Cloud
            Services](../the-function-stack/functions/cloud-services.html)
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
        
        -   [Response
            Caching](../the-function-stack/additional-features/response-caching.html)
        
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
        
        -   [Using the Xano
            Database](../the-database/database-basics/using-the-xano-database.html)
        -   [Field
            Types](../the-database/database-basics/field-types.html)
        -   [Relationships](../the-database/database-basics/relationships.html)
        -   [Database
            Views](../the-database/database-basics/database-views.html)
        -   [Export and
            Sharing](../the-database/database-basics/export-and-sharing.html)
        -   [Data
            Sources](../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to
            Xano](../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to
            Xano](../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import &
            Export](../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema
            Versioning](../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting
            Clients](../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP
            Functions](../ai-tools/mcp-builder/mcp-functions.html)
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
        
        -   [Separating User
            Data](../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access
            (RBAC)](../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth
            (SSO)](../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
        
        -   [Release Track
            Preferences](../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP
            (Outgoing)](../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server
            Region](../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database
            Connector](../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and
            Restore](../xano-features/instance-settings/backup-and-restore.html)
        -   [Security
            Policy](../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit
            Logs](../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano
            Link](../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API
            (Deprecated)](../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata
            API](../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and
            Schema](../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../xano-features/metadata-api/content.html)
        -   [Search](../xano-features/metadata-api/search.html)
        -   [File](../xano-features/metadata-api/file.html)
        -   [Request
            History](../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and
            Export](../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes
            Reference](../xano-features/metadata-api/token-scopes-reference.html)
        
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
        
        -   [Agency
            Dashboard](../agencies/agency-features/agency-dashboard.html)
        -   [Client
            Invite](../agencies/agency-features/client-invite.html)
        -   [Transfer
            Ownership](../agencies/agency-features/transfer-ownership.html)
        -   [Agency
            Profile](../agencies/agency-features/agency-profile.html)
        -   [Commission](../agencies/agency-features/commission.html)
        -   [Private
            Marketplace](../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a
                    Model](../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant
            Center](../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance
            Center](../enterprise/enterprise-features/compliance-center.html)
        -   [Security
            Policy](../enterprise/enterprise-features/security-policy.html)
        -   [Instance
            Activity](../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access
            Control)](../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano
            Link](../enterprise/enterprise-features/xano-link.html)
        -   [Resource
            Management](../enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels
            slow](../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels
            slow](../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM
            Usage](../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack
            Performance](../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting
            Access](../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of
            Conduct](../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification
            Policy](../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and
            Issues](../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
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

1.  [Before You
    Begin](using-these-docs.html)

The Development Life Cycle 
==========================

Learn more about the fundamentals of application development and the
software development life cycle.

Before you start building, we wanted to share some best practices around
how to think about creating your product or service. If you don\'t need
to learn this, you can go straight to [setting up your
Database](../the-database/getting-started-shortcuts.html).

![](../_gitbook/image5ea2.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FMVmZxBfrQvJ8AijWZnda%252Fimage.png%3Falt%3Dmedia%26token%3D8b086ef6-1c1f-4ec3-89dd-79e1d033fce8&width=768&dpr=4&quality=100&sign=34f68383&sv=2)

A visual representation of the Software Development Life Cycle

When you have an idea for an app or a project that you\'d like to build,
it\'s easy to feel overwhelmed and not even know where to begin.
Regardless of whether you\'re on your own or with a team, it\'s
important to have a framework around how you approach designing,
launching, and maintaining your application. Luckily, when building in
Xano, you can leverage a tried and tested methodology called the
**Software Development Life Cycle (SDLC)**.

**There are** **six phases** to the Software Development Life cycle**,**
and Xano was designed to support you and your team through each one.

![](../_gitbook/image9c8d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FjQGX366vbHomF1fd3o2r%252Fimage.png%3Falt%3Dmedia%26token%3D859c05cd-bfc9-4a11-acbc-b8a93c56123b&width=768&dpr=4&quality=100&sign=ea923b66&sv=2)

A visual representation of the Software Development Life Cycle

Planning / Analysis

The first stage of the SLDC usually consists of two parts: **planning**
and **analysis**. Gather requirements passively or actively from
potential customers or other relevant stakeholders, and ensure you are
solving a real problem. You would then be able to analyze the
feasibility of creating the product, revenue potential, cost, and more.

Once you decide what you\'re building is in line with stakeholder goals,
addresses user needs, and is feasible to create, you can move to the
second stage.

Design

The design phase is where you start to put your ideas to paper. This
might include creating actual designs in a tool like
[Figma](https://www.figma.com/), or going higher level and using a tool like
[Miro](https://miro.com/) to create a wireframe or flowchart. From a Xano
perspective, this is where you would start designing a data model.

Development

With a solid foundation to work with, this phase is where the actual
development happens and where you turn specifications and designs into
an actual product. This phase usually takes the most time, so setting
expectations with yourself and the stakeholders you are working with is
important.

Xano helps accelerate this stage with features like:

-   
    
        
    
    [Generation of API CRUD
    Operations](../the-function-stack/building-with-visual-development/apis.html)
    
-   
    
        
    
    [Auto-Documentation](../the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html)
    
-   
    
        
    
    [Real-time
    Collaboration](../team-collaboration/realtime-collaboration.html)
    
If you\'re working with a team, you can leverage Xano features like
[real-time
collaboration](../team-collaboration/realtime-collaboration.html) to seamlessly work within the same workspace, or create
[Branches and
Merge](../team-collaboration/branching-and-merging.html) them in when you\'re ready to move to the testing phase.

Testing

Before launching any product or service, it\'s important to have
everything tested. At this phase, you would have a quality assurance
(QA) team step in to run tests, but if you\'re on your own, you\'ll need
to think through every part of testing your product which is more than
just fixing critical bugs.

This might sound easier than it seems, but it\'s essential to test all
the different permutations and ways that your users might interact with
your application. Here are some different types of testing that you can
do in this phase.

-   
    
        
    
    **Performance testing** Is your product ready to handle the
    traffic/storage requirements?
    
-   
    
        
    
    **Functional testing** Does your application meet the requirements
    set for in the Planning/Analysis phase?
    
-   
    
        
    
    **Security testing** Is your data in a secure place, and do you meet
    the appropriate compliance certifications within your country, or if
    you\'re dealing with sensitive data?
    
-   
    
        
    
    **Unit testing** Does every part of your app work the way it\'s
    supposed to?
    
-   
    
        
    
    **Usability testing** Do your users actually understand how to use
    your app?
    
**Xano provides a few features to help you in this phase**. Using [Unit
Tests](../testing-debugging/unit-tests.html), [Test
Suites](../testing-debugging/test-suites.html) and [Data
Sources](../the-database/database-basics/data-sources.html) can help you use dummy data without affecting what will
be live in production. We support drafts to help you and your team get
things right before Publishing.
[Branches](../team-collaboration/branching-and-merging.html) can be used to create separate testing environments
(Development, Staging, Production). For more complex use cases, Xano
also supports [Xano
Link](../xano-features/advanced-back-end-features/xano-link.html), which allows you to keep all of your Workspaces and
Instances in sync with a master so your customers have a consistent
experience.

Deployment

The Deployment stage is where your product or service is shipped to its
intended user(s). This process can depend on the nature of what is being
released; however, it\'s best practice to launch to a small set of users
(typically called a canary release).

Maintenance

Maintenance is typically the last stage of the SDLC; however, in
today\'s world, people are moving toward a more [Agile software
development](https://monday.com/blog/rnd/agile-sdlc/) approach where the product or service is continually
improved, and sometimes the feedback from users makes it necessary to go
back to the first step of the SDLC. This is why most images of the SDLC
that you find are circular because it is a process that keeps repeating
itself once you find something that\'s working.

Last updated 3 months ago

Was this helpful?