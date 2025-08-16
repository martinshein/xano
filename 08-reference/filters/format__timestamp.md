---
title: Timestamp Filters Reference - Complete Guide for No-Code Development
description: Master Xano's comprehensive timestamp filter library including format_timestamp, parse_timestamp, time calculations, and date transformations for dynamic time-based applications in n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - date-time-guide.md
  - timezone-handling.md
  - php-datetime-formats.md
tags:
  - timestamp-filters
  - date-formatting
  - time-calculations
  - timezone-conversion
  - date-parsing
  - temporal-operations
---

## 📋 **Quick Summary**

Master Xano's complete timestamp filter library for sophisticated date and time operations. This reference covers date formatting, parsing, time calculations, timezone conversions, and relative date transformations essential for building time-aware applications with n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Complete timestamp filter reference with practical examples
- Date formatting and display techniques
- Time parsing from various string formats
- Timestamp calculations and adjustments
- Timezone handling and conversions
- Relative date transformations
- Performance optimization for date operations
- Integration patterns for time-based features

# Timestamp Filters Reference

## 📅 **Date Formatting**

### format_timestamp

**Purpose**: Converts a timestamp into a human-readable formatted date using PHP DateTime format syntax.

**Parameters:**
- `parent_value`: The timestamp to format (epoch in milliseconds, UTC)
- `format`: PHP DateTime format string (e.g., `"Y-m-d H:i:s"`)
- `timezone`: Target timezone for output (e.g., `"America/New_York"`)

**Examples:**

**Basic Date Formatting:**
```javascript
// Input
parent_value: 1698710400000  // Oct 31, 2023 00:00:00 UTC
format: "Y-m-d"
timezone: "UTC"

// Output
"2023-10-31"
```

**Full Date and Time:**
```javascript
// Input
parent_value: 1698710400000
format: "M j, Y h:i A"
timezone: "America/New_York"

// Output
"Oct 30, 2023 08:00 PM"  // EDT timezone adjustment
```

**Long Format:**
```javascript
// Input
parent_value: 1698710400000
format: "l, F j, Y \\a\\t g:i A"
timezone: "UTC"

// Output
"Tuesday, October 31, 2023 at 12:00 AM"
```

**🔗 Real-World Use Cases:**

**User Interface Display:**
```javascript
// WeWeb: Display user-friendly dates
const formatUserDate = (timestamp) => {
  const userTimezone = getCurrentUserTimezone();
  
  return {
    short: timestamp.format_timestamp("M j", userTimezone),
    medium: timestamp.format_timestamp("M j, Y", userTimezone),
    long: timestamp.format_timestamp("l, F j, Y", userTimezone),
    withTime: timestamp.format_timestamp("M j, Y g:i A", userTimezone)
  };
};

// Usage in components
const postDate = formatUserDate(post.created_at);
// { short: "Oct 31", medium: "Oct 31, 2023", ... }
```

**Multi-Language Date Formatting:**
```javascript
// n8n: Internationalized date display
const formatDateByLocale = (timestamp, locale, timezone) => {
  const formats = {
    'en-US': "M j, Y g:i A",
    'en-GB': "j/n/Y H:i",
    'de-DE': "j.n.Y H:i",
    'fr-FR': "j/n/Y H\\hi",
    'ja-JP': "Y年n月j日 H:i"
  };
  
  const format = formats[locale] || formats['en-US'];
  return timestamp.format_timestamp(format, timezone);
};
```

**Data Export Formatting:**
```javascript
// Make.com: Format timestamps for CSV exports
const exportData = records.map(record => ({
  id: record.id,
  name: record.name,
  created_date: record.created_at.format_timestamp("Y-m-d", "UTC"),
  created_time: record.created_at.format_timestamp("H:i:s", "UTC"),
  created_iso: record.created_at.format_timestamp("c", "UTC")
}));
```

## 🔍 **Date Parsing**

### parse_timestamp

**Purpose**: Parses date/time strings from various formats into epoch millisecond timestamps (UTC).

**Parameters:**
- `parent_value`: The date/time string to parse
- `format`: PHP DateTime format string for parsing
- `timezone`: Source timezone for interpretation

**Examples:**

**American Date Format:**
```javascript
// Input
parent_value: "10/31/2023"
format: "m/d/Y"
timezone: "America/New_York"

// Output
1698728400000  // Converted to UTC epoch
```

**ISO Date Format:**
```javascript
// Input
parent_value: "2023-10-31 14:30:15"
format: "Y-m-d H:i:s"
timezone: "UTC"

// Output
1698762615000
```

**Natural Language Format:**
```javascript
// Input
parent_value: "October 31, 2023 2:30 PM"
format: "F j, Y g:i A"
timezone: "America/Los_Angeles"

// Output
1698781800000  // PST/PDT converted to UTC
```

