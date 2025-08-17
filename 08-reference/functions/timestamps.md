---
title: Timestamp Data Type Reference
description: Complete guide to working with timestamps in Xano - handle dates, times, and timezone operations for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- timestamp
- data-types
- datetime
- timezone
- unix-time
- date-formatting
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 08-reference/filters/format__timestamp.md
- 02-core-concepts/function-stack/data-types.md
- expressions/configuring-expressions.md
---

# Timestamp Data Type Reference

## 📋 **Quick Summary**
Timestamps in Xano store dates and times as Unix timestamps in milliseconds. Essential for tracking events, scheduling, user activity, and time-based logic in no-code platforms like n8n, WeWeb, and Make.com.

## What You'll Learn
- Understanding Unix timestamps and milliseconds
- Timezone handling and conversions
- Timestamp input and output formats
- Integration patterns for no-code platforms
- Date/time manipulation techniques
- Common timestamp use cases

## Understanding Timestamps

Xano stores timestamps as **Unix timestamps in milliseconds**:
### Unix Timestamp Format

**Raw Timestamp (Milliseconds):**
```javascript
1604959474000  // November 9, 2020 @ 10:04pm UTC
```

**Key Concepts:**
- Unix epoch starts January 1, 1970 at UTC
- Xano uses **milliseconds** (not seconds)
- No timezone info in raw timestamp
- Always stored as UTC internally

## 🔄 **No-Code Platform Integration**

### n8n Integration
```javascript
// In n8n Set node - timestamp operations
{
  "current_timestamp": "{{Date.now()}}",
  "formatted_date": "{{new Date().toISOString()}}",
  "days_ago_7": "{{Date.now() - (7 * 24 * 60 * 60 * 1000)}}",
  "readable_time": "{{new Date($json.timestamp).toLocaleString()}}"
}
```

### WeWeb Integration
```javascript
// WeWeb formula for date formatting
new Date(timestamp).toLocaleDateString()
// Time calculations
Math.floor((Date.now() - created_at) / (1000 * 60 * 60 * 24)) // Days ago
```

### Make.com Integration
```javascript
// Make.com date functions
{
  "timestamp": "{{timestamp}}",
  "formatted": "{{formatDate(timestamp; 'YYYY-MM-DD HH:mm:ss')}}",
  "add_days": "{{addDays(timestamp; 7)}}"
}
```

## Timestamp Input Formats

### 1. Raw Timestamp (Recommended)
```javascript
1604959474000  // Milliseconds since Unix epoch
```

### 2. ISO 8601 Format
```javascript
"2004-02-12T15:19:21+00:00"  // Standard format with timezone
"2025-01-17T14:30:00Z"       // UTC time (Z = UTC)
```

### 3. Postgres Format
```javascript
"2020-11-09 14:13:18-0800"   // Space instead of T, no colon in offset
```

### 4. Relative Time
```javascript
"now"          // Current time
"last Monday"  // Previous Monday
"+7 days"      // 7 days from now
"-1 hour"      // 1 hour ago
"next week"    // Following week
```

## 💡 **Try This: Event Management System**

Create a comprehensive timestamp-based system:

```javascript
{
  "event": {
    "id": 123,
    "title": "Product Launch Webinar",
    "start_time": 1705507200000,      // 2025-01-17 14:00:00 UTC
    "end_time": 1705510800000,        // 2025-01-17 15:00:00 UTC
    "timezone": "America/New_York",
    "created_at": 1705420800000,      // When event was created
    "updated_at": 1705507000000       // Last modification
  },
  "registration": {
    "user_id": 456,
    "registered_at": 1705421400000,   // Registration timestamp
    "reminder_sent_at": null,         // When reminder was sent
    "attended_at": null              // When user joined
  },
  "computed_fields": {
    "days_until_event": 7,
    "registration_open": true,
    "event_status": "upcoming",
    "time_remaining": "6 days, 14 hours"
  }
}
```

## Timezone Handling

### Timezone Types

**1. Timezone Region (Recommended):**
```javascript
"America/New_York"     // Handles DST automatically
"Europe/London"        // GMT/BST switching
"Asia/Tokyo"           // No DST
"UTC"                  // Universal time
```

**2. Timezone Abbreviation:**
```javascript
"PST"  // Pacific Standard Time (-08:00)
"PDT"  // Pacific Daylight Time (-07:00)
"EST"  // Eastern Standard Time (-05:00)
"GMT"  // Greenwich Mean Time (+00:00)
```

