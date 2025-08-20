---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- CRUD
- AI
- Setup
- Workspace
title: During setup, make sure to choose Create With AI
---

# Get Started Assistant: Create With AI

## 📋 **Quick Summary**
Xano's AI-powered workspace creation helps you build databases and CRUD endpoints automatically. Choose "Create With AI" during setup to leverage intelligent database design recommendations, auto-generated endpoints, and conversational development assistance for faster project initialization.

## 🎯 **Core Concepts**

### AI Workspace Creation
When creating a new Xano workspace, you can:
- **Start from scratch**: Manual database and endpoint creation
- **Create With AI**: Automated database design and CRUD endpoint generation

### AI Generator Capabilities
- Database schema recommendations
- Automatic table creation with relationships
- CRUD endpoint generation
- Template-based initialization
- Conversational development guidance

## 🛠️ **Implementation Guide**

### Step 1: Choose Create With AI During Setup

```javascript
// When creating a new workspace in Xano dashboard:
// 1. Click "New Workspace"
// 2. Select "Create With AI" option
// 3. Proceed to AI conversation interface
```

### Step 2: Provide AI Instructions

There are three main approaches to working with the AI generator:

#### Option A: Start with Template
```javascript
// Example AI prompt:
"I want to build an e-commerce platform. 
Show me available templates and help customize one for my needs."

// AI will:
// - Present relevant templates
// - Allow customization through conversation
// - Generate appropriate database structure
```

#### Option B: Describe Your Project
```javascript
// Example AI prompt:
"I'm building a task management app for teams. 
Users should be able to create projects, assign tasks, 
track progress, and collaborate with team members."

// AI will:
// - Analyze requirements
// - Suggest database design
// - Create tables and relationships
// - Generate CRUD endpoints
```

#### Option C: Specify Database Structure
```javascript
// Example AI prompt:
"Create these tables:
- Users (id, name, email, role)
- Projects (id, title, description, user_id)
- Tasks (id, title, status, project_id, assigned_to)
- Comments (id, content, task_id, user_id)

Set up proper relationships and CRUD endpoints."

// AI will:
// - Create exact table structure
// - Establish foreign key relationships
// - Generate appropriate endpoints
```

## 🔗 **Integration Examples**

### n8n Workflow Integration
```javascript
// n8n HTTP Request node to newly created AI endpoints
{
  "method": "POST",
  "url": "https://your-xano-workspace.xano.io/api:v1/projects",
  "headers": {
    "Authorization": "Bearer {{$node.auth.token}}",
    "Content-Type": "application/json"
  },
  "body": {
    "title": "{{$json.projectName}}",
    "description": "{{$json.description}}",
    "user_id": "{{$json.userId}}"
  }
}
```

### WeWeb Component Integration
```vue
<template>
  <div class="ai-generated-dashboard">
    <!-- Bind to auto-generated Xano collections -->
    <ww-list 
      :data="xano.projects"
      :loading="isLoading"
    >
      <template #item="{ item }">
        <project-card :project="item" />
      </template>
    </ww-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoading: false
    }
  },
  async created() {
    // Fetch from AI-generated endpoints
    await this.fetchProjects()
  },
  methods: {
    async fetchProjects() {
      this.isLoading = true
      try {
        // Use auto-generated collection bindings
        await this.$xano.projects.fetch()
      } catch (error) {
        console.error('Error fetching projects:', error)
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>
```

## 🚀 **Advanced Usage Patterns**

### Iterative Development with AI
```javascript
// Initial AI conversation:
"Create a blog platform with users, posts, and comments"

// Follow-up refinements:
"Add categories and tags to posts"
"Include user roles (admin, editor, author)"
"Add post scheduling functionality"
"Create analytics tracking for post views"

// AI adapts existing structure incrementally
```

### Template Customization Flow
```javascript
// Start with template:
"Use the social media template"

// Customize features:
"Remove video upload, add polls feature"
"Change user profiles to include company information"
"Add private messaging between users"
"Include content moderation workflows"
```

## 🎯 **Best Practices**

### 1. Clear Project Description
```javascript
// Good prompt:
"Build a customer support ticketing system with:
- Customer ticket creation
- Agent assignment and routing
- Priority levels and status tracking
- Internal notes and customer communication
- Reporting and analytics"

// Avoid vague prompts:
"Create a support system"
```

### 2. Specify Relationships
```javascript
// Be explicit about data relationships:
"Each customer can have multiple tickets.
Each ticket belongs to one customer and one agent.
Tickets can have multiple comments from both customers and agents."
```

### 3. Define User Roles Early
```javascript
"Include these user types:
- Customers (can create tickets, view own tickets)
- Agents (can be assigned tickets, add internal notes)
- Admins (full access, can manage agents and customers)"
```

## 🔧 **Common Use Cases**

### E-commerce Platform
```javascript
"Create an e-commerce backend with products, categories, 
orders, customers, inventory tracking, and payment processing"
```

### Event Management System
```javascript
"Build an event platform where organizers can create events, 
users can register, and there's ticketing with different price tiers"
```

### Learning Management System
```javascript
"Design an LMS with courses, lessons, students, instructors, 
assignments, grades, and progress tracking"
```

### Project Management Tool
```javascript
"Create a project management system with workspaces, projects, 
tasks, team members, time tracking, and milestone management"
```

## 📊 **Expected Outputs**

When using AI workspace creation, you'll receive:

1. **Database Tables**: Properly structured with appropriate field types
2. **Relationships**: Foreign keys and table connections
3. **CRUD Endpoints**: Auto-generated API endpoints for each table
4. **Authentication Setup**: User management and security configurations
5. **Sample Data**: Optional test records for development

## 🔍 **Troubleshooting**

### AI Misunderstood Requirements
- Provide more specific details in follow-up messages
- Use examples to clarify complex relationships
- Reference similar platforms or applications

### Missing Features
- Ask AI to add specific tables or fields
- Request additional endpoints or functions
- Describe the missing functionality clearly

### Structure Modifications
- AI can modify existing tables and relationships
- Request schema changes through conversation
- Test changes in development environment first

---

*This AI-powered setup process significantly accelerates initial project development and ensures proper database design patterns from the start.*