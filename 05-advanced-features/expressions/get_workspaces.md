---
title: Get Workspaces - Workspace and Database Schema Management
description: Complete guide to retrieving workspaces, managing database tables, and schema operations using Xano's Metadata API with comprehensive examples for no-code platforms
category: expressions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - api__master_metadata_api.md
  - create_content.md
  - search_where_id___10.md
subcategory: 05-advanced-features/expressions
tags:
  - workspace-management
  - database-schema
  - table-operations
  - metadata-api
  - workspace-api
  - no-code
---

## 📋 **Quick Summary**

The Get Workspaces API endpoint provides comprehensive workspace and database schema management capabilities. This essential Metadata API functionality enables workspace discovery, table management, schema creation, and index operations, making it the foundation for building dynamic database administration tools with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Retrieving and managing workspaces through the Metadata API
- Database table creation and modification techniques
- Schema design and field management operations
- Index creation and optimization strategies
- Bulk operations for efficient database management
- Integration patterns for automated workspace administration

# Get Workspaces and Database Management

## Overview

**Workspace Management** through the Metadata API provides programmatic access to workspace discovery, database table operations, and schema management. This comprehensive system enables you to build sophisticated database administration interfaces and automated workspace management tools.

### API Structure

**Core Endpoints:**
- **Get Workspaces**: `/api/metadata/workspaces` - Retrieve all accessible workspaces
- **Get Tables**: `/api/metadata/workspaces/{id}/tables` - List tables in a workspace
- **Table Operations**: `/api/metadata/tables` - Create, modify, and manage tables
- **Schema Management**: `/api/metadata/tables/{id}/schema` - Manage table schema
- **Index Operations**: `/api/metadata/tables/{id}/indexes` - Create and manage indexes

## 🏗️ **Workspace Discovery and Management**

### Basic Workspace Retrieval

**API Endpoint**: `GET /api/metadata/workspaces`

**Response Format:**
```json
[
  {
    "id": "workspace_uuid_1",
    "name": "Production Environment",
    "description": "Main production workspace",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2025-01-16T08:45:00Z",
    "status": "active",
    "region": "us-east-1",
    "plan": "professional",
    "table_count": 15,
    "api_endpoint_count": 28
  },
  {
    "id": "workspace_uuid_2", 
    "name": "Development Environment",
    "description": "Development and testing workspace",
    "created_at": "2024-02-20T14:20:00Z",
    "updated_at": "2025-01-16T09:30:00Z",
    "status": "active",
    "region": "us-west-2",
    "plan": "starter",
    "table_count": 8,
    "api_endpoint_count": 12
  }
]
```

### n8n Workspace Management Workflow

