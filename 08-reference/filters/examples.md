---
title: Filter Examples and Practical Use Cases - Complete Guide for No-Code Development
description: Master practical filter applications with real-world examples, use cases, and implementation patterns for data manipulation, object transformation, and conditional operations in n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - filter-reference.md
  - array-filters.md
  - text-filters.md
  - object-manipulation.md
tags:
  - filter-examples
  - practical-use-cases
  - data-manipulation
  - object-transformation
  - conditional-operations
  - best-practices
---

## 📋 **Quick Summary**

Master practical filter applications through comprehensive examples and real-world use cases. This guide demonstrates data manipulation, object transformation, conditional operations, and advanced filtering patterns essential for building robust applications with n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Practical filter examples for common scenarios
- Object manipulation and transformation patterns
- Array creation and population techniques
- Conditional data operations
- Path-based data access and modification
- Error handling and default value strategies
- Performance optimization tips

# Filter Examples and Practical Use Cases

## 🔧 **Data Manipulation Filters**

### fill

**Purpose**: Creates an array of a specified size filled with a default value.

**Parameters:**
- `parent_value`: The default value to fill each array element
- `start`: Starting index (usually 0)
- `length`: Number of items to create

**Examples:**

**Basic Array Creation:**
```javascript
// Input
parent_value: "Default Value"
start: 0
length: 10

// Output
[
  "Default Value",
  "Default Value", 
  "Default Value",
  "Default Value",
  "Default Value",
  "Default Value",
  "Default Value",
  "Default Value",
  "Default Value",
  "Default Value"
]
```

**🔗 Real-World Use Cases:**

**Form Field Initialization:**
```javascript
// n8n: Initialize form with default values
const defaultFormData = "".fill(0, 5); // Create 5 empty fields
const formFields = [
  "firstName", "lastName", "email", "phone", "company"
];

const initialForm = formFields.map((field, index) => ({
  [field]: defaultFormData[index] || ""
}));
```

**Placeholder Data Generation:**
```javascript
// WeWeb: Create placeholder content for loading states
const placeholderText = "Loading...".fill(0, 8);
const skeletonItems = placeholderText.map((text, index) => ({
  id: index,
  title: text,
  content: `${text} content ${index + 1}`
}));
```

**Batch Processing Setup:**
```javascript
// Make.com: Initialize batch processing queues
const batchSize = 100;
const emptyBatch = null.fill(0, batchSize);
const processingQueue = emptyBatch.map((_, index) => ({
  batch_id: index,
  status: "pending",
  items: []
}));
```

### fill_keys

**Purpose**: Creates an object with specified keys, all set to the same default value.

**Parameters:**
- `parent_value`: The default value for all keys
- `keys`: Array of key names to create

**Examples:**

**Object Template Creation:**
```javascript
// Input
parent_value: "default value"
keys: ["key1", "key2", "key3"]

// Output
{
  "key1": "default value",
  "key2": "default value", 
  "key3": "default value"
}
```

**🔗 Practical Applications:**

**API Response Template:**
```javascript
// n8n: Create consistent API response structure
const responseKeys = [
  "status", "message", "data", "errors", "metadata"
];
const defaultValue = null;
const responseTemplate = defaultValue.fill_keys(responseKeys);

// Result:
{
  "status": null,
  "message": null,
  "data": null,
  "errors": null,
  "metadata": null
}
```

**User Preferences Initialization:**
```javascript
// WeWeb: Initialize user preferences with defaults
const preferenceKeys = [
  "theme", "language", "notifications", "privacy", "display"
];
const defaultPreferences = "default".fill_keys(preferenceKeys);

// Customize specific values
const userPreferences = {
  ...defaultPreferences,
  theme: "dark",
  language: "en",
  notifications: true
};
```

**Configuration Object Setup:**
```javascript
// Make.com: Create configuration template
const configKeys = [
  "database_url", "api_key", "timeout", "retries", "cache_ttl"
];
const configTemplate = "".fill_keys(configKeys);

// Later populate from environment
const config = {
  ...configTemplate,
  database_url: process.env.DATABASE_URL,
  api_key: process.env.API_KEY,
  timeout: 30000
};
```

## 🎯 **Conditional Operations**

### first_notempty

**Purpose**: Returns the first value that is not empty (not 0, null, "", or empty string).

