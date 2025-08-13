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
    
    [How do I write Lambda functions in Xano?](#how-do-i-write-lambda-functions-in-xano)

-   [Using the Lambda AI Assistant](#using-the-lambda-ai-assistant)

-   [Using NPM Packages](#npm)

-   [Working with Files](#working-with-files)

-   [Reading Files](#reading-files)

-   [Writing Files](#writing-files)

-   [File Operations](#file-operations)

-   [Directory Operations](#directory-operations)

-   [File Information](#file-information)

-   [Temporary Files and Directories](#temporary-files-and-directories)

-   [Working with Paths](#working-with-paths)

-   [Important Notes for Xano Lambda Environment](#important-notes-for-xano-lambda-environment)

Was this helpful?

Copy


2.  Functions
3.  [APIs & Lambdas](../apis-and-lambdas.html)

Lambda Functions 
================

 

Quick Summary

Lambda functions allow you to execute JavaScript or TypeScript inside of your Xano function stacks. You may prefer to do this if you are porting old workflows to Xano and already have the code written, or maybe you just prefer to write code instead of using the function stack.

You can also use Lambda functions to leverage custom NPM packages.

 

How do I write Lambda functions in Xano?

####  

Special Variables

Lambdas have the ability to reference all the available data just like normal function stack statements. All special variables are prefixed with a `$` symbol.

-   
    
        
    
    Xano variables are accessible through the `$var` special variable. To access a Xano variable named title, you would reference it as `$var.title`.
    
-   
    
        
    
    Xano inputs are accessible through the `$input` special variable. To access a Xano input named score, you would reference it as `$input.score`.
    
-   
    
        
    
    Xano environment variables are accessible through the `$env` special variable. To access a Xano environment variable named ip, you would reference it as `$env.ip`.
    
-   
    
        
    
    The authenticated user details are accessible through the `$auth` special variable. The most common members of this variable include `$auth.id` and `$auth.extras`. If there is no authenticated user, then `$auth.id` will evaluate as 0.
    
####  

Context Variables

Depending on how you use a Lambda, you may have support to access some additional variables, known as context variables. These follow the same naming convention as special variables by using a `$` prefix. The most common context variables will be `$this`, `$index`, `$parent`, and `$result`. The meaning of these variables are best described within the examples of the [higher order filters](../../filters/transform.html#lambda-filters).

 

Using the Lambda AI Assistant

<div>

1

###  

Give the assistant context by running your function stack first.

If you don\'t do this, you can still use the AI assistant, but it will make certain inferences that may not be correct.

2

###  

Look for the [![](../../../_gitbook/image9913.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F3A8Nrwer2IbTCTrRExe0%252FCleanShot%25202025-02-24%2520at%252010.43.11.png%3Falt%3Dmedia%26token%3De15eb6f0-d3be-4fe1-821c-7019198ea0a5&width=300&dpr=4&quality=100&sign=79004e2c&sv=2)] button and click it to enable the assistant.

3

###  

Ask the assistant for help as needed.

In this example, we\'re asking the assistant to write a function that imports the Decamelize library and applies it to our \'test\' input.

![](../../../_gitbook/image16ed.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252F5n6Ova55hjKAtMx4MIRs%252FCleanShot%25202025-02-24%2520at%252010.45.23.png%3Falt%3Dmedia%26token%3Dea46c9d1-d114-4f91-aa4c-f4115b928de4&width=768&dpr=4&quality=100&sign=6eddd1f6&sv=2)

4

###  

Choose how to proceed with the assistant\'s suggestions.

You can click [![](../../../_gitbook/image2f61.jpg?url=https%3A%2F%2F3699875497-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2tWsL4o1vHmDGb2UAUDD%252Fuploads%252Fpo252whDIYwwhJkStZSp%252FCleanShot%25202025-02-24%2520at%252010.46.22.png%3Falt%3Dmedia%26token%3Dee2d23bc-c146-4d86-b3f6-210c0770593f&width=300&dpr=4&quality=100&sign=1613754a&sv=2)] to add the suggestions to the Lambda function code, or you can copy it manually and place it as needed.

Be sure to **rate the assistant\'s suggestion(s)** using the [👍] and [👎] buttons. We\'ll use this information to improve the behavior of the assistant in future iterations.

</div>

 

Using NPM Packages

 

Before you begin

It is **highly recommended** that you include version numbers in your imports to ensure code stability; this will allow you time to verify updates to packages and avoid any potential issues.

If you have an NPM package you\'d like to use in your Lambda functions, you can import it using the following format:

Copy

``` 
const { default: Decamelize } = await import ("npm:decamelize");
```

When we want to utilize the functions imported from the package listed, we can do so like this:

Copy

``` 
return Decamelize($input.test);
```

Native Node libraries that are native can be accessed with a `node:` prefix instead of `npm:`

Copy

``` 
const { request } = await import("node:https");
```

Please note that not all NPM packages may function properly inside of Xano. If you encounter an issue importing a specific package, please reach out to our support team for further clarification.

 

**Working with Files**

Xano provides a comprehensive set of filesystem functions that allow you to read, write, and manipulate files and directories. These functions are available through the global `Deno` namespace.

###  

Reading Files

####  

Read Text Files

Copy

``` 
// Read entire file as string
const content = await Deno.readTextFile("/path/to/file.txt");
```

####  

Read Binary Files

Copy

``` 
// Read entire file as Uint8Array
const data = await Deno.readFile("/path/to/file.bin");
```

####  

Read File Stream

Copy

``` 
// Open a file for reading as a stream
const file = await Deno.open("/path/to/large-file.txt");
// Create a reader from the file
const reader = file.readable.getReader();
// Read chunks
const { value, done } = await reader.read();
// Close the file when done
file.close();
```

###  

Writing Files

####  

Write Text Files

Copy

``` 
// Write string to file (creates or overwrites)
await Deno.writeTextFile("/path/to/output.txt", "Hello, world!");
```

####  

Write Binary Files

Copy

``` 
// Write binary data to file
const data = new Uint8Array([104, 101, 108, 108, 111]);
await Deno.writeFile("/path/to/output.bin", data);
```

####  

Append to Files

Copy

``` 
// Append to an existing file
await Deno.writeTextFile("/path/to/log.txt", "New log entry\n", { append: true });
```

###  

File Operations

####  

Check if File Exists

Copy

``` 
try  catch (error)  else {
    // Other error
  }
}
```

####  

Copy Files

Copy

``` 
await Deno.copyFile("/path/source.txt", "/path/destination.txt");
```

####  

Rename/Move Files

Copy

``` 
await Deno.rename("/path/oldname.txt", "/path/newname.txt");
```

####  

Delete Files

Copy

``` 
await Deno.remove("/path/to/file.txt");
```

###  

Directory Operations

####  

Create Directory

Copy

``` 
// Create a single directory
await Deno.mkdir("/path/to/dir");

// Create nested directories (like mkdir -p)
await Deno.mkdir("/path/to/nested/dir", { recursive: true });
```

####  

Read Directory Contents

Copy

``` 
// List files and directories in a directory
for await (const entry of Deno.readDir("/path/to/dir")) 
```

####  

Remove Directory

Copy

``` 
// Remove empty directory
await Deno.remove("/path/to/empty-dir");

// Remove directory with contents
await Deno.remove("/path/to/dir", { recursive: true });
```

###  

File Information

####  

Get File Stats

Copy

``` 
const fileInfo = await Deno.stat("/path/to/file.txt");
console.log(fileInfo.size); // Size in bytes
console.log(fileInfo.mtime); // Last modification time
console.log(fileInfo.birthtime); // Creation time
console.log(fileInfo.isFile); // Is it a file
console.log(fileInfo.isDirectory); // Is it a directory
```

####  

File Permissions

Copy

``` 
// Check if we have read permission
const canRead = await Deno.permissions.query();
```

###  

Temporary Files and Directories

####  

Create Temporary File

Copy

``` 
// Create a temp file and return its path
const tempFile = await Deno.makeTempFile();
```

####  

Create Temporary Directory

Copy

``` 
// Create a temp directory and return its path
const tempDir = await Deno.makeTempDir();
```

###  

Working with Paths

Deno provides a `path` module for working with file paths:

Copy

``` 
import { join, dirname, basename, extname } from "https://deno.land/std/path/mod.ts";

const filePath = join("dir", "subdir", "file.txt"); // OS-appropriate path joining
const dir = dirname("/path/to/file.txt"); // "/path/to"
const base = basename("/path/to/file.txt"); // "file.txt"
const ext = extname("/path/to/file.txt"); // ".txt"
```

###  

Important Notes for Xano Lambda Environment

1.  
    
        
    
    In Xano\'s Lambda environment, filesystem operations are primarily useful for temporary file operations
    
2.  
    
        
    
    Use the `/tmp` directory for temporary file storage
    
3.  
    
        
    
    Files in the Lambda environment are ephemeral - they will not persist between function calls
    
4.  
    
        
    
    Filesystem operations are useful for:

    -   
        
                
        
        Processing uploaded files
        
    -   
        
                
        
        Generating temporary files for processing
        
    -   
        
                
        
        Creating logs or debug information
            

Last updated 1 month ago

Was this helpful?