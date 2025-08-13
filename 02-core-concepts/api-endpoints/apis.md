---
category: api-endpoints
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/api-endpoints
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
- cache
- transaction
- crud
- function
- background-task
- custom-function
- rest
- database
title: '[![](../../_gitbook/image771a.jpg?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2'
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
            
            -   [Swagger (OpenAPI
                Documentation)](apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async
                Functions](custom-functions/async-functions.html)
                    -   [Background Tasks](background-tasks.html)
        -   [Triggers](triggers.html)
        -   [Middleware](middleware.html)
        -   [Configuring
            Expressions](configuring-expressions.html)
        -   [Working with Data](working-with-data.html)
            -   Functions
        
        -   [AI Tools](../functions/ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering
                    Examples](../functions/database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get
                Record](../functions/database-requests/get-record.html)
            -   [Add
                Record](../functions/database-requests/add-record.html)
            -   [Edit
                Record](../functions/database-requests/edit-record.html)
            -   [Add or Edit
                Record](../functions/database-requests/add-or-edit-record.html)
            -   [Patch
                Record](../functions/database-requests/patch-record.html)
            -   [Delete
                Record](../functions/database-requests/delete-record.html)
            -   [Bulk
                Operations](../functions/database-requests/bulk-operations.html)
            -   [Database
                Transaction](../functions/database-requests/database-transaction.html)
            -   [External Database
                Query](../functions/database-requests/external-database-query.html)
            -   [Direct Database
                Query](../functions/database-requests/direct-database-query.html)
            -   [Get Database
                Schema](../functions/database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create
                Variable](../functions/data-manipulation/create-variable.html)
            -   [Update
                Variable](../functions/data-manipulation/update-variable.html)
            -   [Conditional](../functions/data-manipulation/conditional.html)
            -   [Switch](../functions/data-manipulation/switch.html)
            -   [Loops](../functions/data-manipulation/loops.html)
            -   [Math](../functions/data-manipulation/math.html)
            -   [Arrays](../functions/data-manipulation/arrays.html)
            -   [Objects](../functions/data-manipulation/objects.html)
            -   [Text](../functions/data-manipulation/text.html)
                    -   [Security](../functions/security.html)
        -   APIs & Lambdas
            
            -   [Realtime
                Functions](../functions/apis-and-lambdas/realtime-functions.html)
            -   [External API
                Request](../functions/apis-and-lambdas/external-api-request.html)
            -   [Lambda
                Functions](../functions/apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching
            (Redis)](../functions/data-caching-redis.html)
        -   [Custom
            Functions](../functions/custom-functions.html)
        -   [Utility
            Functions](../functions/utility-functions.html)
        -   [File
            Storage](../functions/file-storage.html)
        -   [Cloud
            Services](../functions/cloud-services.html)
            -   Filters
        
        -   [Manipulation](../filters/manipulation.html)
        -   [Math](../filters/math.html)
        -   [Timestamp](../filters/timestamp.html)
        -   [Text](../filters/text.html)
        -   [Array](../filters/array.html)
        -   [Transform](../filters/transform.html)
        -   [Conversion](../filters/conversion.html)
        -   [Comparison](../filters/comparison.html)
        -   [Security](../filters/security.html)
            -   Data Types
        
        -   [Text](../data-types/text.html)
        -   [Expression](../data-types/expression.html)
        -   [Array](../data-types/array.html)
        -   [Object](../data-types/object.html)
        -   [Integer](../data-types/integer.html)
        -   [Decimal](../data-types/decimal.html)
        -   [Boolean](../data-types/boolean.html)
        -   [Timestamp](../data-types/timestamp.html)
        -   [Null](../data-types/null.html)
            -   Environment Variables
    -   Additional Features
        
        -   [Response
            Caching](../additional-features/response-caching.html)
        
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
            Database](../../the-database/database-basics/using-the-xano-database.html)
        -   [Field
            Types](../../the-database/database-basics/field-types.html)
        -   [Relationships](../../the-database/database-basics/relationships.html)
        -   [Database
            Views](../../the-database/database-basics/database-views.html)
        -   [Export and
            Sharing](../../the-database/database-basics/export-and-sharing.html)
        -   [Data
            Sources](../../the-database/database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to
            Xano](../../the-database/migrating-your-data/airtable-to-xano.html)
        -   [Supabase to
            Xano](../../the-database/migrating-your-data/supabase-to-xano.html)
        -   [CSV Import &
            Export](../../the-database/migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](../../the-database/database-performance-and-maintenance/storage.html)
        -   [Indexing](../../the-database/database-performance-and-maintenance/indexing.html)
        -   [Maintenance](../../the-database/database-performance-and-maintenance/maintenance.html)
        -   [Schema
            Versioning](../../the-database/database-performance-and-maintenance/schema-versioning.html)
        
