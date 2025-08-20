---
category: functions
description: Understanding zero-dependency architecture in Xano Actions and how to build shareable, portable functions without external dependencies
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - actions.md
  - custom-functions.md
  - middleware.md
  - lambda-functions.md
subcategory: 08-reference/functions
tags:
  - actions
  - zero-dependency
  - architecture
  - integration
  - sharing
  - portability
title: What does zero dependency mean?
---

# What does zero dependency mean?

## 📋 **Quick Summary**
Zero-dependency architecture in Xano Actions enables portable, shareable functions that work across any workspace without external dependencies. Build reusable logic that anyone can install and use immediately.

## What You'll Learn
- Core principles of zero-dependency architecture
- What components are restricted in Actions
- How to build portable, shareable functions
- Best practices for Action development
- Integration patterns with existing systems
- Settings Registry for secure configuration

## Understanding Zero-Dependency Architecture

**Zero-dependency** means Xano Actions are completely self-contained and portable. They don't rely on external workspace resources, making them instantly shareable and usable across different environments.

### Key Benefits
```javascript
// Zero-dependency advantages
const zeroDependencyBenefits = {
  portability: "Works in any Xano workspace instantly",
  shareability: "Can be distributed to any user or team",
  isolation: "No conflicts with existing workspace setup",
  testing: "Can be tested without full Xano account",
  versioning: "Easy to fork and create variations",
  marketplace: "Can be published for community use"
};
```

### Architecture Comparison
```javascript
// Traditional Function Stack (has dependencies)
const traditionalFunction = {
  dependencies: [
    "Database tables",
    "Environment variables", 
    "Middleware",
    "Lambda functions",
    "Redis cache",
    "Specific workspace configuration"
  ],
  portability: "Limited to specific workspace",
  sharing: "Requires manual setup by recipient"
};

// Zero-Dependency Action (portable)
const zeroDepAction = {
  dependencies: [],
  selfContained: true,
  portability: "Works anywhere immediately",
  sharing: "One-click install and use"
};
```

## Restricted Components in Actions

### What's NOT Available
```javascript
// Components excluded from Actions
const restrictedComponents = {
  "database_operations": {
    "restriction": "No database requests or table dependencies",
    "reason": "Tables vary between workspaces",
    "alternative": "Use inputs/outputs to pass data"
  },
  "middleware": {
    "restriction": "No middleware functions",
    "reason": "Middleware is workspace-specific",
    "alternative": "Implement logic directly in Action"
  },
  "environment_variables": {
    "restriction": "No environment variable access",
    "reason": "Variables are workspace-specific", 
    "alternative": "Use Settings Registry for configuration"
  },
  "lambda_functions": {
    "restriction": "No Lambda function calls",
    "reason": "Lambda code is workspace-specific",
    "alternative": "Include logic directly in Action"
  },
  "redis_caching": {
    "restriction": "No Redis cache access",
    "reason": "Cache is instance-specific",
    "alternative": "Use memory variables for temporary storage"
  },
  "microservices": {
    "restriction": "No Docker microservice dependencies",
    "reason": "Services are infrastructure-specific",
    "alternative": "Use external API requests"
  }
};
```

### What IS Available
```javascript
// Components available in Actions
const availableComponents = {
  "data_manipulation": [
    "Variables", "Conditionals", "Loops", "Math operations",
    "Text processing", "Array manipulation", "Object handling"
  ],
  "external_apis": [
    "HTTP requests", "Webhooks", "Third-party integrations"
  ],
  "logic_processing": [
    "Business logic", "Data validation", "Transformations"
  ],
  "utility_functions": [
    "Date/time operations", "String manipulation", "Calculations"
  ]
};
```

## Building Zero-Dependency Actions

