---
title: "API Request History with Metadata API - Complete Guide"
description: "Master Xano's request history tracking via Metadata API - perfect for monitoring performance, debugging issues, and building admin dashboards with n8n, WeWeb, and Make"
category: api-endpoints
tags:
  - Request History
  - API Monitoring
  - Performance Tracking
  - Debugging
  - API Analytics
difficulty: intermediate
reading_time: 8 minutes
last_updated: '2025-01-23'
prerequisites:
  - Metadata API access token
  - Understanding of API requests
  - Basic knowledge of filtering and sorting
---

# API Request History with Metadata API

## 📋 **Quick Summary**

**What it does:** The Metadata API's request history feature lets you programmatically access and analyze all API requests made to your Xano workspace for monitoring, debugging, and analytics.

**Why it matters:** This enables you to:
- Monitor API performance and response times
- Debug issues by examining failed requests
- Build custom analytics dashboards
- Track usage patterns and optimize endpoints
- Create automated alerting systems

**Time to implement:** 5-10 minutes for basic querying, 30+ minutes for advanced analytics

---

## What You'll Learn

- How to browse and search request history
- Filtering by duration, status codes, and timestamps
- Building performance monitoring dashboards
- Debugging failed requests with detailed analysis
- Automating request history analysis workflows
- Integration patterns for monitoring tools

## Understanding Request History in Xano

Think of the request history as your API's black box recorder - it captures every detail about every request made to your workspace, from response times to error details.

### 🎯 **Perfect For:**
- Performance monitoring dashboards
- Debugging production issues
- Usage analytics and reporting
- Automated alerting systems
- Compliance and audit trails

## Authentication & Setup

### Access Requirements

Request history requires proper Metadata API authentication:

```javascript
headers: {
  'Authorization': 'Bearer YOUR_METADATA_TOKEN',
  'Content-Type': 'application/json'
}
```

## Browsing Request History

### Basic Request History Retrieval

Get a simple list of recent API requests:

```json
GET /api:metadata/request-history/browse
{
  "workspace_id": 12345,
  "page": 1,
  "per_page": 50
}
```

### 📝 **Example Response**

```json
{
  "data": [
    {
      "id": "req_abc123",
      "created_at": 1681349436618,
      "duration": 0.245,
      "status": 200,
      "method": "POST",
      "path": "/api/users/login",
      "api_id": 789,
      "query_id": 456,
      "branch_id": "main",
      "user_agent": "Mozilla/5.0...",
      "ip_address": "192.168.1.100"
    }
  ],
  "pagination": {
    "current_page": 1,
    "per_page": 50,
    "total": 1250
  }
}
```

### Filtering Options

| Parameter | Description | Example |
|-----------|-------------|----------|
| `workspace_id` | Your workspace identifier | `12345` |
| `branch_id` | Specific branch (optional) | `"main"`, `"dev"` |
| `api_id` | API group filter | `789` |
| `query_id` | Specific endpoint ID | `456` |
| `include_output` | Include response data | `true`/`false` |

### 💡 **Focused Monitoring**

```javascript
// Monitor specific endpoint performance
const loginRequests = await metadataAPI.browseHistory({
  workspace_id: 12345,
  query_id: 456, // Login endpoint
  per_page: 100,
  include_output: false // Faster queries
});
```

## Advanced Search & Filtering

### Search by Performance Metrics

Find slow requests for optimization:

```json
POST /api:metadata/request-history/search
{
  "workspace_id": 12345,
  "page": 1,
  "per_page": 50,
  "sort": {
    "duration": "desc"
  },
  "search": [
    {
      "duration|>|": 2.0
    }
  ]
}
```

### Search by Status Codes

Identify error patterns:

```json
{
  "workspace_id": 12345,
  "sort": {
    "created_at": "desc"
  },
  "search": [
    {
      "status|in|": [400, 401, 403, 500]
    }
  ]
}
```

