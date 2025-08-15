---
title: "Response Caching"
description: "Improve API performance and reduce server load using Xano's response caching mechanisms"
category: function-stack
difficulty: intermediate
tags:
  - caching
  - performance
  - optimization
  - redis
  - api-response
  - speed
related_docs:
  - data-caching-redis
  - performance
  - optimization
  - middleware
last_updated: '2025-01-23'
---

# Response Caching

## Quick Summary
Response caching stores API responses temporarily to improve performance, reduce database load, and provide faster user experiences for frequently accessed data. Essential for high-traffic applications and data-heavy operations.

## What You'll Learn
- Implementing response caching strategies
- Cache invalidation and TTL management
- Performance optimization techniques
- Integration with Redis and memory caching
- Best practices for cache-aware API design

## Core Caching Concepts

### Cache Types
- **Memory Cache** - Fast in-memory storage for immediate access
- **Redis Cache** - Distributed caching for scalable applications
- **CDN Caching** - Edge caching for global content delivery
- **Browser Cache** - Client-side caching with HTTP headers
- **Database Query Cache** - Cache expensive database operations

### Cache Strategies
- **Cache-Aside** - Application manages cache explicitly
- **Write-Through** - Write to cache and database simultaneously
- **Write-Behind** - Write to cache first, database later
- **Refresh-Ahead** - Proactively refresh before expiration

## Basic Response Caching

### Simple Cache Implementation
```javascript
// Basic response caching function
function getCachedResponse(cacheKey, fetchFunction, ttl = 300) {
  // 1. Check if cached response exists
  const cached = getFromCache(cacheKey);
  
  if (cached && !isExpired(cached)) {
    return cached.data;
  }
  
  // 2. Fetch fresh data
  const freshData = fetchFunction();
  
  // 3. Store in cache with TTL
  storeInCache(cacheKey, {
    data: freshData,
    timestamp: Date.now(),
    ttl: ttl
  });
  
  return freshData;
}
```

### Cache Key Generation
```javascript
// Generate unique cache keys
function generateCacheKey(endpoint, params = {}) {
  const sortedParams = Object.keys(params)
    .sort()
    .map(key => `${key}:${params[key]}`)
    .join('|');
    
  return `api:${endpoint}:${sortedParams}`;
}

// Examples
generateCacheKey('products', { category: 'electronics', page: 1 });
// Result: "api:products:category:electronics|page:1"
```

## Advanced Caching Patterns

### Conditional Caching
```javascript
// Cache based on data characteristics
function smartCache(data, context) {
  let ttl = 300; // Default 5 minutes
  
  // Adjust TTL based on data type
  if (context.dataType === 'user_profile') {
    ttl = 900; // 15 minutes for profiles
  } else if (context.dataType === 'product_catalog') {
    ttl = 1800; // 30 minutes for products
  } else if (context.dataType === 'real_time_data') {
    ttl = 30; // 30 seconds for real-time
  }
  
  // Don't cache error responses
  if (data.error) {
    return data;
  }
  
  // Don't cache personalized data
  if (context.isPersonalized) {
    return data;
  }
  
  return cacheResponse(data, ttl);
}
```

### Multi-Layer Caching
```javascript
// Implement cache hierarchy
async function getWithMultiLayerCache(key, fetchFunction) {
  // Layer 1: Memory cache (fastest)
  let result = memoryCache.get(key);
  if (result) {
    return result;
  }
  
  // Layer 2: Redis cache (fast)
  result = await redisCache.get(key);
  if (result) {
    // Promote to memory cache
    memoryCache.set(key, result, 60); // 1 minute in memory
    return result;
  }
  
  // Layer 3: Database (slowest)
  result = await fetchFunction();
  
  // Store in both cache layers
  await redisCache.set(key, result, 900); // 15 minutes in Redis
  memoryCache.set(key, result, 60); // 1 minute in memory
  
  return result;
}
```

## Cache Invalidation Strategies

### Time-Based Invalidation (TTL)
```javascript
// TTL-based cache management
const cacheTTLConfig = {
  'user_profiles': 900,      // 15 minutes
  'product_data': 1800,      // 30 minutes
  'system_config': 3600,     // 1 hour
  'analytics_data': 7200,    // 2 hours
  'static_content': 86400    // 24 hours
};

function setCacheWithTTL(key, data, category) {
  const ttl = cacheTTLConfig[category] || 300;
  return cache.set(key, data, ttl);
}
```

