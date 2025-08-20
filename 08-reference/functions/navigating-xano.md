---
category: functions
has_code_examples: true
difficulty: beginner
last_updated: '2025-01-23'
related_docs: []
subcategory: 08-reference/functions
tags:
- authentication
- api
- webhook
- trigger
- query
- filter
- middleware
- expression
- realtime
- transaction
- function
- background-task
- custom-function
- rest
- database
- navigation
- interface
- getting-started
title: Navigating Xano
---

# Navigating Xano

## 📋 **Quick Summary**
Comprehensive guide to navigating Xano's interface, from account setup to workspace management. Learn essential navigation patterns, keyboard shortcuts, and interface components for efficient backend development and integration with tools like n8n and WeWeb.















## 🎯 **Core Interface Components**

### Xano Platform Structure
Xano's interface follows a hierarchical navigation pattern designed for efficient backend development and integration workflows.

## 🚀 **Getting Started**

### Account Creation and Access

```javascript
// Account Setup Flow
{
  "signup_url": "https://xano.com",
  "login_url": "https://app.xano.com/login",
  "authentication_methods": [
    "email_password",
    "google_sso",
    "github_sso"
  ],
  "free_tier": {
    "included": true,
    "limitations": {
      "instances": "shared",
      "requests_per_month": 10000,
      "storage_gb": 1
    }
  }
}
```

### First-Time Setup

```javascript
// Initial Workspace Creation
{
  "workspace_options": {
    "start_from_scratch": "Manual database and API creation",
    "use_template": "Pre-built application templates",
    "create_with_ai": "AI-assisted database design"
  },
  "recommended_path": "create_with_ai",
  "initial_configuration": {
    "workspace_name": "My First Project",
    "description": "Learning Xano fundamentals",
    "environment": "development"
  }
}
```

## 📱 **Main Interface Layout**

### Left Sidebar Navigation

```javascript
// Primary Navigation Structure
{
  "navigation_sections": {
    "database": {
      "icon": "database",
      "description": "Tables, relationships, and data management",
      "sub_items": ["Tables", "Views", "Import/Export", "Relationships"]
    },
    "api": {
      "icon": "code",
      "description": "REST endpoints and function stacks",
      "sub_items": ["API Groups", "Endpoints", "Authentication", "Documentation"]
    },
    "functions": {
      "icon": "function",
      "description": "Reusable business logic components",
      "sub_items": ["Custom Functions", "Async Functions", "Background Tasks"]
    },
    "file_storage": {
      "icon": "folder",
      "description": "File upload and media management",
      "sub_items": ["Public Files", "Private Files", "Storage Settings"]
    },
    "realtime": {
      "icon": "lightning",
      "description": "WebSocket connections and live updates",
      "sub_items": ["Channels", "Permissions", "Event Handling"]
    },
    "settings": {
      "icon": "settings",
      "description": "Workspace and instance configuration",
      "sub_items": ["General", "Team", "Environment Variables", "Billing"]
    }
  }
}
```

### Top Navigation Bar

```javascript
// Header Components
{
  "header_elements": {
    "workspace_selector": {
      "purpose": "Switch between different projects",
      "location": "top-left",
      "shows_current_workspace": true
    },
    "environment_toggle": {
      "purpose": "Switch between dev/staging/production",
      "location": "top-center",
      "options": ["development", "staging", "production"]
    },
    "search_bar": {
      "purpose": "Global search across all resources",
      "location": "top-center",
      "searches": ["Tables", "APIs", "Functions", "Files"]
    },
    "user_menu": {
      "purpose": "Account settings and preferences",
      "location": "top-right",
      "includes": ["Profile", "Billing", "Logout"]
    }
  }
}
```

### Main Content Area

```javascript
// Content Panel Structure
{
  "content_areas": {
    "resource_list": {
      "description": "Lists tables, APIs, functions, etc.",
      "features": ["Search", "Sort", "Filter", "Bulk Actions"]
    },
    "detail_view": {
      "description": "Edit individual resources",
      "includes": ["Properties", "Configuration", "Testing"]
    },
    "function_stack_builder": {
      "description": "Visual workflow editor",
      "features": ["Drag & Drop", "Auto-suggestions", "Error Highlighting"]
    }
  }
}
```

## 🔄 **Navigation Workflows**

### Database Management Flow

