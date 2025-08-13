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
title: 'API: External Api Request'
---

# API: External Api Request

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
    What is an external API request?
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Functions
3.  APIs & Lambdas
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
Click [] from the panel that opens.
3
###  
Tell the AI Assistant about the API you want to access, and any specifics about the request you want to make.
4
###  
You can either choose to apply the AI\'s suggestion, or continue to converse with the AI to iterate or make changes.
5
###  
For things like API keys, you can either pass them to the AI or fill them in manually after you\'ve applied the suggestion.[]
</div>
3
###  
Or, build the request manually or with a cURL command
You can copy cURL commands from API documentation, and paste them using []. Xano will build the request for you.
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
[]
headers
Any headers you need to send with the request, such as authentication.
Add headers by hovering over the value space and click [**push**
]
[][
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
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    What URL you\'ll be calling
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    What parameters or data you need to send
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    What the response will look like
    :::
Most API documentation also includes **cURL commands**, which you can copy and paste right into Xano by clicking []on the External API Request function panel. This is the optimal way to create external API request in Xano, as it ensures consistency with what the API requires and is much faster.
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
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Development and Testing Environments**: When working with development servers that use self-signed certificates or have hostnames that don\'t match their certificates
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Internal Services with Misconfigured Certificates**: In corporate environments where internal services may have certificates that don\'t exactly match the hostnames used to access them, especially in legacy systems.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Troubleshooting SSL Issues**: To isolate whether hostname verification is causing connection problems when debugging API connectivity issues.
    :::
###  
Peer Verification
Secure certificates are usually issued by certain trusted authorities, such as LetsEncrypt. Peer Verification enables checking whether or not the certificate is issued by one of these known trusted authorities, validating its authenticity.
This value can be `true` or `false`
**Recommended Setting:** `true`
You might want to set this to false if the server you\'re sending the request to falls under one of the scenarios outlined above under **Host Verification**.
###  
SSL Authentication
This is a set of additional options you can use to validate the security of the request being made. The provider of the service you\'re calling should be able to provide these for you, if necessary.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `certificate`: The content of the client certificate file. Usually, you\'d be provided with a .crt or a .pem file --- just open it up in your text editor of choice and paste the contents here.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `certificate_pass`: Password for the certificate if it\'s password-protected
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `private_key`: The contents of the private key file. Usually, you\'d be provided with a .pem file for this --- just open it up in your text editor of choice and paste the contents here.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `private_key_pass`: Password for the private key if it\'s password-protected
    :::
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

## Code Examples

```
 
-----BEGIN CERTIFICATE-----
MIIDITCCAgmgAwIBAgIUJqrGM2rS34H8YryJJLAMarvab8AwDQYJKoZIhvcNAQEL
BQAwIDEeMBwGA1UEAwwVbXlDdXN0b21DZXJ0aWZpY2F0ZUNKX...
-----END CERTIFICATE-----

```

