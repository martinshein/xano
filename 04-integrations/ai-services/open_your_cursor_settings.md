---
category: ai-services
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Open your Cursor settings
---

# Open your Cursor settings

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'connecting-clients'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Connecting Clients \| Xano Documentation'
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
     Cursor
Was this helpful?
Copy
1.  Build For AI
2.  MCP Builder
Connecting Clients 
==================
 Cursor
The below instructions will allow you to connect your Xano MCP server to Cursor and make them available across any project. The below method does not support authentication. If you need authentication or want to define per-project MCPs, use these instructions instead.
<div>
1
###  
Open your Cursor settings
2
###  
Under the [ Features ] subsection, scroll down to MCP Servers
3
###  
Click [ + Add new MCP Server ]
Give your server a name.
The `type` should be `sse`
Paste your server URL in the Server URL section. You can retrieve your server URL by navigating to your server in Xano and clicking **Copy Connection URL**.
4
###  
You should now see your MCP Server ready in Cursor
5
###  
In your chat window, you can now interact with the tools included in your MCP server that\'s connected
Make sure the conversation type is set to Agent
In our example, we have a tool that checks if a user is marked as an administrator.
</div>
 Cursor (per-project)
<div>
1
###  
In your project\'s root directory, create a new folder called `.cursor`
2
###  
Create a new file inside of that folder called `mcp.json`
3
###  
Fill out the required details inside of `mcp.json`
If the file is blank, start with the basic structure and replace the placeholder values with your own.
Copy
``` 
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization:$"
      ],
      "env": 
    }
  }
}
```
You can add multiple entries if you have multiple MCP servers. See the below example.
Copy
``` 
{
  "mcpServers": {
    "xano_development": ,
    "xano_production": ,
    "xano_tools": 
  }
}
```
4
###  
Restart Cursor.
In your chat window, you can now interact with the tools included in your MCP server that\'s connected
Make sure the conversation type is set to Agent
In our example, we have a tool that checks if a user is marked as an administrator.
</div>
------------------------------------------------------------------------
 Claude Desktop
<div>
1
###  
Install the prerequisites
You need Node.js installed on your system.
Download the latest installer from the Node.js official website for your specific platform.
2
###  
Open Claude Desktop\'s config file in your text / code editor of choice
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Mac OS: `~/Library/Application Support/Claude/claude_desktop_config.json`
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Windows: `%APPDATA%\Claude\claude_desktop_config.json`
    :::
3
###  
Add an entry in the config file for your Xano MCP server
Click **Edit Config** and in the window that opens, open `claude_desktop_config.json` in your favorite text or code editor.
If the file is blank, start with the basic structure and replace the placeholder values with your own.
Copy
``` 
{
  "mcpServers": {
    "YOUR SERVER NAME HERE": 
  }
}
```
If any of your tools require authentication, you can add that to your config file. See the below example.
Copy
``` 
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization: Bearer $"
      ],
      "env": 
    }
  }
}
```
**Windows Users:**
Claude Desktop currently has a bug related to spaces inside of headers. To mitigate this, change the authentication section of your config file to look like the following:
Copy
``` 
        "Authorization:$"
      ],
      "env": {
        "AUTH_TOKEN": "Bearer YOUR AUTH TOKEN HERE"
```
You can add multiple entries if you have multiple MCP servers. See the below example.
Copy
``` 
{
  "mcpServers": {
    "xano_development": ,
    "xano_production": ,
    "xano_tools": 
  }
}
```
4
###  
Relaunch Claude Desktop to interact with your MCP server(s)
In Claude, you should see a new icon under your chat box with a [🛠️] icon.
You can click on this to view information about your available tools.
</div>
------------------------------------------------------------------------
Windsurf
<div>
1
###  
Head to your Windsurf settings
2
###  
Click Cascade, and then Add Server
3
###  
Click \'Add Custom Server\'
4
###  
Fill out the config file with your MCP server details
If the file is blank, start with the basic structure and replace the placeholder values with your own.
Copy
``` 
{
  "mcpServers": {
    "YOUR SERVER NAME HERE": 
  }
}
```
If any of your tools require authentication, you can add that to your config file. See the below example.
Copy
``` 
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization: Bearer $"
      ],
      "env": 
    }
  }
}
```
You can add multiple entries if you have multiple MCP servers. See the below example.
Copy
``` 
{
  "mcpServers": {
    "xano_development": ,
    "xano_production": ,
    "xano_tools": 
  }
}
```
5
###  
Click the Refresh button, and you should see your MCP server(s) available
</div>
------------------------------------------------------------------------
Methods
###  
Streaming
Streaming connections allow your MCP server to deliver responses in smaller chunks. Great for emulating the typical chatbot experience, where you can provide the experience of the response being \'typed\'.
###  
SSE
SSE connections may be more compatible with certain systems, but deliver the entire response as a whole once its ready, instead of in smaller pieces.
Which one should I use?
It depends on your use case and what you\'re using to connect to the MCP server. Streaming connections allow for a more organic, \"chatbot-like\" experience and means that your users won\'t have to wait as long to start seeing the response. However, whatever is connecting to your MCP server needs to support streaming responses for this to work.
------------------------------------------------------------------------
FAQ and Troubleshooting
####  
How do I use my MCP server in one of these clients?
Once you\'re connected following the instructions above, you should be able to converse with the AI like you would any other, asking real-world questions that the tools you built should be able to answer.
For example, if we have a tool that just returns a true or false, we\'d probably be asking yes or no questions, such as \"Does this user, [\[email protected\]](../../cdn-cgi/l/email-protection.html), have administrator access?\"
An example of using a Xano MCP server in Claude Desktop
####  
I can\'t connect to my server from my client of choice.
Check the error message you\'re receiving for clues. This could be due to one of the following:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    An incorrectly formatted configuration file
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Your Xano MCP Server is not set to allow connections
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You\'re not providing an authentication token to a server that requires it
    :::
####  
For MCP servers with tools that require authentication, after a long waiting period, I get a connection error.
In our current testing, we are finding that running multiple MCP clients causes this issue. Our recommendation is to stick with a single client for the time being.
Try these steps:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Close any open MCP clients
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Ensure that your authentication token is not expired
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    On Mac, run
    ::: 
    ::: 
    :::
    Copy
    ``` 
    rm -rf ~/.mcp-auth
    ```
    :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Restart your MCP client and try connecting again
    :::
Last updated 2 months ago
Was this helpful?

## Code Examples

```javascript
 
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization:$"
      ],
      "env": 
    }
  }
}

```

```javascript
 
{
  "mcpServers": {
    "xano_development": ,
    "xano_production": ,
    "xano_tools": 
  }
}

```

```javascript
 
{
  "mcpServers": {
    "YOUR SERVER NAME HERE": 
  }
}

```

```javascript
 
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization: Bearer $"
      ],
      "env": 
    }
  }
}

```

```javascript
 
        "Authorization:$"
      ],
      "env": {
        "AUTH_TOKEN": "Bearer YOUR AUTH TOKEN HERE"

```

```javascript
 
{
  "mcpServers": {
    "xano_development": ,
    "xano_production": ,
    "xano_tools": 
  }
}

```

```javascript
 
{
  "mcpServers": {
    "YOUR SERVER NAME HERE": 
  }
}

```

```javascript
 
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization: Bearer $"
      ],
      "env": 
    }
  }
}

```

```javascript
 
{
  "mcpServers": {
    "xano_development": ,
    "xano_production": ,
    "xano_tools": 
  }
}

```

```
 
    rm -rf ~/.mcp-auth
    
```

