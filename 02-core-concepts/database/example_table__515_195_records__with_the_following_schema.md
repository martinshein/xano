---
category: database
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'Example Table: 515,195 records, with the following schema'
---

# Example Table: 515,195 records, with the following schema

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: indexing
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Indexing \| Xano Documentation'
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
    What is an Index?
Was this helpful?
Copy
1.  The Database
2.  Database Performance and Maintenance
Indexing 
========
<div>
</div>
**What is an Index?**
An index is a database feature that helps improve the speed and efficiency of queries made against a database table. They help when searching through large, unordered data sets and give the database search engine a quick way to sort and find specific data. Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access to ordered records.
**How do they work?**
A table index is very similar in practice to the index of a textbook. When there is a specific piece of information that you want to find, reading every page of that book to find what you are looking for can be very slow and inefficient. So, you would use the index at the back of the book to find exactly which page contains the information you need.
This is the same concept for a database table index. They create a special type of lookup table in the background that the database engine can use to retrieve the data faster than looking through each individual row for every search.
**When to use an Index?**
Indexes are the most beneficial in the following scenario(s):
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You have a specific query that you want to ensure is as performant as possible
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The query uses simple operators in one or more conditions
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Yes**: Where user region = Canada
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **No**: Where user ID is even, or user region is empty
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The table has 10,000 records or more
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The table is not frequently written to or updated
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        This is because when a table is indexed and frequently written to, the performance of inserting new data can suffer because the index has to be updated at the same time. You can index a table that has frequent writes, but use caution.
        :::
    :::
