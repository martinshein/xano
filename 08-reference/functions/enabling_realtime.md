---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Enabling Realtime
---

# Enabling Realtime

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'realtime-in-xano'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Realtime in Xano \| Xano Documentation'
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
    What is Realtime?
Was this helpful?
Copy
1.  Realtime
Realtime in Xano 
================
What is Realtime?
<div>
</div>
Realtime can be defined as anything that enables your application to provide live updates inside of your application. Think of something like a chat window, where volume of interactions can be high, and it doesn\'t really make sense to constantly ping an API for new updates. Realtime enables an always-open connection, and in combination with our Javascript SDK or other frontend integration, can easily be enabled in your applications that use Xano as a backend.
Behind the scenes, Realtime connections are powered by a Websocket server to maintain connections. It can enable you to build dynamic and responsive functions for your website or application, such as a real-time chat, collaboration, or instant in-app notifications.
Realtime can also refer to database triggers, which is logic that can run immediately when something changes in a database table. For more information on triggers, see this section of our documentation.
How does Realtime work in Xano?
When your client (user or application) connects to a Realtime **channel** in your backend, it will start *listening* for new messages. A **channel** is just a way to segregate messages into \'sections\'; similar to having separate chat threads with different people, each thread would have its own channel.
A **message** can be anything you want, from plain text to complex JSON. To keep things easy to understand, the instructions below will be using plain text messages.
In this example, we have a **channel** for a \'Marvel Chat Room\'. All of our users are connected to this chat room. Anytime someone sends a message, it will appear for every user connected. Functionally, this means that if Jill sends (or **broadcasts**) a new message, John and Jack will receive it, but Jill will also receive the message back; this makes it super simple to ensure that the view across all clients remains in sync.
Realtime allows you to use as many **channels** as you want. If we were to open a new channel, a \'DC Chat Room\', and Jack joins both of them, he will be able to send and receive messages in both channels. John will not be able to interact with the DC chat room until he joins the channel; same with Jill and the Marvel chat room.
How do I use Realtime?
###  
Enabling Realtime
If you haven\'t done so already, you\'ll need to enable Realtime at the workspace level. From your workspace dashboard, open the menu in the top-right corner, choose Realtime Settings, change the dropdown to Yes, and then click Save.
If this is the first workspace to have Realtime enabled in your instance (even if you\'ve had it enabled and then disabled it previously), Xano will need to provision the additional resources required for Realtime to function. This should only take a few minutes to complete, and you can check progress from the Realtime Settings panel.
After Realtime is enabled, you\'ll need to define some channel permissions. For a deep dive into how channel permissions work, see this section of our documentation.
###  
Implementation using the Xano SDK
We\'ve made using Xano Realtime as easy as possible to build into your application by integrating it into our Xano SDK.
**Access the Xano SDK** **here****.**
If you aren\'t familiar with Javascript, **that\'s okay**. We hope to have more direct integrations with your favorite frontends in the near future. Each code snippet is broken down into a special **Code Explanation** section to help you understand what\'s going on.
To get started, import the SDK to your project by\...
**Using our HTML import (best for beginners)**
Copy
``` 
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@xano/js-sdk@latest/dist/xano.min.js"></script>
```
**Using NPM**
Copy
``` 
npm install @xano/js-sdk
```
Next, you\'ll need to collect the following information:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    An instance base URL, which you can find anywhere when logged into Xano.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    The **realtime connection hash**, which is located in your Realtime Settings panel.
    :::
We need to initialize a new xanoClient, using the following Javascript.
If you are already initializing the SDK for other purposes, just add the `realtimeConnectionHash` parameter. You do not need to specify instanceBaseUrl if you are providing an API group base URL.
Copy
``` 
const xanoClient = new XanoClient();
```
Code Explanation
Copy
``` 
const xanoClient = new XanoClient
```
This defines a new variable called xanoClient. The value for this variable is \"new XanoClient\", which calls the SDK to tell it we\'re establishing a connection to Xano.
The ({ lets the code know that we are going to send some parameters to the SDK along with our request to establish a connection.
Copy
``` 
  instanceBaseURL: "http://abc1-def2-ghi3.xano.io/",
  realtimeConnectionHash: "a1b2c3d4e5f6g7h8i9",
});
```
This is the instance URL and our realtime connection hash that we are using to establish our connection.
We also need to define a channel for our messages to live in.
Copy
``` 
const marvelChannel = xanoClient.channel("marvel-chat-room");
```
Code Explanation
Copy
``` 
const marvelChannel = this.xanoClient.channel("marvel-chat-room");
```
Just like before, we\'re defining a new variable, this time called **marvelChannel** with `const marvelChannel`
For the value, we are referencing `this.xanoClient`. \'this\' refers to the **global object**. Without getting into too much detail, the global object can just be thought of as the entirety of your Javascript code. `channel("marvel-chat-room");` just defines the channel name.
Now that you have initialized your Xano SDK and defined a channel, we can listening for new messages.
Copy
``` 
marvelChannel.on((message) => {
  switch (message.action) 
});
```
**Code Explanation**
Copy
``` 
marvelChannel.on((message) => {
```
We previously defined our `marvelChannel`, so now we can issue commands to it. In this case, the \'`on`\' command just tells the SDK \"I\'m ready to listen for messages; whenever there is a message, run the code inside the `` brackets.
Copy
``` 
 switch (message.action) {
```
`Switch` starts a decision-making process (kind of like our If/Then statements) based on the contents of the command received.
Copy
``` 
  case 'message':
      messageReceived(message.payload);
      break;
```
We\'re now telling our `switch` command \"When you see `[Realtime] Message` sent to you, call a function called `messageReceived` with the message contents from `message.payload` and then stop (`break`). Don\'t worry, we haven\'t gone over messageReceived yet, so it\'s okay if that seems strange. This would be the function that your frontend uses to actually display the message, so it will vary based on your specific application.
Copy
``` 
    default:
      console.info(message);
  }
});
```
This last piece tells our `switch` command \"If the message is anything else but `[Realtime] Message`, do this instead. In this case, \'this\' is just logging the message so we can review it in our browser\'s Developer Console.
So far, we\'ve enabled the Xano SDK, set up our Marvel channel, and implemented a function to listen for new messages. The last piece is to add a function to send new messages to the channel.
Copy
``` 
marvelChannel.message("Hello World!");
```
Code Explanation
Copy
``` 
marvelChannel.message("Hello World!");
```
In this code snippet, we\'re talking to our marvelChannel, and sending a message of Hello World!
With that, we\'re ready to start building Realtime into our front-end! View and play with a completed example below.
Be aware that the demo code below assumes you have a channel called **marvel-chat-room** defined in your channel permissions. If you\'d like to use a different channel name, find this line:
Copy
``` 
 const marvelChannel = xanoClient.channel('marvel-chat-room');
```
and update \"marvel-chat-room\" to your channel name.
**Instructions:**
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click here to open the demo in a new tab.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Fill in your API group base URL and Connection Hash.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    Click \'Submit\'.
    :::
To achieve the maximum effect, duplicate the tab and have a little chat with yourself!
Xano Auth + Realtime
To authenticate your users with channels that require authentication, you will use your `xanoClient` as usual. The client will automatically authenticate if the `realtimeAuthToken` setting is set.
After your `xanoClient` is defined, perform an API request to your login or signup endpoint and store the returned auth token using the setRealtimeAuthToken command.
You can generate separate auth tokens when your users log in, sign up, or otherwise are ready to initiate a connection to Realtime.
Copy
``` 
xanoClient.setRealtimeAuthToken(authToken);
```
Previously, this was accomplished with setAuthToken, and will continue to function as such until **July 1, 2024**. On that date, it will become **required** to use setRealtimeAuthToken instead to authenticate a realtime connection. If you don\'t need separate tokens, you can just supply the same auth token for both values.
Message Types
The realtime connection has several different message types that can be sent, and you can modify your custom code to react differently to each message type.
Status
Meaning
connection\_status
Informs the status of the connection to your Realtime server. This appears in your console log when initiating a connection to a channel.
error
An error has occurred connecting to or interacting with Realtime. Check your console log for more details.
event
An event is anything beyond a standard realtime message, and can be used to enable dynamic handling of different data being sent through Realtime
join
Sent when joining a channel
leave
Sent when leaving a channel
message
A new message has been received
presence\_full
A full list of all clients connected to the channel
presence\_update
Sent when a new client joins or leaves the channel
Message History
When setting up your Realtime channels, you have the option of storing message history as well.
Message history for your channels is backed by Redis cache, and it\'s important to consider how else you are using caching, if at all, when determining how much data to hold on to.
Message history can store up to 100 messages per channel, and can be returned to clients with the following:
Copy
``` 
channel.history();
channel.on('history', function(action) );
```
Common Issues & FAQ
I can\'t send or receive messages using Realtime
Check your browser\'s Javascript console for the following output:
[]
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    If you do not see this message at all, there is a problem with your implementation of the SDK or the realtime integration you are using. Check your code and reference our documentation on connecting with the SDK to find out more, or reach out to your frontend support for more information if it uses a direct integration.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    If you see this message, but it does not say \'connected\', check your instance base URL, api group base URL, or connection hash to ensure it is accurate.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    If you see this message and it says connected, but you aren\'t seeing your messages send or receive, make sure your frontend is handling rendering your messages properly. **Hint:** Add a console.log(message) to ensure that the messages are working properly before trying to address the frontend.
    :::
When my users refresh their app or page, previous messages have disappeared
Realtime does not keep message history, and would require a custom implementation such as one that utilizes our Realtime Event function or Realtime Triggers.
What is the performance impact of Realtime on the rest of my backend?
Realtime uses dedicated resources for connections and message handling. This means that ultimately, realtime usage would not impact any other area of your backend such as APIs and background tasks.
However, it is important to note the following:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    A mass of connections to Realtime beyond what your instance can handle can cause issues.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Realtime resources scale with each plan upgrade just like other resources. Depending on your Realtime needs, it may necessitate an upgrade to your Xano subscription to utilize effectively.
    :::
Some strategies you can use to manage connections are:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Being strict about what data you use Realtime to deliver vs your APIs
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Timing out connections after a certain period of inactivity by sending a Leave event from your front-end
    :::
Last updated 5 months ago
Was this helpful?

## Code Examples

```
 
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@xano/js-sdk@latest/dist/xano.min.js"></script>

```

```
 
npm install @xano/js-sdk

```

```
 
const xanoClient = new XanoClient();

```

```
 
const xanoClient = new XanoClient

```

```
 
  instanceBaseURL: "http://abc1-def2-ghi3.xano.io/",
  realtimeConnectionHash: "a1b2c3d4e5f6g7h8i9",
});

```

```
 
const marvelChannel = xanoClient.channel("marvel-chat-room");

```

```
 
const marvelChannel = this.xanoClient.channel("marvel-chat-room");

```

```javascript
 
marvelChannel.on((message) => {
  switch (message.action) 
});

```

```javascript
 
marvelChannel.on((message) => {

```

```javascript
 
 switch (message.action) {

```

```
 
  case 'message':
      messageReceived(message.payload);
      break;

```

```
 
    default:
      console.info(message);
  }
});

```

```
 
marvelChannel.message("Hello World!");

```

```
 
marvelChannel.message("Hello World!");

```

```
 
 const marvelChannel = xanoClient.channel('marvel-chat-room');

```

```
 
xanoClient.setRealtimeAuthToken(authToken);

```

```javascript
 
channel.history();
channel.on('history', function(action) );

```

