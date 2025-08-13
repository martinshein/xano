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
title: '[![](_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fg'
---

[![](_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)![](_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Favatar-1626464608697.png%3Fgeneration%3D1626464608902290%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=ed8a4004&sv=2)](index.html)















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
            
            -   [Swagger (OpenAPI Documentation)](the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](the-function-stack/building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](the-function-stack/building-with-visual-development/background-tasks.html)
        -   [Triggers](the-function-stack/building-with-visual-development/triggers.html)
        -   [Middleware](the-function-stack/building-with-visual-development/middleware.html)
        -   [Configuring Expressions](the-function-stack/building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](the-function-stack/building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](the-function-stack/functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](the-function-stack/functions/database-requests/get-record.html)
            -   [Add Record](the-function-stack/functions/database-requests/add-record.html)
            -   [Edit Record](the-function-stack/functions/database-requests/edit-record.html)
            -   [Add or Edit Record](the-function-stack/functions/database-requests/add-or-edit-record.html)
            -   [Patch Record](the-function-stack/functions/database-requests/patch-record.html)
            -   [Delete Record](the-function-stack/functions/database-requests/delete-record.html)
            -   [Bulk Operations](the-function-stack/functions/database-requests/bulk-operations.html)
            -   [Database Transaction](the-function-stack/functions/database-requests/database-transaction.html)
            -   [External Database Query](the-function-stack/functions/database-requests/external-database-query.html)
            -   [Direct Database Query](the-function-stack/functions/database-requests/direct-database-query.html)
            -   [Get Database Schema](the-function-stack/functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](the-function-stack/functions/data-manipulation/create-variable.html)
            -   [Update Variable](the-function-stack/functions/data-manipulation/update-variable.html)
            -   [Conditional](the-function-stack/functions/data-manipulation/conditional.html)
            -   [Switch](the-function-stack/functions/data-manipulation/switch.html)
            -   [Loops](the-function-stack/functions/data-manipulation/loops.html)
            -   [Math](the-function-stack/functions/data-manipulation/math.html)
            -   [Arrays](the-function-stack/functions/data-manipulation/arrays.html)
            -   [Objects](the-function-stack/functions/data-manipulation/objects.html)
            -   [Text](the-function-stack/functions/data-manipulation/text.html)
                    -   [Security](the-function-stack/functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](the-function-stack/functions/apis-and-lambdas/realtime-functions.html)
            -   [External API Request](the-function-stack/functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](the-function-stack/functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](the-function-stack/functions/data-caching-redis.html)
        -   [Custom Functions](the-function-stack/functions/custom-functions.html)
        -   [Utility Functions](the-function-stack/functions/utility-functions.html)
        -   [File Storage](the-function-stack/functions/file-storage.html)
        -   [Cloud Services](the-function-stack/functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](the-function-stack/filters/manipulation.html)
        -   [Math](the-function-stack/filters/math.html)
        -   [Timestamp](the-function-stack/filters/timestamp.html)
        -   [Text](the-function-stack/filters/text.html)
        -   [Array](the-function-stack/filters/array.html)
        -   [Transform](the-function-stack/filters/transform.html)
        -   [Conversion](the-function-stack/filters/conversion.html)
        -   [Comparison](the-function-stack/filters/comparison.html)
        -   [Security](the-function-stack/filters/security.html)
            -   Data Types
        
        -   [Text](the-function-stack/data-types/text.html)
        -   [Expression](the-function-stack/data-types/expression.html)
        -   [Array](the-function-stack/data-types/array.html)
        -   [Object](the-function-stack/data-types/object.html)
        -   [Integer](the-function-stack/data-types/integer.html)
        -   [Decimal](the-function-stack/data-types/decimal.html)
        -   [Boolean](the-function-stack/data-types/boolean.html)
        -   [Timestamp](the-function-stack/data-types/timestamp.html)
        -   [Null](the-function-stack/data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response Caching](the-function-stack/additional-features/response-caching.html)
        
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
        
        -   [Using the Xano Database](the-database/database-basics/using-the-xano-database.html)
        -   [Field Types](the-database/database-basics/field-types.html)
        -   [Relationships](the-database/database-basics/relationships.html)
        -   [Database Views](the-database/database-basics/database-views.html)
        -   [Export and Sharing](the-database/database-basics/export-and-sharing.html)
        -   [Data Sources](the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema Versioning](the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting Clients](ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP Functions](ai-tools/mcp-builder/mcp-functions.html)
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
        
        -   [Separating User Data](building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
        
        -   [Release Track Preferences](xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP (Outgoing)](xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server Region](xano-features/instance-settings/change-server-region.html)
        -   [Direct Database Connector](xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and Restore](xano-features/instance-settings/backup-and-restore.html)
        -   [Security Policy](xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit Logs](xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano Link](xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API (Deprecated)](xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata API](xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and Schema](xano-features/metadata-api/tables-and-schema.html)
        -   [Content](xano-features/metadata-api/content.html)
        -   [Search](xano-features/metadata-api/search.html)
        -   [File](xano-features/metadata-api/file.html)
        -   [Request History](xano-features/metadata-api/request-history.html)
        -   [Workspace Import and Export](xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes Reference](xano-features/metadata-api/token-scopes-reference.html)
        
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
        
        -   [Agency Dashboard](agencies/agency-features/agency-dashboard.html)
        -   [Client Invite](agencies/agency-features/client-invite.html)
        -   [Transfer Ownership](agencies/agency-features/transfer-ownership.html)
        -   [Agency Profile](agencies/agency-features/agency-profile.html)
        -   [Commission](agencies/agency-features/commission.html)
        -   [Private Marketplace](agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a Model](enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant Center](enterprise/enterprise-features/tenant-center.html)
        -   [Compliance Center](enterprise/enterprise-features/compliance-center.html)
        -   [Security Policy](enterprise/enterprise-features/security-policy.html)
        -   [Instance Activity](enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access Control)](enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano Link](enterprise/enterprise-features/xano-link.html)
        -   [Resource Management](enterprise/enterprise-features/resource-management.html)
        
