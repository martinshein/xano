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
- fundamentals
- concepts
title: Key Concepts
---

# Key Concepts

## 📋 **Quick Summary**
Essential Xano terminology and concepts covering instances, workspaces, APIs, databases, and JSON data structures. Understanding these fundamentals is crucial for building backend applications and integrating with frontend frameworks like n8n and WeWeb.

## 🎯 **Core Architecture Concepts**















### Understanding Xano Architecture
Xano uses a hierarchical structure: **Instance** → **Workspace** → **APIs & Databases**. Each level provides isolation and resource management for different aspects of your backend applications.

## 🏗️ **Infrastructure Components**

### 🖥️ Instance
Your dedicated server environment that hosts all Xano resources.

```javascript
// Instance Architecture
{
  "instance_id": "prod-instance-123",
  "plan": "professional", // free, starter, professional, enterprise
  "resources": {
    "cpu_cores": 4,
    "memory_gb": 16,
    "storage_gb": 500,
    "bandwidth_gb": 1000
  },
  "isolation": "dedicated", // shared on free plan
  "availability": "99.9%",
  "region": "us-east-1"
}
```

**Plan Differences:**
- **Free Plan**: Shared instance with resource limits
- **Paid Plans**: Dedicated resources with full isolation
- **Enterprise**: Custom configurations and advanced features

### 📂 Workspace
Project containers within your instance for organizing applications.

```javascript
// Workspace Structure
{
  "workspace_id": "ecommerce-app",
  "name": "E-commerce Backend",
  "environment": "production", // development, staging, production
  "resources": {
    "apis": 25,
    "database_tables": 12,
    "background_tasks": 5,
    "custom_functions": 8
  },
  "team_members": [
    {"email": "dev@company.com", "role": "admin"},
    {"email": "designer@company.com", "role": "viewer"}
  ]
}
```

**Use Cases:**
- Separate projects (e.g., "Mobile App", "Web Dashboard")
- Environment separation (dev, staging, production)
- Client project isolation for agencies

## 🔄 **Application Architecture**

### 🧠 Backend (Xano)
Server-side logic, data processing, and business rules.

```javascript
// Backend Components in Xano
{
  "apis": {
    "rest_endpoints": "Handle HTTP requests (GET, POST, PUT, DELETE)",
    "custom_functions": "Reusable business logic components",
    "background_tasks": "Scheduled or queued operations"
  },
  "database": {
    "tables": "Structured data storage",
    "relationships": "Data connections and constraints",
    "queries": "Data retrieval and manipulation"
  },
  "integrations": {
    "external_apis": "Third-party service connections",
    "webhooks": "Real-time event notifications",
    "file_storage": "Media and document management"
  }
}
```

### 📱 Frontend (n8n, WeWeb, etc.)
User interface and client-side interactions.

```javascript
// Frontend Integration Examples
{
  "n8n_workflows": {
    "purpose": "Automation and data processing",
    "integration": "HTTP requests to Xano APIs",
    "triggers": "Webhooks, schedules, manual execution"
  },
  "weweb_apps": {
    "purpose": "Visual web application building",
    "integration": "Direct Xano collection bindings",
    "features": "Real-time data, user authentication"
  },
  "custom_apps": {
    "mobile": "React Native, Flutter",
    "web": "React, Vue, Angular",
    "desktop": "Electron, Tauri"
  }
}
```

## 💾 **Data Management**

### 🗄️ Database
Structured data storage with relationships and constraints.

```javascript
// Database Table Example
{
  "table_name": "users",
  "fields": {
    "id": {
      "type": "integer",
      "primary_key": true,
      "auto_increment": true
    },
    "email": {
      "type": "text",
      "unique": true,
      "required": true
    },
    "name": {
      "type": "text",
      "required": true
    },
    "avatar": {
      "type": "file",
      "file_types": ["image"]
    },
    "created_at": {
      "type": "datetime",
      "default": "now"
    }
  },
  "relationships": {
    "orders": {
      "type": "one_to_many",
      "foreign_table": "orders",
      "foreign_key": "user_id"
    }
  }
}
```

