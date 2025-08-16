---
title: Conversion and Encoding Filters Reference - Complete Guide for No-Code Development
description: Master Xano's conversion and encoding filters including base64, JSON, URL encoding, CSV, YAML, and data type conversions for powerful data processing in n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - text-filters.md
  - array-filters.md
  - security-filters.md
tags:
  - conversion-filters
  - encoding
  - base64
  - json
  - url-encoding
  - csv
  - yaml
  - data-types
---

## 📋 **Quick Summary**

Master Xano's comprehensive conversion and encoding filter library to transform data between different formats and types. This reference covers base64 encoding/decoding, JSON processing, URL encoding, CSV manipulation, data type conversions, and more for seamless integration with n8n, WeWeb, and Make.com platforms.

## What You'll Learn

- Complete conversion and encoding filter reference
- Base64, JSON, URL, CSV, and YAML processing
- Data type conversion techniques
- Number base conversions (binary, hex, octal)
- Security-focused encoding practices
- Integration patterns for external platforms

# Conversion and Encoding Filters Reference

## 🔐 **Base64 Encoding/Decoding**

### base64_encode

**Purpose**: Encodes a value and returns the result as base64 text.

**Examples:**
```javascript
// Input
parent_value: "Hello, World!"

// Output
"SGVsbG8sIFdvcmxkIQ=="

// Binary data encoding
parent_value: image_file_content

// Output
"/9j/4AAQSkZJRgABAQEAYABgAAD..." // Base64 image data
```

**🔗 Real-World Use Cases:**
```javascript
// n8n: Encode file for API transmission
const encodedFile = fileContent.base64_encode();

// WeWeb: Prepare image for data URL
const dataUrl = `data:image/png;base64,${imageData.base64_encode()}`;
```

### base64_decode

**Purpose**: Decodes a base64 encoded value and returns the original result.

**Examples:**
```javascript
// Input
parent_value: "SGVsbG8sIFdvcmxkIQ=="

// Output
"Hello, World!"

// Image data decoding
parent_value: "/9j/4AAQSkZJRgABAQEAYABgAAD..."

// Output
[Binary image data]
```

**💡 Security Note:**
```javascript
// Always validate decoded content
const decodedData = encodedInput.base64_decode();
// Validate before processing
if (!isValidImageData(decodedData)) {
  throw new Error("Invalid image data");
}
```

### base64_encode_urlsafe / base64_decode_urlsafe

**Purpose**: URL-safe base64 encoding/decoding (uses `-` and `_` instead of `+` and `/`).

**Examples:**
```javascript
// Standard base64 (may contain +, /, =)
standard: "SGVsbG8gV29ybGQ+Pz8/+"

// URL-safe base64 (uses -, _, no padding)
urlsafe: "SGVsbG8gV29ybGQ-Pz8_"
```

**🔗 Use Case - URL Parameters:**
```javascript
// Make.com: Safe data transmission in URLs
const urlSafeToken = tokenData.base64_encode_urlsafe();
const apiUrl = `https://api.example.com/data?token=${urlSafeToken}`;
```

## 📊 **JSON Processing**

### json_encode

**Purpose**: Encodes a value and returns it as JSON text.

**Examples:**
```javascript
// Object to JSON
parent_value: {
  "name": "John Doe",
  "age": 30,
  "skills": ["JavaScript", "API Design"]
}

// Output
'{"name":"John Doe","age":30,"skills":["JavaScript","API Design"]}'

// Array to JSON
parent_value: [1, 2, 3, "test", true]

// Output
'[1,2,3,"test",true]'
```

**🔗 Integration Examples:**
```javascript
// n8n: Prepare data for webhook
const jsonPayload = formData.json_encode();

// WeWeb: Store complex data in localStorage
localStorage.setItem('userPreferences', preferences.json_encode());
```

### json_decode

**Purpose**: Decodes JSON text and returns the original data structure.

**Examples:**
```javascript
// JSON string to object
parent_value: '{"name":"John","age":30}'

// Output
{
  "name": "John",
  "age": 30
}

// JSON array to array
parent_value: '[1,2,3,"test"]'

// Output
[1, 2, 3, "test"]
```

**💡 Error Handling:**
```javascript
// Safe JSON parsing
try {
  const data = jsonString.json_decode();
  return data;
} catch (error) {
  return {error: "Invalid JSON format"};
}
```

## 🌐 **URL Encoding/Decoding**

### url_encode

**Purpose**: Encodes a value for safe transmission in URLs.

**Examples:**
```javascript
// Basic URL encoding
parent_value: "Hello World & Special Characters!"

// Output
"Hello%20World%20%26%20Special%20Characters%21"

// Query parameter encoding
parent_value: "user@example.com"

