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
- Mathematical Operations
- Operator Precedence
- Data Types
- n8n
- WeWeb
- Logic
title: 'Operator Precedence & Expression System'
---

# Operator Precedence & Expression System

## 📋 **Quick Summary**
Master operator precedence and expression syntax in Xano for building complex mathematical calculations, conditional logic, and data transformations. Essential for creating dynamic business rules, pricing calculations, and automated decision-making in your n8n and WeWeb applications.

## 🎯 **Core Concepts**

### Understanding Operator Precedence
Operator precedence determines the order in which operations are evaluated in expressions. Just like in mathematics, some operators have higher priority and are calculated first, regardless of their position in the expression.

**Key Principles:**
- **Parentheses** have the highest precedence (force evaluation order)
- **Multiplication (*) and Division (/)** are evaluated before addition and subtraction
- **Left-to-Right** evaluation for operators of equal precedence
- **Logical operators** follow specific precedence rules for complex conditions

### The Expression System
Xano's expression system provides a flexible, real-time parsing environment that supports inline syntax for mathematical expressions, data manipulation, and conditional logic.

## 🔢 **Mathematical Operators**

### Basic Arithmetic
```javascript
// Mathematical operators and their precedence
{
  "arithmetic_operators": {
    "addition": {
      "operator": "+",
      "example": "100 + 101",
      "result": 201,
      "precedence": "low"
    },
    "subtraction": {
      "operator": "-", 
      "example": "100 - 101",
      "result": -1,
      "precedence": "low"
    },
    "multiplication": {
      "operator": "*",
      "example": "100 * 101", 
      "result": 10100,
      "precedence": "high"
    },
    "division": {
      "operator": "/",
      "example": "100 / 10",
      "result": 10,
      "precedence": "high"
    }
  }
}
```

### Operator Precedence Rules
```javascript
// Understanding evaluation order
{
  "precedence_examples": {
    "basic_left_to_right": {
      "expression": "1 + 2 + 3",
      "evaluation": "(1 + 2) + 3",
      "result": 6,
      "explanation": "Equal precedence operators evaluated left to right"
    },
    
    "multiplication_first": {
      "expression": "1 + 2 * 3", 
      "evaluation": "1 + (2 * 3)",
      "result": 7,
      "wrong_result": 9,
      "explanation": "Multiplication has higher precedence than addition"
    },
    
    "division_first": {
      "expression": "1 + 4 / 2",
      "evaluation": "1 + (4 / 2)", 
      "result": 3,
      "wrong_result": 2.5,
      "explanation": "Division has higher precedence than addition"
    },
    
    "parentheses_override": {
      "expression": "(1 + 2) * 3",
      "evaluation": "(1 + 2) * 3",
      "result": 9,
      "explanation": "Parentheses force evaluation order"
    }
  }
}
```

### Complex Mathematical Expressions
```javascript
// Advanced mathematical calculations with proper precedence
{
  "advanced_calculations": {
    "pricing_formula": {
      "base_price": 100,
      "tax_rate": 0.08,
      "discount_percentage": 15,
      "quantity": 3,
      "expression": "(base_price * quantity) * (1 - discount_percentage / 100) * (1 + tax_rate)",
      "evaluation_steps": [
        "base_price * quantity = 300",
        "discount_percentage / 100 = 0.15", 
        "1 - 0.15 = 0.85",
        "1 + tax_rate = 1.08",
        "300 * 0.85 = 255",
        "255 * 1.08 = 275.40"
      ],
      "final_result": 275.40
    },
    
    "compound_interest": {
      "principal": 1000,
      "rate": 0.05,
      "time": 2,
      "compounds_per_year": 4,
      "expression": "principal * (1 + rate / compounds_per_year) ^ (compounds_per_year * time)",
      "result": 1104.49
    }
  }
}
```

## 🔤 **Text and Array Operators**