**3. Timezone Offset:**
```javascript
"+00:00"  // UTC
"-05:00"  // Eastern Time
"-08:00"  // Pacific Time
"+09:00"  // Japan Time
```

### Best Practices
- Use timezone regions for automatic DST handling
- Store all timestamps in UTC
- Convert to local time for display only
- Always specify timezone when parsing user input

## Common Timestamp Operations

### Current Time
```javascript
// Get current timestamp
now()  // Returns current Unix timestamp in milliseconds
```

### Date Arithmetic
```javascript
// Add time
now() + (7 * 24 * 60 * 60 * 1000)  // Add 7 days
now() + (2 * 60 * 60 * 1000)       // Add 2 hours

// Subtract time
now() - (30 * 24 * 60 * 60 * 1000) // 30 days ago
```

### Format for Display
```javascript
// Format timestamp for display
format_timestamp(timestamp, "Y-m-d H:i:s", "America/New_York")
// Result: "2025-01-17 09:00:00"

format_timestamp(timestamp, "M j, Y g:i A", "UTC")
// Result: "Jan 17, 2025 2:00 PM"
```

## ⚠️ **Common Mistakes to Avoid**

1. **Seconds vs Milliseconds**: Xano uses milliseconds, not seconds
2. **Timezone Confusion**: Always specify timezone when needed
3. **DST Issues**: Use timezone regions instead of fixed offsets
4. **Browser Timezone**: Database viewer shows times in browser timezone

## 🚀 **Pro Tips**

### Database Configuration
```javascript
// Timestamp field setup
{
  "field_name": "created_at",
  "field_type": "timestamp",
  "default_value": "now()",
  "auto_update": false
}

// Auto-updating timestamp
{
  "field_name": "updated_at",
  "field_type": "timestamp",
  "auto_update": true  // Updates on record modification
}
```

### Timestamp Validation
```javascript
// Validate timestamp range
function isValidTimestamp(ts) {
  const now = Date.now();
  const oneYearAgo = now - (365 * 24 * 60 * 60 * 1000);
  const oneYearFromNow = now + (365 * 24 * 60 * 60 * 1000);
  return ts >= oneYearAgo && ts <= oneYearFromNow;
}
```

### Time-based Queries
```javascript
// Find records from last 7 days
WHERE created_at >= {{now() - (7 * 24 * 60 * 60 * 1000)}}

// Find records for today (in specific timezone)
WHERE DATE(created_at, 'America/New_York') = CURDATE()

// Find upcoming events
WHERE start_time > {{now()}} AND start_time < {{now() + (30 * 24 * 60 * 60 * 1000)}}
```

## Integration Best Practices

### For n8n Workflows
- Use Date.now() for current timestamps
- Convert to ISO strings for external APIs
- Handle timezone conversions in Set nodes

### For WeWeb Apps
- Display timestamps in user's local timezone
- Use computed properties for relative time displays
- Format dates consistently across components

### For Make.com Scenarios
- Use formatDate() for consistent formatting
- Handle different timezone inputs gracefully
- Implement proper date arithmetic functions

## Common Format Patterns

### Display Formats
```javascript
// Common timestamp formats
"Y-m-d H:i:s"           // 2025-01-17 14:30:00
"M j, Y g:i A"           // Jan 17, 2025 2:30 PM
"l, F j, Y"             // Friday, January 17, 2025
"c"                     // 2025-01-17T14:30:00+00:00 (ISO 8601)
"r"                     // Fri, 17 Jan 2025 14:30:00 +0000 (RFC 2822)
```

### API Response Patterns
```javascript
// Clean timestamp API response
{
  "success": true,
  "data": {
    "event": {
      "id": 123,
      "start_time": 1705507200000,
      "start_time_iso": "2025-01-17T14:00:00Z",
      "start_time_local": "2025-01-17 09:00:00",
      "timezone": "America/New_York"
    }
  },
  "meta": {
    "server_time": 1705420800000,
    "timezone": "UTC"
  }
}
```

## Related Functions
- [Timestamp Filters](../filters/format__timestamp.md) - Formatting and manipulation
- [Data Types](../../02-core-concepts/function-stack/data-types.md) - Understanding data types
- [Configuring Expressions](../../05-advanced-features/expressions/configuring-expressions.md) - Using timestamps in expressions

Timestamps are essential for time-sensitive applications in Xano. Master these patterns to build reliable scheduling, tracking, and time-based logic that works seamlessly with your no-code platforms.