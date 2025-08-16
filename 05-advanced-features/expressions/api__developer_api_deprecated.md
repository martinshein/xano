---
title: Developer API (Deprecated) - Legacy API Management and Migration
description: Guide to the deprecated Developer API in Xano, migration strategies to modern APIs, and maintaining legacy integrations for no-code platforms
category: expressions
difficulty: intermediate
last_updated: '2025-01-16'
related_docs:
  - api__master_metadata_api.md
  - advanced_back_end_features.md
  - configuring-expressions.md
subcategory: 05-advanced-features/expressions
tags:
  - deprecated-api
  - legacy-systems
  - api-migration
  - developer-tools
  - backwards-compatibility
  - no-code
---

## 📋 **Quick Summary**

The Developer API in Xano has been deprecated in favor of more modern and secure API management solutions. This guide helps existing users understand the deprecation timeline, migrate to current APIs, and maintain legacy integrations while transitioning to modern alternatives with n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- Understanding the Developer API deprecation and its implications
- Migration strategies from deprecated APIs to modern alternatives
- Maintaining backwards compatibility during transition periods
- Best practices for updating no-code platform integrations
- Timeline and support for legacy API endpoints
- Modern API alternatives and their advantages

# Developer API (Deprecated)

## Overview

The **Developer API** was a legacy endpoint management system in Xano that provided programmatic access to instance configuration and workspace management. This API has been **deprecated** and replaced with more modern, secure, and feature-rich alternatives including the Master Metadata API and enhanced function stack capabilities.

### Deprecation Status

**Current Status:** ⚠️ **DEPRECATED**
**End of Support:** Check official Xano documentation for timeline
**Migration Required:** Yes, for continued functionality
**Legacy Access:** Limited support during transition period

### Why the Developer API Was Deprecated

**Security Improvements:**
- Enhanced authentication and authorization mechanisms
- Better rate limiting and access control
- Improved audit logging and monitoring capabilities
- Stronger data validation and sanitization

**Performance Enhancements:**
- More efficient API endpoints and response formats
- Better caching and optimization strategies
- Reduced latency and improved reliability
- Scalable architecture for growing applications

**Feature Limitations:**
- Limited functionality compared to modern alternatives
- Outdated response formats and data structures
- Lack of real-time capabilities and event-driven features
- Missing integration with newer Xano features

## 🔄 **Migration Strategies**

### Assessing Current Usage

**Step 1: Inventory Existing Integrations**

```javascript
// Example script to identify Developer API usage
const auditDeveloperAPIUsage = {
  endpoints_to_check: [
    '/developer/workspaces',
    '/developer/instances',
    '/developer/schemas',
    '/developer/backups',
    '/developer/deployments'
  ],
  
  migration_mapping: {
    '/developer/workspaces': {
      new_endpoint: '/metadata/workspaces',
      api_type: 'Master Metadata API',
      changes: 'Enhanced response format with additional metadata'
    },
    '/developer/instances': {
      new_endpoint: '/metadata/instances',
      api_type: 'Master Metadata API',
      changes: 'Improved authentication and access control'
    },
    '/developer/schemas': {
      new_endpoint: '/metadata/database/schema',
      api_type: 'Master Metadata API',
      changes: 'Real-time schema updates and validation'
    }
  }
};

// Usage assessment function
function assessCurrentUsage(integrationList) {
  const migrationPlan = {};
  
  integrationList.forEach(integration => {
    if (integration.endpoints.some(endpoint => endpoint.includes('/developer/'))) {
      migrationPlan[integration.name] = {
        priority: 'high',
        estimated_effort: calculateMigrationEffort(integration),
        recommended_timeline: '30-60 days',
        breaking_changes: identifyBreakingChanges(integration)
      };
    }
  });
  
  return migrationPlan;
}
```

### n8n Migration Example

