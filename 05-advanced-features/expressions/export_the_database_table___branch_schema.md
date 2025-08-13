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
title: export the database table + branch schema
---

# export the database table + branch schema

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'workspace-import-and-export'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Workspace Import and Export \| Xano Documentation'
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
    [[POST]export the database table + branch schema](#post-workspace-workspace_id-export-schema)
Was this helpful?
Copy
1.  Xano Features
2.  Metadata API
Workspace Import and Export 
===========================
**Before you proceed\...**
Workspace exports will only contain one branch which defaults to live unless you specify a branch in the request.
Drafts are not exported.
Imports overwrite the entire contents of the destination workspace.
These endpoints will only function properly on **paid Xano plans**.
For large workspaces, import may not function properly using the Metadata API. In these cases, reach out to support and we can assist with the import process.
<div>
</div>
###  
export the database table + branch schema
post
[https://xxfo-0dml-kzcl.dev.xano.io/api:meta]/workspace/[]/export-schema
Leave the `branch` parameter empty to indicate the current live branch. `password` is optional. If provided, will encrypt the export and will be required when importing the file.
Required API Scope:
Instance Workspace: Read
Authorizations
Path parameters
[[workspace\_id][integer · int64][Required]]
Body
[application/json]
application/jsonmultipart/form-data
[[password][string][Optional]]
[[branch][string][Optional]]
Responses
[200]
Success!
application/json
[[Response][object]]
[400]
Input Error. Check the request payload for issues.
[401]
Unauthorized
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
post
/workspace/[]/export-schema
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
POST /api:meta/workspace//export-schema HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 27
```
[application/json]
application/jsonmultipart/form-data
Test it
[[200][]]
Success!
Copy
``` 
```
###  
export the workspace and content
post
[https://xxfo-0dml-kzcl.dev.xano.io/api:meta]/workspace/[]/export
Leave the `branch` parameter empty to indicate the current live branch. `password` is optional. If provided, will encrypt the export and will be required when importing the file.
Required API Scope:
Instance Workspace: Read
Authorizations
Path parameters
[[workspace\_id][integer · int64][Required]]
Body
[application/json]
application/jsonmultipart/form-data
[[password][string][Optional]]
[[branch][string][Optional]]
Responses
[200]
Success!
application/json
[[Response][object]]
[400]
Input Error. Check the request payload for issues.
[401]
Unauthorized
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
post
/workspace/[]/export
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
POST /api:meta/workspace//export HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 27
```
[application/json]
application/jsonmultipart/form-data
Test it
[[200][]]
Success!
Copy
``` 
```
###  
import schema into a new branch and optionally set it live
post
[https://xxfo-0dml-kzcl.dev.xano.io/api:meta]/workspace/[]/import-schema
import schema into a new branch and optionally set it live
Authentication: required
Required API Scope:
Instance Workspace: Read
Authorizations
Path parameters
[[workspace\_id][integer · int64][Required]]
Body
[[file][string · binary][Required]]
[[newbranch][string][Required]]
[[setlive][boolean][Optional]]
[[password][string][Optional]]
Responses
[200]
Success!
application/json
[[Response][object]]
[400]
Input Error. Check the request payload for issues.
[401]
Unauthorized
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
post
/workspace/[]/import-schema
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
POST /api:meta/workspace//import-schema HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: multipart/form-data
Accept: */*
Content-Length: 69
```
Test it
[[200][]]
Success!
Copy
``` 
```
###  
import the archive into the specified workspace and replace it with supplied content and configuration
post
[https://xxfo-0dml-kzcl.dev.xano.io/api:meta]/workspace/[]/import
If the file is encrypted, the correct `password` is required to decrypt.
Required API Scope:
Instance Workspace: Update
Authorizations
Path parameters
[[workspace\_id][integer · int64][Required]]
Body
[[password][string][Optional]]
[[file][string · binary][Required]]
Responses
[200]
Success!
application/json
[[Response][object]]
Show properties
[400]
Input Error. Check the request payload for issues.
[401]
Unauthorized
[403]
Access denied. Additional privileges are needed access the requested resource.
[404]
Not Found. The requested resource does not exist.
[429]
Rate Limited. Too many requests.
[500]
Unexpected error
post
/workspace/[]/import
[HTTP]
HTTPcURLJavaScriptPython
Copy
``` 
POST /api:meta/workspace//import HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: multipart/form-data
Accept: */*
Content-Length: 35
```
Test it
[[200][]]
Success!
Copy
``` 
{
  "id": 1,
  "name": "text",
  "description": "text",
  "branch": {
    "id": 1,
    "created_at": "text",
    "updated_at": "text",
    "description": "text",
    "label": "text",
    "backup": true,
    "color": "#ebc346",
    "parent_id": 1,
    "guid": "text",
    "workspace": ,
    "user": ,
    "history": ,
    "middleware": {
      "function_pre": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "function_post": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "query_pre": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "query_post": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "task_pre": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "task_post": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "defaults": 
  }
}
```
Last updated 3 months ago
Was this helpful?

## Code Examples

```
 
POST /api:meta/workspace//export-schema HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 27

```

```
 

```

```
 
POST /api:meta/workspace//export HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 27

```

```
 

```

```
 
POST /api:meta/workspace//import-schema HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: multipart/form-data
Accept: */*
Content-Length: 69

```

```
 

```

```
 
POST /api:meta/workspace//import HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: multipart/form-data
Accept: */*
Content-Length: 35

```

```javascript
 
{
  "id": 1,
  "name": "text",
  "description": "text",
  "branch": {
    "id": 1,
    "created_at": "text",
    "updated_at": "text",
    "description": "text",
    "label": "text",
    "backup": true,
    "color": "#ebc346",
    "parent_id": 1,
    "guid": "text",
    "workspace": ,
    "user": ,
    "history": ,
    "middleware": {
      "function_pre": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "function_post": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "query_pre": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "query_post": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "task_pre": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "task_post": [
        {
          "name": "text",
          "as": "text",
          "context": ,
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": ,
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": ,
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  },
                  "children": [
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "defaults": 
  }
}

```