### Event-Based Invalidation
```javascript
// Invalidate cache when data changes
function invalidateCacheOnUpdate(tableName, recordId) {
  const keysToInvalidate = [
    `${tableName}:${recordId}`,
    `${tableName}:list:*`,
    `dashboard:${tableName}:*`
  ];
  
  keysToInvalidate.forEach(pattern => {
    if (pattern.includes('*')) {
      // Wildcard invalidation
      const keys = cache.keys(pattern);
      cache.del(keys);
    } else {
      cache.del(pattern);
    }
  });
}
```

### Tag-Based Invalidation
```javascript
// Cache with tags for grouped invalidation
function cacheWithTags(key, data, tags, ttl = 300) {
  // Store main data
  cache.set(key, data, ttl);
  
  // Store tag associations
  tags.forEach(tag => {
    const tagKey = `tag:${tag}`;
    cache.sadd(tagKey, key);
    cache.expire(tagKey, ttl);
  });
}

function invalidateByTag(tag) {
  const tagKey = `tag:${tag}`;
  const keys = cache.smembers(tagKey);
  
  if (keys.length > 0) {
    cache.del(keys);
    cache.del(tagKey);
  }
}

// Example usage
cacheWithTags('product:123', productData, ['products', 'electronics', 'featured']);
// Later: invalidate all electronics products
invalidateByTag('electronics');
```

## Integration with n8n

### Cache-Aware Data Processing
```javascript
// n8n workflow with caching
const cacheKey = `report:${$json.report_type}:${$json.date_range}`;

// Check cache first
const cachedResult = await $httpRequest({
  method: 'GET',
  url: `https://your-instance.xano.io/api:cache/get/${cacheKey}`
});

if (cachedResult.data) {
  // Use cached data
  return cachedResult.data;
} else {
  // Generate fresh report
  const reportData = await generateReport($json);
  
  // Cache the result
  await $httpRequest({
    method: 'POST',
    url: 'https://your-instance.xano.io/api:cache/set',
    body: {
      key: cacheKey,
      data: reportData,
      ttl: 3600 // 1 hour
    }
  });
  
  return reportData;
}
```

### Cache Warming
```javascript
// n8n workflow to warm cache with popular data
const popularProducts = await $httpRequest({
  method: 'GET',
  url: 'https://your-instance.xano.io/api:analytics/popular-products'
});

// Pre-cache popular products
for (const product of popularProducts.data) {
  const productData = await $httpRequest({
    method: 'GET',
    url: `https://your-instance.xano.io/api:products/${product.id}`
  });
  
  // Cache for 1 hour
  await $httpRequest({
    method: 'POST',
    url: 'https://your-instance.xano.io/api:cache/set',
    body: {
      key: `product:${product.id}`,
      data: productData,
      ttl: 3600
    }
  });
}
```

## Integration with WeWeb

### Client-Side Cache Management
```javascript
// WeWeb component with intelligent caching
export default {
  data() {
    return {
      cache: new Map(),
      cacheTTL: 5 * 60 * 1000, // 5 minutes
      loading: false
    };
  },
  
  methods: {
    async fetchWithCache(endpoint, params = {}) {
      const cacheKey = this.generateCacheKey(endpoint, params);
      const cached = this.cache.get(cacheKey);
      
      // Check if cache is still valid
      if (cached && Date.now() - cached.timestamp < this.cacheTTL) {
        return cached.data;
      }
      
      this.loading = true;
      
      try {
        // Fetch fresh data
        const response = await this.$xano.get(endpoint, { params });
        
        // Store in cache
        this.cache.set(cacheKey, {
          data: response.data,
          timestamp: Date.now()
        });
        
        return response.data;
      } finally {
        this.loading = false;
      }
    },
    
    invalidateCache(pattern) {
      // Remove matching cache entries
      for (const [key] of this.cache) {
        if (key.includes(pattern)) {
          this.cache.delete(key);
        }
      }
    },
    
    generateCacheKey(endpoint, params) {
      const paramString = JSON.stringify(params);
      return `${endpoint}:${btoa(paramString)}`;
    }
  }
};
```

### Cache-First Component Pattern
```javascript
// WeWeb product list with smart caching
export default {
  data() {
    return {
      products: [],
      cacheStatus: 'checking'
    };
  },
  
  async mounted() {
    await this.loadProducts();
  },
  
  methods: {
    async loadProducts() {
      this.cacheStatus = 'checking';
      
      try {
        // Try cache first
        const cached = await this.checkCache();
        
        if (cached) {
          this.products = cached;
          this.cacheStatus = 'cached';
          
          // Optionally refresh in background
          this.refreshInBackground();
        } else {
          // Fetch fresh data
          await this.fetchFreshProducts();
        }
      } catch (error) {
        console.error('Error loading products:', error);
        this.cacheStatus = 'error';
      }
    },
    
    async checkCache() {
      const cacheKey = 'products:list';
      const cached = localStorage.getItem(cacheKey);
      
      if (cached) {
        const { data, timestamp } = JSON.parse(cached);
        const maxAge = 10 * 60 * 1000; // 10 minutes
        
        if (Date.now() - timestamp < maxAge) {
          return data;
        }
      }
      
      return null;
    },
    
    async fetchFreshProducts() {
      this.cacheStatus = 'fetching';
      
      const response = await this.$xano.get('/products');
      this.products = response.data;
      
      // Cache the results
      localStorage.setItem('products:list', JSON.stringify({
        data: response.data,
        timestamp: Date.now()
      }));
      
      this.cacheStatus = 'fresh';
    },
    
    async refreshInBackground() {
      // Silent refresh for next visit
      try {
        const response = await this.$xano.get('/products');
        localStorage.setItem('products:list', JSON.stringify({
          data: response.data,
          timestamp: Date.now()
        }));
      } catch (error) {
        // Silent fail for background refresh
        console.warn('Background refresh failed:', error);
      }
    }
  }
};
```

## Performance Optimization

### Cache Hit Rate Monitoring
```javascript
// Track cache performance
const cacheMetrics = {
  hits: 0,
  misses: 0,
  errors: 0
};