```javascript
// n8n workflow migration from Developer API to Master Metadata API
{
  "nodes": [
    {
      "name": "Legacy API Check",
      "type": "Code",
      "parameters": {
        "jsCode": `
          // Check if using deprecated Developer API endpoints
          const legacyEndpoints = [
            '/developer/workspaces',
            '/developer/instances',
            '/developer/schemas'
          ];
          
          const currentEndpoint = $env.XANO_ENDPOINT;
          const isLegacy = legacyEndpoints.some(endpoint => 
            currentEndpoint.includes(endpoint)
          );
          
          if (isLegacy) {
            // Map to new endpoints
            const endpointMapping = {
              '/developer/workspaces': '/metadata/workspaces',
              '/developer/instances': '/metadata/instances',
              '/developer/schemas': '/metadata/database/schema'
            };
            
            const newEndpoint = Object.keys(endpointMapping).reduce((result, oldPath) => {
              return result.replace(oldPath, endpointMapping[oldPath]);
            }, currentEndpoint);
            
            return [{
              json: {
                is_legacy: true,
                old_endpoint: currentEndpoint,
                new_endpoint: newEndpoint,
                migration_required: true,
                deprecation_warning: 'Developer API is deprecated. Please migrate to Master Metadata API.'
              }
            }];
          }
          
          return [{
            json: {
              is_legacy: false,
              endpoint: currentEndpoint,
              migration_required: false
            }
          }];
        `
      }
    },
    {
      "name": "Modern API Call",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com{{ $json.new_endpoint || $json.endpoint }}",
        "method": "GET",
        "headers": {
          "Authorization": "Bearer {{ $env.XANO_API_KEY }}",
          "Content-Type": "application/json",
          "X-Migration-Source": "developer-api-deprecated"
        }
      }
    },
    {
      "name": "Handle Response Format",
      "type": "Code",
      "parameters": {
        "jsCode": `
          const response = $input.first().json;
          const migrationInfo = $('Legacy API Check').first().json;
          
          // Handle different response formats between old and new APIs
          if (migrationInfo.is_legacy && migrationInfo.migration_required) {
            // Transform new API response to match expected legacy format
            const transformedResponse = transformToLegacyFormat(response);
            
            return [{
              json: {
                ...transformedResponse,
                _migration_info: {
                  api_version: 'v2_metadata',
                  migrated_from: 'developer_api',
                  migration_timestamp: new Date().toISOString()
                }
              }
            }];
          }
          
          return [{ json: response }];
          
          function transformToLegacyFormat(newResponse) {
            // Transform new response format to maintain compatibility
            if (newResponse.metadata && newResponse.data) {
              return {
                ...newResponse.data,
                metadata: newResponse.metadata
              };
            }
            return newResponse;
          }
        `
      }
    },
    {
      "name": "Log Migration Event",
      "type": "HTTP Request",
      "parameters": {
        "url": "{{ $env.MIGRATION_LOG_ENDPOINT }}",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $env.LOG_API_KEY }}",
          "Content-Type": "application/json"
        },
        "body": {
          "event_type": "api_migration_usage",
          "old_endpoint": "{{ $('Legacy API Check').first().json.old_endpoint }}",
          "new_endpoint": "{{ $('Legacy API Check').first().json.new_endpoint }}",
          "migration_status": "{{ $('Legacy API Check').first().json.migration_required ? 'pending' : 'completed' }}",
          "timestamp": "{{ new Date().toISOString() }}",
          "workflow_id": "{{ $workflow.id }}"
        }
      }
    }
  ]
}
```

### WeWeb Integration Migration

