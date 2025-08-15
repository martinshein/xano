---
title: "Expression Builder - Dynamic Query Logic"
description: "Master Xano's Expression Builder for creating dynamic, computed fields, conditional logic, and advanced data transformations in your database operations"
category: data-operations
tags:
  - Expression Builder
  - Dynamic Expressions
  - Computed Fields
  - Conditional Logic
  - Data Transformation
  - Advanced Queries
difficulty: advanced
reading_time: 15 minutes
last_updated: '2025-01-15'
prerequisites:
  - Understanding of database operations
  - Familiarity with JavaScript expressions
  - Knowledge of Xano data types
---

# Expression Builder - Dynamic Query Logic

## 📋 **Quick Summary**

**What it does:** The Expression Builder allows you to create dynamic, computed fields and conditional logic using JavaScript-like expressions within your database operations and function stacks.

**Why it matters:** Expression Builder enables you to:
- **Create computed fields** that calculate values dynamically
- **Build conditional logic** for complex data processing
- **Transform data** on-the-fly during queries
- **Implement business rules** directly in your database layer
- **Reduce code complexity** with declarative expressions

**Time to implement:** 15-20 minutes for basic expressions, 1+ hour for complex business logic

---

## What You'll Learn

- How to use Xano's Expression Builder effectively
- Creating computed fields and dynamic calculations
- Building conditional expressions and business rules
- Performance optimization for expression-heavy queries
- Integration patterns with no-code platforms

## Basic Expression Syntax

### Simple Computed Fields

```javascript
// Basic mathematical expressions
{
  "total_price": "quantity * unit_price",
  "discount_amount": "total_price * (discount_percentage / 100)",
  "final_price": "total_price - discount_amount",
  "tax_amount": "final_price * 0.08"
}

// String concatenation
{
  "full_name": "first_name + ' ' + last_name",
  "email_display": "name + ' <' + email + '>'",
  "formatted_phone": "'+1 (' + area_code + ') ' + phone_number"
}

// Date calculations
{
  "days_since_created": "(now() - created_at) / (24 * 60 * 60 * 1000)",
  "is_recent": "days_since_created <= 30",
  "expiry_date": "created_at + (30 * 24 * 60 * 60 * 1000)"
}
```

### Conditional Expressions

```javascript
// If-then-else logic
{
  "status_label": "status === 'active' ? 'Active User' : status === 'pending' ? 'Pending Approval' : 'Inactive'",
  
  "priority_level": "total_spent > 1000 ? 'high' : total_spent > 500 ? 'medium' : 'low'",
  
  "shipping_cost": "total_amount > 50 ? 0 : weight > 5 ? 15.99 : 9.99",
  
  "user_type": "subscription_type ? 'premium' : total_orders > 10 ? 'valued' : 'standard'"
}
```

## Advanced Expression Patterns

### Complex Business Logic

```javascript
// E-commerce pricing logic
class PricingExpressions {
  static getProductPricingExpressions() {
    return {
      // Base calculations
      "base_price": "original_price",
      
      // Quantity discounts
      "quantity_discount": `
        quantity >= 100 ? 0.20 :
        quantity >= 50 ? 0.15 :
        quantity >= 20 ? 0.10 :
        quantity >= 10 ? 0.05 : 0
      `,
      
      // Seasonal pricing
      "seasonal_multiplier": `
        (function() {
          const month = new Date().getMonth() + 1;
          return month === 12 || month === 1 ? 1.2 :
                 month >= 6 && month <= 8 ? 0.9 : 1.0;
        })()
      `,
      
      // Customer tier pricing
      "tier_discount": `
        customer_tier === 'platinum' ? 0.25 :
        customer_tier === 'gold' ? 0.15 :
        customer_tier === 'silver' ? 0.10 : 0
      `,
      
      // Final price calculation
      "final_price": `
        base_price * 
        (1 - quantity_discount) * 
        seasonal_multiplier * 
        (1 - tier_discount)
      `,
      
      // Savings display
      "total_savings": "base_price - final_price",
      "savings_percentage": "(total_savings / base_price) * 100"
    };
  }
}
```

### User Segmentation Logic

