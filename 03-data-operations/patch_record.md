---
category: 03-data-operations
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Patch Record
---

# Patch Record

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
    :::
    :::
    ::: 
    **Edit Record** is best used when you have a static expectation for which fields need to be updated when the function is executed. For example, maybe you have an endpoint specifically to allow a user to update their password. Edit Record would make sense here, because you would not be changing any other information.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Patch Record** is best used when you have an endpoint that can update multiple fields, but may not always need to do so. Something like a user submitting a collection of edits to their user profile would fall under this example.
    :::
**Patch Record** is a little different than **Edit Record** in the way values are provided to it. While Edit Record gives you the option to address each field individually inside of the function, **Patch** only expects a field name and field value (so it knows which record to patch) and a JSON object representing all of the values to be updated.
In the following example, let\'s say that our record currently looks like this:
Copy
``` 
```
We want to build an endpoint that allows our users to update one or more of these fields in one swing. This means that we need to construct a JSON object that contains **only** the values to be updated and provide that to our Patch Record statement.
If Chris wants to update only his city, the object we provide to Patch would look like this:
Copy
``` 
```
And our patch statement might look like this:
However, using the **set filter** in the scenario where multiple fields **might** be provided is not recommended. This is because if Patch is provided empty or null values, it will write those to the record, and the goal is to only write the fields we want.
**Please be aware that Patch will write every field provided in the JSON object to the record, even blank and null values.
The JSON object used for Patch should only provide the fields you want to update, and nothing more. Providing empty or null values unintentionally can result in data loss.**
Some frontends will always send empty or null values regardless of what data points are actually defined.
To make Patch work as it is normally expected, you\'ll want to leverage filters like:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `filter_null` to remove null values
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `filter_empty_text` to remove empty text strings
    :::
Using a **Get All Raw Input** function along with **Patch Record** can be a perfect combination.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Get All Raw Input** provides a JSON object of all of the input fields passed to the API.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    We can then provide the output of this function to **Patch Record**, giving us an easy and fast method of building a flexible endpoint for editing records.
    :::
Our final endpoint might look something like this:
Last updated 4 months ago
Was this helpful?

## Code Examples

```
 

```

```
 

```

