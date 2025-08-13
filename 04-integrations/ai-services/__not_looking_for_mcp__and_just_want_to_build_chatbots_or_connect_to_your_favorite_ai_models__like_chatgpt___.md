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
title: '**Not looking for MCP, and just want to build chatbots or connect to your
  favorite AI models, like ChatGPT?**'
---

# **Not looking for MCP, and just want to build chatbots or connect to your favorite AI models, like ChatGPT?**

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'mcp-builder'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'MCP Builder \| Xano Documentation'
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
    Introduction to building MCP Servers in Xano
Was this helpful?
Copy
1.  Build For AI
MCP Builder 
===========
####  
**Not looking for MCP, and just want to build chatbots or connect to your favorite AI models, like ChatGPT?**
**Check out this resource instead:** Chatbots
Quick Summary
**MCP** stands for Model Context Protocol, and is essentially a standardized way for AI models (also referred to as Large Language Models, or LLMs) to interact with other services.
Think about the typical flow every time you interact with an AI. You, the **user**, utilize a **client**, like ChatGPT, to send instructions or ask questions to an **LLM**. The client is responsible for taking your input and transforming it into a way that the LLM you\'re interacting with can understand.
With MCP in the mix, clients are able to take your input, and instruct an LLM on how to interact with *other* services and tools, like your Xano database, for example. Each separate task that is exposed to the client via the MCP standard is called a **tool**.
Xano\'s **MCP Builder** feature allows you to build tools just like you build any other function stack and expose them to any client that supports the MCP standard, opening up the opportunity to build for AI, using the power of visual development in Xano.
[](https://youtu.be/VQGjbBBY96s)
 **Introduction to MCP**
[](https://youtu.be/5-K4nCW1YHE)
 **Build an MCP Server in 10min or Less**
[](https://youtu.be/D1HtzC6yiO4)
 **MCP Tools and Functions**
[](https://youtu.be/5M6Qx6-rcbo)
 **Building an MCP Server & Client**
Introduction to building MCP Servers in Xano
MCP stands for **Model Context Protocol**.
At its core, MCP is a standardized framework that enables seamless communication and interaction between AI models (especially Large Language Models, or LLMs) and external services. Think of it as a universal language and set of rules that allows AI models to go beyond their internal knowledge and capabilities by intelligently leveraging external data sources, tools, and functionalities.
Traditionally, interacting with external services from an AI model required complex and often proprietary integrations built into specific clients. MCP simplifies this by providing a consistent and structured way for client applications to describe available tools and instruct AI models on how to use them. This includes defining the tool\'s purpose, its input parameters, and how the AI model can expect to receive results.
###  
Get Started
Jump right to the section you\'re looking for, or keep scrolling to learn more!
[Creating an MCP Server]
[Creating MCP Tools]
Why would I build MCP Servers in Xano?
Building MCP Servers in Xano offers a fundamental shift in how you integrate AI capabilities into your applications. Instead of being limited to building traditional REST APIs for standard web or mobile interactions, Xano\'s MCP Builder empowers you to create **AI-native functionalities**.
You can build function stacks in Xano specifically designed to be used by AI models. This means that you can create tools for your AI to:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Retrieve specific data from your Xano database based on natural language queries
    ::: 
    ::: 
    :::
    :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Perform complex data manipulations and calculations triggered by AI insights
    ::: 
    ::: 
    :::
    :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Write data back to your Xano database based on AI-driven decisions or user requests interpreted by the AI
    ::: 
    ::: 
    :::
    :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Interact with other external APIs and services through your Xano function stacks, orchestrated by the AI
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Interact with your own APIs and services you\'ve already built in Xano through the AI
    :::
What\'s supported with Xano\'s MCP Builder?
We have built our current MCP support using the SSE transport method. Only tools are available at this time.
You can use any available function we have today in your MCP servers.
As MCP is an evolving protocol, we aim to continue to expand the functionality as it develops. If you are utilizing MCP in Xano and have any feedback or questions, please reach out to our support team.
------------------------------------------------------------------------
Getting Started with MCP Builder
###  
First, create an MCP Server.
To build MCP servers in Xano, we\'ll first need to create a server that will house some tools.
<div>
1
###  
From the left-hand navigation menu, click [ AI Tools ]
2
###  
Click [ + Add MCP Server ] to create your first MCP server
3
###  
Fill out the necessary information
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Name**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Give your server a name that clearly indicates its purpose.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Description**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        This is an internal field just for you to expand on the purpose of the MCP server.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Allow Connections**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Choose whether or not to allow connections to this MCP server
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Add Tag**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Tag your MCP servers for easier search throughout your Xano workspace.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **MCP Instructions**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        These instructions are what your clients will look at to understand the purpose of the MCP server. Markdown format is recommended for easy readability for your LLMs and clients. These instructions apply to the server as a whole, and are not used for individual tool instructions.
        :::
    :::
</div>
###  
After you\'ve created a server, add some tools.
What is a tool?
Tools are essentially individual actions that your MCP server can perform, such as querying a database, adding new records, or calling an external API. You\'ll build tools just like you build any other function stack.
###  
Using Existing Function Stacks as Tools
<div>
1
####  
In the existing function stack, click the ⋮ settings icon in the upper-right corner and click [Use As AI Tool]
2
####  
Choose the MCP Server you\'d like to add the tool to, and give it a name. This name is what the command will be, so make sure it\'s understandable
3
####  
Navigate to your MCP Server and check for the newly created tool
Xano will not make a copy of your existing function stack; instead, it will use a Run Endpoint function and call that API internally. This is ideal so you only have to maintain one function stack.
A tool created from an existing API endpoint
4
####  
Adjust the settings for your newly created tool and add instructions
Instructions are important to have so the AI models and clients interacting with this tool understand how to use it.
</div>
###  
Creating Tools from Scratch
<div>
1
####  
From the left-hand navigation menu, click Tools, then [ + Add Tool ]
2
####  
Fill out the required information
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Name**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Give your tool a recognizable name. This is also the command that will be used to execute your tool.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Description**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        This is an internal-only field just for you to describe the purpose of the tool.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Allow Connections**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Enable or disable connection to this specific tool
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Add Tag**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Tag your tools for easier search across your Xano workspace
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Authentication**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Determine if this tool requires an authentication token
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Tool Instructions**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        These instructions are what your clients will use to understand how to send requests to the tool, and what the expected result will be. Markdown format is recommended.
        :::
    :::
3
####  
Build your tool\'s function stack
If you haven\'t already, make sure you\'re familiar with Building with Visual Development
4
####  
When you\'re ready, publish your changes
</div>
------------------------------------------------------------------------
MCP Authentication
Before you continue
It\'s important to understand that MCP is an evolving protocol. Authentication methods and best practices are in flux and may change. The best course of action right now for per-user authentication is to build a custom client that can authenticate your users.
Your MCP tools can have authentication enabled. The method of authentication is a bearer token, similar to the secure APIs you\'re already building in Xano. You\'ll include a valid token inside of your client\'s configuration (if you\'re using a ready-made client such as Claude Desktop or Cursor), and it will send that token along with your requests.
If you are building a publicly available application with its own user base, and need to make sure that your tools work across your set of users and separates data properly, you\'ll need to serve your own client that can handle dynamic authentication.
Our end-to-end MCP Server tutorial walks you through one example of building your own server and client, both using Xano.
<div>
</div>
------------------------------------------------------------------------
MCP Variables
When working with data as part of an MCP tool function stack, you have access to two special variables.
####  
token
The Token variable contains a token that is passed as part of the connection URL. This token can be used for building custom authentication, or any other purpose that you see fit.
`https://your-xano-instance.xano.io/x2/mcp/67Dx5RNL/``token_here``/sse`
####  
params
You can also pass URL parameters as a part of your connection URL, such as `?beta=true`
`https://yourxano.stage.xano.io/x2/mcp/67Dx5RNL/token_here/sse``?beta=true&param=here`
You can use the URL parameters in your tool function stacks to determine the behavior of the tool(s).
Hint
Use the token and / or params in combination with Triggers for building powerful and complex MCP logic.
Connecting to your MCP Server
Now that you\'ve built an MCP server and added some tools to it, you can connect with your client of choice. Choose from the list below for a quick getting started guide.
If you\'re new to MCP servers, we recommend starting with Cursor.
####  
 Cursor
####  
 Claude Desktop
------------------------------------------------------------------------
Best Practices & FAQs
There are some best practices when building tools that we recommend following for the best experience.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Use** **enum inputs** **wherever possible** so the AI model understands what options are available for your inputs.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Use **clear naming conventions** and instructions.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Try to find a balance when writing instructions** between being clear and descriptive, but also concise. Reducing the amount of tokens sent to an AI model will reduce token cost, improve speed, and improve responses.
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Use error handling with clear error messages**. If an AI model fails to use a tool, clear error messages will allow it to retry the tool successfully.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **What are the benefits of using MCP?**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Standardization:** MCP provides a common way for different applications and LLMs to interact, reducing the need for custom integrations.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Interoperability:** MCP enables different LLMs and applications to work together more easily.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Flexibility:** MCP allows developers to connect LLMs to a wide range of external resources.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Efficiency:** MCP streamlines the process of building AI agents and applications.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Is MCP tied to a specific LLM or platform?**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        No, MCP is designed to be an open and vendor-neutral protocol, allowing it to be used with various LLMs and platforms.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **How does MCP relate to APIs?**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        While APIs provide access to specific functions, MCP provides a standardized way for LLMs to discover and use those functions in a context-aware manner.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **What is the role of \"context\" in MCP?**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Context is crucial in MCP. It provides the LLM with the necessary information about the user\'s request, the available tools, and the overall environment, enabling the LLM to make more informed decisions.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **How is security handled in MCP?**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        MCP emphasizes secure communication between clients and servers. Mechanisms like authentication, authorization, and secure data transfer are important considerations in MCP implementations.
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Can I build multiple MCP servers?**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Yes, in Xano you can build multiple MCP servers and they can all have their own tools available.
        :::
    :::
Last updated 1 month ago
Was this helpful?