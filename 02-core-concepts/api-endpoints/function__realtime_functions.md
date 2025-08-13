---
category: api-endpoints
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: 'Function: Realtime Functions'
---

# Function: Realtime Functions

[](../../../index.html)
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
    Using the Realtime Event Function
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../../building-with-visual-development.html)
2.  Functions
3.  APIs & Lambdas
Realtime Functions 
==================
While Realtime is fully functional without implementing anything in your function stacks, you may find yourself wanting to build function stacks to extend the functionality of Realtime.
This is possible with the new **Realtime Event** function, located under APIs & Lambdas in the function panel.
###  
Using the Realtime Event Function
This function sends a message of type \'event\' to the channel specified. Remember, a message can be anything from plain text to a JSON object for even further flexibility.
**Channel** - The channel to send the event to
**Data** - The payload of the event
**Database** - If this channel requires authentication, select the corresponding database that handles your authentication here
You can use variables for Channel and Data to make the event behave dynamically.
Please note that Event is different than Message, and will need to be handled accordingly by your frontend.
###  
Example
Realtime connections do not log message history. This means that once a user leaves our Marvel chat room, if they come back, they won\'t be able to see any of the previous messages. So, we want to store our messages in a database table as they are sent to the channel.
We could approach this in a couple of different ways.
1.  ::: 
    ::: 
    :::
    :::
    ::: 
    Have our frontend send an API request at the same time a message is sent to the channel to log the message.
    :::
2.  ::: 
    ::: 
    :::
    :::
    ::: 
    Have our frontend only send an API request, and our API can handle delivering the message once it is stored.
    :::
For this example, we will use the second option. We need to first modify our frontend code to send the API request, instead of sending the message directly to the channel. We\'ll do this by defining a new function and then calling it when our button is clicked.
Copy
``` 
function sendMessageToRealtime(channel, message) {
        fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: ,
        body: JSON.stringify()
  });
}
document.getElementById('form').addEventListener('submit', (event) => );
```
**Code Explanation**
First, we define the function and make sure we define two parameters: channel for the channel to send the message to, and message for the message body.
Copy
``` 
function sendMessageToRealtime(channel, message) {
```
After that, we\'re using fetch, a Javascript function to send API requests, to our endpoint. We don\'t need to worry much about the technical details here if you aren\'t comfortable, but you may need to change the method and/or add new parameters to the body of the request depending on your use case. For this example, all our API needs is that channel name and message.
Copy
``` 
fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: ,
        body: JSON.stringify()
  });
```
Now, we need to handle what happens when our Send button is clicked. We\'ll start by looking for that element and adding an event listener to it. It just looks for our form, which has an ID of form, and a submit button inside of it.
Copy
``` 
document.getElementById('form').addEventListener('submit', (event) => {
```
We\'ll add a line to ensure that no \'default\' behavior occurs when a user clicks the send button.
Copy
``` 
event.preventDefault();
```
Next, we\'ll call our sendMessageToRealtime function and give it our \'marvel-chat-room\' channel name and the value of the message input box. Right after that, we clear the input to prepare for the next message.
Copy
``` 
sendMessageToRealtime('marvel_chat_room', document.getElementById(event.target.message.value))
event.target.message.value = '';
```
We need to set up a database table to log the messages.
Here\'s the API endpoint we are sending these requests to.
This endpoint takes in the channel name and message data, fires our Realtime Event function, and then stores the message in the database table.
At this point, we have modified our frontend code and set up the API in Xano to handle the requests. Now, when our users send messages, they will be logged in the database table, and we still get all of the benefits of utilizing the realtime connection.
Last updated 6 months ago
Was this helpful?

## Code Examples

```javascript
 
function sendMessageToRealtime(channel, message) {
        fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: ,
        body: JSON.stringify()
  });
}
document.getElementById('form').addEventListener('submit', (event) => );

```

```javascript
 
function sendMessageToRealtime(channel, message) {

```

```javascript
 
fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: ,
        body: JSON.stringify()
  });

```

```javascript
 
document.getElementById('form').addEventListener('submit', (event) => {

```

```
 
event.preventDefault();

```

```
 
sendMessageToRealtime('marvel_chat_room', document.getElementById(event.target.message.value))
event.target.message.value = '';

```