**Use Case**: Perfect for providing fallback values when input might be missing or empty.

**Examples:**

**Basic Fallback:**
```javascript
// Input 1: Empty value scenario
parent_value: ""  // Empty string
value: "default"

// Output
"default"

// Input 2: Value provided scenario  
parent_value: "user input"
value: "default"

// Output
"user input"
```

**🔗 Fallback Patterns:**

**User Profile Updates:**
```javascript
// n8n: Handle optional profile updates
const updatedUser = {
  name: userInput.name.first_notempty(existingUser.name),
  email: userInput.email.first_notempty(existingUser.email),
  bio: userInput.bio.first_notempty(existingUser.bio),
  avatar: userInput.avatar.first_notempty(existingUser.avatar)
};

// Only updates fields that have new values
```

**Configuration with Defaults:**
```javascript
// WeWeb: Application configuration with fallbacks
const appConfig = {
  api_endpoint: envConfig.api_endpoint.first_notempty("https://api.default.com"),
  timeout: envConfig.timeout.first_notempty(30000),
  theme: userPrefs.theme.first_notempty("light"),
  language: userPrefs.language.first_notempty("en")
};
```

**Dynamic Content Display:**
```javascript
// Make.com: Content with fallbacks
const displayContent = {
  title: post.title.first_notempty("Untitled Post"),
  excerpt: post.excerpt.first_notempty(post.content.substring(0, 150)),
  image: post.featured_image.first_notempty("/images/default-post.jpg"),
  author: post.author.first_notempty("Anonymous")
};
```

### first_notnull

**Purpose**: Returns the first value that is not `null` (specifically checks for null, not other empty values).

**Examples:**

**Null Handling:**
```javascript
// Input: null value
parent_value: null
value: "default"

// Output
"default"

// Input: empty string (not null)
parent_value: ""
value: "default"

// Output
""  // Empty string is returned because it's not null
```

**🔗 Null Safety Patterns:**

**Database Field Handling:**
```javascript
// n8n: Handle potentially null database fields
const safeUserData = {
  id: dbRecord.id.first_notnull(0),
  created_at: dbRecord.created_at.first_notnull(new Date().toISOString()),
  metadata: dbRecord.metadata.first_notnull({}),
  permissions: dbRecord.permissions.first_notnull([])
};
```

**API Response Safety:**
```javascript
// WeWeb: Safe API response handling
const processApiResponse = (response) => {
  return {
    data: response.data.first_notnull([]),
    pagination: response.pagination.first_notnull({
      page: 1,
      limit: 10,
      total: 0
    }),
    filters: response.filters.first_notnull({})
  };
};
```

## 🔍 **Data Access and Modification**

### get

**Purpose**: Safely retrieves values from objects/arrays with fallback defaults.

**Parameters:**
- `parent_value`: Object or array to search
- `path`: Path to the desired value
- `default_value`: Value to return if path doesn't exist

**Examples:**

**Object Property Access:**
```javascript
// Input
parent_value: {
  user: {
    name: "John",
    age: 30
  }
}
path: "user.name"
default_value: "Unknown"

// Output
"John"
```

**Array Index Access:**
```javascript
// Input
parent_value: ["apple", "banana", "cherry"]
path: "1"
default_value: "no fruit"

// Output
"banana"
```

**Missing Path Handling:**
```javascript
// Input
parent_value: {
  user: {
    name: "John"
  }
}
path: "user.email"
default_value: "no email provided"

// Output
"no email provided"
```

**🔗 Safe Data Access Patterns:**

**User Profile Display:**
```javascript
// WeWeb: Safe user profile rendering
const displayUser = {
  name: userData.get("profile.name", "Anonymous User"),
  avatar: userData.get("profile.avatar", "/images/default-avatar.png"),
  bio: userData.get("profile.bio", "No bio available"),
  location: userData.get("profile.location", "Location not specified"),
  joinDate: userData.get("created_at", "Unknown")
};
```

**API Response Processing:**
```javascript
// n8n: Process potentially incomplete API responses
const processWebhookData = (data) => {
  return {
    userId: data.get("user.id", null),
    userName: data.get("user.profile.name", "Unknown User"),
    eventType: data.get("event.type", "unknown"),
    timestamp: data.get("event.timestamp", new Date().toISOString()),
    metadata: data.get("metadata", {}),
    customFields: data.get("custom_data.fields", [])
  };
};
```