```javascript
// WeWeb component for handling Developer API migration
class DeveloperAPIMigration {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
    this.migrationMap = this.initializeMigrationMap();
    this.migrationStatus = this.loadMigrationStatus();
  }
  
  initializeMigrationMap() {
    return {
      '/developer/workspaces': {
        newEndpoint: '/metadata/workspaces',
        responseTransform: 'workspaceFormat',
        breaking_changes: ['workspace_id format changed', 'additional metadata fields']
      },
      '/developer/instances': {
        newEndpoint: '/metadata/instances',
        responseTransform: 'instanceFormat',
        breaking_changes: ['instance status enum values updated']
      },
      '/developer/schemas': {
        newEndpoint: '/metadata/database/schema',
        responseTransform: 'schemaFormat',
        breaking_changes: ['relationship format enhanced', 'field type validation improved']
      },
      '/developer/backups': {
        newEndpoint: '/metadata/backups',
        responseTransform: 'backupFormat',
        breaking_changes: ['backup metadata structure changed']
      }
    };
  }
  
  loadMigrationStatus() {
    return JSON.parse(localStorage.getItem('xano_migration_status') || '{}');
  }
  
  saveMigrationStatus() {
    localStorage.setItem('xano_migration_status', JSON.stringify(this.migrationStatus));
  }
  
  async makeAPICall(endpoint, options = {}) {
    try {
      // Check if endpoint is deprecated
      const migration = this.migrationMap[endpoint];
      
      if (migration) {
        // Log usage of deprecated endpoint
        this.logDeprecatedUsage(endpoint);
        
        // Use new endpoint if migration is enabled
        if (this.migrationStatus[endpoint]?.migrated) {
          endpoint = migration.newEndpoint;
        } else {
          // Show migration warning
          this.showMigrationWarning(endpoint, migration);
        }
      }
      
      const response = await fetch(`${this.baseUrl}/api${endpoint}`, {
        method: options.method || 'GET',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json',
          'X-Migration-Source': migration ? 'developer-api-deprecated' : 'direct',
          ...options.headers
        },
        body: options.body ? JSON.stringify(options.body) : undefined
      });
      
      let data = await response.json();
      
      // Transform response if needed for backwards compatibility
      if (migration && migration.responseTransform) {
        data = this.transformResponse(data, migration.responseTransform);
      }
      
      // Update WeWeb variables
      if (data) {
        wwLib.wwVariable.updateValue('api_response', data);
        wwLib.wwVariable.updateValue('last_api_call', {
          endpoint: endpoint,
          migrated: !!migration,
          timestamp: new Date().toISOString()
        });
      }
      
      return data;
    } catch (error) {
      console.error('API call failed:', error);
      wwLib.wwUtils.showErrorToast('API call failed. Check migration status.');
      return null;
    }
  }
  
  transformResponse(data, transformType) {
    switch (transformType) {
      case 'workspaceFormat':
        // Transform new workspace format to legacy format
        if (data.workspaces) {
          return data.workspaces.map(workspace => ({
            id: workspace.workspace_id,
            name: workspace.display_name,
            status: workspace.status,
            // Map other fields as needed
            ...workspace.metadata
          }));
        }
        break;
        
      case 'instanceFormat':
        // Transform new instance format to legacy format
        if (data.instances) {
          return data.instances.map(instance => ({
            instance_id: instance.id,
            instance_name: instance.name,
            region: instance.deployment_region,
            status: this.mapInstanceStatus(instance.status)
          }));
        }
        break;
        
      case 'schemaFormat':
        // Transform new schema format to legacy format
        if (data.schema) {
          return {
            tables: data.schema.tables.map(table => ({
              table_id: table.id,
              table_name: table.name,
              fields: table.columns.map(col => ({
                field_id: col.id,
                field_name: col.name,
                field_type: col.data_type,
                required: col.nullable === false
              }))
            }))
          };
        }
        break;
        
      default:
        return data;
    }
    
    return data;
  }
  
  mapInstanceStatus(newStatus) {
    // Map new status values to legacy values
    const statusMap = {
      'running': 'active',
      'stopped': 'inactive',
      'maintenance': 'updating',
      'error': 'failed'
    };
    
    return statusMap[newStatus] || newStatus;
  }
  
  logDeprecatedUsage(endpoint) {
    const usage = this.migrationStatus[endpoint] || { count: 0, last_used: null };
    usage.count += 1;
    usage.last_used = new Date().toISOString();
    this.migrationStatus[endpoint] = usage;
    this.saveMigrationStatus();
    
    // Send analytics
    if (typeof gtag !== 'undefined') {
      gtag('event', 'deprecated_api_usage', {
        endpoint: endpoint,
        usage_count: usage.count
      });
    }
  }
  
  showMigrationWarning(endpoint, migration) {
    if (!this.migrationStatus[endpoint]?.warning_dismissed) {
      const message = `
        ⚠️ Deprecated API Usage Detected
        
        Endpoint: ${endpoint}
        New Endpoint: ${migration.newEndpoint}
        
        This API will be discontinued. Please migrate to the new endpoint.
      `;
      
      wwLib.wwUtils.showWarningToast(message);
      
      // Store warning shown status
      this.migrationStatus[endpoint] = {
        ...this.migrationStatus[endpoint],
        warning_shown: true,
        warning_timestamp: new Date().toISOString()
      };
      this.saveMigrationStatus();
    }
  }
  
  async enableMigration(endpoint) {
    if (this.migrationMap[endpoint]) {
      this.migrationStatus[endpoint] = {
        ...this.migrationStatus[endpoint],
        migrated: true,
        migration_date: new Date().toISOString()
      };
      this.saveMigrationStatus();
      
      wwLib.wwUtils.showSuccessToast(`Migration enabled for ${endpoint}`);
      wwLib.wwVariable.updateValue('migration_status', this.migrationStatus);
    }
  }
  
  getMigrationReport() {
    const report = {
      total_deprecated_endpoints: Object.keys(this.migrationMap).length,
      migrated_endpoints: 0,
      pending_migrations: [],
      usage_statistics: {}
    };
    
    Object.keys(this.migrationMap).forEach(endpoint => {
      const status = this.migrationStatus[endpoint];
      
      if (status?.migrated) {
        report.migrated_endpoints += 1;
      } else if (status?.count > 0) {
        report.pending_migrations.push({
          endpoint: endpoint,
          usage_count: status.count,
          last_used: status.last_used,
          new_endpoint: this.migrationMap[endpoint].newEndpoint
        });
      }
      
      report.usage_statistics[endpoint] = {
        usage_count: status?.count || 0,
        migrated: status?.migrated || false
      };
    });
    
    return report;
  }
}

// Initialize migration helper
const apiMigration = new DeveloperAPIMigration(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

// Usage functions
async function fetchWorkspaces() {
  return await apiMigration.makeAPICall('/developer/workspaces');
}

async function fetchInstances() {
  return await apiMigration.makeAPICall('/developer/instances');
}

async function migrateEndpoint() {
  const endpoint = wwLib.wwVariable.getValue('endpoint_to_migrate');
  await apiMigration.enableMigration(endpoint);
}

async function generateMigrationReport() {
  const report = apiMigration.getMigrationReport();
  wwLib.wwVariable.updateValue('migration_report', report);
}
```