**🔗 Practical Applications:**

**Form Input Processing:**
```javascript
// WeWeb: Parse user date inputs
const processDateInput = (userInput, inputFormat) => {
  const userTimezone = getCurrentUserTimezone();
  
  try {
    const timestamp = userInput.parse_timestamp(inputFormat, userTimezone);
    return {
      success: true,
      timestamp: timestamp,
      formatted: timestamp.format_timestamp("Y-m-d H:i:s", "UTC")
    };
  } catch (error) {
    return {
      success: false,
      error: "Invalid date format",
      input: userInput
    };
  }
};

// Usage
const birthday = processDateInput("03/15/1990", "m/d/Y");
```

**CSV Import Processing:**
```javascript
// n8n: Parse various date formats from imports
const parseImportDates = (csvData) => {
  const dateFormats = [
    "Y-m-d H:i:s",    // ISO format
    "m/d/Y H:i:s",    // US format with time
    "d/m/Y H:i:s",    // EU format with time
    "Y-m-d",          // Date only
    "m/d/Y",          // US date only
    "d/m/Y"           // EU date only
  ];
  
  return csvData.map(row => {
    let parsedDate = null;
    
    for (const format of dateFormats) {
      try {
        parsedDate = row.date_field.parse_timestamp(format, "UTC");
        break;
      } catch (e) {
        continue;
      }
    }
    
    return {
      ...row,
      parsed_date: parsedDate,
      valid_date: parsedDate !== null
    };
  });
};
```

**API Data Integration:**
```javascript
// Make.com: Handle multiple external API date formats
const normalizeApiDates = (apiResponse) => {
  const apiDateFormats = {
    'service_a': "Y-m-d\\TH:i:s\\Z",
    'service_b': "m/d/Y h:i A",
    'service_c': "D, d M Y H:i:s O"
  };
  
  return apiResponse.map(record => {
    const serviceType = record.source_service;
    const format = apiDateFormats[serviceType];
    
    return {
      ...record,
      normalized_date: record.date_string.parse_timestamp(format, "UTC"),
      original_date: record.date_string
    };
  });
};
```

## ⏰ **Time Calculations**

### add_ms_to_timestamp

**Purpose**: Add milliseconds to a timestamp (negative values allowed).

**Examples:**
```javascript
// Add 500 milliseconds
parent_value: 1698710400000
milliseconds: 500
// Output: 1698710400500

// Subtract 250 milliseconds
parent_value: 1698710400000
milliseconds: -250
// Output: 1698710399750
```

### add_secs_to_timestamp

**Purpose**: Add seconds to a timestamp (negative values allowed).

**Examples:**
```javascript
// Add 1 hour (3600 seconds)
parent_value: 1698710400000
seconds: 3600
// Output: 1698714000000

// Subtract 1 minute (60 seconds)
parent_value: 1698710400000
seconds: -60
// Output: 1698710340000
```

**🔗 Time Calculation Patterns:**

**Session Timeout Management:**
```javascript
// n8n: Calculate session expiration
const createSession = (userId) => {
  const now = Date.now();
  const sessionDuration = 30 * 60; // 30 minutes in seconds
  const expiresAt = now.add_secs_to_timestamp(sessionDuration);
  
  return {
    session_id: generateSessionId(),
    user_id: userId,
    created_at: now,
    expires_at: expiresAt,
    is_expired: () => Date.now() > expiresAt
  };
};
```

**Rate Limiting:**
```javascript
// WeWeb: Implement rate limiting with precise timing
const checkRateLimit = (userId, actionType) => {
  const now = Date.now();
  const windowDuration = 60; // 1 minute window
  const windowStart = now.add_secs_to_timestamp(-windowDuration);
  
  const recentActions = getUserActions(userId, actionType, windowStart, now);
  const maxActions = getMaxActionsPerWindow(actionType);
  
  return {
    allowed: recentActions.length < maxActions,
    remaining: Math.max(0, maxActions - recentActions.length),
    reset_at: now.add_secs_to_timestamp(windowDuration)
  };
};
```

**Performance Monitoring:**
```javascript
// Make.com: Track operation timing with millisecond precision
const trackOperationTiming = (operationName, startTime) => {
  const endTime = Date.now();
  const durationMs = endTime - startTime;
  const thresholdMs = 1000; // 1 second threshold
  
  return {
    operation: operationName,
    start_time: startTime,
    end_time: endTime,
    duration_ms: durationMs,
    is_slow: durationMs > thresholdMs,
    performance_grade: durationMs < 100 ? 'excellent' :
                      durationMs < 500 ? 'good' :
                      durationMs < 1000 ? 'acceptable' : 'slow'
  };
};
```

