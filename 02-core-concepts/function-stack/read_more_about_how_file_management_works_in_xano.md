---
category: function-stack
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Read more about how file management works in Xano
---

# Read more about how file management works in Xano

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
    Read more about how file management works in Xano
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Functions
File Storage 
============
###  
Read more about how file management works in Xano
[[File Storage in Xano]]
The Content Upload Flow
When working with files in Xano, they can exist in a few different states.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **File Resource**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        The file resource can be thought of as a reference to your raw file data. It is a base64 encoded string that represents the file during execution, enabling you to pass the data through variables and functions that handle content management with ease.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Raw File Data**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        When necessary, you do also have the ability to turn your file resource into raw file data, and manipulate it inside of the function stack when appropriate, such as a CSV file.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Metadata**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        While the metadata is not a representation of the file data itself, the metadata is necessary when the file needs to be referenced inside of a database table. The tables do not store the files themselves, but hold onto the metadata, so that when the record is retrieved, you can also retrieve the file data, or deliver a link to the file.
        :::
    :::
Files in Xano always start with a **file resource**. Here\'s what a typical flow looks like. In this example, we\'ll be adding a file to our database table.
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Files in a function stack always start with a **file resource.** The file resource can come via a **file resource input**, or by using a **Create File Resource** function in the function stack itself (such as if the file comes from an external API request).
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    After we have our file resource (in this case, our File Resource input), we need to generate **metadata** for that file in preparation to store it in our database table.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Finally, once we have our **metadata**, we can write it to our database table, adding the metadata to the appropriate field in the record.
    :::
This is the simplest and most typical scenario when working with files in Xano. Following this flow will allow you to ingest files through your API and store them in your database. You can then read the metadata from the table and use the URL from there to deliver those files back to your front-end.
Input, Field Types, and Functions
###  
The File Resource Input
Your content upload function stacks should always start with a **file resource input**, if your users are uploading files through your application. You can then utilize the file resource input in future functions, such as **metadata generation,** to store the file in your database or return a URL to the file.
###  
Field Types
Xano supports several different field types in the database related to content upload.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Image** - For storing images
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Video** - For storing video
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Audio** - For storing audio
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Attachment** - For storing anything else
    :::
###  
Functions
The Content Upload Functions are:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Create Image Metadata** - Creates image metadata from a file resource so that it can be formatted properly to be stored in Xano.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Create Video Metadata** - Creates video metadata from a file resource so that it can be formatted properly to be stored in Xano.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Create Audio Metadata** - Creates auto metadata from a file resource so that it can be formatted properly to be stored in Xano
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Create Attachment Metadata** - Creates attachment metadata from a file resource so that it can be formatted properly to be stored in Xano.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Create File Resource** - This functions is able to create a file resource in the function stack from a variable. Typically, you will use a file resource as an input. However, there are certain use cases, for example, where you may hit an external API which is providing you with a raw image or file. In this event, you will want to first use this function to create a file resource then use one of the create metadata functions.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Delete File Resource** - This function will permanently delete a file stored in your Xano file storage. You\'ll usually pair this with a database operation like Get Record / Query All Records, or you can delete a file created earlier in your function stack as long as one of the Metadata functions have been executed, as the Delete File Resource function requires you to specify the path to the file.
    **Files are not recoverable. Proceed with caution**.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Create File Resource** - Creates a new, empty zip file that you can add files to in your function stack
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Add File Resource** - Used to add additional files into an existing zip file
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Remove File Resource** - Used to remove files from an existing zip file
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Extract Zip File Resource** - Used to extract a zip file and generate separate file resources for each file extracted
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: View Contents** - Show details about the files contained inside of a zip file
    :::
Serving File Downloads
There are a couple of different ways you can serve downloads of files, depending on your use case.
<div>
1
###  
Provide the URL for your frontend to process.
When you use one of the **Create Metadata** steps to store the file in your Xano files library, it returns a **path** key which contains a path to the file.
Returning a complete URL requires prepending this path with the URL to your Xano instance.
If our metadata looks like this\...
Copy
``` 
{
    "access":"public",
    "path":"/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf",
    "name":"form_submission_1741703680742.pdf",
    "type":"pdf",
    "size":3247192,
    "mime":"application/pdf",
    "meta":
    }
```
\...our full URL would look like this:
Copy
``` 
https://my-xano-instance.xano.io/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf
```
2
###  
Serve the raw file contents for direct download.
If you want an API call to immediately initiate a file download, add the following headers to your function stack using the **HTTP Header** function.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    `Content-Disposition: attachment; filename="replaceme"`
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    `Content-Type: application/octet-stream`
    :::