-   CI/CD

-   
    Build For AI
    
    -   Agents
        
        -   [Templates](../../ai-tools/agents/templates.html)
            -   MCP Builder
        
        -   [Connecting
            Clients](../../ai-tools/mcp-builder/connecting-clients.html)
        -   [MCP
            Functions](../../ai-tools/mcp-builder/mcp-functions.html)
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
            Data](../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access
            (RBAC)](../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth
            (SSO)](../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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
            Preferences](../../xano-features/instance-settings/release-track-preferences.html)
        -   [Static IP
            (Outgoing)](../../xano-features/instance-settings/static-ip-outgoing.html)
        -   [Change Server
            Region](../../xano-features/instance-settings/change-server-region.html)
        -   [Direct Database
            Connector](../../xano-features/instance-settings/direct-database-connector.html)
        -   [Backup and
            Restore](../../xano-features/instance-settings/backup-and-restore.html)
        -   [Security
            Policy](../../xano-features/instance-settings/security-policy.html)
            -   Workspace Settings
        
        -   [Audit
            Logs](../../xano-features/workspace-settings/audit-logs.html)
            -   Advanced Back-end Features
        
        -   [Xano
            Link](../../xano-features/advanced-back-end-features/xano-link.html)
        -   [Developer API
            (Deprecated)](../../xano-features/advanced-back-end-features/developer-api-deprecated.html)
            -   Metadata API
        
        -   [Master Metadata
            API](../../xano-features/metadata-api/master-metadata-api.html)
        -   [Tables and
            Schema](../../xano-features/metadata-api/tables-and-schema.html)
        -   [Content](../../xano-features/metadata-api/content.html)
        -   [Search](../../xano-features/metadata-api/search.html)
        -   [File](../../xano-features/metadata-api/file.html)
        -   [Request
            History](../../xano-features/metadata-api/request-history.html)
        -   [Workspace Import and
            Export](../../xano-features/metadata-api/workspace-import-and-export.html)
        -   [Token Scopes
            Reference](../../xano-features/metadata-api/token-scopes-reference.html)
        
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
            Dashboard](../../agencies/agency-features/agency-dashboard.html)
        -   [Client
            Invite](../../agencies/agency-features/client-invite.html)
        -   [Transfer
            Ownership](../../agencies/agency-features/transfer-ownership.html)
        -   [Agency
            Profile](../../agencies/agency-features/agency-profile.html)
        -   [Commission](../../agencies/agency-features/commission.html)
        -   [Private
            Marketplace](../../agencies/agency-features/private-marketplace.html)
        
