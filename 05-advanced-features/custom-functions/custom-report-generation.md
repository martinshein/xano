---
title: Custom Report Generation - Dynamic Data Reports and Analytics
description: Complete guide to building custom reports in Xano including database views, scheduled reports, real-time analytics, and integration with dashboards and no-code platforms
category: custom-functions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - background-tasks.md
  - building-with-visual-development.md
  - database-views.md
subcategory: 05-advanced-features/custom-functions
tags:
  - reports
  - analytics
  - data-visualization
  - dashboard
  - business-intelligence
  - no-code
---

## 📋 **Quick Summary**

Custom report generation enables you to create dynamic, data-driven reports from your Xano database. Whether you need scheduled analytics reports, on-demand business intelligence, or real-time dashboards, Xano provides flexible tools for data aggregation, visualization, and distribution. Perfect for integrating with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- How to design and build custom report generation systems
- Database views for quick read-only report sharing
- Scheduled vs on-demand report generation strategies
- Advanced data aggregation and transformation techniques
- Integration patterns for dashboards and analytics platforms
- Performance optimization for large dataset reporting

# Custom Report Generation

## Overview

**Custom Report Generation** transforms raw database information into meaningful, actionable insights. Xano offers multiple approaches to report creation, from simple database views for read-only sharing to sophisticated function stacks that aggregate, transform, and distribute complex business intelligence reports.

### Report Generation Approaches

**Database Views:**
- Quick read-only report sharing
- No programming required
- Direct database table representation
- Limited customization options

**Function Stack Reports:**
- Full customization and data transformation
- Complex aggregations and calculations
- API endpoints for on-demand generation
- Background tasks for scheduled reporting

## 🚀 **Database Views for Simple Reports**

### Creating Read-Only Report Views

**Basic Database View Configuration:**

```javascript
// Database view for user analytics
{
  "view_name": "user_analytics_report",
  "description": "Monthly user registration and activity summary",
  "base_table": "users",
  "columns": [
    {
      "name": "registration_month",
      "expression": "DATE_FORMAT(created_at, '%Y-%m')",
      "alias": "Month"
    },
    {
      "name": "new_users",
      "expression": "COUNT(*)",
      "alias": "New Registrations"
    },
    {
      "name": "active_users",
      "expression": "COUNT(CASE WHEN last_login >= DATE_SUB(NOW(), INTERVAL 30 DAY) THEN 1 END)",
      "alias": "Active Users (30 days)"
    }
  ],
  "filters": [
    {
      "condition": "created_at >= DATE_SUB(NOW(), INTERVAL 12 MONTH)"
    }
  ],
  "group_by": ["DATE_FORMAT(created_at, '%Y-%m')"],
  "order_by": ["registration_month DESC"]
}
```

### Advanced Database View Patterns

**Sales Performance Dashboard View:**

```sql
-- Complex database view for sales reporting
CREATE VIEW sales_performance_report AS
SELECT 
  DATE(o.created_at) AS sale_date,
  WEEK(o.created_at) AS week_number,
  MONTH(o.created_at) AS month_number,
  YEAR(o.created_at) AS year_number,
  COUNT(o.id) AS total_orders,
  SUM(o.total_amount) AS revenue,
  AVG(o.total_amount) AS average_order_value,
  COUNT(DISTINCT o.customer_id) AS unique_customers,
  SUM(oi.quantity) AS total_items_sold,
  p.category AS product_category,
  COUNT(o.id) / COUNT(DISTINCT o.customer_id) AS orders_per_customer
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
GROUP BY 
  DATE(o.created_at),
  p.category
ORDER BY 
  sale_date DESC,
  revenue DESC;
```

## 🔗 **No-Code Platform Integration**

### n8n Report Distribution Workflows

**Automated Report Generation and Distribution:**

