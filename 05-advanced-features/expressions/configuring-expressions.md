---
title: Configuring Expressions - Advanced Conditional Logic and Data Validation
description: Complete guide to configuring expressions and conditional logic in Xano, including operators, data validation, and best practices for no-code platforms
category: expressions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - api__master_metadata_api.md
  - advanced_back_end_features.md
  - allow_direct_query.md
subcategory: 05-advanced-features/expressions
tags:
  - expressions
  - conditional-logic
  - data-validation
  - operators
  - filtering
  - no-code
---

## 📋 **Quick Summary**

Expressions in Xano provide powerful conditional logic and data validation capabilities using a comprehensive set of operators. This system enables complex data filtering, validation rules, and business logic implementation essential for building sophisticated applications with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Understanding expression builder components and operators
- Implementing conditional logic with AND/OR combinations
- Using comparison, text, and array operators effectively
- Building complex validation rules and filters
- Best practices for expression optimization and debugging
- Integration patterns for no-code platform automation

# Configuring Expressions

## Overview

**Expressions** in Xano are the foundation for implementing conditional logic, data validation, and filtering operations throughout your application. The expression builder provides a visual interface for creating complex conditional statements that determine how data flows through your function stacks and API endpoints.

### Expression Components

**Basic Structure:**
- **Conditional Type**: Determines logical combination (AND/OR)
- **Left Value**: The data field or variable being evaluated
- **Operator**: The comparison or evaluation method
- **Right Value**: The comparison value or reference

**Advanced Features:**
- Nested conditional groups for complex logic
- Variable references and dynamic value evaluation
- Type-aware comparisons and validations
- Real-time expression testing and debugging

## 🔧 **Expression Builder Components**

### Conditional Types

**AND Conditionals:**
- Require all conditions to be satisfied
- Used for restrictive filtering and validation
- Example: "User is admin AND account is active"
- Best for security and access control logic

**OR Conditionals:**
- Require any condition to be satisfied
- Used for inclusive filtering and alternatives
- Example: "User is admin OR user is manager"
- Best for flexible access patterns and fallbacks

### n8n Expression Integration

