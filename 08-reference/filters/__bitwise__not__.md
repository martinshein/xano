---
title: Bitwise and Math Filters Reference - Complete Guide for No-Code Development
description: Master Xano's bitwise operations and mathematical filters including bitwise_not, comparisons, even/odd checks, and mathematical calculations for advanced data processing in n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: advanced
last_updated: '2025-01-16'
related_docs:
  - math-filters.md
  - conversion-filters.md
  - comparison-filters.md
tags:
  - bitwise-operations
  - mathematical-filters
  - comparison
  - even-odd
  - binary-operations
  - numeric-processing
---

## 📋 **Quick Summary**

Master Xano's bitwise operations and mathematical filters for advanced numeric processing. This reference covers bitwise manipulations, comparison operations, even/odd checks, and mathematical calculations perfect for system-level programming, data analysis, and complex logic implementation in n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Complete bitwise operations reference
- Mathematical comparison filters
- Even/odd number validation
- Binary data manipulation techniques
- Performance optimization for numeric operations
- Integration patterns for complex calculations

# Bitwise and Math Filters Reference

## 🔢 **Bitwise Operations**

### bitwise_not

**Purpose**: Returns the existing value with its bits flipped (bitwise NOT operation).

**How It Works**: Performs a bitwise NOT operation, flipping all bits in the binary representation of a number. In most systems, this is equivalent to `-(n + 1)` due to two's complement representation.

**Examples:**

**Basic Bitwise NOT:**
```javascript
// Input
parent_value: 5

// Binary representation: 00000101
// After bitwise_not:     11111010
// Output: -6 (in two's complement)
```

**Understanding the Operation:**
```javascript
// Positive numbers
parent_value: 0
// Binary: 00000000
// Result: 11111111 = -1

parent_value: 1  
// Binary: 00000001
// Result: 11111110 = -2

parent_value: 7
// Binary: 00000111  
// Result: 11111000 = -8
```

**🔗 Real-World Use Cases:**

**Permission Systems:**
```javascript
// Toggle all permission bits
const allPermissions = 255;  // 11111111
const noPermissions = allPermissions.bitwise_not(); // 00000000 = -256

// Flip specific flags
const currentPermissions = 85;  // 01010101
const flippedPermissions = currentPermissions.bitwise_not(); // 10101010
```

**Color Manipulation:**
```javascript
// Invert color values (for dark/light mode)
const redValue = 255;
const invertedRed = redValue.bitwise_not(); // Creates complementary color

// WeWeb: Dynamic theme switching
const invertThemeColor = (colorValue) => {
  return (colorValue & 0xFF).bitwise_not() & 0xFF; // Keep within byte range
};
```

**Data Masking:**
```javascript
// n8n: Simple data obfuscation
const dataValue = 42;
const maskedValue = dataValue.bitwise_not();
// To unmask: maskedValue.bitwise_not() returns original 42
```

## 🔍 **Comparison Operations**

### equals

**Purpose**: Returns a boolean indicating whether two values are equal.

**Examples:**

**Basic Equality:**
```javascript
// Input
parent_value: 7
comparison_value: 7

// Output
true

// Different values
parent_value: 5
comparison_value: 7

// Output
false
```

**Type-Aware Comparisons:**
```javascript
// String vs Number
parent_value: "123"
comparison_value: 123

// Output
false  // Different types

// Boolean comparisons
parent_value: true
comparison_value: 1

// Output
false  // Different types
```

**🔗 Integration Examples:**

**Conditional Logic in n8n:**
```javascript
// n8n: Route data based on equality
const userRole = userData.role;
const isAdmin = userRole.equals("administrator");

if (isAdmin) {
  // Route to admin workflow
} else {
  // Route to standard user workflow
}
```

**WeWeb Form Validation:**
```javascript
// WeWeb: Password confirmation
const password = formData.password;
const confirmPassword = formData.confirm_password;
const passwordsMatch = password.equals(confirmPassword);

if (!passwordsMatch) {
  showError("Passwords do not match");
}
```

**Make.com Data Filtering:**
```javascript
// Make.com: Filter records by status
const records = getAllRecords();
const activeRecords = records.filter(record => 
  record.status.equals("active")
);
```

