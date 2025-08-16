---
title: Mathematical Filters Reference - Complete Guide for No-Code Development
description: Master Xano's comprehensive mathematical filter library including arithmetic operations, trigonometric functions, logarithms, statistical calculations, and advanced mathematical operations for data processing in n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - bitwise-filters.md
  - array-statistics.md
  - numeric-operations.md
tags:
  - mathematical-filters
  - arithmetic-operations
  - trigonometric-functions
  - logarithms
  - statistical-calculations
  - numeric-processing
---

## 📋 **Quick Summary**

Master Xano's complete mathematical filter library for sophisticated numeric processing and calculations. This comprehensive reference covers arithmetic operations, trigonometric functions, logarithms, statistical calculations, and advanced mathematical operations essential for building data-driven applications with n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Complete mathematical filters reference with practical examples
- Arithmetic operations (add, subtract, multiply, divide)
- Trigonometric functions (sin, cos, tan, arc functions)
- Logarithmic and exponential operations
- Statistical calculations (average, min, max, sum)
- Number formatting and rounding techniques
- Performance optimization for mathematical operations
- Integration patterns for complex calculations

# Mathematical Filters Reference

## ➕ **Basic Arithmetic Operations**

### add

**Purpose**: Add two values together and return the result.

**Parameters:**
- `parent_value`: The first number in the addition
- `value`: The second number to add to the primary value

**Examples:**

```javascript
// Basic addition
parent_value: 5
value: 3
// Output: 8

// Decimal addition
parent_value: 10.5
value: 4.2
// Output: 14.7

// Negative numbers
parent_value: -2
value: 7
// Output: 5
```

**🔗 Real-World Applications:**

**E-commerce Total Calculation:**
```javascript
// n8n: Calculate order totals
const orderItems = [
  { name: "Laptop", price: 999.99, quantity: 1 },
  { name: "Mouse", price: 29.99, quantity: 2 },
  { name: "Keyboard", price: 79.99, quantity: 1 }
];

const subtotal = orderItems.reduce((total, item) => 
  total.add(item.price.multiply(item.quantity)), 0
);

const tax = subtotal.multiply(0.08);
const shipping = 15.99;
const finalTotal = subtotal.add(tax).add(shipping);
```

**Financial Planning:**
```javascript
// WeWeb: Budget calculation
const monthlyIncomes = [3500, 2800, 4200, 3100];
const totalIncome = monthlyIncomes.reduce((sum, income) => 
  sum.add(income), 0
);

const monthlyExpenses = [2200, 800, 450, 300];
const totalExpenses = monthlyExpenses.reduce((sum, expense) => 
  sum.add(expense), 0
);

const netIncome = totalIncome.subtract(totalExpenses);
```

### subtract

**Purpose**: Subtract two values and return the result.

**Examples:**

```javascript
// Basic subtraction
parent_value: 10
value: 4
// Output: 6

// Negative result
parent_value: 5
value: 8
// Output: -3

// Decimal subtraction
parent_value: 3.5
value: 1.2
// Output: 2.3
```

### multiply

**Purpose**: Multiply two values together and return the result.

**Examples:**

```javascript
// Basic multiplication
parent_value: 4
value: 3
// Output: 12

// Decimal multiplication
parent_value: 2.5
value: 6
// Output: 15

// Negative multiplication
parent_value: -7
value: 2
// Output: -14
```

**🔗 Scaling and Unit Conversion:**

```javascript
// Make.com: Unit conversions and scaling
const convertUnits = (value, conversionFactor) => {
  return value.multiply(conversionFactor);
};

// Examples
const milesPerHour = 60;
const kilometersPerHour = milesPerHour.multiply(1.60934);

const fahrenheit = 68;
const celsius = fahrenheit.subtract(32).multiply(5).divide(9);

const pounds = 150;
const kilograms = pounds.multiply(0.453592);
```

### divide

**Purpose**: Divide two values and return the result.

**Examples:**

```javascript
// Basic division
parent_value: 10
value: 2
// Output: 5

// Decimal result
parent_value: 7
value: 2
// Output: 3.5

// Exact division
parent_value: 9
value: 3
// Output: 3
```

**🔗 Rate and Ratio Calculations:**

