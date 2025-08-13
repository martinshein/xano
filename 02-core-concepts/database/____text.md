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
title: "[\U0001F4C4] Text"
---

# [📄] Text

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'field-types'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Field Types \| Xano Documentation'
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
     Text
Was this helpful?
Copy
1.  The Database
2.  Database Basics
Field Types 
===========
###  
[📄] Text
A text field can contain anything that you\'d want to provide, such as names, addresses, location names, and descriptions.
Copy
``` 
Hello
John Smith
Chicago
```
###  
[🔢] Integer
An integer is just a whole number, such as 3, 42, 100, etc\...
Copy
``` 
1
100
1000
```
###  
[㊙️] UUID
UUID stands for **universally unique identifier**, and is a random string of letters and numbers, typically used to enforce uniqueness amongst other records in the table.
Copy
``` 
105c8b80-fd24-4cf3-bbed-a43e8134c8b0
984x0t12-rt12-5ey6-poqw-b12y1923e6l0
```
###  
[🍱] Object
Imagine a folder that can hold different types of information together - like how a contact card holds someone\'s name, phone, and address. Or, recording certain data about vehicles, such as year, make, and model.
Copy
``` 
```
###  
[❓] Table Reference
This field type is like a quick link to a record in another table (or even the same table, if your use case requires it). Table references are useful when separating data between tables and maintaining relationships between them.
For example, you might have a table of users, and a table of user roles. In your users table, you could add a table reference to your roles table to link each user to a specific role. This is advantageous because it is easier to maintain consistency and make changes to role types.
###  
[🤖] Vector
Vectors are used for AI/LLM applications to store data that helps the model find the most relevant information based on the query being made. Think of it like a DNA sequence - it\'s just a string of values that might not mean much to us when we look at them directly, but they encode important information that the AI system knows how to interpret.
Copy
``` 
[-0.235, 0.458, -0.891, 0.023, 0.444, -0.657, ...]
```
-   ::: 
    ::: 
    :::
    :::
    ::: 
    It\'s a fixed-length array of numbers (often hundreds or thousands of elements)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The numbers are usually floating-point values (often between -1 and 1)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Each vector has the same dimensionality (length) within a given field
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The individual numbers themselves don\'t have inherent meaning - they\'re abstract representations that are provided by an AI model and stored for later use.
    :::
###  
[🛑] Enum
An enum is like a text field, but only allows for specific values. It\'s like a multiple choice question instead of a freeform input. For example, an enum field would be appropriate to use if you wanted to store a color from a specific list.
Copy
``` 
Red
Blue
Green
Orange
```
###  
[🕕] Timestamp
Xano stores timestamps in UNIX Epoch format. They are stored in the database as an integer, but appear to you as human readable timestamps in your local timezone. While it may seem unintuitive, this format is ideal for ensuring that you can always store and return accurate time-based data in a user\'s local time zone, and have the most flexibility when down-to-the-millisecond accuracy is required.
Copy
``` 
1733762528000 // This Epoch timestamp in MS represents Mon, 09 Dec 2024 16:42:08 GMT
```
###  
[📅] Date
This is just a calendar date. It offers less flexibility than the recommended Timestamp field, but can be useful when exact times are not important, such as birthdays or anniversaries.
###  
[✅] Boolean
A boolean is just a true or false value. It\'s a bit different than storing true or false in a text string and the recommended option if you need to store true and false values.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Booleans take up less storage space, as they are one-bit values (0/1) instead of the full text.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    They enforce data validation and ensure that only true / false values are stored in the database instead of different variations with potential errors (such as TRUE, true, ture, Y, 1)
    :::
###  
[🔢] Decimal
This is similar to the integer field, but allows for decimal points. Use this field type for things like money (\$12.34) or measurments (3.14 inches).
###  
[📨] Email
Xano\'s Email field is really just a text field, but enforces proper formatting to ensure that emails are entered properly into the database.
###  
[🔑] Password
Xano\'s Password field is really just a text field, but includes extra security around storing and showing the value to you.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Xano\'s passwords are stored encrypted. Password fields will never store passwords in plain text.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    They are not viewable from the database view.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    If you return the password field in a database query, only the encrypted version is shown. It is not possible to retrieve raw user passwords from a password field.
    :::
###  
[💻] JSON
Think of this as a flexible container that can hold different types of information in an organized way - like a recipe that lists ingredients and steps.
Copy
``` 
{
  "name": "Classic Chocolate Chip Cookies",
  "prepTime": 15,
  "ingredients": [
    ,
  ],
  "steps": [
    "Cream butter and sugars",
    "Add eggs and vanilla",
    "Mix in dry ingredients",
    "Stir in chocolate chips"
  ],
  "isGlutenFree": false,
  "servings": 24
}
```
###  
[🖼️] Storage
Xano includes support for file storage, and utilizes your database to record files you have stored in Xano. The database tables themselves do not include the actual files; only metadata for the files themselves, such as name, size, and location.
Copy
``` 
{
  "promoImage": {
    "access": "public",
    "path": "/vault/ABC123xyz/D3F4G5hij/K7L8M9.../sample-image.png",
    "name": "sample-image.png",
    "type": "image",
    "size": 123456,
    "mime": "image/png",
    "meta": ,
    "url": "https://example-domain.io/vault/ABC123xyz/sample-image.png"
  }
}
```
###  
[🗺️] Geography
Geography fields in Xano can contain different types of information, all based around latitude and longitude.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Points on a map
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    A route of connected points
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    A polygon of points, such as a specific geographical area
    :::
####  
Geo Point
Copy
``` 
{
    "type": "point",
    "data": 
}
```
####  
Path
Copy
``` 
{
    "type": "path",
    "data": [
            ,
        ]
}
```
####  
Polygon
Copy
``` 
{
 "type": "poly",
 "data": [
   ,
   ,
   ,
   ,
 ]
}
```
Last updated 5 months ago
Was this helpful?

## Code Examples

```
 
Hello
John Smith
Chicago

```

```
 
1
100
1000

```

```
 
105c8b80-fd24-4cf3-bbed-a43e8134c8b0
984x0t12-rt12-5ey6-poqw-b12y1923e6l0

```

```
 

```

```
 
[-0.235, 0.458, -0.891, 0.023, 0.444, -0.657, ...]

```

```
 
Red
Blue
Green
Orange

```

```
 
1733762528000 // This Epoch timestamp in MS represents Mon, 09 Dec 2024 16:42:08 GMT

```

```javascript
 
{
  "name": "Classic Chocolate Chip Cookies",
  "prepTime": 15,
  "ingredients": [
    ,
  ],
  "steps": [
    "Cream butter and sugars",
    "Add eggs and vanilla",
    "Mix in dry ingredients",
    "Stir in chocolate chips"
  ],
  "isGlutenFree": false,
  "servings": 24
}

```

```javascript
 
{
  "promoImage": {
    "access": "public",
    "path": "/vault/ABC123xyz/D3F4G5hij/K7L8M9.../sample-image.png",
    "name": "sample-image.png",
    "type": "image",
    "size": 123456,
    "mime": "image/png",
    "meta": ,
    "url": "https://example-domain.io/vault/ABC123xyz/sample-image.png"
  }
}

```

```javascript
 
{
    "type": "point",
    "data": 
}

```

```javascript
 
{
    "type": "path",
    "data": [
            ,
        ]
}

```

```javascript
 
{
 "type": "poly",
 "data": [
   ,
   ,
   ,
   ,
 ]
}

```

