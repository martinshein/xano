---
category: function-stack
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- CRUD
title: Configure
---

# Configure

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
    Elasticsearch
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Functions
Cloud Services 
==============
Elasticsearch
Elasticsearch is a robust search engine designed for quick and efficient data retrieval in applications. It handles diverse data types, employs a distributed architecture, and offers a powerful query language for real-time search needs. Integration into your applications enhances search experiences, enabling developers to implement efficient full-text searches and complex queries. Elasticsearch\'s indexing capabilities make it valuable for applications such as monitoring systems, log analysis tools, and other scenarios requiring fast and relevant data access.
**Below is a video for our OpenSearch functionality, which can be used as a reference when working with our Elasticsearch functions; they are largely the same.**
<div>
</div>
Xano offers a few functions to make Elasticsearch requests simple.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Elasticsearch: Query Wizard
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Elasticsearch: Document
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Elasticsearch: Request
    :::
Connect to Elasticsearch
Requires an Elasticsearch domain.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    `auth_type`
    Choose between `Basic` , `Bearer` or `API Key` to set the type of authentication process to use.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    `key_id`
    If using `Basic`, enter the username you wish to authenticate with.
    If using `Bearer`, leave this blank.
    If using `API Key`, enter the API key identifier you wish to authenticate with.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    `access_key`
    If using `Basic`, enter the API key secret you with to authenticate with.
    If using `Bearer` , no access key is required.
    If using `API Key` , enter the value that corresponds with the key identifier you wish to authenticate with.
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    `base_url`
    Set to the domain endpoint where Elasticsearch is hosted.
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    `index`
    Enter the name of the Elasticsearch index to send request.
    Only applicable on Document and Query functions.
    :::
Elasticsearch Query Wizard Function
Use the query wizard to easily search documents stored in Elasticsearch.
###  
Configure
See Connect to Elasticsearch for details on configuration.
Then, select a `return_type` from the options below.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `search` - Returns records that match query
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `count` - Returns number of total records matching query
    :::
###  
Query
**Query Wizard**
Set filter criteria using the Xano query builder. The left input is the field to filter on. Then set the operator and value to evaluate. Optionally, add multiple conditions using AND / OR logic.
Select 'Update Payload' to ensure your changes are reflected in the query payload.
**Output Options**
These options can only be set on 'search' return type (not 'count').
Size: the number of results to return (useful for pagination)
From: the number to offset the results (useful for pagination)
Included Fields: field names to include in the results. Can be formatted as JSON array or comma separated string.
Sort: order to return results. Default is by Elasticsearch relevance score. Option to choose one or more fields to sort in ascending or descending order.
**Payload (auto-generated)**
The JSON sent as the payload to Elasticsearch. This is generated by the Query Wizard and Output Options sections. Useful for debugging.
Dynamic values (variables, inputs, etc.) are escaped using parentheses and use Xano expression syntax. These will be evaluated at the time of the request.
Changes made directly to the payload may be overwritten by other areas of the query wizard. If you already have a query payload you want to use, it is recommended to use the Elasticsearch Request function instead.
Elasticsearch: Document (CRUD) Function
Easily get, add, update, or remove documents from an Elasticsearch index.
###  
Configure
See Connect to Elasticsearch for details on configuration.
###  
Get Document
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set method of API request to GET
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Specify doc\_id
    :::
###  
Create or Update Document
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set `method` to `POST` (create) or `PUT` (update)
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set `doc_id` (optional for POST)
    :::
###  
Elasticsearch Request
Send any Elasticsearch API request using similar configuration methods as outlined in Connect to Elasticsearch.
Set the `url` to use the desired endpoint of the request.
Set `query` to the JSON payload if necessary.
OpenSearch
OpenSearch is an open-source search and analytics tool suite, derived from ElasticSearch, offered as a scalable and flexible solution by Amazon Web Services.
With OpenSearch, you can apply natural language processing, text analyzers, and built in machine learning to quickly return the most relevant data. This makes it a great tool for log analytics, application monitoring, and website searches.
<div>
</div>
Xano offers a few functions to make OpenSearch requests simple.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    AWS OpenSearch: Query Wizard
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    AWS OpenSearch: Document
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    AWS OpenSearch: Request
    :::
