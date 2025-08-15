---
title: "Lambda Functions"
description: "Execute custom JavaScript/TypeScript code within Xano function stacks with full access to NPM packages and filesystem operations"
category: function-stack
difficulty: advanced
tags:
  - lambda
  - javascript
  - typescript
  - npm
  - custom-code
  - serverless
related_docs:
  - custom-functions
  - external-api-request
  - background-tasks
  - async-functions
last_updated: '2025-01-23'
---

# Lambda Functions

## Quick Summary
Lambda functions let you execute JavaScript or TypeScript code directly within your Xano function stacks. Perfect for complex logic, custom algorithms, NPM package integration, and scenarios where visual programming reaches its limits.

## What You'll Learn
- How to write and use Lambda functions in Xano
- Working with special variables and context data
- Integrating NPM packages and Node.js libraries
- File system operations and data processing
- Best practices for Lambda function development

## When to Use Lambda Functions

### Perfect For:
- **Complex algorithms** that are hard to build visually
- **NPM package integration** for specialized functionality
- **Data transformations** requiring custom logic
- **File processing** and manipulation
- **Mathematical calculations** and statistical operations
- **String parsing** and advanced text manipulation

### Consider Visual Functions For:
- Simple CRUD operations
- Basic data validation
- Standard API calls
- Simple conditional logic

## Basic Lambda Function Structure

### Hello World Example
```javascript
// Simple Lambda function
return "Hello, " + $input.name + "!";
```

### Accessing Xano Data
```javascript
// Access different Xano data sources
const userName = $var.current_user_name;  // Xano variables
const userEmail = $input.email;           // Function inputs
const apiKey = $env.THIRD_PARTY_API_KEY;  // Environment variables
const userId = $auth.id;                  // Authenticated user

return {
  user: userName,
  email: userEmail,
  isAuthenticated: userId > 0
};
```

## Special Variables Reference

### Core Variables
- **`$var.variable_name`** - Access Xano variables
- **`$input.field_name`** - Access function stack inputs
- **`$env.ENV_NAME`** - Access environment variables
- **`$auth.id`** - Current user ID (0 if not authenticated)
- **`$auth.extras`** - Additional user data

### Context Variables
- **`$this`** - Current item in loops/transforms
- **`$index`** - Current index in arrays
- **`$parent`** - Parent context in nested operations
- **`$result`** - Previous function result

### Authentication Example
```javascript
// Check user permissions
if ($auth.id === 0) {
  return { error: "Authentication required" };
}

// Access user data
const user = {
  id: $auth.id,
  role: $auth.extras.role,
  permissions: $auth.extras.permissions || []
};

// Role-based logic
if (user.role === 'admin') {
  return processAdminRequest($input);
} else {
  return processUserRequest($input, user.id);
}
```

## Using NPM Packages

### Installing Packages
```javascript
// Import with version for stability
const { default: moment } = await import("npm:moment@2.29.4");
const { default: lodash } = await import("npm:lodash@4.17.21");
const { v4: uuidv4 } = await import("npm:uuid@9.0.0");

// Use the imported libraries
const formattedDate = moment().format('YYYY-MM-DD HH:mm:ss');
const uniqueData = lodash.uniqBy($input.items, 'id');
const newId = uuidv4();

return {
  timestamp: formattedDate,
  processed_items: uniqueData,
  session_id: newId
};
```

### Node.js Built-in Modules
```javascript
// Use Node.js built-ins with node: prefix
const { createHash } = await import("node:crypto");
const { readFile } = await import("node:fs/promises");

// Hash sensitive data
const hash = createHash('sha256')
  .update($input.password + $env.SALT)
  .digest('hex');

return { passwordHash: hash };
```

## Real-World Examples

### 1. Data Processing Pipeline
```javascript
// Process CSV data from file upload
const { parse } = await import("npm:csv-parse@5.4.0");

// Parse uploaded CSV
const records = parse($input.csvContent, {
  columns: true,
  skip_empty_lines: true
});

// Transform and validate data
const processedData = records.map((record, index) => {
  // Validate required fields
  if (!record.email || !record.name) {
    throw new Error(`Invalid data at row ${index + 1}`);
  }
  
  return {
    name: record.name.trim(),
    email: record.email.toLowerCase(),
    phone: record.phone?.replace(/\D/g, '') || null,
    created_at: new Date().toISOString()
  };
});

return {
  total_records: processedData.length,
  processed_data: processedData
};
```