```javascript
// Dynamic user segmentation
const userSegmentationExpressions = {
  // Activity score calculation
  "activity_score": `
    (login_count * 0.3) + 
    (order_count * 0.4) + 
    (review_count * 0.2) + 
    (referral_count * 0.1)
  `,
  
  // Engagement level
  "engagement_level": `
    activity_score >= 100 ? 'high' :
    activity_score >= 50 ? 'medium' :
    activity_score >= 20 ? 'low' : 'inactive'
  `,
  
  // Customer lifetime value prediction
  "predicted_ltv": `
    (average_order_value * order_frequency * 12) * 
    (engagement_level === 'high' ? 2.5 :
     engagement_level === 'medium' ? 1.8 :
     engagement_level === 'low' ? 1.2 : 0.5)
  `,
  
  // Churn risk assessment
  "churn_risk": `
    (function() {
      const daysSinceLastOrder = (Date.now() - last_order_date) / (24 * 60 * 60 * 1000);
      const daysSinceLastLogin = (Date.now() - last_login_date) / (24 * 60 * 60 * 1000);
      
      if (daysSinceLastOrder > 90 || daysSinceLastLogin > 60) return 'high';
      if (daysSinceLastOrder > 60 || daysSinceLastLogin > 30) return 'medium';
      return 'low';
    })()
  `,
  
  // Personalization tags
  "personalization_tags": `
    [
      churn_risk === 'high' ? 'retention_campaign' : null,
      predicted_ltv > 1000 ? 'vip_treatment' : null,
      engagement_level === 'high' ? 'brand_advocate' : null,
      order_count === 1 ? 'first_time_buyer' : null
    ].filter(tag => tag !== null)
  `
};
```

## Function Stack Integration

### Dynamic Query Building

```javascript
// Function that uses expressions to build dynamic queries
function buildDynamicProductQuery(filters) {
  const baseQuery = {
    table: 'products',
    fields: [
      'id',
      'name',
      'original_price',
      'category',
      'stock_quantity',
      // Dynamic computed fields
      {
        field: 'current_price',
        expression: `
          original_price * 
          (1 - (sale_discount || 0)) * 
          (category === 'clearance' ? 0.7 : 1.0)
        `
      },
      {
        field: 'availability_status',
        expression: `
          stock_quantity > 20 ? 'in_stock' :
          stock_quantity > 0 ? 'low_stock' : 'out_of_stock'
        `
      },
      {
        field: 'price_tier',
        expression: `
          current_price > 100 ? 'premium' :
          current_price > 50 ? 'mid_range' : 'budget'
        `
      },
      {
        field: 'is_featured',
        expression: `
          featured === true || 
          (new Date() - created_at) / (24 * 60 * 60 * 1000) <= 7 ||
          rating >= 4.5
        `
      }
    ]
  };
  
  // Add dynamic filters based on user input
  const dynamicFilters = {};
  
  if (filters.priceRange) {
    dynamicFilters.current_price = {
      $gte: filters.priceRange.min,
      $lte: filters.priceRange.max
    };
  }
  
  if (filters.availability) {
    dynamicFilters.availability_status = filters.availability;
  }
  
  if (filters.featured) {
    dynamicFilters.is_featured = true;
  }
  
  baseQuery.filters = dynamicFilters;
  
  return baseQuery;
}
```

### Real-time Data Processing