```javascript
// n8n workflow for dynamic expression building and evaluation
{
  "nodes": [
    {
      "name": "Build Dynamic Expression",
      "type": "Code",
      "parameters": {
        "jsCode": `
          // Expression builder for dynamic Xano filters
          const expressionBuilder = {
            conditions: [],
            
            addCondition(leftValue, operator, rightValue, conditionalType = 'AND') {
              this.conditions.push({
                conditional_type: conditionalType,
                left_value: leftValue,
                operator: operator,
                right_value: rightValue
              });
              return this;
            },
            
            addGroup(groupConditions, conditionalType = 'AND') {
              this.conditions.push({
                conditional_type: conditionalType,
                group: groupConditions
              });
              return this;
            },
            
            build() {
              return {
                filter_type: 'expression',
                conditions: this.conditions
              };
            },
            
            // Pre-built expression templates
            createUserAccessFilter(userId, roles = []) {
              return this
                .addCondition('user_id', '==', userId)
                .addCondition('status', '==', 'active', 'AND')
                .addCondition('role', 'IN', roles, 'AND')
                .build();
            },
            
            createDateRangeFilter(startDate, endDate, dateField = 'created_at') {
              return this
                .addCondition(dateField, '>=', startDate)
                .addCondition(dateField, '<=', endDate, 'AND')
                .build();
            },
            
            createTextSearchFilter(searchTerm, fields = ['name', 'description']) {
              const searchConditions = fields.map((field, index) => ({
                conditional_type: index === 0 ? 'OR' : 'OR',
                left_value: field,
                operator: 'INCLUDES',
                right_value: searchTerm
              }));
              
              return {
                filter_type: 'expression',
                conditions: searchConditions
              };
            },
            
            createAdvancedProductFilter(criteria) {
              const { category, priceMin, priceMax, inStock, tags, rating } = criteria;
              
              this.addCondition('category', '==', category);
              
              if (priceMin !== undefined) {
                this.addCondition('price', '>=', priceMin, 'AND');
              }
              
              if (priceMax !== undefined) {
                this.addCondition('price', '<=', priceMax, 'AND');
              }
              
              if (inStock) {
                this.addCondition('stock_quantity', '>', 0, 'AND');
              }
              
              if (tags && tags.length > 0) {
                this.addCondition('tags', 'OVERLAPS', tags, 'AND');
              }
              
              if (rating) {
                this.addCondition('average_rating', '>=', rating, 'AND');
              }
              
              return this.build();
            }
          };
          
          // Example usage with dynamic criteria
          const userCriteria = {
            user_id: $env.USER_ID,
            roles: ['admin', 'manager'],
            start_date: $env.START_DATE,
            end_date: $env.END_DATE
          };
          
          // Build user access filter
          const userFilter = expressionBuilder.createUserAccessFilter(
            userCriteria.user_id,
            userCriteria.roles
          );
          
          // Build date range filter
          const dateFilter = expressionBuilder.createDateRangeFilter(
            userCriteria.start_date,
            userCriteria.end_date
          );
          
          // Build combined expression
          const combinedExpression = {
            filter_type: 'expression',
            conditions: [
              {
                conditional_type: 'AND',
                group: userFilter.conditions
              },
              {
                conditional_type: 'AND',
                group: dateFilter.conditions
              }
            ]
          };
          
          return [{
            json: {
              user_filter: userFilter,
              date_filter: dateFilter,
              combined_expression: combinedExpression,
              expression_count: combinedExpression.conditions.length
            }
          }];
        `
      }
    },
    {
      "name": "Execute Xano Query with Expression",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/query-with-expression",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "table": "{{ $env.TARGET_TABLE }}",
          "expression": "{{ $json.combined_expression }}",
          "limit": "{{ $env.QUERY_LIMIT || 50 }}",
          "sort": "{{ $env.SORT_FIELD || 'created_at' }} {{ $env.SORT_ORDER || 'desc' }}"
        }
      }
    },
    {
      "name": "Validate Expression Results",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const queryResult = $input.first().json;
          const expressionData = $('Build Dynamic Expression').first().json;
          
          // Validate and analyze query results
          const validation = {
            success: queryResult.success || false,
            results_count: queryResult.data?.length || 0,
            expression_complexity: calculateExpressionComplexity(expressionData.combined_expression),
            performance_metrics: {
              execution_time: queryResult.execution_time || null,
              rows_scanned: queryResult.rows_scanned || null,
              index_usage: queryResult.index_usage || null
            },
            recommendations: generateOptimizationRecommendations(queryResult, expressionData)
          };
          
          function calculateExpressionComplexity(expression) {
            let complexity = 0;
            
            if (expression.conditions) {
              expression.conditions.forEach(condition => {
                complexity += 1;
                if (condition.group) {
                  complexity += condition.group.length;
                }
              });
            }
            
            return {
              total_conditions: complexity,
              complexity_level: complexity <= 3 ? 'simple' : 
                               complexity <= 7 ? 'moderate' : 'complex'
            };
          }
          
          function generateOptimizationRecommendations(result, expressionData) {
            const recommendations = [];
            
            // Performance recommendations
            if (result.execution_time > 1000) {
              recommendations.push({
                type: 'performance',
                priority: 'high',
                message: 'Query execution time is high. Consider adding database indexes.',
                suggestion: 'Add indexes on frequently filtered columns'
              });
            }
            
            // Expression complexity recommendations
            if (expressionData.combined_expression.conditions.length > 5) {
              recommendations.push({
                type: 'complexity',
                priority: 'medium',
                message: 'Complex expression detected. Consider breaking into multiple queries.',
                suggestion: 'Split complex filters into multiple simpler queries'
              });
            }
            
            // Result count recommendations
            if (validation.results_count === 0) {
              recommendations.push({
                type: 'results',
                priority: 'low',
                message: 'No results returned. Verify filter criteria.',
                suggestion: 'Check if filter conditions are too restrictive'
              });
            }
            
            return recommendations;
          }
          
          return [{ json: validation }];
        `
      }
    }
  ]
}
```

### WeWeb Expression Builder Interface

```javascript
// WeWeb component for dynamic expression building
class XanoExpressionBuilder {
  constructor() {
    this.conditions = [];
    this.operators = this.initializeOperators();
    this.dataTypes = this.initializeDataTypes();
  }
  