**Configuration Reading:**
```javascript
// Make.com: Safe configuration access
const getConfig = (configObject) => {
  return {
    database: {
      host: configObject.get("database.host", "localhost"),
      port: configObject.get("database.port", 5432),
      name: configObject.get("database.name", "app_db")
    },
    api: {
      baseUrl: configObject.get("api.base_url", "https://api.example.com"),
      timeout: configObject.get("api.timeout", 30000),
      retries: configObject.get("api.retries", 3)
    }
  };
};
```

### has

**Purpose**: Checks if a specific path exists in an object/array, returns boolean.

**Examples:**

**Path Existence Check:**
```javascript
// Input: Path exists
parent_value: {
  user: {
    name: "John",
    age: 30
  }
}
path: "user.age"

// Output
true

// Input: Path doesn't exist
parent_value: {
  user: {
    name: "John"
  }
}
path: "user.email"

// Output
false
```

**🔗 Conditional Logic Patterns:**

**Feature Flag Checking:**
```javascript
// n8n: Dynamic feature enabling
const enableFeature = (userConfig, featureName) => {
  const hasFeature = userConfig.has(`features.${featureName}`);
  const isEnabled = hasFeature ? userConfig.get(`features.${featureName}`, false) : false;
  
  return {
    available: hasFeature,
    enabled: isEnabled,
    canActivate: hasFeature && !isEnabled
  };
};
```

**Form Validation:**
```javascript
// WeWeb: Dynamic form validation
const validateForm = (formData) => {
  const validations = {
    hasName: formData.has("name"),
    hasEmail: formData.has("email"),
    hasValidEmail: formData.has("email") && formData.get("email", "").includes("@"),
    hasPassword: formData.has("password"),
    hasStrongPassword: formData.has("password") && formData.get("password", "").length >= 8
  };
  
  return {
    isValid: Object.values(validations).every(v => v),
    checks: validations
  };
};
```

### set

**Purpose**: Replaces or inserts data at a specified path in an object/array.

**Examples:**

**Object Property Setting:**
```javascript
// Input
parent_value: {
  user: {
    name: "John"
  }
}
path: "user.age"
value: 30

// Output
{
  user: {
    name: "John",
    age: 30
  }
}
```

**Nested Object Creation:**
```javascript
// Input
parent_value: {}
path: "user.profile.settings.theme"
value: "dark"

// Output
{
  user: {
    profile: {
      settings: {
        theme: "dark"
      }
    }
  }
}
```

**🔗 Data Construction Patterns:**

**API Response Building:**
```javascript
// n8n: Build API response dynamically
let response = {};
response = response.set("status", "success");
response = response.set("data.users", userArray);
response = response.set("data.pagination.page", currentPage);
response = response.set("data.pagination.total", totalRecords);
response = response.set("metadata.timestamp", new Date().toISOString());

// Result: Complete nested response object
```

**User Profile Assembly:**
```javascript
// WeWeb: Assemble user profile from multiple sources
let userProfile = {};
userProfile = userProfile.set("basic.name", dbUser.name);
userProfile = userProfile.set("basic.email", dbUser.email);
userProfile = userProfile.set("preferences.theme", userSettings.theme);
userProfile = userProfile.set("preferences.language", userSettings.language);
userProfile = userProfile.set("activity.lastLogin", authData.lastLogin);
userProfile = userProfile.set("activity.loginCount", authData.loginCount);
```

### set_conditional

**Purpose**: Conditionally sets a value based on whether a condition is true.

**Examples:**

**Conditional User Status:**
```javascript
// Input
parent_value: {
  user: {
    name: "John",
    age: 25
  }
}
path: "user.status"
value: "adult"
conditional: true  // age > 18

// Output
{
  user: {
    name: "John",
    age: 25,
    status: "adult"
  }
}
```

**🔗 Conditional Logic Patterns:**

**Dynamic Permissions:**
```javascript
// n8n: Set permissions based on user role
let userObject = baseUserData;

userObject = userObject.set_conditional(
  "permissions.admin",
  true,
  userRole.equals("administrator")
);

userObject = userObject.set_conditional(
  "permissions.moderator", 
  true,
  userRole.equals("moderator") || userRole.equals("administrator")
);

userObject = userObject.set_conditional(
  "features.beta",
  true,
  userSubscription.equals("premium")
);
```

