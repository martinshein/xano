---
category: functions
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Create a new API endpoint with a POST method
---

# Create a new API endpoint with a POST method

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
description: Webhooks are specialized API endpoints designed to be triggered based on other events
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: webhooks
twitter:card: summary\_large\_image
twitter:description: Webhooks are specialized API endpoints designed to be triggered based on other events
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Webhooks \| Xano Documentation'
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
    Building Webhooks
Was this helpful?
Copy
1.  Building Backend Features
Webhooks 
========
Webhooks are specialized API endpoints designed to be triggered based on other events
Quick Summary
Webhooks are API endpoints specifically designed for one system to **automatically push** information to another when a specific **event** happens. For example, Slack provides you with a webhook URL. This URL is ready and listening, much like your own API endpoint.
But here's the key difference:
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Something like a **form submission endpoint** receives data because the *user initiated* the request (e.g., they clicked \'Submit\').
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    The **Slack webhook** receives data because *your server*, after processing the form (the **event**), *initiated* a new request, automatically pushing the form details *to* Slack\'s URL. Slack didn\'t ask for it; your system sent it because something happened.
    :::
You\'d build webhooks in Xano typically to ingest information ***pushed*** from other places --- like if a user pays for something via Stripe, or they perform an action in your app that you want to log.
<div>
</div>
Building Webhooks
<div>
1
###  
Create a new API endpoint with a POST method
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click [ + Add API Endpoint ] from inside one of your API groups.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Choose **Custom API Endpoint** and fill in the details. Make sure to select **POST** as the verb.
    []
    :::
2
###  
Add a Get All Raw Input function
Typically, webhooks need to be able to dynamically process data that might look a little different between requests. So, we use Get All Raw Input to make sure that we aren\'t confined to just the inputs that are defined in the inputs section.
You\'ll need to choose the encoding, or the format, of the data being sent to this endpoint. This will more often than not be JSON.
While Get All Raw Input offers flexibility, always check the documentation of the service *sending* the webhook. They will specify the structure (schema) of the data payload you should expect.
3
###  
Process the output of Get All Raw Input as needed
From here, the process is completely unique to whatever data is being sent to the webhook, and what you need to do with it.
**Examples:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Store the data in a database table using Add Record
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    If the webhook is receiving a list of items, loop against them using For Each Loop
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Transform or manipulate the data using Filters or an Expression
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Send the data to another service, such as an analytics platform, using an External API Request
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Begin a more in-depth process using a combination of the above to perform multiple actions, such as transforming data, storing it, and sending Emails
    :::
</div>
Securing your Webhooks
Just like any other API endpoint you\'re building, it\'s important to ensure that they are built securely. Webhooks have some more specific-to-them ways that they are usually kept locked up.
<div>
1
###  
Signature Verification (recommended)
The service you\'re accepting requests from may offer signature verification. At a high level, this means that you would cross-check the signature they sent with your own calculated signature, using a private key that only you and the service are aware of, and ensure that they match.
**If they match**: The request is verified and you can proceed.
**If they don\'t match**: you should deny the request
In general, this process follows a typical flow:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Extract the signature provided in the request headers
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Ensure you have a raw, unaltered copy of the request body (which you do using Get All Raw Input)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Use the proper Security filter (such as hmac\_sha256 / hmac384 / hmac512) to encode your own signature, and ensure that it matches with the one you extracted from the request.
    :::
2
###  
Check a static token provided in the headers
Similar to how standard User Authentication & User Data works, some services may just send an API key or bearer token as part of the request header. You\'ll want to compare this against your own stored key and ensure that they match.
It\'s also good practice to rotate this token on a regular basis to ensure that it is not compromised.
</div>
Tip
Use Middleware or Custom Functions to build your webhook verification and quickly deploy it across multiple function stacks.
Last updated 3 months ago
Was this helpful?