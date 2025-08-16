---
title: Complete Filters Reference Guide - Master Data Processing for No-Code Development
description: Comprehensive guide to all Xano filters organized by category including text manipulation, array operations, mathematical functions, security filters, and advanced transformations for n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: beginner-to-advanced
last_updated: '2025-01-16'
related_docs:
  - array-filters.md
  - text-filters.md
  - security-filters.md
  - filter-examples.md
tags:
  - filters-reference
  - data-processing
  - text-manipulation
  - array-operations
  - mathematical-functions
  - security-filters
  - transformations
---

## 📋 **Quick Summary**

Master all Xano filters with this comprehensive reference guide. Organized by category, this guide covers text manipulation, array operations, mathematical functions, security filters, conversions, and advanced transformations essential for building powerful no-code applications with n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Complete filter catalog organized by functionality
- Best practices for filter selection and usage
- Performance considerations and optimization tips
- Integration patterns for common use cases
- Filter chaining and composition techniques
- Troubleshooting and debugging filter operations

# Complete Filters Reference Guide

## 🗂️ **Filter Categories Overview**

Xano filters are organized into logical categories based on their functionality. Understanding these categories helps you quickly find the right filter for your data processing needs.

### Filter Categories:
1. **[Text Filters](#text-filters)** - String manipulation and formatting
2. **[Array Filters](#array-filters)** - Array operations and transformations
3. **[Mathematical Filters](#mathematical-filters)** - Numeric operations and calculations
4. **[Comparison Filters](#comparison-filters)** - Value comparison and validation
5. **[Conversion Filters](#conversion-filters)** - Data type conversion and encoding
6. **[Security Filters](#security-filters)** - Encryption, hashing, and security operations
7. **[Timestamp Filters](#timestamp-filters)** - Date and time manipulation
8. **[Object Manipulation Filters](#object-manipulation-filters)** - Object property operations
9. **[Conditional Filters](#conditional-filters)** - Logic and flow control
10. **[Transform Filters](#transform-filters)** - Advanced data transformations

## 📝 **Text Filters**

### String Manipulation
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `uppercase` | Convert to uppercase | User input normalization |
| `lowercase` | Convert to lowercase | Email address processing |
| `trim` | Remove whitespace | Form input cleaning |
| `substring` | Extract text portion | Display truncated content |
| `replace` | Replace text patterns | Data sanitization |
| `split` | Split into array | CSV processing |
| `length` | Get string length | Validation and limits |

**Example Usage:**
```javascript
// n8n: Clean and format user input
const cleanEmail = userInput.email
  .trim()
  .lowercase()
  .replace(/[^a-z0-9@._-]/g, '');

// WeWeb: Format display names
const displayName = userData.name
  .trim()
  .replace(/\s+/g, ' ')
  .substring(0, 50);
```

### Text Formatting
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `capitalize` | Capitalize first letter | Name formatting |
| `title_case` | Title case formatting | Heading display |
| `slug` | Create URL-friendly text | SEO-friendly URLs |
| `strip_tags` | Remove HTML tags | Content sanitization |
| `nl2br` | Convert newlines to `<br>` | Text display formatting |

**Example Usage:**
```javascript
// Make.com: Create SEO-friendly URLs
const articleUrl = articleTitle
  .lowercase()
  .replace(/[^a-z0-9\s-]/g, '')
  .replace(/\s+/g, '-')
  .trim('-');
```

### Text Validation
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `is_email` | Validate email format | Form validation |
| `is_url` | Validate URL format | Link verification |
| `is_numeric` | Check if numeric | Input validation |
| `contains` | Check for substring | Content filtering |
| `starts_with` | Check prefix | Category filtering |
| `ends_with` | Check suffix | File type validation |

## 🔢 **Array Filters**

### Array Creation and Population
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `fill` | Create filled array | Initialize form fields |
| `fill_keys` | Create object template | API response structure |
| `range` | Generate number sequence | Pagination controls |
| `safe_array` | Ensure array format | Input normalization |

**Example Usage:**
```javascript
// WeWeb: Initialize form with default fields
const formFields = "".fill(0, 5);
const formTemplate = ["name", "email", "phone", "company", "message"]
  .fill_keys("");
```

### Array Manipulation
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `append` | Add to end | Build dynamic lists |
| `prepend` | Add to beginning | Priority items |
| `merge` | Combine arrays | Data aggregation |
| `slice` | Extract portion | Pagination |
| `sort` | Sort elements | Data ordering |
| `reverse` | Reverse order | Display latest first |
| `shuffle` | Random order | Content randomization |

### Array Analysis
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `count` | Get length | Display totals |
| `sum` | Calculate total | Financial calculations |
| `average` | Calculate mean | Statistics |
| `min` | Find minimum | Data analysis |
| `max` | Find maximum | Limit checking |
| `first` | Get first element | Default selection |
| `last` | Get last element | Latest entry |

### Array Filtering
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `filter_empty` | Remove empty values | Data cleaning |
| `filter_null` | Remove null values | Null safety |
| `unique` | Remove duplicates | Data deduplication |
| `remove` | Remove specific values | Content filtering |
| `diff` | Find differences | Change detection |
| `intersect` | Find common elements | Overlap analysis |

## 🔢 **Mathematical Filters**

### Basic Arithmetic
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `add` | Addition | Price calculations |
| `subtract` | Subtraction | Discount application |
| `multiply` | Multiplication | Quantity pricing |
| `divide` | Division | Average calculations |
| `modulo` | Remainder | Pagination logic |
| `abs` | Absolute value | Distance calculations |
| `round` | Round to nearest | Currency formatting |

**Example Usage:**
```javascript
// n8n: Calculate order totals
const subtotal = orderItems
  .map(item => item.price.multiply(item.quantity))
  .sum();

const tax = subtotal.multiply(0.08).round(2);
const total = subtotal.add(tax);
```

### Advanced Math
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `ceil` | Round up | Pagination pages |
| `floor` | Round down | Bulk pricing tiers |
| `power` | Exponentiation | Growth calculations |
| `sqrt` | Square root | Distance formulas |
| `min` | Minimum value | Limit enforcement |
| `max` | Maximum value | Cap calculations |

### Number Validation
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `even` | Check if even | Alternating logic |
| `odd` | Check if odd | Row styling |
| `positive` | Check if positive | Validation |
| `negative` | Check if negative | Balance checks |
| `zero` | Check if zero | Empty state logic |

## ⚖️ **Comparison Filters**

### Basic Comparisons
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `equals` | Exact match | Status checking |
| `not_equals` | Not equal | Exclusion logic |
| `greater_than` | Greater than | Threshold checks |
| `less_than` | Less than | Limit validation |
| `greater_equal` | Greater or equal | Minimum requirements |
| `less_equal` | Less or equal | Maximum limits |

### Advanced Comparisons
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `between` | Within range | Age validation |
| `in_array` | Value in list | Category validation |
| `not_in_array` | Value not in list | Exclusion logic |
| `is_empty` | Check if empty | Validation |
| `is_null` | Check if null | Null safety |
| `is_defined` | Check if exists | Property validation |

**Example Usage:**
```javascript
// WeWeb: User access control
const hasAccess = userAge.greater_equal(18)
  && userRole.in_array(["admin", "moderator", "member"])
  && userStatus.equals("active");
```

## 🔄 **Conversion Filters**

### Data Type Conversion
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `to_text` | Convert to string | Display formatting |
| `to_int` | Convert to integer | Numeric operations |
| `to_dec` | Convert to decimal | Precise calculations |
| `to_bool` | Convert to boolean | Logic operations |
| `to_timestamp` | Convert to timestamp | Date operations |

### Encoding/Decoding
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `base64_encode` | Base64 encoding | File transmission |
| `base64_decode` | Base64 decoding | File processing |
| `url_encode` | URL encoding | Safe URLs |
| `url_decode` | URL decoding | Parameter processing |
| `json_encode` | JSON encoding | Data serialization |
| `json_decode` | JSON decoding | Data parsing |

### Format Conversion
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `csv_encode` | CSV formatting | Data export |
| `csv_decode` | CSV parsing | Data import |
| `yaml_encode` | YAML formatting | Configuration export |
| `yaml_decode` | YAML parsing | Configuration import |

**Example Usage:**
```javascript
// Make.com: Data format conversion
const exportData = databaseRecords
  .map(record => [
    record.id.to_text(),
    record.name,
    record.created_at.format_date()
  ])
  .csv_encode();
```

## 🔐 **Security Filters**

### Hashing
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `md5` | MD5 hash | Legacy systems |
| `sha1` | SHA1 hash | Git-like systems |
| `sha256` | SHA256 hash | Secure hashing |
| `sha512` | SHA512 hash | High security |

### HMAC Authentication
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `hmac_sha256` | HMAC SHA256 | API signatures |
| `hmac_sha512` | HMAC SHA512 | High-security auth |

### Encryption
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `encrypt` | Encrypt data | Sensitive storage |
| `decrypt` | Decrypt data | Data retrieval |
| `jwe_encode` | JWE token creation | Secure tokens |
| `jwe_decode` | JWE token parsing | Token validation |

### ID Security
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `create_uid` | Generate UID | Unique identifiers |
| `secureid_encode` | Encode database ID | URL security |
| `secureid_decode` | Decode secure ID | Database lookup |

**Example Usage:**
```javascript
// n8n: Secure API communication
const apiSignature = requestBody
  .json_encode()
  .hmac_sha256(apiSecret);

const secureHeaders = {
  'X-Signature': `sha256=${apiSignature}`,
  'X-Timestamp': Date.now().to_text()
};
```

## 📅 **Timestamp Filters**

### Date Formatting
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `format_date` | Format date display | User interfaces |
| `format_timestamp` | Format with time | Detailed timestamps |
| `iso_date` | ISO 8601 format | API standardization |
| `relative_time` | Human-readable time | Social features |

### Date Calculations
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `add_days` | Add days | Deadline calculation |
| `subtract_days` | Subtract days | Historical analysis |
| `add_hours` | Add hours | Scheduling |
| `add_minutes` | Add minutes | Precise timing |
| `start_of_day` | Day beginning | Daily aggregation |
| `end_of_day` | Day end | Cutoff times |

### Date Analysis
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `age` | Calculate age | User demographics |
| `days_between` | Days difference | Duration calculation |
| `is_weekend` | Check weekend | Business logic |
| `is_past` | Check if past | Validation |
| `is_future` | Check if future | Scheduling validation |

**Example Usage:**
```javascript
// WeWeb: Event scheduling
const eventDate = userInput.eventDate.to_timestamp();
const isValidDate = eventDate.is_future();
const daysUntil = eventDate.days_between("now");
const formattedDate = eventDate.format_date("MMM DD, YYYY");
```

## 🎯 **Object Manipulation Filters**

### Property Access
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `get` | Safe property access | API response handling |
| `has` | Check property exists | Conditional logic |
| `set` | Set property value | Data construction |
| `unset` | Remove property | Data cleaning |

### Conditional Setting
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `set_conditional` | Conditional property set | Dynamic properties |
| `set_ifnotempty` | Set if not empty | Partial updates |
| `set_ifnotnull` | Set if not null | Null safety |

### Object Transformation
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `pick` | Select properties | Data projection |
| `unpick` | Exclude properties | Sensitive data removal |
| `keys` | Get property names | Dynamic processing |
| `values` | Get property values | Value extraction |

**Example Usage:**
```javascript
// n8n: Safe API response processing
const processedData = apiResponse
  .get("data.results", [])
  .map(item => item
    .pick(["id", "name", "status", "created_at"])
    .set_conditional("is_new", true, item.created_at.is_recent(7))
  );
```

## 🔀 **Conditional Filters**

### Value Selection
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `first_notempty` | First non-empty value | Fallback logic |
| `first_notnull` | First non-null value | Null handling |
| `default` | Default value | Missing data handling |

### Conditional Logic
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `if_then_else` | Ternary operation | Conditional display |
| `switch` | Multi-condition logic | Status mapping |
| `case_when` | Complex conditions | Business rules |

**Example Usage:**
```javascript
// Make.com: Dynamic pricing logic
const finalPrice = basePrice
  .multiply(
    customerType.equals("premium") ? 0.9 :
    customerType.equals("student") ? 0.8 :
    1.0
  )
  .round(2);
```

## 🔄 **Transform Filters**

### Universal Transform
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `transform` | Universal transformation | Complex data mapping |
| `map` | Array transformation | Data projection |
| `filter` | Array filtering | Data selection |
| `reduce` | Array reduction | Aggregation |

### Advanced Transforms
| Filter | Purpose | Example Use Case |
|--------|---------|------------------|
| `group_by` | Group data | Categorization |
| `flatten` | Flatten structure | Data normalization |
| `pivot` | Pivot data | Report formatting |
| `aggregate` | Aggregate values | Statistics |

**Example Usage:**
```javascript
// WeWeb: Complex data transformation
const dashboardData = userData.transform(`
  {
    summary: {
      totalUsers: $$|count,
      activeUsers: $$|filter:($$.status == "active")|count,
      avgAge: $$|filter:($$.age > 0)|average:age
    },
    byRegion: $$|group_by:region|map:(
      {
        region: $$.key,
        count: $$.items|count,
        avgRevenue: $$.items|average:revenue
      }
    )
  }
`);
```

## 💡 **Filter Selection Best Practices**

### Performance Considerations

**Efficient Filter Chaining:**
```javascript
// ✅ GOOD: Chain operations efficiently
const result = data
  .filter_empty()
  .unique("id")
  .sort("created_at", "desc")
  .slice(0, 10);

// ❌ AVOID: Multiple separate operations
let result = data;
result = result.filter_empty();
result = result.unique("id");
result = result.sort("created_at", "desc");
result = result.slice(0, 10);
```

**Choose Specific Filters:**
```javascript
// ✅ GOOD: Use specific filters
data.filter_null()        // Better than filter_empty for nulls
data.filter_empty_text()  // Better than filter_empty for strings

// ❌ AVOID: Generic filters when specific ones exist
data.filter_empty()       // Less efficient for specific cases
```

### Filter Categories by Use Case

**Data Validation Pipeline:**
```javascript
const validateUserData = (userData) => {
  return userData
    .set_ifnotempty("email", userData.email?.lowercase().trim())
    .set_conditional("email_valid", true, userData.email?.is_email())
    .set_ifnotempty("age", userData.age?.to_int())
    .set_conditional("age_valid", true, userData.age?.between(13, 120))
    .unset("password"); // Remove sensitive data
};
```

**Data Transformation Pipeline:**
```javascript
const processOrderData = (orders) => {
  return orders
    .filter_empty()
    .map(order => order
      .set("total", order.items.sum("price"))
      .set("tax", order.total.multiply(0.08).round(2))
      .set("formatted_date", order.created_at.format_date("MMM DD, YYYY"))
    )
    .sort("created_at", "desc")
    .slice(0, 50);
};
```

## 🚨 **Common Filter Pitfalls**

### Type Safety
```javascript
// ❌ DANGEROUS: No type checking
const result = userInput.age.add(5); // Might fail if age is string

// ✅ SAFE: Type conversion first
const result = userInput.age.to_int().add(5);
```

### Null Safety
```javascript
// ❌ DANGEROUS: No null checking
const name = userData.profile.name.uppercase(); // Fails if profile is null

// ✅ SAFE: Use get with defaults
const name = userData.get("profile.name", "Anonymous").uppercase();
```

### Performance Issues
```javascript
// ❌ INEFFICIENT: Multiple database queries in loop
orders.map(order => {
  return order.set("customer", getCustomer(order.customer_id));
});

// ✅ EFFICIENT: Batch fetch and map
const customerMap = getAllCustomers().group_by("id");
orders.map(order => {
  return order.set("customer", customerMap.get(order.customer_id, {}));
});
```

## 🔧 **Filter Debugging**

### Debug Filter Chains
```javascript
// Add logging between filter operations
const debugResult = data
  .filter_empty() // Log: "After filter_empty: ${result.count()} items"
  .unique("id")   // Log: "After unique: ${result.count()} items"
  .sort("name")   // Log: "After sort: first item = ${result.first().name}"
  .slice(0, 10);  // Log: "Final result: ${result.count()} items"
```

### Validate Filter Inputs
```javascript
// Validate data before complex filter chains
const processData = (inputData) => {
  if (!inputData || !inputData.length) {
    return [];
  }
  
  return inputData
    .filter(item => item && item.id) // Ensure valid items
    .map(item => ({
      ...item,
      id: item.id.to_text(),
      status: item.status?.lowercase() || "unknown"
    }));
};
```

## 📚 **Filter Reference Quick Links**

- **[Array Filters](array-filters.md)** - Complete array manipulation reference
- **[Text Filters](text-filters.md)** - String processing and formatting
- **[Security Filters](security-filters.md)** - Encryption, hashing, and authentication
- **[Filter Examples](filter-examples.md)** - Practical use cases and patterns
- **[Mathematical Filters](math-filters.md)** - Numeric operations and calculations
- **[Timestamp Filters](timestamp-filters.md)** - Date and time manipulation

---

**Next Steps**: Dive into specific filter categories or explore [Advanced Filter Patterns](advanced-filter-patterns.md) for complex data processing scenarios.