### Text Concatenation
```javascript
// Text operators and string manipulation
{
  "text_operators": {
    "concatenation": {
      "operator": "~",
      "basic_example": "a ~ b",
      "result": "ab",
      "with_spaces": "a ~ ' ' ~ b",
      "spaced_result": "a b"
    },
    
    "dynamic_concatenation": {
      "user_data": {
        "first_name": "John",
        "last_name": "Doe" 
      },
      "expression": "first_name ~ ' ' ~ last_name",
      "result": "John Doe",
      "use_case": "Dynamic full name generation"
    },
    
    "template_building": {
      "email_template": "Hello ~ user.name ~ ', your order #' ~ order.id ~ ' has been confirmed.'",
      "variables": {
        "user.name": "Sarah",
        "order.id": "12345"
      },
      "result": "Hello Sarah, your order #12345 has been confirmed."
    }
  }
}
```

### Array Operations
```javascript
// Array operators and manipulation
{
  "array_operators": {
    "spread_operator": {
      "operator": "...",
      "example": "[1,2,3, ...[4,5,6], 7]",
      "result": [1,2,3,4,5,6,7],
      "use_case": "Merging arrays inline"
    },
    
    "range_operator": {
      "operator": "..",
      "example": "1..10", 
      "result": [1,2,3,4,5,6,7,8,9,10],
      "use_case": "Generating number sequences"
    },
    
    "array_indexing": {
      "array": ["a","b","c","d","e"],
      "positive_index": {
        "expression": "array[0]",
        "result": "a"
      },
      "negative_index": {
        "expression": "array[-1]", 
        "result": "e",
        "explanation": "Negative indexes count from the end"
      }
    }
  }
}
```

## 🔍 **Comparison and Logical Operators**

### Comparison Operators
```javascript
// Comparison operators with precedence considerations
{
  "comparison_operators": {
    "equality": [
      {
        "operator": "==",
        "description": "Equals with type conversion",
        "example": "1 == '1'",
        "result": true
      },
      {
        "operator": "===",
        "description": "Strict equals (no type conversion)",
        "example": "1 === '1'",
        "result": false
      }
    ],
    
    "inequality": [
      {
        "operator": "!=",
        "description": "Not equals with type conversion", 
        "example": "1 != '1'",
        "result": false
      },
      {
        "operator": "!==",
        "description": "Strict not equals",
        "example": "1 !== '1'",
        "result": true
      }
    ],
    
    "numerical": [
      {
        "operator": ">",
        "example": "5 > 3",
        "result": true
      },
      {
        "operator": ">=",
        "example": "5 >= 5", 
        "result": true
      },
      {
        "operator": "<",
        "example": "3 < 5",
        "result": true
      },
      {
        "operator": "<=",
        "example": "3 <= 3",
        "result": true
      }
    ]
  }
}
```

### Logical Operators and Precedence
```javascript
// Logical operators with precedence rules
{
  "logical_operators": {
    "not_operator": {
      "operator": "!",
      "example": "!true",
      "result": false,
      "precedence": "highest"
    },
    
    "and_operator": {
      "operator": "&&",
      "example": "1 < 2 && 1 != 1",
      "evaluation": "true && false", 
      "result": false,
      "precedence": "medium"
    },
    
    "or_operator": {
      "operator": "||",
      "example": "1 < 2 || 1 != 1",
      "evaluation": "true || false",
      "result": true,
      "precedence": "low"
    },
    
    "complex_logical": {
      "expression": "!false && (true || false) && 5 > 3",
      "evaluation_steps": [
        "!false = true",
        "(true || false) = true",
        "5 > 3 = true", 
        "true && true && true = true"
      ],
      "result": true
    }
  }
}
```

## 🔀 **Conditional Operators**

### Ternary Operators
```javascript
// Conditional operators for inline decision making
{
  "conditional_operators": {
    "traditional_ternary": {
      "operator": "a ? b : c",
      "description": "If/else conditional",
      "example": "1 < 2 ? 'yes' : 'no'",
      "result": "yes",
      "use_case": "Simple conditional assignment"
    },
    
    "shorthand_ternary": {
      "operator": "a ?: b", 
      "description": "This/that (truthiness check)",
      "example": "1 ?: 2",
      "result": 1,
      "explanation": "Returns first truthy value"
    },
    
    "null_coalescing": {
      "operator": "a ?? b",
      "description": "Null coalescing",
      "example": "null ?? 10",
      "result": 10,
      "explanation": "Returns right value only if left is null/undefined"
    }
  }
}
```