Connect to OpenSearch
Requires an OpenSearch Service domain hosted by AWS.
Find AWS Documentation on Creating and managing Amazon OpenSearch Service domains.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    `auth_type`
    Choose between `IAM` (AWS Identity and Access Management) and `master` (basic auth from internal user database) to set the type of authentication process to use.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    `key_id`
    If using `IAM`, enter the IAM key id you wish to authenticate with.
    If using `master` , enter the username you wish to authenticate with.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    `access_key`
    If using `IAM`, enter the access key you wish to authenticate with.
    If using `master` , enter the password you wish to authenticate with.
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    `region`
    Only required for `IAM`. Set to the configured OpenSearch region (example: `us-east-2`).
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    `base_url`
    Set to the domain endpoint (IPv4) specified on AWS.
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    `index`
    Enter the name of the OpenSearch index to send request.
    Only applicable on Document and Query functions.
    :::
Configure OpenSearch connection using IAM or internal user database credentials.
AWS OpenSearch Query Wizard Function
Use the query wizard to easily search documents stored in OpenSearch.
###  
Configure
See Connect to OpenSearch for details on configuration.
Then, select a `return_type` from the options below.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `search -` Returns records that match query
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `count` - Returns number of total records matching query
    :::
###  
Query
**Query Wizard**
Set filter criteria using the Xano query builder. The left input is the field to filter on. Then set the operator and value to evaluate. Optionally, add multiple conditions using AND / OR logic.
Select 'Update Payload' to ensure your changes are reflected in the query payload.
**Output Options**
These options can only be set on 'search' return type (not 'count').
Size: the number of results to return (useful for pagination)
From: the number to offset the results (useful for pagination)
Included Fields: field names to include in the results. Can be formatted as JSON array or comma separated string.
Sort: order to return results. Default is by OpenSearch relevance score. Option to choose one or more fields to sort in ascending or descending order.
**Payload (auto-generated)**
The JSON sent as the payload to OpenSearch. This is generated by the Query Wizard and Output Options sections. Useful for debugging.
Dynamic values (variables, inputs, etc.) are escaped using parentheses and use Xano expression syntax. These will be evaluated at the time of the request.
Changes made directly to the payload may be overwritten by other areas of the query wizard. If you already have a query payload you want to use, it is recommended to use the OpenSearch Request function instead.
AWS OpenSearch: Document (CRUD) Function
Easily get, add, update, or remove documents from an OpenSearch index.
###  
Configure
See Connect to OpenSearch for details on configuration.
###  
Get Document
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set method of API request to GET
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Specify doc\_id
    :::
###  
Create or Update Document
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set `method` to `POST` (create) or `PUT` (update)
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set `doc_id` (optional for POST)
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Set document payload. Click 'Use Index Schema' if you want to import the schema (mapping) directly from the OpenSearch index set under Configure tab. This will use the credentials provided to make a request to OpenSearch on your behalf to get the mapping.
    :::
###  
AWS OpenSearch Request
Send any OpenSearch API request using similar configuration methods as outlined in Connect to OpenSearch.
Set the `url` to use the desired endpoint of the request.
Set `query` to the JSON payload if necessary.
Google Cloud Storage
Manage Google Cloud Storage buckets directly in the Xano function stack.
<div>
</div>
####  
Google Service Account
You need to set up a Google Service Account in the Google Cloud Console.
Navigate to IAM & Admin and select Service Accounts.
Select **+ Create Service Account.**
####  
Roles
**Be sure to include the following Roles for the Service Account**:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `Service Account User`
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `Storage Admin`
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `Storage Object Admin`
    :::