// Output
"user%40example.com"
```

### url_decode

**Purpose**: Decodes URL-encoded values.

**Examples:**
```javascript
// Input
parent_value: "Hello%20World%20%26%20Special%20Characters%21"

// Output
"Hello World & Special Characters!"
```

### url_encode_rfc3986 / url_decode_rfc3986

**Purpose**: RFC3986-compliant URL encoding/decoding (stricter standard).

**Examples:**
```javascript
// RFC3986 encoding (encodes more characters)
parent_value: "hello(world)"

// Standard encoding
"hello(world)"  // Parentheses not encoded

// RFC3986 encoding
"hello%28world%29"  // Parentheses encoded
```

**🔗 API Integration Patterns:**
```javascript
// WeWeb: Safe search query transmission
const searchQuery = userInput.url_encode_rfc3986();
const apiUrl = `https://api.example.com/search?q=${searchQuery}`;

// n8n: Clean webhook URLs
const cleanParam = webhookData.url_decode();
```

## 📄 **CSV Processing**

### csv_encode

**Purpose**: Encodes data as CSV-formatted text.

**Examples:**
```javascript
// Array of arrays to CSV
parent_value: [
  ["Name", "Age", "City"],
  ["John Doe", "30", "New York"],
  ["Jane Smith", "25", "Los Angeles"]
]

// Output
"Name,Age,City\nJohn Doe,30,New York\nJane Smith,25,Los Angeles"

// Object array to CSV (automatic headers)
parent_value: [
  {"name": "John", "age": 30, "city": "New York"},
  {"name": "Jane", "age": 25, "city": "Los Angeles"}
]

// Output
"name,age,city\nJohn,30,New York\nJane,25,Los Angeles"
```

### csv_decode

**Purpose**: Decodes CSV text into array format.

**Examples:**
```javascript
// Input
parent_value: "Name,Age,City\nJohn Doe,30,New York\nJane Smith,25,Los Angeles"

// Output
[
  ["Name", "Age", "City"],
  ["John Doe", "30", "New York"],
  ["Jane Smith", "25", "Los Angeles"]
]
```

**🔗 Data Processing Patterns:**
```javascript
// Make.com: Process uploaded CSV files
const csvData = uploadedFile.csv_decode();
const processedData = csvData.slice(1).map(row => ({
  name: row[0],
  age: parseInt(row[1]),
  city: row[2]
}));

// n8n: Generate reports as CSV
const reportData = userRecords.map(user => [
  user.name,
  user.email,
  user.created_at
]);
const csvReport = reportData.csv_encode();
```

## 📝 **YAML Processing**

### yaml_encode

**Purpose**: Encodes data as YAML text.

**Examples:**
```javascript
// Object to YAML
parent_value: {
  "database": {
    "host": "localhost",
    "port": 5432,
    "credentials": {
      "username": "admin",
      "password": "secret"
    }
  },
  "features": ["auth", "api", "webhooks"]
}

// Output
`database:
  host: localhost
  port: 5432
  credentials:
    username: admin
    password: secret
features:
  - auth
  - api
  - webhooks`
```

### yaml_decode

**Purpose**: Decodes YAML text into data structure.

**Examples:**
```javascript
// Input
parent_value: `
name: John Doe
age: 30
skills:
  - JavaScript
  - Python
  - API Design
`

// Output
{
  "name": "John Doe",
  "age": 30,
  "skills": ["JavaScript", "Python", "API Design"]
}
```

**🔗 Configuration Management:**
```javascript
// WeWeb: Process configuration files
const config = yamlConfig.yaml_decode();
const apiEndpoint = config.api.endpoint;

// n8n: Generate dynamic configurations
const workflowConfig = {
  triggers: webhookUrls,
  actions: processingSteps
};
const yamlOutput = workflowConfig.yaml_encode();
```

## 🔢 **Number Base Conversions**

### Binary Conversions

**decbin**: Converts decimal to binary string
```javascript
// Input
parent_value: 10

// Output
"1010"
```

**bindec**: Converts binary string to decimal
```javascript
// Input
parent_value: "1010"

// Output
10
```

### Hexadecimal Conversions

**dechex**: Converts decimal to hexadecimal
```javascript
// Input
parent_value: 255

// Output
"ff"
```

**hexdec**: Converts hexadecimal to decimal
```javascript
// Input
parent_value: "ff"

// Output
255
```

**bin2hex**: Converts binary to hexadecimal
```javascript
// Input
parent_value: "01010101"

// Output
"55"
```

**hex2bin**: Converts hexadecimal to binary
```javascript
// Input
parent_value: "55"

// Output
"01010101"
```

### Octal Conversions

**decoct**: Converts decimal to octal
```javascript
// Input
parent_value: 64

// Output
"100"
```

**octdec**: Converts octal to decimal
```javascript
// Input
parent_value: "100"

