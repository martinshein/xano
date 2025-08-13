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
title: View the sample Webflow project here
---

# View the sample Webflow project here

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'realtime-in-webflow'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'Realtime in Webflow \| Xano Documentation'
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
    Getting Started
Was this helpful?
Copy
1.  Realtime
Realtime in Webflow 
===================
**Realtime is in beta, and this documentation can change at any time.**
Getting Started
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Make sure you\'ve reviewed the Realtime documentation here, as it is helpful to understand the process and how to use the Xano SDK before continuing.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    You need to be comfortable adding and modifying custom code in your Webflow project.
    :::
Building a Live Chat in Webflow (Example)
Head to your Site Settings.
In the Custom Code section, paste the following line of code. This loads the Xano SDK and enables us to use it in the rest of our project. It also defines our \'xanoClient\', which we\'ll call in our separate pages to enable Realtime functionality. Make sure to place your API group base URL and realtime connection hash in the appropriate places, and click Save.
If you prefer, you can change the variable name `const ``xanoClient` to something else. Please note that any of our examples here will continue to use `xanoClient`, and you\'ll need to update them accordingly.
Copy
``` 
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@xano/js-sdk@latest/dist/xano.min.js"></script>
<script type="text/javascript">
  const xanoClient = new XanoClient();
</script>
```
At this point, Webflow will ask you to publish your site to see the changes. Please note that you may need to view a published version of the site to verify that Realtime is enabled and working as expected.
Head back to the Designer, and we can start building realtime functionality into our project.
For this example, we\'ve set up a simple chat application, similar to the example prepared in the main Realtime documentation.
We know that we want this page to connect to a specific channel, so let\'s head to our page settings and add some custom code.
Copy
``` 
<script type="text/javascript">
const marvelChannel = xanoClient.channel("marvel-chat-room");
marvelChannel.on((message) => {
  switch (message.action) 
});
</script>
```
Please note that when it comes to how you want to handle realtime implementation for your specific project, your custom code and configuration may look vastly different. The code provided in this section is for demonstration purposes only.
Typically when performing an action like this in Webflow, it follows a basic structure, where we\...
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Create an element on our page to serve as a template, and assign it a class.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Once you have styled the element to your liking, give it a subclass. Change the properties of the subclass to set Display to None.
    :::
3.  ::: 
    ::: 
    :::
    :::
    ::: 
    In your custom code, when it\'s time to render a message, you\'ll need to generate a copy of the original element containing the message or other content to show.
    :::
This piece of code, placed in the \'before \</body\> tag\' section, tells the page that we want to connect to the marvel-chat-room channel and listen for messages. Any time we receive a new message, we want to execute another function called messageReceived, which will handle rendering the new message on the page.
Now that we\'ve set up actually connecting to the realtime server, we can start working with our messages. This is an example code snippet that lives right above our \</body\> tag to render new messages on the page.
Copy
``` 
function messageReceived(payload) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
  const messageText = document.createElement("div");
  messageText.classList.add("message-text");
  messageText.textContent = payload;
  messageDiv.appendChild(messageText);
  messageDiv.style.display = 'block';
  const chatboxes = document.getElementsByClassName("chatbox");
  for (const chatbox of chatboxes) 
}
```
**Code Explanation**
In this code, we start by defining our function and the data it needs to run.
Copy
``` 
function messageReceived(payload) {
```
We then define a couple of variables, messageDiv and messageText, targeting newly created div elements to contain our message. We\'re also applying some styling to the message block to make sure it displays.
Copy
``` 
const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
const messageText = document.createElement("div");
  messageText.classList.add("message-text");
  messageText.textContent = payload;
  messageDiv.appendChild(messageText);
  messageDiv.style.display = 'block';
```
In the final section, we look for the element on our page with the class of \'chatbox\' and place the new div inside of it.
Copy
``` 
const chatboxes = document.getElementsByClassName("chatbox");
  for (const chatbox of chatboxes) 
}
```
We\'re almost there. The last thing we need to do is add the ability to send new messages.
Copy
``` 
function sendMessage() 
    document.getElementById("sendButton").addEventListener("click", sendMessage);
```
Code Explanation
First, we define a new function called sendMessage that is triggered every time we need to send a new message to the channel.
Copy
``` 
function sendMessage() {
```
Inside of this function, we define our message as the value of our input.
Copy
``` 
const message = document.getElementById("messageInput").value;
```
We can then send our message to the channel, and then clear the input value to prepare for a new message.
Copy
``` 
     marvelChannel.message(message);
      document.getElementById("messageInput").value = "";
    }
```
The last line of the code adds an event listener to our sendButton. This makes sure that every time the button is clicked, the function is executed.
Copy
``` 
  document.getElementById("sendButton").addEventListener("click", sendMessage);
```
And with that, you\'ve just built live chat in your Webflow site. Publish your changes and check it out!
###  
View the sample Webflow project here
.
You\'ll want to clone this project so you can fill in your API group base URL and connection hash in the site settings.
Last updated 6 months ago
Was this helpful?

## Code Examples

```
 
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@xano/js-sdk@latest/dist/xano.min.js"></script>
<script type="text/javascript">
  const xanoClient = new XanoClient();
</script>

```

```javascript
 
<script type="text/javascript">
const marvelChannel = xanoClient.channel("marvel-chat-room");
marvelChannel.on((message) => {
  switch (message.action) 
});
</script>

```

```javascript
 
function messageReceived(payload) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
  const messageText = document.createElement("div");
  messageText.classList.add("message-text");
  messageText.textContent = payload;
  messageDiv.appendChild(messageText);
  messageDiv.style.display = 'block';
  const chatboxes = document.getElementsByClassName("chatbox");
  for (const chatbox of chatboxes) 
}

```

```javascript
 
function messageReceived(payload) {

```

```
 
const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
const messageText = document.createElement("div");
  messageText.classList.add("message-text");
  messageText.textContent = payload;
  messageDiv.appendChild(messageText);
  messageDiv.style.display = 'block';

```

```
 
const chatboxes = document.getElementsByClassName("chatbox");
  for (const chatbox of chatboxes) 
}

```

```javascript
 
function sendMessage() 
    document.getElementById("sendButton").addEventListener("click", sendMessage);

```

```javascript
 
function sendMessage() {

```

```
 
const message = document.getElementById("messageInput").value;

```

```
 
     marvelChannel.message(message);
      document.getElementById("messageInput").value = "";
    }

```

```
 
  document.getElementById("sendButton").addEventListener("click", sendMessage);

```

