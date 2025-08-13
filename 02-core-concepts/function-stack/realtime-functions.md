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
                
                -   [External Filtering Examples](../database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](../database-requests/get-record.html)
            -   [Add Record](../database-requests/add-record.html)
            -   [Edit Record](../database-requests/edit-record.html)
            -   [Add or Edit Record](../database-requests/add-or-edit-record.html)
            -   [Patch Record](../database-requests/patch-record.html)
            -   [Delete Record](../database-requests/delete-record.html)
            -   [Bulk Operations](../database-requests/bulk-operations.html)
            -   [Database Transaction](../database-requests/database-transaction.html)
            -   [External Database Query](../database-requests/external-database-query.html)
            -   [Direct Database Query](../database-requests/direct-database-query.html)
            -   [Get Database Schema](../database-requests/get-database-schema.html)
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
            
            -   [Realtime Functions](realtime-functions.html)
            -   [External API Request](external-api-request.html)
            -   [Lambda Functions](lambda-functions.html)
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

-   
    
    [Using the Realtime Event Function](#using-the-realtime-event-function)

-   [Example](#example)

Was this helpful?

Copy


2.  Functions
3.  [APIs & Lambdas](../apis-and-lambdas.html)

Realtime Functions 
==================

While Realtime is fully functional without implementing anything in your function stacks, you may find yourself wanting to build function stacks to extend the functionality of Realtime.

This is possible with the new **Realtime Event** function, located under APIs & Lambdas in the function panel.

![](../../../_gitbook/image8ba1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FZSrJiRGGzswk17ROUB0w%252FCleanShot%25202024-05-09%2520at%252016.38.39.png%3Falt%3Dmedia%26token%3D106180b6-203b-4052-93f5-5be60877a8de&width=768&dpr=4&quality=100&sign=68f8350d&sv=2)

###  

Using the Realtime Event Function

This function sends a message of type \'event\' to the channel specified. Remember, a message can be anything from plain text to a JSON object for even further flexibility.

![](../../../_gitbook/imagea21e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FGkvvDibOl0YasHIOLOTN%252FCleanShot%25202024-05-09%2520at%252017.02.27.png%3Falt%3Dmedia%26token%3D97973ece-7e6f-45b6-a1e0-468414a71f77&width=768&dpr=4&quality=100&sign=acba2bc3&sv=2)

**Channel** - The channel to send the event to

**Data** - The payload of the event

**Database** - If this channel requires authentication, select the corresponding database that handles your authentication here

You can use variables for Channel and Data to make the event behave dynamically.

Please note that Event is different than Message, and will need to be handled accordingly by your frontend.

###  

Example

Realtime connections do not log message history. This means that once a user leaves our Marvel chat room, if they come back, they won\'t be able to see any of the previous messages. So, we want to store our messages in a database table as they are sent to the channel.

We could approach this in a couple of different ways.

1.  
    
        
    
    Have our frontend send an API request at the same time a message is sent to the channel to log the message.
    
2.  
    
        
    
    Have our frontend only send an API request, and our API can handle delivering the message once it is stored.
    
For this example, we will use the second option. We need to first modify our frontend code to send the API request, instead of sending the message directly to the channel. We\'ll do this by defining a new function and then calling it when our button is clicked.

Copy

``` 
function sendMessageToRealtime(channel, message) {
        fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json'
           },
        body: JSON.stringify({
        channel: 'your_channel_name',
        message: 'your_message'
    })
  });
}

document.getElementById('form').addEventListener('submit', (event) => );
```

**Code Explanation**

First, we define the function and make sure we define two parameters: channel for the channel to send the message to, and message for the message body.

Copy

``` 
function sendMessageToRealtime(channel, message) 
fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json'
           },
        body: JSON.stringify({
        channel: channel,
        message: message
    })
  });
```

Now, we need to handle what happens when our Send button is clicked. We\'ll start by looking for that element and adding an event listener to it. It just looks for our form, which has an ID of form, and a submit button inside of it.

Copy

``` 
document.getElementById('form').addEventListener('submit', (event) => 
event.preventDefault();
```

Next, we\'ll call our sendMessageToRealtime function and give it our \'marvel-chat-room\' channel name and the value of the message input box. Right after that, we clear the input to prepare for the next message.

Copy

``` 
sendMessageToRealtime('marvel_chat_room', document.getElementById(event.target.message.value))
event.target.message.value = '';
```

We need to set up a database table to log the messages.

![](../../../_gitbook/imagef4c1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FEiAisWVCFDLiPL2XAgpG%252FCleanShot%25202024-05-09%2520at%252019.18.59%25402x.png%3Falt%3Dmedia%26token%3Dac5bdba0-ffaa-48db-af90-cae95b86c986&width=768&dpr=4&quality=100&sign=43dbf174&sv=2)

Here\'s the API endpoint we are sending these requests to.

![](../../../_gitbook/image406b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F2WBDfT6794EAefkyyS1q%252FCleanShot%25202024-05-09%2520at%252019.20.06%25402x.png%3Falt%3Dmedia%26token%3D076f85a5-37c3-4e0b-9dfa-863e12edd939&width=768&dpr=4&quality=100&sign=e0b052ed&sv=2)

![](../../../_gitbook/imaged4e6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F95dVJsGCzUopt4wEZH2L%252FCleanShot%25202024-05-09%2520at%252019.26.11%25402x.png%3Falt%3Dmedia%26token%3Da84204ce-e9a7-4dec-94c9-4c4f7b744d07&width=768&dpr=4&quality=100&sign=d24c5186&sv=2)

This endpoint takes in the channel name and message data, fires our Realtime Event function, and then stores the message in the database table.

At this point, we have modified our frontend code and set up the API in Xano to handle the requests. Now, when our users send messages, they will be logged in the database table, and we still get all of the benefits of utilizing the realtime connection.

Last updated 6 months ago

Was this helpful?