```javascript
// n8n: Performance metrics calculation
const calculateMetrics = (data) => {
  const totalViews = data.views.sum();
  const totalClicks = data.clicks.sum();
  const totalConversions = data.conversions.sum();
  
  return {
    click_through_rate: totalClicks.divide(totalViews).multiply(100),
    conversion_rate: totalConversions.divide(totalClicks).multiply(100),
    cost_per_conversion: data.total_spend.divide(totalConversions),
    average_order_value: data.total_revenue.divide(totalConversions)
  };
};
```

## 📊 **Statistical Operations**

### sum

**Purpose**: Returns the sum of all values in an array.

**Examples:**

```javascript
// Integer array
parent_value: [1, 2, 3, 4, 5]
// Output: 15

// Decimal array
parent_value: [10.5, 20.3, 5.7]
// Output: 36.5

// Mixed positive/negative
parent_value: [-1, 0, 1]
// Output: 0
```

### avg

**Purpose**: Returns the average (mean) of all values in an array.

**Examples:**

```javascript
// Simple average
parent_value: [1, 2, 3, 4, 5]
// Output: 3

// Decimal average
parent_value: [10, 20, 30, 40]
// Output: 25

// Fractional average
parent_value: [2.5, 3.5, 4.5]
// Output: 3.5
```

**🔗 Analytics and Reporting:**

```javascript
// WeWeb: User engagement analytics
const calculateEngagementMetrics = (userSessions) => {
  const sessionDurations = userSessions.map(session => session.duration);
  const pageViews = userSessions.map(session => session.page_views);
  const bounceRates = userSessions.map(session => session.bounce_rate);
  
  return {
    average_session_duration: sessionDurations.avg(),
    total_page_views: pageViews.sum(),
    average_page_views: pageViews.avg(),
    overall_bounce_rate: bounceRates.avg(),
    engagement_score: sessionDurations.avg().multiply(pageViews.avg()).divide(100)
  };
};
```

### array_max / array_min

**Purpose**: Returns the maximum or minimum value from an array.

**Examples:**

```javascript
// Finding maximum
parent_value: [1, 5, 3, 9, 2]
// array_max output: 9

// Finding minimum
parent_value: [1, 5, 3, 9, 2]
// array_min output: 1

// Negative numbers
parent_value: [-10, -5, -20]
// array_max output: -5
// array_min output: -20
```

### max / min

**Purpose**: Returns the maximum or minimum of two values.

**Examples:**

```javascript
// Two positive numbers
parent_value: 5
value: 10
// max output: 10
// min output: 5

// Negative numbers
parent_value: -3
value: -7
// max output: -3
// min output: -7

// Decimals
parent_value: 8.2
value: 8.15
// max output: 8.2
// min output: 8.15
```

**🔗 Data Validation and Constraints:**

```javascript
// Make.com: Implement data constraints
const applyConstraints = (userInput, constraints) => {
  return {
    age: userInput.age.max(constraints.min_age).min(constraints.max_age),
    salary: userInput.salary.max(constraints.min_salary).min(constraints.max_salary),
    score: userInput.score.max(0).min(100), // 0-100 range
    rating: userInput.rating.max(1).min(5)   // 1-5 star rating
  };
};
```

## 🔄 **Rounding and Formatting**

### round

**Purpose**: Round a decimal to a specified precision.

**Parameters:**
- `parent_value`: The number to round
- `precision`: Number of decimal places (default: 0)

**Examples:**

```javascript
// Round to nearest integer
parent_value: 3.14159
precision: 0
// Output: 3

// Round to 2 decimal places
parent_value: 3.14159
precision: 2
// Output: 3.14

// Round negative number
parent_value: -3.55
precision: 1
// Output: -3.6
```

### ceil

**Purpose**: Round a decimal up to its integer equivalent.

**Examples:**

```javascript
// Round up positive
parent_value: 3.1
// Output: 4

// Round up large decimal
parent_value: 7.9
// Output: 8

// Round up negative (towards zero)
parent_value: -2.3
// Output: -2
```

### floor

**Purpose**: Round a decimal down to its integer equivalent.

**Examples:**

