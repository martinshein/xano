---
category: database
difficulty: advanced
last_updated: '2025-01-23'
related_docs: []
subcategory: 02-core-concepts/database
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
title: indexing
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
        
        -   [Using the Xano Database](../database-basics/using-the-xano-database.html)
        -   [Field Types](../database-basics/field-types.html)
        -   [Relationships](../database-basics/relationships.html)
        -   [Database Views](../database-basics/database-views.html)
        -   [Export and Sharing](../database-basics/export-and-sharing.html)
        -   [Data Sources](../database-basics/data-sources.html)
            -   Migrating your Data
        
        -   [Airtable to Xano](../migrating-your-data/airtable-to-xano.html)
        -   [Supabase to Xano](../migrating-your-data/supabase-to-xano.html)
        -   [CSV Import & Export](../migrating-your-data/csv-import-and-export.html)
            -   Database Performance and Maintenance
        
        -   [Storage](storage.html)
        -   [Indexing](indexing.html)
        -   [Maintenance](maintenance.html)
        -   [Schema Versioning](schema-versioning.html)
        
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
    
    [What is an Index?](#what-is-an-index)

-   [How do they work?](#how-do-they-work)

-   [When to use an Index?](#when-to-use-an-index)

-   [How do I apply an index properly?](#how-do-i-apply-an-index-properly)

-   [When should I index a single field by itself vs multiple fields in the same index?](#when-should-i-index-a-single-field-by-itself-vs-multiple-fields-in-the-same-index)

-   [Using the GIN Index to search complex data types](#using-the-gin-index-to-search-complex-data-types)

-   [How to Apply an Index in the Database View](#how-to-apply-an-index-in-the-database-view)

-   [Types of Indexes](#types-of-indexes)

-   [When should you not use an index?](#when-should-you-not-use-an-index)

Was this helpful?

Copy

1.  [The Database](../getting-started-shortcuts.html)
2.  Database Performance and Maintenance

Indexing 
========

<div>

</div>

 

**What is an Index?**

An index is a database feature that helps improve the speed and efficiency of queries made against a database table. They help when searching through large, unordered data sets and give the database search engine a quick way to sort and find specific data. Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access to ordered records.

 

**How do they work?**

A table index is very similar in practice to the index of a textbook. When there is a specific piece of information that you want to find, reading every page of that book to find what you are looking for can be very slow and inefficient. So, you would use the index at the back of the book to find exactly which page contains the information you need.

This is the same concept for a database table index. They create a special type of lookup table in the background that the database engine can use to retrieve the data faster than looking through each individual row for every search.

 

**When to use an Index?**

Indexes are the most beneficial in the following scenario(s):

-   
    
        
    
    You have a specific query that you want to ensure is as performant as possible
    
-   
    
        
    
    The query uses simple operators in one or more conditions

    -   
        
                
        
        **Yes**: Where user region = Canada
        
    -   
        
                
        
        **No**: Where user ID is even, or user region is empty
            
-   
    
        
    
    The table has 10,000 records or more
    
-   
    
        
    
    The table is not frequently written to or updated

    -   
        
                
        
        This is because when a table is indexed and frequently written to, the performance of inserting new data can suffer because the index has to be updated at the same time. You can index a table that has frequent writes, but use caution.
            
 

How do I apply an index properly?

It's important to construct your index based on the query being performed that you are trying to address. We will use the an example scenario to explain an approach to indexing. All scenarios were built and performed on a Launch plan instance with no additional load or processing. Your results may vary based on other factors related to your specific instance or the plan you are on.

####  

Example Table: 515,195 records, with the following schema

id

name

region

country

profession

firstname

lastname

email

birthday

####  

Example Query: Find all users in a specific country, with a specific profession

![](../../_gitbook/image9235.jpg?url=https%3A%2F%2Flh3.googleusercontent.com%2FDqBBS92W4kPeFmqQ_opVpKYhaZjOlvMj_-F5W5f6FsbYRNYepExRJ57jOfdR-obut1jM25r-e3PsqUaZ2c8p4GsL7idsLdP3hQe3p3yITkTxeno21GuXBq3McFgC2uwvj0EzbEEJrbFa-F7vWh7rN-w&width=768&dpr=4&quality=100&sign=7455f455&sv=2)

Example query with no indexing

With no indexing applied, this query takes **0.62** seconds to complete.

Because these two pieces of data can exist independently of each other \-- meaning we don\'t need to know a country to determine a profession, and vice versa, we will apply two separate indexes to our table, one for each field.

![](../../_gitbook/image23af.jpg?url=https%3A%2F%2Flh5.googleusercontent.com%2FHKQ-aHlQjct6toQpewypBYsLXLdD5Y8hH3nk7gi_cTxUjk3gaxbjeMT83iIcaPb8Z1IO-f8SAF2xTiWsepqpfAm_qd6v4RVCG07CSN65ShG_Q-zmZrKtS6rBICqVRtYXK1sjBuDhw-7XE8FpZwbQYvM&width=768&dpr=4&quality=100&sign=13ec09cd&sv=2)

Indexes applied based on the sample query

With these indexes applied, the example query now executes in **0.05** seconds, a **95% increase in query speed.**

![](../../_gitbook/imageaedc.jpg?url=https%3A%2F%2Flh5.googleusercontent.com%2FHm6j45xDF7o_AZLnIZKt6rpCIm6G2PPuFnSSMZdW6Kn2dT34Xnkq4yEo-g5BZLZCF-g0VeQm6FtVlWmysjcr03D15ajBGMdrVrpE7k683g8FwrKcziY-kJCdG71WDsOdJLH-p0YLTPRX9rkxProi95c&width=768&dpr=4&quality=100&sign=16a4929a&sv=2)

Example query with indexing applied

###  

When should I index a single field by itself vs multiple fields in the same index?

This is based on the hierarchy of the query being performed, and what makes the most sense in terms of your data set. It is also important to understand how multi-field indexes are executed.

**The order of fields in your index matters.** When building a multi-field index, you want to start with the field that contains the **least** amount of unique values, moving forward to finishing with the field that has the **most** unique values.

With a multi-field index, each \'step\' (field) is essentially placed into a new bucket that the database knows it can use to potentially find matching data. Using an example of location data where we have a `city`, `state`, and `country` field, we know that country has the least unique values. This means that when we\'re building our index, we\'d add the country field first. Moving on from there, we would add our states, and then finally the cities, so when the database builds the index, it builds the most efficient bucketing possible.

In an adverse example, consider an index on a timestamp field. Timestamps in Xano use milliseconds, which obviously means that these values will almost be unique for every single record. If we built a multi-field index that started with this timestamp field, we are creating that many buckets right away before trying to look for less specific data, which means that the query becomes extremely inefficient.

It is also important to note that if you have multiple fields defined in a single index, but are not using both of those fields in your query, the index will not provide any benefit to the performance of that query. Indexes are only useful if you are indexing based on the queries you are making, and the hierarchy of your query makes sense.

You can use a field in a double-field index as well as a single-field index, but it is important to consider the storage requirement for each index you create. In addition, it is possible to 'trap' yourself into a situation where you have too many indexes, and it becomes more difficult to determine what is helping and what is not.

**Example Query: Find all users who are part of a specific subset of artists**

![](../../_gitbook/image7d7d.jpg?url=https%3A%2F%2Flh5.googleusercontent.com%2FTE8piA-TZd-1pohkWh7GO3RuZ549fQSQU3LINMkM7uvkfuqGk5TVDp65tsIqwFW1kycjvezEtzvJ8RfQtREhdYCl4kXnK2YCaIGgubAyRbFcbNbaxZymu7nXSbdPK7qY1MgS2GbMAZTgAorZ5M6nafI&width=768&dpr=4&quality=100&sign=5f8412fb&sv=2)

Example query with no indexing

Executing the example query, with no indexing applied, takes **1.44s**.

Because we know that the artist\_service field requires the profession field to make sense in the context of our query, we will place both of those fields, in order, in the same index.

![](../../_gitbook/image20f3.jpg?url=https%3A%2F%2Flh4.googleusercontent.com%2Fd2SO_6uzBigUQvCbSnVTuXs_afX0f4oM0yUveZeQ5VjO6SFg0PKv2lXI6G2ORqAFMRGPJZ0lQc2_E8sJ97Bwp0HgzGF5xsNh7CN71Y9Orve4tVWtBAKDAL0YwmOpIDwl7YqDuXtIvpV1FhAQ12hhlv0&width=768&dpr=4&quality=100&sign=114414fb&sv=2)

Applying the index for the example query

![](../../_gitbook/image869c.jpg?url=https%3A%2F%2Flh5.googleusercontent.com%2FxyJz6sIMQf1BWzUZM6d9JWjSXr9788IGaESrLwj16ffrE_U_yQ7hUZSpLGiIJUQ7l339TZBvXiyTzfdEMMMAY_map6YDR1him_xVm3MxpvOPMM4e5jxxqhPUqIpz-Tf0OWpsj267b3Py3OqnDleirME&width=768&dpr=4&quality=100&sign=74e48a6b&sv=2)

Example query results with indexing applied

After applying the index shown, this query completes in **0.02 seconds, 98% faster.**

In this same scenario, if there was a world where we would potentially query **artist\_service** by itself, and it did not also need a **profession** to make sense based on the context of our query, we would want to create single-field indexes for these fields.

**Example 2: When to use Single-Field vs. Multi-Field Indexes**

We have a table of people, and each person lives in a specific region. We want to build a query where we find all people named \"Jack\" in a specific region. We will not be building any other queries to search our table of people.

**In this example, we would build one index with both fields**. This is because we are not utilizing these fields in any other queries, and they are both required in the context of the query we are building.

**Example 3:** **When to use Single-Field vs Multi-Field Indexes**

We have a table of people, and each person lives in a specific region. We want to build a query where we find all people named \"Jack\" in a specific region. We also want to build a second query that just finds us all people named \"Jack\", and a third query that finds all people in a certain region without specifying a name.

**In this example, we would build two single-field indexes, one for each field.** This is because we are utilizing the fields in multiple different queries.

###  

Using the GIN Index to search complex data types

The GIN index is used specifically when searching through more complex data types, such as objects and arrays, as these fields can not be indexed using the methods described previously.

This index is automatically applied to all of your database tables; you do not need to add or maintain this.

Let\'s say, as an example, we have a list field called **my\_list**, and we want to find all records that contain a value of **special** inside of **my\_list.**

To use the GIN index in this query, we first need to create a variable with the following structure:

Copy

``` 
{"my_list":[
    "special"
    ]
}
```

The structure starts with an object containing the name of the field, with the value being an empty array. We then use the **push** filter to add the value we are searching for inside of that list. You can use multiple push filters to search for multiple values.

![](../../_gitbook/imagee241.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FG2iA75Tkf9aMtKEt8WcA%252FCleanShot%25202023-04-20%2520at%252016.17.16%25402x.png%3Falt%3Dmedia%26token%3D5fefbf46-5940-44a8-9c49-869f0d3c285a&width=768&dpr=4&quality=100&sign=3d1f1aa1&sv=2)

Constructing the variable to be used in our query

Once we have our object constructed, we will set up our custom query by selecting the table on the left side, which leaves us with the \'contains\' operator, and our constructed object on the right.

![](../../_gitbook/imagec3ea.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F16cefiUxuFrO4uTfH33s%252FCleanShot%25202023-04-20%2520at%252016.18.45%25402x.png%3Falt%3Dmedia%26token%3Dbbd03fcc-abe7-484b-8b6b-5a28657b4dbc&width=768&dpr=4&quality=100&sign=69df10df&sv=2)

An example of a GIN index query

In this example, a query without indexing takes **0.23** seconds.

In this example, utilizing the GIN index, the query takes **0.02** seconds.

 

How to Apply an Index in the Database View

In the database view, click on the table that you want to index. Choose \"Indexes\" from the top bar.

![](../../_gitbook/imageb1bf.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FNLSpR9dcm1yxNmP8v17c%252FCleanShot%25202023-04-20%2520at%252015.57.18.png%3Falt%3Dmedia%26token%3Dc1eea360-54a6-4d4a-b1cb-8c5355bfc9cb&width=768&dpr=4&quality=100&sign=46fc093d&sv=2)

Click \"Create Index\" to add a new index, or click on an existing index to manage it.

![](../../_gitbook/imagef842.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FSIWX3PpXi9fkHw3OO9m3%252FCleanShot%25202023-04-20%2520at%252015.58.20.png%3Falt%3Dmedia%26token%3Dc6a8d121-c191-4e92-b4f5-34b48be5c800&width=768&dpr=4&quality=100&sign=64a5ce4b&sv=2)

Choose the fields, sort, and index type. When done, click \'Save\'.

![](../../_gitbook/image1ea5.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252FdywTuWImzeBDjKXCNFVq%252FCleanShot%25202023-04-20%2520at%252015.59.07.png%3Falt%3Dmedia%26token%3D45c09db0-7c28-4bc2-9521-622fef66e9b0&width=768&dpr=4&quality=100&sign=2d8b59a&sv=2)

**Note**: Creating or updating an index can take several minutes depending on the complexity and the size of the database table.

**Note**: Indexes will significantly increase the storage your database table requires. Please ensure you have enough free space (we recommend trying to stay around \~50% free space) before indexing your tables.

###  

Types of Indexes

-   
    
        
    
    **Primary**

    -   
        
                
        
        Automatically applied and maintained
        
    -   
        
                
        
        Indexes the primary key (ID) of each record and enforces uniqueness
            
-   
    
        
    
    **GIN**

    -   
        
                
        
        Automatically applied and maintained
        
    -   
        
                
        
        Most suitable for complex data types (JSON, lists, objects) and full-text search
            
-   
    
        
    
    **Index**

    -   
        
                
        
        The most common index type
        
    -   
        
                
        
        Used when indexing for standard queries
            
-   
    
        
    
    **Unique**

    -   
        
                
        
        A special type of index to enforce unique values in a column'
            
-   
    
        
    
    **Spatial**

    -   
        
                
        
        A special type of index designed to optimize queries involving spatial data, such as geography fields.
            
-   
    
        
    
    **Search**

    -   
        
                
        
        A special type of index to be used in conjunction with Xano fuzzy search
            
-   
    
        
    
    **Vector**

    -   
        
                
        
        A unique indexing type used for working with the [Vector field type](../database-basics/field-types.html#vector).
        
    -   
        
                
        
        Indexing should **always** be used on vector columns, regardless of the amount of records.

        -   
            
                        
            
            **L2 Distance** - Measures the Euclidean distance between vectors
            
        -   
            
                        
            
            **L1 Distance** - Measures the taxicab distance between vectors.
            
        -   
            
                        
            
            **Inner product** - Measures dissimilarity based solely on amplitude (recommended for OpenAI and other normalized vectors)
            
        -   
            
                        
            
            **Cosine Distance** - Measures dissimilarity between vectors, considering their length and amplitude
                        
 

When should you *not* use an index?

-   
    
        
    
    Do not use an index on a table containing only a few records. They are most valuable when your record count approaches \>5,000 records.
    
-   
    
        
    
    Indexes should not be used on fields that have or will have a high number of **null** values, because that essentially means there is nothing to index on.
    
-   
    
        
    
    You can not apply a normal index to an array or object field, so keep that in mind when designing your database structure. You can use the automatically maintained GIN index, detailed later on this page.
    
-   
    
        
    
    If your field / column names are frequently changing, you should not index that field.
    
-   
    
        
    
    If a table is frequently used to add / edit data, it may be best practice to not index this table. While your query speeds can still benefit, they can also slow the performance of adding to or editing data on this table given the nature of creating an index behind the scenes.
    

Last updated 7 months ago

Was this helpful?