// Output
64
```

### base_convert

**Purpose**: Converts a value between any two bases (2-36).

**Examples:**
```javascript
// Convert from base 10 to base 16
parent_value: 255
from_base: 10
to_base: 16

// Output
"ff"

// Convert from base 2 to base 10
parent_value: "1010"
from_base: 2
to_base: 10

// Output
"10"

// Convert to base 36 (uses 0-9, a-z)
parent_value: 123456
from_base: 10
to_base: 36

// Output
"2n9c"
```

**🔗 Use Cases:**
```javascript
// Generate short IDs
const shortId = timestamp.base_convert(10, 36);

// Color conversions
const hexColor = rgbValue.base_convert(10, 16);
```

## 🔄 **Data Type Conversions**

### to_text

**Purpose**: Converts any value to text/string.

**Examples:**
```javascript
// Number to text
parent_value: 123

// Output
"123"

// Boolean to text
parent_value: true

// Output
"true"

// Object to text (JSON representation)
parent_value: {"name": "John"}

// Output
'{"name":"John"}'
```

### to_int

**Purpose**: Converts value to integer.

**Examples:**
```javascript
// Text to integer
parent_value: "123"

// Output
123

// Decimal to integer (truncated)
parent_value: 123.456

// Output
123

// Boolean to integer
parent_value: true

// Output
1
```

### to_dec

**Purpose**: Converts value to decimal.

**Examples:**
```javascript
// Text to decimal
parent_value: "123.456"

// Output
123.456

// Integer to decimal
parent_value: 123

// Output
123.0
```

### to_bool

**Purpose**: Converts value to boolean.

**Examples:**
```javascript
// Text to boolean
parent_value: "true"

// Output
true

// Number to boolean
parent_value: 0

// Output
false

// Non-zero number
parent_value: 42

// Output
true

// Empty string
parent_value: ""

// Output
false
```

### to_timestamp

**Purpose**: Converts text expressions to timestamp format.

**Examples:**
```javascript
// Natural language
parent_value: "now"

// Output
"2025-01-16T10:30:00Z"

// Relative dates
parent_value: "next Friday"

// Output
"2025-01-24T00:00:00Z"

// Specific formats
parent_value: "2025-01-16 10:30:00"

// Output
"2025-01-16T10:30:00Z"
```

**🔗 Dynamic Date Processing:**
```javascript
// n8n: Schedule future tasks
const scheduleTime = "tomorrow at 9am".to_timestamp();

// WeWeb: Parse user-friendly dates
const eventDate = userInput.to_timestamp();
```

## 🔧 **Object Creation**

### create_object

**Purpose**: Creates an object from arrays of keys and values.

**Examples:**
```javascript
// Basic object creation
keys: ["name", "age", "city"]
values: ["John Doe", 30, "New York"]

// Output
{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}

// Dynamic object creation
keys: ["field1", "field2", "field3"]
values: [dynamicValue1, dynamicValue2, dynamicValue3]

// Output
{
  "field1": dynamicValue1,
  "field2": dynamicValue2,
  "field3": dynamicValue3
}
```

**🔗 Dynamic Form Processing:**
```javascript
// WeWeb: Convert form arrays to objects
const formKeys = ["username", "email", "preferences"];
const formValues = [inputUsername, inputEmail, userPreferences];
const userObject = create_object(formKeys, formValues);

// n8n: Build dynamic API payloads
const apiKeys = webhookData.requiredFields;
const apiValues = webhookData.fieldValues;
const apiPayload = create_object(apiKeys, apiValues);
```

## 🔗 **Integration Patterns**

### n8n Workflow Examples

**Data Format Conversion Pipeline:**
```javascript
// n8n Code node: Multi-format data processing
const inputData = $input.all()[0].json;

// Convert to different formats for different endpoints
const formats = {
  json: inputData.json_encode(),
  csv: inputData.csv_encode(),
  yaml: inputData.yaml_encode(),
  base64: inputData.json_encode().base64_encode()
};

return formats;
```

**Secure Data Transmission:**
```javascript
// Encode sensitive data for webhook transmission
const sensitiveData = {
  user_id: userId,
  api_key: apiKey,
  payload: requestData
};

const securePayload = sensitiveData.json_encode().base64_encode();
const webhookUrl = `https://endpoint.com/webhook?data=${securePayload}`;
```

### WeWeb Component Integration

**Dynamic Configuration Processing:**
```javascript
// WeWeb: Process configuration from various sources
const processConfig = (configString, format) => {
  switch(format) {
    case 'json':
      return configString.json_decode();
    case 'yaml':
      return configString.yaml_decode();
    case 'base64':
      return configString.base64_decode().json_decode();
    default:
      return configString;
  }
};
```

**File Upload Processing:**
```javascript
// WeWeb: Handle multiple file formats
const processUploadedFile = (fileContent, fileType) => {
  if (fileType === 'csv') {
    return fileContent.csv_decode();
  } else if (fileType === 'json') {
    return fileContent.json_decode();
  } else if (fileType === 'yaml') {
    return fileContent.yaml_decode();
  }
  return fileContent;
};
```

### Make.com Scenario Patterns

**Multi-Format Data Export:**
```javascript
// Make.com: Generate reports in multiple formats
const reportData = [
  {name: "John", sales: 1000},
  {name: "Jane", sales: 1500}
];

