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
- Expressions
- Comparison Operators
- Conditionals
- Data Validation
- n8n
- WeWeb
- Logic
title: 'Right Value & Comparison Operators'
---

# Right Value & Comparison Operators

## 📋 **Quick Summary**
Master right values and comparison operators in Xano expressions for creating dynamic conditionals, data validation, and complex business logic. Essential for building intelligent filters, user permissions, and automated decision-making in your n8n and WeWeb applications.

## 🎯 **Core Concepts**

### Understanding Right Values
The **right value** is the comparison target in any conditional expression. It's what you compare your left value (variable, field, or expression) against to make decisions in your function stacks.

**Components of a Comparison:**
- **Left Value**: The data you're evaluating (variable, database field, API response)
- **Operator**: The comparison method (equals, greater than, contains, etc.)
- **Right Value**: The target value you're comparing against

### Types of Right Values
- **Hardcoded Values**: Static numbers, text, or booleans
- **Variables**: Dynamic values from previous function steps
- **Database Fields**: Values from the current record or related records
- **Expressions**: Calculated values using functions or operations

## 🔧 **Comparison Operators Guide**

### Equality Operators

#### Equals (==) - Exact Match
```javascript
// Basic equality comparison
{
  "conditional_example": {
    "left_value": "{{user.subscription_status}}",
    "operator": "==",
    "right_value": "active",
    "description": "Check if user has active subscription"
  },
  
  "use_cases": [
    "Status validation",
    "Type checking", 
    "Simple value matching",
    "Boolean comparisons"
  ]
}
```

#### Strict Equals (===) - Value and Type Match
```javascript
// Type-sensitive equality
{
  "strict_comparison": {
    "scenario": "Age verification with type checking",
    "left_value": "{{user.age}}",
    "operator": "===",
    "right_value": 18,
    "note": "Fails if age is '18' (string) instead of 18 (number)"
  },
  
  "practical_example": {
    "function_stack": [
      {
        "function": "Get Record",
        "table": "users",
        "record_id": "{{input.user_id}}"
      },
      {
        "function": "Conditional",
        "condition": "{{users.age === 18}}",
        "true_functions": [
          {
            "function": "Return Response",
            "body": {"eligible": true, "message": "Exact age match"}
          }
        ]
      }
    ]
  }
}
```

#### Not Equals (!=) and Strict Not Equals (!==)
```javascript
// Exclusion comparisons
{
  "exclusion_examples": {
    "not_equals": {
      "left_value": "{{order.status}}",
      "operator": "!=",
      "right_value": "cancelled",
      "description": "Process all orders except cancelled ones"
    },
    
    "strict_not_equals": {
      "left_value": "{{product.price}}",
      "operator": "!==",
      "right_value": 0,
      "description": "Exclude free products (type-sensitive)"
    }
  }
}
```

### Numerical Comparisons

#### Greater Than (>) and Greater Than or Equal (>=)
```javascript
// Numerical range comparisons
{
  "numerical_comparisons": {
    "discount_eligibility": {
      "function_stack": [
        {
          "function": "Conditional",
          "condition": "{{cart.total > 100}}",
          "true_functions": [
            {
              "function": "Create Variable",
              "name": "discount_percentage",
              "value": 10
            }
          ]
        },
        {
          "function": "Conditional",
          "condition": "{{user.loyalty_points >= 500}}",
          "true_functions": [
            {
              "function": "Create Variable",
              "name": "free_shipping",
              "value": true
            }
          ]
        }
      ]
    }
  }
}
```

#### Less Than (<) and Less Than or Equal (<=)
```javascript
// Limitation and threshold checking
{
  "threshold_examples": {
    "inventory_check": {
      "condition": "{{product.stock < 10}}",
      "action": "Send low stock alert"
    },
    
    "user_limits": {
      "condition": "{{user.api_calls_today <= 1000}}",
      "action": "Allow API access"
    },
    
    "time_based_logic": {
      "condition": "{{days_since_signup <= 7}}",
      "action": "Show new user onboarding"
    }
  }
}
```

### Text Comparison Operators

#### LIKE - Case-Insensitive Text Matching
```javascript
// Flexible text comparisons
{
  "text_matching": {
    "case_insensitive_search": {
      "left_value": "{{user.name}}",
      "operator": "LIKE",
      "right_value": "john",
      "matches": ["John", "JOHN", "john", "JoHn"]
    },
    
    "practical_implementation": {
      "function_stack": [
        {
          "function": "Get Records",
          "table": "customers",
          "filter": {
            "name": {"$like": "{{search_term}}"}
          }
        }
      ]
    }
  }
}
```

