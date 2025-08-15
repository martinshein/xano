---
title: "Utility Functions - Essential Helper Tools"
description: "Master Xano's built-in utility functions for common operations like date formatting, string manipulation, validation, and data processing"
category: function-stack
tags:
  - Utility Functions
  - Helper Functions
  - String Operations
  - Date/Time Functions
  - Validation
  - Data Processing
  - Built-in Functions
difficulty: beginner
reading_time: 10 minutes
last_updated: '2025-01-15'
prerequisites:
  - Basic understanding of function stacks
  - Familiarity with data types
---

# Utility Functions - Essential Helper Tools

## 📋 **Quick Summary**

**What it does:** Utility functions provide essential helper tools for common operations like string manipulation, date formatting, validation, and data processing within your function stacks.

**Why it matters:** This enables you to:
- Perform common operations without custom code
- Format data consistently across your application
- Validate inputs and sanitize data efficiently
- Save development time with pre-built functions

**Time to implement:** 2-5 minutes for basic operations, essential for daily development

---

## What You'll Learn

- String manipulation and formatting functions
- Date and time operations
- Data validation utilities
- Number and math functions
- Common utility patterns for no-code platforms

## String Utility Functions

### String Manipulation
```javascript
// Common string operations available in Xano
trim()          // Remove whitespace from start/end
toLowerCase()   // Convert to lowercase
toUpperCase()   // Convert to uppercase
length()        // Get string length
substring()     // Extract part of string
replace()       // Replace text patterns
split()         // Split string into array
```

### String Validation
```javascript
// Validation utilities
isEmpty()       // Check if string is empty
isEmail()       // Validate email format
isUrl()         // Validate URL format
isAlphanumeric() // Check for letters and numbers only
contains()      // Check if string contains substring
```

### String Formatting Examples
```javascript
// Format user display name
const displayName = `${firstName.trim()} ${lastName.trim()}`;

// Clean and validate email
const cleanEmail = email.toLowerCase().trim();
const isValidEmail = isEmail(cleanEmail);

// Format phone number
const cleanPhone = phone.replace(/[^\d]/g, ''); // Remove non-digits
```

## Date and Time Utilities

### Date Formatting
```javascript
// Common date operations
formatDate()     // Format date for display
addDays()        // Add/subtract days
addHours()       // Add/subtract hours
getTimestamp()   // Get Unix timestamp
parseDate()      // Parse date string
```

### Date Calculation Examples
```javascript
// Calculate age from birthdate
const birthDate = parseDate(userBirthdate);
const age = Math.floor((Date.now() - birthDate) / (365.25 * 24 * 60 * 60 * 1000));

// Set expiration date (30 days from now)
const expirationDate = addDays(Date.now(), 30);

// Format for display
const displayDate = formatDate(created_at, 'MMM DD, YYYY');
```

### Timezone Handling
```javascript
// Convert to user's timezone
const userTimezone = 'America/New_York';
const localTime = convertTimezone(utcTime, userTimezone);

// Get current time in specific timezone
const currentPacificTime = getCurrentTime('America/Los_Angeles');
```

## Number and Math Utilities

### Number Formatting
```javascript
// Format currency
const price = formatCurrency(29.99, 'USD'); // "$29.99"

// Format percentage
const discount = formatPercentage(0.15); // "15%"

// Round to decimal places
const rounded = roundTo(3.14159, 2); // 3.14
```

### Math Operations
```javascript
// Common calculations
sum()           // Add numbers
average()       // Calculate average
min()           // Find minimum value
max()           // Find maximum value
round()         // Round to nearest integer
random()        // Generate random number
```

### Practical Math Examples
```javascript
// Calculate order total with tax
const subtotal = sum(itemPrices);
const taxAmount = subtotal * 0.08;
const total = roundTo(subtotal + taxAmount, 2);

// Calculate discount
const discountPercent = 0.20;
const discountAmount = subtotal * discountPercent;
const finalPrice = subtotal - discountAmount;
```

## Data Validation Utilities

