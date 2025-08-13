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
title: Two Conditions Combined with OR
---

# Two Conditions Combined with OR

[](../../../../index.html)
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
    Basic Equals Operation
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../../building-with-visual-development.html)
2.  Functions
3.  Database Requests
4.  Query All Records
External Filtering Examples 
===========================
**Basic Equals Operation**
Checking if a user ID equals 1:
Copy
``` 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "=",
      "right": 
    }
  }]
}
```
**Between Operation**
Finding transactions with amount between 100 and 1000:
Copy
``` 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "between",
      "right": 
    }
  }]
}
```
**Contains Operation**
Finding users with email containing \'\@company.com\':
Copy
``` 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "contains",
      "right": 
    }
  }]
}
```
**Multiple Conditions Example**
Finding active premium users who have made at least 5 purchases:
Copy
``` 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": ">=",
        "right": 
      }
    }
  ]
}
```
**Case-Insensitive Pattern Matching (ilike)**
Finding products with names starting with \'phone\', regardless of case:
Copy
``` 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "ilike",
      "right": 
    }
  }]
}
```
**Array Membership (in)**
Finding orders with specific status values:
Copy
``` 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "in",
      "right": 
    }
  }]
}
```
**Complex Multiple Conditions**
Finding high-value transactions (\>1000) made in the last 30 days by premium users:
Copy
``` 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": ">",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": ">=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}
```
Using And/Or
By default, all statements will be considered an \'and\' statement, and nothing needs to be specified. You\'ll only need to specify whether `or` is `true` when you want to use it.
For readability purposes, however, you can specify `or` is `false` if you\'d like.
The two examples below demonstrate this and would return the same result.
Copy
``` 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}
```
Copy
``` 
// Verbose specification of "or"
{
  "expression": [
    {
      "or": false,
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}
```
###  
Two Conditions Combined with OR
This example filters for users whose status is \'inactive\' OR whose account type is \'basic\'.
Copy
``` 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "or": true,
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}
```
###  
Three Conditions with AND and OR
This example filters for active users AND (whose purchase count is less than 10 OR whose last login is before a specific date).
Copy
``` 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": "<",
        "right": 
      }
    },
    {
      "or": true,
      "statement": {
        "left": ,
        "op": "<",
        "right": 
      }
    }
  ]
}
```
###  
Using And/Or Groups - (Condition A AND Condition B) OR (Condition C AND Condition D)
Here\'s how the logic `(a = 1 AND b = 2) OR (a = 4 AND b = 5)` would be represented:
Copy
``` 
{
    "expression": [
      {
        "or": false,
        "type": "group",
        "group": {
          "expression": [
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            },
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            }
          ]
        }
      },
      {
        "or": true,
        "type": "group",
        "group": {
          "expression": [
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            },
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            }
          ]
        }
      }
    ]
  }
```
Last updated 3 months ago
Was this helpful?

## Code Examples

```javascript
 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "=",
      "right": 
    }
  }]
}

```

```javascript
 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "between",
      "right": 
    }
  }]
}

```

```javascript
 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "contains",
      "right": 
    }
  }]
}

```

```javascript
 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": ">=",
        "right": 
      }
    }
  ]
}

```

```javascript
 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "ilike",
      "right": 
    }
  }]
}

```

```javascript
 
{
  "expression": [{
    "statement": {
      "left": ,
      "op": "in",
      "right": 
    }
  }]
}

```

```javascript
 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": ">",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": ">=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}

```

```javascript
 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}

```

```javascript
 
// Verbose specification of "or"
{
  "expression": [
    {
      "or": false,
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}

```

```javascript
 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "or": true,
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    }
  ]
}

```

```javascript
 
{
  "expression": [
    {
      "statement": {
        "left": ,
        "op": "=",
        "right": 
      }
    },
    {
      "statement": {
        "left": ,
        "op": "<",
        "right": 
      }
    },
    {
      "or": true,
      "statement": {
        "left": ,
        "op": "<",
        "right": 
      }
    }
  ]
}

```

```javascript
 
{
    "expression": [
      {
        "or": false,
        "type": "group",
        "group": {
          "expression": [
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            },
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            }
          ]
        }
      },
      {
        "or": true,
        "type": "group",
        "group": {
          "expression": [
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            },
            {
              "or": false,
              "statement": {
                "left": ,
                "op": "=",
                "right": 
              },
              "type": "statement"
            }
          ]
        }
      }
    ]
  }

```