How do I apply an index properly?
It's important to construct your index based on the query being performed that you are trying to address. We will use the an example scenario to explain an approach to indexing. All scenarios were built and performed on a Launch plan instance with no additional load or processing. Your results may vary based on other factors related to your specific instance or the plan you are on.
####  
Example Table: 515,195 records, with the following schema
id
name
region
country
profession
firstname
lastname
email
birthday
####  
Example Query: Find all users in a specific country, with a specific profession
Example query with no indexing
With no indexing applied, this query takes **0.62** seconds to complete.
Because these two pieces of data can exist independently of each other \-- meaning we don\'t need to know a country to determine a profession, and vice versa, we will apply two separate indexes to our table, one for each field.
Indexes applied based on the sample query
With these indexes applied, the example query now executes in **0.05** seconds, a **95% increase in query speed.**
Example query with indexing applied
###  
When should I index a single field by itself vs multiple fields in the same index?
This is based on the hierarchy of the query being performed, and what makes the most sense in terms of your data set. It is also important to understand how multi-field indexes are executed.
**The order of fields in your index matters.** When building a multi-field index, you want to start with the field that contains the **least** amount of unique values, moving forward to finishing with the field that has the **most** unique values.
With a multi-field index, each \'step\' (field) is essentially placed into a new bucket that the database knows it can use to potentially find matching data. Using an example of location data where we have a `city`, `state`, and `country` field, we know that country has the least unique values. This means that when we\'re building our index, we\'d add the country field first. Moving on from there, we would add our states, and then finally the cities, so when the database builds the index, it builds the most efficient bucketing possible.
In an adverse example, consider an index on a timestamp field. Timestamps in Xano use milliseconds, which obviously means that these values will almost be unique for every single record. If we built a multi-field index that started with this timestamp field, we are creating that many buckets right away before trying to look for less specific data, which means that the query becomes extremely inefficient.
It is also important to note that if you have multiple fields defined in a single index, but are not using both of those fields in your query, the index will not provide any benefit to the performance of that query. Indexes are only useful if you are indexing based on the queries you are making, and the hierarchy of your query makes sense.
You can use a field in a double-field index as well as a single-field index, but it is important to consider the storage requirement for each index you create. In addition, it is possible to 'trap' yourself into a situation where you have too many indexes, and it becomes more difficult to determine what is helping and what is not.
**Example Query: Find all users who are part of a specific subset of artists**
Example query with no indexing
Executing the example query, with no indexing applied, takes **1.44s**.
Because we know that the artist\_service field requires the profession field to make sense in the context of our query, we will place both of those fields, in order, in the same index.
Applying the index for the example query
Example query results with indexing applied
After applying the index shown, this query completes in **0.02 seconds, 98% faster.**
In this same scenario, if there was a world where we would potentially query **artist\_service** by itself, and it did not also need a **profession** to make sense based on the context of our query, we would want to create single-field indexes for these fields.
**Example 2: When to use Single-Field vs. Multi-Field Indexes**
We have a table of people, and each person lives in a specific region. We want to build a query where we find all people named \"Jack\" in a specific region. We will not be building any other queries to search our table of people.
**In this example, we would build one index with both fields**. This is because we are not utilizing these fields in any other queries, and they are both required in the context of the query we are building.
**Example 3:** **When to use Single-Field vs Multi-Field Indexes**
We have a table of people, and each person lives in a specific region. We want to build a query where we find all people named \"Jack\" in a specific region. We also want to build a second query that just finds us all people named \"Jack\", and a third query that finds all people in a certain region without specifying a name.
**In this example, we would build two single-field indexes, one for each field.** This is because we are utilizing the fields in multiple different queries.
###  
Using the GIN Index to search complex data types
The GIN index is used specifically when searching through more complex data types, such as objects and arrays, as these fields can not be indexed using the methods described previously.
This index is automatically applied to all of your database tables; you do not need to add or maintain this.
Let\'s say, as an example, we have a list field called **my\_list**, and we want to find all records that contain a value of **special** inside of **my\_list.**
To use the GIN index in this query, we first need to create a variable with the following structure:
Copy
``` 
```
The structure starts with an object containing the name of the field, with the value being an empty array. We then use the **push** filter to add the value we are searching for inside of that list. You can use multiple push filters to search for multiple values.
Constructing the variable to be used in our query
Once we have our object constructed, we will set up our custom query by selecting the table on the left side, which leaves us with the \'contains\' operator, and our constructed object on the right.
An example of a GIN index query
In this example, a query without indexing takes **0.23** seconds.
In this example, utilizing the GIN index, the query takes **0.02** seconds.
How to Apply an Index in the Database View
In the database view, click on the table that you want to index. Choose \"Indexes\" from the top bar.
Click \"Create Index\" to add a new index, or click on an existing index to manage it.
Choose the fields, sort, and index type. When done, click \'Save\'.
**Note**: Creating or updating an index can take several minutes depending on the complexity and the size of the database table.
**Note**: Indexes will significantly increase the storage your database table requires. Please ensure you have enough free space (we recommend trying to stay around \~50% free space) before indexing your tables.
###  
Types of Indexes
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Primary**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Automatically applied and maintained
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Indexes the primary key (ID) of each record and enforces uniqueness
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **GIN**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Automatically applied and maintained
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Most suitable for complex data types (JSON, lists, objects) and full-text search
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Index**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        The most common index type
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Used when indexing for standard queries
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Unique**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        A special type of index to enforce unique values in a column'
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Spatial**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        A special type of index designed to optimize queries involving spatial data, such as geography fields.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Search**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        A special type of index to be used in conjunction with Xano fuzzy search
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Vector**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        A unique indexing type used for working with the Vector field type.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Indexing should **always** be used on vector columns, regardless of the amount of records.
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            **L2 Distance** - Measures the Euclidean distance between vectors
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            **L1 Distance** - Measures the taxicab distance between vectors.
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            **Inner product** - Measures dissimilarity based solely on amplitude (recommended for OpenAI and other normalized vectors)
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            **Cosine Distance** - Measures dissimilarity between vectors, considering their length and amplitude
            :::
        :::
    :::
When should you *not* use an index?
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Do not use an index on a table containing only a few records. They are most valuable when your record count approaches \>5,000 records.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Indexes should not be used on fields that have or will have a high number of **null** values, because that essentially means there is nothing to index on.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You can not apply a normal index to an array or object field, so keep that in mind when designing your database structure. You can use the automatically maintained GIN index, detailed later on this page.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    If your field / column names are frequently changing, you should not index that field.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    If a table is frequently used to add / edit data, it may be best practice to not index this table. While your query speeds can still benefit, they can also slow the performance of adding to or editing data on this table given the nature of creating an index behind the scenes.
    :::
Last updated 7 months ago
Was this helpful?

## Code Examples

```
 

```

