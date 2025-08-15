---
title: "External Filtering Examples - Advanced Query Patterns"
description: "Master complex external filtering in Xano with practical examples for dynamic queries, advanced operators, and multi-condition filtering patterns"
category: function-stack
tags:
  - External Filtering
  - Query Operations
  - Database Filtering
  - Advanced Queries
  - Dynamic Filters
  - Conditional Logic
  - Search Patterns
  - Data Retrieval
difficulty: advanced
reading_time: 15 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of Query All Records function
  - Knowledge of database filtering concepts
  - Familiarity with JSON structure
  - Basic understanding of logical operators
---

# External Filtering Examples - Advanced Query Patterns

## 📋 **Quick Summary**

**What it does:** External filtering enables you to build complex, dynamic database queries with multiple conditions, logical operators, and advanced patterns that go beyond simple filtering.

**Why it matters:** External filtering enables you to:
- **Build dynamic search interfaces** with multiple filter criteria
- **Create complex business logic** with conditional queries
- **Optimize performance** with precise data retrieval
- **Support advanced user interfaces** with sophisticated filtering options
- **Implement real-world query patterns** like e-commerce search and CRM filtering

**Time to implement:** 15-30 minutes for basic patterns, 1-2 hours for complex multi-condition queries

---

## What You'll Learn

- Complete external filtering syntax and structure
- Practical examples for all major operators
- Advanced logical combinations (AND/OR)
- Dynamic filtering patterns for user interfaces
- Performance optimization techniques
- Real-world use cases and implementations

## Understanding External Filtering Structure

External filtering uses a JSON-based query language that allows for complex conditional logic:

```json
{
  "filters": [
    {
      "query": {
        "column": "field_name",
        "op": "operator",
        "right": {
          "operand": "value"
        }
      },
      "or": false,
      "type": "statement"
    }
  ]
}
```

### Key Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **column** | Database field to filter | `"name"`, `"created_at"`, `"user.email"` |
| **op** | Comparison operator | `"="`, `">="`, `"contains"`, `"in"` |
| **operand** | Value to compare against | `"John"`, `100`, `["active", "pending"]` |
| **or** | Logical operator (default: false = AND) | `true` for OR, `false` for AND |
| **type** | Statement type | `"statement"` for basic, `"group"` for nested |

## Basic Filtering Examples

### Simple Equality Filter

