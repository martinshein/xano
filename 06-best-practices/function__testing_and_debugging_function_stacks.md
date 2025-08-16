---
title: Testing and Debugging Function Stacks - Complete Guide for No-Code Development
description: Master testing and debugging techniques for Xano function stacks, including testing workflows, debugging tools, error handling, and performance optimization for n8n, WeWeb, and Make.com integrations
category: 06-best-practices
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - performance-optimization.md
  - troubleshooting-guide.md
  - function-stack-basics.md
subcategory: 06-best-practices
tags:
  - testing
  - debugging
  - function-stacks
  - performance
  - troubleshooting
  - best-practices
  - automation
  - quality-assurance
---

## 📋 **Quick Summary**

Learn comprehensive testing and debugging techniques for Xano function stacks to ensure reliable, high-performance applications. This guide covers testing workflows, debugging tools, error handling strategies, and performance optimization specifically designed for no-code developers using n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Complete testing workflow for function stacks in Xano
- Advanced debugging techniques and tools
- Performance monitoring and optimization strategies
- Error handling and troubleshooting methods
- Integration testing with external platforms (n8n, WeWeb, Make.com)
- Unit testing best practices for API endpoints
- Memory management and safe mode operations

## 🧪 **Testing Function Stacks**

### The Testing Workflow

**Step 1: Execute Your Function Stack**

Click the **Run** button at the top of your workflow to execute it. This opens the Run panel where you can input test data and review results.

**Step 2: Populate Test Inputs**

```javascript
// Example test input for user registration function
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securePassword123",
  "role": "customer"
}
```

**Pro Tip:** Use the Format button to structure JSON input properly. This makes your test data more readable without affecting functionality.

**Step 3: Run the Test**

Click **Run** to execute the workflow with your test data.

### 🔧 **Safe Mode Testing**

For large datasets or complex function stacks that might cause memory issues:

**When to Use Safe Mode:**
- Working with large data loops
- Processing bulk operations
- Experiencing crashes or memory issues
- Testing performance-intensive workflows

**How Safe Mode Works:**
```javascript
// Safe Mode limitations
{
  "memory_usage": "minimal - no context retained",
  "autocomplete": "disabled",
  "debugging_info": "limited",
  "benefits": [
    "prevents crashes with large datasets",
    "allows testing of resource-intensive operations",
    "maintains core functionality"
  ]
}
```

**To Enable Safe Mode:**
1. Click the arrow next to the Run button
2. Choose **Safe Mode**
3. Run your function stack normally

### 📊 **Understanding Test Results**

**Response Analysis:**
```javascript
// Example successful response
{
  "status": 201,
  "data": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2025-01-16T10:30:00Z"
  },
  "execution_time": "247ms"
}
```

**Key Actions in Response Panel:**
- **Copy Response**: Copy JSON for documentation or integration
- **Copy as cURL**: Generate cURL command for external testing
- **Create Unit Test**: Automatically generate test cases
- **Activate Debugger**: Deep-dive into execution steps

**Timing Analysis:**
The Timing block shows individual step performance:
```javascript
// Example timing breakdown
{
  "steps": [
    {"function": "validate_input", "time": "12ms"},
    {"function": "database_query", "time": "156ms"},
    {"function": "format_response", "time": "8ms"},
    {"function": "total_execution", "time": "247ms"}
  ]
}
```

### 📝 **Creating Swagger Documentation Examples**

**Setting Up API Examples:**

1. **After a successful test run**, click **Set As Example** in the response section
2. **Review and clean up** the sample input/output (remove sensitive data)
3. **Save the example** - it will appear in your Swagger documentation

**Example Documentation Structure:**
```javascript
// Swagger example for user creation endpoint
{
  "endpoint": "/api/users",
  "method": "POST",
  "example_input": {
    "name": "John Doe",
    "email": "john@example.com",
    "role": "customer"
  },
  "example_output": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2025-01-16T10:30:00Z"
  }
}
```

## 🔍 **Advanced Debugging Tools**

### Simple Mode Debugging