// Generate different format outputs
const formats = {
  json: reportData.json_encode(),
  csv: reportData.csv_encode(),
  yaml: reportData.yaml_encode()
};

// Send to different destinations based on format preference
```

**API Response Processing:**
```javascript
// Process different API response formats
const processAPIResponse = (response, contentType) => {
  if (contentType.includes('application/json')) {
    return response.json_decode();
  } else if (contentType.includes('text/csv')) {
    return response.csv_decode();
  } else if (contentType.includes('application/x-yaml')) {
    return response.yaml_decode();
  }
  return response;
};
```

## 💡 **Best Practices**

### Security Considerations

**Safe Decoding:**
```javascript
// Always validate decoded content
const validateBase64 = (encoded) => {
  try {
    const decoded = encoded.base64_decode();
    // Validate content before processing
    if (decoded.length > MAX_SIZE) {
      throw new Error("Content too large");
    }
    return decoded;
  } catch (error) {
    return null;
  }
};
```

**URL Safety:**
```javascript
// Use RFC3986 for maximum compatibility
const safeUrlParam = userInput.url_encode_rfc3986();
```

### Performance Optimization

**Efficient Format Conversion:**
```javascript
// Cache converted formats when possible
const formatCache = new Map();

const getFormat = (data, format) => {
  const cacheKey = `${data.hash()}_${format}`;
  
  if (formatCache.has(cacheKey)) {
    return formatCache.get(cacheKey);
  }
  
  let result;
  switch(format) {
    case 'json': result = data.json_encode(); break;
    case 'csv': result = data.csv_encode(); break;
    case 'yaml': result = data.yaml_encode(); break;
  }
  
  formatCache.set(cacheKey, result);
  return result;
};
```

### Error Handling

**Robust Conversion Pipeline:**
```javascript
// Handle conversion errors gracefully
const safeConvert = (data, conversions) => {
  let result = data;
  
  for (const conversion of conversions) {
    try {
      result = result[conversion]();
    } catch (error) {
      return {
        error: `Conversion failed at step: ${conversion}`,
        partial_result: result
      };
    }
  }
  
  return result;
};

// Usage
const converted = safeConvert(inputData, [
  'json_encode',
  'base64_encode',
  'url_encode'
]);
```

## 🎯 **Common Patterns**

### Data Format Bridge

```javascript
// Convert between different API formats
const formatBridge = (inputData, fromFormat, toFormat) => {
  // First decode from input format
  let decoded;
  switch(fromFormat) {
    case 'json': decoded = inputData.json_decode(); break;
    case 'csv': decoded = inputData.csv_decode(); break;
    case 'yaml': decoded = inputData.yaml_decode(); break;
    case 'base64': decoded = inputData.base64_decode(); break;
    default: decoded = inputData;
  }
  
  // Then encode to output format
  switch(toFormat) {
    case 'json': return decoded.json_encode();
    case 'csv': return decoded.csv_encode();
    case 'yaml': return decoded.yaml_encode();
    case 'base64': return decoded.json_encode().base64_encode();
    default: return decoded;
  }
};
```

### Type-Safe Conversions

```javascript
// Ensure proper type conversion with validation
const safeTypeConvert = (value, targetType) => {
  switch(targetType) {
    case 'int':
      const intVal = value.to_int();
      return isNaN(intVal) ? 0 : intVal;
      
    case 'bool':
      if (typeof value === 'string') {
        return ['true', '1', 'yes', 'on'].includes(value.toLowerCase());
      }
      return value.to_bool();
      
    case 'text':
      return value === null || value === undefined ? '' : value.to_text();
      
    default:
      return value;
  }
};
```

### Bulk Data Processing

```javascript
// Process large datasets with format conversion
const processBulkData = (dataArray, operations) => {
  return dataArray.map(item => {
    let processed = item;
    
    operations.forEach(op => {
      if (op.type === 'convert') {
        processed = processed[op.filter]();
      } else if (op.type === 'validate') {
        if (!op.validator(processed)) {
          throw new Error(`Validation failed: ${op.message}`);
        }
      }
    });
    
    return processed;
  });
};
```

---

**Next Steps**: Explore more filter types in [Text Filters](text-filters.md) and [Security Filters](security-filters.md) to complete your data processing toolkit.