function trackCacheHit(key, hit) {
  if (hit) {
    cacheMetrics.hits++;
  } else {
    cacheMetrics.misses++;
  }
  
  // Log metrics periodically
  if ((cacheMetrics.hits + cacheMetrics.misses) % 100 === 0) {
    const hitRate = cacheMetrics.hits / (cacheMetrics.hits + cacheMetrics.misses);
    console.log(`Cache hit rate: ${(hitRate * 100).toFixed(2)}%`);
  }
}
```

### Memory Usage Optimization
```javascript
// Implement cache size limits
class LRUCache {
  constructor(maxSize = 1000) {
    this.maxSize = maxSize;
    this.cache = new Map();
  }
  
  get(key) {
    if (this.cache.has(key)) {
      // Move to end (most recent)
      const value = this.cache.get(key);
      this.cache.delete(key);
      this.cache.set(key, value);
      return value;
    }
    return null;
  }
  
  set(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.maxSize) {
      // Remove oldest entry
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    
    this.cache.set(key, value);
  }
}
```

## Try This: Build a Smart Caching System

1. **Implement Multi-Layer Cache**
   ```
   1. Create memory cache for immediate access
   2. Add Redis cache for persistence
   3. Implement cache-aside pattern
   4. Add cache warming for popular data
   5. Monitor cache hit rates and performance
   ```

2. **Add Intelligent Invalidation**
   ```
   1. Tag-based invalidation by data type
   2. Event-driven cache clearing
   3. Partial cache updates for efficiency
   4. Cache versioning for rolling updates
   5. Background cache refresh
   ```

3. **Frontend Integration**
   ```
   1. Client-side caching in WeWeb
   2. Cache-first loading strategies
   3. Background refresh patterns
   4. Cache synchronization across tabs
   5. Offline cache capabilities
   ```

## Common Mistakes to Avoid

❌ **Caching personalized data** - Never cache user-specific content
❌ **Not setting TTL** - All cached data should have expiration
❌ **Cache stampede** - Multiple requests fetching same data simultaneously
❌ **Ignoring cache size** - Implement size limits to prevent memory issues
❌ **Caching errors** - Don't cache error responses or failed requests
❌ **Not monitoring performance** - Track cache hit rates and effectiveness

## Pro Tips

💡 **Use cache tags** for grouped invalidation strategies
💡 **Implement cache warming** for better user experience
💡 **Monitor cache hit rates** to optimize strategy
💡 **Use compression** for large cached objects
💡 **Implement graceful degradation** when cache is unavailable
💡 **Set appropriate TTL** based on data change frequency
💡 **Use cache hierarchies** for optimal performance

Response caching is essential for building fast, scalable applications that provide excellent user experiences even under heavy load.