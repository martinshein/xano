---
title: "Redis Caching - Lightning-Fast Data Storage"
description: "Speed up your backend with temporary in-memory data caching"
category: function-stack
subcategory: caching
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- redis
- caching
- performance
- memory-storage
- optimization
---

# Redis Caching - Lightning-Fast Data Storage



## Quick Summary

> **What it is:** Temporary high-speed memory storage for frequently accessed data
> 
> **When to use:** Speeding up repeated database queries, storing session data, or implementing rate limiting
> 
> **Key benefit:** 100x faster than database queries for cached data
> 
> **Perfect for:** Non-developers optimizing app performance without complex infrastructure

## What You'll Learn

- Understanding cache concepts
- Setting and getting cached values
- Managing cache expiration
- Rate limiting implementation
- Best practices for caching

## Why Use Caching?

Without cache:
```
User Request → Database Query (100ms) → Response
User Request → Same Query (100ms) → Response
User Request → Same Query (100ms) → Response
```

With cache:
```
User Request → Database Query (100ms) → Cache → Response
User Request → Cache (1ms) → Response
User Request → Cache (1ms) → Response
```

## Cache Functions Overview

### Basic Operations
- **Set Cache Value** - Store data
- **Get Cache Value** - Retrieve data
- **Has Cache Value** - Check existence
- **Delete Cache Value** - Remove data

### Counters
- **Increment/Decrement** - Atomic counters
- **Rate Limit** - Request throttling

### Lists
- **Add/Remove from List** - Queue operations
- **Get List Elements** - Batch retrieval

## Setting Cache Values

```javascript
// Store API response
weather_data = Call_Weather_API()

Set_Cache_Value {
  key: "weather_london",
  data: weather_data,
  ttl: 3600  // Cache for 1 hour
}
```

### Key Naming Strategies

```javascript
// User-specific
key: "user_123_settings"

// Time-based
key: "daily_report_2024_01_15"

// Category-based
key: "product_category_electronics"
```

## Getting Cache Values

```javascript
// Check cache first
cached_data = Get_Cache_Value("weather_london")

if (cached_data) {
  // Use cached data (fast!)
  return cached_data
} else {
  // Fetch fresh data
  fresh_data = Call_Weather_API()
  Set_Cache_Value("weather_london", fresh_data, 3600)
  return fresh_data
}
```

## Integration Examples

### With n8n - API Response Caching

```javascript
// n8n webhook request
request_id = Input.endpoint + Input.params

// Check cache
cached = Get_Cache_Value(request_id)
if (cached) return cached

// Process if not cached
result = Complex_Processing()
Set_Cache_Value(request_id, result, 300)
return result
```

### With WeWeb - User Sessions

```javascript
// Store user session
Set_Cache_Value {
  key: "session_" + token,
  data: {
    user_id: user.id,
    permissions: user.permissions,
    expires: timestamp
  },
  ttl: 86400  // 24 hours
}
```

## Rate Limiting

Protect your APIs from abuse:

```javascript
Rate_Limit {
  key: "api_" + user_id,
  max: 100,      // 100 requests
  ttl: 3600,     // per hour
  error: "Rate limit exceeded"
}

// Continues only if under limit
Process_Request()
```

## Common Caching Patterns

### Cache-Aside Pattern

```javascript
function Get_Product(id) {
  // Try cache
  cached = Get_Cache("product_" + id)
  if (cached) return cached
  
  // Load from database
  product = Query_Database(id)
  
  // Store in cache
  Set_Cache("product_" + id, product, 600)
  
  return product
}
```

### Session Storage

```javascript
// Login
session_data = {
  user_id: user.id,
  login_time: now(),
  ip_address: request.ip
}
Set_Cache("session_" + token, session_data, 7200)

// Validate
session = Get_Cache("session_" + token)
if (!session) return "Session expired"
```

### Counter Pattern

```javascript
// Page views
views = Increment_Cache("pageviews_" + page_id, 1)

// API calls
calls = Increment_Cache("api_calls_" + date, 1)

// Inventory holds
Decrement_Cache("stock_" + product_id, quantity)
```

## Cache Management

### TTL (Time To Live)

```javascript
// Short-lived (seconds)
Set_Cache(key, data, 60)      // 1 minute

// Medium (minutes/hours)  
Set_Cache(key, data, 3600)    // 1 hour

// Long-lived (days)
Set_Cache(key, data, 86400)   // 24 hours

// Permanent (use carefully!)
Set_Cache(key, data, 0)        // Never expires
```

### Cache Invalidation

```javascript
// After update
Update_Product(product)
Delete_Cache("product_" + product.id)

// Bulk invalidation
keys = Get_Cache_Keys("product_*")
For Each key {
  Delete_Cache(key)
}
```

## List Operations

### Queue Processing

```javascript
// Add to queue
Add_to_End_of_List("email_queue", email_data)

// Process queue
email = Remove_from_Beginning_of_List("email_queue")
if (email) {
  Send_Email(email)
}
```

### Recent Items

```javascript
// Add recent search
Add_to_Beginning_of_List("recent_searches", term)

// Get last 10
recent = Get_Elements_from_List("recent_searches", 0, 9)
```

## Best Practices

### Cache Keys
- Use consistent naming
- Include version numbers
- Add user/tenant prefixes
- Keep keys short

### What to Cache
✅ **Good candidates:**
- Database query results
- API responses
- Computed values
- Session data

❌ **Don't cache:**
- Sensitive data
- Frequently changing data
- Large files
- Personal information

### Cache Strategies

```javascript
// Lazy loading
if (!cached) {
  load_and_cache()
}

// Pre-warming
On_Startup {
  Cache_Popular_Items()
}

// Background refresh
Background_Task {
  Refresh_Cache()
}
```

## Try This

Build a cached API endpoint:
1. Create API to fetch data
2. Add cache check at start
3. Cache miss: fetch and store
4. Cache hit: return immediately
5. Test response times

## Pro Tips

💡 **Start Small:** Cache one slow query first

💡 **Monitor Hit Rate:** Track cache effectiveness

💡 **Set Reasonable TTLs:** Balance freshness vs performance

💡 **Handle Failures:** Always have fallback to database

💡 **Clear on Updates:** Invalidate cache when data changes

## Common Issues

### Stale Data
- Problem: Cached data outdated
- Solution: Shorter TTL or invalidation on update

### Memory Limits
- Problem: 100MB limit reached
- Solution: Reduce TTL, clean old keys

### Cache Stampede
- Problem: Many requests after cache expires
- Solution: Add small random TTL variation

## Next Steps

1. Identify slow queries
2. Add caching layer
3. Monitor performance gains
4. Implement cache invalidation
5. Add rate limiting

Remember: Caching is temporary storage - always have a plan for when cache is empty!