```javascript
// Round down positive
parent_value: 3.7
// Output: 3

// Round down large decimal
parent_value: 8.1
// Output: 8

// Round down negative (away from zero)
parent_value: -2.3
// Output: -3
```

**🔗 Pagination and Chunking:**

```javascript
// n8n: Calculate pagination parameters
const calculatePagination = (totalItems, itemsPerPage, currentPage) => {
  const totalPages = totalItems.divide(itemsPerPage).ceil();
  const offset = currentPage.subtract(1).multiply(itemsPerPage);
  const remainingItems = totalItems.subtract(offset);
  const itemsOnPage = remainingItems.min(itemsPerPage);
  
  return {
    total_pages: totalPages,
    current_page: currentPage,
    items_per_page: itemsPerPage,
    offset: offset,
    items_on_page: itemsOnPage,
    has_next: currentPage < totalPages,
    has_previous: currentPage > 1
  };
};
```

### number_format

**Purpose**: Format a number with flexible decimal places and separators.

**Parameters:**
- `parent_value`: The number to format
- `decimal_places`: Number of decimal places (default: 0)
- `decimal_separator`: Character for decimal point (default: ".")
- `thousands_separator`: Character for thousands separator (default: ",")

**Examples:**

```javascript
// Standard US format
parent_value: 1234.56
decimal_places: 2
decimal_separator: "."
thousands_separator: ","
// Output: "1,234.56"

// European format
parent_value: 1234.56
decimal_places: 2
decimal_separator: ","
thousands_separator: " "
// Output: "1 234,56"

// Integer display
parent_value: 1234.56
decimal_places: 0
// Output: "1,235"
```

**🔗 Financial and Currency Display:**

```javascript
// WeWeb: Multi-currency formatting
const formatCurrency = (amount, currency, locale) => {
  const formats = {
    'USD': { decimal_places: 2, decimal_separator: '.', thousands_separator: ',' },
    'EUR': { decimal_places: 2, decimal_separator: ',', thousands_separator: ' ' },
    'JPY': { decimal_places: 0, decimal_separator: '.', thousands_separator: ',' }
  };
  
  const format = formats[currency] || formats['USD'];
  const formatted = amount.number_format(
    format.decimal_places,
    format.decimal_separator,
    format.thousands_separator
  );
  
  const symbols = { 'USD': '$', 'EUR': '€', 'JPY': '¥' };
  return `${symbols[currency] || currency} ${formatted}`;
};
```

## 🔢 **Advanced Mathematical Functions**

### pow

**Purpose**: Returns the value raised to the power of exponent.

**Examples:**

```javascript
// Basic exponentiation
parent_value: 2
exponent: 3
// Output: 8

// Square
parent_value: 10
exponent: 2
// Output: 100

// Fractional exponent (square root)
parent_value: 3
exponent: 0.5
// Output: 1.7320508075
```

### sqrt

**Purpose**: Returns the square root of the value.

**Examples:**

```javascript
// Perfect square
parent_value: 4
// Output: 2

// Another perfect square
parent_value: 9
// Output: 3

// Irrational result
parent_value: 2
// Output: 1.4142136
```

**🔗 Distance and Geometry Calculations:**

```javascript
// Make.com: Calculate distances and areas
const calculateDistance = (point1, point2) => {
  const deltaX = point2.x.subtract(point1.x);
  const deltaY = point2.y.subtract(point1.y);
  const distanceSquared = deltaX.pow(2).add(deltaY.pow(2));
  return distanceSquared.sqrt();
};

const calculateCircleArea = (radius) => {
  const pi = 3.14159265359;
  return pi.multiply(radius.pow(2));
};

const calculateTriangleArea = (base, height) => {
  return base.multiply(height).divide(2);
};
```

### abs

**Purpose**: Returns the absolute value (magnitude) of a number.

**Examples:**

```javascript
// Negative to positive
parent_value: -5
// Output: 5

// Positive unchanged
parent_value: 10
// Output: 10

// Decimal
parent_value: -3.14
// Output: 3.14
```

### modulus

**Purpose**: Returns the remainder after division.

**Examples:**

```javascript
// Basic modulus
parent_value: 7
value: 3
// Output: 1

// Larger example
parent_value: 15
value: 4
// Output: 3

// Negative dividend
parent_value: -8
value: 3
// Output: -2
```