## 🔄 **Relative Date Transformations**

### transform_timestamp

**Purpose**: Apply relative transformations to timestamps using natural language expressions.

**Parameters:**
- `parent_value`: Reference timestamp (epoch in milliseconds)
- `transformation`: String describing the relative transformation
- `timezone`: Timezone for the calculation

**Examples:**

**Day-based Transformations:**
```javascript
// Go back 7 days
parent_value: 1698710400000
transformation: "-7 days"
timezone: "UTC"
// Output: 1698105600000 (7 days earlier)

// Next Monday
parent_value: 1698710400000  // Tuesday
transformation: "next Monday"
timezone: "UTC"
// Output: timestamp for next Monday
```

**Month-based Transformations:**
```javascript
// First day of this month
parent_value: 1698710400000
transformation: "first day of this month"
timezone: "UTC"
// Output: 1698768000000 (October 1, 2023)

// Last day of next month
parent_value: 1698710400000
transformation: "last day of next month"
timezone: "UTC"
// Output: timestamp for November 30, 2023
```

**🔗 Advanced Transformation Patterns:**

**Reporting Period Calculations:**
```javascript
// n8n: Generate reporting periods
const generateReportingPeriods = (referenceDate) => {
  const timezone = "America/New_York";
  
  return {
    today: {
      start: referenceDate.transform_timestamp("today 00:00:00", timezone),
      end: referenceDate.transform_timestamp("today 23:59:59", timezone)
    },
    yesterday: {
      start: referenceDate.transform_timestamp("yesterday 00:00:00", timezone),
      end: referenceDate.transform_timestamp("yesterday 23:59:59", timezone)
    },
    thisWeek: {
      start: referenceDate.transform_timestamp("monday this week 00:00:00", timezone),
      end: referenceDate.transform_timestamp("sunday this week 23:59:59", timezone)
    },
    lastWeek: {
      start: referenceDate.transform_timestamp("monday last week 00:00:00", timezone),
      end: referenceDate.transform_timestamp("sunday last week 23:59:59", timezone)
    },
    thisMonth: {
      start: referenceDate.transform_timestamp("first day of this month 00:00:00", timezone),
      end: referenceDate.transform_timestamp("last day of this month 23:59:59", timezone)
    },
    lastMonth: {
      start: referenceDate.transform_timestamp("first day of last month 00:00:00", timezone),
      end: referenceDate.transform_timestamp("last day of last month 23:59:59", timezone)
    }
  };
};
```

**Recurring Event Scheduling:**
```javascript
// WeWeb: Calculate recurring event dates
const calculateRecurringEvents = (startDate, recurrenceType, count) => {
  const events = [];
  let currentDate = startDate;
  
  const transformations = {
    daily: "+1 day",
    weekly: "+1 week",
    monthly: "+1 month",
    yearly: "+1 year"
  };
  
  const transformation = transformations[recurrenceType];
  
  for (let i = 0; i < count; i++) {
    events.push({
      sequence: i + 1,
      date: currentDate,
      formatted: currentDate.format_timestamp("Y-m-d H:i:s", "UTC")
    });
    
    currentDate = currentDate.transform_timestamp(transformation, "UTC");
  }
  
  return events;
};

// Usage
const weeklyMeetings = calculateRecurringEvents(
  Date.now(),
  "weekly",
  10
);
```

**Business Day Calculations:**
```javascript
// Make.com: Calculate business days and deadlines
const calculateBusinessDeadlines = (startDate, businessDaysToAdd) => {
  let currentDate = startDate;
  let addedDays = 0;
  const results = [];
  
  while (addedDays < businessDaysToAdd) {
    currentDate = currentDate.transform_timestamp("+1 day", "UTC");
    
    // Check if it's a weekday (Monday = 1, Friday = 5)
    const dayOfWeek = currentDate.format_timestamp("N", "UTC");
    
    if (dayOfWeek >= 1 && dayOfWeek <= 5) {
      addedDays++;
      results.push({
        business_day: addedDays,
        date: currentDate,
        day_name: currentDate.format_timestamp("l", "UTC")
      });
    }
  }
  
  return {
    start_date: startDate,
    business_days_added: businessDaysToAdd,
    final_date: currentDate,
    all_dates: results
  };
};
```

## 🌍 **Timezone Management**

### Common Timezone Patterns

**User Timezone Detection:**
```javascript
// WeWeb: Handle user timezone preferences
const handleUserTimezone = (timestamp, userTimezone) => {
  const fallbackTimezone = "UTC";
  const safeTimezone = userTimezone || fallbackTimezone;
  
  return {
    utc: timestamp.format_timestamp("Y-m-d H:i:s", "UTC"),
    local: timestamp.format_timestamp("Y-m-d H:i:s", safeTimezone),
    timezone_name: safeTimezone,
    timezone_offset: timestamp.format_timestamp("P", safeTimezone)
  };
};
```