  initializeOperators() {
    return {
      comparison: [
        { value: '==', label: 'Equals', types: ['all'] },
        { value: '!=', label: 'Not Equals', types: ['all'] },
        { value: '===', label: 'Equals (Type Match)', types: ['all'] },
        { value: '!==', label: 'Not Equals (Type Match)', types: ['all'] },
        { value: '>', label: 'Greater Than', types: ['number', 'date'] },
        { value: '>=', label: 'Greater Than or Equal', types: ['number', 'date'] },
        { value: '<', label: 'Less Than', types: ['number', 'date'] },
        { value: '<=', label: 'Less Than or Equal', types: ['number', 'date'] }
      ],
      text: [
        { value: 'LIKE', label: 'Like (Case Insensitive)', types: ['text'] },
        { value: 'NOT LIKE', label: 'Not Like', types: ['text'] },
        { value: 'INCLUDES', label: 'Includes (Partial Match)', types: ['text'] },
        { value: 'DOES NOT INCLUDE', label: 'Does Not Include', types: ['text'] },
        { value: 'REGEX MATCHES', label: 'Regex Matches', types: ['text'] },
        { value: 'REGEX DOES NOT MATCH', label: 'Regex Does Not Match', types: ['text'] }
      ],
      array: [
        { value: 'IN', label: 'In Array', types: ['array'] },
        { value: 'NOT IN', label: 'Not In Array', types: ['array'] },
        { value: 'OVERLAPS', label: 'Arrays Overlap', types: ['array'] },
        { value: 'DOES NOT OVERLAP', label: 'Arrays Do Not Overlap', types: ['array'] },
        { value: 'CONTAINS', label: 'Contains (Exact Schema)', types: ['json', 'array'] },
        { value: 'DOES NOT CONTAIN', label: 'Does Not Contain', types: ['json', 'array'] }
      ]
    };
  }
  
  initializeDataTypes() {
    return {
      text: { validation: /^.+$/, defaultValue: '' },
      number: { validation: /^-?\d*\.?\d+$/, defaultValue: 0 },
      boolean: { validation: /^(true|false)$/, defaultValue: false },
      date: { validation: /^\d{4}-\d{2}-\d{2}/, defaultValue: new Date().toISOString().split('T')[0] },
      array: { validation: null, defaultValue: [] },
      json: { validation: null, defaultValue: {} }
    };
  }
  
  addCondition(conditionalType = 'AND') {
    const newCondition = {
      id: this.generateConditionId(),
      conditional_type: conditionalType,
      left_value: '',
      operator: '==',
      right_value: '',
      data_type: 'text',
      validation_errors: []
    };
    
    this.conditions.push(newCondition);
    this.updateWeWebVariables();
    return newCondition;
  }
  
  removeCondition(conditionId) {
    this.conditions = this.conditions.filter(condition => condition.id !== conditionId);
    this.updateWeWebVariables();
  }
  
  updateCondition(conditionId, updates) {
    const condition = this.conditions.find(c => c.id === conditionId);
    if (condition) {
      Object.assign(condition, updates);
      
      // Validate the updated condition
      condition.validation_errors = this.validateCondition(condition);
      
      // Auto-adjust operator based on data type
      if (updates.data_type) {
        condition.operator = this.getDefaultOperatorForType(updates.data_type);
      }
      
      this.updateWeWebVariables();
    }
  }
  