## ✅ **Even/Odd Validation**

### even

**Purpose**: Returns whether the value is even (divisible by 2).

**Examples:**
```javascript
// Even number
parent_value: 24

// Output
true

// Odd number  
parent_value: 23

// Output
false

// Zero is even
parent_value: 0

// Output
true

// Negative even number
parent_value: -8

// Output
true
```

### odd

**Purpose**: Returns whether the value is odd (not divisible by 2).

**Examples:**
```javascript
// Odd number
parent_value: 23

// Output
true

// Even number
parent_value: 24

// Output
false

// Negative odd number
parent_value: -7

// Output
true
```

**🔗 Practical Applications:**

**Data Processing Patterns:**
```javascript
// n8n: Process records in alternating patterns
const recordIndex = currentRecord.index;
const shouldProcessNow = recordIndex.odd();

if (shouldProcessNow) {
  // Process odd-indexed records immediately
  processRecord(currentRecord);
} else {
  // Queue even-indexed records for batch processing
  queueRecord(currentRecord);
}
```

**UI Layout Logic:**
```javascript
// WeWeb: Alternating row colors in tables
const rowIndex = item.index;
const isAlternateRow = rowIndex.even();
const rowClass = isAlternateRow ? 'bg-gray-100' : 'bg-white';
```

**Load Balancing:**
```javascript
// Make.com: Distribute workload between servers
const taskId = task.id;
const useServerA = taskId.even();
const targetServer = useServerA ? 'server-a' : 'server-b';

// Route task to appropriate server
routeToServer(task, targetServer);
```

## 🧮 **Advanced Mathematical Operations**

### Mathematical Validation Patterns

**Range Validation:**
```javascript
// Check if number is within bounds
const validateRange = (value, min, max) => {
  const isAboveMin = value >= min;
  const isBelowMax = value <= max;
  return isAboveMin && isBelowMax;
};

// Usage in WeWeb form validation
const age = formInput.age.to_int();
const isValidAge = validateRange(age, 0, 150);
```

**Divisibility Checks:**
```javascript
// Check if divisible by specific number
const isDivisibleBy = (value, divisor) => {
  return (value % divisor).equals(0);
};

// n8n: Batch processing every 10th record
const recordNumber = record.id;
const shouldCreateBatch = isDivisibleBy(recordNumber, 10);
```

### Number Classification

**Perfect Number Detection:**
```javascript
// Check if number equals sum of its proper divisors
const isPerfectNumber = (n) => {
  let sum = 1; // 1 is always a proper divisor
  for (let i = 2; i * i <= n; i++) {
    if (isDivisibleBy(n, i)) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
  }
  return sum.equals(n);
};

// Usage: isPerfectNumber(28) returns true (1+2+4+7+14=28)
```

**Prime Number Checking:**
```javascript
// Basic prime number validation
const isPrime = (n) => {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n.even() || isDivisibleBy(n, 3)) return false;
  
  for (let i = 5; i * i <= n; i += 6) {
    if (isDivisibleBy(n, i) || isDivisibleBy(n, i + 2)) {
      return false;
    }
  }
  return true;
};
```

## 🔐 **Security and Encryption Applications**

### Simple Hash Generation

**Using Bitwise Operations for Hashing:**
```javascript
// Simple hash function using bitwise operations
const simpleHash = (input) => {
  let hash = 0;
  const str = input.to_text();
  
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash; // Convert to 32-bit integer
  }
  
  return Math.abs(hash);
};

// n8n: Generate simple checksums
const dataChecksum = simpleHash(webhookData);
```

### Data Integrity Checks

**Parity Bit Calculation:**
```javascript
// Calculate parity bit for error detection
const calculateParity = (value) => {
  let count = 0;
  let temp = value;
  
  while (temp > 0) {
    if (temp.odd()) count++;
    temp = Math.floor(temp / 2);
  }
  
  return count.odd(); // Odd parity
};

// Usage in data transmission validation
const dataIntegrityCheck = (data) => {
  const expectedParity = calculateParity(data);
  const receivedParity = extractParityBit(data);
  return expectedParity.equals(receivedParity);
};
```