**🔗 Cyclic Operations and Patterns:**

```javascript
// n8n: Implement cyclic patterns
const createCyclicPattern = (items, cycleLength) => {
  return items.map((item, index) => ({
    ...item,
    cycle_position: index.modulus(cycleLength),
    is_cycle_start: index.modulus(cycleLength) === 0,
    cycle_number: index.divide(cycleLength).floor().add(1)
  }));
};

// Time-based patterns
const getTimePattern = (timestamp) => {
  const hours = timestamp.divide(3600).floor().modulus(24);
  const minutes = timestamp.divide(60).floor().modulus(60);
  const seconds = timestamp.modulus(60);
  
  return {
    hours: hours,
    minutes: minutes,
    seconds: seconds,
    is_even_hour: hours.modulus(2) === 0,
    quarter_hour: minutes.divide(15).floor()
  };
};
```

## 📐 **Trigonometric Functions**

### sin / cos / tan

**Purpose**: Calculate trigonometric functions (input in radians).

**Examples:**

```javascript
// Sine function
parent_value: 0
// sin output: 0

parent_value: 1.5707963267948966  // π/2
// sin output: 1

// Cosine function
parent_value: 0
// cos output: 1

parent_value: 3.141592653589793  // π
// cos output: -1

// Tangent function
parent_value: 0
// tan output: 0

parent_value: 0.7853981633974483  // π/4
// tan output: 1
```

### asin / acos / atan

**Purpose**: Calculate inverse trigonometric functions (output in radians).

**Examples:**

```javascript
// Arc sine
parent_value: 0
// asin output: 0

parent_value: 1
// asin output: 1.5707963267948966

// Arc cosine
parent_value: 1
// acos output: 0

parent_value: 0
// acos output: 1.5707963267948966

// Arc tangent
parent_value: 0
// atan output: 0

parent_value: 1
// atan output: 0.7853981633974483
```

**🔗 Geometric and Physics Applications:**

```javascript
// WeWeb: Calculate angles and rotations
const calculateObjectRotation = (startPoint, endPoint) => {
  const deltaX = endPoint.x.subtract(startPoint.x);
  const deltaY = endPoint.y.subtract(startPoint.y);
  
  const angle = deltaY.divide(deltaX).atan();
  const distance = deltaX.pow(2).add(deltaY.pow(2)).sqrt();
  
  return {
    angle_radians: angle,
    angle_degrees: angle.rad2deg(),
    distance: distance,
    velocity_x: distance.multiply(angle.cos()),
    velocity_y: distance.multiply(angle.sin())
  };
};
```

### deg2rad / rad2deg

**Purpose**: Convert between degrees and radians.

**Examples:**

```javascript
// Degrees to radians
parent_value: 0
// deg2rad output: 0

parent_value: 90
// deg2rad output: 1.5707963267948966

parent_value: 180
// deg2rad output: 3.141592653589793

// Radians to degrees
parent_value: 0
// rad2deg output: 0

parent_value: 1.5707963267948966
// rad2deg output: 90

parent_value: 3.141592653589793
// rad2deg output: 180
```

## 📈 **Logarithmic and Exponential Functions**

### ln / log / log10

**Purpose**: Calculate natural logarithm, custom base logarithm, and base-10 logarithm.

**Examples:**

```javascript
// Natural logarithm
parent_value: 1
// ln output: 0

parent_value: 2.718
// ln output: 0.9998141515394643

// Custom base logarithm
parent_value: 100
base: 10
// log output: 2

parent_value: 8
base: 2
// log output: 3

// Base-10 logarithm
parent_value: 1
// log10 output: 0

parent_value: 100
// log10 output: 2
```

### exp

**Purpose**: Calculate e raised to the power of the input.

**Examples:**

```javascript
// e^0
parent_value: 0
// Output: 1

// e^1 (approximately)
parent_value: 1
// Output: 2.718281828459045

// e^2
parent_value: 2
// Output: 7.3890560989306495
```

**🔗 Growth and Decay Calculations:**