-   
    Custom Plans (Enterprise)
    
    -   Xano for Enterprise (Custom Plans)
    -   Custom Plan Features
        
        -   Microservices
            
            -   Ollama
                
                -   [Choosing a
                    Model](../../enterprise/enterprise-features/microservices/ollama/choosing-a-model.html)
                                    -   [Tenant
            Center](../../enterprise/enterprise-features/tenant-center.html)
        -   [Compliance
            Center](../../enterprise/enterprise-features/compliance-center.html)
        -   [Security
            Policy](../../enterprise/enterprise-features/security-policy.html)
        -   [Instance
            Activity](../../enterprise/enterprise-features/instance-activity.html)
        -   [Deployment](../../enterprise/enterprise-features/deployment.html)
        -   [RBAC (Role-based Access
            Control)](../../enterprise/enterprise-features/rbac-role-based-access-control.html)
        -   [Xano
            Link](../../enterprise/enterprise-features/xano-link.html)
        -   [Resource
            Management](../../enterprise/enterprise-features/resource-management.html)
        
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
            slow](../../troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.html)
        -   [When everything feels
            slow](../../troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.html)
        -   [RAM
            Usage](../../troubleshooting-and-support/troubleshooting-performance/ram-usage.html)
        -   [Function Stack
            Performance](../../troubleshooting-and-support/troubleshooting-performance/function-stack-performance.html)
            -   Getting Help
        
        -   [Granting
            Access](../../troubleshooting-and-support/getting-help/granting-access.html)
        -   [Community Code of
            Conduct](../../troubleshooting-and-support/getting-help/community-code-of-conduct.html)
        -   [Community Content Modification
            Policy](../../troubleshooting-and-support/getting-help/community-content-modification-policy.html)
        -   [Reporting Potential Bugs and
            Issues](../../troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.html)
        
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
    
    [What is an API?](#what-is-an-api)

-   [Auto-generated APIs](#auto-generated-apis)

-   [CRUD Operations](#crud-operations)

-   [Authentication](#authentication)

-   [File Storage](#file-storage)

-   [Custom](#custom)

-   [API Groups & API Group
    Settings](#api-groups-and-api-group-settings)

-   [CORS Management for API
    Groups](#cors-management-for-api-groups)

-   [Creating a new API](#creating-a-new-api)

-   [Click to create a new API
    endpoint.](#click-to-create-a-new-api-endpoint)

-   [API Settings](#api-settings)

-   [From the Settings panel](#from-the-settings-panel)

Was this helpful?

Copy

1.  [[🛠️]The Visual
    Builder](../building-with-visual-development.html)
2.  Building with Visual Development

APIs 
====

Learn more about building APIs using visual development in Xano

**Quick Summary**

Think of an API like a waiter in a restaurant - you (the user) give your
order to the waiter (the API), who takes it to the kitchen and brings
back exactly what you asked for. The waiter creates a seamless
connection between you and the kitchen, just like an API connects
different parts of an application.

An API acts like a messenger between different parts of an application.
When your website needs something done (like creating a new user), it
sends a request with the necessary data and gets back a response
containing the results. Both requests and responses include headers
(which provide context) and data (the actual content being sent or
received).

 

What is an API?

APIs allow different applications to communicate and share data with
each other. When you use Google Maps inside another app, that\'s an API
at work. When you click a Buy Now button on Amazon, APIs are firing at
all cylinders behind the scenes.

APIs don\'t have to only be based on user action, either. For example,
most websites implement some sort of tracking to ensure that the user
experience is as smooth as possible. When you visit these websites,
there are API calls being made as you navigate through their frontend.

APIs set the rules for how different pieces of software can talk to each
other, making it possible for developers to integrate various services
without starting from scratch.

An API has a few main components.

<div>

1

###  

Headers

Headers are the configuration that rides along with an API request. They
contain information like where the request is coming from and what type
of data it contains.

2

###  

Method

The method, also known as the verb, is assigned to an API to typically
dictate the type of operation the API is designed to complete.

-   
    
        
    
    **GET**

    -   
        
                
        
        Retrieve data
            
-   
    
        
    
    **POST**

    -   
        
                
        
        Send data
            
-   
    
        
    
    **PUT / PATCH**

    -   
        
                
        
        Update data
            
-   
    
        
    
    **DELETE**

    -   
        
                
        
        Delete data
            

Please note that when you build APIs in Xano, you can choose the method
to apply, giving you full flexibility in exactly what function that API
serves. While it isn\'t always best practice, a DELETE endpoint could
technically do nothing but add new data, if it makes sense for your use
case.

3

###  

Query parameters / Request body

Query parameters and the request body are kind of the same thing, but
sent in an API request in different ways.

-   
    
        
    
    **Query parameters** live as part of the request URL. If the API URL
    is `https://myapi.com/getThings` and expects you to send a
    thingId with your request, you would append it to the URL with
    `?thingId=99`, so your full
    request URL would be
    `https://myapi.com/getThings?thingId=99.` You would typically use query
    parameters for GET and DELETE endpoints.
    
-   
    
        
    
    **Request Body** is like a set of query parameters, but sent as a
    JSON object. It\'s more flexible when sending complex data types,
    such as lists, nested objects, or files.
    
In the Xano visual builder, these are known as **inputs**. You can add
inputs manually, or add a **Database Link** input to automatically
populate and sync all fields from a database table.

4

###  

Response

The response is whatever the API sends back once it has completed the
logic it is meant to perform. An API doesn\'t necessarily need to
deliver a response, but it is typical.

Think of your frontend sending an API request when a user logs in. That
API request would probably return information about the user logging in,
such as their name, location, or other relevant user data.

A response has a few different pieces, similar to what\'s included in
the request, including **response headers** and a **response body**.

</div>

------------------------------------------------------------------------

 

Auto-generated APIs

When adding a new API endpoint in Xano, you have four options to choose
from --- some of which will give you prebuilt APIs, ready to go right
away!

###  

CRUD Operations

These are database operations for reading, adding, and updating data in
your database.

Please note that our default **PATCH** endpoint is designed to
automatically filter out any null values or empty text strings that are
typically sent by most frontend platforms. If you don\'t need these, you
can remove the filters **filter\_null** and **filter\_empty\_text** from
the Patch Record function.

###  

Authentication

These are APIs that handle login, signup, and checking an authenticated
user\'s information.

###  

File Storage

These APIs facilitate file upload to Xano.

###  

Custom

Start with a blank canvas. Build anything.

------------------------------------------------------------------------

 

API Groups & API Group Settings

All APIs live inside of API groups. These are just like folders that you
can use to organize all of your different APIs.

Each API group can be customized to your liking using the following
options.

Setting

Function

Name

The name of the API group. Each name in an API group must be unique,
including trailing parameters. This means that if you have an API named
/user/{user\_id}, you can not also have an API named /user/getUser

Description

An internal description of the API group

Tags

Tags are used to label different things you build in Xano, used to
search for related items across the workspace

Swagger

Determines the access level of your auto-generated API documentation
**Public** - Anyone with the link can access **Private (requires
token)** - Anyone with the link appended with an auto-generated token
can access **Disabled** - No API documentation will be made available

[📖] [**Learn more about API
auto-documentation**](apis/swagger-openapi-documentation.html)

Request History

Choose whether to inherit your workspace\'s default request history
settings, or specify new ones for this API group

[📖] [**Learn more about request
history**](../../maintenance-monitoring-and-logging/request-history.html)

External Access

Quickly enable or disable public access to these APIs

Additionally, you can change the **canonical ID** of an API group from
the Security section of the settings menu. The canonical ID dictates
part of the endpoint URLs used to access those APIs, so proceed with
caution before changing this.

To access your API groups, click
[![](../../_gitbook/imageb76c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F9ke9LBO0fuJnaVrgjeRB%252FCleanShot%25202024-12-20%2520at%252022.59.05.png%3Falt%3Dmedia%26token%3D89501c2d-acd8-46a9-89a8-091f83d77280&width=300&dpr=4&quality=100&sign=cd86cd2&sv=2)]in the left-hand navigation menu.

Click on a group to enter it, or click
[![](../../_gitbook/image5975.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FwtC0w6VkgSooxnziywTB%252FCleanShot%25202024-12-20%2520at%252023.00.00.png%3Falt%3Dmedia%26token%3D69b55ed1-8d46-4f9e-9a24-952c475620a9&width=300&dpr=4&quality=100&sign=34be3ff5&sv=2)]to create a new one.

Some of these settings are only available after the API group is
created.

###  

CORS Management for API Groups

CORS, or Cross-Origin Resource Sharing, is like a security guard for web
applications. It ensures that resources on a web page only talk to
servers they are allowed to. Imagine visiting a friend\'s house; if your
friend\'s parents don\'t know you, they might not let you in. Similarly,
CORS ensures that only trusted sources can interact with your web
application, keeping data safe and secure. This is important because it
helps protect users from potentially harmful interactions between
different websites.

In Xano, you can change CORS to one of three options:

-   
    
        
    
    **Default** - Xano uses wildcard values to allow all origins,
    methods, and headers. This satisfies the requirements of servers
    that ask for CORS, and also ensures that all requests are allowed.
    
-   
    
        
    
    **Custom** - You can specify your own CORS rules from here, such as
    only allowing requests from certain servers.

    -   
        
                
        
        **Allow Credentials** - When checked, this allows requests to
        include credentials like cookies, HTTP authentication, or
        client-side SSL certificates. This is necessary if your frontend
        needs to send authentication information to your backend.
        
    -   
        
                
        
        **Allow Methods** - These are the HTTP methods that your API
        will accept from other origins.
        
    -   
        
                
        
        **Allow Origins** - This section lets you specify which domains
        can access your API. The \"Add Origin\" button lets you:

        -   
            
                        
            
            Add specific domains (e.g.,
            [https://yourfrontend.com](https://yourfrontend.com/))
            
        -   
            
                        
            
            Use wildcards (e.g., \*)
            
        -   
            
                        
            
            List multiple allowed origins
                    
    -   
        
                
        
        **Allow Headers** - Defines which HTTP headers can be used in
        requests. The \"Add Header\" button lets you specify custom
        headers beyond the standard ones.
        
    -   
        
                
        
        **Max Age** - Set to 1 hour by default, this determines how long
        browsers should cache the CORS preflight response. This helps
        reduce the number of preflight requests (OPTIONS calls) that
        browsers make.
            

**What is a preflight request?**

Before accessing data from another site, your browser sends a
\"preflight request\" to ask for permission. If approved, it proceeds
with the main request. This step ensures your information stays safe
during web interactions.

------------------------------------------------------------------------

 

Creating a new API

###  

Click
[![](../../_gitbook/image337f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FIVYHDRGmoONJCa1MvIvB%252FCleanShot%25202024-12-20%2520at%252023.07.25.png%3Falt%3Dmedia%26token%3D5db41eba-9917-4385-8b93-afaf0673159a&width=300&dpr=4&quality=100&sign=f62afcb3&sv=2)] to create a new API endpoint.

Choose from one of the four different API types available.

CRUD Database Operations

Authentication

Upload Content

Custom

CRUD stands for **create, read, update,** and **delete**. These are
basic database operations that most applications will need to perform on
one or more tables.

Xano can create these for you automatically, based on your database
tables.

1.  
    
        
    
    Choose the table you want to create an action for.
    
2.  
    
        
    
    Select the endpoint type you want to create.
    
3.  
    
        
    
    Adjust any settings you wish for the new endpoint being created, and
    click
    [![](../../_gitbook/imaged193.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FbnVusKe06qZXzC77CFrO%252FCleanShot%25202024-12-20%2520at%252023.15.35.png%3Falt%3Dmedia%26token%3De504345f-ca9b-49d6-a879-4b28f209fbfa&width=300&dpr=4&quality=100&sign=ce5efed9&sv=2)]
    

Authentication endpoints are used for basic auth operations such as


Xano has pre-built authentication endpoints ready to go that can be
added here.

1.  
    
        
    
    Choose the authentication endpoint you would like to add.
    
2.  
    
        
    
    Choose your user table.
    

If you don\'t see the database table you want to authenticate against,
then you need to first enable authentication for that specific database
table within its settings panel.

1.  
    
        
    
    Adjust any settings you wish for the new endpoint being created, and
    click
    [![](../../_gitbook/imaged193.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FbnVusKe06qZXzC77CFrO%252FCleanShot%25202024-12-20%2520at%252023.15.35.png%3Falt%3Dmedia%26token%3De504345f-ca9b-49d6-a879-4b28f209fbfa&width=300&dpr=4&quality=100&sign=ce5efed9&sv=2)]
    

These endpoints are pre-built content upload functions that you can use
to upload and store images, videos, and other attachments in Xano.

1.  
    
        
    
    Choose the endpoint type you\'d like to create.
    
2.  
    
        
    
    Adjust any settings you wish for the new endpoint being created, and
    click
    [![](../../_gitbook/imaged193.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FbnVusKe06qZXzC77CFrO%252FCleanShot%25202024-12-20%2520at%252023.15.35.png%3Falt%3Dmedia%26token%3De504345f-ca9b-49d6-a879-4b28f209fbfa&width=300&dpr=4&quality=100&sign=ce5efed9&sv=2)]
    

Start with a blank canvas to build upon.

1.  
    
        
    
    Adjust any settings you wish for the new endpoint being created, and
    click
    [![](../../_gitbook/imaged193.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FbnVusKe06qZXzC77CFrO%252FCleanShot%25202024-12-20%2520at%252023.15.35.png%3Falt%3Dmedia%26token%3De504345f-ca9b-49d6-a879-4b28f209fbfa&width=300&dpr=4&quality=100&sign=ce5efed9&sv=2)]
    
------------------------------------------------------------------------

 

API Settings

###  

From the Settings panel

![](../../_gitbook/image522d.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FmjI2kCsucENivoHsthRW%252FCleanShot%25202024-12-23%2520at%252009.56.20.png%3Falt%3Dmedia%26token%3Dc98faeba-9ced-4be2-8397-da89dcd32fc3&width=768&dpr=4&quality=100&sign=88874836&sv=2)

Name

Purpose

Name

The name of the API endpoint. This also directly impacts the API URL.

Description

An internal description, just for you.

Verb

The API method

Tags

Use tags to organize objects throughout your Xano workspace and find
them later

Request History

-   
    
        
    
    Inherit Settings

    -   
        
                
        
        Use whatever is set in your workspace branch defaults
            
-   
    
        
    
    Other

    -   
        
                
        
        Set specific request history settings for this endpoint
            
[📖] [**Learn more about request
history**](../../maintenance-monitoring-and-logging/request-history.html)

External access

When disabled, this endpoint will not respond to requests.

Authentication

Choose whether this endpoint requires a valid authentication token
present in the headers to execute

Response type

-   
    
        
    
    Standard

    -   
        
                
        
        Waits for execution to finish and delivers the response all at
        once
            
-   
    
        
    
    Streaming

    -   
        
                
        
        Used with the Streaming API Response function, stream the
        response in chunks to a service that supports it
            
[📖] [**Learn more about streaming
APIs**](../../xano-ai/streaming-apis.html#streaming-api-response)

Response caching

Cache the response and redeliver it for future calls [📖]
[**Learn more about response
caching**](../additional-features/response-caching.html)

Last updated 4 months ago

Was this helpful?