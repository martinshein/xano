---
title: Master Metadata API - Modern API Management and Integration
description: Complete guide to Xano's Master Metadata API for workspace management, database schema access, and comprehensive instance control with no-code platforms
category: expressions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - api__developer_api_deprecated.md
  - advanced_back_end_features.md
  - allow_direct_query.md
subcategory: 05-advanced-features/expressions
tags:
  - metadata-api
  - workspace-management
  - schema-access
  - modern-api
  - integration-platform
  - no-code
---

## 📋 **Quick Summary**

The Master Metadata API is Xano's modern, comprehensive API for workspace management, database schema access, and instance control. It provides enhanced security, real-time capabilities, and extensive integration options for building sophisticated applications with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Understanding the Master Metadata API architecture and capabilities
- Workspace and instance management through programmatic access
- Database schema inspection and manipulation techniques
- Authentication and security best practices
- Integration patterns for no-code platforms
- Real-time event handling and webhook configurations

# Master Metadata API

## Overview

The **Master Metadata API** is Xano's flagship API solution for programmatic access to workspace metadata, database schemas, instance management, and system configuration. It replaces the deprecated Developer API with enhanced security, performance, and functionality designed for modern application architectures.

### API Capabilities

**Workspace Management:**
- Workspace creation, configuration, and deletion
- Team member management and permissions
- Resource allocation and monitoring
- Cross-workspace data operations

**Database Schema Access:**
- Real-time schema inspection and validation
- Table and field metadata retrieval
- Relationship mapping and constraints
- Index and performance optimization data

**Instance Control:**
- Instance status monitoring and management
- Configuration updates and deployments
- Backup and restore operations
- Performance metrics and analytics

**Integration Features:**
- Webhook management and event streaming
- External service authentication
- API key management and rotation
- Rate limiting and quota monitoring

## 🏗️ **API Architecture and Authentication**

### Modern Authentication System

**API Key Management:**
- Scoped API keys with granular permissions
- Automatic key rotation and expiration
- Role-based access control integration
- Audit logging for all API access

