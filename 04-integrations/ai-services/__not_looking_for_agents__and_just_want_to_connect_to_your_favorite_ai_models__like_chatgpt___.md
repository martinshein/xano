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
title: '**Not looking for Agents, and just want to connect to your favorite AI models,
  like ChatGPT?**'
---

# **Not looking for Agents, and just want to connect to your favorite AI models, like ChatGPT?**

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
description: 'Agents are used to perform \''fuzzy logic\'', or perform workflows that require intricate decision making powered by an AI model'
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: agents
twitter:card: summary\_large\_image
twitter:description: 'Agents are used to perform \''fuzzy logic\'', or perform workflows that require intricate decision making powered by an AI model'
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Agents \| Xano Documentation'
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
    What are Agents?
Was this helpful?
Copy
1.  Build For AI
Agents 
======
Agents are used to perform \'fuzzy logic\', or perform workflows that require intricate decision making powered by an AI model
####  
**Not looking for Agents, and just want to connect to your favorite AI models, like ChatGPT?**
**Check out this resource instead:** Chatbots
Quick Summary
AI agents in Xano refer to autonomous entities designed to perform tasks by leveraging artificial intelligence. Your Xano Agents can integrate with your database, APIs, tasks, and functions, as well as external systems.
These agents can process data, make decisions, and execute actions without human intervention. AI agents in Xano can efficiently handle a variety of applications, from chatbots to data analysis tools, enhancing automation and productivity.
[](https://youtu.be/iEn20cy5LUw?feature=shared)
 **Introduction to AI Agents**
[](https://youtu.be/D1HtzC6yiO4)
 **Tools for Agents & MCP Servers**
<div>
</div>
What are Agents?
AI agents in Xano serve as integral components for building intelligent, automated systems as a part of your backend. These agents are designed to function autonomously, interacting with various elements of your app such as your APIs and database, as well as external systems, to streamline operations and enhance efficiency. AI agents can intelligently interpret inputs, process data, and deliver actionable outputs, all without the need for continuous human oversight.
Agents in Xano can leverage any of the most popular AI models once you provide an API key, such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    OpenAI
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Grok
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Anthropic / Claude
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Google Gemini
    :::
You can leverage the same visual builder you\'re used to using today to create workflows and functions that enable the agents to interact seamlessly with databases and external systems. With these foundational elements in place, AI agents can execute complex tasks, perform data analysis, or even serve as intelligent chatbots, making them versatile tools for a wide range of applications.
Building Agents in Xano
<div>
1
###  
From the left-hand navigation, click AI, then [ Agents ]
2
###  
Click [ + Add Agent ]
3
###  
Fill out the necessary information
Note
Please note that **not all models support certain features** such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Structured outputs
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Reasoning
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Tool calls
    :::
In addition, some models may support individual features, but not **combinations of features**, such as:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Structured outputs with tool calls
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Tool calls with reasoning
    :::
This is not an issue with Xano or with your agent builds --- this is dictated by the model you\'re using. If you encounter errors when testing your Agents, try using a different model and check to make sure that your model supports the feature(s) you have enabled, especially if you are using more than one of these features together.
Use the **Prompt Assistant** to help you build the best system prompts for your Agents!
[]
Parameter Name
Purpose
Example
Name
Give your agent a name that describes its role or primary function
Order Processing Agent
Description
Internal only field for describing what your agent does
Analyzes incoming orders, decides on fulfillment priority, and triggers shipping workflows
Agent Settings
Define dynamic inputs the Agent can accept from Function Stack workflows and reference environment variables
Configure placeholders with `{}` for workflow inputs, and `{}` for environment variables
Model Host
Select the AI model host for the agent
Anthropic (Claude)
OpenAI
Google Gemini
Max Steps
Define how many steps the Agent can execute to complete its task.
5
System Prompt
The core instructions that define your Agent\'s role, capabilities, and behavior
You are a helpful AI Agent that completes tasks accurately. When you need additional information to complete a task, use the available tools. Never make assumptions.
Prompt Type
The type of prompt that is being provided to the Agent. This can be either `messages`, which is a list of previous messages from another conversation, or `prompt`, which is just a standard prompt.
`messages` or `prompt`
Prompt
Additional context and instructions sent with each request
Please help the customer with their inquiry: {}. Their account ID is {}.
Structured Outputs
Configure your Agent to return responses in a specific JSON format using structured outputs and your predefined schema
Checkbox to enable/disable
Output Schema
Define the JSON structure for structured outputs
text, user\_email
Tags
Categories for organizing your Agents
contact, messaging
Request History
Controls logging of requests toRequest History
Inherit Settings: Uses workspace logging settings
Disabled: No logs recorded
Enabled: Logs requests with options for storage limits
4
###  
Add some tools to your Agent
An Agent needs tools to function --- the tools are essentially single functions that the Agent can perform, such as looking up user data or cancelling a subscription.
<div>
</div>
###  
Using Existing Function Stacks as Tools
<div>
1
####  
In the existing function stack, click the ⋮ settings icon in the upper-right corner of another function stack, and click [ Use As AI Tool ]
2
####  
Choose the Agent or MCP Server you\'d like to add the tool to, and give it a name. This name is what the command will be, so make sure it\'s understandable
3
####  
A new tool will be created in your chosen destination with a function to call the function stack
Xano will not make a copy of your existing function stack; instead, it will use a Run Endpoint function and call that function stack internally. This is ideal, so you only have to maintain one function stack.
A tool created from an existing API endpoint
4
####  
Head to your tool\'s settings and add instructions
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
        Enable or diffsable connection to this specific tool
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
Add the tool to an Agent or MCP Server
From the Agent or MCP Server, choose + Add Tool and select the tool you just created.
</div>
</div>
Running your Agent
Your Agents will be called as a part of another function stack using the **Call AI Agent** function.
<div>
1
###  
Add the Call AI Agent function to your function stack
2
###  
Select your Agent from the list
3
###  
Configure your Agent\'s arguments and options
In the `args` section, define a JSON object by typing `` into the box.
You can also just copy and paste an entire JSON object here to speed up the process, if you have that available.
Use the Set filter by clicking Set when hovering over the value box.
Set requires a key and a value --- the key is essentially \"this is the type of data\" and the value is the data itself. These are going to correspond to the arguments you defined when setting up your agent.
For example, if my system prompt looks like this:
`Please use the customer data here: {} to answer the customer question`
Your args would look like this, replacing the value with actual customer information.
In the `allow_tool_execution` section, you can decide whether or not this run should allow execution of any tools the agent has access to using a `true` or `false` value.
</div>
Structured Outputs
Structured Outputs are used for providing a specific format that you need your agent to return its result as. This is especially useful when you are calling agents from other agents and want to ensure that the output from Agent 1 is clear and easy to understand for Agent 2.
You can add structured outputs to your Agent in the settings by checking the Structured Outputs checkbox, and then clicking [ + Add Output Schema ] to build your output schema.
Example Agents
###  
[🤖] Customer Support Agent
**Purpose**
This Agent is designed to handle customer inquiries that don\'t typically need human interaction.
**Tools**
An Agent designed for this purpose might have the following tools available:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Get User Information**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Retrieves user information from the database
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Update User Information**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Retrieves existing user information from the database, and updates it per a user\'s request, such as changing their phone number or address
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Send Verification Code**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        This tool could be used as a secondary security measure to verify that the request is coming from the user that the data belongs to
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Change Subscription**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Based on the user\'s request, this could be used to stop an upcoming renewal, or cancel a subscription immediately. Because Agents excel at \'fuzzy logic\' depending on certain circumstances, this could also be used for things like churn prevention --- dynamically offering the user a discount to stay, for example
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Search Documentation**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Calls an external API from your chosen documentation platform to search your product documentation in an attempt to solve the user\'s query without human intervention
        :::
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Create Support Ticket**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        In the case that the Agent does not have the necessary tools to solve the user\'s concerns, create a support ticket for human intervention
        :::
    :::
###  
Agent Configuration
Parameter Name
Purpose
Example
Name
Give your agent a name that describes its role or primary function
Customer Support Agent
Description
Internal only field for describing what your agent does
Handles customer inquiries that don\'t typically need human interaction. Can retrieve user information, update accounts, send verification codes, manage subscriptions, search documentation, and escalate to human support when needed.
Agent Settings
Define dynamic inputs the Agent can accept from Function Stack workflows and reference environment variables
`{}`, `{}`, `{}`, `{}`
Model Host
Select the AI model host for the agent
Claude Sonnet 4
Max Steps
Define how many AI requests the Agent can execute to complete a task
8
System Prompt
The core instructions that define your Agent\'s role, capabilities, and behavior
You are a helpful Customer Support Agent that resolves customer inquiries efficiently. Always verify user identity before making account changes. Use available tools to gather information and resolve issues. If you cannot resolve an issue, create a support ticket for human intervention. Be polite, professional, and solution-oriented.
Prompt
Additional context and instructions sent with each request
Customer inquiry: `{}`. User ID: `{}`. Account status: `{}`. Please help resolve this customer\'s issue while following security protocols.
Structured Outputs
Configure your Agent to return responses in JSON format using structured outputs and your predefined schema
✅ Enabled
Output Schema
Define the JSON structure for agent responses
response\_message, action\_taken, ticket\_created, follow\_up\_required
Tags
Categories for organizing your Agents
customer-service, support, automation
Request History
Controls logging of tool requests
Enabled: Logs requests with options for storage limits
###  
Example Interaction Flowcharts
####  
1\. Account Information Request
*\"What\'s my current subscription plan?\"*
####  
2\. Address Change Request
*\"I need to update my shipping address\"*
####  
3\. Billing Question
*\"Why was I charged twice this month?\"*
####  
4\. Technical Issue
*\"The app keeps crashing on my phone\"*
Last updated 21 minutes ago
Was this helpful?