```javascript
// n8n workflow for comprehensive workspace and schema management
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
          "Content-Type": "application/json"
        }
      }
    },
    {
      "name": "Process Workspace Data",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const workspaces = $input.first().json;
          
          // Process and enrich workspace information
          const processedWorkspaces = workspaces.map(workspace => {
            // Calculate workspace metrics
            const metrics = {
              table_density: workspace.table_count / (workspace.api_endpoint_count || 1),
              last_activity_days: Math.floor(
                (Date.now() - new Date(workspace.updated_at).getTime()) / (1000 * 60 * 60 * 24)
              ),
              plan_tier: getPlanTier(workspace.plan),
              resource_utilization: calculateResourceScore(workspace)
            };
            
            // Determine workspace health
            const health = {
              status: workspace.status,
              health_score: calculateHealthScore(workspace, metrics),
              recommendations: generateRecommendations(workspace, metrics)
            };
            
            return {
              ...workspace,
              metrics: metrics,
              health: health,
              management_actions: getAvailableActions(workspace, health)
            };
          });
          
          // Calculate summary statistics
          const summary = {
            total_workspaces: processedWorkspaces.length,
            active_workspaces: processedWorkspaces.filter(w => w.status === 'active').length,
            total_tables: processedWorkspaces.reduce((sum, w) => sum + w.table_count, 0),
            total_endpoints: processedWorkspaces.reduce((sum, w) => sum + w.api_endpoint_count, 0),
            average_health_score: processedWorkspaces.reduce((sum, w) => sum + w.health.health_score, 0) / processedWorkspaces.length,
            regions: [...new Set(processedWorkspaces.map(w => w.region))],
            plans: processedWorkspaces.reduce((acc, w) => {
              acc[w.plan] = (acc[w.plan] || 0) + 1;
              return acc;
            }, {})
          };
          
          function getPlanTier(plan) {
            const tiers = { starter: 1, professional: 2, enterprise: 3 };
            return tiers[plan] || 0;
          }
          
          function calculateResourceScore(workspace) {
            // Simple scoring based on table and endpoint counts
            const tableScore = Math.min(workspace.table_count / 20, 1) * 40;
            const endpointScore = Math.min(workspace.api_endpoint_count / 50, 1) * 40;
            const activityScore = workspace.status === 'active' ? 20 : 0;
            return Math.round(tableScore + endpointScore + activityScore);
          }
          
          function calculateHealthScore(workspace, metrics) {
            let score = 100;
            
            // Deduct points for issues
            if (workspace.status !== 'active') score -= 30;
            if (metrics.last_activity_days > 30) score -= 20;
            if (metrics.table_density > 3) score -= 10; // Too many endpoints per table
            if (metrics.table_density < 0.5) score -= 5; // Too few endpoints per table
            
            return Math.max(0, score);
          }
          
          function generateRecommendations(workspace, metrics) {
            const recommendations = [];
            
            if (metrics.last_activity_days > 30) {
              recommendations.push({
                type: 'activity',
                priority: 'medium',
                message: 'Workspace has been inactive for over 30 days',
                action: 'Review and update workspace or consider archiving'
              });
            }
            
            if (metrics.table_density > 3) {
              recommendations.push({
                type: 'architecture',
                priority: 'low',
                message: 'High endpoint-to-table ratio detected',
                action: 'Consider consolidating similar endpoints or reviewing API design'
              });
            }
            
            if (workspace.table_count > 25) {
              recommendations.push({
                type: 'performance',
                priority: 'medium',
                message: 'Large number of tables may impact performance',
                action: 'Review table usage and consider archiving unused tables'
              });
            }
            
            return recommendations;
          }
          
          function getAvailableActions(workspace, health) {
            const actions = ['view_details', 'get_tables', 'create_table'];
            
            if (health.health_score < 70) {
              actions.push('optimize_workspace');
            }
            
            if (workspace.status === 'active') {
              actions.push('backup_workspace', 'export_schema');
            }
            
            return actions;
          }
          
          return [{
            json: {
              workspaces: processedWorkspaces,
              summary: summary,
              timestamp: new Date().toISOString()
            }
          }];
        `
      }
    },
    {
      "name": "Get Workspace Tables",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/metadata/workspaces/{{ $json.workspaces[0].id }}/tables",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_METADATA_API_KEY }}",
          "Content-Type": "application/json"
        }
      }
    },
    {
      "name": "Analyze Table Structure",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const tables = $input.first().json;
          const workspaceData = $('Process Workspace Data').first().json;
          
          // Analyze table structure and relationships
          const tableAnalysis = tables.map(table => {
            const analysis = {
              table_id: table.id,
              table_name: table.name,
              field_count: table.schema?.length || 0,
              has_relationships: (table.relationships?.length || 0) > 0,
              relationship_count: table.relationships?.length || 0,
              index_count: table.indexes?.length || 0,
              estimated_size: table.metadata?.estimated_rows || 0,
              last_modified: table.updated_at,
              field_types: analyzeFieldTypes(table.schema || []),
              schema_issues: validateSchema(table.schema || []),
              optimization_suggestions: generateOptimizationSuggestions(table)
            };
            
            return analysis;
          });
          
          // Generate overall schema health report
          const schemaReport = {
            total_tables: tables.length,
            total_fields: tableAnalysis.reduce((sum, t) => sum + t.field_count, 0),
            total_relationships: tableAnalysis.reduce((sum, t) => sum + t.relationship_count, 0),
            total_indexes: tableAnalysis.reduce((sum, t) => sum + t.index_count, 0),
            tables_with_issues: tableAnalysis.filter(t => t.schema_issues.length > 0).length,
            field_type_distribution: calculateFieldTypeDistribution(tableAnalysis),
            recommendations: generateSchemaRecommendations(tableAnalysis)
          };
          
          function analyzeFieldTypes(schema) {
            const types = {};
            schema.forEach(field => {
              types[field.type] = (types[field.type] || 0) + 1;
            });
            return types;
          }
          
          function validateSchema(schema) {
            const issues = [];
            
            // Check for primary key
            const hasPrimaryKey = schema.some(field => field.is_primary_key);
            if (!hasPrimaryKey) {
              issues.push({
                type: 'missing_primary_key',
                severity: 'high',
                message: 'Table lacks a primary key field'
              });
            }
            
            // Check for timestamp fields
            const hasTimestamps = schema.some(field => field.name === 'created_at') &&
                                schema.some(field => field.name === 'updated_at');
            if (!hasTimestamps) {
              issues.push({
                type: 'missing_timestamps',
                severity: 'medium',
                message: 'Table lacks created_at/updated_at timestamp fields'
              });
            }
            
            // Check for overly long field names
            const longFieldNames = schema.filter(field => field.name.length > 50);
            if (longFieldNames.length > 0) {
              issues.push({
                type: 'long_field_names',
                severity: 'low',
                message: \`\${longFieldNames.length} fields have excessively long names\`,
                fields: longFieldNames.map(f => f.name)
              });
            }
            
            return issues;
          }
          
          function generateOptimizationSuggestions(table) {
            const suggestions = [];
            
            if ((table.indexes?.length || 0) === 0 && (table.metadata?.estimated_rows || 0) > 1000) {
              suggestions.push({
                type: 'indexing',
                priority: 'medium',
                message: 'Consider adding indexes for frequently queried fields',
                action: 'Add appropriate indexes to improve query performance'
              });
            }
            
            if ((table.relationships?.length || 0) === 0 && (table.schema?.length || 0) > 5) {
              suggestions.push({
                type: 'relationships',
                priority: 'low',
                message: 'Table has no relationships but has multiple fields',
                action: 'Review if data should be normalized into related tables'
              });
            }
            
            return suggestions;
          }
          
          function calculateFieldTypeDistribution(tableAnalysis) {
            const distribution = {};
            tableAnalysis.forEach(table => {
              Object.entries(table.field_types).forEach(([type, count]) => {
                distribution[type] = (distribution[type] || 0) + count;
              });
            });
            return distribution;
          }
          
          function generateSchemaRecommendations(tableAnalysis) {
            const recommendations = [];
            
            const tablesWithoutIndexes = tableAnalysis.filter(t => t.index_count === 0);
            if (tablesWithoutIndexes.length > 0) {
              recommendations.push({
                category: 'performance',
                priority: 'medium',
                title: 'Add database indexes',
                description: \`\${tablesWithoutIndexes.length} tables lack indexes for query optimization\`,
                tables: tablesWithoutIndexes.map(t => t.table_name)
              });
            }
            
            const tablesWithIssues = tableAnalysis.filter(t => t.schema_issues.length > 0);
            if (tablesWithIssues.length > 0) {
              recommendations.push({
                category: 'schema_health',
                priority: 'high',
                title: 'Address schema issues',
                description: \`\${tablesWithIssues.length} tables have schema validation issues\`,
                tables: tablesWithIssues.map(t => ({ name: t.table_name, issues: t.schema_issues }))
              });
            }
            
            return recommendations;
          }
          
          return [{
            json: {
              workspace_data: workspaceData,
              table_analysis: tableAnalysis,
              schema_report: schemaReport,
              analysis_timestamp: new Date().toISOString()
            }
          }];
        `
      }
    },
    {
      "name": "Create New Table with Schema",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/metadata/tables",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_METADATA_API_KEY }}",
          "Content-Type": "application/json",
          "X-Workspace-ID": "{{ $json.workspace_data.workspaces[0].id }}"
        },
        "body": {
          "name": "{{ $env.NEW_TABLE_NAME || 'products' }}",
          "description": "{{ $env.NEW_TABLE_DESCRIPTION || 'Product catalog table' }}",
          "schema": [
            {
              "name": "id",
              "type": "integer",
              "is_primary_key": true,
              "auto_increment": true,
              "nullable": false
            },
            {
              "name": "created_at",
              "type": "timestamp",
              "default": "CURRENT_TIMESTAMP",
              "nullable": false
            },
            {
              "name": "updated_at", 
              "type": "timestamp",
              "default": "CURRENT_TIMESTAMP",
              "on_update": "CURRENT_TIMESTAMP",
              "nullable": false
            },
            {
              "name": "name",
              "type": "text",
              "nullable": false,
              "max_length": 255
            },
            {
              "name": "description",
              "type": "text",
              "nullable": true
            },
            {
              "name": "price",
              "type": "decimal",
              "precision": 10,
              "scale": 2,
              "nullable": false
            },
            {
              "name": "category",
              "type": "text",
              "nullable": false,
              "max_length": 100
            },
            {
              "name": "in_stock",
              "type": "boolean",
              "default": true,
              "nullable": false
            },
            {
              "name": "tags",
              "type": "json",
              "nullable": true
            },
            {
              "name": "metadata",
              "type": "json",
              "nullable": true
            }
          ],
          "indexes": [
            {
              "type": "btree",
              "fields": ["name"],
              "unique": true,
              "name": "idx_products_name_unique"
            },
            {
              "type": "btree", 
              "fields": ["category"],
              "name": "idx_products_category"
            },
            {
              "type": "btree",
              "fields": ["price"],
              "name": "idx_products_price"
            }
          ]
        }
      }
    }
  ]
}
```

### WeWeb Workspace Management Interface

```javascript
// WeWeb component for workspace and database management
class XanoWorkspaceManager {
  constructor(xanoBaseUrl, apiKey) {
    this.baseUrl = xanoBaseUrl;
    this.apiKey = apiKey;
    this.workspaces = [];
    this.selectedWorkspace = null;
    this.tables = [];
  }
  