These headers will tell any browser accessing the API that we\'re serving a direct download. Just make sure to change \"replaceme\" to the actual filename you are serving.
Add a **Get File Resource Data** function so we have the raw file data to be delivered.
Finally, in your response, return the .`data `path from the output of **Get File Resource Data**.
Your function stack should look something like this:
To ensure it\'s working as expected, when you run it in Xano, you should see a **Download** button available in the Run panel.
</div>
Private File Storage
Private file storage is available as a premium add-on for our Launch plans, or included with **Scale** or HIPAA compliance.
All files stored as private files are only accessible through on-demand time sensitive URL generation. This means that all files in your Private Storage are inaccessible until you generate a new URL in your function stack.
To work with private file storage, there are two key components to understand: **private file database fields** and the **Private File: Sign URL function.**
###  
**Private File Database Field**
To store files in your private files library and have them accessible from your function stacks, you\'ll need to use a database field that is enabled for private file storage. You can enable this for any of the current file field types. Keep in mind that the file access is defined per field, which means that you can not store both public and private files in the same field.
[]
When private files are enabled for a file storage field, a lock icon is displayed in the field name. You will also notice that private files do not display previews from the database view; this is by design, as the files are not accessible until a new URL is generated.
[]
###  
**Private File: Sign URL function**
To generate a signed URL that enables a private file to be accessible, you first need to retrieve the path of the file, which is stored in the database record. In this example, we have queried our files table and this is the expected return for a private image. The main difference here is that on public files, a URL is returned. For private files, no URL is provided.
[]
We can then leverage the **Private File: Sign URL** function to generate a publicly accessible link to the file. Provide the path as offered from the database record, a TTL (how long in seconds the link should be valid for), and finally a return variable to contain the output of the function
[]
When we run this function, we are returned our new signed URL.
[]
Zip Management
<div>
</div>
###  
Viewing Zip File Contents
In this example, all we want to do is upload a zip file and review its contents in our function stack.
We\'ve added our file resource input to ingest the file, and then utilize the **Zip: View Contents** function, targeting our file resource input. We can also provide a password to this function if our zip file requires one to open.
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: View Contents** - Returns the contents of our zip file to a variable
    :::
###  
Extracting a Zip File
In this example, our users will be uploading a zip file. We then want to extract all of those files from the zip file in order to add those files individually to our database.
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Create Attachment Metadata** - Creates metadata for the uploaded zip file so we can get the filename
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Extract Zip File Resource** - Extracts the zip file and returns individual file resources for each file
    []
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Create Variable** - Creates an empty array to store our individual files metadata
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    **For Each Loop** - Loops against the array of file resources created in step 2
    1.  ::: 
        ::: 
        :::
        :::
        ::: 
        **Conditional** - Checks for junk files generated by Mac OS and skips them. This step is optional.
        1.  ::: 
            ::: 
            :::
            :::
            ::: 
            **Create Attachment** - Creates metadata for the file resource that the loop is currently iterating through
            :::
        2.  ::: 
            ::: 
            :::
            :::
            ::: 
            **Array: Add to End** - Adds the generated metadata to our metadata array established in step 3
            :::
        :::
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Add Record** - Adds our metadata to the database
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Delete File** - Deletes the zip file. This is only necessary if you generate metadata for it as we did in step 1.
    :::
###  
Adding to a zip file
In this example, our users are uploading a zip file, and we want to add another file to that same zip file. We have two file resource inputs: one is for the zip file, and one is for the new file to add.
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Add File Resource** - Adds the new file into the existing zip file
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: View Contents** - Allows us to view the contents of the updated zip file
    :::
###  
Removing from a zip file
In this example, our users are uploading a zip file, as well as specifying a file to remove, and we want to remove that file from the zip file. We have two inputs: a file resource input for the zip file, and a text input for the file name to remove.
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Delete File Resource** - Removes the file matching the filename from the existing zip file
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: View Contents** - Allows us to view the contents of the updated zip file
    :::
###  
Creating a zip file from scratch
See Serving File Downloads to learn how to provide a download of a created ZIP file.
In this example, our users are uploading multiple files, and we want to store them inside of a zip file.
**From multiple file resource inputs**
In this scenario, we have multiple file resource inputs for each incoming file.
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Create File Resource** - Creates our zip file that we can add to in the rest of the function stack
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Add File Resource** - Adds the data from file1 into our zip file
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Add File Resource** - Adds the data from file2 into our zip file
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: View Contents** - Allows us to review the zip file contents after completion
    :::
**From an array of files via a single file resource input**
In this scenario, we have a single file resource input, formatted as a list. This is good if you need to dynamically determine how many files your API is ingesting.
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: Create File Resource** - Creates our zip file that we can add to in the rest of the function stack
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **For Each Loop** - Loops against our list file resource input
    1.  ::: 
        ::: 
        :::
        :::
        ::: 
        **Zip: Add File Resource** - Adds the file the loop is currently iterating through to our zip file established in step 1
        :::
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Zip: View Contents** - Allows us to review the zip file contents after completion
    :::
###  
A note about encryption
Xano supports creating and working with encrypted zip files. In the zip functions available, you\'ll notice one or both of the following fields:
[]
The **password** field is to set the password you want applied to the zip file.
The **password\_encryption** field is available for you to set the encryption method applied to the zip file upon creation. The following encryption methods are available:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Standard** - This is the most compatible form of encryption (Traditional PKWARE encryption). This is required if you need to be able to extract your zip files using Windows\' native zip extraction.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **AES-128**
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **AES-256**
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **AES-512**
    :::
Last updated 3 months ago
Was this helpful?

## Code Examples

```javascript
 
{
    "access":"public",
    "path":"/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf",
    "name":"form_submission_1741703680742.pdf",
    "type":"pdf",
    "size":3247192,
    "mime":"application/pdf",
    "meta":
    }

```

```
 
https://my-xano-instance.xano.io/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf

```

