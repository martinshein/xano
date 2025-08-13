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
    
    [What is an external API request?](#what-is-an-external-api-request)

-   [Using the External API Request Function](#using-the-external-api-request-function)

-   [Add an External API Request function](#add-an-external-api-request-function)

-   [Use the AI Assistant to help you build your API request](#use-the-ai-assistant-to-help-you-build-your-api-request)

-   [Or, build the request manually or with a cURL command](#or-build-the-request-manually-or-with-a-curl-command)

-   [Understanding API Documentation](#understanding-api-documentation)

-   [Start by evaluating the four key sections that almost every API documentation has.](#start-by-evaluating-the-four-key-sections-that-almost-every-api-documentation-has)

-   [Finding the endpoint(s) you need](#finding-the-endpoint-s-you-need)

-   [Multipart (File) Support](#multipart-file-support)

-   [Security Settings](#security-settings)

-   [Host Verification](#host-verification)

-   [Peer Verification](#peer-verification)

-   [SSL Authentication](#ssl-authentication)

-   [CA Certificate](#ca-certificate)

Was this helpful?

Copy


2.  Functions
3.  [APIs & Lambdas](../apis-and-lambdas.html)

External API Request 
====================

 

What is an external API request?

The External API Request function is used to send requests to external APIs. You\'ll use this anytime you want to interact with a third party service, such as a payment platform or email provider.

 

Using the External API Request Function

<div>

1

###  

Add an External API Request function

2

###  

Use the AI Assistant to help you build your API request

<div>

1

###  

Add an External API Request function to your function stack.

This is located inside of the **APIs & Lambdas** category.

2

###  

Click [![](../../../_gitbook/imaged5bc.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F1G2mEZvVXlOR6d9kiD6I%252FCleanShot%25202025-04-02%2520at%252015.44.45.png%3Falt%3Dmedia%26token%3D53cbbf6d-62b9-4a06-893c-c5e14b6fb3d1&width=300&dpr=4&quality=100&sign=ed805135&sv=2)] from the panel that opens.

3

###  

Tell the AI Assistant about the API you want to access, and any specifics about the request you want to make.

![](../../../_gitbook/imagec482.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FjT1vrsN9at0cDSPSsqoy%252FCleanShot%25202025-04-02%2520at%252015.57.03.png%3Falt%3Dmedia%26token%3D2312e5ad-08f1-44c2-8972-3fe01ceb90b6&width=768&dpr=4&quality=100&sign=e397100&sv=2)

4

###  

You can either choose to apply the AI\'s suggestion, or continue to converse with the AI to iterate or make changes.

![](../../../_gitbook/imagea5c5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F0dc9zZTKSIf6xRICbJdP%252FCleanShot%25202025-04-02%2520at%252015.58.52.png%3Falt%3Dmedia%26token%3D48c8ed4d-2f55-42f7-b64f-b91cc46563b1&width=768&dpr=4&quality=100&sign=785b98c&sv=2)

5

###  

For things like API keys, you can either pass them to the AI or fill them in manually after you\'ve applied the suggestion.[![](../../../_gitbook/imagef6a6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F2QElXqiTiOIkcD0CVPE6%252FCleanShot%25202025-04-02%2520at%252016.00.32.gif%3Falt%3Dmedia%26token%3D9e4c1fb4-7c59-4031-850d-53711c86567a&width=300&dpr=4&quality=100&sign=1a95adff&sv=2)]

</div>

3

###  

Or, build the request manually or with a cURL command

You can copy cURL commands from API documentation, and paste them using [![](../../../_gitbook/image6cec.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F9KzZvPT2roU7bgb6F316%252FCleanShot%25202025-01-13%2520at%252013.20.09.png%3Falt%3Dmedia%26token%3D74555411-4309-48d3-b3d7-8a63f53b0449&width=300&dpr=4&quality=100&sign=d512dfb&sv=2)]. Xano will build the request for you.

Option

Description

url

The URL of the API you\'re calling, such as:
`https://api.service.com/send_message`

method

The verb the API is designed to respond to, such as GET, POST, DELETE, etc\...

params

Also known as \"query parameters\", these are options sent along with the request, such as searching and filtering options, or other data that the request needs to execute.
You may also see this referred to as **request body**.
Hover over the params value space and click [**set**] to add a new parameter.
[![](../../../_gitbook/imaged5da.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FLzdUGqz2VqknybEqzsYy%252FCleanShot%25202025-02-05%2520at%252016.35.54.png%3Falt%3Dmedia%26token%3D89f1e710-c421-4a09-921c-1cebc2027909&width=300&dpr=4&quality=100&sign=3b4b36da&sv=2)]

headers

Any headers you need to send with the request, such as authentication.
Add headers by hovering over the value space and click [**push**
]
[![](../../../_gitbook/imageb6c9.jpg?url=https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FpAWCEAw4h7e2OfMOAFJk%252FCleanShot%25202025-02-05%2520at%252016.37.28.png%3Falt%3Dmedia%26token%3Dba4e92fc-4b3c-4358-9e13-ccbe3e15711c&width=300&dpr=4&quality=100&sign=1816ee35&sv=2)][
]

timeout

How long Xano should allow the request to take before considering it timed out (failed)

follow\_location

Determines if you wish to automatically follow the redirects (if there are any) in the API call.

An example of this would be an API that generates a file for you, then gives you a redirect to get that file.

</div>

 

Understanding API Documentation

<div>

1

###  

Start by evaluating the four key sections that almost every API documentation has.

The Getting Started guide is your entry point - it typically covers the basics of authentication, shows a simple example request, and helps you make your first API call successfully.

The Authentication section explains how to get your API keys and how to include them in your requests. This is crucial since you\'ll need this working before you can try anything else.

The API Reference details every possible endpoint and operation. Don\'t try to read this cover-to-cover. Instead, find the specific endpoint that matches what you\'re trying to do, then study its parameters, required headers, and example responses.

The Examples/Tutorials section often has complete code snippets showing common use cases. These are invaluable for seeing how different API calls work together to accomplish a task.

2

###  

Finding the endpoint(s) you need

When you find the endpoint you need, focus on three things:

1.  
    
        
    
    What URL you\'ll be calling
    
2.  
    
        
    
    What parameters or data you need to send
    
3.  
    
        
    
    What the response will look like
    
Most API documentation also includes **cURL commands**, which you can copy and paste right into Xano by clicking [![](../../../_gitbook/image6cec.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F9KzZvPT2roU7bgb6F316%252FCleanShot%25202025-01-13%2520at%252013.20.09.png%3Falt%3Dmedia%26token%3D74555411-4309-48d3-b3d7-8a63f53b0449&width=300&dpr=4&quality=100&sign=d512dfb&sv=2)]on the External API Request function panel. This is the optimal way to create external API request in Xano, as it ensures consistency with what the API requires and is much faster.

**Tip**

Most API documentation has a \"try it out\" or interactive portion that allows you to experiment with the API --- it\'s the fastest way to understand how everything works.

</div>

 

Multipart (File) Support

Xano has support for sending images through the external API request function. You can send a file resource - either as an input or variable - through the parameters section of the external API request as a key-value pair or as the entire parameter (depending on what the specific API requires).

 

Security Settings

###  

Host Verification

When an API request is sent to a secure server (you\'ll know if it\'s a secure request if the URL starts with https --- most requests will), the domain\'s secure connection is verified using a certificate. Enabling host verification checks the certificate to make sure that it matches the domain you\'re sending the request to.

This value can be `true` or `false`

**Recommended Setting:** `true`

You might want to set Host Verification to \'false\' in a few specific scenarios:

1.  
    
        
    
    **Development and Testing Environments**: When working with development servers that use self-signed certificates or have hostnames that don\'t match their certificates
    
2.  
    
        
    
    **Internal Services with Misconfigured Certificates**: In corporate environments where internal services may have certificates that don\'t exactly match the hostnames used to access them, especially in legacy systems.
    
3.  
    
        
    
    **Troubleshooting SSL Issues**: To isolate whether hostname verification is causing connection problems when debugging API connectivity issues.
    
###  

Peer Verification

Secure certificates are usually issued by certain trusted authorities, such as [LetsEncrypt](https://letsencrypt.org/). Peer Verification enables checking whether or not the certificate is issued by one of these known trusted authorities, validating its authenticity.

This value can be `true` or `false`

**Recommended Setting:** `true`

You might want to set this to false if the server you\'re sending the request to falls under one of the scenarios outlined above under **Host Verification**.

###  

SSL Authentication

This is a set of additional options you can use to validate the security of the request being made. The provider of the service you\'re calling should be able to provide these for you, if necessary.

-   
    
        
    
    `certificate`: The content of the client certificate file. Usually, you\'d be provided with a .crt or a .pem file --- just open it up in your text editor of choice and paste the contents here.
    
-   
    
        
    
    `certificate_pass`: Password for the certificate if it\'s password-protected
    
-   
    
        
    
    `private_key`: The contents of the private key file. Usually, you\'d be provided with a .pem file for this --- just open it up in your text editor of choice and paste the contents here.
    
-   
    
        
    
    `private_key_pass`: Password for the private key if it\'s password-protected
    
###  

CA Certificate

Custom CA certificates allow you to specify your own trusted Certificate Authority for peer verification. This is an advanced option that is useful when connecting to servers that use certificates signed by private or internal CAs --- as in, a CA that is not listed as a known trusted authority.

A custom certificate is usually provided as a file that you\'d just open up in a text editor and paste here. It will look something like this:

Copy

``` 
-----BEGIN CERTIFICATE-----
MIIDITCCAgmgAwIBAgIUJqrGM2rS34H8YryJJLAMarvab8AwDQYJKoZIhvcNAQEL
BQAwIDEeMBwGA1UEAwwVbXlDdXN0b21DZXJ0aWZpY2F0ZUNKX...
-----END CERTIFICATE-----
```

Last updated 4 months ago

Was this helpful?