Once the Service Account is created, select actions and **Manage keys.**
Then add a new key and select the JSON option.
Google will provide a JSON file for download. Open the file and copy the JSON key. Paste this into your Xano workspace either as an Environment Variable or as a variable in the function stack that you are using the Google Cloud Storage functions.
The JSON key must be entered as a **text string**. Do not import the key as JSON when adding it to Xano.
###  
List Directory
List the contents of a Google Cloud Storage Bucket.
**Service Account** - the JSON key, stored as text, from your Google Service Account
**Bucket** - the name of the Bucket you wish to access.
**Path** - the path you wish to see the contents of.
###  
Signed URL
Generate a signed URL to provide limited permissions. These can be used with a TTL (time to live) similar to an expiring token.
**Service Account** - the JSON key, stored as text, from your Google Service Account
**Bucket** - the name of the Bucket you wish to access.
**filePath** - the path of the file you wish to generate the URL for.
**Method** - the HTTP method (GET or POST)
**TTL** - time to live, in seconds. (How long until the URL expires).
###  
Upload a File
Upload a File to the specific Google Cloud Storage bucket.
**Service Account** - the JSON key, stored as text, from your Google Service Account
**Bucket** - the name of the Bucket you upload a file to.
**filePath** - the path and name of the file you wish to store in the bucket. For example \"files/image1\" will upload the image in the files folder and name it image1.
**File** - the file being uploaded. This should come from a file resource input or a file resource variable.
###  
Delete File
Delete a specific file from a Bucket.
**Service Account** - the JSON key, stored as text, from your Google Service Account
**Bucket** - the name of the Bucket that contains the file.
**filePath** - the path of the file you wish to delete from the Bucket.
###  
Create Variable From File Resource
Return the file resource as a variable in Xano, including the raw image. This can be used, for example, to send to another service if file transfer is needed.
**Service Account** - the JSON key, stored as text, from your Google Service Account
**Bucket** - the name of the Bucket that contains the file.
**filePath** - the path of the file you wish to create a variable of.
####  
Example - Using the Variable Created from File Resource
Turn your API endpoint into a redirect to the file by returning the data field from the return variable and setting a custom header of Content-Type with the mime of the file resource.
Here\'s an example return of Create Variable from File Resource:
If we return the raw image (data) and use a Set Header function to define `Content-Type` the mime (in this example `image/png`). We can have our endpoint URL redirect to the file.
Amazon S3
###  
Access Key and Secret Access Key
From your AWS Developer Console, navigate to **Security Credentials**.
Scroll down to **Access Keys** and select **Create access key** unless you have an access key and secret already generated.
Select **Command Line Interface (CLI)** as the use case and choose next, optionally add a description, then create the access key.
Store the **Access key** and **Secret access key** in a safe place. It\'s recommended to save these in your Xano workspace as Environment Variables as they will be used in the Amazon S3 Cloud Storage Functions.
###  
Bucket and Region
The s3 bucket name and region will also be required when calling the Amazon s3 Cloud Storage Functions.
When navigating to your s3 buckets, the bucket name can be found under name. The region is under region but only requires the identifier. For example, in the below image the bucket name is **xano-s3-test** and the region is **us-west-2**.
###  
Amazon S3: List Directory
Lists the directory details of the specific Amazon s3 bucket.
**Bucket -** The name of the s3 bucket you want to get the details of.
**Region -** The region of the bucket.
**Key -** The access key
**Secret -** The secret access key
**Next\_page\_token -** optional. The next page token is provided in the response if there is a next page, use this value to get the next page of items. S3 buckets limit 1,000 items per page.
###  
Amazon S3: Signed URL
Creates a signed URL of the file to be shared with an expiration.
**Bucket -** The name of the s3 bucket you want to get the details of.
**Region -** The region of the bucket.
**Key -** The access key
**Secret -** The secret access key
**File\_key -** The file key of the file. This can be found in the s3 bucket when selecting the file and finding Key. Additionally, the Key is listed in the payload for List Directory.
**TTL** - Time to live. How long, in seconds, the signed URL is viewable until it expires.
###  
Amazon S3: Upload a File
Upload a file to a specified Amazon S3 Bucket
**Bucket -** The name of the s3 bucket you want to get the details of.
**Region -** The region of the bucket.
**Key -** The access key
**Secret -** The secret access key
**File\_key -** Optionally define the file key. If nothing is defined, one will be automatically assigned by Amazon S3.
**File** - The file being uploaded. This must come from a file resource input or file resource variable.
###  
Amazon S3: Delete File
Delete a file from a specified S3 Bucket.
**Bucket -** The name of the s3 bucket you want to get the details of.
**Region -** The region of the bucket.
**Key -** The access key
**Secret -** The secret access key
**File\_key -** The file key of the file you wish to delete.
###  
Amazon S3: Create Var From File Resource
Return the file resource as a variable in Xano, including the raw image. This can be used, for example, to send to another service if file transfer is needed.
**Bucket -** The name of the s3 bucket you want to get the details of.
**Region -** The region of the bucket.
**Key -** The access key
**Secret -** The secret access key
**File\_key -** The file key of the file you wish to return the file resource as a variable.
The result, shown on the right-hand side of the above image returns an object with the file name, size, mime type, and raw image represented in the path data.
Check out the example above to return the image through an API request.
Microsoft Azure Blob Storage
Manage storage containers from your Microsoft Azure account directly from the Xano function stack.
###  
Setup
Please ensure you have a Microsoft Azure account. If you don\'t yet have an account sign up to Microsoft Azure and navigate to the Azure portal.
####  
Create a storage account
A storage account is required to store files on Azure. First, select **Create a resource** from the portal homepage.
Select Create a resource from the portal home page.
Navigate to storage and select **Create** under storage account.
Create a storage account.
Fill out the required information in **Basics**, if you don\'t already have a resource group, create a new one.
Create a storage account.
Configure any additional settings and create the storage account once you\'re ready.
####  
Create a container
Once the resource is deployed, navigate to containers and create a new container.
Create a new container.
####  
Access key
After creating a container, you need to retrieve your account access key to use the Azure functions in Xano.
Find **Access keys** under **Security + Networking** on the left navigation bar. Select **Show** next to **Key** under **key1**. Copy the key and store it as an Environment Variable in Xano.
Locate your Azure Access Key.
Do not share your access key. It is recommended to store your access key as an Environment Variable in Xano for safe keeping.
###  
List Directory
List directory will list the blobs, properties, and metadata in a container or at a specified path within the container.
List the Azure Directory.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_name - Azure storage account name.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_key - Azure Access Key.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    conatiner\_name - Container name within Azure storage account.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    path - (Optional) Use this to specify a specific blob or folder within a container.
    :::