**Basic Debug Controls:**
- **Stop Debugging**: Exit debug mode
- **Restart Debugger**: Reset to beginning
- **Next Step**: Move through execution step by step

**Visual Debugging Features:**
- **Current Step**: Highlighted in the interface
- **Completed Steps**: Shown in green
- **Variables Panel**: Updates with current data at each step
- **Direct Navigation**: Click any step to jump to that point

### Advanced Debugging Options

**Step-by-Step Execution:**

**Step Over**: Skip nested functions (custom functions/middleware)
```javascript
// When to use Step Over
{
  "scenario": "debugging main workflow",
  "skip": ["custom_validation_function", "middleware_auth"],
  "focus": "primary business logic"
}
```

**Step Into/Step Out**: Navigate nested functions seamlessly
```javascript
// Debugging nested functions
{
  "step_into": "enter custom function debugging",
  "step_out": "return to main workflow debugging",
  "use_case": "troubleshooting specific custom functions"
}
```

**Advanced Debug Features:**

**Breakpoints**: Pause execution at specific steps
- Hover over the function icon
- Click to set/remove breakpoints
- Enable/disable all breakpoints globally

**Watches**: Monitor custom expressions
```javascript
// Example watch expressions
{
  "watches": [
    "user.email.length > 0",
    "data.total_records",
    "response.status === 200",
    "Math.round(performance.memory_usage)"
  ]
}
```

**Variables**: Real-time variable monitoring
- View current variable values
- Copy variable contents
- Add variables to watch list

## 🚨 **Error Handling and Troubleshooting**

### Common Error Types

**Unknown Error Messages:**
```javascript
// Typical error scenarios
{
  "unknown_error": {
    "causes": [
      "unhandled exception in logic",
      "rare edge case not covered",
      "server resource constraints"
    ],
    "solutions": [
      "review function logic",
      "contact support for rare errors",
      "try Safe Mode execution"
    ]
  }
}
```

**Debugger Errors:**
```javascript
// Debugger error handling
{
  "debugger_encountered_error": {
    "immediate_actions": [
      "try Safe Mode",
      "check memory usage",
      "review large dataset processing"
    ],
    "escalation": "contact support team"
  }
}
```

### Memory Management

**Safe Mode Implementation:**
```javascript
// Safe Mode configuration
{
  "memory_management": {
    "context_retention": false,
    "autocomplete": false,
    "debugging_info": "limited",
    "benefits": [
      "handles large datasets",
      "prevents memory crashes",
      "maintains core functionality"
    ]
  }
}
```

## 🔗 **Integration Testing with No-Code Platforms**

### n8n Workflow Testing

**Testing Xano Integration in n8n:**
```javascript
// n8n test workflow for Xano function stack
{
  "nodes": [
    {
      "name": "Test Data Generator",
      "type": "Function",
      "parameters": {
        "code": `
          return [
            {
              name: "Test User 1",
              email: "test1@example.com"
            },
            {
              name: "Test User 2", 
              email: "test2@example.com"
            }
          ];
        `
      }
    },
    {
      "name": "Create User in Xano",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-instance.xano.com/api/users",
        "method": "POST",
        "body": "{{ $json }}",
        "headers": {
          "Content-Type": "application/json",
          "Authorization": "Bearer YOUR_TOKEN"
        }
      }
    },
    {
      "name": "Validate Response",
      "type": "Function",
      "parameters": {
        "code": `
          if ($input.first().status !== 201) {
            throw new Error('User creation failed');
          }
          return $input.all();
        `
      }
    }
  ]
}
```

### WeWeb Integration Testing