### 2. Advanced String Processing
```javascript
// Natural language processing example
const { default: natural } = await import("npm:natural@6.5.0");

const text = $input.user_message;

// Sentiment analysis
const sentiment = natural.SentimentAnalyzer.getSentiment(
  natural.WordTokenizer.tokenize(text)
    .map(token => natural.PorterStemmer.stem(token))
);

// Extract keywords
const keywords = natural.WordTokenizer.tokenize(text)
  .filter(word => word.length > 3)
  .map(word => natural.PorterStemmer.stem(word))
  .slice(0, 5);

return {
  original_text: text,
  sentiment_score: sentiment,
  keywords: keywords,
  word_count: text.split(/\s+/).length
};
```

### 3. Mathematical Calculations
```javascript
// Complex statistical analysis
const { default: ss } = await import("npm:simple-statistics@7.8.2");

const data = $input.sales_data; // Array of numbers

// Calculate comprehensive statistics
const stats = {
  mean: ss.mean(data),
  median: ss.median(data),
  standardDeviation: ss.standardDeviation(data),
  percentile75: ss.quantile(data, 0.75),
  percentile25: ss.quantile(data, 0.25),
  correlation: data.length > 1 ? ss.pearsonCorrelationCoefficient(
    data, 
    data.map((_, i) => i)
  ) : 0
};

// Identify outliers
const q1 = stats.percentile25;
const q3 = stats.percentile75;
const iqr = q3 - q1;
const outliers = data.filter(value => 
  value < q1 - 1.5 * iqr || value > q3 + 1.5 * iqr
);

return {
  statistics: stats,
  outliers: outliers,
  data_quality: {
    total_points: data.length,
    outlier_count: outliers.length,
    outlier_percentage: (outliers.length / data.length) * 100
  }
};
```

## File System Operations

### Reading and Writing Files
```javascript
// Process uploaded file
const uploadedFile = $input.file_path;

// Read file content
const content = await Deno.readTextFile(uploadedFile);

// Process the content
const lines = content.split('\n');
const processedLines = lines
  .filter(line => line.trim().length > 0)
  .map(line => line.toUpperCase());

// Write processed content to temporary file
const tempFile = await Deno.makeTempFile({ suffix: '.txt' });
await Deno.writeTextFile(tempFile, processedLines.join('\n'));

return {
  original_lines: lines.length,
  processed_lines: processedLines.length,
  temp_file_path: tempFile
};
```

### Directory Operations
```javascript
// Work with directories
const tempDir = await Deno.makeTempDir();

// Create subdirectories
await Deno.mkdir(`${tempDir}/processed`, { recursive: true });
await Deno.mkdir(`${tempDir}/failed`, { recursive: true });

// Process files
const files = $input.file_list;
const results = [];

for (const file of files) {
  try {
    const content = await Deno.readTextFile(file.path);
    // Process file...
    await Deno.writeTextFile(
      `${tempDir}/processed/${file.name}`, 
      content
    );
    results.push({ file: file.name, status: 'success' });
  } catch (error) {
    results.push({ file: file.name, status: 'failed', error: error.message });
  }
}

return {
  temp_directory: tempDir,
  processing_results: results
};
```

## Integration with n8n

### Data Transformation for n8n
```javascript
// Transform Xano data for n8n consumption
const { default: camelCase } = await import("npm:camelcase@7.0.1");

const xanoData = $input.database_result;

// Convert snake_case to camelCase for JavaScript frontend
const transformedData = xanoData.map(item => {
  const transformed = {};
  
  Object.keys(item).forEach(key => {
    const camelKey = camelCase(key);
    transformed[camelKey] = item[key];
  });
  
  return transformed;
});

return {
  n8n_format: transformedData,
  record_count: transformedData.length,
  transformation_timestamp: new Date().toISOString()
};
```