```javascript
// Order processing with dynamic calculations
function processOrderWithExpressions(orderData) {
  const orderCalculations = {
    // Line item calculations
    line_items: orderData.items.map(item => ({
      ...item,
      // Dynamic line total with complex business rules
      line_total: `
        (function() {
          const baseTotal = quantity * unit_price;
          
          // Volume discount
          const volumeDiscount = quantity >= 10 ? 0.1 : 
                                quantity >= 5 ? 0.05 : 0;
          
          // Product-specific discount
          const productDiscount = product_category === 'clearance' ? 0.2 : 0;
          
          // Apply discounts
          return baseTotal * (1 - Math.max(volumeDiscount, productDiscount));
        })()
      `,
      
      // Tax calculation per item
      tax_amount: `
        line_total * (tax_rate || 0.08)
      `
    })),
    
    // Order-level calculations
    subtotal: `
      line_items.reduce((sum, item) => sum + item.line_total, 0)
    `,
    
    total_tax: `
      line_items.reduce((sum, item) => sum + item.tax_amount, 0)
    `,
    
    // Shipping calculation
    shipping_cost: `
      (function() {
        if (subtotal >= 75) return 0; // Free shipping
        
        const weight = line_items.reduce((sum, item) => sum + (item.weight * item.quantity), 0);
        const baseShipping = weight <= 5 ? 9.99 : 15.99;
        
        // Express shipping multiplier
        return shipping_method === 'express' ? baseShipping * 1.5 : baseShipping;
      })()
    `,
    
    // Final total
    grand_total: `subtotal + total_tax + shipping_cost`,
    
    // Order classification
    order_type: `
      grand_total > 500 ? 'large' :
      grand_total > 200 ? 'medium' : 'small'
    `,
    
    // Processing priority
    processing_priority: `
      customer_tier === 'platinum' ? 1 :
      shipping_method === 'express' ? 2 :
      order_type === 'large' ? 3 : 5
    `
  };
  
  return orderCalculations;
}
```

## No-Code Platform Integration

### 🔗 **n8n Expression Workflows**

```javascript
// n8n workflow with dynamic expressions
function processDataWithExpressions($input) {
  const data = $input.body;
  
  // Apply expressions to transform data
  const transformedData = data.map(record => ({
    ...record,
    
    // Computed fields using expressions
    computed_fields: {
      // Age calculation
      age: `Math.floor((Date.now() - new Date(birth_date)) / (365.25 * 24 * 60 * 60 * 1000))`,
      
      // Status determination
      status: `
        age >= 65 ? 'senior' :
        age >= 18 ? 'adult' :
        age >= 13 ? 'teen' : 'child'
      `,
      
      // Score calculation
      engagement_score: `
        (email_opens * 2) + 
        (link_clicks * 5) + 
        (purchases * 10) + 
        (referrals * 15)
      `,
      
      // Segment assignment
      segment: `
        engagement_score >= 100 ? 'champion' :
        engagement_score >= 50 ? 'loyal' :
        engagement_score >= 20 ? 'potential' : 'new'
      `
    }
  }));
  
  return {
    success: true,
    processed_count: transformedData.length,
    data: transformedData
  };
}
```

### 🌐 **WeWeb Dynamic Display**

```javascript
// WeWeb component with expression-based display logic
class WeWebExpressionHelper {
  static setupDynamicDisplay() {
    // Register computed properties
    wwLib.computed.register('userDisplayInfo', (user) => {
      return {
        // Dynamic name formatting
        display_name: user.preferred_name || `${user.first_name} ${user.last_name}`,
        
        // Status badge
        status_badge: {
          text: user.subscription_active ? 'Premium' : 
                user.trial_active ? 'Trial' : 'Free',
          color: user.subscription_active ? 'gold' : 
                 user.trial_active ? 'blue' : 'gray'
        },
        
        // Progress indicators
        profile_completion: Math.round(
          (Object.values(user.profile).filter(v => v).length / 
           Object.keys(user.profile).length) * 100
        ),
        
        // Activity status
        activity_level: (() => {
          const daysSinceLogin = Math.floor(
            (Date.now() - new Date(user.last_login)) / (24 * 60 * 60 * 1000)
          );
          
          return daysSinceLogin <= 1 ? 'very_active' :
                 daysSinceLogin <= 7 ? 'active' :
                 daysSinceLogin <= 30 ? 'moderate' : 'inactive';
        })()
      };
    });
    
    // Dynamic content visibility
    wwLib.computed.register('contentVisibility', (user, content) => {
      return {
        show_premium: user.subscription_active || user.trial_active,
        show_upgrade: !user.subscription_active,
        show_onboarding: user.profile_completion < 50,
        show_activity_prompt: user.activity_level === 'inactive'
      };
    });
  }
  
  static applyDynamicStyling(element, expressions) {
    Object.keys(expressions).forEach(property => {
      const value = this.evaluateExpression(expressions[property]);
      element.style[property] = value;
    });
  }
  
  static evaluateExpression(expression) {
    // Safe expression evaluation with context
    try {
      const context = {
        user: wwLib.auth.getCurrentUser(),
        theme: wwLib.theme.getCurrent(),
        viewport: wwLib.viewport.getInfo(),
        ...wwLib.variables
      };
      
      return new Function('ctx', `with(ctx) { return ${expression}; }`)(context);
    } catch (error) {
      console.error('Expression evaluation failed:', error);
      return null;
    }
  }
}
```