**Testing Xano APIs in WeWeb:**
```javascript
// WeWeb testing framework for Xano integration
class XanoTestSuite {
  constructor(baseUrl, authToken) {
    this.baseUrl = baseUrl;
    this.authToken = authToken;
    this.testResults = [];
  }
  
  async testUserCreation(userData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/users`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.authToken}`
        },
        body: JSON.stringify(userData)
      });
      
      const result = await response.json();
      
      this.testResults.push({
        test: 'user_creation',
        status: response.status === 201 ? 'passed' : 'failed',
        response: result,
        timestamp: new Date().toISOString()
      });
      
      return result;
    } catch (error) {
      this.testResults.push({
        test: 'user_creation',
        status: 'error',
        error: error.message,
        timestamp: new Date().toISOString()
      });
      
      throw error;
    }
  }
  
  getTestResults() {
    return this.testResults;
  }
}

// Usage in WeWeb
const testSuite = new XanoTestSuite(
  'https://your-instance.xano.com',
  wwLib.wwVariable.getValue('auth_token')
);

await testSuite.testUserCreation({
  name: 'Test User',
  email: 'test@example.com'
});
```

### Make.com Integration Testing

**Testing Xano Scenarios in Make.com:**
```javascript
// Make.com test scenario configuration
{
  "scenario_name": "Test Xano User Management",
  "modules": [
    {
      "name": "HTTP Request - Create User",
      "type": "http",
      "url": "https://your-instance.xano.com/api/users",
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer {{auth_token}}"
      },
      "body": {
        "name": "{{test_name}}",
        "email": "{{test_email}}"
      }
    },
    {
      "name": "Condition - Check Success",
      "type": "condition",
      "condition": "{{1.status}} = 201"
    },
    {
      "name": "HTTP Request - Get User",
      "type": "http",
      "url": "https://your-instance.xano.com/api/users/{{1.id}}",
      "method": "GET",
      "headers": {
        "Authorization": "Bearer {{auth_token}}"
      }
    }
  ]
}
```

## 💡 **Testing Best Practices**

### Pre-Testing Checklist

```markdown
□ Test data prepared (no sensitive information)
□ Expected outcomes defined
□ Error scenarios identified
□ Performance benchmarks set
□ Integration endpoints verified
```

### During Testing

**Performance Monitoring:**
- Monitor execution times for each step
- Identify bottlenecks in the Timing panel
- Test with realistic data volumes
- Verify memory usage patterns

**Error Testing:**
- Test edge cases and invalid inputs
- Verify error handling and messages
- Check authentication failures
- Test rate limiting scenarios

### Post-Testing Actions

**Documentation:**
- Create Swagger examples from successful tests
- Document error scenarios and solutions
- Update integration guides
- Share test results with team

**Optimization:**
- Address performance bottlenecks
- Optimize slow-running steps
- Improve error handling
- Enhance user experience

## 🎯 **Testing Strategies by Use Case**

### API Endpoint Testing

**CRUD Operations Testing:**
```javascript
// Comprehensive API testing approach
const testSuite = {
  "create_test": {
    "endpoint": "/api/users",
    "method": "POST",
    "test_data": {"name": "Test", "email": "test@example.com"},
    "expected_status": 201
  },
  "read_test": {
    "endpoint": "/api/users/123",
    "method": "GET",
    "expected_status": 200
  },
  "update_test": {
    "endpoint": "/api/users/123",
    "method": "PATCH",
    "test_data": {"name": "Updated Name"},
    "expected_status": 200
  },
  "delete_test": {
    "endpoint": "/api/users/123",
    "method": "DELETE",
    "expected_status": 204
  }
};
```

### Integration Testing

**External API Integration:**
```javascript
// Testing external API calls
{
  "test_external_integration": {
    "description": "Test third-party API integration",
    "steps": [
      "mock external API response",
      "test successful integration",
      "test API failure scenarios",
      "verify error handling",
      "check retry mechanisms"
    ]
  }
}
```

### Performance Testing

**Load Testing Approach:**
```javascript
// Performance testing configuration
{
  "load_test": {
    "concurrent_users": 100,
    "test_duration": "5 minutes",
    "success_criteria": {
      "response_time": "< 500ms",
      "error_rate": "< 1%",
      "throughput": "> 1000 requests/minute"
    }
  }
}
```

---

**Next Steps**: Ready to optimize your function stacks? Continue with [Performance Optimization](performance-optimization.md) or explore [Troubleshooting Guide](troubleshooting-guide.md)