### Time-based Analysis

Track requests within specific timeframes:

```json
{
  "workspace_id": 12345,
  "search": [
    {
      "created_at|>=|": 1681305600000,
      "created_at|<=|": 1681392000000
    }
  ],
  "sort": {
    "created_at": "asc"
  }
}
```

## Performance Monitoring Patterns

### Pattern 1: Real-time Performance Dashboard

```yaml
Real-time Monitor:
1. Query last 5 minutes of requests
2. Calculate average response time
3. Count errors by status code
4. Identify slow endpoints
5. Display metrics in dashboard
```

### Pattern 2: Error Analysis Workflow

```yaml
Error Investigation:
1. Filter by error status codes (4xx, 5xx)
2. Group by endpoint and error type
3. Analyze request patterns
4. Generate incident reports
5. Create alerts for recurring issues
```

### Pattern 3: Usage Analytics

```yaml
Usage Reporting:
1. Aggregate requests by time periods
2. Calculate endpoint popularity
3. Track user activity patterns
4. Generate usage reports
5. Optimize based on data
```

## No-Code Platform Integrations

### 🔗 **n8n Monitoring Workflow**

```yaml
1. Schedule Trigger (Every 5 minutes)
2. HTTP Request (Get recent request history)
3. Function Node (Calculate performance metrics)
4. IF Node (Check for performance issues)
5. Email Node (Alert on issues)
6. HTTP Request (Log to monitoring service)
```

**n8n Configuration Example:**
```javascript
// Calculate average response time
const requests = $input.all()[0].json.data;
const avgDuration = requests.reduce((sum, req) => sum + req.duration, 0) / requests.length;
const errorCount = requests.filter(req => req.status >= 400).length;

return {
  avgResponseTime: avgDuration,
  errorRate: (errorCount / requests.length) * 100,
  totalRequests: requests.length
};
```

### 🌐 **WeWeb Analytics Dashboard**

```javascript
// WeWeb collection for request analytics
async function loadRequestMetrics() {
  const history = await wwLib.api.post({
    url: wwLib.envVars.XANO_METADATA_API + '/request-history/search',
    data: {
      workspace_id: wwLib.envVars.WORKSPACE_ID,
      search: [
        {
          "created_at|>=|": Date.now() - (24 * 60 * 60 * 1000) // Last 24 hours
        }
      ]
    },
    headers: {
      'Authorization': 'Bearer ' + wwLib.envVars.METADATA_TOKEN
    }
  });
  
  // Process data for charts
  const metrics = processRequestMetrics(history.data);
  
  // Update WeWeb collections
  wwLib.collections.requestMetrics.update(metrics);
  
  return metrics;
}
```

### 🔧 **Make Performance Monitoring**

```yaml
Scenario Steps:
1. Schedule (Every 15 minutes)
2. HTTP Request (Get request history)
3. Array Aggregator (Group by status)
4. Math Function (Calculate metrics)
5. Filter (Check thresholds)
6. Slack Message (Send alerts)
```

## Debugging with Request History

### Finding Failed Requests

```javascript
// Search for recent failures
const searchParams = {
  workspace_id: 12345,
  search: [
    {
      "status|>=|": 400,
      "created_at|>=|": Date.now() - (60 * 60 * 1000) // Last hour
    }
  ],
  include_output: true,
  sort: {
    "created_at": "desc"
  }
};
```

### Analyzing Error Patterns

```javascript
// Group errors by endpoint and status
function analyzeErrors(requests) {
  const errorsByEndpoint = {};
  
  requests.forEach(req => {
    if (req.status >= 400) {
      const key = `${req.method} ${req.path}`;
      if (!errorsByEndpoint[key]) {
        errorsByEndpoint[key] = {
          count: 0,
          statuses: {},
          examples: []
        };
      }
      
      errorsByEndpoint[key].count++;
      errorsByEndpoint[key].statuses[req.status] = 
        (errorsByEndpoint[key].statuses[req.status] || 0) + 1;
      
      if (errorsByEndpoint[key].examples.length < 3) {
        errorsByEndpoint[key].examples.push({
          timestamp: req.created_at,
          status: req.status,
          duration: req.duration,
          output: req.output
        });
      }
    }
  });
  
  return errorsByEndpoint;
}
```

