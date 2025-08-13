---
category: database
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- CRUD
title: Head to the database
---

# Head to the database

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'using-the-xano-database'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Using the Xano Database \| Xano Documentation'
viewport: 'width=device-width, initial-scale=1, maximum-scale=1'
---
[](../../index.html)
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
     Create a Database Table
Was this helpful?
Copy
1.  The Database
2.  Database Basics
Using the Xano Database 
=======================
**Hint**
Use the [✨]**AI Database Assistant** to create and update tables for you!
[👨‍🏭] Create a Database Table
<div>
1
###  
Head to the database
Click []in the left hand menu.
2
###  
Add a new table
Click []in the top right corner.
Choose **Import Data** to import data from a CSV file, or **Enter Data Manually** to start with an empty table where you can add your own data later, or generate sample data automatically.
If you\'re just starting out, we\'d recommend choosing **Enter Data Manually** and using the sample data generator. You can always import data later.
In the panel that opens, give your table a name and a description
3
###  
Give your table a name and a description.
When naming your table, it\'s considered best practice to use camelCase for multiple words, and to not use plurals in the table name. For example, a table of dog breeds would be named `dogBreed`
The description is just for you to make notes on what this table will contain, notable data constraints, or any other information you\'d like to store.
4
###  
Choose your primary key type.
The primary key is the ID of each record. Xano offers two types of primary keys to choose from.
When should you use Sequential, and when should you use UUID?
When designing your database structure in Xano, choosing the right identifier type is an important decision. Here\'s a straightforward guide to help you decide:
**Sequential IDs are best for:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Performance-sensitive operations - they\'re faster to index and query
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Human-friendly references - easier to communicate (\"Please check record \#42\")
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Storage efficiency - they consume less space in your database
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    When chronological order matters - the sequence reveals creation order
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Single-database applications where centralized ID generation works well
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Systems that benefit from predictable numbering patterns
    :::
**Common use cases:** Customer IDs, order numbers, ticket systems, invoice numbers, internal record tracking
**UUIDs are best for:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Distributed systems where multiple services create records independently
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Data synchronization across different databases or systems
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Preventing ID guessing or enumeration attacks
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Frontend-first workflows where IDs need to be generated before server contact
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Multi-region deployments with separate databases
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    When you don\'t want to expose information about record counts
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Scenarios where data privacy is paramount
    :::
**Common use cases:** User accounts in modern applications, cross-system record tracking, session management, event logging in distributed architectures
Please note that there is **no support** for converting tables to / from different primary key types. However, this can be done with a manual migration to a new table.
Sequential (1, 2, 3\...)
A sequential identifier is just a sequence of whole numbers (1, 2, 3, etc\...).
Think of sequential IDs like numbered tickets at a deli counter. They start at 1 and count up one by one (2, 3, 4\...). Just like how the first customer gets ticket \#1, the first row in your database gets ID \#1. This system is straightforward but requires coordination - just as you can\'t have two deli counters giving out the same numbers (it would confuse customers), you need to ensure you\'re not creating duplicate IDs across different parts of your system.
UUID
A UUID is like the serial number on your electronics - something like \"550e8400-e29b-41d4-a716-446655440000\". It\'s longer and looks random, similar to how no two iPhone serial numbers are alike, even if they were made in different factories. This makes UUIDs particularly useful when you have data coming from multiple sources or need to merge databases - you don\'t have to worry about ID conflicts, just like how Apple doesn\'t need to check with Samsung about what serial numbers they\'re using.
Some users feel that using UUIDs is also more secure. UUIDs do provide some security benefits through obscurity - you can\'t easily guess other valid IDs by simply incrementing a number. If a website shows you order \#1234, you might guess that order \#1235 exists. But if you see order 550e8400-e29b-41d4-a716-446655440000, you can\'t easily guess other valid orders.
However, it\'s crucial to understand that using UUIDs is not a replacement for proper security measures. You should never rely on the difficulty of guessing IDs as your only security mechanism. Proper authentication and authorization should be in place regardless of ID type.
5
###  
Add some tags.
Tags in Xano can be applied to any object (tables, APIs, functions, etc\...) and are used to easily find related objects when searching your workspace.
6
###  
Choose to add basic CRUD endpoints.
Xano can provide you with some standard pre-built APIs for basic operations against this table. If you choose this option, you\'ll also want to supply an **API Group** for those endpoints to live in. You can always choose to generate these endpoints later, too.
7
###  
Confirm your choices.
Once you\'ve confirmed all of your settings are as you want them to be, click **Add Table**.
</div>
------------------------------------------------------------------------
[ℹ️] Navigating the Table View
Let\'s start with the top control bar.
[🧭] Navigation Controls
[]Table name, ID, description, and tags
[] Go back to your list of database tables.
[] Refresh the list of records
[] Change the database view
[🔎] Searching, Filtering, and Sorting
[] Search for specific records
[] Filter your records by certain conditions, such as \"all records with an ID greater than 100\"
[] Sort your database records
[] Hide database fields from view
[🧰] Tools and Advanced Controls
[] Cut, Copy, Paste, Undo, and Redo
[] Show Schema
[] Show References
[] Indexes
[] Review available keyboard shortcuts for the database view
Just below the control bar, you\'ll see your database records.
Use your mouse or arrow keys to navigate between records and individual cells.
To modify data, just select the cell and make your desired changes. They will be saved automatically.
[] Select one or more records by checking these boxes
[] Open a card view of the selected record
[] Add a new field
------------------------------------------------------------------------
[➕] Adding a new field
When Working in Large Tables
Making changes to your schema, such as renaming or adding fields in a extremely large table requires significant server resources. Please contact support if you encounter any issues.
Click the [] to add a new field, and choose the type of field you want to add from the panel that opens.
After you\'ve selected your desired field type, you will be presented with a number of options. You can review each one of them and what they mean below.
Setting
Required?
Description
Name
The name of the field you are creating
Description
Add additional details here
Data Structure
**Single** - Each record will only store one value in this field. This is the more common selection.
**List** - Each record can hold multiple values in this field. For example, if this was a table of authors, we might have a field that can store multiple books for each author.
Allow Nullable Values
A `null` value is similar to an empty value in that it represents \"nothing is here\", but it\'s still an actual value written to the record. Useful if you need to specifically check whether or not that field has data stored.
Format
For some field types, you can specify a format. This does not change the actual data being stored and is only used to enable easier viewing and editing for you inside of the table view.
Default Value
When adding new records, you can automatically populate a default value
^**Note:**^ ^If\ your\ field\ allows\ nullable\ values,\ they\ will\ auto-apply\ null\ to\ new\ records\ as\ a\ default\ value.\ Adding\ \'null\'\ to\ the\ default\ value\ field\ manually\ will\ be\ processed\ as\ text\ and\ have\ unintended\ results.^
**Note**
The settings listed below only impact your API endpoints that utilize the database link feature. This means that it is possible to make changes that break these rules via the database table view.
Setting
Required?
Description
Required
Determines whether or not this field is required when adding a record
Sensitive Data
Hide the contents of this field from certain areas, such as request history
Column Visibility
**Public** - The field will be available as an input
**Private** - This field will not appear in inputs
**Internal** - Hide this field from API inputs and responses
Custom Rules & Filters
See below.
####  
Custom Rules & Filters
For each field, you can apply various rules and filters to ensure that the data is stored in the format that you expect.
Filter Name
Purpose
min
Enforces a minimum number of required characters
max
Enforces a maximum number of required characters
startsWith
Enforces a prefix
endsWith
Enforces a suffix
prevent
Blacklists phrases
lower
Stores the value in all lowercase
upper
Stores the value in all uppercase
alphaOk
Whitelist certain alphanumeric characters
digitOk
Whitelist certain numbers
ok
Whitelist certain characters
pattern
Enforce a regex pattern
------------------------------------------------------------------------
[⚙️] Field Options
Right-click on the header of a field to access field-related settings and make adjustments to the options already detailed above, as well as some additional controls.
[] Rename this field
Please note that renaming a field should be handled with care, as it may impact any function steps that reference that field.
You can click [] when viewing a database table to open **Referenced By** and view any database operations that utilize that column first to understand where changes need to be made. In the screenshot below, we know we want to update the name column, so we can use **Referenced By** to find where it\'s used beforehand.
[]
[] Access field settings (the options detailed earlier in this document)
[] Make a copy of this column
[] Insert a new column directly after the selected column
[] Reorder your database fields. This does not impact how the data is returned in your function stacks.
[] Change the data type of the column
Xano will attempt to convert the data in the column to the new data type, but because of potential variations between data types, and the specific data being converted, this may not always be successful. It is **always** recommended to create a new column instead.
[] Delete the column
Deleting a column is irreversible. Proceed with caution.
------------------------------------------------------------------------
[🔢] Adding Data
###  
Generate Test Data
After you\'ve created your database schema, you can generate some sample data to use right away by clicking [ ][🪄][**Generate Records** ]
This option is located at the **bottom** of your database records --- so, if you have no records, you should see it right at the top.
The record generation will look at the name and the data type for each of your fields and try to auto-suggest what they should be filled with.
You can click on one of those data types to change what that field is populated with, or specific settings related to that data type.
In the bottom-right corner, you can change the number of records generated, up to 100 at a time.
When you\'re ready, click \"Generate\" and you should see your new sample data populated. You can always generate more records if you\'d like.
Hint
Want to clear out all of the sample data? There\'s a quick \"Clear All Records\" shortcut in the upper-right settings menu. **This will delete all records in the table in one swing.**
###  
Adding Data Manually
Click []at the bottom of your existing records (if any) to add a new record.
The record will be created using any default values you\'ve specified in the field options, and you can click on each cell to fill it in manually.
You can also click []to open up the card view and fil in multiple, or all fields at once when creating a new record.
------------------------------------------------------------------------
[⚙️] Additional Table Settings
Click []to access table settings after creation, including both settings detailed earlier in this document, as well as some additional options.
Setting Name
Description
Authentication
Determines whether or not this table is used for user authentication.
Security
Change the table GUID.
Versions
Xano maintains a version history of your table schema. You can roll back to a previous version of your schema if you\'ve made changes that you want to undo.
**Note**: This does not change the data in your table, only the fields. If you need to restore a backup of your table data, see this document.
Triggers
Access your database triggers.
Auto-complete
Access your auto-complete settings.
Clear all records
Deletes all records in the table. You can also choose to reset the primary ID back to 1 on tables that use a sequential ID.
Clone table
Cloning copies the table schema. Cloning **does not** copy existing data.
Export data
Export your table data using the current view as a CSV
Import data
Import records from a CSV [📖] **Learn More**
------------------------------------------------------------------------
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
------------------------------------------------------------------------
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
Last updated 1 month ago
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

