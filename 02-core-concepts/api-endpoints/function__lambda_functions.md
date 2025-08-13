---
category: api-endpoints
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'Function: Lambda Functions'
---

# Function: Lambda Functions

[](../../../index.html)
Xano Documentation
[Ctrl][K]
-   ::: 
    Before You Begin
    :::
-   ::: 
    [🛠️]The Visual Builder
    :::
        ::: 
            ::: 
            -   Swagger (OpenAPI Documentation)
            :::
            ::: 
            -   Async Functions
            :::
        -   Background Tasks
        -   Triggers
        -   Middleware
        -   Configuring Expressions
        -   Working with Data
        :::
        ::: 
        -   AI Tools
            ::: 
                ::: 
                -   External Filtering Examples
                :::
            -   Get Record
            -   Add Record
            -   Edit Record
            -   Add or Edit Record
            -   Patch Record
            -   Delete Record
            -   Bulk Operations
            -   Database Transaction
            -   External Database Query
            -   Direct Database Query
            -   Get Database Schema
            :::
            ::: 
            -   Create Variable
            -   Update Variable
            -   Conditional
            -   Switch
            -   Loops
            -   Math
            -   Arrays
            -   Objects
            -   Text
            :::
        -   Security
            ::: 
            -   Realtime Functions
            -   External API Request
            -   Lambda Functions
            :::
        -   Data Caching (Redis)
        -   Custom Functions
        -   Utility Functions
        -   File Storage
        -   Cloud Services
        :::
        ::: 
        -   Manipulation
        -   Math
        -   Timestamp
        -   Text
        -   Array
        -   Transform
        -   Conversion
        -   Comparison
        -   Security
        :::
        ::: 
        -   Text
        -   Expression
        -   Array
        -   Object
        -   Integer
        -   Decimal
        -   Boolean
        -   Timestamp
        -   Null
        :::
        ::: 
        -   Response Caching
        :::
-   ::: 
    Testing and Debugging
    :::
-   ::: 
    The Database
    :::
        ::: 
        -   Using the Xano Database
        -   Field Types
        -   Relationships
        -   Database Views
        -   Export and Sharing
        -   Data Sources
        :::
        ::: 
        -   Airtable to Xano
        -   Supabase to Xano
        -   CSV Import & Export
        :::
        ::: 
        -   Storage
        -   Indexing
        -   Maintenance
        -   Schema Versioning
        :::
-   ::: 
    Build For AI
    :::
        ::: 
        -   Templates
        :::
        ::: 
        -   Connecting Clients
        -   MCP Functions
        :::
-   ::: 
    Build With AI
    :::
-   ::: 
    File Storage
    :::
-   ::: 
    Realtime
    :::
-   ::: 
    Maintenance, Monitoring, and Logging
    :::
        ::: 
        :::
-   ::: 
    Building Backend Features
    :::
        ::: 
        -   Separating User Data
        -   Restricting Access (RBAC)
        -   OAuth (SSO)
        :::
-   ::: 
    Xano Features
    :::
        ::: 
        -   Release Track Preferences
        -   Static IP (Outgoing)
        -   Change Server Region
        -   Direct Database Connector
        -   Backup and Restore
        -   Security Policy
        :::
        ::: 
        -   Audit Logs
        :::
        ::: 
        -   Xano Link
        -   Developer API (Deprecated)
        :::
        ::: 
        -   Master Metadata API
        -   Tables and Schema
        -   Content
        -   Search
        -   File
        -   Request History
        -   Workspace Import and Export
        -   Token Scopes Reference
        :::
-   ::: 
    Xano Transform
    :::
-   ::: 
    Xano Actions
    :::
-   ::: 
    Team Collaboration
    :::
-   ::: 
    Agencies
    :::
        ::: 
        -   Agency Dashboard
        -   Client Invite
        -   Transfer Ownership
        -   Agency Profile
        -   Commission
        -   Private Marketplace
        :::
-   ::: 
    Custom Plans (Enterprise)
    :::
        ::: 
            ::: 
                ::: 
                -   Choosing a Model
                :::
            :::
        -   Tenant Center
        -   Compliance Center
        -   Security Policy
        -   Instance Activity
        -   Deployment
        -   RBAC (Role-based Access Control)
        -   Xano Link
        -   Resource Management
        :::
-   ::: 
    Your Xano Account
    :::
-   ::: 
    Troubleshooting & Support
    :::
        ::: 
        -   When a single workflow feels slow
        -   When everything feels slow
        -   RAM Usage
        -   Function Stack Performance
        :::
        ::: 
        -   Granting Access
        -   Community Code of Conduct
        -   Community Content Modification Policy
        -   Reporting Potential Bugs and Issues
        :::
-   ::: 
    Special Pricing
    :::
-   ::: 
    Security
    :::
-   ::: 
    :::
    How do I write Lambda functions in Xano?
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Functions
3.  APIs & Lambdas
Lambda Functions 
================
Quick Summary
Lambda functions allow you to execute JavaScript or TypeScript inside of your Xano function stacks. You may prefer to do this if you are porting old workflows to Xano and already have the code written, or maybe you just prefer to write code instead of using the function stack.
You can also use Lambda functions to leverage custom NPM packages.
How do I write Lambda functions in Xano?
####  
Special Variables
Lambdas have the ability to reference all the available data just like normal function stack statements. All special variables are prefixed with a `$` symbol.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Xano variables are accessible through the `$var` special variable. To access a Xano variable named title, you would reference it as `$var.title`.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Xano inputs are accessible through the `$input` special variable. To access a Xano input named score, you would reference it as `$input.score`.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Xano environment variables are accessible through the `$env` special variable. To access a Xano environment variable named ip, you would reference it as `$env.ip`.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The authenticated user details are accessible through the `$auth` special variable. The most common members of this variable include `$auth.id` and `$auth.extras`. If there is no authenticated user, then `$auth.id` will evaluate as 0.
    :::