## Building Analytics Dashboards

### Performance Metrics Calculation

```javascript
function calculatePerformanceMetrics(requests) {
  const now = Date.now();
  const oneHourAgo = now - (60 * 60 * 1000);
  const oneDayAgo = now - (24 * 60 * 60 * 1000);
  
  const hourlyRequests = requests.filter(r => r.created_at >= oneHourAgo);
  const dailyRequests = requests.filter(r => r.created_at >= oneDayAgo);
  
  return {
    requestsPerHour: hourlyRequests.length,
    requestsPerDay: dailyRequests.length,
    avgResponseTime: {
      hourly: average(hourlyRequests.map(r => r.duration)),
      daily: average(dailyRequests.map(r => r.duration))
    },
    errorRates: {
      hourly: errorRate(hourlyRequests),
      daily: errorRate(dailyRequests)
    },
    slowestEndpoints: findSlowestEndpoints(dailyRequests),
    topErrors: getTopErrors(dailyRequests)
  };
}
```

### Real-time Alerting Logic

```javascript
function checkPerformanceThresholds(metrics) {
  const alerts = [];
  
  // Check response time
  if (metrics.avgResponseTime.hourly > 2.0) {
    alerts.push({
      type: 'performance',
      severity: 'warning',
      message: `Average response time is ${metrics.avgResponseTime.hourly}s (threshold: 2.0s)`
    });
  }
  
  // Check error rate
  if (metrics.errorRates.hourly > 5) {
    alerts.push({
      type: 'errors',
      severity: 'critical',
      message: `Error rate is ${metrics.errorRates.hourly}% (threshold: 5%)`
    });
  }
  
  // Check request volume drop
  if (metrics.requestsPerHour < (metrics.requestsPerDay / 24) * 0.3) {
    alerts.push({
      type: 'volume',
      severity: 'info',
      message: 'Request volume is significantly below daily average'
    });
  }
  
  return alerts;
}
```

## Advanced Use Cases

### Use Case 1: Automated Performance Optimization

```javascript
// Identify and optimize slow endpoints
class PerformanceOptimizer {
  async analyzeSlowEndpoints() {
    const slowRequests = await this.getRequestHistory({
      search: [{ "duration|>|": 1.0 }],
      include_output: true
    });
    
    const analysis = this.groupByEndpoint(slowRequests);
    
    return Object.entries(analysis).map(([endpoint, data]) => ({
      endpoint,
      avgDuration: data.avgDuration,
      requestCount: data.count,
      recommendations: this.generateOptimizationTips(data)
    }));
  }
  
  generateOptimizationTips(endpointData) {
    const tips = [];
    
    if (endpointData.avgDuration > 3.0) {
      tips.push("Consider adding database indexes");
      tips.push("Review N+1 query patterns");
    }
    
    if (endpointData.count > 1000) {
      tips.push("Implement caching strategy");
      tips.push("Consider response pagination");
    }
    
    return tips;
  }
}
```

### Use Case 2: User Behavior Analytics

```javascript
// Track user interaction patterns
class UserBehaviorAnalyzer {
  async analyzeUserJourneys() {
    const userRequests = await this.getRequestHistory({
      search: [
        {
          "created_at|>=|": Date.now() - (7 * 24 * 60 * 60 * 1000) // Last week
        }
      ],
      sort: { "created_at": "asc" }
    });
    
    const journeys = this.groupByUser(userRequests);
    
    return this.identifyCommonPaths(journeys);
  }
  
  identifyCommonPaths(userJourneys) {
    const pathCounts = {};
    
    Object.values(userJourneys).forEach(journey => {
      const path = journey.map(req => req.path).join(' → ');
      pathCounts[path] = (pathCounts[path] || 0) + 1;
    });
    
    return Object.entries(pathCounts)
      .sort(([,a], [,b]) => b - a)
      .slice(0, 10);
  }
}
```

