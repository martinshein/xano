---
category: 01-getting-started
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- CRUD
title: The Development Life Cycle
---

# The Development Life Cycle

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
The first stage of the SLDC usually consists of two parts: **planning** and **analysis**.
Gather requirements passively or actively from potential customers or other relevant stakeholders, and ensure you are solving a real problem. You would then be able to analyze the feasibility of creating the product, revenue potential, cost, and more.
Once you decide what you\'re building is in line with stakeholder goals, addresses user needs, and is feasible to create, you can move to the second stage.
Design
The design phase is where you start to put your ideas to paper. This might include creating actual designs in a tool like Figma, or going higher level and using a tool like Miro to create a wireframe or flowchart. From a Xano perspective, this is where you would start designing a data model.
Development
With a solid foundation to work with, this phase is where the actual development happens and where you turn specifications and designs into an actual product. This phase usually takes the most time, so setting expectations with yourself and the stakeholders you are working with is important.
Xano helps accelerate this stage with features like:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Generation of API CRUD Operations
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Auto-Documentation
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    Real-time Collaboration
    :::
If you\'re working with a team, you can leverage Xano features like real-time collaboration to seamlessly work within the same workspace, or create Branches and Merge them in when you\'re ready to move to the testing phase.
Testing
Before launching any product or service, it\'s important to have everything tested. At this phase, you would have a quality assurance (QA) team step in to run tests, but if you\'re on your own, you\'ll need to think through every part of testing your product which is more than just fixing critical bugs.
This might sound easier than it seems, but it\'s essential to test all the different permutations and ways that your users might interact with your application. Here are some different types of testing that you can do in this phase.
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Performance testing** Is your product ready to handle the traffic/storage requirements?
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Functional testing** Does your application meet the requirements set for in the Planning/Analysis phase?
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Security testing** Is your data in a secure place, and do you meet the appropriate compliance certifications within your country, or if you\'re dealing with sensitive data?
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Unit testing** Does every part of your app work the way it\'s supposed to?
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    **Usability testing** Do your users actually understand how to use your app?
    :::
**Xano provides a few features to help you in this phase**. Using Unit Tests, Test Suites and Data Sources can help you use dummy data without affecting what will be live in production. We support drafts to help you and your team get things right before Publishing. Branches can be used to create separate testing environments (Development, Staging, Production). For more complex use cases, Xano also supports Xano Link, which allows you to keep all of your Workspaces and Instances in sync with a master so your customers have a consistent experience.
Deployment
The Deployment stage is where your product or service is shipped to its intended user(s). This process can depend on the nature of what is being released; however, it\'s best practice to launch to a small set of users (typically called a canary release).
Maintenance
Maintenance is typically the last stage of the SDLC; however, in today\'s world, people are moving toward a more Agile software development approach where the product or service is continually improved, and sometimes the feedback from users makes it necessary to go back to the first step of the SDLC. This is why most images of the SDLC that you find are circular because it is a process that keeps repeating itself once you find something that\'s working.
Last updated 3 months ago
Was this helpful?