```javascript
// Navigate: Database → Tables → Create/Edit
{
  "workflow": [
    {
      "step": 1,
      "action": "Click 'Database' in left sidebar",
      "result": "View all database tables"
    },
    {
      "step": 2,
      "action": "Click '+ New Table' or existing table name",
      "result": "Open table editor"
    },
    {
      "step": 3,
      "action": "Add fields, set types, configure relationships",
      "result": "Define table structure"
    },
    {
      "step": 4,
      "action": "Click 'Save' or use Ctrl+S",
      "result": "Commit changes to database"
    }
  ],
  "keyboard_shortcuts": {
    "new_field": "Ctrl+N",
    "save_table": "Ctrl+S",
    "duplicate_field": "Ctrl+D"
  }
}
```

### API Development Flow

```javascript
// Navigate: API → Groups → Endpoints → Function Stack
{
  "workflow": [
    {
      "step": 1,
      "action": "Click 'API' in left sidebar",
      "result": "View API groups and endpoints"
    },
    {
      "step": 2,
      "action": "Select API group or create new one",
      "result": "Access grouped endpoints"
    },
    {
      "step": 3,
      "action": "Click '+ Add Endpoint' or existing endpoint",
      "result": "Open endpoint configuration"
    },
    {
      "step": 4,
      "action": "Configure method, path, authentication",
      "result": "Set API endpoint basics"
    },
    {
      "step": 5,
      "action": "Build function stack with visual editor",
      "result": "Define business logic"
    },
    {
      "step": 6,
      "action": "Test endpoint with built-in tester",
      "result": "Validate functionality"
    }
  ]
}
```

### Function Stack Building

```javascript
// Visual Function Stack Editor Navigation
{
  "editor_components": {
    "function_palette": {
      "location": "left panel",
      "categories": [
        "Database Requests",
        "Data Manipulation",
        "External APIs",
        "Logic & Flow Control",
        "Utility Functions"
      ]
    },
    "canvas": {
      "location": "center",
      "features": [
        "Drag & drop functions",
        "Auto-connect data flow",
        "Error indicators",
        "Execution preview"
      ]
    },
    "properties_panel": {
      "location": "right panel",
      "shows": [
        "Function configuration",
        "Input/output mapping",
        "Variable inspection",
        "Debug information"
      ]
    }
  }
}
```

## ⌨️ **Keyboard Shortcuts & Productivity**

### Global Shortcuts

```javascript
// Universal Xano Shortcuts
{
  "global_shortcuts": {
    "search": {
      "keys": "Ctrl/Cmd + K",
      "description": "Open global search",
      "context": "Any screen"
    },
    "save": {
      "keys": "Ctrl/Cmd + S",
      "description": "Save current resource",
      "context": "Editors"
    },
    "new_item": {
      "keys": "Ctrl/Cmd + N",
      "description": "Create new resource",
      "context": "List views"
    },
    "duplicate": {
      "keys": "Ctrl/Cmd + D",
      "description": "Duplicate selected item",
      "context": "Selected resource"
    },
    "quick_test": {
      "keys": "Ctrl/Cmd + Enter",
      "description": "Run API test",
      "context": "API editor"
    }
  }
}
```

### Function Stack Editor Shortcuts

```javascript
// Function Builder Specific Shortcuts
{
  "function_editor_shortcuts": {
    "add_function": {
      "keys": "Ctrl/Cmd + Shift + F",
      "description": "Open function selector"
    },
    "connect_functions": {
      "keys": "Click + Drag",
      "description": "Connect function outputs to inputs"
    },
    "delete_function": {
      "keys": "Delete/Backspace",
      "description": "Remove selected function"
    },
    "copy_function": {
      "keys": "Ctrl/Cmd + C",
      "description": "Copy function with settings"
    },
    "paste_function": {
      "keys": "Ctrl/Cmd + V",
      "description": "Paste copied function"
    }
  }
}
```

## 🔗 **Integration Navigation Patterns**

### API Documentation Access

```javascript
// Quick API Documentation Navigation
{
  "documentation_access": {
    "swagger_ui": {
      "path": "API → [API Group] → Documentation tab",
      "features": ["Interactive testing", "Schema exploration", "Code examples"]
    },
    "endpoint_urls": {
      "format": "https://your-workspace.xano.io/api:v1/endpoint-path",
      "copy_button": "Available in endpoint header"
    },
    "authentication_info": {
      "location": "API → Authentication tab",
      "includes": ["Token requirements", "Header examples", "CORS settings"]
    }
  }
}
```

### External Tool Integration Setup

```javascript
// n8n Integration Navigation
{
  "n8n_setup_flow": [
    {
      "step": "Get API credentials",
      "path": "Settings → API Keys → Generate New Key"
    },
    {
      "step": "Copy endpoint URLs",
      "path": "API → [Endpoint] → Copy URL button"
    },
    {
      "step": "Test connection",
      "path": "API → [Endpoint] → Test tab"
    }
  ]
}

// WeWeb Integration Navigation
{
  "weweb_setup_flow": [
    {
      "step": "Configure CORS",
      "path": "Settings → CORS → Add WeWeb domain"
    },
    {
      "step": "Set up authentication",
      "path": "API → Authentication → Configure JWT/API key"
    },
    {
      "step": "Export collection schema",
      "path": "Database → [Table] → Export → JSON Schema"
    }
  ]
}
```

