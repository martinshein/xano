---
title: "Database Requests - Complete CRUD Operations Guide"
description: "Master all Xano database operations with comprehensive patterns for Create, Read, Update, Delete operations, advanced queries, and data management best practices"
category: function-stack
tags:
  - Database Operations
  - CRUD
  - Query Functions
  - Data Management
  - SQL Operations
  - Database Functions
  - Data Processing
  - API Development
difficulty: intermediate
reading_time: 12 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of database concepts
  - Knowledge of Xano function stacks
  - Familiarity with data relationships
---

# Database Requests - Complete CRUD Operations Guide

## 📋 **Quick Summary**

**What it does:** Database request functions provide the foundation for all data operations in Xano, enabling Create, Read, Update, and Delete (CRUD) operations with advanced querying, filtering, and data management capabilities.

**Why it matters:** Database functions enable you to:
- **Build complete data workflows** with full CRUD operations
- **Query and filter data** dynamically based on user inputs
- **Manage relationships** between tables and complex data structures
- **Optimize performance** with efficient database operations
- **Ensure data integrity** with validation and transaction support

**Time to implement:** 5-10 minutes for basic operations, 30+ minutes for complex data workflows

---

## What You'll Learn

- Complete overview of all database request functions
- Best practices for each CRUD operation
- Advanced querying and filtering techniques
- Performance optimization patterns
- Error handling and data validation
- Integration with no-code platforms

## Core Database Functions Overview

### 📖 **Read Operations**

| Function | Purpose | Use Cases |
|----------|---------|-----------|
| **Query All Records** | Retrieve multiple records with filtering | List pages, search results, data exports |
| **Get Record** | Retrieve single record by ID | Detail pages, user profiles, specific lookups |
| **Get Database Schema** | Retrieve table structure | Dynamic forms, API documentation |

### ✏️ **Write Operations**

| Function | Purpose | Use Cases |
|----------|---------|-----------|
| **Add Record** | Create new database record | User registration, content creation |
| **Edit Record** | Update existing record completely | Profile updates, content editing |
| **Patch Record** | Update specific fields only | Status changes, partial updates |
| **Add or Edit Record** | Create or update based on conditions | Upsert operations, sync processes |

### 🗑️ **Delete Operations**

| Function | Purpose | Use Cases |
|----------|---------|-----------|
| **Delete Record** | Remove single record | Account deletion, content removal |
| **Bulk Operations** | Multiple operations in batch | Mass updates, bulk imports |

### 🔧 **Advanced Operations**

| Function | Purpose | Use Cases |
|----------|---------|-----------|
| **Database Transaction** | Group operations atomically | Payment processing, complex workflows |
| **External Database Query** | Query external databases | Data integration, legacy systems |
| **Direct Database Query** | Raw SQL operations | Complex queries, reporting |

## Query All Records - Dynamic Data Retrieval

### Basic Implementation

```javascript
// Function Stack: Get All Users
// 1. Query All Records from 'users' table
const users = await queryAllRecords({
  table: 'users',
  sort: { created_at: 'desc' },
  limit: 50
});

return users;
```

### Advanced Filtering Patterns

```javascript
// Dynamic filtering based on user input
const searchFilters = {};

// Add filters conditionally
if (input.search_term) {
  searchFilters['name|like'] = `%${input.search_term}%`;
}

if (input.status) {
  searchFilters.status = input.status;
}

if (input.created_after) {
  searchFilters['created_at|>='] = input.created_after;
}

const filteredResults = await queryAllRecords({
  table: 'users',
  filters: searchFilters,
  sort: { [input.sort_field || 'created_at']: input.sort_direction || 'desc' },
  limit: input.limit || 20,
  offset: (input.page - 1) * (input.limit || 20)
});

return {
  data: filteredResults,
  pagination: {
    page: input.page,
    limit: input.limit,
    total: filteredResults.length
  }
};
```

### Relationship Loading

```javascript
// Load related data efficiently
const postsWithAuthors = await queryAllRecords({
  table: 'posts',
  include: ['author', 'categories', 'comments.user'],
  filters: {
    status: 'published',
    'author.active': true
  },
  sort: { published_at: 'desc' }
});
```