#### INCLUDES - Partial Text Matching
```javascript
// Substring detection
{
  "partial_matching": {
    "email_domain_check": {
      "left_value": "{{user.email}}",
      "operator": "INCLUDES",
      "right_value": "@company.com",
      "description": "Check if user has company email"
    },
    
    "tag_filtering": {
      "left_value": "{{post.tags}}",
      "operator": "INCLUDES", 
      "right_value": "urgent",
      "description": "Find posts with urgent tag"
    }
  }
}
```

### Array and Collection Operators

#### IN - Value Exists in Array
```javascript
// Check membership in collections
{
  "array_membership": {
    "role_verification": {
      "left_value": "{{user.role}}",
      "operator": "IN",
      "right_value": ["admin", "moderator", "editor"],
      "description": "Check if user has privileged role"
    },
    
    "category_filtering": {
      "left_value": "{{product.category_id}}",
      "operator": "IN", 
      "right_value": "{{allowed_categories}}",
      "description": "Filter products by allowed categories"
    }
  }
}
```

#### OVERLAPS - Array Intersection
```javascript
// Compare arrays for common elements
{
  "array_intersection": {
    "permission_check": {
      "left_value": "{{user.permissions}}",
      "operator": "OVERLAPS",
      "right_value": "{{required_permissions}}",
      "description": "User has at least one required permission"
    },
    
    "tag_matching": {
      "left_value": "{{post.tags}}",
      "operator": "OVERLAPS",
      "right_value": "{{user_interests}}",
      "description": "Show posts matching user interests"
    }
  }
}
```

### Advanced Comparison Patterns

#### REGEX MATCHES - Pattern Matching
```javascript
// Regular expression comparisons
{
  "pattern_matching": {
    "email_validation": {
      "left_value": "{{user.email}}",
      "operator": "REGEX MATCHES",
      "right_value": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
      "description": "Validate email format"
    },
    
    "phone_format": {
      "left_value": "{{user.phone}}",
      "operator": "REGEX MATCHES",
      "right_value": "^\\+?[1-9]\\d{1,14}$",
      "description": "International phone format"
    }
  }
}
```

#### CONTAINS - JSON Schema Matching
```javascript
// Deep object comparisons
{
  "json_matching": {
    "nested_object_check": {
      "left_value": "{{user.profile}}",
      "operator": "CONTAINS",
      "right_value": {"preferences": {"newsletter": true}},
      "description": "Check if user opted in to newsletter"
    },
    
    "metadata_filtering": {
      "left_value": "{{product.metadata}}",
      "operator": "CONTAINS",
      "right_value": {"features": ["organic", "gluten-free"]},
      "description": "Find products with specific features"
    }
  }
}
```

## 🔗 **n8n Integration Examples**

### Dynamic Filtering with Right Values
```javascript
// n8n workflow with dynamic comparisons
{
  "n8n_filtering_workflow": {
    "nodes": [
      {
        "node": "Webhook",
        "description": "Receive filter criteria"
      },
      {
        "node": "Set Variables",
        "variables": {
          "filter_field": "{{$json.field}}",
          "filter_operator": "{{$json.operator}}",
          "filter_value": "{{$json.value}}"
        }
      },
      {
        "node": "HTTP Request",
        "method": "POST",
        "url": "{{xano_instance}}/api/filtered-data",
        "body": {
          "field": "{{$node.Set_Variables.json.filter_field}}",
          "operator": "{{$node.Set_Variables.json.filter_operator}}",
          "value": "{{$node.Set_Variables.json.filter_value}}"
        }
      }
    ],
    
    "xano_function_stack": [
      {
        "function": "Create Variable",
        "name": "dynamic_filter",
        "value": {
          "{{input.field}}": {
            "{{input.operator}}": "{{input.value}}"
          }
        }
      },
      {
        "function": "Get Records",
        "table": "products",
        "filter": "{{dynamic_filter}}"
      }
    ]
  }
}
```