**Pricing Logic:**
```javascript
// Make.com: Dynamic pricing based on conditions
let orderData = baseOrder;

orderData = orderData.set_conditional(
  "discount.student",
  0.1,
  customer.type.equals("student")
);

orderData = orderData.set_conditional(
  "discount.bulk",
  0.15,
  order.quantity > 100
);

orderData = orderData.set_conditional(
  "shipping.express",
  true,
  customer.membership.equals("premium")
);
```

### set_ifnotempty / set_ifnotnull

**Purpose**: Sets a value only if the provided value is not empty (or not null).

**Examples:**

**Profile Update Pattern:**
```javascript
// Input: Update user profile with only provided fields
parent_value: {
  id: 123,
  name: "John Doe",
  email: "john@example.com"
}

// User provides new bio but not phone
userInput = {
  bio: "Software developer",
  phone: ""  // Empty
}

// Using set_ifnotempty
result = parent_value
  .set_ifnotempty("bio", userInput.bio)      // Sets bio
  .set_ifnotempty("phone", userInput.phone); // Doesn't set phone

// Output
{
  id: 123,
  name: "John Doe", 
  email: "john@example.com",
  bio: "Software developer"
  // phone not added because it was empty
}
```

**🔗 Partial Update Patterns:**

**Database Record Updates:**
```javascript
// n8n: Update database record with only provided fields
const updateUserRecord = (existingUser, updateData) => {
  let updatedUser = existingUser;
  
  updatedUser = updatedUser.set_ifnotempty("name", updateData.name);
  updatedUser = updatedUser.set_ifnotempty("email", updateData.email);
  updatedUser = updatedUser.set_ifnotempty("bio", updateData.bio);
  updatedUser = updatedUser.set_ifnotempty("location", updateData.location);
  updatedUser = updatedUser.set_ifnotempty("website", updateData.website);
  
  // Only modified timestamp if any field was actually updated
  if (!updatedUser.equals(existingUser)) {
    updatedUser = updatedUser.set("updated_at", new Date().toISOString());
  }
  
  return updatedUser;
};
```

**Form Processing:**
```javascript
// WeWeb: Process form submission with partial data
const processFormData = (existingData, formSubmission) => {
  let processedData = existingData;
  
  // Only update fields that have values
  Object.keys(formSubmission).forEach(field => {
    processedData = processedData.set_ifnotempty(field, formSubmission[field]);
  });
  
  return processedData;
};
```

## 🔄 **Data Transformation**

### transform

**Purpose**: Universal data transformation using expressions. Works with arrays, objects, and scalar values.

**Special Variable**: `$$` refers to the parent value being transformed.

**Examples:**

**Array Transformation:**
```javascript
// Input
parent_value: [1, 2, 3]
expression: $$|count

// Output
3

// Complex transformation
parent_value: [1, 2, 3]
expression: ($$|count) + ($$|sum)

// Output
9  // 3 (count) + 6 (sum)
```

**Object Transformation:**
```javascript
// Input
parent_value: {
  first: "Alpha",
  last: "Beta"
}
expression: $$.first ~ " " ~ $$.last

// Output
"Alpha Beta"
```

**🔗 Advanced Transformation Patterns:**

**Data Aggregation:**
```javascript
// n8n: Complex data transformations
const salesData = [
  {amount: 100, region: "north"},
  {amount: 200, region: "south"},
  {amount: 150, region: "north"}
];

// Total sales
const totalSales = salesData.transform("$$|sum:amount");

// Regional breakdown
const regionalSales = salesData.transform(`
  $$|group_by:region|map:(
    {
      region: $$.key,
      total: $$.items|sum:amount,
      count: $$.items|count
    }
  )
`);
```

**User Data Processing:**
```javascript
// WeWeb: Transform user data for display
const userData = {
  first_name: "John",
  last_name: "Doe",
  birth_date: "1990-05-15",
  preferences: {
    theme: "dark",
    language: "en"
  }
};

const displayData = userData.transform(`
  {
    fullName: $$.first_name ~ " " ~ $$.last_name,
    age: ($$.birth_date|to_timestamp|age_in_years),
    displayPrefs: $$.preferences.theme ~ " theme, " ~ $$.preferences.language
  }
