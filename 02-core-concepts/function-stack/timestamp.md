---
title: "Timestamp Data Type and Functions"
description: "Master date and time handling in Xano function stacks for accurate temporal data processing and formatting"
category: function-stack
difficulty: intermediate
tags:
  - timestamp
  - datetime
  - data-types
  - formatting
  - timezone
  - calendar
related_docs:
  - data-types
  - filters
  - expressions
  - scheduling
last_updated: '2025-01-23'
---

# Timestamp Data Type and Functions

## Quick Summary
Timestamp functions in Xano handle date and time operations with precision, supporting timezone conversions, formatting, and calculations. Essential for applications requiring accurate temporal data management.

## What You'll Learn
- Working with timestamp data types
- Date and time formatting options
- Timezone handling and conversions
- Timestamp calculations and comparisons
- Best practices for temporal data
- Integration with scheduling systems

## Understanding Timestamps

### Timestamp Basics

Xano stores timestamps as UTC (Coordinated Universal Time) internally:

```javascript
// Timestamp examples
{
  "created_at": "2025-01-23T15:30:00Z",
  "updated_at": "2025-01-23T15:45:30.123Z",
  "scheduled_date": "2025-01-24T09:00:00Z",
  "expires_at": "2025-01-30T23:59:59Z"
}
```

### Timestamp Components
- **Date**: Year, month, day (YYYY-MM-DD)
- **Time**: Hour, minute, second (HH:MM:SS)
- **Milliseconds**: Optional fractional seconds
- **Timezone**: UTC offset or timezone identifier

## Core Timestamp Functions

### Creating Timestamps

**Now**: Get current timestamp
```javascript
// Current moment
now()
result: "2025-01-23T15:30:00Z"
```

**Date**: Create from date components
```javascript
// Specific date creation
date(2025, 1, 23, 15, 30, 0)
result: "2025-01-23T15:30:00Z"
```

**Parse**: Convert string to timestamp
```javascript
// Parse date string
parse("2025-01-23 15:30:00")
result: "2025-01-23T15:30:00Z"
```

### Formatting Timestamps

**Format**: Convert timestamp to string
```javascript
// Custom formatting
timestamp: "2025-01-23T15:30:00Z"
format: "Y-m-d H:i:s"
result: "2025-01-23 15:30:00"
```

**ISO Format**: Standard timestamp format
```javascript
// ISO 8601 format
timestamp: "2025-01-23T15:30:00Z"
iso_format: true
result: "2025-01-23T15:30:00.000Z"
```

**Human Readable**: User-friendly formatting
```javascript
// Readable format
timestamp: "2025-01-23T15:30:00Z"
format: "F j, Y g:i A"
result: "January 23, 2025 3:30 PM"
```

### Timestamp Calculations

**Add Time**: Add duration to timestamp
```javascript
// Add 7 days
timestamp: "2025-01-23T15:30:00Z"
add: {
  "days": 7,
  "hours": 2,
  "minutes": 30
}
result: "2025-01-30T18:00:00Z"
```

**Subtract Time**: Remove duration from timestamp
```javascript
// Subtract 1 week
timestamp: "2025-01-23T15:30:00Z"
subtract: {
  "weeks": 1
}
result: "2025-01-16T15:30:00Z"
```

**Difference**: Calculate time between timestamps
```javascript
// Time difference
start: "2025-01-23T15:30:00Z"
end: "2025-01-25T18:45:30Z"
difference: "hours"
result: 51.25
```

## Timezone Operations

### Timezone Conversion

```javascript
// Convert timezone
timestamp: "2025-01-23T15:30:00Z"
from_timezone: "UTC"
to_timezone: "America/New_York"
result: "2025-01-23T10:30:00-05:00"
```

### Common Timezone Examples

```javascript
// Global timezone conversions
{
  "UTC": "2025-01-23T15:30:00Z",
  "Eastern": "2025-01-23T10:30:00-05:00",
  "Pacific": "2025-01-23T07:30:00-08:00",
  "London": "2025-01-23T15:30:00+00:00",
  "Tokyo": "2025-01-24T00:30:00+09:00"
}
```

## Integration Patterns

### For n8n Users
Date/time workflow automation:

```javascript
// n8n datetime processing
{
  "current_time": "{{$now}}",
  "formatted_date": "{{$now.format('YYYY-MM-DD')}}",
  "next_week": "{{$now.plus({days: 7}).toISO()}}",
  "business_hours": {
    "start": "{{$now.set({hour: 9, minute: 0, second: 0})}}",
    "end": "{{$now.set({hour: 17, minute: 0, second: 0})}}"
  }
}
```

### For WeWeb Users
Dynamic date display and calculations:

```javascript
// WeWeb date binding
{
  "display_date": "{{created_at.toLocaleDateString()}}",
  "time_ago": "{{formatDistanceToNow(created_at)}}",
  "is_recent": "{{differenceInDays(now, created_at) < 7}}",
  "formatted_time": "{{format(created_at, 'MMM dd, yyyy HH:mm')}}"
}
```

### API Response Formatting

```json
{
  "event": {
    "id": 123,
    "title": "Team Meeting",
    "start_time": "2025-01-24T09:00:00Z",
    "end_time": "2025-01-24T10:00:00Z",
    "duration_minutes": 60,
    "formatted_date": "January 24, 2025",
    "formatted_time": "9:00 AM UTC",
    "timezone": "UTC",
    "created_at": "2025-01-23T15:30:00Z",
    "updated_at": "2025-01-23T15:30:00Z"
  }
}
```

## Common Use Cases

### Event Scheduling

```javascript
// Meeting scheduler
1. Parse user input date/time
2. Convert to UTC for storage
3. Calculate duration
4. Check for conflicts
5. Send calendar invitations
```

### Content Management

```javascript
// Blog post workflow
1. Set publication timestamp
2. Calculate reading time
3. Format display date
4. Handle scheduled publishing
5. Track modification dates
```

### Data Analytics

```javascript
// Time-based analytics
1. Group events by time periods
2. Calculate average response times
3. Identify peak usage hours
4. Generate time-series reports
5. Compare period-over-period metrics
```

## Try This
1. **Basic Operations**: Practice creating and formatting timestamps
2. **Timezone Handling**: Convert between different timezones
3. **Calculations**: Add/subtract time and calculate differences
4. **Scheduling Logic**: Build event scheduling functionality
5. **Analytics**: Create time-based data aggregations

## Common Mistakes to Avoid

❌ **Don't:**
- Store timestamps in local timezone
- Ignore daylight saving time changes
- Use inconsistent date formats
- Forget to validate date inputs
- Mix different timezone representations

✅ **Do:**
- Always store timestamps in UTC
- Convert to local timezone for display
- Use consistent formatting patterns
- Validate date ranges and formats
- Handle timezone changes properly

## Pro Tips

💡 **Storage Best Practices:**
- Store all timestamps in UTC
- Convert to user timezone for display
- Use ISO 8601 format for APIs
- Include timezone info when needed

🚀 **Performance Optimization:**
- Cache timezone conversion results
- Use database indexes on timestamp fields
- Batch timestamp operations
- Pre-calculate common date ranges

⚡ **User Experience:**
- Show relative times ("2 hours ago")
- Display in user's local timezone
- Provide multiple format options
- Handle invalid dates gracefully

## Advanced Techniques

### Business Hours Calculation

```javascript
// Check business hours
function isBusinessHours(timestamp, timezone) {
  const local = convertTimezone(timestamp, timezone);
  const hour = extractHour(local);
  const day = extractDayOfWeek(local);
  
  return day >= 1 && day <= 5 && hour >= 9 && hour <= 17;
}
```

### Recurring Events

```javascript
// Generate recurring dates
function generateRecurring(start, pattern, count) {
  const dates = [];
  for (let i = 0; i < count; i++) {
    const date = addTime(start, {
      [pattern.unit]: pattern.interval * i
    });
    dates.push(date);
  }
  return dates;
}
```

### Time Zone Detection

```javascript
// Auto-detect user timezone
function getUserTimezone() {
  // From user agent or IP geolocation
  return detectTimezone() || "UTC";
}
```

## Date Format Reference

### Common Patterns

```javascript
// Format examples
{
  "Y-m-d": "2025-01-23",
  "d/m/Y": "23/01/2025",
  "F j, Y": "January 23, 2025",
  "H:i:s": "15:30:00",
  "g:i A": "3:30 PM",
  "c": "2025-01-23T15:30:00+00:00",
  "r": "Thu, 23 Jan 2025 15:30:00 +0000"
}
```

### Relative Formatting

```javascript
// Relative time examples
{
  "now": "just now",
  "1 minute ago": "1 minute ago",
  "1 hour ago": "1 hour ago",
  "yesterday": "yesterday",
  "last week": "last week",
  "2 months ago": "2 months ago"
}
```

## Performance Considerations

### Timestamp Processing
- Use database functions for complex date calculations
- Cache frequently used timezone conversions
- Index timestamp fields for fast queries
- Batch timestamp operations when possible

### Memory Management
- Avoid creating unnecessary timestamp objects
- Use efficient date libraries
- Cache formatted date strings
- Clean up temporary date calculations

Proper timestamp handling ensures your applications work accurately across different timezones and provide excellent user experiences with temporal data.