**Database Features:**
- **ACID Compliance**: Data integrity and consistency
- **Relationships**: Link related data across tables
- **Indexing**: Optimize query performance
- **Backup & Restore**: Data protection and recovery

## 🌐 **API Communication**

### 🔌 API (Application Programming Interface)
Communication protocols between different software systems.

```javascript
// Complete API Request/Response Example
{
  "request": {
    "method": "POST",
    "url": "https://your-xano.xano.io/api:v1/auth/login",
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer abc123...",
      "User-Agent": "MyApp/1.0"
    },
    "body": {
      "email": "user@example.com",
      "password": "securePassword123"
    }
  },
  "response": {
    "status_code": 200,
    "headers": {
      "Content-Type": "application/json",
      "Cache-Control": "no-store"
    },
    "body": {
      "authToken": "jwt-token-here",
      "user": {
        "id": 123,
        "name": "John Doe",
        "email": "user@example.com"
      },
      "expires_in": 3600
    }
  }
}
```

### HTTP Methods in Xano

```javascript
// REST API Method Examples
const apiMethods = {
  "GET": {
    "purpose": "Retrieve data",
    "example": "GET /api:v1/products?category=electronics",
    "use_case": "Fetch product listings, user profiles"
  },
  "POST": {
    "purpose": "Create new data",
    "example": "POST /api:v1/users",
    "body": {"name": "John", "email": "john@example.com"},
    "use_case": "User registration, order creation"
  },
  "PUT": {
    "purpose": "Update entire resource",
    "example": "PUT /api:v1/users/123",
    "body": {"name": "John Updated", "email": "john.new@example.com"},
    "use_case": "Complete profile updates"
  },
  "PATCH": {
    "purpose": "Partial update",
    "example": "PATCH /api:v1/users/123",
    "body": {"name": "John Updated"},
    "use_case": "Update specific fields only"
  },
  "DELETE": {
    "purpose": "Remove data",
    "example": "DELETE /api:v1/users/123",
    "use_case": "Account deletion, order cancellation"
  }
}
```

### API Integration Patterns

```javascript
// n8n HTTP Request Node Configuration
{
  "method": "POST",
  "url": "https://your-xano.xano.io/api:v1/orders",
  "authentication": {
    "type": "headerAuth",
    "headerAuth": {
      "name": "Authorization",
      "value": "Bearer {{$node.auth.token}}"
    }
  },
  "body": {
    "product_id": "{{$json.productId}}",
    "quantity": "{{$json.quantity}}",
    "user_id": "{{$json.userId}}"
  }
}

// WeWeb API Collection Binding
{
  "collection_name": "products",
  "api_endpoint": "https://your-xano.xano.io/api:v1/products",
  "auth_type": "bearer_token",
  "filters": {
    "category": "{{page.categoryFilter}}",
    "price_max": "{{page.maxPrice}}"
  },
  "pagination": {
    "limit": 20,
    "offset": "{{page.currentOffset}}"
  }
}
```

## 🔧 **Development Concepts**

### 🏷️ Variables
Temporary data containers used during function stack execution.

```javascript
// Variable Usage in Xano Function Stack
{
  "function_stack": [
    // Step 1: Create variable from user input
    {
      "function": "Create Variable",
      "variable_name": "user_email",
      "value": "{{inputs.email}}",
      "type": "text"
    },
    
    // Step 2: Query database using variable
    {
      "function": "Get Record",
      "table": "users",
      "filter": {
        "email": "{{user_email}}"
      },
      "return_variable": "user_record"
    },
    
    // Step 3: Update variable with processed data
    {
      "function": "Update Variable",
      "variable": "user_email",
      "operation": "lowercase",
      "value": "{{user_record.email}}"
    },
    
    // Step 4: Use variable in response
    {
      "function": "Response",
      "body": {
        "message": "Welcome {{user_record.name}}",
        "normalized_email": "{{user_email}}"
      }
    }
  ]
}
```