## 🔧 **Backwards Compatibility**

### Transition Period Support

**Graceful Degradation Strategy:**
- Maintain existing integrations during migration period
- Provide clear deprecation warnings and timelines
- Offer response format transformation for compatibility
- Support legacy authentication methods temporarily

**Migration Timeline:**
1. **Phase 1**: Deprecation announcement and new API availability
2. **Phase 2**: Side-by-side operation with migration tools
3. **Phase 3**: Reduced support for legacy endpoints
4. **Phase 4**: Complete discontinuation of Developer API

### Alternative Solutions

**Master Metadata API:**
- Enhanced security and performance
- Real-time capabilities and event streaming
- Comprehensive workspace and instance management
- Modern authentication and authorization

**Function Stack Approach:**
- Custom API endpoints built with function stacks
- Full control over request/response handling
- Integration with all Xano features and capabilities
- Optimized for specific use cases and requirements

## 💡 **Pro Tips**

- **Migrate Early**: Start migration planning as soon as deprecation is announced
- **Test Thoroughly**: Validate all functionality with new APIs before switching
- **Monitor Usage**: Track legacy API usage to prioritize migration efforts
- **Document Changes**: Maintain detailed records of API endpoint changes
- **Plan Rollback**: Have contingency plans for migration issues
- **Communicate**: Keep team and stakeholders informed of migration progress

## 🔧 **Troubleshooting**

### Common Migration Issues

**Problem**: Legacy API endpoints returning errors  
**Solution**: Check deprecation status and migrate to Master Metadata API endpoints

**Problem**: Response format differences breaking existing code  
**Solution**: Implement response transformation layers to maintain compatibility

**Problem**: Authentication failures with legacy credentials  
**Solution**: Update to modern authentication methods and regenerate API keys

**Problem**: Performance degradation during migration  
**Solution**: Implement gradual migration and monitor API performance metrics

---

**Next Steps**: Ready to modernize your API integrations? Explore [Master Metadata API](api__master_metadata_api.md) for current alternatives or check [Advanced Backend Features](advanced_back_end_features.md) for comprehensive API management