```json
{
  "filters": [
    {
      "query": {
        "column": "status",
        "op": "=",
        "right": {
          "operand": "active"
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find all active users
**Xano Implementation:**
```javascript
const activeUsers = await queryAllRecords({
  table: 'users',
  filters: {
    status: 'active'
  }
});
```

### Numeric Comparison

```json
{
  "filters": [
    {
      "query": {
        "column": "age",
        "op": ">=",
        "right": {
          "operand": "18"
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find adult users (18+)

### Date Range Filtering

```json
{
  "filters": [
    {
      "query": {
        "column": "created_at",
        "op": ">=",
        "right": {
          "operand": "2024-01-01"
        }
      },
      "type": "statement"
    },
    {
      "query": {
        "column": "created_at",
        "op": "<=",
        "right": {
          "operand": "2024-12-31"
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find records created in 2024

## Advanced Operator Examples

### Text Search with LIKE/ILIKE

```json
{
  "filters": [
    {
      "query": {
        "column": "name",
        "op": "ilike",
        "right": {
          "operand": "%john%"
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Case-insensitive search for names containing "john"
**Patterns:**
- `"john%"` - Starts with "john"
- `"%john"` - Ends with "john"  
- `"%john%"` - Contains "john"

### Array Membership (IN)

```json
{
  "filters": [
    {
      "query": {
        "column": "status",
        "op": "in",
        "right": {
          "operand": ["pending", "processing", "shipped"]
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find orders with multiple possible statuses

### Between Range

```json
{
  "filters": [
    {
      "query": {
        "column": "price",
        "op": "between",
        "right": {
          "operand": ["100", "1000"]
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find products in a price range

### NULL Checks

```json
{
  "filters": [
    {
      "query": {
        "column": "deleted_at",
        "op": "is",
        "right": {
          "operand": null
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find non-deleted records (soft delete pattern)

## Logical Combinations (AND/OR)

### Multiple AND Conditions

```json
{
  "filters": [
    {
      "query": {
        "column": "status",
        "op": "=",
        "right": {
          "operand": "active"
        }
      },
      "type": "statement"
    },
    {
      "query": {
        "column": "subscription_type",
        "op": "=",
        "right": {
          "operand": "premium"
        }
      },
      "type": "statement"
    },
    {
      "query": {
        "column": "purchase_count",
        "op": ">=",
        "right": {
          "operand": "5"
        }
      },
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find active premium users with 5+ purchases

### OR Conditions

```json
{
  "filters": [
    {
      "query": {
        "column": "status",
        "op": "=",
        "right": {
          "operand": "inactive"
        }
      },
      "type": "statement"
    },
    {
      "query": {
        "column": "account_type",
        "op": "=",
        "right": {
          "operand": "basic"
        }
      },
      "or": true,
      "type": "statement"
    }
  ]
}
```

**Use Case:** Find inactive users OR basic account users

### Complex Grouping: (A AND B) OR (C AND D)

```json
{
  "filters": [
    {
      "filters": [
        {
          "query": {
            "column": "status",
            "op": "=",
            "right": {
              "operand": "active"
            }
          },
          "type": "statement"
        },
        {
          "query": {
            "column": "subscription_type",
            "op": "=",
            "right": {
              "operand": "premium"
            }
          },
          "type": "statement"
        }
      ],
      "type": "group"
    },
    {
      "filters": [
        {
          "query": {
            "column": "trial_active",
            "op": "=",
            "right": {
              "operand": true
            }
          },
          "type": "statement"
        },
        {
          "query": {
            "column": "trial_expires",
            "op": ">",
            "right": {
              "operand": "2024-12-01"
            }
          },
          "type": "statement"
        }
      ],
      "or": true,
      "type": "group"
    }
  ]
}
```

**Use Case:** Find (active premium users) OR (users with active unexpired trials)

## Real-World Implementation Patterns

### E-commerce Product Search

```javascript
// Dynamic product filtering function
class ProductFilter {
  static buildProductFilters(searchCriteria) {
    const filters = [];
    
    // Text search in name or description
    if (searchCriteria.search) {
      filters.push({
        "filters": [
          {
            "query": {
              "column": "name",
              "op": "ilike",
              "right": {
                "operand": `%${searchCriteria.search}%`
              }
            },
            "type": "statement"
          },
          {
            "query": {
              "column": "description",
              "op": "ilike",
              "right": {
                "operand": `%${searchCriteria.search}%`
              }
            },
            "or": true,
            "type": "statement"
          }
        ],
        "type": "group"
      });
    }
    
    // Price range
    if (searchCriteria.min_price) {
      filters.push({
        "query": {
          "column": "price",
          "op": ">=",
          "right": {
            "operand": searchCriteria.min_price.toString()
          }
        },
        "type": "statement"
      });
    }
    
    if (searchCriteria.max_price) {
      filters.push({
        "query": {
          "column": "price",
          "op": "<=",
          "right": {
            "operand": searchCriteria.max_price.toString()
          }
        },
        "type": "statement"
      });
    }
    
    // Category filter
    if (searchCriteria.categories && searchCriteria.categories.length > 0) {
      filters.push({
        "query": {
          "column": "category_id",
          "op": "in",
          "right": {
            "operand": searchCriteria.categories
          }
        },
        "type": "statement"
      });
    }
    
    // Availability
    filters.push({
      "query": {
        "column": "stock_quantity",
        "op": ">",
        "right": {
          "operand": "0"
        }
      },
      "type": "statement"
    });
    
    // Active products only
    filters.push({
      "query": {
        "column": "status",
        "op": "=",
        "right": {
          "operand": "active"
        }
      },
      "type": "statement"
    });
    
    return { filters };
  }
}

// Usage in Xano function stack
const searchFilters = ProductFilter.buildProductFilters({
  search: input.search_term,
  min_price: input.min_price,
  max_price: input.max_price,
  categories: input.category_ids
});

const products = await queryAllRecords({
  table: 'products',
  external_filters: searchFilters,
  sort: { [input.sort_by || 'name']: input.sort_direction || 'asc' },
  limit: input.limit || 24
});
```

### User Management with Complex Permissions

```javascript
// Advanced user filtering with role-based access
class UserManagementFilter {
  static buildUserFilters(currentUser, filterCriteria) {
    const filters = [];
    
    // Base visibility rules
    if (currentUser.role !== 'super_admin') {
      // Regular admins can only see users in their organization
      filters.push({
        "query": {
          "column": "organization_id",
          "op": "=",
          "right": {
            "operand": currentUser.organization_id.toString()
          }
        },
        "type": "statement"
      });
    }
    
    // Status filtering
    if (filterCriteria.status) {
      if (Array.isArray(filterCriteria.status)) {
        filters.push({
          "query": {
            "column": "status",
            "op": "in",
            "right": {
              "operand": filterCriteria.status
            }
          },
          "type": "statement"
        });
      } else {
        filters.push({
          "query": {
            "column": "status",
            "op": "=",
            "right": {
              "operand": filterCriteria.status
            }
          },
          "type": "statement"
        });
      }
    }
    
    // Role filtering
    if (filterCriteria.roles && filterCriteria.roles.length > 0) {
      filters.push({
        "query": {
          "column": "role",
          "op": "in",
          "right": {
            "operand": filterCriteria.roles
          }
        },
        "type": "statement"
      });
    }
    
    // Date range for last login
    if (filterCriteria.last_login_after || filterCriteria.last_login_before) {
      if (filterCriteria.last_login_after && filterCriteria.last_login_before) {
        // Both dates provided - use between
        filters.push({
          "query": {
            "column": "last_login_at",
            "op": "between",
            "right": {
              "operand": [filterCriteria.last_login_after, filterCriteria.last_login_before]
            }
          },
          "type": "statement"
        });
      } else {
        // Single date boundary
        if (filterCriteria.last_login_after) {
          filters.push({
            "query": {
              "column": "last_login_at",
              "op": ">=",
              "right": {
                "operand": filterCriteria.last_login_after
              }
            },
            "type": "statement"
          });
        }
        
        if (filterCriteria.last_login_before) {
          filters.push({
            "query": {
              "column": "last_login_at",
              "op": "<=",
              "right": {
                "operand": filterCriteria.last_login_before
              }
            },
            "type": "statement"
          });
        }
      }
    }
    
    // Search in name or email
    if (filterCriteria.search) {
      filters.push({
        "filters": [
          {
            "query": {
              "column": "name",
              "op": "ilike",
              "right": {
                "operand": `%${filterCriteria.search}%`
              }
            },
            "type": "statement"
          },
          {
            "query": {
              "column": "email",
              "op": "ilike",
              "right": {
                "operand": `%${filterCriteria.search}%`
              }
            },
            "or": true,
            "type": "statement"
          }
        ],
        "type": "group"
      });
    }
    
    return { filters };
  }
}
```

### Analytics and Reporting Filters

```javascript
// Complex reporting filters
class ReportingFilter {
  static buildAnalyticsFilters(reportType, dateRange, segmentation) {
    const filters = [];
    
    // Date range (always required for analytics)
    filters.push({
      "query": {
        "column": "created_at",
        "op": ">=",
        "right": {
          "operand": dateRange.start
        }
      },
      "type": "statement"
    });
    
    filters.push({
      "query": {
        "column": "created_at",
        "op": "<=",
        "right": {
          "operand": dateRange.end
        }
      },
      "type": "statement"
    });
    
    // Report-specific filters
    switch (reportType) {
      case 'revenue':
        // Only completed transactions
        filters.push({
          "query": {
            "column": "status",
            "op": "=",
            "right": {
              "operand": "completed"
            }
          },
          "type": "statement"
        });
        
        // Exclude refunds
        filters.push({
          "query": {
            "column": "type",
            "op": "!=",
            "right": {
              "operand": "refund"
            }
          },
          "type": "statement"
        });
        break;
        
      case 'user_engagement':
        // Active users only
        filters.push({
          "query": {
            "column": "status",
            "op": "=",
            "right": {
              "operand": "active"
            }
          },
          "type": "statement"
        });
        
        // Users with activity in the period
        filters.push({
          "query": {
            "column": "last_activity_at",
            "op": ">=",
            "right": {
              "operand": dateRange.start
            }
          },
          "type": "statement"
        });
        break;
        
      case 'conversion':
        // Trial or freemium users who converted
        filters.push({
          "filters": [
            {
              "query": {
                "column": "previous_plan",
                "op": "=",
                "right": {
                  "operand": "trial"
                }
              },
              "type": "statement"
            },
            {
              "query": {
                "column": "previous_plan",
                "op": "=",
                "right": {
                  "operand": "freemium"
                }
              },
              "or": true,
              "type": "statement"
            }
          ],
          "type": "group"
        });
        
        filters.push({
          "query": {
            "column": "current_plan",
            "op": "in",
            "right": {
              "operand": ["basic", "premium", "enterprise"]
            }
          },
          "type": "statement"
        });
        break;
    }
    
    // Segmentation filters
    if (segmentation.geography && segmentation.geography.length > 0) {
      filters.push({
        "query": {
          "column": "country",
          "op": "in",
          "right": {
            "operand": segmentation.geography
          }
        },
        "type": "statement"
      });
    }
    
    if (segmentation.user_type) {
      filters.push({
        "query": {
          "column": "user_type",
          "op": "=",
          "right": {
            "operand": segmentation.user_type
          }
        },
        "type": "statement"
      });
    }
    
    return { filters };
  }
}
```

## No-Code Platform Integration

### 🔗 **n8n Dynamic Filtering**

```yaml
Dynamic Filter Workflow:
1. Webhook (Receive filter criteria)
2. Function Node (Build external filter JSON)
3. HTTP Request (Query Xano with filters)
4. Function Node (Process and format results)
5. HTTP Response (Return filtered data)
```

**n8n Filter Builder Function:**
```javascript
// Build dynamic external filters
const filterCriteria = $input.body;
const filters = [];

// Text search
if (filterCriteria.search) {
  filters.push({
    "query": {
      "column": "name",
      "op": "ilike",
      "right": {
        "operand": `%${filterCriteria.search}%`
      }
    },
    "type": "statement"
  });
}

// Status filter
if (filterCriteria.status && filterCriteria.status.length > 0) {
  filters.push({
    "query": {
      "column": "status",
      "op": "in",
      "right": {
        "operand": filterCriteria.status
      }
    },
    "type": "statement"
  });
}

// Date range
if (filterCriteria.date_from) {
  filters.push({
    "query": {
      "column": "created_at",
      "op": ">=",
      "right": {
        "operand": filterCriteria.date_from
      }
    },
    "type": "statement"
  });
}

if (filterCriteria.date_to) {
  filters.push({
    "query": {
      "column": "created_at",
      "op": "<=",
      "right": {
        "operand": filterCriteria.date_to
      }
    },
    "type": "statement"
  });
}

// Return the filter structure
return {
  external_filters: { filters },
  table: filterCriteria.table || 'records',
  limit: filterCriteria.limit || 50,
  sort: filterCriteria.sort || { created_at: 'desc' }
};
```

### 🌐 **WeWeb Advanced Search Interface**

```javascript
// WeWeb dynamic search with external filtering
class WeWebAdvancedSearch {
  constructor(tableName) {
    this.tableName = tableName;
    this.filters = [];
    this.currentFilters = {};
  }
  
  // Add text search filter
  addTextSearch(fields, searchTerm) {
    if (!searchTerm) return this;
    
    const textFilters = fields.map((field, index) => ({
      "query": {
        "column": field,
        "op": "ilike",
        "right": {
          "operand": `%${searchTerm}%`
        }
      },
      "or": index > 0,
      "type": "statement"
    }));
    
    this.filters.push({
      "filters": textFilters,
      "type": "group"
    });
    
    return this;
  }
  
  // Add status filter
  addStatusFilter(statuses) {
    if (!statuses || statuses.length === 0) return this;
    
    this.filters.push({
      "query": {
        "column": "status",
        "op": "in",
        "right": {
          "operand": statuses
        }
      },
      "type": "statement"
    });
    
    return this;
  }
  
  // Add date range filter
  addDateRange(column, startDate, endDate) {
    if (startDate) {
      this.filters.push({
        "query": {
          "column": column,
          "op": ">=",
          "right": {
            "operand": startDate
          }
        },
        "type": "statement"
      });
    }
    
    if (endDate) {
      this.filters.push({
        "query": {
          "column": column,
          "op": "<=",
          "right": {
            "operand": endDate
          }
        },
        "type": "statement"
      });
    }
    
    return this;
  }
  
  // Add numeric range filter
  addNumericRange(column, min, max) {
    if (min !== null && min !== undefined) {
      this.filters.push({
        "query": {
          "column": column,
          "op": ">=",
          "right": {
            "operand": min.toString()
          }
        },
        "type": "statement"
      });
    }
    
    if (max !== null && max !== undefined) {
      this.filters.push({
        "query": {
          "column": column,
          "op": "<=",
          "right": {
            "operand": max.toString()
          }
        },
        "type": "statement"
      });
    }
    
    return this;
  }
  
  // Execute the search
  async execute(options = {}) {
    const searchConfig = {
      external_filters: { filters: this.filters },
      sort: options.sort || { created_at: 'desc' },
      limit: options.limit || 50,
      offset: options.offset || 0
    };
    
    try {
      const response = await wwLib.api.post({
        url: `${wwLib.envVars.XANO_API_URL}/search/${this.tableName}`,
        data: searchConfig,
        headers: {
          'Authorization': 'Bearer ' + wwLib.auth.getAuthToken(),
          'Content-Type': 'application/json'
        }
      });
      
      return {
        success: true,
        data: response.data,
        total: response.data.length
      };
      
    } catch (error) {
      console.error('Search failed:', error);
      return {
        success: false,
        error: error.message,
        data: []
      };
    }
  }
  
  // Clear all filters
  clear() {
    this.filters = [];
    return this;
  }
}

// Usage in WeWeb
const productSearch = new WeWebAdvancedSearch('products');

async function performProductSearch() {
  const searchTerm = wwLib.form.getValue('search');
  const selectedCategories = wwLib.form.getValue('categories');
  const minPrice = wwLib.form.getValue('min_price');
  const maxPrice = wwLib.form.getValue('max_price');
  const dateFrom = wwLib.form.getValue('date_from');
  const dateTo = wwLib.form.getValue('date_to');
  
  const results = await productSearch
    .clear()
    .addTextSearch(['name', 'description'], searchTerm)
    .addStatusFilter(['active', 'featured'])
    .addNumericRange('price', minPrice, maxPrice)
    .addDateRange('created_at', dateFrom, dateTo)
    .execute({
      sort: { name: 'asc' },
      limit: 20
    });
  
  if (results.success) {
    wwLib.collections.products.update(results.data);
    wwLib.showAlert(`Found ${results.total} products`);
  } else {
    wwLib.showAlert('Search failed: ' + results.error);
  }
}
```

## Performance Optimization

### Efficient Filtering Patterns

```javascript
// Optimized external filtering for performance
class OptimizedFiltering {
  static buildIndexedFilters(criteria) {
    const filters = [];
    
    // Always filter by indexed columns first
    if (criteria.status) {
      filters.push({
        "query": {
          "column": "status", // Ensure this column is indexed
          "op": "=",
          "right": {
            "operand": criteria.status
          }
        },
        "type": "statement"
      });
    }
    
    // Use precise date ranges instead of open-ended queries
    if (criteria.date_range) {
      filters.push({
        "query": {
          "column": "created_at", // Ensure this column is indexed
          "op": "between",
          "right": {
            "operand": [criteria.date_range.start, criteria.date_range.end]
          }
        },
        "type": "statement"
      });
    }
    
    // Limit text searches to specific needs
    if (criteria.search && criteria.search.length >= 3) { // Minimum 3 characters
      filters.push({
        "query": {
          "column": "search_vector", // Use full-text search if available
          "op": "@@",
          "right": {
            "operand": criteria.search
          }
        },
        "type": "statement"
      });
    }
    
    return { filters };
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Create basic external filters:
1. Build a simple status filter
2. Add text search functionality
3. Implement date range filtering
4. Test with sample data

### Intermediate Challenge
Build complex search interface:
1. Combine multiple filter types
2. Implement OR logic between groups
3. Add dynamic filter building
4. Create filter presets for common searches

### Advanced Challenge
Create enterprise search system:
1. Build role-based filtering
2. Implement complex nested conditions
3. Add search analytics and optimization
4. Create filter performance monitoring

## Common External Filtering Mistakes

1. **No index optimization** - Filter by indexed columns first
2. **Overly complex queries** - Simplify logic where possible
3. **Missing input validation** - Validate filter values before queries
4. **No performance limits** - Set reasonable limits on results
5. **Poor error handling** - Handle malformed filter JSON gracefully

## Quick Reference Guide

### Operator Reference

```yaml
Comparison Operators:
  - "=": Equality
  - "!=": Not equal
  - ">": Greater than
  - ">=": Greater than or equal
  - "<": Less than
  - "<=": Less than or equal
  - "between": Range (requires array)

Text Operators:
  - "like": Case-sensitive pattern matching
  - "ilike": Case-insensitive pattern matching
  - "contains": String contains
  - "starts_with": String starts with
  - "ends_with": String ends with

Array Operators:
  - "in": Value in array
  - "not_in": Value not in array

Null Operators:
  - "is": IS NULL (operand: null)
  - "is_not": IS NOT NULL (operand: null)
```

## Next Steps

- Master [Query All Records](query-all-records.md) for basic filtering
- Learn [Database Requests](database-requests.md) for complete CRUD operations
- Explore [Data Manipulation](data-manipulation.md) for processing results
- Understand [Performance Optimization](../best-practices/performance.md)

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - External filtering discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Query building guides
- 📖 [Advanced Patterns](../../best-practices/query-optimization.md) - Performance techniques
- 🔧 [Support](https://xano.com/support) - Complex query assistance