**Token-Based Authentication:**
```javascript
// Authentication headers for Master Metadata API
const authHeaders = {
  'Authorization': 'Bearer YOUR_API_KEY',
  'X-API-Version': 'v2',
  'Content-Type': 'application/json',
  'X-Request-ID': generateRequestId() // For request tracking
};

// Request ID generation for tracing
function generateRequestId() {
  return `req_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
}
```

### n8n Integration with Master Metadata API

```javascript
// n8n workflow for comprehensive workspace management
{
  "nodes": [
    {
      "name": "Get All Workspaces",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/metadata/workspaces",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_METADATA_API_KEY }}",
          "X-API-Version": "v2",
          "Content-Type": "application/json"
        },
        "options": {
          "response": {
            "response": {
              "neverError": true
            }
          }
        }
      }
    },
    {
      "name": "Process Workspace Data",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const workspaces = $input.first().json;
          
          // Process and enrich workspace data
          const enrichedWorkspaces = workspaces.data.map(workspace => {
            // Calculate workspace health score
            const healthScore = calculateHealthScore(workspace);
            
            // Determine workspace status
            const status = determineWorkspaceStatus(workspace);
            
            // Extract key metrics
            const metrics = {
              table_count: workspace.metadata.database_tables || 0,
              api_endpoint_count: workspace.metadata.api_endpoints || 0,
              function_stack_count: workspace.metadata.function_stacks || 0,
              last_deployment: workspace.last_deployment_timestamp,
              resource_usage: workspace.resource_utilization
            };
            
            return {
              workspace_id: workspace.id,
              workspace_name: workspace.name,
              environment: workspace.environment,
              health_score: healthScore,
              status: status,
              metrics: metrics,
              team_members: workspace.team_members || [],
              created_at: workspace.created_at,
              last_activity: workspace.last_activity_timestamp
            };
          });
          
          // Calculate summary statistics
          const summary = {
            total_workspaces: enrichedWorkspaces.length,
            active_workspaces: enrichedWorkspaces.filter(w => w.status === 'active').length,
            unhealthy_workspaces: enrichedWorkspaces.filter(w => w.health_score < 70).length,
            total_api_endpoints: enrichedWorkspaces.reduce((sum, w) => sum + w.metrics.api_endpoint_count, 0),
            avg_health_score: enrichedWorkspaces.reduce((sum, w) => sum + w.health_score, 0) / enrichedWorkspaces.length
          };
          
          function calculateHealthScore(workspace) {
            let score = 100;
            
            // Deduct points for various issues
            if (!workspace.last_deployment_timestamp) score -= 20;
            if (workspace.resource_utilization?.cpu > 80) score -= 15;
            if (workspace.resource_utilization?.memory > 80) score -= 15;
            if (workspace.error_rate > 0.05) score -= 10; // 5% error rate threshold
            if (Date.now() - new Date(workspace.last_activity_timestamp) > 7 * 24 * 60 * 60 * 1000) score -= 20; // Inactive for 7 days
            
            return Math.max(0, score);
          }
          
          function determineWorkspaceStatus(workspace) {
            if (!workspace.is_active) return 'inactive';
            if (workspace.maintenance_mode) return 'maintenance';
            if (workspace.resource_utilization?.cpu > 90 || workspace.resource_utilization?.memory > 90) return 'overloaded';
            if (workspace.error_rate > 0.1) return 'error';
            return 'active';
          }
          
          return [{
            json: {
              workspaces: enrichedWorkspaces,
              summary: summary,
              timestamp: new Date().toISOString()
            }
          }];
        `
      }
    },
    {
      "name": "Get Database Schema",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/metadata/database/schema",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_METADATA_API_KEY }}",
          "X-API-Version": "v2",
          "Content-Type": "application/json"
        },
        "qs": {
          "workspace_id": "{{ $json.workspaces[0].workspace_id }}",
          "include_relationships": "true",
          "include_indexes": "true"
        }
      }
    },
    {
      "name": "Analyze Schema Structure",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const schema = $input.first().json;
          const workspaceData = $('Process Workspace Data').first().json;
          
          // Analyze database schema for insights
          const schemaAnalysis = {
            tables: schema.tables.map(table => ({
              table_name: table.name,
              table_id: table.id,
              column_count: table.columns.length,
              has_primary_key: table.columns.some(col => col.is_primary_key),
              has_timestamps: table.columns.some(col => col.name === 'created_at') && 
                             table.columns.some(col => col.name === 'updated_at'),
              column_types: table.columns.reduce((types, col) => {
                types[col.data_type] = (types[col.data_type] || 0) + 1;
                return types;
              }, {}),
              relationships: table.relationships || [],
              indexes: table.indexes || [],
              estimated_size: table.metadata?.estimated_row_count || 0
            })),
            relationships: schema.relationships || [],
            total_tables: schema.tables.length,
            total_columns: schema.tables.reduce((sum, table) => sum + table.columns.length, 0),
            total_relationships: (schema.relationships || []).length
          };
          
          // Identify potential issues
          const schemaIssues = [];
          
          schemaAnalysis.tables.forEach(table => {
            if (!table.has_primary_key) {
              schemaIssues.push({
                type: 'missing_primary_key',
                table: table.table_name,
                severity: 'high',
                recommendation: 'Add a primary key column to improve performance'
              });
            }
            
            if (!table.has_timestamps) {
              schemaIssues.push({
                type: 'missing_timestamps',
                table: table.table_name,
                severity: 'medium',
                recommendation: 'Add created_at and updated_at columns for audit trail'
              });
            }
            
            if (table.indexes.length === 0 && table.estimated_size > 1000) {
              schemaIssues.push({
                type: 'missing_indexes',
                table: table.table_name,
                severity: 'medium',
                recommendation: 'Consider adding indexes for frequently queried columns'
              });
            }
          });
          
          return [{
            json: {
              workspace_analysis: workspaceData,
              schema_analysis: schemaAnalysis,
              schema_issues: schemaIssues,
              recommendations: generateRecommendations(schemaAnalysis, schemaIssues)
            }
          }];
          
          function generateRecommendations(analysis, issues) {
            const recommendations = [];
            
            // Performance recommendations
            if (analysis.total_tables > 20) {
              recommendations.push({
                category: 'performance',
                title: 'Consider database optimization',
                description: 'Large number of tables detected. Consider using views or consolidating related tables.',
                priority: 'medium'
              });
            }
            
            // Security recommendations
            const highSeverityIssues = issues.filter(issue => issue.severity === 'high');
            if (highSeverityIssues.length > 0) {
              recommendations.push({
                category: 'security',
                title: 'Address high-severity schema issues',
                description: \`\${highSeverityIssues.length} high-severity issues found that should be addressed immediately.\`,
                priority: 'high'
              });
            }
            
            // Best practices recommendations
            if (analysis.total_relationships / analysis.total_tables < 0.5) {
              recommendations.push({
                category: 'best_practices',
                title: 'Consider adding more relationships',
                description: 'Low relationship density detected. Adding proper relationships can improve data integrity.',
                priority: 'low'
              });
            }
            
            return recommendations;
          }
        `
      }
    },
    {
      "name": "Generate Health Report",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.HEALTH_REPORT_WEBHOOK }}",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.WEBHOOK_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": "{{ $json }}"
      }
    }
  ]
}
```

### WeWeb Master Metadata Integration

```javascript
// WeWeb component for Master Metadata API integration
class XanoMetadataManager {
  constructor(xanoBaseUrl, apiKey) {
    this.baseUrl = xanoBaseUrl;
    this.apiKey = apiKey;
    this.apiVersion = 'v2';
    this.requestCache = new Map();
    this.cacheTimeout = 300000; // 5 minutes
  }
  