### Action Structure
```javascript
// Example: Currency converter Action
{
  "name": "Currency Converter",
  "description": "Convert amounts between currencies using live exchange rates",
  "inputs": {
    "amount": {
      "type": "decimal",
      "required": true,
      "description": "Amount to convert"
    },
    "from_currency": {
      "type": "text",
      "required": true,
      "description": "Source currency code (e.g., USD)"
    },
    "to_currency": {
      "type": "text", 
      "required": true,
      "description": "Target currency code (e.g., EUR)"
    },
    "api_key": {
      "type": "text",
      "required": true,
      "settings_registry": true,
      "description": "Exchange rate API key"
    }
  },
  "logic": [
    {
      "function": "Validate Inputs",
      "logic": `
        if (!amount || amount <= 0) {
          return error(400, "Amount must be greater than 0");
        }
        
        if (!from_currency || !to_currency) {
          return error(400, "Currency codes are required");
        }
        
        // Validate currency code format
        const currencyPattern = /^[A-Z]{3}$/;
        if (!currencyPattern.test(from_currency) || !currencyPattern.test(to_currency)) {
          return error(400, "Invalid currency code format");
        }
      `
    },
    {
      "function": "Get Exchange Rate",
      "external_api": {
        "url": "https://api.exchangerate-api.com/v4/latest/{from_currency}",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {api_key}"
        }
      }
    },
    {
      "function": "Calculate Conversion",
      "logic": `
        const rate = exchange_data.rates[to_currency];
        
        if (!rate) {
          return error(404, "Exchange rate not found for currency pair");
        }
        
        const converted_amount = amount * rate;
        
        return {
          original_amount: amount,
          from_currency: from_currency,
          to_currency: to_currency,
          exchange_rate: rate,
          converted_amount: Math.round(converted_amount * 100) / 100,
          timestamp: new Date().toISOString()
        };
      `
    }
  ]
}
```

### Settings Registry Implementation
```javascript
// Using Settings Registry for secure configuration
{
  "settings_registry": {
    "purpose": "Store sensitive configuration without hard-coding",
    "usage": "Similar to environment variables but Action-specific",
    "benefits": [
      "Secure API key storage",
      "User-configurable values", 
      "No hard-coded secrets",
      "Portable across workspaces"
    ]
  },
  
  "implementation": {
    "step1": "Mark input as Settings Registry",
    "step2": "Provide default for testing",
    "step3": "Users configure when installing",
    "step4": "Values are workspace-specific"
  }
}
```

## Practical Examples

### Data Processing Action
```javascript
// Example: JSON data transformer
{
  "name": "Advanced JSON Transformer",
  "purpose": "Transform JSON data with mapping rules",
  "inputs": {
    "source_data": {
      "type": "object",
      "description": "Source JSON data to transform"
    },
    "mapping_rules": {
      "type": "object", 
      "description": "Transformation mapping configuration"
    }
  },
  "logic": `
    function transformData(data, rules) {
      const result = {};
      
      for (const [targetPath, sourcePath] of Object.entries(rules)) {
        const value = getNestedValue(data, sourcePath);
        setNestedValue(result, targetPath, value);
      }
      
      return result;
    }
    
    function getNestedValue(obj, path) {
      return path.split('.').reduce((current, key) => current?.[key], obj);
    }
    
    function setNestedValue(obj, path, value) {
      const keys = path.split('.');
      const lastKey = keys.pop();
      const target = keys.reduce((current, key) => {
        current[key] = current[key] || {};
        return current[key];
      }, obj);
      target[lastKey] = value;
    }
    
    // Transform the data
    const transformed = transformData(source_data, mapping_rules);
    
    return {
      success: true,
      original_data: source_data,
      mapping_applied: mapping_rules,
      transformed_data: transformed,
      transformation_time: new Date().toISOString()
    };
  `
}
```