### Advanced Conditional Logic
```javascript
// Complex conditional expressions for business logic
{
  "business_logic_examples": {
    "user_discount": {
      "scenario": "Calculate user discount based on membership and order value",
      "variables": {
        "user_tier": "premium",
        "order_total": 150,
        "is_first_order": false
      },
      "expression": "(user_tier === 'premium' ? 0.15 : user_tier === 'gold' ? 0.10 : 0.05) + (order_total > 100 ? 0.05 : 0) + (is_first_order ? 0.10 : 0)",
      "calculation": "0.15 + 0.05 + 0 = 0.20",
      "result": "20% discount"
    },
    
    "shipping_calculation": {
      "variables": {
        "weight": 2.5,
        "distance": 150,
        "is_expedited": true
      },
      "base_rate": 10,
      "expression": "base_rate + (weight > 2 ? (weight - 2) * 3 : 0) + (distance > 100 ? 15 : 5) + (is_expedited ? 25 : 0)",
      "calculation": "10 + 1.5 + 15 + 25 = 51.5",
      "result": 51.50
    }
  }
}
```

## 🔗 **n8n Integration Examples**

### Dynamic Calculations in Workflows
```javascript
// n8n workflow with complex expression calculations
{
  "n8n_calculation_workflow": {
    "nodes": [
      {
        "node": "Webhook",
        "description": "Receive order data"
      },
      {
        "node": "Set Variables", 
        "variables": {
          "base_price": "{{$json.base_price}}",
          "quantity": "{{$json.quantity}}",
          "discount_code": "{{$json.discount_code}}"
        }
      },
      {
        "node": "Code",
        "code": `
// Complex pricing calculation with operator precedence
const calculatePrice = () => {
  const basePrice = $node.Set_Variables.json.base_price;
  const quantity = $node.Set_Variables.json.quantity;
  const discountCode = $node.Set_Variables.json.discount_code;
  
  // Tiered pricing based on quantity
  const unitPrice = quantity >= 10 ? basePrice * 0.9 : 
                   quantity >= 5 ? basePrice * 0.95 : 
                   basePrice;
  
  // Apply discount codes
  const discountMultiplier = discountCode === 'SAVE20' ? 0.8 :
                            discountCode === 'SAVE10' ? 0.9 :
                            1.0;
  
  // Calculate final total
  const subtotal = unitPrice * quantity;
  const discountedTotal = subtotal * discountMultiplier;
  const tax = discountedTotal * 0.08;
  const finalTotal = discountedTotal + tax;
  
  return {
    subtotal,
    discountedTotal,
    tax,
    finalTotal: Math.round(finalTotal * 100) / 100
  };
};

return [calculatePrice()];`
      },
      {
        "node": "HTTP Request",
        "method": "POST",
        "url": "{{xano_instance}}/api/orders/create",
        "body": {
          "pricing_details": "{{$json}}"
        }
      }
    ]
  }
}
```

### Conditional Workflow Routing
```javascript
// Use expressions for dynamic workflow routing
{
  "conditional_routing": {
    "order_processing_logic": {
      "expression": "order_value > 500 ? 'high_value' : order_value > 100 ? 'medium_value' : 'standard'",
      "routing": {
        "high_value": "Manual review workflow",
        "medium_value": "Automated approval with manager notification",
        "standard": "Instant processing"
      }
    },
    
    "user_onboarding_path": {
      "expression": "user_type === 'enterprise' ? 'enterprise_setup' : user_referral_code ? 'referral_bonus' : 'standard_onboarding'",
      "paths": {
        "enterprise_setup": "Custom onboarding with dedicated support",
        "referral_bonus": "Standard onboarding + referral rewards",
        "standard_onboarding": "Default user experience"
      }
    }
  }
}
```

## 🌐 **WeWeb Integration**

