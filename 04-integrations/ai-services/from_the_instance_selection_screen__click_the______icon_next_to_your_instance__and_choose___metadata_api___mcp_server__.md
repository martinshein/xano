---
category: ai-services
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: "From the Instance selection screen, click the [\u2699\uFE0F] icon next to\
  \ your instance, and choose [ Metadata API & MCP Server ]"
---

# From the Instance selection screen, click the [⚙️] icon next to your instance, and choose [ Metadata API & MCP Server ]

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
description: Manage your Xano data using your favorite MCP client
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'xano-mcp-server'
twitter:card: summary\_large\_image
twitter:description: Manage your Xano data using your favorite MCP client
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Xano MCP Server \| Xano Documentation'
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
    What is the Xano MCP Server?
Was this helpful?
Copy
1.  Build For AI
Xano MCP Server 
===============
Manage your Xano data using your favorite MCP client
Need a primer on MCP? Read this first: Introduction to building MCP Servers in Xano
Quick Summary
The Xano MCP Server allows you to interact with your Xano instance and workspaces using MCP. This enables you to do things like\...
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Create database tables and update table schema
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Generate sample data
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Parse and search your request history
    :::
\...all from your favorite MCP client, such as Claude, Cursor, or Windsurf.
The Xano MCP Server is powered by our Metadata API, and we expect to eventually allow for all of the methods present there to be used as tools within the Xano MCP Server.
Connect to the Xano MCP Server from your instance settings -\> **Metadata API & MCP Server**
What is the Xano MCP Server?
The Xano MCP Server, powered by our Metadata API, enables you to interact with your Xano instance and workspaces without leaving your favorite MCP client.
Connecting to the Xano MCP Server
<div>
1
###  
From the Instance selection screen, click the [⚙️] icon next to your instance, and choose [ Metadata API & MCP Server ]
2
###  
Generate an Access Token
Access Tokens are used for authentication when connecting to the Xano MCP server. For more information on generating access tokens, see this reference: Generate an Access Token
3
###  
Choose your connection method
For most clients, at this time, SSE is likely the method that you\'ll want to choose. However, we have made a streaming connection available as well. Click the URL to copy it to your clipboard.
4
###  
Connect using your client of choice
For more information on connecting your clients to an MCP server, refer to Connecting Clients or to your client\'s documentation for the most up to date information.
The instructions linked above are for connecting an MCP server built using Xano\'s MCP builder, but are fundamentally the same for the Xano MCP Server --- just replace the URL with what you copied in step 3.
</div>
Available Tools
###  
User Authentication
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getLoggedInUser** - Validates the provided Access Token and returns the associated account details.
    :::
###  
Workspace Management
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **listWorkspaces** - Lists all workspaces accessible by the authenticated user.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getWorkspace** - Retrieves detailed information about a specific workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getWorkspaceBranches** - Lists all branches (e.g., development, production) within the specified workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **workspaceGetDataSources** - Lists all external data sources connected to the specified workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **workspaceRealtimeDetails** - Retrieves Realtime information for the specified workspace.
    :::
###  
Table Management
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **addTable** - Creates a new table within the specified workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getTables** - Lists all tables within a specific workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getTable** - Retrieves the details of a specific table within the workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **deleteTable** - Deletes a specific table and all data it contains from the workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **updateTableMeta** - Modifies the metadata (e.g., schema, field definitions, descriptions) of the specified table.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **updateTableSecurity** - Updates the security rules for the specified table.
    :::
###  
Table Content Management
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getTableContent** - Retrieves a list of records from the specified table.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getTableContentItem** - Retrieves a single, specific record from the table using its ID.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **updateTableContentItem** - Updates an existing record in the table using its ID.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **deleteTableContentItem** - Deletes a single, specific record from the table using its ID.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **searchTableContent** - Searches for records within the table using complex filter criteria and sorting options.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **patchTableContentBySearch** - Updates fields of all records in the table that match the specified search criteria.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **deleteTableContentBySearch** - Deletes all records from the table that match the specified search criteria.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **addTableContentBulk** - Adds multiple new records to the table in a single operation.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **patchTableContentBulk** - Updates multiple existing records in the table in a single bulk operation.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **deleteTableContentBulk** - Deletes multiple records from the table in bulk, based on a list of record IDs.
    :::
###  
API Management
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **listAPIGroups** - Lists all API groups within the specified workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getApiGroup** - Retrieves details for a specific API group within the workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **listAPIs** - Lists all individual API endpoints defined within a specific API group.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getApiGroupSwagger** - Returns the JSON version of the Swagger (OpenAPI Documentation) for a specific API group
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getApiSwagger** - Returns the JSON version of the Swagger (OpenAPI Documentation) for a specific API
    :::
###  
Request Management
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **getRequestHistory** - Lists the history of API requests made to the specified workspace.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **searchRequestHistory** - Performs an advanced search of the workspace\'s API request history using filters and sorting.
    :::
Last updated 2 months ago
Was this helpful?