### Input Validation Functions
```javascript
// Common validation checks
isRequired()     // Check if value exists
isMinLength()    // Minimum string length
isMaxLength()    // Maximum string length
isNumeric()      // Check if numeric
isInteger()      // Check if integer
isInRange()      // Check if number in range
```

### Validation Patterns
```javascript
// User registration validation
const validationErrors = [];

if (!isRequired(email)) {
  validationErrors.push('Email is required');
} else if (!isEmail(email)) {
  validationErrors.push('Invalid email format');
}

if (!isRequired(password)) {
  validationErrors.push('Password is required');
} else if (!isMinLength(password, 8)) {
  validationErrors.push('Password must be at least 8 characters');
}

if (!isRequired(age)) {
  validationErrors.push('Age is required');
} else if (!isInRange(age, 13, 120)) {
  validationErrors.push('Age must be between 13 and 120');
}
```

### Data Sanitization
```javascript
// Clean user input
const sanitizedData = {
  name: trim(stripHtml(userName)),
  email: toLowerCase(trim(userEmail)),
  phone: cleanPhoneNumber(userPhone),
  bio: trim(userBio).substring(0, 500) // Limit bio length
};
```

## No-Code Platform Integration

### 🌐 **WeWeb Utility Integration**

Use Xano utilities to format data for WeWeb:

```javascript
// WeWeb collection formatter
async function formatUserDataForWeWeb(users) {
  return users.map(user => ({
    ...user,
    // Format display values
    display_name: `${user.first_name} ${user.last_name}`.trim(),
    formatted_join_date: formatDate(user.created_at, 'MMM DD, YYYY'),
    avatar_initials: getInitials(user.first_name, user.last_name),
    
    // WeWeb-specific formatting
    is_online: user.last_seen > addMinutes(Date.now(), -15),
    member_since: formatRelativeTime(user.created_at),
    clean_email: user.email.toLowerCase().trim()
  }));
}
```

### 🔗 **n8n Data Processing**

Process data with utilities in n8n workflows:

```yaml
n8n Workflow: Contact List Cleanup
1. HTTP Request → Get contacts from Xano
2. Function Node → Clean and validate data
   ```javascript
   const cleanedContacts = items.map(contact => ({
     name: contact.name.trim(),
     email: contact.email.toLowerCase().trim(),
     phone: cleanPhoneNumber(contact.phone),
     is_valid_email: isEmail(contact.email),
     formatted_date: formatDate(contact.created_at, 'YYYY-MM-DD')
   }));
   ```
3. Filter → Only valid contacts
4. HTTP Request → Update cleaned data in Xano
```

### 🔧 **Make Data Transformation**

Use utilities in Make scenarios:

```yaml
Make Scenario: Order Processing
1. Webhook → New order data
2. Text Parser → Extract and clean fields
   - Clean customer name (trim, title case)
   - Validate email format
   - Format phone number
3. Math → Calculate totals and discounts
4. Date/Time → Set delivery dates
5. HTTP Request → Send to fulfillment
```

## Common Utility Patterns

### Pattern 1: User Profile Formatter
```javascript
function formatUserProfile(userData) {
  return {
    // Clean and format strings
    display_name: titleCase(trim(userData.name)),
    bio: trim(userData.bio).substring(0, 160),
    
    // Format contact info
    email: toLowerCase(trim(userData.email)),
    phone: formatPhoneNumber(userData.phone),
    
    // Calculate derived fields
    age: calculateAge(userData.birthdate),
    member_duration: formatDuration(userData.join_date, Date.now()),
    
    // Format dates
    join_date_display: formatDate(userData.join_date, 'MMMM YYYY'),
    last_active: formatRelativeTime(userData.last_seen)
  };
}
```

### Pattern 2: Order Data Processor
```javascript
function processOrderData(orderData) {
  return {
    // Format monetary values
    subtotal: formatCurrency(orderData.subtotal),
    tax_amount: formatCurrency(orderData.tax),
    total: formatCurrency(orderData.total),
    
    // Format dates
    order_date: formatDate(orderData.created_at, 'MMM DD, YYYY'),
    estimated_delivery: formatDate(
      addDays(orderData.created_at, orderData.shipping_days), 
      'MMM DD'
    ),
    
    // Process items
    item_count: orderData.items.length,
    total_quantity: sum(orderData.items.map(item => item.quantity)),
    
    // Generate tracking info
    tracking_code: generateTrackingCode(orderData.id),
    status_display: titleCase(orderData.status.replace('_', ' '))
  };
}
```