**Multi-Region Display:**
```javascript
// n8n: Display time across multiple regions
const getGlobalTimes = (timestamp) => {
  const regions = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney',
    'Los Angeles': 'America/Los_Angeles'
  };
  
  const globalTimes = {};
  
  Object.entries(regions).forEach(([city, timezone]) => {
    globalTimes[city] = {
      time: timestamp.format_timestamp("g:i A", timezone),
      date: timestamp.format_timestamp("M j, Y", timezone),
      timezone: timezone,
      offset: timestamp.format_timestamp("P", timezone)
    };
  });
  
  return globalTimes;
};
```

## 📊 **Performance Optimization**

### Efficient Date Operations

**Batch Date Processing:**
```javascript
// Process multiple timestamps efficiently
const batchFormatDates = (timestamps, format, timezone) => {
  // Pre-calculate timezone offset once
  const sampleTimestamp = timestamps[0] || Date.now();
  const timezoneInfo = {
    name: timezone,
    offset: sampleTimestamp.format_timestamp("P", timezone)
  };
  
  return timestamps.map(timestamp => ({
    original: timestamp,
    formatted: timestamp.format_timestamp(format, timezone),
    timezone: timezoneInfo
  }));
};
```

**Cached Format Strings:**
```javascript
// Cache commonly used format strings
const DateFormats = {
  ISO_DATE: "Y-m-d",
  ISO_DATETIME: "Y-m-d H:i:s",
  US_SHORT: "m/d/Y",
  US_LONG: "F j, Y",
  DISPLAY_FRIENDLY: "M j, Y g:i A",
  LOG_FORMAT: "Y-m-d H:i:s.v",
  API_FORMAT: "c"
};

const formatForDisplay = (timestamp, timezone = "UTC") => {
  return timestamp.format_timestamp(DateFormats.DISPLAY_FRIENDLY, timezone);
};
```

## 🎯 **Common Integration Patterns**

### Event Scheduling System

```javascript
// Complete event scheduling with timezone support
const createEventSchedule = (eventData) => {
  const eventTimezone = eventData.timezone || "UTC";
  const eventStart = eventData.start_time.parse_timestamp(
    "Y-m-d H:i:s",
    eventTimezone
  );
  
  return {
    event_id: eventData.id,
    title: eventData.title,
    
    // Various time representations
    times: {
      start_utc: eventStart,
      start_local: eventStart.format_timestamp("Y-m-d H:i:s", eventTimezone),
      start_display: eventStart.format_timestamp("l, F j \\a\\t g:i A", eventTimezone)
    },
    
    // Calculated deadlines
    deadlines: {
      registration_closes: eventStart.add_secs_to_timestamp(-24 * 60 * 60), // 24 hours before
      setup_starts: eventStart.add_secs_to_timestamp(-2 * 60 * 60), // 2 hours before
      cleanup_ends: eventStart.add_secs_to_timestamp(4 * 60 * 60) // 4 hours after
    },
    
    // Business logic
    status: {
      is_upcoming: eventStart > Date.now(),
      is_today: eventStart.format_timestamp("Y-m-d", eventTimezone) === 
                Date.now().format_timestamp("Y-m-d", eventTimezone),
      days_until: Math.ceil((eventStart - Date.now()) / (1000 * 60 * 60 * 24))
    }
  };
};
```

### Activity Timeline

```javascript
// Generate activity timeline with relative timestamps
const generateActivityTimeline = (activities) => {
  const now = Date.now();
  
  return activities.map(activity => {
    const activityTime = activity.timestamp;
    const timeDiff = now - activityTime;
    
    // Calculate relative time
    let relativeTime;
    if (timeDiff < 60000) { // Less than 1 minute
      relativeTime = "just now";
    } else if (timeDiff < 3600000) { // Less than 1 hour
      const minutes = Math.floor(timeDiff / 60000);
      relativeTime = `${minutes} minute${minutes !== 1 ? 's' : ''} ago`;
    } else if (timeDiff < 86400000) { // Less than 1 day
      const hours = Math.floor(timeDiff / 3600000);
      relativeTime = `${hours} hour${hours !== 1 ? 's' : ''} ago`;
    } else {
      relativeTime = activityTime.format_timestamp("M j, Y", "UTC");
    }
    
    return {
      ...activity,
      formatted_time: activityTime.format_timestamp("g:i A", "UTC"),
      relative_time: relativeTime,
      is_recent: timeDiff < 3600000 // Within last hour
    };
  });
};
```

---

**Next Steps**: Explore [Array Filters](array-filters.md) and [Text Processing Filters](text-filters.md) to complete your data manipulation toolkit.