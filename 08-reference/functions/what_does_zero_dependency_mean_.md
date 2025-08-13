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
title: What does zero dependency mean?
---

# What does zero dependency mean?

apple-mobile-web-app-status-bar-style: black
apple-mobile-web-app-title: Xano Documentation
color-scheme: dark light
generator: GitBook (28f7fba)
lang: en
mobile-web-app-capable: yes
robots: 'index, follow'
title: 'what-are-actions'
twitter:card: summary\_large\_image
twitter:image: 'https://docs.xano.com/\~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fsocialpreview%252FB4Ck16bnUcYEeDgEY62Y%252Fxano\_docs.png%3Falt%3Dmedia%26token%3D2979b9da-f20a-450a-9f22-10bf085a0715&width=1200&height=630&sign=550fee9a&sv=2'
twitter:title: 'What are Actions? \| Xano Documentation'
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
    What does zero dependency mean?
Was this helpful?
Copy
1.  Xano Actions
What are Actions? 
=================
<div>
</div>
A Xano Action is a powerful, zero-dependency function that anyone can create, share, fork (create new versions), and install. Actions can be previewed, tested, and edited in Run mode outside of a Xano instance, meaning they do not require an account for testing and trying them out.
Actions are a lightweight version of the Xano function stack designed for specific processes such as integrations with external APIs or business logic executions. They are similar to custom functions, but without dependencies and shareable to anyone.
Discover Actions on xano.com/actions. Browse Actions created by the Xano team or other community members. Clicking on an Action allows you to:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Run & Debug** the Action.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Make edits** to the Action.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Clone**: Make a copy of the Action, change whatever you\'d like, and publish a new (separate) version of the Action.
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Add** the Action into your workspace to be used in any function stack.
    :::
###  
What does zero dependency mean?
Actions are designed not to contain dependencies to support more seamless integration to existing Xano workspaces and function stacks. Additionally, it promotes easy shareability for anyone, regardless of if they\'re a Xano user, to interact with Actions.
Zero-dependency means Actions do not contain:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Database request functions or database tables
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Middleware
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Environment variables\*
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Lambdas
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Redis caching
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Multiple Xano objects
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Docker Microservices
    :::
*\*Settings registry is available for actions for API keys and other sensitive tokens or keys.*
###  
Browsing and Using Actions
<div>
1
###  
From the left-hand navigation menu, click Actions
2
###  
Browse for and add new actions from here, or at xano.com/actions
3
###  
From any function stack, under the Actions category, you\'ll see your installed actions available for use
</div>
###  
Creating an Action
Click [**+ Create Action** ]to begin building a new Action.
Building a new Action is very similar to building in a regular Xano function stack.
Please note that because Actions are designed to not have dependencies outside of the Action itself, certain functions such as database operations are not available.
###  
Action Settings
Click the three dots in the upper-right corner to access **Action Settings**. From this panel, you can update the following:
**Name** - Give your action a unique name
**Instructions** - You can write documentation to accompany your action here. This field supports markdown for formatting. View the expandable section below for a quick reference.
**Quick Markdown Reference**
Copy
``` 
# Header 1
## Header 2
### Header 3
*Italic* or _Italic_
**Bold** or __Bold__
***Bold and Italic*** or ___Bold and Italic___
Link text
Alt text
`inline code`
```code block```
```
You can also preview your instructions using the **Preview** tab.
**Category** - You must provide a category for your Action before publishing
**Video URL** - You can insert a YouTube or Loom video link here to accompany your action
###  
Action Packages
Packages can be used to bundle and install multiple Actions at once.
<div>
1
###  
Click [] on the left-hand navigation.
2
###  
Give your package a name, description, and check the other settings in the panel that opens.
3
###  
Add Actions to your package by clicking []
You can choose to either copy the action into the package, or move it.
You can also create new actions at this time specifically for your package.
4
###  
When your Package is ready, click Publish, and once publishing completes, you can add it to your workspace(s).
</div>
###  
Publishing
When you publish your Action, you\'ll be able to review and make any changes to the documentation and certain Action settings once more before going live.
Make sure to choose the appropriate access level for your Action.
**Public** - This Action will be available for anyone to browse for, install and use.
**Private** - This Action will not be available for distribution. Use this for specific Actions that you only want to use internally.
**Unlisted** - This Action will be available to anyone that has the URL, but will not be found when browsing available Actions.
###  
Settings Registry
Because Actions have no dependencies, each Action contains a Settings Registry, which is used in a similar manner to environment variables. You will use the Settings Registry for situations where an Action requires an API key or other sensitive data that you need to ensure users of the Action supply without supplying it yourself.
To add a new value to the Settings Registry, just add a new input to your Action. In the settings for that input, you\'ll see a new option in the **Configuration** section called Settings Registry.
Checking this box will mark this input as part of the Settings Registry, enabling you to provide your own data for testing and make sure it is apparent when these values need to be provided for others utilizing the Action you are building.
###  
Deleting an Action
Please note that deleting an action does not impact users who have already imported your action into their workspace.
Click the settings icon in the top-right of your published action, and click Delete Action**.**
Think of projects as a folder for related actions to reside in. They are necessary for any actions you create, and include a number of helpful features to keep you organized.
###  
Actions
Your project can have multiple Actions inside of it. You can add new actions to a Project by clicking Create Action inside of the Project.
###  
Members
You can invite collaborators to a Project that you own by clicking the **Invite Collaborators** button.
Once you\'ve sent an invite, it will show up on the Members screen, as shown below.
The invitee will receive an email similar to the one below allowing them to accept the invitation.
###  
Settings
**Name** - The name of your project
**Custom Project ID** - You can assign a custom ID to your project here. The project ID determines the slug, or portion of the URL, that leads to the project.
**Description** - A description of your project
From this screen, you can also delete your project.
Last updated 2 months ago
Was this helpful?

## Code Examples

```
code block
```