## 📊 **Monitoring & Debugging Navigation**

### Request History and Debugging

```javascript
// Debug and Monitor Navigation
{
  "debugging_tools": {
    "request_history": {
      "path": "API → Request History",
      "filters": ["Endpoint", "Status Code", "Time Range", "User"]
    },
    "function_stack_logs": {
      "path": "API → [Endpoint] → Logs tab",
      "shows": ["Execution steps", "Variable values", "Error details"]
    },
    "database_activity": {
      "path": "Database → Activity tab",
      "monitors": ["Query performance", "Connection usage", "Storage metrics"]
    },
    "instance_dashboard": {
      "path": "Settings → Instance Dashboard",
      "metrics": ["CPU usage", "Memory usage", "Request volume", "Error rates"]
    }
  }
}
```

### Performance Analysis Navigation

```javascript
// Performance Monitoring Workflow
{
  "performance_analysis": {
    "api_performance": {
      "location": "API → Analytics tab",
      "metrics": ["Response time", "Throughput", "Error rate", "Geographic distribution"]
    },
    "database_performance": {
      "location": "Database → Performance tab",
      "includes": ["Slow queries", "Index usage", "Storage optimization"]
    },
    "function_profiling": {
      "location": "Functions → [Function] → Performance tab",
      "details": ["Execution time", "Memory usage", "Call frequency"]
    }
  }
}
```

## 🚀 **Advanced Navigation Features**

### Workspace Management

```javascript
// Multi-Workspace Navigation
{
  "workspace_features": {
    "workspace_switcher": {
      "location": "Top navigation bar",
      "functionality": "Quick switch between projects",
      "keyboard_shortcut": "Ctrl/Cmd + W"
    },
    "cross_workspace_search": {
      "location": "Global search (Ctrl/Cmd + K)",
      "scope": "Search across all accessible workspaces"
    },
    "workspace_templates": {
      "location": "Settings → Templates",
      "purpose": "Save and reuse workspace configurations"
    }
  }
}
```

### Collaboration Features

```javascript
// Team Collaboration Navigation
{
  "collaboration_tools": {
    "real_time_editing": {
      "indication": "User avatars on edited resources",
      "conflict_resolution": "Automatic merge with change indicators"
    },
    "comments_and_annotations": {
      "location": "Any resource → Comments tab",
      "features": ["Threaded discussions", "Mentions", "Status tracking"]
    },
    "version_history": {
      "location": "Any resource → History tab",
      "capabilities": ["Change diff", "Rollback", "Branch comparison"]
    },
    "team_activity": {
      "location": "Settings → Activity Feed",
      "shows": ["Recent changes", "User actions", "System events"]
    }
  }
}
```

## 🎯 **Best Practices for Efficient Navigation**

### Organizational Strategies

```javascript
// Workspace Organization Best Practices
{
  "naming_conventions": {
    "apis": "Use descriptive names: 'user-auth', 'product-catalog'",
    "tables": "Singular nouns: 'user', 'product', 'order'",
    "functions": "Action-oriented: 'validate-email', 'calculate-tax'"
  },
  "grouping_strategies": {
    "by_feature": "Group related APIs and tables by application feature",
    "by_environment": "Separate development, staging, and production",
    "by_client": "For agencies: organize by client projects"
  },
  "documentation_habits": {
    "api_descriptions": "Clear, concise endpoint descriptions",
    "function_comments": "Document complex business logic",
    "field_labels": "User-friendly database field labels"
  }
}
```

### Quick Access Patterns

```javascript
// Efficiency Tips for Daily Use
{
  "productivity_tips": {
    "bookmark_frequently_used": "Use browser bookmarks for specific endpoints",
    "use_global_search": "Ctrl/Cmd + K for quick resource access",
    "master_shortcuts": "Learn keyboard shortcuts for common actions",
    "customize_interface": "Arrange panels for your workflow",
    "use_templates": "Create templates for common patterns"
  },
  "development_workflow": {
    "test_early_often": "Use built-in testing tools frequently",
    "monitor_performance": "Regularly check request history and metrics",
    "version_control": "Use branching for experimental changes",
    "document_as_you_go": "Add descriptions and comments during development"
  }
}
```

---

*Mastering Xano's navigation patterns accelerates development and improves integration efficiency with external tools like n8n and WeWeb.*