## Get Record - Single Item Retrieval

### Basic Usage

```javascript
// Function Stack: Get User Profile
// 1. Get Record from 'users' table
const user = await getRecord({
  table: 'users',
  id: input.user_id,
  include: ['profile', 'preferences']
});

// 2. Precondition: Ensure user exists
if (!user) {
  throw new Error('User not found', 404);
}

return user;
```

### Security Pattern with Ownership Validation

```javascript
// Secure user data access
const requestedUser = await getRecord({
  table: 'users',
  id: input.user_id
});

// Validate user can access this data
if (requestedUser.id !== auth.user.id && auth.user.role !== 'admin') {
  throw new Error('Access denied', 403);
}

return requestedUser;
```

## Add Record - Creating New Data

### Basic Implementation

```javascript
// Function Stack: Create New Post
// 1. Add Record to 'posts' table
const newPost = await addRecord({
  table: 'posts',
  data: {
    title: input.title,
    content: input.content,
    author_id: auth.user.id,
    status: 'draft',
    created_at: new Date().toISOString()
  }
});

return newPost;
```

### Advanced Creation with Validation

```javascript
// Comprehensive post creation
class PostCreator {
  static async createPost(input, userId) {
    // 1. Validate input data
    await this.validatePostData(input);
    
    // 2. Check user permissions
    await this.validateUserPermissions(userId);
    
    // 3. Process and clean data
    const processedData = await this.processPostData(input, userId);
    
    // 4. Create the post
    const newPost = await addRecord({
      table: 'posts',
      data: processedData
    });
    
    // 5. Handle post-creation tasks
    await this.handlePostCreated(newPost);
    
    return newPost;
  }
  
  static async validatePostData(input) {
    if (!input.title || input.title.trim().length < 5) {
      throw new Error('Title must be at least 5 characters', 400);
    }
    
    if (!input.content || input.content.trim().length < 50) {
      throw new Error('Content must be at least 50 characters', 400);
    }
    
    // Check for duplicate titles
    const existingPost = await queryAllRecords({
      table: 'posts',
      filters: { title: input.title.trim() },
      limit: 1
    });
    
    if (existingPost.length > 0) {
      throw new Error('Post with this title already exists', 409);
    }
  }
  
  static async processPostData(input, userId) {
    return {
      title: input.title.trim(),
      content: input.content.trim(),
      author_id: userId,
      status: input.status || 'draft',
      featured_image: input.featured_image || null,
      tags: input.tags || [],
      seo_description: input.seo_description || input.content.substring(0, 160),
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    };
  }
  
  static async handlePostCreated(post) {
    // Add to search index
    await this.addToSearchIndex(post);
    
    // Send notifications
    if (post.status === 'published') {
      await this.notifySubscribers(post);
    }
    
    // Update author stats
    await this.updateAuthorStats(post.author_id);
  }
}
```

## Edit Record - Complete Updates

### Basic Update

```javascript
// Function Stack: Update User Profile
// 1. Get existing record for validation
const existingUser = await getRecord({
  table: 'users',
  id: input.user_id
});

// 2. Validate ownership
if (existingUser.id !== auth.user.id) {
  throw new Error('Can only edit your own profile', 403);
}

// 3. Edit Record
const updatedUser = await editRecord({
  table: 'users',
  id: input.user_id,
  fields: {
    name: input.name,
    email: input.email,
    bio: input.bio,
    updated_at: new Date().toISOString()
  }
});

return updatedUser;
```

### Conditional Updates with History

