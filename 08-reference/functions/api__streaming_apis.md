---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'API: Streaming Apis'
---

# API: Streaming Apis

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'streaming-apis'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Streaming APIs \| Xano Documentation'
viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---
[](../index.html)
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
    Streaming API Request
Was this helpful?
Copy
1.  Build With AI
Streaming APIs 
==============
###  
Streaming API Request
<div>
</div>
You can use the Streaming External API Request endpoint to call an API that returns a stream in almost exactly the same way as you call normal APIs from your function stacks. The only difference is the structure of data returned, which would typically be an array of items that you would leverage a For Each loop to work with.
###  
Streaming API Response
When delivering certain types of API responses, you may want to \'stream\' this response (similar to your favorite AI-powered chatbots). In Xano, this is possible with a simple combination of a For Each loop and a Streaming API Response function.
<div>
</div>
We\'ll be using a poem in the public domain to demonstrate the streaming response. You can copy the sample below and use it in your own function stacks to test.
Copy
``` 
["Two roads diverged in a yellow wood,","And sorry I could not travel both","And be one traveler, long I stood","And looked down one as far as I could","To where it bent in the undergrowth;","","Then took the other, as just as fair,","And having perhaps the better claim,","Because it was grassy and wanted wear;","Though as for that the passing there","Had worn them really about the same,","","And both that morning equally lay","In leaves no step had trodden black.","Oh, I kept the first for another day!","Yet knowing how way leads on to way,","I doubted if I should ever come back.","","I shall be telling this with a sigh","Somewhere ages and ages hence:","Two roads diverged in a wood, and I—","I took the one less traveled by,","And that has made all the difference."]
```
Data that you use for a streaming response needs to be separated into logical pieces. In this example, each item in the array is a new line in the poem. It would typically make the most sense to build a streaming response against an array just for ease of implementation.
###  
Setting up a streaming response
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Set the API response type to \'streaming\' from the API settings, or choose the streaming option when creating a new API endpoint.
    []
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    In your function stack, once you have the data you want to stream ready to go, use a For Each loop to start looping against each item in your array.
    []
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Inside of the loop, use a **Streaming API Response** function to deliver each item inside of the array as the loop iterates through it.
    []
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You can now test your streaming API, and should see each item in the array streamed as part of the response.
    :::
Please note that your front-end must support streaming responses. If it does not, the response can still be delivered traditionally.
Using Run & Debug will not display a stream, and only the entire response once the stream has completed.
###  
Testing your Streaming Response
####  
Testing in Postman
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Create a new request with type HTTP
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Paste your API endpoint URL in the URL input, and click Send.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You will see your API response delivered in the result panel.
    :::
####  
Testing in Insomnia
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Create a new request with type Event Stream
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Paste your API endpoint URL in the URL input, and click Connect
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You will see your API response delivered in the result panel.
    :::
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
["Two roads diverged in a yellow wood,","And sorry I could not travel both","And be one traveler, long I stood","And looked down one as far as I could","To where it bent in the undergrowth;","","Then took the other, as just as fair,","And having perhaps the better claim,","Because it was grassy and wanted wear;","Though as for that the passing there","Had worn them really about the same,","","And both that morning equally lay","In leaves no step had trodden black.","Oh, I kept the first for another day!","Yet knowing how way leads on to way,","I doubted if I should ever come back.","","I shall be telling this with a sigh","Somewhere ages and ages hence:","Two roads diverged in a wood, and I—","I took the one less traveled by,","And that has made all the difference."]

```