###  
Signed URL
Creates a signed URL for a file with a specified time to live (TTL) or expiration.
Create a signed URL for an Azure blob.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_name - Azure storage account name.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_key - Azure Access Key.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    conatiner\_name - Container name within Azure storage account.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    path - The path of the file to create a signed URL for.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    ttl - Time to Live (in seconds); how long the signed URL is accessible.
    :::
###  
Upload a File
Upload a file to an Azure blob container.
Upload a file to an Azure blob container.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_name - Azure storage account name.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_key - Azure Access Key.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    conatiner\_name - Container name within Azure storage account.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    filePath - The path name for the file being uploaded.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    file - The file being uploaded. This must come from a file resource.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    metadata - (Optional). Optionally include additional metadata with the file stored in object format.
    :::
###  
Delete a File
Delete a file from an Azure blob container.
Delete a file from an Azure blob container.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_name - Azure storage account name.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_key - Azure Access Key.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    conatiner\_name - Container name within Azure storage account.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    filePath - The path name for the file being deleted.
    :::
###  
Create Variable From File Resource
Create a variable from a file resource in Azure to use it in the Xano Function Stack.
Create Variable From File Resource.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_name - Azure storage account name.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_key - Azure Access Key.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    conatiner\_name - Container name within Azure storage account.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    filePath - The path name for the file being created as a variable.
    :::
Check out the example above of leveraging the Variable from File Resource in the Function Stack.
###  
Get File Metadata
Get the metadata of a file from an Azure blob container.
Retrieve the metadata from a Azure storage blob.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_name - Azure storage account name.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    account\_key - Azure Access Key.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    conatiner\_name - Container name within Azure storage account.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    filePath - The path name for the file to retrieve the metadata from.
    :::
Last updated 6 months ago
Was this helpful?