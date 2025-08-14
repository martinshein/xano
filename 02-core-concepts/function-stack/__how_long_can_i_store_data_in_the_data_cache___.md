---
title: "Data Caching with Redis in Xano"
description: "Master high-performance data caching in Xano using Redis for temporary storage, rate limiting, and performance optimization"
category: function-stack
subcategory: performance
has_code_examples: true
last_updated: '2025-01-23'
tags:
- caching
- redis
- performance
- rate-limiting
- temporary-storage
---

# Data Caching with Redis in Xano

## Quick Summary

> **What it is:** Xano's built-in data caching service powered by Redis that stores frequently-accessed data in memory for lightning-fast retrieval
> 
> **When to use:** Perfect for storing temporary data, API responses, user sessions, or any data that needs quick access for a limited time
> 
> **Key benefit:** Dramatically improves performance by reducing database queries and external API calls
> 
> **Plan requirement:** Starter plan or higher

## What You'll Learn

- Setting up and managing cache values with key-value pairs
- Implementing cache expiration strategies
- Using lists for queue management
- Setting up rate limiting for API protection
- Real-world caching patterns for n8n and WeWeb integrations

## Understanding Data Caching

Think of caching like keeping frequently-used items on your desk instead of in a filing cabinet. When you cache data in Xano, you're storing it in super-fast memory (RAM) instead of the database, making it instantly accessible.

### Cache Storage Duration

You control how long data stays cached through two methods:
1. **Time-based expiration:** Set a specific time-to-live (TTL) in seconds
2. **Size limit:** Automatically overwrites oldest data when reaching 100MB limit

⚠️ **Important:** Cache is temporary storage! Never store irreplaceable data in cache - always use the database for permanent storage.

## Core Cache Functions

### 1. Set a Cache Value

Store any data with a unique key for later retrieval.

**Configuration:**
- **Key:** Your unique identifier (like "user_123_profile")
- **Data:** The information to cache (can be any data type)
- **TTL:** Time in seconds before auto-deletion (0 = never expire)

**Example for n8n/WeWeb:**
```javascript
// Cache user preferences for 1 hour (3600 seconds)
Key: "user_preferences_" + user_id
Data: {
  theme: "dark",
  language: "en",
  notifications: true
}
TTL: 3600
```

### 2. Get a Cache Value

Retrieve cached data using its key.

**Returns:** The cached data or `false` if not found

**Smart Pattern:**
```javascript
1. Try to get from cache
2. If not found (returns false):
   - Fetch from database/API
   - Cache the result
   - Return the data
3. If found: use cached data
```

### 3. Check if Cache Exists

Verify if a cache value exists without retrieving it.

**Use case:** Checking if a user session is still active
```javascript
Key: "session_" + session_token
Returns: true (exists) or false (expired/not found)
```

## Working with Lists

Lists are perfect for queues, recent activities, or temporary collections.

### List Operations

**Add to Beginning:** Insert at start (like a stack - LIFO)
```javascript
Key: "recent_searches"
Value: "Xano tutorials"
// Newest searches appear first
```

**Add to End:** Append to end (like a queue - FIFO)
```javascript
Key: "processing_queue"
Value: {task_id: 123, type: "email"}
// Process oldest tasks first
```

**Remove Items:** Delete from any position
- Remove from beginning/end
- Remove specific values
- Remove multiple occurrences

**Get List Info:**
- Length: Count items in list
- Range: Retrieve specific portions (supports negative indexing)

## Rate Limiting

Protect your APIs from overuse with built-in rate limiting.

**Configuration:**
```javascript
Key: "api_limit_" + user_id
Max: 100         // Maximum requests
TTL: 3600        // Per hour (in seconds)
Error: "Rate limit exceeded. Try again later."
```

**Try This:** Implement tiered rate limits
- Free users: 100 requests/hour
- Pro users: 1000 requests/hour
- Enterprise: Unlimited

## Increment/Decrement Counters

Perfect for tracking counts without database writes.

**Use cases:**
- Page view counters
- Available inventory
- Active user sessions
- Limited-time promotions

```javascript
// Track first 100 signups for special offer
Key: "promo_signups"
Increment by: 1
// Check if result <= 100 for eligibility
```

## Best Practices for n8n/WeWeb

### 1. Cache External API Responses
```javascript
Key: "weather_api_" + city
Data: API response
TTL: 600  // 10 minutes for weather data
```

### 2. Session Management
```javascript
Key: "session_" + token
Data: {user_id, permissions, expires_at}
TTL: 1800  // 30-minute sessions
```

### 3. Temporary Form Data
```javascript
Key: "form_draft_" + user_id
Data: form_fields
TTL: 86400  // Save drafts for 24 hours
```

## Common Mistakes to Avoid

1. **Storing Critical Data Only in Cache**
   - Always have a database backup
   - Cache can be cleared anytime

2. **Using Complex Objects as Keys**
   - Keep keys simple and string-based
   - Use prefixes for organization

3. **Forgetting TTL Settings**
   - Always set appropriate expiration
   - Consider your use case carefully

4. **Not Handling Cache Misses**
   - Always check if data exists
   - Have a fallback strategy

## Pro Tips

💡 **JSON Storage Trick:** Store complex objects as JSON strings for better compatibility with Redis operations

💡 **Key Naming Convention:** Use prefixes like `user_`, `api_`, `temp_` for easy management

💡 **Cache Warming:** Pre-load frequently accessed data during off-peak hours

💡 **Monitoring:** Use Get Cache Keys with wildcards to monitor cache usage

## Integration Examples

### With n8n
- Cache webhook payloads for retry logic
- Store temporary workflow states
- Rate limit incoming webhooks

### With WeWeb
- Cache user preferences
- Store shopping cart data
- Manage temporary UI states

## Try This

Create a simple view counter:
1. Set up an increment cache for page views
2. Display the count in your frontend
3. Reset daily using TTL of 86400 seconds
4. Compare with database analytics weekly

Remember: Caching is about speed, not permanence. Use it wisely to create lightning-fast experiences for your users!