## 🔄 **Bit Manipulation Patterns**

### Flag Management

**Permission Flags:**
```javascript
// Define permission constants
const PERMISSIONS = {
  READ: 1,     // 00000001
  WRITE: 2,    // 00000010  
  EXECUTE: 4,  // 00000100
  DELETE: 8    // 00001000
};

// Check if user has specific permission
const hasPermission = (userPermissions, permission) => {
  return (userPermissions & permission) !== 0;
};

// Grant permission
const grantPermission = (userPermissions, permission) => {
  return userPermissions | permission;
};

// Revoke permission  
const revokePermission = (userPermissions, permission) => {
  return userPermissions & permission.bitwise_not();
};

// WeWeb: Dynamic UI based on permissions
const canEdit = hasPermission(currentUser.permissions, PERMISSIONS.WRITE);
const showEditButton = canEdit;
```

### Status Tracking

**Multi-State Flags:**
```javascript
// Feature flags using bitwise operations
const FEATURES = {
  DARK_MODE: 1,
  NOTIFICATIONS: 2,
  ANALYTICS: 4,
  BETA_FEATURES: 8
};

// Check if feature is enabled
const isFeatureEnabled = (settings, feature) => {
  return (settings & feature) !== 0;
};

// Toggle feature
const toggleFeature = (settings, feature) => {
  return settings ^ feature; // XOR to toggle
};

// Make.com: Feature rollout management
const userSettings = user.feature_flags;
const showBetaFeatures = isFeatureEnabled(userSettings, FEATURES.BETA_FEATURES);
```

## 📊 **Performance Optimization**

### Efficient Calculations

**Fast Even/Odd Detection:**
```javascript
// More efficient than modulo operation
const isFastEven = (n) => {
  return (n & 1).equals(0);
};

const isFastOdd = (n) => {
  return (n & 1).equals(1);
};

// Use in high-performance loops
const processLargeDataset = (data) => {
  return data.map((item, index) => {
    const useOptimizedPath = isFastEven(index);
    return useOptimizedPath ? optimizedProcess(item) : standardProcess(item);
  });
};
```

**Power of 2 Detection:**
```javascript
// Check if number is power of 2
const isPowerOfTwo = (n) => {
  return n > 0 && (n & (n - 1)).equals(0);
};

// Usage in buffer size validation
const isValidBufferSize = (size) => {
  return isPowerOfTwo(size) && size >= 1024;
};
```

## 🔗 **Integration Patterns**

### n8n Workflow Examples

**Conditional Processing:**
```javascript
// n8n Code node: Route based on numeric properties
const items = $input.all();

const processedItems = items.map(item => {
  const id = item.json.id;
  const isEven = id.even();
  
  return {
    ...item.json,
    processing_queue: isEven ? 'queue_a' : 'queue_b',
    priority: isEven ? 'normal' : 'high'
  };
});

return processedItems;
```

**Data Validation Pipeline:**
```javascript
// Validate numeric data in webhooks
const validateNumericData = (data) => {
  const validations = {
    is_positive: data > 0,
    is_even: data.even(),
    is_within_range: data >= 1 && data <= 1000,
    equals_expected: data.equals(expectedValue)
  };
  
  const isValid = Object.values(validations).every(v => v);
  
  return {
    data: data,
    valid: isValid,
    validations: validations
  };
};
```

### WeWeb Component Integration

**Dynamic Styling:**
```javascript
// WeWeb: Apply styles based on numeric properties
const getRowStyling = (index) => {
  const isAlternate = index.even();
  const isSpecial = (index % 5).equals(0);
  
  return {
    backgroundColor: isAlternate ? '#f9f9f9' : '#ffffff',
    fontWeight: isSpecial ? 'bold' : 'normal',
    border: isSpecial ? '2px solid #007bff' : '1px solid #ddd'
  };
};
```

**Form Logic:**
```javascript
// WeWeb: Conditional form behavior
const updateFormLogic = (step) => {
  const isEvenStep = step.even();
  const isLastStep = step.equals(totalSteps);
  
  return {
    showProgressBar: !isLastStep,
    allowSkip: isEvenStep,
    requireValidation: isEvenStep,
    nextButtonText: isLastStep ? 'Submit' : 'Next'
  };
};
```