### Dynamic UI Calculations
```javascript
// WeWeb component with dynamic calculations
{
  "weweb_dynamic_calculations": {
    "shopping_cart_component": {
      "computed_properties": {
        "subtotal": "items.reduce((sum, item) => sum + (item.price * item.quantity), 0)",
        "shipping": "subtotal > 50 ? 0 : 9.99",
        "tax": "subtotal * 0.08",
        "total": "subtotal + shipping + tax"
      },
      
      "discount_logic": `
// Complex discount calculation with operator precedence
const calculateDiscount = (subtotal, userTier, couponCode) => {
  // Base discount by user tier
  const tierDiscount = userTier === 'platinum' ? 0.15 :
                      userTier === 'gold' ? 0.10 :
                      userTier === 'silver' ? 0.05 : 0;
  
  // Coupon code discounts
  const couponDiscount = couponCode === 'WELCOME20' ? 0.20 :
                        couponCode === 'SAVE15' ? 0.15 :
                        couponCode === 'FREESHIP' ? 0 : 0;
  
  // Apply maximum discount rule: tier OR coupon, whichever is higher
  const maxDiscount = Math.max(tierDiscount, couponDiscount);
  
  // Apply minimum order requirements
  const finalDiscount = subtotal >= 25 ? maxDiscount : maxDiscount * 0.5;
  
  return subtotal * finalDiscount;
};`
    }
  }
}
```

### Real-Time Formula Validation
```javascript
// WeWeb form with real-time calculation validation
{
  "formula_validation": {
    "loan_calculator": {
      "inputs": ["principal", "rate", "term"],
      "formula": "principal * (rate * (1 + rate)^term) / ((1 + rate)^term - 1)",
      "validation_rules": {
        "principal": "principal > 0 && principal <= 1000000",
        "rate": "rate > 0 && rate <= 0.30", 
        "term": "term >= 1 && term <= 30"
      },
      "real_time_calculation": `
// WeWeb computed property with operator precedence
computed: {
  monthlyPayment() {
    const P = this.principal;
    const r = this.rate / 12; // Monthly rate
    const n = this.term * 12; // Total payments
    
    if (P && r && n) {
      // PMT formula: P * [r(1+r)^n] / [(1+r)^n - 1]
      const numerator = P * (r * Math.pow(1 + r, n));
      const denominator = Math.pow(1 + r, n) - 1;
      
      return Math.round((numerator / denominator) * 100) / 100;
    }
    return 0;
  }
}`
    }
  }
}
```

## 🎯 **Best Practices**

### Expression Optimization
```javascript
// Best practices for efficient expressions
{
  "optimization_guidelines": {
    "parentheses_usage": [
      "Use parentheses to make precedence explicit",
      "Group related operations for clarity",
      "Force evaluation order when needed"
    ],
    
    "performance_tips": [
      "Cache complex calculations in variables",
      "Avoid nested ternary operators when possible", 
      "Use early returns with logical operators",
      "Minimize expensive operations in loops"
    ],
    
    "readability": [
      "Break complex expressions into multiple steps",
      "Use meaningful variable names",
      "Add comments for complex business logic",
      "Consider custom functions for reusable calculations"
    ]
  }
}
```

### Common Pitfalls
```javascript
// Avoid these common expression mistakes
{
  "common_mistakes": {
    "precedence_confusion": {
      "mistake": "1 + 2 * 3 + 4",
      "expected": 21,
      "actual": 11,
      "solution": "(1 + 2) * (3 + 4)"
    },
    
    "type_coercion": {
      "mistake": "'5' + 3",
      "expected": 8,
      "actual": "53",
      "solution": "parseInt('5') + 3"
    },
    
    "null_handling": {
      "mistake": "user.age > 18",
      "problem": "Fails if user.age is null",
      "solution": "(user.age ?? 0) > 18"
    }
  }
}
```

---

*Master operator precedence and expression syntax to build sophisticated calculations, dynamic business logic, and intelligent decision-making systems in your Xano applications. These patterns form the foundation for complex automation and data-driven functionality.*