`);
```

### unset

**Purpose**: Removes a key from an object.

**Examples:**

**Sensitive Data Removal:**
```javascript
// Input
parent_value: {
  id: 123,
  name: "John Doe",
  email: "john@example.com",
  password: "secret123",
  ssn: "123-45-6789"
}
path: "password"

// Output
{
  id: 123,
  name: "John Doe",
  email: "john@example.com",
  ssn: "123-45-6789"
}
```

**🔗 Data Cleaning Patterns:**

**API Response Sanitization:**
```javascript
// n8n: Remove sensitive fields before sending to client
const sanitizeUserData = (userData) => {
  let cleanData = userData;
  
  // Remove sensitive fields
  const sensitiveFields = [
    "password", "ssn", "credit_card", "bank_account", 
    "internal_notes", "admin_flags", "system_metadata"
  ];
  
  sensitiveFields.forEach(field => {
    cleanData = cleanData.unset(field);
  });
  
  return cleanData;
};
```

**Configuration Cleanup:**
```javascript
// Make.com: Remove environment-specific configs
const prepareConfigForExport = (config) => {
  let exportConfig = config;
  
  const envSpecificFields = [
    "database.password",
    "api_keys.private",
    "internal.debug_flags",
    "local.file_paths"
  ];
  
  envSpecificFields.forEach(field => {
    exportConfig = exportConfig.unset(field);
  });
  
  return exportConfig;
};
```

## 🎯 **Complete Real-World Examples**

### E-commerce Order Processing

```javascript
// n8n: Complete order processing workflow
const processOrder = (orderData, customerData, inventory) => {
  // Start with base order structure
  let processedOrder = {}.fill_keys([
    "id", "customer", "items", "totals", "shipping", "payment", "status"
  ]);
  
  // Set basic order information
  processedOrder = processedOrder.set("id", orderData.get("order_id", null));
  processedOrder = processedOrder.set("status", "processing");
  
  // Process customer information with fallbacks
  const customerInfo = {
    id: customerData.get("id", null),
    name: customerData.get("profile.name", "Guest Customer"),
    email: customerData.get("contact.email", "no-email@example.com"),
    shipping_address: customerData.get("addresses.shipping", {})
  };
  
  processedOrder = processedOrder.set("customer", customerInfo);
  
  // Calculate totals with discounts
  const hasStudentDiscount = customerData.has("discounts.student");
  const hasBulkDiscount = orderData.get("items", []).length > 5;
  
  processedOrder = processedOrder.set_conditional(
    "discounts.student",
    0.1,
    hasStudentDiscount
  );
  
  processedOrder = processedOrder.set_conditional(
    "discounts.bulk", 
    0.05,
    hasBulkDiscount
  );
  
  // Set shipping based on customer tier
  const isPremium = customerData.get("membership.tier", "basic").equals("premium");
  processedOrder = processedOrder.set_conditional(
    "shipping.free",
    true,
    isPremium
  );
  
  return processedOrder;
};
```

### User Profile Management

```javascript
// WeWeb: Comprehensive user profile management
const manageUserProfile = (existingProfile, updateData, permissions) => {
  // Start with existing profile
  let updatedProfile = existingProfile;
  
  // Update basic information only if provided
  updatedProfile = updatedProfile.set_ifnotempty("personal.first_name", updateData.firstName);
  updatedProfile = updatedProfile.set_ifnotempty("personal.last_name", updateData.lastName);
  updatedProfile = updatedProfile.set_ifnotempty("personal.bio", updateData.bio);
  
  // Handle avatar upload
  if (updateData.has("avatar")) {
    const avatarUrl = updateData.get("avatar", null);
    updatedProfile = updatedProfile.set_ifnotempty("personal.avatar", avatarUrl);
  }
  
  // Update preferences with validation
  const validThemes = ["light", "dark", "auto"];
  const newTheme = updateData.get("preferences.theme", "");
  if (validThemes.includes(newTheme)) {
    updatedProfile = updatedProfile.set("preferences.theme", newTheme);
  }
  
  // Set admin fields only if user has permission
  const canEditAdmin = permissions.has("admin.edit_users");
  updatedProfile = updatedProfile.set_conditional(
    "admin.verified",
    updateData.get("admin.verified", false),
    canEditAdmin
  );
  
  // Remove sensitive data for client response
  const clientProfile = updatedProfile
    .unset("internal.password_hash")
    .unset("internal.reset_tokens")
    .unset("admin.internal_notes");
  
  return {
    internal: updatedProfile,
    client: clientProfile
  };
};
```