**Variable Types:**
- **Temporary**: Exist only during function execution
- **Scoped**: Available within current function stack
- **Typed**: String, integer, array, object, boolean
- **Mutable**: Can be updated during execution

**Variables vs Database:**
- **Variables**: Temporary, fast access, workflow-specific
- **Database**: Persistent, structured, cross-workflow accessible

## 📊 **Data Formats**

### 🗃️ JSON (JavaScript Object Notation)
Standardized data format for API communication and data storage.

```javascript
// Complete E-commerce Order JSON Example
{
  "order_id": "ORD-2024-001",
  "customer": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "address": {
      "street": "123 Main St",
      "city": "New York",
      "state": "NY",
      "zip": "10001",
      "country": "USA"
    }
  },
  "items": [
    {
      "product_id": "PROD-001",
      "name": "Wireless Headphones",
      "price": 99.99,
      "quantity": 2,
      "total": 199.98
    },
    {
      "product_id": "PROD-002",
      "name": "Phone Case",
      "price": 24.99,
      "quantity": 1,
      "total": 24.99
    }
  ],
  "payment": {
    "method": "credit_card",
    "last_four": "4242",
    "status": "completed",
    "transaction_id": "txn_abc123"
  },
  "shipping": {
    "method": "standard",
    "cost": 9.99,
    "estimated_delivery": "2024-01-25",
    "tracking_number": "1Z999AA1234567890"
  },
  "totals": {
    "subtotal": 224.97,
    "tax": 18.00,
    "shipping": 9.99,
    "total": 252.96
  },
  "status": "processing",
  "created_at": "2024-01-20T10:30:00Z",
  "updated_at": "2024-01-20T10:30:00Z"
}
```

**JSON Structure Benefits:**
- **Human Readable**: Easy to understand and debug
- **Machine Parseable**: Efficiently processed by applications
- **Lightweight**: Minimal syntax overhead
- **Universal**: Supported by all programming languages

### JSON Structure Types

#### 📄 Objects
Key-value pairs representing entities or complex data.

```javascript
// User Profile Object
{
  "user_id": 123,
  "profile": {
    "personal": {
      "first_name": "John",
      "last_name": "Doe",
      "email": "john@example.com",
      "phone": "+1-555-123-4567"
    },
    "preferences": {
      "theme": "dark",
      "language": "en",
      "notifications": {
        "email": true,
        "sms": false,
        "push": true
      }
    },
    "metadata": {
      "last_login": "2024-01-20T10:30:00Z",
      "login_count": 47,
      "account_type": "premium"
    }
  }
}
```

#### 📑 Arrays
Ordered lists of items (any JSON data type).

```javascript
// Product Catalog Array
[
  {
    "id": "PROD-001",
    "name": "Wireless Headphones",
    "category": "electronics",
    "price": 99.99,
    "in_stock": true,
    "tags": ["wireless", "bluetooth", "noise-cancelling"],
    "reviews": {
      "average_rating": 4.5,
      "total_reviews": 128
    }
  },
  {
    "id": "PROD-002",
    "name": "Organic Coffee Beans",
    "category": "food",
    "price": 24.99,
    "in_stock": false,
    "tags": ["organic", "fair-trade", "dark-roast"],
    "reviews": {
      "average_rating": 4.8,
      "total_reviews": 89
    }
  }
]
```

#### 🪺 Nested Data
Complex hierarchical data structures.

```javascript
// Company Organization Structure
{
  "company": {
    "name": "Tech Solutions Inc",
    "departments": [
      {
        "name": "Engineering",
        "manager": {
          "name": "Alice Johnson",
          "employee_id": "EMP-001"
        },
        "teams": [
          {
            "name": "Backend",
            "members": [
              {"name": "Bob Smith", "role": "Senior Developer"},
              {"name": "Carol Lee", "role": "Developer"}
            ],
            "technologies": ["Xano", "PostgreSQL", "Node.js"]
          },
          {
            "name": "Frontend",
            "members": [
              {"name": "David Chen", "role": "Senior Developer"},
              {"name": "Eva Rodriguez", "role": "UI/UX Developer"}
            ],
            "technologies": ["WeWeb", "React", "TypeScript"]
          }
        ]
      }
    ]
  }
}
```