### Webhook Data Processing
```javascript
// Process complex webhook data from n8n
const incomingData = $input.webhook_payload;

// Parse and validate structure
if (!incomingData.events || !Array.isArray(incomingData.events)) {
  return { error: "Invalid webhook format" };
}

// Process each event
const processedEvents = incomingData.events.map(event => {
  return {
    id: event.id,
    type: event.type,
    timestamp: new Date(event.timestamp).toISOString(),
    data: JSON.stringify(event.data),
    source: 'n8n_webhook'
  };
});

return {
  processed_events: processedEvents,
  total_events: processedEvents.length,
  processing_complete: true
};
```

## Error Handling and Debugging

### Comprehensive Error Handling
```javascript
try {
  // Validate inputs
  if (!$input.data || !Array.isArray($input.data)) {
    throw new Error("Input data must be an array");
  }
  
  // Process data with detailed error tracking
  const results = [];
  const errors = [];
  
  for (const [index, item] of $input.data.entries()) {
    try {
      // Process individual item
      const processed = await processItem(item);
      results.push(processed);
    } catch (itemError) {
      errors.push({
        index: index,
        item: item,
        error: itemError.message
      });
    }
  }
  
  return {
    success: true,
    results: results,
    errors: errors,
    summary: {
      total: $input.data.length,
      successful: results.length,
      failed: errors.length
    }
  };
  
} catch (error) {
  // Log error details
  console.error("Lambda function error:", error);
  
  return {
    success: false,
    error: error.message,
    timestamp: new Date().toISOString(),
    input_received: typeof $input
  };
}

async function processItem(item) {
  // Your processing logic here
  return { ...item, processed: true };
}
```

## Try This: Build a Data Validator

1. **Create a Lambda function that validates complex data:**
   ```javascript
   const { default: Joi } = await import("npm:joi@17.9.2");
   
   // Define validation schema
   const schema = Joi.object({
     email: Joi.string().email().required(),
     age: Joi.number().integer().min(0).max(120),
     interests: Joi.array().items(Joi.string()).min(1)
   });
   
   // Validate input data
   const { error, value } = schema.validate($input.user_data);
   
   if (error) {
     return { valid: false, errors: error.details };
   }
   
   return { valid: true, data: value };
   ```

2. **Test with various data formats**
3. **Add custom validation rules**
4. **Integrate with your Xano database operations**

## Common Mistakes to Avoid

❌ **Not handling async operations properly** - Always use await for async functions
❌ **Forgetting error handling** - Lambda functions can break your entire stack
❌ **Not specifying NPM versions** - Use specific versions for stability
❌ **Blocking operations** - Avoid synchronous operations that could timeout
❌ **Not validating inputs** - Always validate data coming into Lambda functions

## Pro Tips

💡 **Use AI Assistant** to help generate complex Lambda code
💡 **Version your NPM imports** to prevent unexpected breaking changes
💡 **Implement comprehensive logging** for debugging production issues
💡 **Cache expensive operations** using Xano variables when possible
💡 **Keep functions focused** - One Lambda should do one thing well
💡 **Use TypeScript syntax** for better code documentation and IDE support
💡 **Test with various data shapes** before deploying to production

## Performance Best Practices

### Optimize Imports
```javascript
// Import only what you need
const { pick, omit } = await import("npm:lodash@4.17.21");

// Rather than importing the entire library
// const _ = await import("npm:lodash@4.17.21");
```

### Memory Management
```javascript
// Process large datasets in chunks
const chunkSize = 100;
const data = $input.large_dataset;
const results = [];

for (let i = 0; i < data.length; i += chunkSize) {
  const chunk = data.slice(i, i + chunkSize);
  const processed = chunk.map(processItem);
  results.push(...processed);
  
  // Allow garbage collection between chunks
  if (i % 1000 === 0) {
    await new Promise(resolve => setTimeout(resolve, 1));
  }
}

return results;
```

Lambda functions provide unlimited flexibility for complex backend logic while maintaining the visual development benefits of Xano.