```javascript
// Advanced update with change tracking
class UserUpdater {
  static async updateUser(userId, updates, currentUserId) {
    // 1. Get current user data
    const currentUser = await getRecord({
      table: 'users',
      id: userId
    });
    
    // 2. Validate permissions
    await this.validateUpdatePermissions(currentUser, currentUserId);
    
    // 3. Track changes
    const changes = this.detectChanges(currentUser, updates);
    
    // 4. Validate updates
    await this.validateUpdates(updates, currentUser);
    
    // 5. Perform update
    const updatedUser = await editRecord({
      table: 'users',
      id: userId,
      fields: {
        ...updates,
        updated_at: new Date().toISOString(),
        updated_by: currentUserId
      }
    });
    
    // 6. Log changes
    if (changes.length > 0) {
      await this.logChanges(userId, changes, currentUserId);
    }
    
    return updatedUser;
  }
  
  static detectChanges(current, updates) {
    const changes = [];
    
    for (const [field, newValue] of Object.entries(updates)) {
      if (current[field] !== newValue) {
        changes.push({
          field,
          old_value: current[field],
          new_value: newValue
        });
      }
    }
    
    return changes;
  }
  
  static async logChanges(userId, changes, changedBy) {
    for (const change of changes) {
      await addRecord({
        table: 'user_change_log',
        data: {
          user_id: userId,
          field: change.field,
          old_value: JSON.stringify(change.old_value),
          new_value: JSON.stringify(change.new_value),
          changed_by: changedBy,
          changed_at: new Date().toISOString()
        }
      });
    }
  }
}
```

## Patch Record - Selective Updates

### Efficient Status Updates

```javascript
// Function Stack: Update Post Status
// 1. Patch Record for efficient updates
const patchedPost = await patchRecord({
  table: 'posts',
  id: input.post_id,
  fields: {
    status: input.new_status,
    published_at: input.new_status === 'published' ? new Date().toISOString() : null,
    updated_at: new Date().toISOString()
  }
});

return patchedPost;
```

### Batch Status Updates

```javascript
// Update multiple records efficiently
class BatchUpdater {
  static async updateMultipleStatuses(postIds, newStatus, userId) {
    const updatePromises = postIds.map(async (postId) => {
      // Validate ownership first
      const post = await getRecord({
        table: 'posts',
        id: postId
      });
      
      if (post.author_id !== userId) {
        throw new Error(`No permission to update post ${postId}`, 403);
      }
      
      // Perform patch update
      return await patchRecord({
        table: 'posts',
        id: postId,
        fields: {
          status: newStatus,
          updated_at: new Date().toISOString(),
          updated_by: userId
        }
      });
    });
    
    const results = await Promise.all(updatePromises);
    
    return {
      updated_count: results.length,
      updated_posts: results
    };
  }
}
```

## Delete Record - Safe Data Removal

### Soft Delete Pattern

```javascript
// Function Stack: Soft Delete Post
// 1. Get record to validate
const post = await getRecord({
  table: 'posts',
  id: input.post_id
});

// 2. Validate ownership
if (post.author_id !== auth.user.id && auth.user.role !== 'admin') {
  throw new Error('Cannot delete posts you do not own', 403);
}

// 3. Soft delete using Patch Record
const deletedPost = await patchRecord({
  table: 'posts',
  id: input.post_id,
  fields: {
    deleted: true,
    deleted_at: new Date().toISOString(),
    deleted_by: auth.user.id
  }
});

return { message: 'Post deleted successfully', post: deletedPost };
```

### Hard Delete with Cleanup

```javascript
// Complete deletion with related data cleanup
class PostDeleter {
  static async deletePost(postId, userId) {
    // 1. Validate permissions
    const post = await getRecord({
      table: 'posts',
      id: postId,
      include: ['comments', 'images']
    });
    
    if (post.author_id !== userId) {
      throw new Error('Cannot delete posts you do not own', 403);
    }
    
    // 2. Clean up related data
    await this.cleanupRelatedData(post);
    
    // 3. Delete the main record
    const deletedPost = await deleteRecord({
      table: 'posts',
      id: postId
    });
    
    // 4. Update author stats
    await this.updateAuthorStats(post.author_id);
    
    return deletedPost;
  }
  
  static async cleanupRelatedData(post) {
    // Delete comments
    if (post.comments && post.comments.length > 0) {
      for (const comment of post.comments) {
        await deleteRecord({
          table: 'comments',
          id: comment.id
        });
      }
    }
    
    // Delete associated images
    if (post.images && post.images.length > 0) {
      for (const image of post.images) {
        await deleteRecord({
          table: 'post_images',
          id: image.id
        });
      }
    }
    
    // Remove from search index
    await this.removeFromSearchIndex(post.id);
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Database Workflows**

```yaml
Database CRUD Workflow:
1. Webhook (Receive data input)
2. Function Node (Validate and format data)
3. HTTP Request (Call Xano database operation)
4. Switch Node (Handle success/error responses)
5. Function Node (Process results)
6. HTTP Response (Return formatted data)
```

**n8n Database Operation Function:**
```javascript
// Process database operation request
const operation = $input.body.operation; // 'create', 'read', 'update', 'delete'
const tableName = $input.body.table;
const data = $input.body.data;

