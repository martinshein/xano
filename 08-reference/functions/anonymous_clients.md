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
title: Anonymous Clients
---

# Anonymous Clients

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'channel-permissions'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Channel Permissions \| Xano Documentation'
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
    Permissions
Was this helpful?
Copy
1.  Realtime
Channel Permissions 
===================
Channels are opened with your front-end\'s implementation of Realtime.
Copy
``` 
const marvelChannel = this.xanoClient.channel("marvel-chat-room");
```
Each channel needs to have permissions defined to ensure that they behave in the way that you expect and remain secure. On this page, we\'ll go over the various permission settings available and show you how to apply them.
Securing your Realtime channels is a multi-step process, and is not always solely reliant on the channel permissions you set. This includes:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Setting the proper channel permissions for your use case
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Using nested channels to separate data
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Using Realtime Triggers to act as a primary or secondary measure to block messages from being sent to the channel
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Generating separate authentication tokens for connecting to the realtime server
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Obfuscating the implementation on your front-end, and ensuring that channel creation is handled properly
    :::
Permissions
###  
Anonymous Clients
Anonymous Clients means that you allow unauthenticated users to connect to your channels, but they can not send messages.
###  
Presence
Every client connected to this channel will receive a the list of all the other clients (including yourself). Note that authenticated client details will be augmented with the extra information stored in their JWT token.
###  
Client Public Messaging
This option allows authenticated and unauthenticated clients to send messages to the channel. These messages will be sent to all the users connected to the channel.
###  
Authenticated Only (Client Public Messaging)
Similar to Client Public Messaging, this permission allows only authenticated users to send messages to the channel. Unauthenticated clients can still see the messages being sent to the channel.
###  
Client Authenticated Messaging
Every message sent to the channel by authenticated clients will only broadcasted to all other authenticated clients. This means that anyone can connect to that channel, but only authenticated client will receive messages broadcasted by the channel. Anonymous client will not receive any messages.
###  
Client Private Messaging
This enables clients to send messages directly to other clients without requiring authentication as long as both clients are present in the channel.
###  
Authenticated Only (Client Private Messaging)
This permission enables client private messaging only between authenticated clients. Unauthenticated clients can not send private messages.
It\'s important to note that some of these permissions may appear to have logical dependencies, but they do not. For example, if you enable **Client Public Messaging**, this implies that **Anonymous Clients** is also enabled.
Applying Permissions
From the Realtime Settings panel, click the icon shown below to define channel permissions.
On the next panel that opens, fill in the options shown.
####  
Channel Status
Defines whether or not these channel permissions are utilized
####  
Channel Target
This is essentially the name of the channel you are creating permissions for. Channel names can be dynamic to support creation of new channels from your front-end by enabling the **nested channels** option. Using nested channels along with a name like \"chatroom/\*\" will allow you to create channels that begin with \"chatroom/\" and anything else afterwards, such as a unique channel identifier. If you do not enable nested channels, the permissions will just apply to the channel name you specify.
####  
Description
Give your permission layout a description for organizational purposes, if you wish.
####  
Permissions
Using the list of permissions on this page, determine the correct set of permissions to apply to any channels that match the name pattern.
**Channel Triggers**
Triggers are function stacks that can run when messages or events are sent to the channel(s) impacted by these permissions. You need to first save your changes to enable adding triggers when creating new permissions.
For more information about Realtime Triggers, see this section of our documentation.
Permission Examples
Please note that **Presence** is usually optional no matter the scenario and is just based on if you want to utilize presence updates in your realtime channels.
Context
Permissions
A chat application where users can both connect and send messages anonymously
[]
A chat application where users can connect anonymously, but authentication is required to send messages
[]
A notification system that allows for unauthenticated users to connect so they can receive notifications, but sending messages is not allowed. You would send notifications to this type of channel through the [Realtime Event] function.
[]
A chat application that only allows authenticated users to connect and send messages
[]
A chat application that only allows authenticated users to connect, and allows direct client-client private messaging for authenticated users
[]
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
const marvelChannel = this.xanoClient.channel("marvel-chat-room");

```