### Make.com Scenario Patterns

**Load Distribution:**
```javascript
// Make.com: Distribute workload evenly
const distributeWork = (tasks) => {
  const servers = ['server-1', 'server-2', 'server-3', 'server-4'];
  
  return tasks.map(task => {
    const serverIndex = task.id % servers.length;
    const isHighPriority = task.id.odd();
    
    return {
      ...task,
      assigned_server: servers[serverIndex],
      priority: isHighPriority ? 'high' : 'normal',
      processing_order: task.id.even() ? 'immediate' : 'queued'
    };
  });
};
```

## 💡 **Best Practices**

### Performance Considerations

**Bitwise vs. Arithmetic Operations:**
```javascript
// Faster bitwise operations for common tasks
const multiplyByTwo = (n) => n << 1;      // Instead of n * 2
const divideByTwo = (n) => n >> 1;        // Instead of n / 2  
const isEven = (n) => (n & 1) === 0;      // Instead of n % 2 === 0
const isPowerOfTwo = (n) => n > 0 && (n & (n - 1)) === 0;
```

**Memory Efficient Flag Storage:**
```javascript
// Store multiple boolean flags in single integer
class FlagManager {
  constructor() {
    this.flags = 0;
  }
  
  setFlag(position, value) {
    if (value) {
      this.flags |= (1 << position);
    } else {
      this.flags &= ~(1 << position);
    }
  }
  
  getFlag(position) {
    return (this.flags & (1 << position)) !== 0;
  }
  
  toggleFlag(position) {
    this.flags ^= (1 << position);
  }
}
```

### Error Handling

**Safe Numeric Operations:**
```javascript
// Handle edge cases in numeric operations
const safeEquals = (a, b) => {
  // Handle null/undefined
  if (a === null || a === undefined || b === null || b === undefined) {
    return a === b;
  }
  
  // Handle NaN
  if (isNaN(a) || isNaN(b)) {
    return isNaN(a) && isNaN(b);
  }
  
  return a.equals(b);
};

const safeEven = (n) => {
  if (typeof n !== 'number' || isNaN(n)) {
    return false;
  }
  return n.even();
};
```

### Data Validation

**Comprehensive Numeric Validation:**
```javascript
// Validate numeric input before operations
const validateNumericInput = (value) => {
  const validations = {
    is_number: typeof value === 'number',
    is_finite: isFinite(value),
    is_integer: Number.isInteger(value),
    is_positive: value > 0,
    is_safe_integer: Number.isSafeInteger(value)
  };
  
  return {
    valid: Object.values(validations).every(v => v),
    checks: validations,
    value: value
  };
};
```

## 🎯 **Common Patterns**

### Cyclic Operations

```javascript
// Implement cyclic behavior using modulo and even/odd
const getCycleState = (iteration, cycleLength) => {
  const position = iteration % cycleLength;
  const isEvenCycle = Math.floor(iteration / cycleLength).even();
  
  return {
    position: position,
    reverse: isEvenCycle,
    phase: isEvenCycle ? 'forward' : 'backward'
  };
};

// Usage in animations or data processing
const animationFrame = getCurrentFrame();
const cycleState = getCycleState(animationFrame, 60);
```

### State Machine Implementation

```javascript
// Simple state machine using numeric states
class SimpleStateMachine {
  constructor(initialState = 0) {
    this.state = initialState;
  }
  
  transition(input) {
    const isEvenState = this.state.even();
    const isEvenInput = input.even();
    
    if (isEvenState && isEvenInput) {
      this.state++;
    } else if (!isEvenState && !isEvenInput) {
      this.state--;
    } else {
      this.state = this.state.bitwise_not() & 0xFF; // Keep in range
    }
    
    return this.state;
  }
  
  isStableState() {
    return this.state.even() && this.state > 0;
  }
}
```

---

**Next Steps**: Explore more filter types in [Mathematical Operations](math-filters.md) and [Text Processing](text-filters.md) to complete your data manipulation toolkit.