```javascript
// n8n workflow for automated report distribution
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "Cron",
      "parameters": {
        "cronExpression": "0 8 * * MON"
      }
    },
    {
      "name": "Generate Weekly Report",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/reports/weekly-summary",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "report_type": "weekly_business_summary",
          "date_range": {
            "start": "{{ $now.minus({ weeks: 1 }).startOf('week').toISO() }}",
            "end": "{{ $now.minus({ weeks: 1 }).endOf('week').toISO() }}"
          },
          "include_charts": true,
          "format": "pdf"
        }
      }
    },
    {
      "name": "Send to Stakeholders",
      "type": "Email",
      "parameters": {
        "to": [
          "ceo@company.com",
          "cfo@company.com",
          "operations@company.com"
        ],
        "subject": "Weekly Business Report - {{ $now.minus({ weeks: 1 }).toFormat('yyyy-MM-dd') }}",
        "message": "Please find attached the weekly business summary report.",
        "attachments": [
          {
            "name": "weekly_report.pdf",
            "data": "{{ $json.report_data }}"
          }
        ]
      }
    },
    {
      "name": "Update Report Log",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/reports/log",
        "method": "POST",
        "body": {
          "report_id": "{{ $json.report_id }}",
          "status": "distributed",
          "recipients": "{{ $json.recipients.length }}",
          "distribution_method": "email"
        }
      }
    }
  ]
}
```

### WeWeb Dashboard Integration

**Real-Time Report Dashboard:**