### ℹ️ JSON Data Types
Primitive and complex data types supported in JSON format.

```javascript
// Complete JSON Data Types Example
{
  // String - Text data in double quotes
  "company_name": "Acme Corporation",
  "description": "Leading provider of innovative solutions",
  
  // Integer - Whole numbers without quotes
  "employee_count": 150,
  "founded_year": 2010,
  
  // Decimal - Numbers with decimal points
  "revenue_millions": 45.7,
  "growth_rate": 0.125,
  "stock_price": 89.50,
  
  // Boolean - true or false values
  "is_public": true,
  "is_hiring": false,
  "profitable": true,
  
  // Null - Represents absence of value
  "parent_company": null,
  "ipo_date": null,
  
  // Array - Ordered list of values
  "office_locations": [
    "New York",
    "San Francisco",
    "London"
  ],
  
  // Array of numbers
  "quarterly_revenue": [10.2, 12.5, 15.8, 18.1],
  
  // Array of objects
  "departments": [
    {
      "name": "Engineering",
      "head_count": 45,
      "budget": 2500000
    },
    {
      "name": "Sales",
      "head_count": 32,
      "budget": 1800000
    }
  ],
  
  // Nested object
  "contact_info": {
    "headquarters": {
      "address": "123 Business Ave",
      "city": "New York",
      "state": "NY",
      "zip": "10001"
    },
    "phone": "+1-555-ACME-001",
    "email": "info@acme.com",
    "website": "https://www.acme.com"
  }
}
```

## 🔗 **Integration Examples**

### n8n JSON Processing
```javascript
// n8n Function Node - Transform Xano API Response
const xanoResponse = items[0].json;

// Extract and transform data
const transformedData = {
  customer_id: xanoResponse.user.id,
  full_name: `${xanoResponse.user.first_name} ${xanoResponse.user.last_name}`,
  order_total: xanoResponse.orders.reduce((sum, order) => sum + order.total, 0),
  last_order_date: xanoResponse.orders[0]?.created_at || null,
  is_premium: xanoResponse.user.subscription_tier === 'premium'
};

return [{
  json: transformedData
}];
```

### WeWeb Data Binding
```javascript
// WeWeb Collection Binding Configuration
{
  "collection_name": "user_dashboard",
  "data_source": {
    "type": "xano",
    "endpoint": "/api:v1/users/{{user.id}}/dashboard",
    "response_mapping": {
      "user_name": "{{response.user.name}}",
      "recent_orders": "{{response.orders}}",
      "total_spent": "{{response.analytics.total_spent}}",
      "favorite_products": "{{response.recommendations}}"
    }
  }
}
```

## 📝 **Best Practices**

### JSON Validation
```javascript
// Common JSON Mistakes to Avoid
{
  // ❌ Incorrect - Trailing comma
  "name": "John",
  "age": 30,
  
  // ❌ Incorrect - Single quotes
  'email': 'john@example.com',
  
  // ❌ Incorrect - Unquoted keys
  phone: "555-1234",
  
  // ✅ Correct format
  "address": {
    "street": "123 Main St",
    "city": "New York"
  }
}
```

### Data Type Consistency
```javascript
// Maintain consistent data types
{
  "user_id": 123,        // Always integer, not "123"
  "is_active": true,     // Boolean, not "true"
  "price": 29.99,        // Number, not "$29.99"
  "tags": ["tag1", "tag2"], // Array, even for single items
  "metadata": null       // Null for missing data, not empty string
}
```

---

*Understanding these key concepts provides the foundation for building robust backend applications with Xano and integrating them effectively with frontend frameworks and automation tools.*