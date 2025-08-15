---
title: "Testing and Debugging Function Stacks"
description: "Master Xano's testing and debugging tools to ensure your function stacks work perfectly and troubleshoot issues effectively"
category: function-stack
difficulty: intermediate
tags:
  - testing
  - debugging
  - function-stack
  - troubleshooting
  - performance
  - safe-mode
related_docs:
  - unit-tests
  - test-suites
  - performance
  - error-handling
last_updated: '2025-01-23'
---

# Testing and Debugging Function Stacks

## Quick Summary
Xano provides powerful testing and debugging tools to ensure your function stacks execute correctly. Test your workflows with sample data, use the debugger to step through execution, and identify performance bottlenecks - all essential for building reliable backend systems.

## What You'll Learn
- How to test function stacks with sample inputs
- Using the visual debugger to troubleshoot issues
- Understanding execution timing and performance
- Setting up Swagger documentation examples
- Working with Safe Mode for memory-intensive operations
- Best practices for debugging complex workflows

## Testing Your Function Stack

### Basic Testing Process

**Step 1: Start the Test**
Click the "Run" button at the top of your function stack to open the testing panel.

**Step 2: Provide Input Data**
Add test data that matches your expected inputs:

```json
{
  "user_id": 123,
  "action": "update_profile",
  "data": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

**Step 3: Execute and Review**
Click "Run" to execute and review:
- Response data and structure
- Execution timing for each step
- Any errors or warnings

### Safe Mode Testing

For memory-intensive operations, use Safe Mode:

```bash
# When to use Safe Mode:
- Processing large datasets
- Complex loops with many iterations
- Memory allocation issues
- Function stack crashes
```

Safe Mode limitations:
- No context retention in memory
- Limited autocomplete functionality
- Reduced debugging information

## Understanding Test Results

### Response Analysis
Your test results include:

**Response Data**: The actual output from your function stack
```json
{
  "success": true,
  "user": {
    "id": 123,
    "name": "John Doe",
    "updated_at": "2025-01-23T10:30:00Z"
  }
}
```

**Execution Timing**: Performance breakdown by step
- Database queries: 45ms
- External API calls: 120ms
- Data processing: 15ms
- Total execution: 180ms

**Available Actions**:
- Copy response data
- Generate cURL command
- Create unit test
- Set as Swagger example

## The Visual Debugger

### Debugger Basics

The debugger lets you step through execution to identify issues:

**Simple Mode Features**:
- Step-by-step execution review
- Variable state inspection
- Highlighted current step
- Green highlighting for completed steps

**Advanced Mode Options**:
- **Step Over**: Skip nested functions
- **Step Into/Out**: Navigate nested function stacks
- **Continue**: Resume normal execution
- **Breakpoints**: Pause at specific steps
- **Watches**: Monitor custom expressions

### Debugging Workflow

```javascript
// Debugging process example
1. Run your function stack normally
2. Activate debugger from response panel
3. Step through each function
4. Check variable values at each step
5. Identify where issues occur
```

### Variable Inspection

Monitor data changes through execution:

```json
// Step 1: Initial variables
{
  "input": {"user_id": 123},
  "user": null
}

// Step 2: After database query
{
  "input": {"user_id": 123},
  "user": {"id": 123, "name": "John"}
}

// Step 3: After processing
{
  "input": {"user_id": 123},
  "user": {"id": 123, "name": "John"},
  "result": "success"
}
```

## Integration Patterns

### For n8n Users
Use Xano test results to configure n8n HTTP Request nodes:

```javascript
// n8n HTTP Request Configuration
{
  "method": "POST",
  "url": "https://your-instance.xano.io/api:endpoint",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{$node['Auth'].json['token']}}"
  },
  "body": {
    "user_id": "{{$node['Previous'].json['id']}}",
    "action": "update_profile"
  }
}
```

### For WeWeb Users
Test data helps configure WeWeb data sources:

1. Run tests with realistic data
2. Copy response structure
3. Use in WeWeb data binding
4. Configure error handling based on test results

### Swagger Documentation Examples

Set up API documentation with test data:

```yaml
# Generated from test results
paths:
  /api/users/update:
    post:
      summary: "Update user profile"
      requestBody:
        example:
          user_id: 123
          data:
            name: "John Doe"
            email: "john@example.com"
      responses:
        200:
          example:
            success: true
            user:
              id: 123
              name: "John Doe"
              updated_at: "2025-01-23T10:30:00Z"
```

## Advanced Debugging Techniques

### Performance Optimization

Identify bottlenecks using timing analysis:

```javascript
// Performance analysis example
Function Stack Timing:
├── Get User Query: 45ms (GOOD)
├── External API Call: 250ms (SLOW - optimize)
├── Data Processing: 15ms (GOOD)
└── Update Record: 30ms (GOOD)

Total: 340ms (Target: <200ms)
```

### Error Handling and Recovery

Test error scenarios:

```json
// Test with invalid data
{
  "user_id": "invalid",
  "action": null
}

// Expected error response
{
  "error": true,
  "message": "Invalid user ID format",
  "code": "VALIDATION_ERROR"
}
```

### Complex Workflow Testing

For multi-step workflows:

```javascript
// Test workflow phases
Phase 1: Data Validation ✓
Phase 2: External API Integration ✓  
Phase 3: Database Transaction ✗ (Error here)
Phase 4: Notification Sending (Not reached)

// Focus debugging on Phase 3
```

## Try This
1. **Basic Test**: Run a simple function stack with sample data
2. **Debug Mode**: Activate debugger and step through execution
3. **Performance Check**: Review timing for optimization opportunities
4. **Error Testing**: Try invalid inputs to test error handling
5. **Documentation**: Set response as Swagger example

## Common Mistakes to Avoid

❌ **Don't:**
- Skip testing with realistic data
- Ignore performance timing
- Test only happy path scenarios
- Forget to document test cases
- Leave sensitive data in examples

✅ **Do:**
- Test with various input scenarios
- Monitor execution performance
- Test error conditions thoroughly
- Document expected behaviors
- Use Safe Mode for large datasets

## Pro Tips

💡 **Testing Best Practices:**
- Create comprehensive test scenarios
- Use realistic data volumes
- Test edge cases and error conditions
- Document expected behaviors

🚀 **Debugging Efficiency:**
- Use breakpoints for complex issues
- Monitor variable changes step-by-step
- Focus on timing for performance issues
- Test with production-like data

⚡ **Performance Optimization:**
- Identify slow steps using timing analysis
- Test with large datasets in Safe Mode
- Optimize database queries based on timing
- Monitor memory usage patterns

## Error Resolution

### Common Error Types

**Unknown Errors**:
- Unhandled exceptions in logic
- Server resource constraints
- Memory allocation issues

**Debugger Errors**:
- Complex nested function issues
- Large dataset processing problems
- Resource timeout scenarios

**Resolution Steps**:
1. Enable Safe Mode for memory issues
2. Check individual step outputs
3. Verify input data format
4. Contact support for unhandled exceptions

## Performance Considerations

### Timing Analysis
- Database operations: Aim for <50ms
- External APIs: Budget 100-200ms
- Data processing: Keep under 20ms
- Total execution: Target <500ms

### Memory Management
- Use Safe Mode for large datasets
- Monitor variable sizes during execution
- Optimize loops and iterations
- Consider pagination for large results

Your testing and debugging workflow ensures reliable, performant function stacks that handle real-world scenarios effectively.