```javascript
// WeWeb component for interactive reporting dashboard
class XanoReportDashboard {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.refreshInterval = null;
  }
  
  async generateReport(reportType, parameters = {}) {
    try {
      const response = await fetch(`${this.baseUrl}/api/reports/generate`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          type: reportType,
          parameters: parameters,
          format: 'json'
        })
      });
      
      const report = await response.json();
      
      // Update WeWeb variables with report data
      wwLib.wwVariable.updateValue(`report_data_${reportType}`, report.data);
      wwLib.wwVariable.updateValue(`report_metadata_${reportType}`, report.metadata);
      wwLib.wwVariable.updateValue(`last_updated_${reportType}`, new Date().toISOString());
      
      return report;
    } catch (error) {
      console.error('Report generation failed:', error);
      wwLib.wwUtils.showErrorToast('Failed to generate report');
      return null;
    }
  }
  
  async getReportTypes() {
    try {
      const response = await fetch(`${this.baseUrl}/api/reports/types`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`
        }
      });
      
      const reportTypes = await response.json();
      wwLib.wwVariable.updateValue('available_report_types', reportTypes);
      
      return reportTypes;
    } catch (error) {
      console.error('Failed to fetch report types:', error);
      return [];
    }
  }
  
  async scheduleReport(reportConfig) {
    try {
      const response = await fetch(`${this.baseUrl}/api/reports/schedule`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          report_type: reportConfig.type,
          schedule: reportConfig.schedule,
          parameters: reportConfig.parameters,
          recipients: reportConfig.recipients,
          format: reportConfig.format || 'pdf'
        })
      });
      
      const result = await response.json();
      
      if (response.ok) {
        wwLib.wwUtils.showSuccessToast('Report scheduled successfully');
        this.refreshScheduledReports();
      } else {
        wwLib.wwUtils.showErrorToast(`Failed to schedule report: ${result.message}`);
      }
      
      return result;
    } catch (error) {
      console.error('Report scheduling failed:', error);
      wwLib.wwUtils.showErrorToast('Network error occurred');
      return { error: 'Scheduling failed' };
    }
  }
  
  async getScheduledReports() {
    try {
      const response = await fetch(`${this.baseUrl}/api/reports/scheduled`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`
        }
      });
      
      const scheduledReports = await response.json();
      wwLib.wwVariable.updateValue('scheduled_reports', scheduledReports);
      
      return scheduledReports;
    } catch (error) {
      console.error('Failed to fetch scheduled reports:', error);
      return [];
    }
  }
  
  async exportReport(reportData, format = 'csv') {
    try {
      const response = await fetch(`${this.baseUrl}/api/reports/export`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          data: reportData,
          format: format,
          filename: `report_${Date.now()}`
        })
      });
      
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `report.${format}`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
        wwLib.wwUtils.showSuccessToast('Report exported successfully');
      } else {
        wwLib.wwUtils.showErrorToast('Export failed');
      }
    } catch (error) {
      console.error('Export failed:', error);
      wwLib.wwUtils.showErrorToast('Export error occurred');
    }
  }
  
  startAutoRefresh(reportType, interval = 300000) { // 5 minutes default
    this.refreshInterval = setInterval(async () => {
      const parameters = wwLib.wwVariable.getValue(`report_params_${reportType}`) || {};
      await this.generateReport(reportType, parameters);
    }, interval);
  }
  
  stopAutoRefresh() {
    if (this.refreshInterval) {
      clearInterval(this.refreshInterval);
      this.refreshInterval = null;
    }
  }
}

// Initialize report dashboard
const reportDashboard = new XanoReportDashboard(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function initializeDashboard() {
  await reportDashboard.getReportTypes();
  await reportDashboard.getScheduledReports();
  
  // Start auto-refresh for main dashboard report
  reportDashboard.startAutoRefresh('dashboard_summary');
}

async function generateCustomReport() {
  const reportType = wwLib.wwVariable.getValue('selected_report_type');
  const parameters = wwLib.wwVariable.getValue('report_parameters');
  
  await reportDashboard.generateReport(reportType, parameters);
}

async function scheduleNewReport() {
  const reportConfig = {
    type: wwLib.wwVariable.getValue('schedule_report_type'),
    schedule: wwLib.wwVariable.getValue('schedule_cron'),
    parameters: wwLib.wwVariable.getValue('schedule_parameters'),
    recipients: wwLib.wwVariable.getValue('schedule_recipients'),
    format: wwLib.wwVariable.getValue('schedule_format')
  };
  
  await reportDashboard.scheduleReport(reportConfig);
}

async function exportCurrentReport() {
  const reportData = wwLib.wwVariable.getValue('current_report_data');
  const format = wwLib.wwVariable.getValue('export_format') || 'csv';
  
  await reportDashboard.exportReport(reportData, format);
}
```

## 🛠️ **Function Stack Report Generation**

### On-Demand API Report Generation

**Comprehensive Sales Report Endpoint:**

```javascript
// API endpoint function stack for sales report generation
[
  {
    "function": "create_variable",
    "name": "report_config",
    "value": {
      "report_type": "{{ request.body.report_type || 'sales_summary' }}",
      "date_range": {
        "start": "{{ request.body.start_date || (now - 2592000) }}",
        "end": "{{ request.body.end_date || now }}"
      },
      "filters": "{{ request.body.filters || {} }}",
      "group_by": "{{ request.body.group_by || 'day' }}",
      "include_charts": "{{ request.body.include_charts || false }}"
    }
  },
  {
    "function": "create_variable",
    "name": "date_grouping",
    "value": {
      "day": "%Y-%m-%d",
      "week": "%Y-%u",
      "month": "%Y-%m",
      "quarter": "CONCAT(YEAR(created_at), '-Q', QUARTER(created_at))",
      "year": "%Y"
    }
  },
  {
    "function": "query_all_records",
    "table": "orders",
    "filter": {
      "created_at": {
        "$gte": "{{ report_config.date_range.start }}",
        "$lte": "{{ report_config.date_range.end }}"
      },
      "status": "completed"
    },
    "return_as": "orders"
  },
  {
    "function": "create_variable",
    "name": "sales_summary",
    "value": {
      "total_orders": "{{ orders|length }}",
      "total_revenue": "{{ orders|sum(attribute='total_amount') }}",
      "average_order_value": "{{ orders|average(attribute='total_amount') }}",
      "unique_customers": "{{ orders|map(attribute='customer_id')|unique|length }}",
      "date_range": "{{ report_config.date_range }}"
    }
  },
  {
    "function": "create_variable",
    "name": "grouped_data",
    "value": "{{ orders|group_by('created_at|date(' + date_grouping[report_config.group_by] + ')') }}"
  },
  {
    "function": "create_variable",
    "name": "time_series_data",
    "value": []
  },
  {
    "function": "loop",
    "array": "{{ grouped_data }}",
    "operations": [
      {
        "function": "create_variable",
        "name": "period_stats",
        "value": {
          "period": "{{ item.key }}",
          "orders": "{{ item.value|length }}",
          "revenue": "{{ item.value|sum(attribute='total_amount') }}",
          "customers": "{{ item.value|map(attribute='customer_id')|unique|length }}",
          "avg_order_value": "{{ item.value|average(attribute='total_amount') }}"
        }
      },
      {
        "function": "update_variable",
        "name": "time_series_data",
        "operation": "append",
        "value": "{{ period_stats }}"
      }
    ]
  },
  {
    "function": "query_all_records",
    "table": "products",
    "join": [
      {
        "table": "order_items",
        "on": "products.id = order_items.product_id"
      },
      {
        "table": "orders",
        "on": "order_items.order_id = orders.id"
      }
    ],
    "filter": {
      "orders.created_at": {
        "$gte": "{{ report_config.date_range.start }}",
        "$lte": "{{ report_config.date_range.end }}"
      },
      "orders.status": "completed"
    },
    "select": [
      "products.name",
      "products.category",
      "SUM(order_items.quantity) as total_sold",
      "SUM(order_items.quantity * order_items.price) as revenue"
    ],
    "group_by": ["products.id", "products.name", "products.category"],
    "order_by": ["revenue DESC"],
    "limit": 20,
    "return_as": "top_products"
  },
  {
    "function": "conditional",
    "condition": "{{ report_config.include_charts }}",
    "true_branch": [
      {
        "function": "custom_function",
        "name": "generate_chart_data",
        "inputs": {
          "time_series": "{{ time_series_data }}",
          "top_products": "{{ top_products }}",
          "chart_types": ["line", "pie", "bar"]
        },
        "return_as": "chart_data"
      }
    ],
    "false_branch": [
      {
        "function": "create_variable",
        "name": "chart_data",
        "value": null
      }
    ]
  },
  {
    "function": "create_variable",
    "name": "report_output",
    "value": {
      "metadata": {
        "report_type": "{{ report_config.report_type }}",
        "generated_at": "{{ now }}",
        "date_range": "{{ report_config.date_range }}",
        "group_by": "{{ report_config.group_by }}"
      },
      "summary": "{{ sales_summary }}",
      "time_series": "{{ time_series_data }}",
      "top_products": "{{ top_products }}",
      "charts": "{{ chart_data }}"
    }
  },
  {
    "function": "add_record",
    "table": "report_generation_log",
    "data": {
      "report_type": "{{ report_config.report_type }}",
      "user_id": "{{ auth.user.id }}",
      "parameters": "{{ report_config }}",
      "generated_at": "{{ now }}",
      "execution_time": "{{ now - request.timestamp }}"
    }
  },
  {
    "function": "return_response",
    "status": 200,
    "body": "{{ report_output }}"
  }
]
```

### Scheduled Background Report Generation

**Weekly Analytics Report Background Task:**

```javascript
// Background task for weekly analytics report
[
  {
    "function": "create_variable",
    "name": "report_period",
    "value": {
      "start": "{{ now - 604800 }}",
      "end": "{{ now }}",
      "week_number": "{{ now|date('W') }}",
      "year": "{{ now|date('Y') }}"
    }
  },
  {
    "function": "custom_function",
    "name": "generate_user_analytics",
    "inputs": {
      "date_range": "{{ report_period }}"
    },
    "return_as": "user_analytics"
  },
  {
    "function": "custom_function",
    "name": "generate_revenue_analytics",
    "inputs": {
      "date_range": "{{ report_period }}"
    },
    "return_as": "revenue_analytics"
  },
  {
    "function": "custom_function",
    "name": "generate_product_analytics",
    "inputs": {
      "date_range": "{{ report_period }}"
    },
    "return_as": "product_analytics"
  },
  {
    "function": "create_variable",
    "name": "weekly_report",
    "value": {
      "report_id": "weekly_{{ report_period.year }}_W{{ report_period.week_number }}",
      "period": "{{ report_period }}",
      "user_metrics": "{{ user_analytics }}",
      "revenue_metrics": "{{ revenue_analytics }}",
      "product_metrics": "{{ product_analytics }}",
      "generated_at": "{{ now }}"
    }
  },
  {
    "function": "add_record",
    "table": "weekly_reports",
    "data": "{{ weekly_report }}"
  },
  {
    "function": "custom_function",
    "name": "format_report_email",
    "inputs": {
      "report_data": "{{ weekly_report }}",
      "template": "weekly_executive_summary"
    },
    "return_as": "formatted_email"
  },
  {
    "function": "loop",
    "array": [
      {"email": "ceo@company.com", "role": "executive"},
      {"email": "marketing@company.com", "role": "marketing"},
      {"email": "sales@company.com", "role": "sales"}
    ],
    "operations": [
      {
        "function": "custom_function",
        "name": "send_report_email",
        "inputs": {
          "recipient": "{{ item }}",
          "report_content": "{{ formatted_email }}",
          "report_data": "{{ weekly_report }}"
        },
        "execution_mode": "async"
      }
    ]
  },
  {
    "function": "external_api_request",
    "url": "{{ env.SLACK_WEBHOOK_URL }}",
    "method": "POST",
    "body": {
      "text": "📊 Weekly Report Generated",
      "blocks": [
        {
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": "*Weekly Business Report - Week {{ report_period.week_number }}*\n\n• New Users: {{ user_analytics.new_users }}\n• Revenue: ${{ revenue_analytics.total_revenue|number_format(2) }}\n• Top Product: {{ product_analytics.top_product.name }}"
          }
        }
      ]
    }
  }
]
```

## 📊 **Advanced Report Patterns**

### Multi-Source Data Aggregation

**Cross-Platform Analytics Report:**

```javascript
// Complex multi-source report generation
[
  {
    "function": "create_variable",
    "name": "data_sources",
    "value": {
      "internal": "xano_database",
      "external_apis": [
        {"name": "google_analytics", "url": "{{ env.GA_API_URL }}"},
        {"name": "stripe", "url": "{{ env.STRIPE_API_URL }}"},
        {"name": "mailchimp", "url": "{{ env.MAILCHIMP_API_URL }}"}
      ]
    }
  },
  {
    "function": "create_variable",
    "name": "consolidated_data",
    "value": {
      "website_traffic": {},
      "payment_data": {},
      "email_metrics": {},
      "app_usage": {}
    }
  },
  {
    "function": "external_api_request",
    "url": "{{ data_sources.external_apis[0].url }}/reports",
    "method": "GET",
    "headers": {
      "Authorization": "Bearer {{ env.GA_ACCESS_TOKEN }}"
    },
    "query": {
      "start_date": "{{ now - 604800 }}",
      "end_date": "{{ now }}",
      "metrics": "sessions,users,pageviews,bounce_rate"
    },
    "return_as": "ga_data"
  },
  {
    "function": "update_variable",
    "name": "consolidated_data",
    "operation": "merge",
    "value": {
      "website_traffic": "{{ ga_data }}"
    }
  },
  {
    "function": "external_api_request",
    "url": "{{ data_sources.external_apis[1].url }}/charges",
    "method": "GET",
    "headers": {
      "Authorization": "Bearer {{ env.STRIPE_SECRET_KEY }}"
    },
    "query": {
      "created[gte]": "{{ (now - 604800)|timestamp }}",
      "limit": 100
    },
    "return_as": "stripe_data"
  },
  {
    "function": "update_variable",
    "name": "consolidated_data",
    "operation": "merge",
    "value": {
      "payment_data": {
        "total_charges": "{{ stripe_data.data|length }}",
        "total_amount": "{{ stripe_data.data|sum(attribute='amount') / 100 }}",
        "successful_charges": "{{ stripe_data.data|select('status', 'succeeded')|length }}"
      }
    }
  },
  {
    "function": "query_all_records",
    "table": "user_sessions",
    "filter": {
      "created_at": {
        "$gte": "{{ now - 604800 }}",
        "$lte": "{{ now }}"
      }
    },
    "return_as": "app_sessions"
  },
  {
    "function": "update_variable",
    "name": "consolidated_data",
    "operation": "merge",
    "value": {
      "app_usage": {
        "total_sessions": "{{ app_sessions|length }}",
        "unique_users": "{{ app_sessions|map(attribute='user_id')|unique|length }}",
        "average_duration": "{{ app_sessions|average(attribute='duration_minutes') }}"
      }
    }
  },
  {
    "function": "custom_function",
    "name": "calculate_conversion_metrics",
    "inputs": {
      "website_data": "{{ consolidated_data.website_traffic }}",
      "payment_data": "{{ consolidated_data.payment_data }}",
      "app_data": "{{ consolidated_data.app_usage }}"
    },
    "return_as": "conversion_metrics"
  },
  {
    "function": "create_variable",
    "name": "comprehensive_report",
    "value": {
      "report_type": "weekly_cross_platform_analytics",
      "period": {
        "start": "{{ now - 604800 }}",
        "end": "{{ now }}"
      },
      "data_sources": "{{ data_sources }}",
      "metrics": "{{ consolidated_data }}",
      "conversions": "{{ conversion_metrics }}",
      "generated_at": "{{ now }}"
    }
  }
]
```

### Real-Time Dashboard Data

**Live Metrics API Endpoint:**

```javascript
// Real-time dashboard data endpoint
[
  {
    "function": "create_variable",
    "name": "current_metrics",
    "value": {
      "timestamp": "{{ now }}",
      "cache_duration": 60
    }
  },
  {
    "function": "query_single_record",
    "table": "cached_metrics",
    "filter": {
      "metric_type": "dashboard_summary",
      "created_at": {"$gte": "{{ now - 60 }}"}
    },
    "return_as": "cached_data"
  },
  {
    "function": "conditional",
    "condition": "{{ cached_data }}",
    "true_branch": [
      {
        "function": "return_response",
        "body": {
          "data": "{{ cached_data.metrics }}",
          "cached": true,
          "cache_age": "{{ now - cached_data.created_at }}"
        }
      }
    ]
  },
  {
    "function": "query_all_records",
    "table": "orders",
    "filter": {
      "created_at": {"$gte": "{{ now - 86400 }}"}
    },
    "return_as": "today_orders"
  },
  {
    "function": "query_all_records",
    "table": "user_sessions",
    "filter": {
      "created_at": {"$gte": "{{ now - 3600 }}"}
    },
    "return_as": "current_sessions"
  },
  {
    "function": "create_variable",
    "name": "live_metrics",
    "value": {
      "sales": {
        "today_revenue": "{{ today_orders|sum(attribute='total_amount') }}",
        "today_orders": "{{ today_orders|length }}",
        "hourly_trend": "{{ today_orders|group_by('created_at|date(\"H\")')|map_values('length') }}"
      },
      "users": {
        "active_now": "{{ current_sessions|length }}",
        "unique_today": "{{ today_orders|map(attribute='customer_id')|unique|length }}",
        "session_duration_avg": "{{ current_sessions|average(attribute='duration_minutes') }}"
      },
      "system": {
        "api_response_time": "{{ avg_response_time }}",
        "error_rate": "{{ error_rate_percent }}",
        "uptime": "{{ system_uptime }}"
      }
    }
  },
  {
    "function": "add_record",
    "table": "cached_metrics",
    "data": {
      "metric_type": "dashboard_summary",
      "metrics": "{{ live_metrics }}",
      "created_at": "{{ now }}"
    }
  },
  {
    "function": "return_response",
    "body": {
      "data": "{{ live_metrics }}",
      "cached": false,
      "generated_at": "{{ now }}"
    }
  }
]
```

## 💡 **Pro Tips**

- **Cache Expensive Reports**: Use caching for reports with complex calculations to improve performance
- **Implement Pagination**: For large datasets, always implement pagination in report APIs
- **Use Background Tasks for Heavy Reports**: Generate large reports asynchronously to avoid timeouts
- **Version Your Report APIs**: Maintain backward compatibility when changing report structures
- **Secure Sensitive Data**: Implement proper access controls for confidential business reports
- **Monitor Report Performance**: Track generation times and optimize slow queries

## 🔧 **Troubleshooting**

### Common Report Generation Issues

**Problem**: Report generation times out for large datasets  
**Solution**: Implement batch processing and move heavy reports to background tasks

**Problem**: Database views not updating with fresh data  
**Solution**: Check view refresh policies and consider materialized views for better performance

**Problem**: Charts not rendering properly in reports  
**Solution**: Validate data format and ensure chart library compatibility with generated data

**Problem**: Scheduled reports not being delivered  
**Solution**: Check background task status, email service configuration, and recipient lists

---

**Next Steps**: Ready to build comprehensive reports? Check out [Background Tasks](background-tasks.md) for scheduled reporting or explore [Building with Visual Development](building-with-visual-development.md) for complete application architecture