-   
    Your Xano Account
    
    -   Account Page
    -   Billing
    -   Referrals & Commissions

-   
    Troubleshooting & Support
    
    -   Error Reference
    -   Troubleshooting Performance
        
        -   [When a single workflow feels slow](troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels slow](troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM Usage](troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack Performance](troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting Access](troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of Conduct](troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification Policy](troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and Issues](troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
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
    
    [What is Xano?](#what-is-xano)

-   [What can I use Xano for?](#what-can-i-use-xano-for)

-   [How does Xano compare to other tools?](#how-does-xano-compare-to-other-tools)

-   [Can I build an Enterprise-grade backend using Xano?](#can-i-build-an-enterprise-grade-backend-using-xano)

-   [How does Xano make sure my data stays secure?](#how-does-xano-make-sure-my-data-stays-secure)

-   [Who owns my data and what I build on Xano?](#who-owns-my-data-and-what-i-build-on-xano)

-   [What happens if Xano shuts down?](#what-happens-if-xano-shuts-down)

-   [How do I get help?](#how-do-i-get-help)

-   [Have more questions?](#have-more-questions)

Was this helpful?

Copy


==================================================================

 

What is Xano?

Xano is, at its core, a visual development platform for building backend solutions. Think of the backend as the powerhouse behind your application or website that handles all of the heavy lifting, data processing, and workflows.

 

What can I use Xano for?

Xano is inherently very flexible. Here\'s what some of our users are utilizing Xano for:

-   
    
        
    
    Complete backend systems
    
-   
    
        
    
    Connecting multiple services together
    
-   
    
        
    
    A data warehouse
    
-   
    
        
    
    Supplementing an existing system (building and deploying microservices)
    
 

How can I generate a backend using AI?

-   
    
        
    
    **Getting Started Assistant**

    -   
        
                
        
        When you create a new workspace in Xano, our Getting Started Assistant will take your idea and generate a database, tables, user authentication, and even basic API endpoints that you can use right away.
        [Get Started Assistant](xano-ai/get-started-assistant.html)
            
-   
    
        
    
    **Database Assistant**

    -   
        
                
        
        After you\'ve started working in Xano, you can continue the conversation with our Database Assistant, designed to talk through and perform updates to your database and tables. Let it know what changes you want to make, review each suggestion for accuracy, and apply them with one click.
        [AI Database Assistant](xano-ai/ai-database-assistant.html)
            
-   
    
        
    
    **SQL Assistant**

    -   
        
                
        
        Now that your backend is up and running, maybe you\'d like to add some additional, more complex database queries to your APIs. Our SQL Assistant can take your idea, generate a query to retrieve exactly the data you\'re looking for, and even display a list of results to make sure it\'s exactly what you need.
        [AI SQL Assistant](xano-ai/ai-sql-assistant.html)
            
-   
    
        
    
    **Lambda Assistant**

    -   
        
                
        
        Our Lambda Assistant is designed to help you write and iterate on Lambda functions. It can take a prompt and generate code for you, with context of the rest of your function stack, as well as importing any external NPM packages required. This is useful for scenarios where you\'d like to add features to your backend that Xano doesn\'t support natively, such as image manipulation or PDF generation.
        [AI Lambda Assistant](xano-ai/ai-lambda-assistant.html)
            
------------------------------------------------------------------------

 

How Xano AI handles your data

Your data stays yours. We process it to generate AI responses but don\'t store it or use it to train our models. Third parties that help run our AI only collect basic usage data for billing.

**You can view our full AI Terms & Conditions** [**here**](https://legal.xano.com/ai-terms)**.**

 

How does Xano compare to other tools?

At a high level, Xano is a complete backend platform with a focus on visual development. That means that we don\'t just focus on the database, nor do we just focus on workflows, and a technical background is not required.

Xano also adopts a flat monthly pricing structure, which means that you never have to worry about overages or surprises.

Check out the links below for more specific comparisons to your tool of choice.

[🔗] [**Xano vs Supabase**](https://www.xano.com/versus/xano-vs-supabase/)
[🔗] [**Xano vs Airtable**](https://www.xano.com/versus/xano-vs-airtable/)
[🔗] [**Xano vs Bubble**](https://www.xano.com/versus/xano-vs-bubble/)

 

Can I build an Enterprise-grade backend using Xano?

**Yes!** Xano is trusted by [many](https://www.xano.com/enterprise/) large-scale organizations, such as Qualtrics, Fluence Energy, and Heimstaden to supply their backend systems needs.

 

How does Xano make sure my data stays secure?



 

Who owns my data and what I build on Xano?

**You do.** Xano claims no ownership over what is built using our platform or any data that is ingested or distributed via your backend built on Xano.

 

What happens if Xano shuts down?

We have a comprehensive [exit plan](https://legal.xano.com/#exit-plan) in place in the unexpected scenario where we can no longer offer our services.

 

How do I get help?

-   
    
        
    
    **Check out the Xano YouTube Channel**

    -   
        
                
        
        Our YouTube channel is always being updated with tutorials, use case examples, feature announcements, and more.
            
-   
    
        
    
    **Visit the Xano Community**

    -   
        
                
        

            
-   
    
        
    
    **Reach out to our support team**

    -   
        
                
        
        Just click the option in the lower-left corner anywhere in Xano to be connected to our support team, 24 hours a day.
            
-   
    
        
    
    **Join us for an Office Hours session**

    -   
        
                
        

            
 

Have more questions?

Check out the additional sections below for more specific FAQs about Xano.

Scaling and Limits

**Does Xano rate limit?**

Only on our free Build plan. Any paid subscription plan does not include a rate limit, but may be limited if your use case or other specifics based on your requirements do not align with the Xano plan you are subscribed to.

**How can I increase the capacity / resources available to my backend?**

Just log in to your Xano account, head to your Billing screen, and choose a higher-tier plan. The change will go into effect immediately, bringing you almost instant results. If you are not sure which plan is the right fit for you, please reach out to our support team.

**Is there anything I can\'t build in Xano?**

Xano is designed to be turing complete, meaning that you can build anything in Xano that you could with traditional programming languages.

Data Management

**Can I export my data?**

You can always export your data from Xano via CSV, a direct database connection, or via an API endpoint. The functions and workflows you build in Xano can also be exported, however it is not considered portable (meaning they are not exported as standard code).

**Can I bring my data into Xano?**

**Yes!** We have multiple methods to bring your existing data into Xano, including CSV import, direct database connection, and via an API endpoint.

**Can I migrate from another platform to Xano?**

We have many different ways to bring your data from other platforms into Xano. Check out the [Migrating Your Data](the-database/migrating-your-data.html) section to learn more.

Billing & Account

**Can I pause my Xano subscription?**

Xano subscriptions can not be paused. If you\'re having difficulties, please reach out to our support team for assistance.

**What happens if I cancel my subscription?**

You will continue to retain access to Xano until the end of your subscription period.

**What is Xano\'s refund policy?**

Xano does not offer refunds on monthly plans. We may offer a refund on a yearly subscription during the first thirty days depending on the circumstances. Refunds are not processed automatically upon cancellation; you need to reach out to our support team **before you cancel** to process your request.

**Can I downgrade back to a free plan?**

Due to technical limitations in our current infrastructure, it is not currently possible to directly downgrade from a paid plan back to a free plan.

Last updated 7 days ago

Was this helpful?