### Dynamic Configuration System

```javascript
// Make.com: Dynamic configuration management
const buildConfiguration = (baseConfig, environmentOverrides, userSettings) => {
  // Start with filled template
  let config = {}.fill_keys([
    "database", "api", "ui", "features", "integrations"
  ]);
  
  // Set base configuration
  config = config.set("database.host", baseConfig.get("db.host", "localhost"));
  config = config.set("database.port", baseConfig.get("db.port", 5432));
  config = config.set("api.timeout", baseConfig.get("api.timeout", 30000));
  
  // Apply environment overrides
  const envKeys = environmentOverrides.get("override_keys", []);
  envKeys.forEach(key => {
    const envValue = environmentOverrides.get(key, null);
    config = config.set_ifnotempty(key, envValue);
  });
  
  // Apply user-specific settings
  const userTheme = userSettings.get("theme", "").first_notempty("system");
  const userLanguage = userSettings.get("language", "").first_notempty("en");
  
  config = config.set("ui.theme", userTheme);
  config = config.set("ui.language", userLanguage);
  
  // Enable features based on user plan
  const userPlan = userSettings.get("subscription.plan", "free");
  config = config.set_conditional("features.advanced_analytics", true, userPlan.equals("premium"));
  config = config.set_conditional("features.api_access", true, userPlan !== "free");
  
  // Transform final config for consumption
  const finalConfig = config.transform(`
    {
      database: {
        connectionString: "postgresql://" ~ $$.database.host ~ ":" ~ $$.database.port,
        timeout: $$.database.timeout
      },
      api: $$.api,
      client: {
        theme: $$.ui.theme,
        language: $$.ui.language,
        features: $$.features
      }
    }
  `);
  
  return finalConfig;
};
```

## 💡 **Best Practices and Performance Tips**

### Chaining Operations Efficiently

```javascript
// ✅ GOOD: Chain operations efficiently
const result = userData
  .set_ifnotempty("name", input.name)
  .set_ifnotempty("email", input.email)
  .set_conditional("verified", true, input.email.includes("@company.com"))
  .unset("internal_data");

// ❌ AVOID: Multiple separate operations
let result = userData;
result = result.set_ifnotempty("name", input.name);
result = result.set_ifnotempty("email", input.email);
result = result.set_conditional("verified", true, input.email.includes("@company.com"));
result = result.unset("internal_data");
```

### Error Handling Patterns

```javascript
// Safe data access with comprehensive fallbacks
const safeGetUserData = (userData) => {
  try {
    return {
      id: userData.get("id", null),
      profile: {
        name: userData.get("profile.name", "Anonymous").first_notempty("Anonymous"),
        email: userData.get("profile.email", "").first_notempty("no-email@example.com"),
        avatar: userData.get("profile.avatar", "").first_notempty("/images/default-avatar.png")
      },
      preferences: userData.get("preferences", {}).first_notempty({
        theme: "light",
        language: "en"
      }),
      metadata: {
        created: userData.get("created_at", new Date().toISOString()),
        updated: userData.get("updated_at", new Date().toISOString())
      }
    };
  } catch (error) {
    return {
      id: null,
      profile: { name: "Error", email: "error@example.com", avatar: "/images/error.png" },
      preferences: { theme: "light", language: "en" },
      metadata: { created: new Date().toISOString(), updated: new Date().toISOString() }
    };
  }
};
```

### Performance Optimization

```javascript
// Efficient data transformation
const optimizedTransform = (largeDataset) => {
  // Use transform for complex operations instead of multiple filters
  return largeDataset.transform(`
    $$|map:(
      {
        id: $$.id,
        name: $$.first_name ~ " " ~ $$.last_name,
        active: $$.status == "active",
        lastSeen: $$.last_login|to_timestamp|format_date
      }
    )|filter:($$.active == true)|sort:name
  `);
};
```

---

**Next Steps**: Apply these patterns in your applications and explore [Advanced Filter Techniques](advanced-filters.md) for more complex data manipulation scenarios.