  async makeRequest(endpoint, options = {}) {
    try {
      const requestId = this.generateRequestId();
      const cacheKey = `${endpoint}_${JSON.stringify(options)}`;
      
      // Check cache for GET requests
      if (options.method !== 'POST' && options.method !== 'PUT' && options.method !== 'DELETE') {
        const cached = this.requestCache.get(cacheKey);
        if (cached && Date.now() - cached.timestamp < this.cacheTimeout) {
          return cached.data;
        }
      }
      
      const response = await fetch(`${this.baseUrl}/api/metadata${endpoint}`, {
        method: options.method || 'GET',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'X-API-Version': this.apiVersion,
          'Content-Type': 'application/json',
          'X-Request-ID': requestId,
          ...options.headers
        },
        body: options.body ? JSON.stringify(options.body) : undefined
      });
      
      if (!response.ok) {
        throw new Error(`API request failed: ${response.status} ${response.statusText}`);
      }
      
      const data = await response.json();
      
      // Cache successful GET requests
      if (options.method !== 'POST' && options.method !== 'PUT' && options.method !== 'DELETE') {
        this.requestCache.set(cacheKey, {
          data: data,
          timestamp: Date.now()
        });
      }
      
      // Update WeWeb tracking variables
      wwLib.wwVariable.updateValue('last_api_request_id', requestId);
      wwLib.wwVariable.updateValue('last_api_response_time', Date.now());
      
      return data;
    } catch (error) {
      console.error('Metadata API request failed:', error);
      wwLib.wwUtils.showErrorToast(`API Error: ${error.message}`);
      throw error;
    }
  }
  
  generateRequestId() {
    return `req_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
  
  // Workspace Management Methods
  async getWorkspaces() {
    const data = await this.makeRequest('/workspaces');
    wwLib.wwVariable.updateValue('workspaces_list', data.workspaces);
    return data;
  }
  
  async getWorkspace(workspaceId) {
    const data = await this.makeRequest(`/workspaces/${workspaceId}`);
    wwLib.wwVariable.updateValue('current_workspace', data.workspace);
    return data;
  }
  
  async createWorkspace(workspaceConfig) {
    const data = await this.makeRequest('/workspaces', {
      method: 'POST',
      body: workspaceConfig
    });
    
    if (data.success) {
      wwLib.wwUtils.showSuccessToast('Workspace created successfully');
      await this.getWorkspaces(); // Refresh list
    }
    
    return data;
  }
  
  async updateWorkspace(workspaceId, updates) {
    const data = await this.makeRequest(`/workspaces/${workspaceId}`, {
      method: 'PUT',
      body: updates
    });
    
    if (data.success) {
      wwLib.wwUtils.showSuccessToast('Workspace updated successfully');
      await this.getWorkspace(workspaceId); // Refresh current workspace
    }
    
    return data;
  }
  
  // Database Schema Methods
  async getDatabaseSchema(workspaceId, options = {}) {
    const endpoint = `/database/schema`;
    const queryParams = new URLSearchParams({
      workspace_id: workspaceId,
      include_relationships: options.includeRelationships || 'true',
      include_indexes: options.includeIndexes || 'true',
      include_constraints: options.includeConstraints || 'true'
    });
    
    const data = await this.makeRequest(`${endpoint}?${queryParams}`);
    wwLib.wwVariable.updateValue('database_schema', data.schema);
    return data;
  }
  
  async getTableSchema(workspaceId, tableName) {
    const data = await this.makeRequest(`/database/tables/${tableName}`, {
      headers: {
        'X-Workspace-ID': workspaceId
      }
    });
    
    wwLib.wwVariable.updateValue('current_table_schema', data.table);
    return data;
  }
  
  async createTable(workspaceId, tableDefinition) {
    const data = await this.makeRequest('/database/tables', {
      method: 'POST',
      headers: {
        'X-Workspace-ID': workspaceId
      },
      body: tableDefinition
    });
    
    if (data.success) {
      wwLib.wwUtils.showSuccessToast(`Table "${tableDefinition.name}" created successfully`);
      await this.getDatabaseSchema(workspaceId); // Refresh schema
    }
    
    return data;
  }
  
  // Instance Management Methods
  async getInstances() {
    const data = await this.makeRequest('/instances');
    wwLib.wwVariable.updateValue('instances_list', data.instances);
    return data;
  }
  
  async getInstanceHealth(instanceId) {
    const data = await this.makeRequest(`/instances/${instanceId}/health`);
    wwLib.wwVariable.updateValue('instance_health', data.health);
    return data;
  }
  
  async getInstanceMetrics(instanceId, timeRange = '1h') {
    const data = await this.makeRequest(`/instances/${instanceId}/metrics`, {
      headers: {
        'X-Time-Range': timeRange
      }
    });
    
    wwLib.wwVariable.updateValue('instance_metrics', data.metrics);
    return data;
  }
  
  // Content and File Management
  async getContent(workspaceId, options = {}) {
    const queryParams = new URLSearchParams({
      workspace_id: workspaceId,
      content_type: options.contentType || 'all',
      limit: options.limit || '50',
      offset: options.offset || '0'
    });
    
    const data = await this.makeRequest(`/content?${queryParams}`);
    wwLib.wwVariable.updateValue('workspace_content', data.content);
    return data;
  }
  
  async uploadFile(workspaceId, file, metadata = {}) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('metadata', JSON.stringify(metadata));
    
    try {
      const response = await fetch(`${this.baseUrl}/api/metadata/files`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'X-API-Version': this.apiVersion,
          'X-Workspace-ID': workspaceId,
          'X-Request-ID': this.generateRequestId()
        },
        body: formData
      });
      
      const data = await response.json();
      
      if (data.success) {
        wwLib.wwUtils.showSuccessToast('File uploaded successfully');
        wwLib.wwVariable.updateValue('uploaded_file', data.file);
      }
      
      return data;
    } catch (error) {
      console.error('File upload failed:', error);
      wwLib.wwUtils.showErrorToast('File upload failed');
      throw error;
    }
  }
  
  // Search and Query Methods
  async searchContent(workspaceId, query, options = {}) {
    const searchData = {
      query: query,
      workspace_id: workspaceId,
      search_type: options.searchType || 'full_text',
      filters: options.filters || {},
      limit: options.limit || 25
    };
    
    const data = await this.makeRequest('/search', {
      method: 'POST',
      body: searchData
    });
    
    wwLib.wwVariable.updateValue('search_results', data.results);
    return data;
  }
  
  // Webhook and Event Management
  async getWebhooks(workspaceId) {
    const data = await this.makeRequest(`/webhooks?workspace_id=${workspaceId}`);
    wwLib.wwVariable.updateValue('webhooks_list', data.webhooks);
    return data;
  }
  
  async createWebhook(workspaceId, webhookConfig) {
    const data = await this.makeRequest('/webhooks', {
      method: 'POST',
      body: {
        ...webhookConfig,
        workspace_id: workspaceId
      }
    });
    
    if (data.success) {
      wwLib.wwUtils.showSuccessToast('Webhook created successfully');
      await this.getWebhooks(workspaceId);
    }
    
    return data;
  }
  
  // Analytics and Reporting
  async generateAnalyticsReport(workspaceId, reportType, options = {}) {
    const reportData = {
      workspace_id: workspaceId,
      report_type: reportType,
      time_range: options.timeRange || '30d',
      metrics: options.metrics || ['api_calls', 'database_operations', 'errors'],
      format: options.format || 'json'
    };
    
    const data = await this.makeRequest('/analytics/reports', {
      method: 'POST',
      body: reportData
    });
    
    wwLib.wwVariable.updateValue('analytics_report', data.report);
    return data;
  }
}

// Initialize metadata manager
const metadataAPI = new XanoMetadataManager(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('metadata_api_key')
);

// Usage functions for WeWeb
async function loadWorkspaceData() {
  const workspaces = await metadataAPI.getWorkspaces();
  const selectedWorkspaceId = wwLib.wwVariable.getValue('selected_workspace_id');
  
  if (selectedWorkspaceId) {
    await metadataAPI.getDatabaseSchema(selectedWorkspaceId);
    await metadataAPI.getContent(selectedWorkspaceId);
  }
}

async function createNewWorkspace() {
  const workspaceConfig = {
    name: wwLib.wwVariable.getValue('new_workspace_name'),
    description: wwLib.wwVariable.getValue('new_workspace_description'),
    environment: wwLib.wwVariable.getValue('new_workspace_environment'),
    template: wwLib.wwVariable.getValue('workspace_template')
  };
  
  await metadataAPI.createWorkspace(workspaceConfig);
}

async function performContentSearch() {
  const workspaceId = wwLib.wwVariable.getValue('selected_workspace_id');
  const searchQuery = wwLib.wwVariable.getValue('search_query');
  const searchOptions = {
    searchType: wwLib.wwVariable.getValue('search_type'),
    limit: wwLib.wwVariable.getValue('search_limit')
  };
  
  await metadataAPI.searchContent(workspaceId, searchQuery, searchOptions);
}

async function uploadWorkspaceFile() {
  const workspaceId = wwLib.wwVariable.getValue('selected_workspace_id');
  const fileInput = document.getElementById('file-upload');
  const file = fileInput.files[0];
  
  if (file && workspaceId) {
    const metadata = {
      category: wwLib.wwVariable.getValue('file_category'),
      tags: wwLib.wwVariable.getValue('file_tags')
    };
    
    await metadataAPI.uploadFile(workspaceId, file, metadata);
  }
}
```

## 🔗 **Real-Time Features and Webhooks**

### Event Streaming Architecture

**Supported Events:**
- Workspace creation, modification, and deletion
- Database schema changes and updates
- API endpoint deployments and modifications
- User authentication and authorization events
- System performance and health status changes

**Webhook Configuration:**
```javascript
// Webhook configuration for real-time updates
const webhookConfig = {
  url: 'https://your-webhook-endpoint.com/xano-events',
  events: [
    'workspace.created',
    'workspace.updated',
    'database.schema_changed',
    'api.endpoint_deployed',
    'system.health_alert'
  ],
  authentication: {
    type: 'bearer_token',
    token: 'your-webhook-secret'
  },
  retry_policy: {
    max_retries: 3,
    retry_delay: 5000,
    exponential_backoff: true
  },
  filters: {
    workspace_ids: ['workspace_1', 'workspace_2'],
    severity_levels: ['high', 'critical']
  }
};
```

## 💡 **Pro Tips**

- **Use Request IDs**: Always include request IDs for tracing and debugging
- **Implement Caching**: Cache metadata responses to reduce API calls
- **Handle Rate Limits**: Implement proper retry logic with exponential backoff
- **Version Management**: Always specify API version headers for consistency
- **Monitor Usage**: Track API usage and performance metrics
- **Security First**: Use scoped API keys and rotate them regularly

## 🔧 **Troubleshooting**

### Common API Issues

**Problem**: Authentication failures with valid API keys  
**Solution**: Verify API key scopes and ensure proper headers are included

**Problem**: Rate limit exceeded errors  
**Solution**: Implement proper rate limiting and retry logic in your applications

**Problem**: Schema operations failing  
**Solution**: Check workspace permissions and validate schema definitions

**Problem**: Webhook events not being received  
**Solution**: Verify webhook URL accessibility and authentication configuration

---

**Next Steps**: Ready to leverage modern API capabilities? Explore [Advanced Backend Features](advanced_back_end_features.md) for comprehensive integration or check [Allow Direct Query](allow_direct_query.md) for database management