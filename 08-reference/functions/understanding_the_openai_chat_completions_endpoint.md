---
category: functions
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- CRUD
title: Understanding the OpenAI Chat Completions Endpoint
---

# Understanding the OpenAI Chat Completions Endpoint

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: chatbots
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Chatbots \| Xano Documentation'
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
    Building a Chatbot with OpenAI/ChatGPT and Xano
Was this helpful?
Copy
1.  Building Backend Features
Chatbots 
========
[](https://www.xano.com/learn/introduction-to-building-with-llms-in-xano/)
 **Intro to LLMs in Xano**
[](chatbots.html#building-a-chatbot-with-openai-chatgpt-and-xano)
 **Build a Chatbot with ChatGPT & Xano**
------------------------------------------------------------------------
Building a Chatbot with OpenAI/ChatGPT and Xano
<div>
</div>
This guide will walk you through building a chatbot using ChatGPT and Xano.
Before we begin, it\'s important that you understand the following key concepts:
Database Basics
Building with Visual Development
APIs & Lambdas
User Authentication & User Data
You should know how to build a database table, build basic function stacks, work with user authentication, and utilize the External API Request function.
------------------------------------------------------------------------
<div>
1
###  
Understanding the OpenAI Chat Completions Endpoint
**Objective:** To create a chatbot, you\'ll primarily use OpenAI\'s chat completions API endpoint.
**Endpoint:** The specific endpoint is `/v1/chat/completions`. You\'ll make `POST` requests to this endpoint.
**Authentication:** All requests to the OpenAI API require authentication. This is done by including an `Authorization` header with a bearer token (your OpenAI API key).
**Request Body:**
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `model`: Specifies which OpenAI model to use (e.g., `gpt-3.5-turbo`). You can find compatible models in the OpenAI documentation.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `messages`: This is a crucial part. It\'s an *array* containing the *entire* conversation history. Unlike interacting directly with ChatGPT, the API requires you to send all previous messages in each request.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Message Object Structure**: Each object in the `messages` array needs a `role` and `content`:
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        `role`: Defines who sent the message.
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            `system`: Sets the initial context or persona for the chatbot (the first \"training\" prompt).
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            `user`: Represents messages sent by the end-user interacting with the bot.
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            `assistant`: Represents messages sent *by* the chatbot (responses from the API).
            :::
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        `content`: The actual text of the message.
        :::
    :::
**Benefits of Sending Full History:** This allows for fine-tuning or guiding the conversation by potentially modifying or constructing messages within the history you send to the API.
**Other Parameters:** There are optional parameters like `temperature`, but they aren\'t required to get started.
2
###  
Define Database Schema
**User Table:** Create at least one test user for authentication purposes later.
**Conversation Table (**`conversation`**)**: This acts as the parent table. Add the following fields:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `name` (Type: text): To easily identify conversations.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `model` (Type: text): To store which OpenAI model is used for this conversation (e.g., \"gpt-3.5-turbo\").
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `user_id` (Type: Table Reference -\> `user`): To link the conversation to the user who initiated it.
    :::
**Messages Table (**`messages`**)**: This stores individual messages. Add the following fields, mirroring the structure needed for the OpenAI API request:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `role` (Type: text): Stores \"system\", \"user\", or \"assistant\".
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `content` (Type: text): Stores the actual message text.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `index` (Type: integer): A number to track the order of messages within a conversation (0, 1, 2, \...). This is crucial for sorting messages correctly for display and for sending them in the right order to the API.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `conversation_id` (Type: Table Reference -\> `conversation`): To link the message back to its parent conversation.
    :::
3
###  
Create an endpoint to call OpenAI
**API Group:** Navigate to your API groups in Xano. You can use the default group or create a new one.
**New API Endpoint:** Add a new API endpoint. Choose \"Start from scratch\" or \"Custom\". Name it something descriptive, like `send_message_to_openai`.
**Inputs:** Define the necessary inputs for this endpoint. You\'ll likely need:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `conversation_id` (Input Type: Table Reference -\> `conversation`): To know which conversation this message belongs to.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    `user_message` (Input Type: text): The new message typed by the user.
    :::
**Function Stack:** This is where the logic happens using Xano\'s visual builder.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Get OpenAI API Key:** Securely retrieve your OpenAI API key. Store it in Xano\'s Environment Variables for security rather than hardcoding it.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Get Conversation History:**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Add a `Query All Records` step for the `messages` table.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Filter by the input `conversation_id`.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Sort** by the `index` field in ascending order. This ensures messages are retrieved chronologically.
        :::
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Add User\'s New Message to History (Temporary):** Add the incoming `user_message` to the list/array of messages retrieved in the previous step. Make sure it has the correct format: ``.
    :::
4.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Add External API Request:** This is the core step to call OpenAI.
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Click the \"+\" button in the function stack and select \"External API Request\".
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Import cURL:** Use the OpenAI documentation\'s cURL example for the chat completions endpoint. Copy the cURL command and use Xano\'s \"Import cURL\" feature. This will pre-fill most settings.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **URL:** Should be `https://api.openai.com/v1/chat/completions`.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Method:** `POST`.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Headers:**
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            Ensure `Content-Type` is `application/json`.
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            Add the `Authorization` header. The value should be `Bearer YOUR_API_KEY`, replacing `YOUR_API_KEY` dynamically using the environment variable retrieved in step 1. Use Xano\'s concatenation filters or sprintf for this.
            :::
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        **Parameters/Body:**
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            Set `model` to your desired model (e.g., \"gpt-3.5-turbo\"). You could make this dynamic based on the `conversation` record if needed.
            :::
        -   ::: 
            ::: 
            :::
            :::
            ::: 
            Set `messages` to the *full* conversation history array you prepared in step 3 (including the new user message).
            :::
        :::
    :::
5.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Process API Response:** The response from OpenAI will contain the assistant\'s reply. You\'ll typically find it in `response.result.choices[0].message.content`. Add steps to extract this content.
    :::
6.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Store Messages in Database:**
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Add a `Add Record` step for the `messages` table to save the *user\'s* new message. Include `conversation_id`, `role` (\"user\"), `content` (`user_message`), and the next `index` number.
        :::
    -   ::: 
        ::: 
        :::
        :::
        ::: 
        Add another `Add Record` step for the `messages` table to save the *assistant\'s* response. Include `conversation_id`, `role` (\"assistant\"), `content` (the extracted response), and the subsequent `index` number.
        :::
    :::
7.  ::: 
    ::: 
    :::
    :::
    ::: 
    **Response:** Define what the Xano API endpoint should return to your frontend (e.g., the assistant\'s message content, or the updated full conversation).
    :::
4
###  
Calling from a Frontend
Call the Xano API endpoint (`send_message_to_openai`) from your frontend application whenever a user sends a message.
Pass the `conversation_id` and the `user_message`.
Display the conversation history, potentially fetching it separately using the auto-generated Xano CRUD endpoints for the `messages` table, ensuring you sort by the `index` field.
</div>
Last updated 3 months ago
Was this helpful?