  validateCondition(condition) {
    const errors = [];
    
    // Validate left value
    if (!condition.left_value.trim()) {
      errors.push('Left value is required');
    }
    
    // Validate right value based on data type
    const dataType = this.dataTypes[condition.data_type];
    if (dataType && dataType.validation) {
      if (!dataType.validation.test(condition.right_value)) {
        errors.push(`Invalid ${condition.data_type} format`);
      }
    }
    
    // Validate operator compatibility
    const validOperators = this.getOperatorsForType(condition.data_type);
    if (!validOperators.includes(condition.operator)) {
      errors.push(`Operator '${condition.operator}' not valid for ${condition.data_type}`);
    }
    
    return errors;
  }
  
  getOperatorsForType(dataType) {
    const allOperators = [...this.operators.comparison, ...this.operators.text, ...this.operators.array];
    return allOperators
      .filter(op => op.types.includes('all') || op.types.includes(dataType))
      .map(op => op.value);
  }
  
  getDefaultOperatorForType(dataType) {
    switch (dataType) {
      case 'text': return 'INCLUDES';
      case 'number': case 'date': return '>=';
      case 'boolean': return '==';
      case 'array': return 'IN';
      case 'json': return 'CONTAINS';
      default: return '==';
    }
  }
  
  generateConditionId() {
    return `condition_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
  
  buildExpression() {
    // Validate all conditions first
    const validConditions = this.conditions.filter(condition => {
      condition.validation_errors = this.validateCondition(condition);
      return condition.validation_errors.length === 0;
    });
    
    if (validConditions.length === 0) {
      throw new Error('No valid conditions found');
    }
    
    return {
      filter_type: 'expression',
      conditions: validConditions.map(condition => ({
        conditional_type: condition.conditional_type,
        left_value: condition.left_value,
        operator: condition.operator,
        right_value: this.formatRightValue(condition.right_value, condition.data_type)
      })),
      metadata: {
        created_at: new Date().toISOString(),
        condition_count: validConditions.length,
        complexity_score: this.calculateComplexityScore(validConditions)
      }
    };
  }
  
  formatRightValue(value, dataType) {
    switch (dataType) {
      case 'number':
        return parseFloat(value);
      case 'boolean':
        return value === 'true' || value === true;
      case 'array':
        return Array.isArray(value) ? value : value.split(',').map(v => v.trim());
      case 'json':
        return typeof value === 'object' ? value : JSON.parse(value);
      default:
        return value;
    }
  }
  
  calculateComplexityScore(conditions) {
    let score = conditions.length;
    
    // Add complexity for advanced operators
    conditions.forEach(condition => {
      if (['REGEX MATCHES', 'CONTAINS', 'OVERLAPS'].includes(condition.operator)) {
        score += 2;
      } else if (['INCLUDES', 'IN'].includes(condition.operator)) {
        score += 1;
      }
    });
    
    return score;
  }
  
  testExpression(sampleData) {
    try {
      const expression = this.buildExpression();
      const results = sampleData.filter(item => this.evaluateExpression(item, expression));
      
      return {
        success: true,
        matched_count: results.length,
        total_count: sampleData.length,
        match_percentage: (results.length / sampleData.length * 100).toFixed(1),
        sample_results: results.slice(0, 5),
        expression: expression
      };
    } catch (error) {
      return {
        success: false,
        error: error.message,
        expression: null
      };
    }
  }
  
  evaluateExpression(item, expression) {
    // Simple client-side expression evaluation for testing
    let result = true;
    let currentOperator = 'AND';
    
    expression.conditions.forEach((condition, index) => {
      const leftValue = this.getValueFromPath(item, condition.left_value);
      const rightValue = condition.right_value;
      const conditionResult = this.evaluateCondition(leftValue, condition.operator, rightValue);
      
      if (index === 0) {
        result = conditionResult;
      } else {
        if (currentOperator === 'AND') {
          result = result && conditionResult;
        } else {
          result = result || conditionResult;
        }
      }
      
      currentOperator = condition.conditional_type;
    });
    
    return result;
  }
  
  getValueFromPath(object, path) {
    return path.split('.').reduce((obj, key) => obj && obj[key], object);
  }
  
  evaluateCondition(leftValue, operator, rightValue) {
    switch (operator) {
      case '==': return leftValue == rightValue;
      case '!=': return leftValue != rightValue;
      case '===': return leftValue === rightValue;
      case '!==': return leftValue !== rightValue;
      case '>': return leftValue > rightValue;
      case '>=': return leftValue >= rightValue;
      case '<': return leftValue < rightValue;
      case '<=': return leftValue <= rightValue;
      case 'INCLUDES': return String(leftValue).toLowerCase().includes(String(rightValue).toLowerCase());
      case 'LIKE': return String(leftValue).toLowerCase() === String(rightValue).toLowerCase();
      case 'IN': return Array.isArray(rightValue) && rightValue.includes(leftValue);
      case 'OVERLAPS': 
        return Array.isArray(leftValue) && Array.isArray(rightValue) && 
               leftValue.some(val => rightValue.includes(val));
      default: return false;
    }
  }
  
  updateWeWebVariables() {
    wwLib.wwVariable.updateValue('expression_conditions', this.conditions);
    wwLib.wwVariable.updateValue('expression_valid', this.conditions.every(c => c.validation_errors.length === 0));
    wwLib.wwVariable.updateValue('condition_count', this.conditions.length);
  }
  
  loadTemplate(template) {
    switch (template) {
      case 'user_filter':
        this.conditions = [
          {
            id: this.generateConditionId(),
            conditional_type: 'AND',
            left_value: 'status',
            operator: '==',
            right_value: 'active',
            data_type: 'text',
            validation_errors: []
          },
          {
            id: this.generateConditionId(),
            conditional_type: 'AND',
            left_value: 'role',
            operator: 'IN',
            right_value: ['admin', 'manager'],
            data_type: 'array',
            validation_errors: []
          }
        ];
        break;
      case 'date_range':
        this.conditions = [
          {
            id: this.generateConditionId(),
            conditional_type: 'AND',
            left_value: 'created_at',
            operator: '>=',
            right_value: new Date(Date.now() - 30*24*60*60*1000).toISOString().split('T')[0],
            data_type: 'date',
            validation_errors: []
          },
          {
            id: this.generateConditionId(),
            conditional_type: 'AND',
            left_value: 'created_at',
            operator: '<=',
            right_value: new Date().toISOString().split('T')[0],
            data_type: 'date',
            validation_errors: []
          }
        ];
        break;
      case 'text_search':
        this.conditions = [
          {
            id: this.generateConditionId(),
            conditional_type: 'OR',
            left_value: 'name',
            operator: 'INCLUDES',
            right_value: '',
            data_type: 'text',
            validation_errors: []
          },
          {
            id: this.generateConditionId(),
            conditional_type: 'OR',
            left_value: 'description',
            operator: 'INCLUDES',
            right_value: '',
            data_type: 'text',
            validation_errors: []
          }
        ];
        break;
    }
    this.updateWeWebVariables();
  }
}

// Initialize expression builder
const expressionBuilder = new XanoExpressionBuilder();

// Usage functions for WeWeb
function addNewCondition() {
  const conditionalType = wwLib.wwVariable.getValue('new_condition_type') || 'AND';
  expressionBuilder.addCondition(conditionalType);
}

function removeCondition() {
  const conditionId = wwLib.wwVariable.getValue('condition_to_remove');
  expressionBuilder.removeCondition(conditionId);
}

function updateConditionField() {
  const conditionId = wwLib.wwVariable.getValue('current_condition_id');
  const field = wwLib.wwVariable.getValue('update_field');
  const value = wwLib.wwVariable.getValue('update_value');
  
  expressionBuilder.updateCondition(conditionId, { [field]: value });
}

function buildAndTestExpression() {
  try {
    const expression = expressionBuilder.buildExpression();
    wwLib.wwVariable.updateValue('built_expression', expression);
    wwLib.wwUtils.showSuccessToast('Expression built successfully');
    
    // Test with sample data if available
    const sampleData = wwLib.wwVariable.getValue('test_data');
    if (sampleData && Array.isArray(sampleData)) {
      const testResults = expressionBuilder.testExpression(sampleData);
      wwLib.wwVariable.updateValue('test_results', testResults);
    }
  } catch (error) {
    wwLib.wwUtils.showErrorToast(`Expression error: ${error.message}`);
  }
}

function loadExpressionTemplate() {
  const template = wwLib.wwVariable.getValue('selected_template');
  expressionBuilder.loadTemplate(template);
}

// Auto-save functionality
setInterval(() => {
  const expression = expressionBuilder.conditions;
  localStorage.setItem('xano_expression_draft', JSON.stringify(expression));
}, 5000);

// Load saved draft on initialization
const savedDraft = localStorage.getItem('xano_expression_draft');
if (savedDraft) {
  try {
    expressionBuilder.conditions = JSON.parse(savedDraft);
    expressionBuilder.updateWeWebVariables();
  } catch (error) {
    console.error('Failed to load expression draft:', error);
  }
}
```

## 📊 **Comprehensive Operator Reference**

### Comparison Operators

**Equals (==)**
- **Use Case**: Exact value matching
- **Example**: `user_id == 12345`
- **Best For**: ID matching, status checks, boolean values

**Not Equals (!=)**
- **Use Case**: Exclusion filtering
- **Example**: `status != 'deleted'`
- **Best For**: Excluding specific values or states

**Type-Strict Equals (===)**
- **Use Case**: Value and type matching
- **Example**: `age === 25` (number 25, not string "25")
- **Best For**: Ensuring data type consistency

**Greater/Less Than (>, >=, <, <=)**
- **Use Case**: Numeric and date comparisons
- **Example**: `price >= 100`, `created_at < '2023-01-01'`
- **Best For**: Range filtering, date filtering, numeric thresholds

### Text Operators

**LIKE (Case Insensitive)**
- **Use Case**: Exact text matching ignoring case
- **Example**: `name LIKE 'John'` matches "john", "JOHN", "John"
- **Best For**: Name matching, case-insensitive equality

**INCLUDES (Partial Match)**
- **Use Case**: Substring searching
- **Example**: `description INCLUDES 'premium'`
- **Best For**: Search functionality, keyword filtering

**REGEX MATCHES**
- **Use Case**: Pattern matching with regular expressions
- **Example**: `email REGEX MATCHES '^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$'`
- **Best For**: Email validation, phone number formats, complex patterns

### Array and JSON Operators

**IN/NOT IN**
- **Use Case**: Checking if value exists in array
- **Example**: `category IN ['electronics', 'computers']`
- **Best For**: Multi-select filters, role checking

**OVERLAPS/DOES NOT OVERLAP**
- **Use Case**: Comparing two arrays for common elements
- **Example**: `user_tags OVERLAPS ['premium', 'vip']`
- **Best For**: Tag matching, permission checking

**CONTAINS/DOES NOT CONTAIN**
- **Use Case**: Exact schema matching in JSON/arrays
- **Example**: `metadata CONTAINS {'verified': true}`
- **Best For**: Complex object validation, nested data filtering

## 💡 **Pro Tips**

- **Performance**: Use indexed fields in left values for faster queries
- **Type Safety**: Always use type-strict operators (===, !==) when type matters
- **Readability**: Group related conditions and use clear variable names
- **Testing**: Test expressions with sample data before deployment
- **Optimization**: Avoid complex regex in high-volume queries
- **Maintenance**: Document complex expressions with comments in function stacks

## 🔧 **Troubleshooting**

### Common Expression Issues

**Problem**: Expression returns unexpected results  
**Solution**: Check data types and use appropriate operators; test with sample data

**Problem**: Performance issues with complex expressions  
**Solution**: Simplify expressions, add database indexes, or split into multiple queries

**Problem**: Type mismatch errors  
**Solution**: Use type-strict operators and validate data types before comparison

**Problem**: Regex patterns not matching  
**Solution**: Test regex patterns separately and escape special characters properly

---

**Next Steps**: Ready to implement advanced conditional logic? Explore [Advanced Backend Features](advanced_back_end_features.md) for comprehensive data handling or check [Master Metadata API](api__master_metadata_api.md) for programmatic access