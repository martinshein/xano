---
category: custom-functions
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Database Triggers
---

# Database Triggers

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
    What are triggers?
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Building with Visual Development
Triggers 
========
**Quick Summary**
Triggers are workflows that can run based on other events that happen in your workspace. Xano offers triggers for:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Database operations (adds, edits, deletes)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Realtime events
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Workspace events (currently limited to branching operations)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    MCP Server connections
    :::
Triggers are available on our **Starter plan** and higher.
What are triggers?
Triggers in Xano are workflows that will run only when triggered by another event. You can build triggers for the following events.
Event Type
Event
**Database**
New records
Record edits
Record deletes
Table truncate (deleting all records)
**Realtime**
Channel events
**Workspace**
New branch
Branch merge
Live branch change
**MCP Server**
Client Connect
Accessing and Creating Triggers
<div>
1
###  
Database Triggers
You can find database triggers on each table by clicking the settings icon in the top-right corner.
Click [ + Add Database Trigger ] to create a new database trigger.
You can specify what Data Sources the trigger will execute on. If no data source is set, then it will execute on all data sources.
Select the **actions** that will activate this trigger.
**Inserts**
Any time a record is added to the table
**Updates**
Any time a record is edited
**Deletes**
Any time a record is deleted
**Truncates**
When the content of the database table is cleared
Finally, you can set up custom filters so that the trigger only runs if the record matches certain conditions. For example, if you only want the trigger to run if a new order is created for a user, or a new user is created with a certain role.
------------------------------------------------------------------------
Database triggers have predefined inputs that contain all of the information you\'ll need to build a workflow based on the database event.
`new`
This is the contents of the new record --- if you\'re adding a record, this will contain the contents of the new record, and if you\'re updating a record, this will contain the contents of the updated record. On deletes and truncates, this will be empty.
`old`
This is the contents of the old record --- if you\'re deleting or editing a record, this will contain the contents of the record before the change. On inserts and truncates, this will be empty.
`action`
The action that activated the trigger. Valid options are `insert` `update` `delete` `truncate`
`data source`
The datasource this trigger has been executed against
------------------------------------------------------------------------
2
###  
Realtime Triggers
Realtime triggers are created for each channel. Once you\'ve created a realtime channel, click the [ + Add Channel Trigger ] button to create a new channel trigger.
Select the **actions** that will activate the trigger.
**Message**
Any time a new message is sent to the channel
**Join**
Any time a new connection is made to the channel
------------------------------------------------------------------------
Realtime triggers have predefined inputs that contain all of the information you\'ll need to build a workflow based on the realtime event.
`Action` and ~~**Command**~~
This will be either \'join\' or \'message\' depending on what was responsible for executing the trigger.
***Action*** *and* ***Command*** *currently have the same values, but behind the scenes, the values do not come from the same source. We maintain two separate inputs for the purpose of expanding this functionality in the future.*
`Channel`
The channel that this command or message is being sent to
`commandOptions`
Any options that are provided with the command being sent to the channel
`payload`
The contents of the command, such as the message body
`client`
An internal client ID
------------------------------------------------------------------------
3
###  
Workspace Triggers
Workspace triggers can be created to execute workflows based on certain workspace-wide events. Currently, these are limited to branch changes.
You can find workspace triggers by clicking the settings icon in the top-right corner of your workspace dashboard.
Click [ + Add Workspace Trigger ] to create a new workspace trigger.
Select the **action(s)** that will execute this trigger.
**Branch Live**
Any time a branch status is set to live
**Branch Merge**
When a branch is merged
**Branch New**
When a new branch is created
4
###  
MCP Triggers
MCP triggers can be created to run any time a client connects to the MCP server. This is useful for functions like:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Logging connections to the MCP server
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Dynamically adjusting server instructions based on other data, such as the user who is connecting
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Restricting tools per connection
    :::
You can find MCP triggers by clicking the settings icon in the top-right corner of your MCP server.
Click [ + Add MCP Server Trigger ] to create a new MCP server trigger.
MCP Server triggers offer the following inputs:
`toolset`
Contains the server information, such as the name and instructions.
`tools[]`
An array that contains each tool.
5
###  
AI Agent Triggers
Agent triggers are similar to MCP triggers. They can be used when an agent is called to perform tasks such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Logging connections
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Dynamically adjusting available functions and tools
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Adjusting the system prompt based on user or other data
    :::
You can find Agent Triggers in the settings for your Agent.
`toolset`
Contains the server information, such as the name and instructions.
`tools[]`
An array that contains each tool.
</div>
Last updated 5 days ago
Was this helpful?