```javascript
// Make.com: Financial growth modeling
const calculateCompoundGrowth = (principal, rate, time, compounds) => {
  // A = P(1 + r/n)^(nt)
  const ratePerPeriod = rate.divide(compounds);
  const totalPeriods = time.multiply(compounds);
  const growthFactor = ratePerPeriod.add(1).pow(totalPeriods);
  
  return {
    initial_amount: principal,
    final_amount: principal.multiply(growthFactor),
    total_growth: principal.multiply(growthFactor).subtract(principal),
    growth_rate: growthFactor.subtract(1).multiply(100)
  };
};

// Exponential decay (half-life calculations)
const calculateDecay = (initialAmount, decayConstant, time) => {
  const decayFactor = decayConstant.multiply(time).multiply(-1).exp();
  return {
    remaining_amount: initialAmount.multiply(decayFactor),
    decayed_amount: initialAmount.multiply(decayFactor.subtract(1).abs()),
    half_life: 0.693.divide(decayConstant)
  };
};
```

## 🔧 **Bitwise Operations**

### bitwise_and / bitwise_or / bitwise_xor

**Purpose**: Perform bitwise operations on integers.

**Examples:**

```javascript
// Bitwise AND
parent_value: 5  // Binary: 101
value: 3         // Binary: 011
// Output: 1       // Binary: 001

// Bitwise OR
parent_value: 5  // Binary: 101
value: 3         // Binary: 011
// Output: 7       // Binary: 111

// Bitwise XOR
parent_value: 5  // Binary: 101
value: 3         // Binary: 011
// Output: 6       // Binary: 110
```

**🔗 Flag and Permission Systems:**

```javascript
// n8n: Implement permission system
const PERMISSIONS = {
  READ: 1,    // 001
  WRITE: 2,   // 010
  EXECUTE: 4  // 100
};

const checkPermission = (userPermissions, requiredPermission) => {
  return userPermissions.bitwise_and(requiredPermission) === requiredPermission;
};

const grantPermission = (userPermissions, newPermission) => {
  return userPermissions.bitwise_or(newPermission);
};

const revokePermission = (userPermissions, permissionToRevoke) => {
  return userPermissions.bitwise_and(permissionToRevoke.bitwise_not());
};

const togglePermission = (userPermissions, permission) => {
  return userPermissions.bitwise_xor(permission);
};
```

## 📊 **Array Mathematical Operations**

### product

**Purpose**: Returns the product of all values in an array.

**Examples:**

```javascript
// Simple multiplication
parent_value: [2, 3, 4]
// Output: 24

// Decimal multiplication
parent_value: [1.5, 2, 3]
// Output: 9

// With zero
parent_value: [10, 0.1, 5]
// Output: 5
```

**🔗 Compound Calculations:**

```javascript
// WeWeb: Calculate compound metrics
const calculateCompoundMetrics = (data) => {
  const conversionRates = data.map(item => item.conversion_rate);
  const growthFactors = data.map(item => item.growth_factor);
  const multipliers = data.map(item => item.multiplier);
  
  return {
    compound_conversion: conversionRates.product(),
    compound_growth: growthFactors.product(),
    total_multiplier: multipliers.product(),
    geometric_mean: conversionRates.product().pow(1 / conversionRates.length)
  };
};
```

## 🎯 **Complex Mathematical Workflows**

### Financial Calculations

```javascript
// Complete financial analysis
const performFinancialAnalysis = (cashFlows, discountRate, periods) => {
  // Net Present Value calculation
  const npv = cashFlows.reduce((total, cashFlow, index) => {
    const discountFactor = discountRate.add(1).pow(index.add(1));
    const presentValue = cashFlow.divide(discountFactor);
    return total.add(presentValue);
  }, 0);
  
  // Internal Rate of Return (iterative approximation)
  let irr = 0.1; // Initial guess
  for (let i = 0; i < 100; i++) {
    const npvAtRate = cashFlows.reduce((total, cashFlow, index) => {
      const discountFactor = irr.add(1).pow(index.add(1));
      return total.add(cashFlow.divide(discountFactor));
    }, 0);
    
    if (npvAtRate.abs() < 0.01) break;
    irr = irr.subtract(npvAtRate.divide(1000)); // Simple adjustment
  }
  
  return {
    net_present_value: npv,
    internal_rate_of_return: irr,
    payback_period: calculatePaybackPeriod(cashFlows),
    profitability_index: npv.divide(cashFlows[0].abs()).add(1)
  };
};
```

