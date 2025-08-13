---
category: expressions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Inheriting Settings
---

# Inheriting Settings

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
description: An explanation of all available workspace settings
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'workspace-settings'
twitter:card: summary\_large\_image
twitter:description: An explanation of all available workspace settings
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Workspace Settings \| Xano Documentation'
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
    General Settings
Was this helpful?
Copy
1.  Xano Features
Workspace Settings 
==================
An explanation of all available workspace settings
Before you begin
Please note that this page provides only a general overview of some settings. When relevant, each section will contain a link to that feature specific documentation, which is recommended reading before adjusting anything
General Settings
> This panel is accessible by heading to your workspace dashboard and clicking the ⋮ icon \> Settings
Setting
Purpose
Name[\*]
^text^
Give your workspace a unique name
Description
^text^
A description of your workspace
Use Internal Documentation Tool ^checkbox^
Enables the Internal Documentation Tool for your function stacks\--a plain text input typically used to house information such as example inputs
Show Start
Enables the Start Page, which offers beginner guidance on working in Xano
Show Marketplace
Enables the Marketplace, which contains snippets and extensions available for import into your Xano workspace
AI Preferences
Accept AI specific license terms to use certain AI-powered features, such as our AI Database Assistant
Data Sources
> Data Sources allow you to maintain separate databases with the same schema. Useful for maintaining things like separate production and testing data sets.
Setting
Purpose
Manage
Quick access to managing your data sources, such as browsing or adding new ones
Migrate
Allows you to migrate data from one data source to another
Branch Defaults
> These are default settings related to what is logged in your Request History
In your workspace settings, you can manage the request history for your entire workspace in the Branch Defaults panel.
From this panel, we can define the request history defaults for each object type (query, function, task, middleware, trigger) that maintains history.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Enable / Disable** - Performs the selected action on the object type
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Function Statement Limit** - The number of statements to record for each object type. You can choose between:
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        No statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        100 statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        1,000 statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        10,000 statements
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Store all statements
        :::
    :::
Please note that request history utilizes your Database (SSD) storage. It is important to consider this when determining how many statements can be stored, or if they need to be stored at all.
####  
Inheriting Settings
In each individual API, function, task, middleware, or trigger\'s settings, you can also control the request history for that object specifically.
By default, these will be set to **inherit**, which means it will obey the branch defaults. Otherwise, you can adjust this for specific objects as necessary.
Middleware
> Provides quick access to Middleware settings
Clone Workspace
> Creates a clone of your workspace
Cloning a workspace will copy all database table schema, API groups, APIs, functions, addons, and tasks into another workspace. It will **not** copy the database table records.
Export Workspace
> Exports a copy of your workspace
Exporting your data is done in the background and may take a significant amount of time to process depending on the amount of data in your workspace.
You may also include media attachments, but this may increase the export size and time significantly depending on the number of files.
**Once the export is complete, you will receive an email notification as well as a notification in Xano that your data is ready to be downloaded. This export will be available for 12 hours.**
Xano Link
> Xano Link is a premium addon for syncing branches and database schema from one workspace to others.
Triggers
> Triggers allow you to build workflows that run based on when certain events happen, such as when a database record is added or when certain branch actions take place.
Statement Explorer
> The Statement Explorer allows you to search for instances of specific statements across your workspace, such as finding all Query All Records functions. This is useful for things like security audits and making sweeping changes or improvements across multiple workflows.
Realtime Settings
> Access your Realtime in Xano settings from here
Reset Drafts
> Resets all drafts in the current workspace
Sometimes, you may want to clear out all drafts and revert fully back to published versions of your function stacks. This option allows you to quickly do so. It can also be useful in the rare circumstance that you have functions that are in draft state or have been recently published and are not behaving correctly.
This action is **not reversible**, so if you have questions, reach out to our support chat before proceeding.
Compliance Center
> Offers quick access to the Compliance Center, which is a premium feature that enables advanced auditing of the state of your workspace and actions of your team members
Table Format
Table Formats - Only relevant for direct database connections
As of our **1.68 release (5/27/25)**, all new workspaces will default to the standard SQL column format for tables. For all workspaces created prior to that, read below.
Your tables can be created using one of two formats:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **JSONB format**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        This creates your tables with two columns:
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            `id` - the ID of the record
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            `jsonb` - contains a JSON representation of the entire record
            :::
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Standard SQL format**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        This creates a more standard table layout. Instead of a jsonb column, each column is written separately.
        :::
    :::
If you are using the Direct Database Connector, Standard SQL format is usually recommended.
###  
**When to Convert to Standard SQL Format:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You need direct database connections with third-party tools that aren\'t friendly to JSONB format, such as Tableau or PowerBI
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You want faster performance for non-indexed queries
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You\'re frequently adding new fields (faster column additions)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You plan to use SQL analytics tools or run complex reports directly against your database
    :::
###  
**When to Keep JSONB Format:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You\'re satisfied with current performance
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You don\'t need direct database connections
    :::
###  
Converting Tables from JSONB to standard SQL
This change is **permanent**. Most users will not need to adjust these settings, and they only impact your experience if you are connecting to your database directly via third-party tools.
Using standard SQL does not mean you can\'t use JSONB --- you have the ability to mix and match table types, if you prefer. You can also still use JSON fields on any table type for more complex, dynamic field structure.
<div>
1
###  
From your workspace dashboard, click the settings icon in the upper-right corner, and click Settings.
2
###  
Scroll down to the Database Preferences section, and check the option to \'Use standard SQL columns for new tables\'
This setting must be enabled before you can convert existing tables to the new format.
3
###  
Convert your table(s) from your workspace settings, or the settings of any table.
From the migration panel, select any of the tables you\'d like to convert, and confirm your choices. The migration will begin immediately.
</div>
Custom SQL Table Names
From your Workspace settings, you can enable **Custom SQL Table Names**.
By default, Xano assigns each table a SQL name in the format mvpw\_ (e.g., mvpw1\_3). This identifier works for direct access, but can be difficult to read or use with direct queries and database tools.
You can replace this with a custom SQL name to make queries more intuitive and improve compatibility with external connectors.
If you change a table\'s SQL name, be sure to update any queries that reference the old name to avoid breaking functionality.
Once you\'ve enabled **Custom SQL Table Names**, head to any database table\'s settings, and click Manage next to SQL Table Name.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Leave the SQL Table Name field blank to use Xano's default SQL table name, which follows the format mvpw\<workspaceID\>\_\<tableID\> (e.g., mvpw1\_3).
    :::
```
<!-- -->
```
-   ::: 
    ::: 
    :::
    :::
    ::: 
    SQL table names must be globally unique across all workspaces.
    **Hint**: Use the Custom Prefix to ensure uniqueness across workspaces.
    :::
```
<!-- -->
```
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Datasources automatically add a suffix based on their environment. For example, **users** becomes **users\_test** in the test datasource.
    :::
```
<!-- -->
```
-   ::: 
    ::: 
    :::
    :::
    ::: 
    To reuse the same base name across workspaces, use a workspace-specific prefix (e.g., projA\_users, projB\_users).
    :::
Last updated 2 months ago
Was this helpful?

## Code Examples

```

<!-- -->

```

```

<!-- -->

```

```

<!-- -->

```