### Conditional Logic Chain
```javascript
// Complex decision making with multiple comparisons
{
  "conditional_chain": {
    "pricing_logic": [
      {
        "function": "Conditional",
        "condition": "{{user.subscription_tier === 'premium'}}",
        "true_functions": [
          {
            "function": "Create Variable",
            "name": "discount",
            "value": 20
          }
        ]
      },
      {
        "function": "Conditional",
        "condition": "{{order.total >= 200}}",
        "true_functions": [
          {
            "function": "Update Variable",
            "variable": "discount",
            "value": "{{discount + 10}}"
          }
        ]
      },
      {
        "function": "Conditional",
        "condition": "{{user.referral_count > 5}}",
        "true_functions": [
          {
            "function": "Update Variable", 
            "variable": "discount",
            "value": "{{discount + 5}}"
          }
        ]
      }
    ]
  }
}
```

## 🌐 **WeWeb Integration**

### Dynamic Form Validation
```javascript
// WeWeb form validation using Xano comparisons
{
  "weweb_validation": {
    "form_component": "User Registration Form",
    "validation_rules": [
      {
        "field": "email",
        "xano_endpoint": "/api/validate-field",
        "validation": {
          "left_value": "{{email}}",
          "operator": "REGEX MATCHES",
          "right_value": "email_pattern"
        }
      },
      {
        "field": "age",
        "validation": {
          "left_value": "{{age}}",
          "operator": ">=",
          "right_value": 13
        }
      },
      {
        "field": "username",
        "xano_endpoint": "/api/check-username",
        "validation": {
          "left_value": "{{existing_usernames}}",
          "operator": "NOT IN",
          "right_value": "{{username}}"
        }
      }
    ]
  }
}
```

### Real-Time Data Filtering
```javascript
// WeWeb data filtering with dynamic right values
{
  "realtime_filtering": {
    "component": "Product List",
    "filter_controls": [
      {
        "type": "price_range",
        "min_condition": "{{product.price >= selected_min_price}}",
        "max_condition": "{{product.price <= selected_max_price}}"
      },
      {
        "type": "category_select",
        "condition": "{{product.category IN selected_categories}}"
      },
      {
        "type": "search_text",
        "condition": "{{product.name INCLUDES search_term}}"
      }
    ],
    
    "implementation": `
// WeWeb component logic
const filteredProducts = products.filter(product => {
  // Price range check
  if (selectedMinPrice && product.price < selectedMinPrice) return false;
  if (selectedMaxPrice && product.price > selectedMaxPrice) return false;
  
  // Category filter
  if (selectedCategories.length && !selectedCategories.includes(product.category)) return false;
  
  // Search term
  if (searchTerm && !product.name.toLowerCase().includes(searchTerm.toLowerCase())) return false;
  
  return true;
});`
  }
}
```

## 🎯 **Best Practices**

### Type Safety and Validation
```javascript
// Ensure type consistency for reliable comparisons
{
  "type_safety": {
    "best_practices": [
      {
        "rule": "Use strict equality (===) for type-sensitive comparisons",
        "example": "{{user.id === parseInt(input.user_id)}}"
      },
      {
        "rule": "Convert types before comparison when necessary",
        "example": "{{toString(product.price) LIKE discount_code}}"
      },
      {
        "rule": "Validate data types before complex operations",
        "example": "{{typeof(user.age) === 'number' && user.age >= 18}}"
      }
    ]
  }
}
```

### Performance Optimization
```javascript
// Optimize comparisons for better performance
{
  "performance_tips": {
    "database_queries": [
      "Use indexed fields as left values when possible",
      "Prefer IN operator over multiple OR conditions",
      "Use LIKE sparingly on large text fields"
    ],
    
    "complex_conditions": [
      "Order conditions by likelihood (most likely first)",
      "Use early returns to avoid unnecessary comparisons",
      "Cache frequently used right values as variables"
    ]
  }
}
```

### Security Considerations
```javascript
// Secure comparison practices
{
  "security_guidelines": {
    "input_validation": [
      "Always validate user input before comparisons",
      "Sanitize text inputs to prevent injection attacks",
      "Use parameterized queries for database comparisons"
    ],
    
    "sensitive_data": [
      "Never expose sensitive values in comparison errors",
      "Use secure comparison methods for passwords/tokens",
      "Log comparison failures for security monitoring"
    ]
  }
}
```

---

*Right values and comparison operators form the foundation of intelligent decision-making in Xano applications. Master these patterns to build sophisticated business logic, user permissions, and automated workflows that respond dynamically to your data.*