### API Integration Action
```javascript
// Example: Slack notification Action
{
  "name": "Smart Slack Notifier", 
  "purpose": "Send formatted notifications to Slack with rich content",
  "inputs": {
    "webhook_url": {
      "type": "text",
      "settings_registry": true,
      "description": "Slack webhook URL"
    },
    "message": {
      "type": "text",
      "required": true,
      "description": "Notification message"
    },
    "severity": {
      "type": "text",
      "default": "info",
      "description": "Message severity: info, warning, error, success"
    },
    "metadata": {
      "type": "object",
      "description": "Additional data to include"
    }
  },
  "logic": `
    // Format message based on severity
    const severityConfig = {
      info: { color: "#36a64f", icon: ":information_source:" },
      warning: { color: "#ff9500", icon: ":warning:" },
      error: { color: "#ff0000", icon: ":x:" },
      success: { color: "#36a64f", icon: ":white_check_mark:" }
    };
    
    const config = severityConfig[severity] || severityConfig.info;
    
    // Build Slack message payload
    const slackPayload = {
      attachments: [{
        color: config.color,
        fields: [
          {
            title: config.icon + " " + severity.toUpperCase(),
            value: message,
            short: false
          }
        ],
        timestamp: Math.floor(Date.now() / 1000)
      }]
    };
    
    // Add metadata if provided
    if (metadata && Object.keys(metadata).length > 0) {
      slackPayload.attachments[0].fields.push({
        title: "Additional Information",
        value: JSON.stringify(metadata, null, 2),
        short: false
      });
    }
    
    // Send to Slack
    const response = await fetch(webhook_url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(slackPayload)
    });
    
    if (!response.ok) {
      throw new Error("Failed to send Slack notification");
    }
    
    return {
      success: true,
      message_sent: message,
      severity: severity,
      sent_at: new Date().toISOString()
    };
  `
}
```

## Integration Patterns

### Using Actions in Function Stacks
```javascript
// Function stack integration
[
  {
    "function": "Get User Data",
    "action": "query_database",
    "table": "users",
    "where": { "id": "inputs.user_id" }
  },
  {
    "function": "Process User Data", 
    "action": "installed_action",
    "action_name": "user-data-processor",
    "inputs": {
      "user_data": "user_record",
      "processing_rules": "configuration.rules"
    }
  },
  {
    "function": "Send Notification",
    "action": "installed_action", 
    "action_name": "smart-slack-notifier",
    "inputs": {
      "message": "User data processed successfully",
      "severity": "success",
      "metadata": "processed_result"
    }
  }
]
```

### n8n Workflow Integration
```javascript
// n8n workflow using Xano Actions
{
  "name": "Data Processing Pipeline",
  "trigger": {
    "type": "webhook",
    "path": "/process-data"
  },
  "nodes": [
    {
      "name": "Transform Data",
      "type": "xano-action",
      "action": "advanced-json-transformer",
      "settings": {
        "source_data": "{{ $json }}",
        "mapping_rules": {
          "user.name": "customer_name",
          "user.email": "customer_email", 
          "order.total": "amount",
          "order.items": "line_items"
        }
      }
    },
    {
      "name": "Validate Result",
      "type": "xano-action",
      "action": "data-validator",
      "settings": {
        "data": "{{ $json.transformed_data }}",
        "schema": "customer-order-schema"
      }
    },
    {
      "name": "Notify Team",
      "type": "xano-action",
      "action": "smart-slack-notifier",
      "settings": {
        "message": "Data processing completed",
        "severity": "{{ $json.validation_passed ? 'success' : 'warning' }}",
        "metadata": "{{ $json }}"
      }
    }
  ]
}
```

## Try This: Create Your First Action

1. **Plan Your Action**
   - Identify a specific, reusable task
   - Define inputs and expected outputs
   - Ensure no external dependencies needed

2. **Build the Logic**
   - Start with simple data validation
   - Add core processing logic
   - Include error handling

3. **Test Thoroughly**
   - Test with various input combinations
   - Verify error handling works
   - Check output format consistency

4. **Document and Share**
   - Write clear instructions
   - Provide usage examples
   - Publish to Action marketplace

## Common Mistakes to Avoid

- **Including database dependencies** - Actions must work without specific tables
- **Hard-coding workspace values** - Use Settings Registry for configuration
- **Complex external dependencies** - Keep Actions focused and simple
- **Poor error handling** - Always validate inputs and handle edge cases
- **Insufficient documentation** - Clear instructions are essential for adoption

## Pro Tips

💡 **Focus on single responsibility** - Each Action should do one thing well

💡 **Use Settings Registry wisely** - For API keys and user-configurable values

💡 **Plan for reusability** - Design Actions that work in multiple contexts

💡 **Test without dependencies** - Ensure Actions work in isolation

💡 **Version your Actions** - Use semantic versioning for updates