## Performance Optimization

### Expression Optimization Strategies

```javascript
// Optimize expressions for better performance
class ExpressionOptimizer {
  static optimizeExpressions(expressions) {
    const optimized = {};
    
    Object.keys(expressions).forEach(key => {
      const expr = expressions[key];
      
      // Cache complex calculations
      if (this.isComplexExpression(expr)) {
        optimized[key] = this.addCaching(expr);
      }
      
      // Simplify redundant calculations
      else if (this.hasRedundantCalculations(expr)) {
        optimized[key] = this.simplifyExpression(expr);
      }
      
      // Keep simple expressions as-is
      else {
        optimized[key] = expr;
      }
    });
    
    return optimized;
  }
  
  static isComplexExpression(expr) {
    // Check for function calls, loops, or heavy calculations
    return expr.includes('function') || 
           expr.includes('reduce') || 
           expr.includes('map') ||
           expr.split('*').length > 3;
  }
  
  static addCaching(expr) {
    return `
      (function() {
        const cacheKey = JSON.stringify(arguments);
        if (this._cache && this._cache[cacheKey]) {
          return this._cache[cacheKey];
        }
        
        const result = ${expr};
        
        if (!this._cache) this._cache = {};
        this._cache[cacheKey] = result;
        
        return result;
      })()
    `;
  }
  
  static simplifyExpression(expr) {
    // Basic expression simplification
    return expr
      .replace(/\s+/g, ' ')
      .replace(/\(\s*([^)]+)\s*\)/g, '($1)')
      .trim();
  }
  
  static getPerformanceRecommendations(expressions) {
    const recommendations = [];
    
    Object.keys(expressions).forEach(key => {
      const expr = expressions[key];
      
      if (this.isComplexExpression(expr)) {
        recommendations.push({
          field: key,
          type: 'performance',
          message: 'Consider caching this complex expression',
          severity: 'medium'
        });
      }
      
      if (expr.includes('Date.now()')) {
        recommendations.push({
          field: key,
          type: 'optimization',
          message: 'Consider passing current time as parameter instead of recalculating',
          severity: 'low'
        });
      }
    });
    
    return recommendations;
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Create basic computed fields:
1. Calculate user age from birth date
2. Create full name from first and last name
3. Determine account status based on subscription
4. Calculate days since last login

### Intermediate Challenge
Build conditional business logic:
1. Create dynamic pricing based on quantity and customer tier
2. Implement user segmentation with multiple criteria
3. Build order priority calculation system
4. Create engagement score formula

### Advanced Challenge
Design complex expression system:
1. Build comprehensive product recommendation engine
2. Create dynamic personalization system
3. Implement real-time risk assessment
4. Build performance-optimized expression cache

## Best Practices

1. **Keep expressions readable** - Use clear variable names and formatting
2. **Avoid over-complexity** - Break complex logic into multiple expressions
3. **Cache expensive calculations** - Store results of heavy computations
4. **Test thoroughly** - Validate expressions with various data inputs
5. **Document business rules** - Explain the logic behind complex expressions
6. **Monitor performance** - Track execution time for expression-heavy queries

## Next Steps

- Master [Query All Records](query_all_records.md) for expression-enhanced queries
- Learn [Database Requests](database_requests.md) for comprehensive operations
- Explore [OR Conditions](two_conditions_combined_with_or.md) for complex filtering
- Understand [Database Transactions](add_a_database_transaction_function_to_your_function_stack_.md) for atomic operations

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Expression building discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Advanced expression guides
- 📖 [Expression Examples](../examples/expressions.md) - Real-world patterns
- 🔧 [Support](https://xano.com/support) - Complex expression assistance