### Pattern 3: Content Formatter
```javascript
function formatContentForDisplay(content) {
  return {
    // Text processing
    title: titleCase(trim(content.title)),
    excerpt: truncateText(stripHtml(content.body), 150),
    reading_time: calculateReadingTime(content.body),
    
    // Format metadata
    author_name: formatAuthorName(content.author),
    publish_date: formatDate(content.published_at, 'MMMM DD, YYYY'),
    category_display: titleCase(content.category),
    
    // Generate SEO fields
    slug: generateSlug(content.title),
    meta_description: truncateText(stripHtml(content.body), 160)
  };
}
```

## Performance Tips

### Efficient Utility Usage
```javascript
// ✅ Good: Process once, use multiple times
const cleanEmail = email.toLowerCase().trim();
const isValidEmail = isEmail(cleanEmail);
const emailDomain = extractDomain(cleanEmail);

// ❌ Avoid: Multiple processing of same data
if (isEmail(email.toLowerCase().trim())) {
  const domain = extractDomain(email.toLowerCase().trim());
}
```

### Batch Processing
```javascript
// Process arrays efficiently
const formattedUsers = users.map(user => ({
  ...user,
  display_name: formatDisplayName(user.first_name, user.last_name),
  clean_email: user.email.toLowerCase().trim()
}));
```

## 💡 **Try This: Build a Data Cleaner**

Create a comprehensive data cleaning utility:

### Step 1: Define Cleaning Rules
```javascript
const cleaningRules = {
  name: (value) => titleCase(trim(value)),
  email: (value) => toLowerCase(trim(value)),
  phone: (value) => cleanPhoneNumber(value),
  date: (value) => parseDate(value),
  currency: (value) => parseFloat(value).toFixed(2)
};
```

### Step 2: Apply Cleaning
```javascript
function cleanData(data, rules) {
  const cleaned = {};
  
  for (const [field, rule] of Object.entries(rules)) {
    if (data[field] !== undefined) {
      cleaned[field] = rule(data[field]);
    }
  }
  
  return cleaned;
}
```

### Step 3: Validate Results
```javascript
function validateCleanedData(data) {
  const errors = [];
  
  if (!isEmail(data.email)) {
    errors.push('Invalid email format');
  }
  
  if (!isValidPhoneNumber(data.phone)) {
    errors.push('Invalid phone number');
  }
  
  return {
    isValid: errors.length === 0,
    errors: errors,
    data: data
  };
}
```

## Common Mistakes to Avoid

❌ **Not validating inputs before processing**
- Always validate data before applying utilities
- Handle null/undefined values gracefully

❌ **Overusing string concatenation**
- Use template literals for complex string building
- Consider performance with large datasets

❌ **Ignoring timezone considerations**
- Always specify timezone for date operations
- Consider user's local timezone for display

❌ **Not sanitizing user input**
- Clean input data before processing
- Validate and escape data appropriately

## Pro Tips

💡 **Chaining Operations**
Chain utility functions for complex processing:
```javascript
const result = trim(toLowerCase(removeSpecialChars(userInput)));
```

💡 **Default Values**
Provide defaults for utility operations:
```javascript
const displayName = trim(userName) || 'Anonymous User';
```

💡 **Validation Before Processing**
Always validate before applying utilities:
```javascript
if (isRequired(email) && isEmail(email)) {
  const cleanEmail = toLowerCase(trim(email));
}
```

💡 **Performance Monitoring**
Monitor utility function performance with large datasets and optimize as needed.

---

**Next Steps:** Ready to organize complex logic? Learn about [Custom Functions](function__custom_functions.md) for building reusable utilities or explore [Data Types](../data-types.md) for working with different data formats.