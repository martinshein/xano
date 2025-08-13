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
- integration
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
            
            -   [Swagger (OpenAPI Documentation)](../building-with-visual-development/apis/swagger-openapi-documentation.html)
                    -   Custom Functions
            
            -   [Async Functions](../building-with-visual-development/custom-functions/async-functions.html)
                    -   [Background Tasks](../building-with-visual-development/background-tasks.html)
        -   [Triggers](../building-with-visual-development/triggers.html)
        -   [Middleware](../building-with-visual-development/middleware.html)
        -   [Configuring Expressions](../building-with-visual-development/configuring-expressions.html)
        -   [Working with Data](../building-with-visual-development/working-with-data.html)
            -   Functions
        
        -   [AI Tools](ai-tools.html)
        -   Database Requests
            
            -   Query All Records
                
                -   [External Filtering Examples](database-requests/query-all-records/external-filtering-examples.html)
                            -   [Get Record](database-requests/get-record.html)
            -   [Add Record](database-requests/add-record.html)
            -   [Edit Record](database-requests/edit-record.html)
            -   [Add or Edit Record](database-requests/add-or-edit-record.html)
            -   [Patch Record](database-requests/patch-record.html)
            -   [Delete Record](database-requests/delete-record.html)
            -   [Bulk Operations](database-requests/bulk-operations.html)
            -   [Database Transaction](database-requests/database-transaction.html)
            -   [External Database Query](database-requests/external-database-query.html)
            -   [Direct Database Query](database-requests/direct-database-query.html)
            -   [Get Database Schema](database-requests/get-database-schema.html)
                    -   Data Manipulation
            
            -   [Create Variable](data-manipulation/create-variable.html)
            -   [Update Variable](data-manipulation/update-variable.html)
            -   [Conditional](data-manipulation/conditional.html)
            -   [Switch](data-manipulation/switch.html)
            -   [Loops](data-manipulation/loops.html)
            -   [Math](data-manipulation/math.html)
            -   [Arrays](data-manipulation/arrays.html)
            -   [Objects](data-manipulation/objects.html)
            -   [Text](data-manipulation/text.html)
                    -   [Security](security.html)
        -   APIs & Lambdas
            
            -   [Realtime Functions](apis-and-lambdas/realtime-functions.html)
            -   [External API Request](apis-and-lambdas/external-api-request.html)
            -   [Lambda Functions](apis-and-lambdas/lambda-functions.html)
                    -   [Data Caching (Redis)](data-caching-redis.html)
        -   [Custom Functions](custom-functions.html)
        -   [Utility Functions](utility-functions.html)
        -   [File Storage](file-storage.html)
        -   [Cloud Services](cloud-services.html)
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
        
        -   [Response Caching](../additional-features/response-caching.html)
        
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
        
        -   [Separating User Data](../../building-backend-features/user-authentication-and-user-data/separating-user-data.html)
        -   [Restricting Access (RBAC)](../../building-backend-features/user-authentication-and-user-data/restricting-access-rbac.html)
        -   [OAuth (SSO)](../../building-backend-features/user-authentication-and-user-data/oauth-sso.html)
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