####  
Context Variables
Depending on how you use a Lambda, you may have support to access some additional variables, known as context variables. These follow the same naming convention as special variables by using a `$` prefix. The most common context variables will be `$this`, `$index`, `$parent`, and `$result`. The meaning of these variables are best described within the examples of the higher order filters.
Using the Lambda AI Assistant
<div>
1
###  
Give the assistant context by running your function stack first.
If you don\'t do this, you can still use the AI assistant, but it will make certain inferences that may not be correct.
2
###  
Look for the [] button and click it to enable the assistant.
3
###  
Ask the assistant for help as needed.
In this example, we\'re asking the assistant to write a function that imports the Decamelize library and applies it to our \'test\' input.
4
###  
Choose how to proceed with the assistant\'s suggestions.
You can click [] to add the suggestions to the Lambda function code, or you can copy it manually and place it as needed.
Be sure to **rate the assistant\'s suggestion(s)** using the [👍] and [👎] buttons. We\'ll use this information to improve the behavior of the assistant in future iterations.
</div>
Using NPM Packages
Before you begin
It is **highly recommended** that you include version numbers in your imports to ensure code stability; this will allow you time to verify updates to packages and avoid any potential issues.
If you have an NPM package you\'d like to use in your Lambda functions, you can import it using the following format:
Copy
``` 
const  = await import ("npm:decamelize");
```
When we want to utilize the functions imported from the package listed, we can do so like this:
Copy
``` 
return Decamelize($input.test);
```
Native Node libraries that are native can be accessed with a `node:` prefix instead of `npm:`
Copy
``` 
const  = await import("node:https");
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
const  = await reader.read();
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
await Deno.writeTextFile("/path/to/log.txt", "New log entry\n", );
```
###  
File Operations
####  
Check if File Exists
Copy
``` 
try  catch (error) {
  if (error instanceof Deno.errors.NotFound)  else 
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
await Deno.mkdir("/path/to/nested/dir", );
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
await Deno.remove("/path/to/dir", );
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
import  from "https://deno.land/std/path/mod.ts";
const filePath = join("dir", "subdir", "file.txt"); // OS-appropriate path joining
const dir = dirname("/path/to/file.txt"); // "/path/to"
const base = basename("/path/to/file.txt"); // "file.txt"
const ext = extname("/path/to/file.txt"); // ".txt"
```
###  
Important Notes for Xano Lambda Environment
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    In Xano\'s Lambda environment, filesystem operations are primarily useful for temporary file operations
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Use the `/tmp` directory for temporary file storage
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Files in the Lambda environment are ephemeral - they will not persist between function calls
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Filesystem operations are useful for:
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Processing uploaded files
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Generating temporary files for processing
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Creating logs or debug information
        :::
    :::
Last updated 1 month ago
Was this helpful?

## Code Examples

```
 
const  = await import ("npm:decamelize");

```

```
 
return Decamelize($input.test);

```

```
 
const  = await import("node:https");

```

```
 
// Read entire file as string
const content = await Deno.readTextFile("/path/to/file.txt");

```

```
 
// Read entire file as Uint8Array
const data = await Deno.readFile("/path/to/file.bin");

```

```
 
// Open a file for reading as a stream
const file = await Deno.open("/path/to/large-file.txt");
// Create a reader from the file
const reader = file.readable.getReader();
// Read chunks
const  = await reader.read();
// Close the file when done
file.close();

```

```
 
// Write string to file (creates or overwrites)
await Deno.writeTextFile("/path/to/output.txt", "Hello, world!");

```

```
 
// Write binary data to file
const data = new Uint8Array([104, 101, 108, 108, 111]);
await Deno.writeFile("/path/to/output.bin", data);

```

```
 
// Append to an existing file
await Deno.writeTextFile("/path/to/log.txt", "New log entry\n", );

```

```javascript
 
try  catch (error) {
  if (error instanceof Deno.errors.NotFound)  else 
}

```

```
 
await Deno.copyFile("/path/source.txt", "/path/destination.txt");

```

```
 
await Deno.rename("/path/oldname.txt", "/path/newname.txt");

```

```
 
await Deno.remove("/path/to/file.txt");

```

```
 
// Create a single directory
await Deno.mkdir("/path/to/dir");
// Create nested directories (like mkdir -p)
await Deno.mkdir("/path/to/nested/dir", );

```

```
 
// List files and directories in a directory
for await (const entry of Deno.readDir("/path/to/dir")) 

```

```
 
// Remove empty directory
await Deno.remove("/path/to/empty-dir");
// Remove directory with contents
await Deno.remove("/path/to/dir", );

```

```
 
const fileInfo = await Deno.stat("/path/to/file.txt");
console.log(fileInfo.size); // Size in bytes
console.log(fileInfo.mtime); // Last modification time
console.log(fileInfo.birthtime); // Creation time
console.log(fileInfo.isFile); // Is it a file
console.log(fileInfo.isDirectory); // Is it a directory

```

```
 
// Check if we have read permission
const canRead = await Deno.permissions.query();

```

```
 
// Create a temp file and return its path
const tempFile = await Deno.makeTempFile();

```

```
 
// Create a temp directory and return its path
const tempDir = await Deno.makeTempDir();

```

```
 
import  from "https://deno.land/std/path/mod.ts";
const filePath = join("dir", "subdir", "file.txt"); // OS-appropriate path joining
const dir = dirname("/path/to/file.txt"); // "/path/to"
const base = basename("/path/to/file.txt"); // "file.txt"
const ext = extname("/path/to/file.txt"); // ".txt"

```