// Validate required fields
if (!operation || !tableName) {
  return { error: 'Missing operation or table name' };
}

// Build Xano API request
const xanoRequest = {
  method: 'POST',
  url: `${$env.XANO_API_URL}/${operation}/${tableName}`,
  headers: {
    'Authorization': 'Bearer ' + $env.XANO_API_KEY,
    'Content-Type': 'application/json'
  },
  data: data
};

// Add specific parameters based on operation
switch (operation) {
  case 'read':
    xanoRequest.method = 'GET';
    if (data.filters) {
      xanoRequest.params = data.filters;
    }
    break;
  
  case 'update':
    xanoRequest.url += `/${data.id}`;
    xanoRequest.data = data.fields;
    break;
  
  case 'delete':
    xanoRequest.method = 'DELETE';
    xanoRequest.url += `/${data.id}`;
    break;
}

return xanoRequest;
```

### 🌐 **WeWeb Database Integration**

```javascript
// WeWeb database operations manager
class WeWebDatabaseManager {
  constructor() {
    this.apiBase = wwLib.envVars.XANO_API_URL;
    this.authToken = wwLib.auth.getAuthToken();
  }
  
  async performCRUD(operation, table, data = {}) {
    const config = this.buildRequestConfig(operation, table, data);
    
    try {
      const response = await wwLib.api.request(config);
      
      // Update local collections
      this.updateLocalCollections(operation, table, response.data);
      
      return {
        success: true,
        data: response.data,
        operation: operation
      };
      
    } catch (error) {
      console.error(`Database ${operation} failed:`, error);
      return {
        success: false,
        error: error.message,
        operation: operation
      };
    }
  }
  
  buildRequestConfig(operation, table, data) {
    const config = {
      headers: {
        'Authorization': 'Bearer ' + this.authToken,
        'Content-Type': 'application/json'
      }
    };
    
    switch (operation) {
      case 'create':
        config.method = 'POST';
        config.url = `${this.apiBase}/crud/${table}`;
        config.data = data;
        break;
        
      case 'read':
        config.method = 'GET';
        config.url = `${this.apiBase}/crud/${table}`;
        if (data.id) {
          config.url += `/${data.id}`;
        }
        if (data.filters) {
          config.params = data.filters;
        }
        break;
        
      case 'update':
        config.method = 'PATCH';
        config.url = `${this.apiBase}/crud/${table}/${data.id}`;
        config.data = data.fields;
        break;
        
      case 'delete':
        config.method = 'DELETE';
        config.url = `${this.apiBase}/crud/${table}/${data.id}`;
        break;
    }
    
    return config;
  }
  
  updateLocalCollections(operation, table, responseData) {
    const collectionName = `${table}Collection`;
    
    switch (operation) {
      case 'create':
        wwLib.collections[collectionName].add(responseData);
        break;
        
      case 'update':
        wwLib.collections[collectionName].update(responseData.id, responseData);
        break;
        
      case 'delete':
        wwLib.collections[collectionName].remove(responseData.id);
        break;
    }
  }
}

// Usage examples
const dbManager = new WeWebDatabaseManager();

// Create new record
async function createPost() {
  const result = await dbManager.performCRUD('create', 'posts', {
    title: wwLib.form.getValue('title'),
    content: wwLib.form.getValue('content'),
    author_id: wwLib.auth.getUserId()
  });
  
  if (result.success) {
    wwLib.goTo('/posts/' + result.data.id);
  } else {
    wwLib.showAlert('Error creating post: ' + result.error);
  }
}