-   
    
    [Elasticsearch](#elasticsearch)

-   [Connect to Elasticsearch](#connect-to-elasticsearch)

-   [Elasticsearch Query Wizard Function](#elasticsearch-query-wizard-function)

-   [Configure](#configure)

-   [Query](#query)

-   [Elasticsearch: Document (CRUD) Function](#elasticsearch-document-crud-function)

-   [Configure](#configure-1)

-   [Get Document](#get-document)

-   [Create or Update Document](#create-or-update-document)

-   [Elasticsearch Request](#elasticsearch-request)

-   [OpenSearch](#opensearch)

-   [Connect to OpenSearch](#connect-to-opensearch)

-   [AWS OpenSearch Query Wizard Function](#aws-opensearch-query-wizard-function)

-   [Configure](#configure-2)

-   [Query](#query-1)

-   [AWS OpenSearch: Document (CRUD) Function](#aws-opensearch-document-crud-function)

-   [Configure](#configure-3)

-   [Get Document](#get-document-1)

-   [Create or Update Document](#create-or-update-document-1)

-   [AWS OpenSearch Request](#aws-opensearch-request)

-   [Google Cloud Storage](#google-cloud-storage)

-   [List Directory](#list-directory)

-   [Signed URL](#signed-url)

-   [Upload a File](#upload-a-file)

-   [Delete File](#delete-file)

-   [Create Variable From File Resource](#create-variable-from-file-resource)

-   [Amazon S3](#amazon-s3)

-   [Access Key and Secret Access Key](#access-key-and-secret-access-key)

-   [Bucket and Region](#bucket-and-region)

-   [Amazon S3: List Directory](#amazon-s3-list-directory)

-   [Amazon S3: Signed URL](#amazon-s3-signed-url)

-   [Amazon S3: Upload a File](#amazon-s3-upload-a-file)

-   [Amazon S3: Delete File](#amazon-s3-delete-file)

-   [Amazon S3: Create Var From File Resource](#amazon-s3-create-var-from-file-resource)

-   [Microsoft Azure Blob Storage](#microsoft-azure-blob-storage)

-   [Setup](#setup)

-   [List Directory](#list-directory-1)

-   [Signed URL](#signed-url-1)

-   [Upload a File](#upload-a-file-1)

-   [Delete a File](#delete-a-file)

-   [Create Variable From File Resource](#create-variable-from-file-resource-1)

-   [Get File Metadata](#get-file-metadata)

Was this helpful?

Copy


2.  Functions

Cloud Services 
==============

 

Elasticsearch

Elasticsearch is a robust search engine designed for quick and efficient data retrieval in applications. It handles diverse data types, employs a distributed architecture, and offers a powerful query language for real-time search needs. Integration into your applications enhances search experiences, enabling developers to implement efficient full-text searches and complex queries. Elasticsearch\'s indexing capabilities make it valuable for applications such as monitoring systems, log analysis tools, and other scenarios requiring fast and relevant data access.

**Below is a video for our OpenSearch functionality, which can be used as a reference when working with our Elasticsearch functions; they are largely the same.**

<div>

</div>

Xano offers a few functions to make Elasticsearch requests simple.

-   
    
        
    
    [Elasticsearch: Query Wizard](cloud-services.html#elasticsearch-query-wizard-function)
    
-   
    
        
    
    [Elasticsearch: Document](cloud-services.html#elasticsearch-document-crud-function)
    
-   
    
        
    
    [Elasticsearch: Request](cloud-services.html#elasticsearch-request)
    
 

Connect to Elasticsearch

Requires an Elasticsearch domain.

1.  
    
        
    
    `auth_type`
    Choose between `Basic` , `Bearer` or `API Key` to set the type of authentication process to use.
    
2.  
    
        
    
    `key_id`
    If using `Basic`, enter the username you wish to authenticate with.
    If using `Bearer`, leave this blank.
    If using `API Key`, enter the API key identifier you wish to authenticate with.
    
3.  
    
        
    
    `access_key`
    If using `Basic`, enter the API key secret you with to authenticate with.
    If using `Bearer` , no access key is required.
    If using `API Key` , enter the value that corresponds with the key identifier you wish to authenticate with.
    
4.  
    
        
    
    `base_url`
    Set to the domain endpoint where Elasticsearch is hosted.
    
5.  
    
        
    
    `index`
    Enter the name of the Elasticsearch index to send request.
    Only applicable on Document and Query functions.
    

![](../../_gitbook/imagefc73.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fbb3FyEQxdZQy3lQzyRUm%252FCleanShot%25202024-03-08%2520at%252010.50.20.png%3Falt%3Dmedia%26token%3Dd6b447a4-ef99-453a-831d-c368a3ab86f8&width=768&dpr=4&quality=100&sign=9e2fee17&sv=2)

 

Elasticsearch Query Wizard Function

Use the query wizard to easily search documents stored in Elasticsearch.

###  

Configure

See [Connect to Elasticsearch](cloud-services.html#connect-to-elasticsearch) for details on configuration.

Then, select a `return_type` from the options below.

-   
    
        
    
    `search` - Returns records that match query
    
-   
    
        
    
    `count` - Returns number of total records matching query
    
###  

Query

**Query Wizard**

Set filter criteria using the Xano query builder. The left input is the field to filter on. Then set the operator and value to evaluate. Optionally, add multiple conditions using AND / OR logic.

Select 'Update Payload' to ensure your changes are reflected in the query payload.

![](../../_gitbook/image435e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FI06JFQu09YJhmvnmTrM8%252FCleanShot%25202024-03-08%2520at%252010.54.53.png%3Falt%3Dmedia%26token%3D5f042a62-ebbe-4de5-90a8-7c55db05a4d7&width=768&dpr=4&quality=100&sign=43e4264&sv=2)

**Output Options**

These options can only be set on 'search' return type (not 'count').

Size: the number of results to return (useful for pagination)

From: the number to offset the results (useful for pagination)

Included Fields: field names to include in the results. Can be formatted as JSON array or comma separated string.

Sort: order to return results. Default is by Elasticsearch relevance score. Option to choose one or more fields to sort in ascending or descending order.

![](../../_gitbook/imagefffa.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FqBIdN3Z8nybjoyqsN7tS%252FCleanShot%25202024-03-08%2520at%252010.55.12.png%3Falt%3Dmedia%26token%3D7dfaecf1-a5a5-4087-8f08-bd5bcdedb6b4&width=768&dpr=4&quality=100&sign=3815c214&sv=2)

**Payload (auto-generated)**

The JSON sent as the payload to Elasticsearch. This is generated by the Query Wizard and Output Options sections. Useful for debugging.

Dynamic values (variables, inputs, etc.) are escaped using parentheses and use Xano expression syntax. These will be evaluated at the time of the request.

Changes made directly to the payload may be overwritten by other areas of the query wizard. If you already have a query payload you want to use, it is recommended to use the Elasticsearch Request function instead.

![](../../_gitbook/image8625.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FarDTqDiTxv6OzarFpP4P%252Fimage.png%3Falt%3Dmedia%26token%3D85c96cc4-5727-46f5-ace0-72c2b31ed1f5&width=768&dpr=4&quality=100&sign=fe052b46&sv=2)

 

Elasticsearch: Document (CRUD) Function

Easily get, add, update, or remove documents from an Elasticsearch index.

###  

Configure

See [Connect to Elasticsearch](cloud-services.html#connect-to-elasticsearch) for details on configuration.

###  

Get Document

1.  
    
        
    
    Set method of API request to GET
    
2.  
    
        
    
    Specify doc\_id
    

![](../../_gitbook/imagecd76.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FtW1wW74nM4cxmSP0CGqr%252FCleanShot%25202024-03-08%2520at%252010.57.49.png%3Falt%3Dmedia%26token%3D4c6e488c-57aa-4384-90cd-1ba6cf1b2cf6&width=768&dpr=4&quality=100&sign=30077ea0&sv=2)

###  

Create or Update Document

1.  
    
        
    
    Set `method` to `POST` (create) or `PUT` (update)
    
2.  
    
        
    
    Set `doc_id` (optional for POST)
    

![](../../_gitbook/imagecf6f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F2R8bCLcSr1cA7AB9oTJr%252FCleanShot%25202024-03-08%2520at%252011.04.12.png%3Falt%3Dmedia%26token%3D9d242129-f126-435e-9c2e-7a55b561ca73&width=768&dpr=4&quality=100&sign=f755a68a&sv=2)

###  

Elasticsearch Request

Send any Elasticsearch API request using similar configuration methods as outlined in [Connect to Elasticsearch](cloud-services.html#connect-to-elasticsearch).

Set the `url` to use the desired endpoint of the request.

Set `query` to the JSON payload if necessary.

 

OpenSearch

OpenSearch is an open-source search and analytics tool suite, derived from ElasticSearch, offered as a scalable and flexible solution by Amazon Web Services.

With OpenSearch, you can apply natural language processing, text analyzers, and built in machine learning to quickly return the most relevant data. This makes it a great tool for log analytics, application monitoring, and website searches.

<div>

</div>

Xano offers a few functions to make OpenSearch requests simple.

-   
    
        
    
    [AWS OpenSearch: Query Wizard](cloud-services.html#aws-opensearch-query-wizard-function)
    
-   
    
        
    
    [AWS OpenSearch: Document](cloud-services.html#aws-opensearch-document-crud-function)
    
-   
    
        
    
    [AWS OpenSearch: Request](cloud-services.html#aws-opensearch-request)
    
 

Connect to OpenSearch

Requires an OpenSearch Service domain hosted by AWS.
Find AWS Documentation on [Creating and managing Amazon OpenSearch Service domains](../../../docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).

1.  
    
        
    
    `auth_type`
    Choose between `IAM` (AWS Identity and Access Management) and `master` (basic auth from internal user database) to set the type of authentication process to use.
    
2.  
    
        
    
    `key_id`
    If using `IAM`, enter the IAM key id you wish to authenticate with.
    If using `master` , enter the username you wish to authenticate with.
    
3.  
    
        
    
    `access_key`
    If using `IAM`, enter the access key you wish to authenticate with.
    If using `master` , enter the password you wish to authenticate with.
    
4.  
    
        
    
    `region`
    Only required for `IAM`. Set to the configured OpenSearch region (example: `us-east-2`).
    
5.  
    
        
    
    `base_url`
    Set to the domain endpoint (IPv4) specified on AWS.
    
6.  
    
        
    
    `index`
    Enter the name of the OpenSearch index to send request.
    Only applicable on Document and Query functions.
    

![](../../_gitbook/imageac8c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FxYttNtS1FGo06uUT6aJV%252Fimage.png%3Falt%3Dmedia%26token%3Dd0b1a2e3-5058-4ac4-acf7-77ef9d1dbc05&width=768&dpr=4&quality=100&sign=450df59c&sv=2)

Configure OpenSearch connection using IAM or internal user database credentials.

 

AWS OpenSearch Query Wizard Function

Use the query wizard to easily search documents stored in OpenSearch.

###  

Configure

See [Connect to OpenSearch](cloud-services.html#connect-to-opensearch) for details on configuration.

Then, select a `return_type` from the options below.

-   
    
        
    
    `search -` Returns records that match query
    
-   
    
        
    
    `count` - Returns number of total records matching query
    
###  

Query

**Query Wizard**

Set filter criteria using the Xano query builder. The left input is the field to filter on. Then set the operator and value to evaluate. Optionally, add multiple conditions using AND / OR logic.

Select 'Update Payload' to ensure your changes are reflected in the query payload.

![](../../_gitbook/image6173.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F6wm0PDjtU4BEEeoXqrVH%252Fimage.png%3Falt%3Dmedia%26token%3Dc347ffb0-9bff-46db-8bf5-24fb2db6f1dc&width=768&dpr=4&quality=100&sign=a97e09bd&sv=2)

**Output Options**

These options can only be set on 'search' return type (not 'count').

Size: the number of results to return (useful for pagination)

From: the number to offset the results (useful for pagination)

Included Fields: field names to include in the results. Can be formatted as JSON array or comma separated string.

Sort: order to return results. Default is by OpenSearch relevance score. Option to choose one or more fields to sort in ascending or descending order.

![](../../_gitbook/image0c55.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F0CQaelCeudZclgIamKiZ%252Fimage.png%3Falt%3Dmedia%26token%3Ddf4a47d2-dfd4-433a-8e98-fa631cb5cbb9&width=768&dpr=4&quality=100&sign=b455eeca&sv=2)

**Payload (auto-generated)**

The JSON sent as the payload to OpenSearch. This is generated by the Query Wizard and Output Options sections. Useful for debugging.

Dynamic values (variables, inputs, etc.) are escaped using parentheses and use Xano expression syntax. These will be evaluated at the time of the request.

Changes made directly to the payload may be overwritten by other areas of the query wizard. If you already have a query payload you want to use, it is recommended to use the OpenSearch Request function instead.

![](../../_gitbook/image8625.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FarDTqDiTxv6OzarFpP4P%252Fimage.png%3Falt%3Dmedia%26token%3D85c96cc4-5727-46f5-ace0-72c2b31ed1f5&width=768&dpr=4&quality=100&sign=fe052b46&sv=2)

 

AWS OpenSearch: Document (CRUD) Function

Easily get, add, update, or remove documents from an OpenSearch index.

###  

Configure

See [Connect to OpenSearch](cloud-services.html#connect-to-opensearch) for details on configuration.

###  

Get Document

1.  
    
        
    
    Set method of API request to GET
    
2.  
    
        
    
    Specify doc\_id
    

![](../../_gitbook/imagebc68.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FwWI04rzfOwZv2xJ6oxLb%252Fimage.png%3Falt%3Dmedia%26token%3Dbaf8a703-2586-453b-a398-2f1fd48f2e30&width=768&dpr=4&quality=100&sign=150c2601&sv=2)

###  

Create or Update Document

1.  
    
        
    
    Set `method` to `POST` (create) or `PUT` (update)
    
2.  
    
        
    
    Set `doc_id` (optional for POST)
    
3.  
    
        
    
    Set document payload. Click 'Use Index Schema' if you want to import the schema (mapping) directly from the OpenSearch index set under Configure tab. This will use the credentials provided to make a request to OpenSearch on your behalf to get the mapping.
    

![](../../_gitbook/image7df5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FevXvozwVgGYi751xl9Yf%252Fimage.png%3Falt%3Dmedia%26token%3Df76350e9-7bf2-4420-83ef-7b6d13dda3c2&width=768&dpr=4&quality=100&sign=1e1b4738&sv=2)

![](../../_gitbook/imagebab6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FoXEiZGLm4zVzhjKleX36%252Fimage.png%3Falt%3Dmedia%26token%3D7afe03e9-6812-47d8-8bb0-419fd1f867af&width=768&dpr=4&quality=100&sign=b78c9953&sv=2)

###  

AWS OpenSearch Request

Send any OpenSearch API request using similar configuration methods as outlined in [Connect to OpenSearch](cloud-services.html#connect-to-opensearch).

Set the `url` to use the desired endpoint of the request.

Set `query` to the JSON payload if necessary.

 

Google Cloud Storage

Manage Google Cloud Storage buckets directly in the Xano function stack.

<div>

</div>

####  

Google Service Account

You need to set up a Google Service Account in the [Google Cloud Console](https://console.cloud.google.com/).

Navigate to IAM & Admin and select Service Accounts.

![](../../_gitbook/image3af1.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FsZqaiOysC8MdrJC1Vhh1%252FCleanShot%25202023-07-31%2520at%252016.13.27%25402x.png%3Falt%3Dmedia%26token%3Da4bcbe13-3f26-4b60-969a-48621d9f7d4f&width=768&dpr=4&quality=100&sign=b4c0d9bf&sv=2)

Select **+ Create Service Account.**

####  

Roles

**Be sure to include the following Roles for the Service Account**:

-   
    
        
    
    `Service Account User`
    
-   
    
        
    
    `Storage Admin`
    
-   
    
        
    
    `Storage Object Admin`
    
Once the Service Account is created, select actions and **Manage keys.**

Then add a new key and select the JSON option.

![](../../_gitbook/image47d2.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FJYftUGeKyqRyFAEAGwaV%252FCleanShot%25202023-07-31%2520at%252016.17.44%25402x.png%3Falt%3Dmedia%26token%3D14a7895f-9360-4687-8dd7-cadb177141e4&width=768&dpr=4&quality=100&sign=b96f2d39&sv=2)

Google will provide a JSON file for download. Open the file and copy the JSON key. Paste this into your Xano workspace either as an Environment Variable or as a variable in the function stack that you are using the Google Cloud Storage functions.

The JSON key must be entered as a **text string**. Do not import the key as JSON when adding it to Xano.

###  

List Directory

List the contents of a Google Cloud Storage Bucket.

![](../../_gitbook/image633a.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FVTFsE7B7MLf2yWiLO9P2%252FCleanShot%25202023-08-01%2520at%252016.34.07.png%3Falt%3Dmedia%26token%3D9057859e-5982-4e7d-b299-d95ba1934aec&width=768&dpr=4&quality=100&sign=a47b89fc&sv=2)

**Service Account** - the JSON key, stored as text, from your Google Service Account

**Bucket** - the name of the Bucket you wish to access.

**Path** - the path you wish to see the contents of.

###  

Signed URL

Generate a signed URL to provide limited permissions. These can be used with a TTL (time to live) similar to an expiring token.

![](../../_gitbook/imagedff3.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fwp0s8tFVbqFpDLlYWG8z%252FCleanShot%25202023-08-01%2520at%252016.35.18.png%3Falt%3Dmedia%26token%3D320ec977-159b-4dd7-aaf6-d60b4eab77e3&width=768&dpr=4&quality=100&sign=15051554&sv=2)

**Service Account** - the JSON key, stored as text, from your Google Service Account

**Bucket** - the name of the Bucket you wish to access.

**filePath** - the path of the file you wish to generate the URL for.

**Method** - the HTTP method (GET or POST)

**TTL** - time to live, in seconds. (How long until the URL expires).

###  

Upload a File

Upload a File to the specific Google Cloud Storage bucket.

![](../../_gitbook/image172b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F1NfjfFrvP75ayyL9GpOl%252FCleanShot%25202023-08-01%2520at%252016.31.21.png%3Falt%3Dmedia%26token%3D252319b6-f2dd-4c45-bdae-bfd9c305bdd3&width=768&dpr=4&quality=100&sign=b4c78c6&sv=2)

**Service Account** - the JSON key, stored as text, from your Google Service Account

**Bucket** - the name of the Bucket you upload a file to.

**filePath** - the path and name of the file you wish to store in the bucket. For example \"files/image1\" will upload the image in the files folder and name it image1.

**File** - the file being uploaded. This should come from a file resource input or a file resource variable.

###  

Delete File

Delete a specific file from a Bucket.

![](../../_gitbook/imagec799.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FmAacFp2Er11DspuO7cJL%252FCleanShot%25202023-08-01%2520at%252016.36.25.png%3Falt%3Dmedia%26token%3D11c874ca-4c9f-4bd2-9bc7-15c5542b42fc&width=768&dpr=4&quality=100&sign=830448da&sv=2)

**Service Account** - the JSON key, stored as text, from your Google Service Account

**Bucket** - the name of the Bucket that contains the file.

**filePath** - the path of the file you wish to delete from the Bucket.

###  

Create Variable From File Resource

Return the file resource as a variable in Xano, including the raw image. This can be used, for example, to send to another service if file transfer is needed.

![](../../_gitbook/imagee906.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FYgOSIoMyXanpu2shHHi7%252FCleanShot%25202023-08-01%2520at%252016.37.10.png%3Falt%3Dmedia%26token%3D3b5b85b7-f4d7-4058-857e-1c5a8b85d39f&width=768&dpr=4&quality=100&sign=e93b8f0f&sv=2)

**Service Account** - the JSON key, stored as text, from your Google Service Account

**Bucket** - the name of the Bucket that contains the file.

**filePath** - the path of the file you wish to create a variable of.

####  

Example - Using the Variable Created from File Resource

Turn your API endpoint into a redirect to the file by returning the data field from the return variable and setting a custom header of Content-Type with the mime of the file resource.

Here\'s an example return of Create Variable from File Resource:

![](../../_gitbook/image7e5c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FIJLQskXCWL3yLjWEIEvy%252FCleanShot%25202023-07-31%2520at%252017.02.31.png%3Falt%3Dmedia%26token%3D01816cc1-51f7-494d-8b08-ec9eee9113d3&width=768&dpr=4&quality=100&sign=ba569e61&sv=2)

If we return the raw image (data) and use a Set Header function to define `Content-Type` the mime (in this example `image/png`). We can have our endpoint URL redirect to the file.

![](../../_gitbook/image3900.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FARG5ckOSrAJL6vcSe5Kw%252FCleanShot%25202023-07-31%2520at%252017.05.40.gif%3Falt%3Dmedia%26token%3D78098c5b-7e62-4b17-87c3-84811323920d&width=768&dpr=4&quality=100&sign=b2e1cdda&sv=2)

 

Amazon S3

###  

Access Key and Secret Access Key

From your AWS Developer Console, navigate to **Security Credentials**.

![](../../_gitbook/imageedc5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FnKe5CS6JUhPWBHr2DpV0%252FCleanShot%25202023-09-26%2520at%252014.31.18.png%3Falt%3Dmedia%26token%3D3f450274-deb1-4c48-a769-5a98d68caf65&width=768&dpr=4&quality=100&sign=31d1498a&sv=2)

Scroll down to **Access Keys** and select **Create access key** unless you have an access key and secret already generated.

![](../../_gitbook/image48a8.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F8RLaWnzZWuGUg1DmleTr%252FCleanShot%25202023-09-26%2520at%252014.33.23.png%3Falt%3Dmedia%26token%3D47dfa2a5-a05b-440c-b482-b134c068bb6c&width=768&dpr=4&quality=100&sign=e096e461&sv=2)

Select **Command Line Interface (CLI)** as the use case and choose next, optionally add a description, then create the access key.

![](../../_gitbook/image7298.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FGjXnSflri9xHfgZPdQ8Z%252FCleanShot%25202023-09-26%2520at%252014.36.15.png%3Falt%3Dmedia%26token%3D7c974b36-c489-415d-9353-ecac39094a60&width=768&dpr=4&quality=100&sign=292d72a1&sv=2)

Store the **Access key** and **Secret access key** in a safe place. It\'s recommended to save these in your Xano workspace as Environment Variables as they will be used in the Amazon S3 Cloud Storage Functions.

![](../../_gitbook/image9590.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FuoXSIdmnrTjUetFwRVgf%252FCleanShot%25202023-09-26%2520at%252014.37.44.png%3Falt%3Dmedia%26token%3D937bbf2d-fb6d-458d-892d-e0f8a47680ed&width=768&dpr=4&quality=100&sign=be01bdb&sv=2)

###  

Bucket and Region

The s3 bucket name and region will also be required when calling the Amazon s3 Cloud Storage Functions.

When navigating to your s3 buckets, the bucket name can be found under name. The region is under region but only requires the identifier. For example, in the below image the bucket name is **xano-s3-test** and the region is **us-west-2**.

![](../../_gitbook/imagee9c6.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FTh5U2tLbdrA3rObg6bc7%252FCleanShot%25202023-09-26%2520at%252014.44.58.png%3Falt%3Dmedia%26token%3D7856d808-f5a5-4fd6-874b-147218ae8418&width=768&dpr=4&quality=100&sign=ac29ced4&sv=2)

###  

Amazon S3: List Directory

Lists the directory details of the specific Amazon s3 bucket.

![](../../_gitbook/imagefbdb.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FffUtPSRzL2aembAzLPmu%252FCleanShot%25202023-09-26%2520at%252014.49.36.png%3Falt%3Dmedia%26token%3D6e0f2df8-29b0-4e98-9f50-d8a93e92035b&width=768&dpr=4&quality=100&sign=16988624&sv=2)

**Bucket -** The name of the s3 bucket you want to get the details of.

**Region -** The region of the bucket.

**Key -** The access key

**Secret -** The secret access key

**Next\_page\_token -** optional. The next page token is provided in the response if there is a next page, use this value to get the next page of items. S3 buckets limit 1,000 items per page.

###  

Amazon S3: Signed URL

Creates a signed URL of the file to be shared with an expiration.

![](../../_gitbook/image61f4.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FYKuTkedaanjpujG0m663%252FCleanShot%25202023-09-26%2520at%252014.56.34.png%3Falt%3Dmedia%26token%3D51a991bf-9184-48e9-904c-a33222bdaed9&width=768&dpr=4&quality=100&sign=9be97ff6&sv=2)

**Bucket -** The name of the s3 bucket you want to get the details of.

**Region -** The region of the bucket.

**Key -** The access key

**Secret -** The secret access key

**File\_key -** The file key of the file. This can be found in the s3 bucket when selecting the file and finding Key. Additionally, the Key is listed in the payload for List Directory.

**TTL** - Time to live. How long, in seconds, the signed URL is viewable until it expires.

###  

Amazon S3: Upload a File

Upload a file to a specified Amazon S3 Bucket

![](../../_gitbook/imagec301.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fb8CzMumI47VgRA5vrkhF%252FCleanShot%25202023-09-26%2520at%252015.03.11.png%3Falt%3Dmedia%26token%3Df05b22d1-7dd1-4af9-a502-a56286a6f300&width=768&dpr=4&quality=100&sign=cee03711&sv=2)

**Bucket -** The name of the s3 bucket you want to get the details of.

**Region -** The region of the bucket.

**Key -** The access key

**Secret -** The secret access key

**File\_key -** Optionally define the file key. If nothing is defined, one will be automatically assigned by Amazon S3.

**File** - The file being uploaded. This must come from a file resource input or file resource variable.

###  

Amazon S3: Delete File

Delete a file from a specified S3 Bucket.

![](../../_gitbook/imageb68c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FsKReDUO5ggszLiWQqvbP%252FCleanShot%25202023-09-26%2520at%252015.06.04.png%3Falt%3Dmedia%26token%3Db30ef6c3-ad83-4f40-b8ff-29abf0f4d962&width=768&dpr=4&quality=100&sign=50a57a2&sv=2)

**Bucket -** The name of the s3 bucket you want to get the details of.

**Region -** The region of the bucket.

**Key -** The access key

**Secret -** The secret access key

**File\_key -** The file key of the file you wish to delete.

###  

Amazon S3: Create Var From File Resource

Return the file resource as a variable in Xano, including the raw image. This can be used, for example, to send to another service if file transfer is needed.

![](../../_gitbook/image2291.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FvCyMThn7YzyeaEngzM5B%252FCleanShot%25202023-09-26%2520at%252015.09.04.png%3Falt%3Dmedia%26token%3Dd9e21cb9-d476-4032-a81b-362fa4bce078&width=768&dpr=4&quality=100&sign=d6bf57b&sv=2)

**Bucket -** The name of the s3 bucket you want to get the details of.

**Region -** The region of the bucket.

**Key -** The access key

**Secret -** The secret access key

**File\_key -** The file key of the file you wish to return the file resource as a variable.

The result, shown on the right-hand side of the above image returns an object with the file name, size, mime type, and raw image represented in the path data.

Check out the [example](cloud-services.html#example-using-the-variable-created-from-file-resource) above to return the image through an API request.

 

Microsoft Azure Blob Storage

Manage storage containers from your Microsoft Azure account directly from the Xano function stack.

###  

Setup



####  

Create a storage account

A storage account is required to store files on Azure. First, select **Create a resource** from the portal homepage.

![](../../_gitbook/imagee45e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FNPLuE7B094Wk9cy1e2Oz%252FCleanShot%25202024-05-13%2520at%252011.31.53.png%3Falt%3Dmedia%26token%3D0bbad7c6-974e-4ad9-9486-ce73fe4dd2b0&width=768&dpr=4&quality=100&sign=7d99b2ab&sv=2)

Select Create a resource from the portal home page.

Navigate to storage and select **Create** under storage account.

![](../../_gitbook/imageb01b.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FicTLomCyZiaNIywmXcEb%252FCleanShot%25202024-05-13%2520at%252011.36.20.png%3Falt%3Dmedia%26token%3D2cbf5f79-c196-47d2-b169-9b0228739f59&width=768&dpr=4&quality=100&sign=b6dca786&sv=2)

Create a storage account.

Fill out the required information in **Basics**, if you don\'t already have a resource group, create a new one.

![](../../_gitbook/image5edd.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FPuRGFMCKICULSb3hKJ4i%252FCleanShot%25202024-05-13%2520at%252011.39.56.png%3Falt%3Dmedia%26token%3Dd0b1215f-1a47-4131-b879-4b0b52b74653&width=768&dpr=4&quality=100&sign=b6112981&sv=2)

Create a storage account.

Configure any additional settings and create the storage account once you\'re ready.

####  

Create a container

Once the resource is deployed, navigate to containers and create a new container.

![](../../_gitbook/imagee85f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F72em4e0vynn64Qusw2LC%252FCleanShot%25202024-05-13%2520at%252011.49.28.png%3Falt%3Dmedia%26token%3D2c09a951-1405-4fba-876d-bd51e402f5e0&width=768&dpr=4&quality=100&sign=c4c0370f&sv=2)

Create a new container.

####  

Access key

After creating a container, you need to retrieve your account access key to use the Azure functions in Xano.

Find **Access keys** under **Security + Networking** on the left navigation bar. Select **Show** next to **Key** under **key1**. Copy the key and store it as an [Environment Variable](../environment-variables.html) in Xano.

![](../../_gitbook/image7176.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FNngM76G31hF9b37MycS2%252FCleanShot%25202024-05-14%2520at%252010.57.53.png%3Falt%3Dmedia%26token%3D534b567c-970f-426f-ba7f-4f94da2b7b1c&width=768&dpr=4&quality=100&sign=2ea38fd4&sv=2)

Locate your Azure Access Key.

Do not share your access key. It is recommended to store your access key as an [Environment Variable](../environment-variables.html) in Xano for safe keeping.

###  

List Directory

List directory will list the blobs, properties, and metadata in a container or at a specified path within the container.

![](../../_gitbook/image856f.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FJccdhQiQJWWPWMVykhuZ%252FCleanShot%25202024-05-14%2520at%252011.06.48.png%3Falt%3Dmedia%26token%3Ddd1c7c1f-4c8d-4fa9-8832-5783d000ccf5&width=768&dpr=4&quality=100&sign=740f71d&sv=2)

List the Azure Directory.

-   
    
        
    
    account\_name - Azure storage account name.
    
-   
    
        
    
    account\_key - Azure [Access Key](cloud-services.html#access-key).
    
-   
    
        
    
    conatiner\_name - Container name within Azure storage account.
    
-   
    
        
    
    path - (Optional) Use this to specify a specific blob or folder within a container.
    
###  

Signed URL

Creates a signed URL for a file with a specified time to live (TTL) or expiration.

![](../../_gitbook/image0556.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FJeiAaDKJS2IVT1DmBipr%252FCleanShot%25202024-05-14%2520at%252011.13.26.png%3Falt%3Dmedia%26token%3D25bd33bc-e654-4610-b6c3-50aa91c93415&width=768&dpr=4&quality=100&sign=6f09afcb&sv=2)

Create a signed URL for an Azure blob.

-   
    
        
    
    account\_name - Azure storage account name.
    
-   
    
        
    
    account\_key - Azure [Access Key](cloud-services.html#access-key).
    
-   
    
        
    
    conatiner\_name - Container name within Azure storage account.
    
-   
    
        
    
    path - The path of the file to create a signed URL for.
    
-   
    
        
    
    ttl - Time to Live (in seconds); how long the signed URL is accessible.
    
###  

Upload a File

Upload a file to an Azure blob container.

![](../../_gitbook/image8b2c.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FY7Hf5yz0GBkHsz9SliyO%252FCleanShot%25202024-05-14%2520at%252011.28.34.png%3Falt%3Dmedia%26token%3D5d7bc359-9988-46ee-9575-4279ddfea2e1&width=768&dpr=4&quality=100&sign=71b53e77&sv=2)

Upload a file to an Azure blob container.

-   
    
        
    
    account\_name - Azure storage account name.
    
-   
    
        
    
    account\_key - Azure [Access Key](cloud-services.html#access-key).
    
-   
    
        
    
    conatiner\_name - Container name within Azure storage account.
    
-   
    
        
    
    filePath - The path name for the file being uploaded.
    
-   
    
        
    
    file - The file being uploaded. This must come from a file resource.
    
-   
    
        
    
    metadata - (Optional). Optionally include additional metadata with the file stored in object format.
    
###  

Delete a File

Delete a file from an Azure blob container.

![](../../_gitbook/image5c89.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FsVml3I74GRjtdvAB5z8L%252FCleanShot%25202024-05-14%2520at%252011.33.16.png%3Falt%3Dmedia%26token%3D44882344-d7f3-4b76-bf03-613131b61346&width=768&dpr=4&quality=100&sign=b7a5cb57&sv=2)

Delete a file from an Azure blob container.

-   
    
        
    
    account\_name - Azure storage account name.
    
-   
    
        
    
    account\_key - Azure [Access Key](cloud-services.html#access-key).
    
-   
    
        
    
    conatiner\_name - Container name within Azure storage account.
    
-   
    
        
    
    filePath - The path name for the file being deleted.
    
###  

Create Variable From File Resource

Create a variable from a file resource in Azure to use it in the Xano Function Stack.

![](../../_gitbook/image1b3e.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FC76OHzNmqaG8MugtGC17%252FCleanShot%25202024-05-14%2520at%252011.36.17.png%3Falt%3Dmedia%26token%3D07a1f33a-4d4d-4599-a208-3ed843fbd7bc&width=768&dpr=4&quality=100&sign=6946474&sv=2)

Create Variable From File Resource.

-   
    
        
    
    account\_name - Azure storage account name.
    
-   
    
        
    
    account\_key - Azure [Access Key](cloud-services.html#access-key).
    
-   
    
        
    
    conatiner\_name - Container name within Azure storage account.
    
-   
    
        
    
    filePath - The path name for the file being created as a variable.
    

Check out the [example above](cloud-services.html#example-using-the-variable-created-from-file-resource) of leveraging the Variable from File Resource in the Function Stack.

###  

Get File Metadata

Get the metadata of a file from an Azure blob container.

![](../../_gitbook/image7e38.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FMRMCFFjsWC6Pk33DM8W5%252FCleanShot%25202024-05-14%2520at%252011.41.12.png%3Falt%3Dmedia%26token%3D203155ff-ef5d-432e-a2c8-914a9ebb9e1e&width=768&dpr=4&quality=100&sign=d0833f3f&sv=2)

Retrieve the metadata from a Azure storage blob.

-   
    
        
    
    account\_name - Azure storage account name.
    
-   
    
        
    
    account\_key - Azure [Access Key](cloud-services.html#access-key).
    
-   
    
        
    
    conatiner\_name - Container name within Azure storage account.
    
-   
    
        
    
    filePath - The path name for the file to retrieve the metadata from.
    

Last updated 6 months ago

Was this helpful?