### Use Case 3: Security Monitoring

```javascript
// Monitor for suspicious activity
class SecurityMonitor {
  async detectAnomalies() {
    const recentRequests = await this.getRequestHistory({
      search: [
        {
          "created_at|>=|": Date.now() - (60 * 60 * 1000) // Last hour
        }
      ]
    });
    
    return {
      bruteForceAttempts: this.detectBruteForce(recentRequests),
      unusualPatterns: this.detectUnusualPatterns(recentRequests),
      blockedIPs: this.detectBlockedIPs(recentRequests)
    };
  }
  
  detectBruteForce(requests) {
    const loginAttempts = requests.filter(r => 
      r.path.includes('login') && r.status === 401
    );
    
    const ipCounts = {};
    loginAttempts.forEach(req => {
      ipCounts[req.ip_address] = (ipCounts[req.ip_address] || 0) + 1;
    });
    
    return Object.entries(ipCounts)
      .filter(([ip, count]) => count > 10)
      .map(([ip, count]) => ({ ip, attempts: count }));
  }
}
```

## 💡 **Try This**

### Beginner Challenge
Create a basic performance monitor that:
1. Queries request history every 5 minutes
2. Calculates average response time
3. Sends email alert if > 2 seconds
4. Logs metrics to a file

### Intermediate Challenge
Build an error tracking dashboard that:
1. Groups errors by endpoint and status code
2. Shows error trends over time
3. Provides detailed error examples
4. Enables drill-down analysis

### Advanced Challenge
Design a comprehensive monitoring system that:
1. Tracks multiple performance metrics
2. Predicts performance issues
3. Automatically scales resources
4. Generates optimization recommendations

## Common Mistakes to Avoid

1. **Not limiting result size** - Always use pagination
2. **Including output unnecessarily** - Slows down queries significantly
3. **No caching strategy** - Raw queries can be expensive
4. **Ignoring time zones** - Timestamps are in UTC
5. **Missing error handling** - History queries can fail

## Performance Tips

### Optimizing Queries

```javascript
// ✅ Good - Focused query
const recentErrors = await getHistory({
  workspace_id: 12345,
  search: [
    {
      "status|>=|": 400,
      "created_at|>=|": Date.now() - (60 * 60 * 1000)
    }
  ],
  per_page: 100,
  include_output: false // Faster
});

// ❌ Bad - Broad query
const allHistory = await getHistory({
  workspace_id: 12345,
  include_output: true, // Slow
  per_page: 500 // Too large
});
```

### Caching Strategies

```javascript
// Cache frequently accessed metrics
class HistoryCache {
  constructor() {
    this.cache = new Map();
    this.ttl = 5 * 60 * 1000; // 5 minutes
  }
  
  async getMetrics(key, fetcher) {
    const cached = this.cache.get(key);
    
    if (cached && Date.now() - cached.timestamp < this.ttl) {
      return cached.data;
    }
    
    const data = await fetcher();
    this.cache.set(key, {
      data,
      timestamp: Date.now()
    });
    
    return data;
  }
}
```

## Next Steps

- Learn about [Search Operations](search.md) for content filtering
- Explore [Token Scopes](token-scopes-reference.md) for security
- Master [Workspace Management](workspace-import-and-export.md)
- Understand [Content Management](content.md) for data operations

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - Monitoring discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step guides  
- 📖 [Metadata API Docs](master-metadata-api.md) - Complete reference
- 🔧 [Support](https://xano.com/support) - Technical assistance