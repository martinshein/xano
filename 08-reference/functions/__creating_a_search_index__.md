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
title: '**Creating a Search Index**'
---

# **Creating a Search Index**

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'fuzzy-search'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Fuzzy Search \| Xano Documentation'
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
    Creating a Search Index
Was this helpful?
Copy
1.  Building Backend Features
Fuzzy Search 
============
Xano offers robust search capabilities, commonly referred to as *fuzzy search*, that you can utilize while querying records in a function stack. This includes normalization of words (ie. party vs parties), case-insensitive support, flexible expressions (words, phrases, and negations), and weighted priorities (ie. title vs description) for relevance.
The following demonstrates how to set up search in your database, the logic behind the search functionality, and best practices for utilizing search queries.
<div>
</div>
**Watch more videos on Fuzzy Search**
###  
**Creating a Search Index**
First, create an index. Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed. An index is used to define which fields of the database table you want to search. You can even build multiple search indexes on the same table to build different search criteria. For example, if you have both public and private data in the same table, you can build a \"normal user\" and an \"administrator\" search.
To create an index, click **Indexes** at the top of the table you would like to build search for, and then click **Create Index.**
Choose **search** as the index type, and give the index a name. Next, specify the language for the data you are searching, the fields you are searching, and the ranking order of the fields being searched.
An example of creating a search index.
In this example, we created a new search index on a database of movies called **search\_movies**, in English, and are searching two fields in that database: title and overview. The title field will rank higher than data in the overview field in the qualified search results.
Once ready, click **Save** and Xano will build your index. This can take a few minutes depending on the volume of data of the table.
###  
Building a Search API
After generating the index, it can be implemented it into a query in the function stack. Use the **Custom Query** feature in the **Filter** tab of the **Query All Records** function.
When adding a custom query, the newly created index is available in the expression builder, noted by the **\$** symbol. It is also labeled as *search* underneath the name.
Look for the **\$** symbol as well as the word **search** to easily find your search index when configuring your query.
Next, set the operator to **search** and specify the search query. In this example, we are using an input called **search\_query.**
Setting the operator to Search and specifying our search query.
Congratulations! 🥳 You\'ve just implemented super-fast search inside your function stack.
###  
Ranking
You can implement a ranking system and sort the search results by this rank for more precise search results. To do this, go to the **Output** tab of the **Query All Records** function, add an **eval** on the search index, and apply the **search\_query** filter. This tells Xano to \"use my search index to generate a ranking score of my results based on my search query\".
Create and Eval on the search index by applying the search\_rank filter so we can sort by ranking.
After, add a sort to the query using the newly created eval (in this example, called \"rank\"). You may also consider to enable paging especially on larger queries.
Add a Sort to the Query by clicking on the Return portion of the Output tab.
Order by in descending order will provide the most relevant search results first.
###  
Different Search Methods
Search queries can be written in different ways to fulfill specific search requirements.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Words separated by a space imply an AND.
    **Example:** A query of *\"toy story\"* means *search for toy AND story*
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Exact phrase searches are possible using double quotes.
    **Example:** If you wanted to search for *\"Toy Story\"* as an exact match, your query would be *\"Toy Story\" with the quotation marks*.
    **Note:** if you are entering this search expression directly into a JSON payload, then you may need to escape the quotes with a backslash. example: ``
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Partial phrase matching
    **Example:** `"Toy * Story"` would return any results that contain Toy Story with one word in between. `"Toy *** Story"` would return any results that contain Toy Story with three words in between.
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    Wildcard matching
    **Example:** `Sto:*` would return any results that contain words that start with sto.
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    Expression groups
    **Example:** `(Woody or Buzz) Toy` would return multiple matches for the word Toy that also include either Woody or Buzz.
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    Negation of specific words is possible by using a - character.
    **Example:** If you wanted to search for movies that have *Toy* in the title, but not *Toy Story*, your query would be `"toy -story"`.
    :::
7.  ::: 
    ::: 
    :::
    :::
    ::: 
    You can also use a combination of these to get even more specific.
    **Example:** Searching for `"toy story" day -night` would mean *search for the phrase Toy Story and the word day, without the word night.*
    :::
8.  ::: 
    ::: 
    :::
    :::
    ::: 
    Priority targets allow you to specify which priority defined in your search index to use for the specific expression. This can be combined with wildcard matching as well.
    **Example:** `Toy Story:2` would search for all records containing the word Toy, as well as the word Story in any fields representing priority 2 in your search index.
    **Example:** `Toy Sto:*2` would search for all records containing the word Toy, as well as words starting with Sto in any fields representing priority 2 in your search index.
    :::
9.  ::: 
    ::: 
    :::
    :::
    ::: 
    Single vs Plural is supported.
    For example, *\"toy\"* will also return results that contain *\"toys\"*.
    :::
**Stop Words** \-- are commonly used words such as articles, pronouns and prepositions. For example: *is, and, an, or, the.* Stop words are not included in your search query.
###  
Search Results
Search results are returned just like any other API response and the data works just like any other variable inside Xano.
Last updated 6 months ago
Was this helpful?