// Update existing record
async function updatePost(postId) {
  const result = await dbManager.performCRUD('update', 'posts', {
    id: postId,
    fields: {
      title: wwLib.form.getValue('title'),
      content: wwLib.form.getValue('content'),
      updated_at: new Date().toISOString()
    }
  });
  
  if (result.success) {
    wwLib.showAlert('Post updated successfully');
  }
}
```

### 🔧 **Make Database Automation**

```yaml
CRUD Automation Scenario:
1. Webhook (Receive database operation request)
2. Router (Route based on operation type)
   - Create Path: Validate → Add Record → Send Notification
   - Read Path: Apply Filters → Query → Format Response
   - Update Path: Check Permissions → Update → Log Changes
   - Delete Path: Validate Ownership → Delete → Cleanup
3. JSON Parser (Format response)
4. HTTP Response (Return results)
```

## Performance Optimization

### Efficient Querying Patterns

```javascript
// Optimized query with strategic includes
const optimizedQuery = {
  table: 'posts',
  include: [
    'author:id,name,avatar', // Only load needed author fields
    'categories:name,slug'   // Only load needed category fields
  ],
  filters: {
    status: 'published',
    'published_at|>': '2024-01-01'
  },
  sort: { published_at: 'desc' },
  limit: 20
};
```

### Pagination Best Practices

```javascript
class PaginatedQuery {
  static async getPaginatedResults(table, filters = {}, page = 1, limit = 20) {
    const offset = (page - 1) * limit;
    
    // Get total count for pagination info
    const totalCount = await this.getCount(table, filters);
    
    // Get paginated results
    const results = await queryAllRecords({
      table: table,
      filters: filters,
      limit: limit,
      offset: offset,
      sort: { created_at: 'desc' }
    });
    
    return {
      data: results,
      pagination: {
        current_page: page,
        per_page: limit,
        total: totalCount,
        total_pages: Math.ceil(totalCount / limit),
        has_next_page: page < Math.ceil(totalCount / limit),
        has_prev_page: page > 1
      }
    };
  }
  
  static async getCount(table, filters) {
    const countResult = await queryAllRecords({
      table: table,
      filters: filters,
      limit: 1,
      select: ['COUNT(*) as total']
    });
    
    return countResult[0]?.total || 0;
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Build a basic CRUD API:
1. Create endpoints for user management
2. Add input validation and error handling
3. Implement basic filtering and sorting
4. Test all operations with sample data

### Intermediate Challenge
Build advanced data workflows:
1. Implement soft delete with restore functionality
2. Add change tracking and audit logs
3. Create batch operations for bulk updates
4. Build search with multiple filter criteria

### Advanced Challenge
Create enterprise data management:
1. Implement database transactions for complex workflows
2. Add data validation and business rules
3. Create automated data archival system
4. Build performance monitoring and optimization

## Common Database Mistakes to Avoid

1. **No input validation** - Always validate data before database operations
2. **Missing error handling** - Handle database errors gracefully
3. **Inefficient queries** - Use appropriate filtering and pagination
4. **No access control** - Validate user permissions for data operations
5. **Ignoring relationships** - Plan for data relationships and integrity

## Database Function Reference

### Quick Function Summary

```yaml
Read Operations:
  - Query All Records: Multiple records with filtering
  - Get Record: Single record by ID
  - Get Database Schema: Table structure information

Write Operations:
  - Add Record: Create new record
  - Edit Record: Complete record update
  - Patch Record: Partial record update
  - Add or Edit Record: Upsert operation

Delete Operations:
  - Delete Record: Remove single record
  - Bulk Operations: Multiple operations

Advanced:
  - Database Transaction: Atomic operations
  - External Database Query: External system integration
  - Direct Database Query: Raw SQL operations
```

## Next Steps

- Master [Query All Records](query-all-records.md) for advanced filtering
- Learn [Database Transactions](database-transaction.md) for complex workflows
- Explore [External Database Query](external-database-query.md) for integrations
- Understand [Bulk Operations](bulk-operations.md) for efficiency

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Database operation discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step database guides
- 📖 [Advanced Patterns](../../best-practices/database-patterns.md) - Professional database techniques
- 🔧 [Support](https://xano.com/support) - Database optimization assistance