  async loadWorkspaces() {
    try {
      const response = await fetch(`${this.baseUrl}/api/metadata/workspaces`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        }
      });
      
      const workspaces = await response.json();
      
      // Process and enhance workspace data
      this.workspaces = workspaces.map(workspace => ({
        ...workspace,
        display_name: workspace.name || `Workspace ${workspace.id.slice(-8)}`,
        last_activity: this.calculateLastActivity(workspace.updated_at),
        health_score: this.calculateWorkspaceHealth(workspace),
        quick_stats: {
          tables: workspace.table_count || 0,
          endpoints: workspace.api_endpoint_count || 0,
          density: this.calculateDensity(workspace)
        }
      }));
      
      // Update WeWeb variables
      wwLib.wwVariable.updateValue('available_workspaces', this.workspaces);
      wwLib.wwVariable.updateValue('workspace_count', this.workspaces.length);
      
      return this.workspaces;
    } catch (error) {
      console.error('Failed to load workspaces:', error);
      wwLib.wwUtils.showErrorToast('Failed to load workspaces');
      return [];
    }
  }
  
  async selectWorkspace(workspaceId) {
    try {
      this.selectedWorkspace = this.workspaces.find(w => w.id === workspaceId);
      
      if (!this.selectedWorkspace) {
        throw new Error('Workspace not found');
      }
      
      // Load tables for the selected workspace
      await this.loadWorkspaceTables(workspaceId);
      
      wwLib.wwVariable.updateValue('selected_workspace', this.selectedWorkspace);
      wwLib.wwVariable.updateValue('workspace_tables', this.tables);
      
      return this.selectedWorkspace;
    } catch (error) {
      console.error('Failed to select workspace:', error);
      wwLib.wwUtils.showErrorToast('Failed to select workspace');
      return null;
    }
  }
  
  async loadWorkspaceTables(workspaceId) {
    try {
      const response = await fetch(`${this.baseUrl}/api/metadata/workspaces/${workspaceId}/tables`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        }
      });
      
      const tables = await response.json();
      
      // Enhance table data with analysis
      this.tables = tables.map(table => ({
        ...table,
        display_name: table.name || `Table ${table.id.slice(-8)}`,
        field_count: table.schema?.length || 0,
        relationship_count: table.relationships?.length || 0,
        index_count: table.indexes?.length || 0,
        health_score: this.calculateTableHealth(table),
        last_modified: table.updated_at,
        quick_stats: this.generateTableStats(table)
      }));
      
      wwLib.wwVariable.updateValue('workspace_tables', this.tables);
      
      return this.tables;
    } catch (error) {
      console.error('Failed to load workspace tables:', error);
      wwLib.wwUtils.showErrorToast('Failed to load tables');
      return [];
    }
  }
  
  async createTable(workspaceId, tableConfig) {
    try {
      const response = await fetch(`${this.baseUrl}/api/metadata/tables`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
          'X-Workspace-ID': workspaceId
        },
        body: JSON.stringify(tableConfig)
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwUtils.showSuccessToast(`Table "${tableConfig.name}" created successfully`);
        
        // Refresh tables list
        await this.loadWorkspaceTables(workspaceId);
        
        return result;
      } else {
        throw new Error(result.error || 'Table creation failed');
      }
    } catch (error) {
      console.error('Table creation failed:', error);
      wwLib.wwUtils.showErrorToast(`Failed to create table: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  async addTableField(tableId, fieldConfig) {
    try {
      const response = await fetch(`${this.baseUrl}/api/metadata/tables/${tableId}/schema`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(fieldConfig)
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwUtils.showSuccessToast(`Field "${fieldConfig.name}" added successfully`);
        
        // Refresh table data
        if (this.selectedWorkspace) {
          await this.loadWorkspaceTables(this.selectedWorkspace.id);
        }
        
        return result;
      } else {
        throw new Error(result.error || 'Field creation failed');
      }
    } catch (error) {
      console.error('Field creation failed:', error);
      wwLib.wwUtils.showErrorToast(`Failed to add field: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  async createIndex(tableId, indexConfig) {
    try {
      const response = await fetch(`${this.baseUrl}/api/metadata/tables/${tableId}/indexes`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(indexConfig)
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwUtils.showSuccessToast(`Index "${indexConfig.name}" created successfully`);
        
        // Refresh table data
        if (this.selectedWorkspace) {
          await this.loadWorkspaceTables(this.selectedWorkspace.id);
        }
        
        return result;
      } else {
        throw new Error(result.error || 'Index creation failed');
      }
    } catch (error) {
      console.error('Index creation failed:', error);
      wwLib.wwUtils.showErrorToast(`Failed to create index: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
  
  async browseTableContent(tableId, options = {}) {
    try {
      const queryParams = new URLSearchParams({
        page: options.page || 1,
        limit: options.limit || 50,
        sort: options.sort || 'id',
        order: options.order || 'desc'
      });
      
      const response = await fetch(`${this.baseUrl}/api/metadata/tables/${tableId}/content?${queryParams}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        }
      });
      
      const result = await response.json();
      
      if (result.success) {
        wwLib.wwVariable.updateValue('table_content', result.data);
        wwLib.wwVariable.updateValue('content_pagination', {
          current_page: result.curPage,
          total_pages: result.pageTotal,
          total_items: result.itemsTotal,
          items_received: result.itemsReceived
        });
        
        return result;
      } else {
        throw new Error(result.error || 'Failed to browse content');
      }
    } catch (error) {
      console.error('Failed to browse table content:', error);
      wwLib.wwUtils.showErrorToast('Failed to load table content');
      return { success: false, error: error.message };
    }
  }
  
  calculateLastActivity(updatedAt) {
    const now = new Date();
    const updated = new Date(updatedAt);
    const diffDays = Math.floor((now - updated) / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return 'Today';
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
    return `${Math.floor(diffDays / 30)} months ago`;
  }
  
  calculateWorkspaceHealth(workspace) {
    let score = 100;
    
    // Deduct for inactivity
    const daysSinceUpdate = Math.floor((Date.now() - new Date(workspace.updated_at)) / (1000 * 60 * 60 * 24));
    if (daysSinceUpdate > 30) score -= 20;
    if (daysSinceUpdate > 90) score -= 30;
    
    // Check table to endpoint ratio
    const density = this.calculateDensity(workspace);
    if (density < 0.5) score -= 10; // Too few endpoints
    if (density > 5) score -= 15; // Too many endpoints per table
    
    return Math.max(0, score);
  }
  
  calculateDensity(workspace) {
    if (!workspace.table_count || workspace.table_count === 0) return 0;
    return (workspace.api_endpoint_count || 0) / workspace.table_count;
  }
  
  calculateTableHealth(table) {
    let score = 100;
    
    // Check for primary key
    const hasPrimaryKey = table.schema?.some(field => field.is_primary_key);
    if (!hasPrimaryKey) score -= 30;
    
    // Check for timestamps
    const hasTimestamps = table.schema?.some(field => field.name === 'created_at') &&
                         table.schema?.some(field => field.name === 'updated_at');
    if (!hasTimestamps) score -= 20;
    
    // Check for indexes
    if (!table.indexes || table.indexes.length === 0) score -= 15;
    
    return Math.max(0, score);
  }
  
  generateTableStats(table) {
    return {
      fields: table.schema?.length || 0,
      relationships: table.relationships?.length || 0,
      indexes: table.indexes?.length || 0,
      estimated_rows: table.metadata?.estimated_rows || 0,
      health_percentage: this.calculateTableHealth(table)
    };
  }
  
  exportWorkspaceSchema() {
    if (!this.selectedWorkspace || !this.tables) {
      wwLib.wwUtils.showErrorToast('No workspace selected or tables loaded');
      return;
    }
    
    const schema = {
      workspace: {
        id: this.selectedWorkspace.id,
        name: this.selectedWorkspace.name,
        exported_at: new Date().toISOString()
      },
      tables: this.tables.map(table => ({
        name: table.name,
        description: table.description,
        schema: table.schema,
        indexes: table.indexes,
        relationships: table.relationships
      }))
    };
    
    const blob = new Blob([JSON.stringify(schema, null, 2)], { type: 'application/json' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${this.selectedWorkspace.name}_schema_${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
    
    wwLib.wwUtils.showSuccessToast('Schema exported successfully');
  }
}

// Initialize workspace manager
const workspaceManager = new XanoWorkspaceManager(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('metadata_api_key')
);

// Usage functions for WeWeb
async function loadAllWorkspaces() {
  await workspaceManager.loadWorkspaces();
}

async function selectWorkspace() {
  const workspaceId = wwLib.wwVariable.getValue('selected_workspace_id');
  await workspaceManager.selectWorkspace(workspaceId);
}

async function createNewTable() {
  const workspaceId = wwLib.wwVariable.getValue('selected_workspace_id');
  const tableConfig = wwLib.wwVariable.getValue('new_table_config');
  
  await workspaceManager.createTable(workspaceId, tableConfig);
}

async function addFieldToTable() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const fieldConfig = wwLib.wwVariable.getValue('new_field_config');
  
  await workspaceManager.addTableField(tableId, fieldConfig);
}

async function createTableIndex() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const indexConfig = wwLib.wwVariable.getValue('new_index_config');
  
  await workspaceManager.createIndex(tableId, indexConfig);
}

async function loadTableContent() {
  const tableId = wwLib.wwVariable.getValue('selected_table_id');
  const options = wwLib.wwVariable.getValue('content_load_options') || {};
  
  await workspaceManager.browseTableContent(tableId, options);
}

function exportSchema() {
  workspaceManager.exportWorkspaceSchema();
}
```

## 📋 **Database Table Operations**

### Table Creation Examples

**Basic Table Creation:**
```json
{
  "name": "users",
  "description": "User accounts table",
  "schema": [
    {
      "name": "id",
      "type": "integer",
      "is_primary_key": true,
      "auto_increment": true,
      "nullable": false
    },
    {
      "name": "email",
      "type": "text",
      "nullable": false,
      "max_length": 255
    },
    {
      "name": "created_at",
      "type": "timestamp",
      "default": "CURRENT_TIMESTAMP",
      "nullable": false
    }
  ]
}
```

**Advanced Table with Schema and Indexes:**
```json
{
  "name": "products",
  "description": "Product catalog",
  "schema": [
    {
      "name": "id",
      "type": "integer", 
      "is_primary_key": true,
      "auto_increment": true,
      "nullable": false
    },
    {
      "name": "name",
      "type": "text",
      "nullable": false,
      "max_length": 255
    },
    {
      "name": "price",
      "type": "decimal",
      "precision": 10,
      "scale": 2,
      "nullable": false
    },
    {
      "name": "category_id",
      "type": "integer",
      "nullable": false
    },
    {
      "name": "metadata",
      "type": "json",
      "nullable": true
    }
  ],
  "indexes": [
    {
      "type": "btree",
      "fields": ["name"],
      "unique": true,
      "name": "idx_products_name_unique"
    },
    {
      "type": "btree",
      "fields": ["category_id"],
      "name": "idx_products_category"
    }
  ]
}
```

### Content Browsing Response Format

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": 1,
        "name": "Premium Laptop",
        "price": 1299.99,
        "category_id": 2,
        "created_at": "2025-01-16T10:30:00Z"
      },
      {
        "id": 2,
        "name": "Wireless Mouse",
        "price": 29.99,
        "category_id": 1,
        "created_at": "2025-01-16T11:15:00Z"
      }
    ],
    "itemsReceived": 2,
    "curPage": 1,
    "nextPage": null,
    "prevPage": null,
    "offset": 0,
    "itemsTotal": 2,
    "pageTotal": 1
  }
}
```

## 💡 **Pro Tips**

- **Workspace Discovery**: Always fetch workspaces first to understand available environments
- **Schema Planning**: Design schema with proper field types, indexes, and relationships from the start
- **Index Strategy**: Create indexes on frequently queried fields for optimal performance
- **Bulk Operations**: Use comprehensive table creation with schema and indexes in single API calls
- **Health Monitoring**: Regularly assess workspace and table health metrics
- **Export Schemas**: Maintain backups of database schemas for disaster recovery

## 🔧 **Troubleshooting**

### Common Workspace Management Issues

**Problem**: Empty workspace list returned  
**Solution**: Verify API key has proper permissions and check workspace access rights

**Problem**: Table creation fails with schema errors  
**Solution**: Validate field types and ensure primary key is properly defined

**Problem**: Index creation fails  
**Solution**: Check field names exist and index type is supported for the field types

**Problem**: Content browsing returns empty results  
**Solution**: Verify table has data and check pagination parameters

---

**Next Steps**: Ready to manage workspaces effectively? Explore [Create Content](create_content.md) for record operations or check [Master Metadata API](api__master_metadata_api.md) for comprehensive API capabilities