### Statistical Analysis

```javascript
// Comprehensive statistics calculation
const calculateStatistics = (dataset) => {
  const sortedData = dataset.sort((a, b) => a - b);
  const n = dataset.length;
  
  // Basic statistics
  const mean = dataset.avg();
  const median = n.modulus(2) === 0 
    ? sortedData[n.divide(2).subtract(1)].add(sortedData[n.divide(2)]).divide(2)
    : sortedData[n.divide(2).floor()];
    
  // Variance and standard deviation
  const variance = dataset.reduce((sum, value) => {
    const deviation = value.subtract(mean);
    return sum.add(deviation.pow(2));
  }, 0).divide(n);
  
  const standardDeviation = variance.sqrt();
  
  // Quartiles
  const q1Index = n.multiply(0.25).floor();
  const q3Index = n.multiply(0.75).floor();
  
  return {
    count: n,
    mean: mean,
    median: median,
    mode: calculateMode(dataset),
    range: dataset.array_max().subtract(dataset.array_min()),
    variance: variance,
    standard_deviation: standardDeviation,
    quartile_1: sortedData[q1Index],
    quartile_3: sortedData[q3Index],
    interquartile_range: sortedData[q3Index].subtract(sortedData[q1Index])
  };
};
```

### Geometric Calculations

```javascript
// Advanced geometry functions
const calculateGeometry = (shapes) => {
  const calculations = {
    // Circle calculations
    circle: (radius) => ({
      area: 3.14159.multiply(radius.pow(2)),
      circumference: 2.multiply(3.14159).multiply(radius),
      diameter: radius.multiply(2)
    }),
    
    // Rectangle calculations
    rectangle: (length, width) => ({
      area: length.multiply(width),
      perimeter: length.add(width).multiply(2),
      diagonal: length.pow(2).add(width.pow(2)).sqrt()
    }),
    
    // Triangle calculations
    triangle: (a, b, c) => {
      const s = a.add(b).add(c).divide(2); // Semi-perimeter
      const area = s.multiply(s.subtract(a)).multiply(s.subtract(b)).multiply(s.subtract(c)).sqrt();
      
      return {
        area: area,
        perimeter: a.add(b).add(c),
        is_valid: a.add(b) > c && b.add(c) > a && a.add(c) > b
      };
    }
  };
  
  return calculations;
};
```

## 💡 **Performance Optimization**

### Efficient Mathematical Operations

```javascript
// Optimize repetitive calculations
const optimizedCalculations = {
  // Pre-calculate common constants
  PI: 3.141592653589793,
  E: 2.718281828459045,
  SQRT_2: 1.4142135623730951,
  
  // Efficient power calculations
  fastPower: (base, exponent) => {
    if (exponent === 0) return 1;
    if (exponent === 1) return base;
    if (exponent === 2) return base.multiply(base);
    return base.pow(exponent);
  },
  
  // Optimized trigonometric calculations
  fastSin: (angle) => {
    // Normalize angle to [0, 2π]
    const normalizedAngle = angle.modulus(2 * optimizedCalculations.PI);
    return normalizedAngle.sin();
  },
  
  // Efficient statistical operations for large datasets
  streamingAverage: (values, currentAvg, count) => {
    return values.reduce((avg, value, index) => {
      const newCount = count.add(index).add(1);
      return avg.add(value.subtract(avg).divide(newCount));
    }, currentAvg);
  }
};
```

## 🔗 **Integration Patterns**

### n8n Mathematical Workflows

```javascript
// n8n Code node: Advanced data processing
const processAnalyticsData = (rawData) => {
  return rawData.map(record => {
    // Statistical calculations
    const metrics = {
      revenue_growth: record.current_revenue
        .subtract(record.previous_revenue)
        .divide(record.previous_revenue)
        .multiply(100),
        
      efficiency_score: record.output
        .divide(record.input)
        .multiply(100),
        
      performance_index: record.actual_value
        .divide(record.target_value)
        .multiply(100),
        
      trend_indicator: record.recent_values.length > 1
        ? record.recent_values.slice(-1)[0]
          .subtract(record.recent_values.slice(-2)[0])
          .divide(record.recent_values.slice(-2)[0])
        : 0
    };
    
    return {
      ...record,
      calculated_metrics: metrics,
      performance_grade: getPerformanceGrade(metrics.performance_index)
    };
  });
};
```

### WeWeb Mathematical Components

```javascript
// WeWeb: Dynamic calculation components
const createCalculatorComponent = (formula, inputs) => {
  const calculate = () => {
    try {
      // Parse and execute mathematical formula
      const result = formula.split(' ').reduce((acc, token, index, tokens) => {
        if (index === 0) return parseFloat(inputs[token] || token);
        
        const operator = tokens[index - 1];
        const value = parseFloat(inputs[token] || token);
        
        switch (operator) {
          case '+': return acc.add(value);
          case '-': return acc.subtract(value);
          case '*': return acc.multiply(value);
          case '/': return acc.divide(value);
          case '^': return acc.pow(value);
          default: return acc;
        }
      });
      
      return {
        result: result,
        formatted: result.round(2).number_format(2, '.', ','),
        valid: true
      };
    } catch (error) {
      return {
        result: 0,
        formatted: 'Error',
        valid: false,
        error: error.message
      };
    }
  };
  
  return calculate();
};
```

### Make.com Mathematical Scenarios

```javascript
// Make.com: Automated mathematical analysis
const performAutomatedAnalysis = (datasets) => {
  return datasets.map(dataset => {
    const analysis = {
      // Descriptive statistics
      descriptive: {
        count: dataset.values.length,
        sum: dataset.values.sum(),
        average: dataset.values.avg(),
        minimum: dataset.values.array_min(),
        maximum: dataset.values.array_max(),
        range: dataset.values.array_max().subtract(dataset.values.array_min())
      },
      
      // Growth analysis
      growth: calculateGrowthMetrics(dataset.values),
      
      // Forecasting
      forecast: generateForecast(dataset.values, 3), // 3 periods ahead
      
      // Anomaly detection
      anomalies: detectAnomalies(dataset.values),
      
      // Quality scores
      quality: {
        completeness: calculateCompleteness(dataset.values),
        consistency: calculateConsistency(dataset.values),
        accuracy: calculateAccuracy(dataset.values, dataset.expected)
      }
    };
    
    return {
      dataset_id: dataset.id,
      analysis: analysis,
      recommendations: generateRecommendations(analysis),
      confidence_score: calculateConfidenceScore(analysis)
    };
  });
};
```

## 📚 **Best Practices**

### Mathematical Precision

```javascript
// Handle floating-point precision issues
const preciseMath = {
  // Use for financial calculations
  preciseAdd: (a, b, precision = 2) => {
    return a.add(b).round(precision);
  },
  
  // Avoid division by zero
  safeDivide: (dividend, divisor, defaultValue = 0) => {
    return divisor === 0 ? defaultValue : dividend.divide(divisor);
  },
  
  // Range validation
  clamp: (value, min, max) => {
    return value.min(max).max(min);
  },
  
  // Percentage calculations
  percentage: (part, whole) => {
    return whole === 0 ? 0 : part.divide(whole).multiply(100);
  }
};
```

### Error Handling

```javascript
// Robust mathematical operations
const safeMath = {
  safeOperation: (operation, fallback = null) => {
    try {
      const result = operation();
      
      // Check for invalid results
      if (isNaN(result) || !isFinite(result)) {
        return fallback;
      }
      
      return result;
    } catch (error) {
      console.log('Mathematical operation failed:', error);
      return fallback;
    }
  },
  
  validateInput: (value, constraints = {}) => {
    const validations = {
      is_number: typeof value === 'number',
      is_finite: isFinite(value),
      is_positive: constraints.positive ? value > 0 : true,
      in_range: constraints.min !== undefined && constraints.max !== undefined
        ? value >= constraints.min && value <= constraints.max
        : true
    };
    
    return {
      valid: Object.values(validations).every(v => v),
      checks: validations,
      value: value
    };
  }
};
```

---

**Next Steps**: With all mathematical filters mastered, explore [Complete Filter Integration Patterns](filter-integration-patterns.md) to combine multiple filter types for complex data processing workflows.