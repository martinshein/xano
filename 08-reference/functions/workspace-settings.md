---
title: Workspace Settings - Complete Configuration and Management Guide
description: Master Xano workspace configuration including general settings, data sources, middleware management, request history, database preferences, compliance center, and team collaboration features for optimal project organization
category: functions
difficulty: intermediate
last_updated: '2025-08-17'
related_docs: []
subcategory: 08-reference/functions
tags:
- workspace-settings
- data-sources
- middleware-management
- request-history
- database-preferences
- compliance-center
- team-collaboration
- workspace-organization
- project-management
- development-workflow
---

# Workspace Settings - Complete Configuration and Management Guide

## 📋 **Quick Summary**

Workspace Settings provide comprehensive control over your Xano development environment, including project organization, data source management, middleware configuration, request logging, database preferences, and team collaboration features. Master these settings to optimize your development workflow and maintain organized, scalable projects.

## What You'll Learn

- **General Settings**: Configure workspace identity, AI preferences, and development tools
- **Data Source Management**: Set up multiple environments and data migration
- **Middleware Configuration**: Manage cross-cutting concerns and request processing
- **Request History**: Configure logging and debugging capabilities
- **Database Preferences**: Optimize database format and table management
- **Team Collaboration**: Implement workspace sharing and access control

## Understanding Workspace Settings

### Workspace Architecture Overview

```javascript
// Workspace settings architecture and organization
const workspaceArchitecture = {
  // Core workspace concepts
  workspaceStructure: {
    identity: {
      name: "Unique workspace identifier",
      description: "Project description and purpose",
      documentation: "Internal documentation tools",
      branding: "Custom workspace appearance"
    },
    
    dataOrganization: {
      dataSources: "Multiple database environments (dev, staging, prod)",
      tableStructure: "JSONB vs Standard SQL formats",
      relationships: "Cross-table relationships and constraints",
      backups: "Automated backup and restore capabilities"
    },
    
    developmentTools: {
      middleware: "Workspace-level cross-cutting concerns",
      triggers: "Event-driven automation workflows",
      requestHistory: "Comprehensive request logging and debugging",
      statementExplorer: "Code search and analysis tools"
    },
    
    collaboration: {
      teamAccess: "Multi-user workspace access",
      permissions: "Role-based access control",
      branching: "Development branch management",
      auditLogs: "Complete activity tracking"
    }
  },
  
  // Settings hierarchy
  settingsHierarchy: {
    workspaceLevel: "Global settings affecting entire workspace",
    instanceLevel: "Infrastructure and deployment settings",
    apiGroupLevel: "API organization and grouping settings",
    individualAPILevel: "Specific endpoint configurations"
  },
  
  // Configuration impact
  configurationImpact: {
    immediateChanges: ["General settings", "Middleware", "Request history"],
    dataChanges: ["Data source modifications", "Table format changes"],
    infrastructureChanges: ["Database preferences", "Table migrations"],
    teamChanges: ["Collaboration settings", "Access permissions"]
  }
};
```

### Workspace vs Instance Settings

```javascript
// Understanding the difference between workspace and instance settings
const settingsComparison = {
  // Workspace settings (project/development level)
  workspaceSettings: {
    scope: "Development environment and project organization",
    affects: "All work within the workspace",
    includes: [
      "Project identity and documentation",
      "Data source management",
      "Development tools configuration",
      "Team collaboration settings",
      "Database structure preferences"
    ],
    
    accessLevel: "Workspace owners and administrators",
    impact: "Development workflow and project organization"
  },
  
  // Instance settings (infrastructure level)
  instanceSettings: {
    scope: "Infrastructure and deployment configuration",
    affects: "Runtime performance and hosting",
    includes: [
      "Custom domain configuration",
      "Performance and scaling settings",
      "Regional deployment options",
      "Security and access policies",
      "Billing and plan management"
    ],
    
    accessLevel: "Instance owners and administrators",
    impact: "Application performance and availability"
  },
  
  // When to use which
  usageGuidelines: {
    workspaceSettings: "Configure during development and project setup",
    instanceSettings: "Configure for production deployment and scaling",
    coordination: "Both settings work together for complete application management"
  }
};
```

## General Settings Configuration

### Workspace Identity and Tools

```javascript
// Complete general settings configuration
const generalSettings = {
  // Workspace identity
  workspaceIdentity: {
    nameConfiguration: {
      purpose: "Unique identifier for the workspace",
      bestPractices: [
        "Use descriptive names that reflect the project",
        "Include environment indicators (dev, staging, prod)",
        "Consider team naming conventions",
        "Keep names concise but meaningful"
      ],
      examples: [
        "E-commerce Platform - Development",
        "Customer Portal API - Production",
        "Analytics Dashboard - Staging"
      ]
    },
    
    descriptionGuidelines: {
      purpose: "Detailed project description and context",
      contents: [
        "Project overview and objectives",
        "Key features and functionality",
        "Integration points and dependencies",
        "Team members and responsibilities"
      ],
      format: "Markdown formatting supported for rich documentation"
    }
  },
  
  // Development tools
  developmentTools: {
    internalDocumentation: {
      purpose: "Enable documentation tools within function stacks",
      benefits: [
        "Document complex business logic",
        "Provide examples and usage notes",
        "Maintain team knowledge base",
        "Support onboarding and training"
      ],
      usage: "Plain text input fields in function stack editors"
    },
    
    startPageConfiguration: {
      purpose: "Beginner guidance and workspace navigation",
      whenToEnable: "New teams or workspace contributors",
      features: [
        "Guided onboarding experience",
        "Quick access to common tasks",
        "Learning resources and tutorials",
        "Best practice recommendations"
      ]
    },
    
    marketplaceAccess: {
      purpose: "Access to snippets and extensions",
      contents: [
        "Pre-built function stack templates",
        "Common integration patterns",
        "Community-contributed solutions",
        "Third-party extensions and add-ons"
      ],
      benefits: "Accelerate development with proven solutions"
    }
  },
  
  // AI integration preferences
  aiPreferences: {
    licenseAcceptance: {
      purpose: "Enable AI-powered development features",
      features: [
        "AI Database Assistant for schema design",
        "AI Lambda Assistant for function creation",
        "AI SQL Assistant for query optimization",
        "Automated code generation and suggestions"
      ]
    },
    
    aiToolConfiguration: {
      databaseAssistant: "Natural language database schema creation",
      lambdaAssistant: "Function stack generation from descriptions",
      sqlAssistant: "Query optimization and generation",
      codeGeneration: "Automated code suggestions and completion"
    }
  }
};
```

### Configuration Best Practices

```javascript
// Best practices for general settings configuration
const configurationBestPractices = {
  // Workspace organization
  workspaceOrganization: {
    namingConventions: {
      workspaces: "ProjectName - Environment (e.g., 'ECommerce - Production')",
      consistency: "Use consistent naming across all workspaces",
      versioning: "Include version information when relevant",
      documentation: "Document naming conventions for team reference"
    },
    
    environmentSeparation: {
      development: "Separate workspace for active development",
      staging: "Testing and quality assurance workspace",
      production: "Live application workspace",
      isolation: "Keep environments completely isolated"
    }
  },
  
  // Team collaboration setup
  teamCollaborationSetup: {
    documentation: {
      enableEarly: "Enable documentation tools from project start",
      standards: "Establish documentation standards and templates",
      maintenance: "Regular documentation review and updates",
      training: "Train team members on documentation tools"
    },
    
    accessManagement: {
      principleOfLeastPrivilege: "Grant minimum necessary access",
      regularReviews: "Periodic access reviews and updates",
      roleDefinition: "Clear role definitions and responsibilities",
      onboardingOffboarding: "Streamlined access provisioning and removal"
    }
  }
};
```

## Data Source Management

### Understanding Data Sources

```javascript
// Comprehensive data source management
const dataSourceManagement = {
  // Data source concepts
  dataSourceConcepts: {
    purpose: "Maintain separate databases with identical schemas",
    useCases: [
      "Development, staging, and production environments",
      "A/B testing with different datasets",
      "Client-specific data isolation",
      "Backup and disaster recovery scenarios",
      "Testing and validation environments"
    ],
    
    schemaConsistency: "All data sources share the same table structure",
    dataIsolation: "Complete data separation between sources"
  },
  
  // Data source configuration
  dataSourceConfiguration: {
    creationProcess: {
      step1: "Navigate to Workspace Settings → Data Sources",
      step2: "Click 'Add New Data Source'",
      step3: "Configure data source name and description",
      step4: "Choose initialization method (empty or clone existing)",
      step5: "Verify schema synchronization"
    },
    
    namingConventions: {
      environments: ["development", "staging", "production", "testing"],
      clientSeparation: ["client_a", "client_b", "demo"],
      testing: ["feature_test", "load_test", "backup_test"],
      documentation: "Clear naming that indicates purpose and scope"
    }
  },
  
  // Data migration between sources
  dataMigration: {
    migrationTypes: {
      fullMigration: "Complete data transfer between sources",
      partialMigration: "Selective data transfer with filtering",
      schemaOnly: "Structure migration without data",
      incremental: "Ongoing synchronization and updates"
    },
    
    migrationProcess: {
      planning: [
        "Assess data volume and complexity",
        "Plan migration timing and downtime",
        "Identify data dependencies",
        "Prepare rollback procedures"
      ],
      
      execution: [
        "Create migration scripts or use built-in tools",
        "Test migration in non-production environment",
        "Execute migration with monitoring",
        "Verify data integrity and completeness"
      ],
      
      validation: [
        "Compare record counts and checksums",
        "Test application functionality",
        "Validate relationships and constraints",
        "Monitor performance after migration"
      ]
    }
  }
};
```

### Advanced Data Source Strategies

```javascript
// Advanced data source management strategies
const advancedDataSourceStrategies = {
  // Multi-environment workflows
  multiEnvironmentWorkflows: {
    developmentWorkflow: {
      dataSource: "development",
      purpose: "Active feature development and testing",
      dataStrategy: "Fresh, synthetic data for testing",
      updates: "Frequent schema and data changes"
    },
    
    stagingWorkflow: {
      dataSource: "staging", 
      purpose: "Pre-production testing and validation",
      dataStrategy: "Production-like data (anonymized)",
      updates: "Synchronized with development changes"
    },
    
    productionWorkflow: {
      dataSource: "production",
      purpose: "Live application data",
      dataStrategy: "Real user data with full security",
      updates: "Carefully managed with backup procedures"
    }
  },
  
  // Client isolation strategies
  clientIsolationStrategies: {
    separateDataSources: {
      approach: "Individual data source per client",
      benefits: "Complete data isolation and security",
      challenges: "Schema synchronization across sources",
      bestFor: "High-security requirements, compliance needs"
    },
    
    tenantIdentifiers: {
      approach: "Single data source with tenant identification",
      benefits: "Simplified schema management",
      challenges: "Data filtering and security implementation",
      bestFor: "SaaS applications with many clients"
    }
  },
  
  // Backup and disaster recovery
  backupDisasterRecovery: {
    backupStrategies: {
      regularBackups: "Automated daily/weekly backups to separate data source",
      pointInTimeRecovery: "Continuous backup for precise recovery points",
      crossRegionBackups: "Geographic redundancy for disaster recovery",
      testingProcedures: "Regular backup restoration testing"
    },
    
    recoveryProcedures: {
      rapidRecovery: "Quick restoration from recent backups",
      dataValidation: "Post-recovery data integrity verification",
      applicationTesting: "Full application testing after recovery",
      communicationPlan: "Stakeholder communication during recovery"
    }
  }
};
```

## Middleware Management

### Workspace-Level Middleware

```javascript
// Workspace middleware configuration and management
const workspaceMiddleware = {
  // Middleware scope and purpose
  middlewareScope: {
    workspaceLevel: {
      scope: "Applies to all APIs within the workspace",
      useCases: [
        "Universal authentication and authorization",
        "Comprehensive logging and monitoring",
        "Standard response formatting",
        "Security headers and policies",
        "Rate limiting and throttling"
      ],
      benefits: "Consistent behavior across all endpoints"
    },
    
    inheritanceHierarchy: {
      workspaceMiddleware: "Applied to all APIs automatically",
      apiGroupMiddleware: "Can extend or override workspace middleware",
      individualAPIMiddleware: "Most specific middleware configuration",
      executionOrder: "Workspace → API Group → Individual API"
    }
  },
  
  // Common workspace middleware patterns
  commonMiddlewarePatterns: {
    universalAuthentication: {
      purpose: "Workspace-wide authentication requirements",
      implementation: [
        "JWT token validation for all protected endpoints",
        "API key verification for service-to-service calls",
        "User context injection for downstream functions",
        "Authentication bypass for public endpoints"
      ]
    },
    
    comprehensiveLogging: {
      purpose: "Complete request/response logging",
      implementation: [
        "Request metadata capture (IP, user agent, timestamp)",
        "Response timing and status code logging",
        "Error tracking and alerting",
        "Performance metrics collection"
      ]
    },
    
    securityEnforcement: {
      purpose: "Workspace-wide security policies",
      implementation: [
        "CORS headers configuration",
        "Security headers injection (CSP, HSTS)",
        "Input sanitization and validation",
        "Rate limiting and abuse prevention"
      ]
    }
  },
  
  // Middleware configuration
  middlewareConfiguration: {
    accessPath: "Workspace Settings → Middleware",
    configurationOptions: {
      preMiddleware: "Execute before API function stacks",
      postMiddleware: "Execute after API function stacks",
      conditionalExecution: "Apply middleware based on conditions",
      errorHandling: "Handle middleware execution errors"
    },
    
    managementFeatures: {
      enableDisable: "Enable or disable middleware groups",
      ordering: "Configure middleware execution order",
      debugging: "Debug middleware execution and performance",
      monitoring: "Monitor middleware effectiveness and errors"
    }
  }
};
```

## Request History Configuration

### Logging and Debugging Setup

```javascript
// Request history configuration and management
const requestHistoryManagement = {
  // Request history concepts
  requestHistoryPurpose: {
    debugging: "Troubleshoot API issues and errors",
    monitoring: "Track API usage and performance",
    auditing: "Maintain compliance and security logs",
    analytics: "Analyze usage patterns and optimization opportunities"
  },
  
  // Configuration options
  configurationOptions: {
    objectTypes: {
      queries: "Database query execution logging",
      functions: "Function stack execution logging",
      tasks: "Background task execution logging",
      middleware: "Middleware execution logging",
      triggers: "Event trigger execution logging"
    },
    
    statementLimits: {
      noStatements: "Disable statement logging (minimal storage)",
      statements100: "Store last 100 statements per object",
      statements1000: "Store last 1,000 statements per object",
      statements10000: "Store last 10,000 statements per object",
      storeAll: "Store all statements (maximum debugging info)"
    }
  },
  
  // Storage considerations
  storageConsiderations: {
    storageImpact: "Request history uses database SSD storage",
    costImplications: "Higher statement limits increase storage costs",
    performance: "Large history volumes may impact query performance",
    retention: "Configure retention policies for long-term storage"
  },
  
  // Branch defaults and inheritance
  branchDefaults: {
    workspaceDefaults: {
      purpose: "Default settings for all objects in workspace",
      configuration: "Applied to new objects automatically",
      modification: "Can be overridden at individual object level"
    },
    
    inheritanceBehavior: {
      defaultInheritance: "Objects inherit workspace default settings",
      customOverrides: "Individual objects can override defaults",
      flexibleConfiguration: "Balance between consistency and customization"
    }
  }
};
```

### Advanced Request History Strategies

```javascript
// Advanced request history management strategies
const advancedRequestHistoryStrategies = {
  // Environment-specific configurations
  environmentSpecificConfigurations: {
    development: {
      statementLimit: "Store all statements for complete debugging",
      retention: "Short retention for rapid iteration",
      monitoring: "Detailed logging for development insights"
    },
    
    staging: {
      statementLimit: "Store 10,000 statements for testing validation",
      retention: "Medium retention for test cycle analysis",
      monitoring: "Performance and load testing metrics"
    },
    
    production: {
      statementLimit: "Store 1,000 statements for efficiency",
      retention: "Long retention for compliance and auditing",
      monitoring: "Error tracking and performance monitoring"
    }
  },
  
  // Selective logging strategies
  selectiveLogging: {
    criticalEndpoints: {
      configuration: "Maximum logging for business-critical APIs",
      purpose: "Ensure complete visibility for important operations",
      examples: "Payment processing, user authentication, data exports"
    },
    
    standardEndpoints: {
      configuration: "Moderate logging for regular operations",
      purpose: "Balance between visibility and storage efficiency",
      examples: "CRUD operations, data retrieval, content management"
    },
    
    highVolumeEndpoints: {
      configuration: "Minimal logging for high-traffic APIs",
      purpose: "Reduce storage overhead for frequent operations",
      examples: "Health checks, status endpoints, frequent queries"
    }
  },
  
  // Monitoring and alerting
  monitoringAlerting: {
    errorRateMonitoring: {
      setup: "Monitor error rates across request history",
      thresholds: "Configure alerts for unusual error patterns",
      automation: "Automatic escalation for critical errors"
    },
    
    performanceMonitoring: {
      setup: "Track execution time trends from request history",
      optimization: "Identify slow queries and functions",
      capacity: "Plan scaling based on performance trends"
    }
  }
};
```

## Database Preferences

### Table Format Configuration

```javascript
// Database format and table management
const databasePreferences = {
  // Table format options
  tableFormatOptions: {
    jsonbFormat: {
      structure: {
        id: "Primary key column",
        jsonb: "JSONB column containing entire record"
      },
      
      advantages: [
        "Flexible schema changes without migrations",
        "Efficient storage for variable data structures",
        "Native JSON operations and queries",
        "Backward compatibility with existing data"
      ],
      
      disadvantages: [
        "Limited compatibility with external SQL tools",
        "Less efficient for non-indexed queries",
        "Requires JSONB-aware query optimization"
      ],
      
      bestFor: "Applications with evolving schemas and JSON-heavy data"
    },
    
    standardSQLFormat: {
      structure: "Individual columns for each field",
      
      advantages: [
        "Full compatibility with external SQL tools",
        "Better performance for non-indexed queries",
        "Faster column additions and modifications",
        "Standard SQL query patterns"
      ],
      
      disadvantages: [
        "Schema migrations required for structure changes",
        "Less flexible for dynamic data structures",
        "Potential for wider tables with many columns"
      ],
      
      bestFor: "Applications requiring SQL tool integration and analytics"
    }
  },
  
  // Migration considerations
  migrationConsiderations: {
    whenToMigrate: [
      "Need for third-party analytics tools (Tableau, PowerBI)",
      "Performance requirements for complex queries",
      "Integration with external SQL-based systems",
      "Compliance requirements for standard SQL formats"
    ],
    
    migrationProcess: {
      preparation: [
        "Enable standard SQL format for new tables",
        "Test migration with non-critical tables",
        "Plan migration timing and downtime",
        "Backup all data before migration"
      ],
      
      execution: [
        "Select tables for migration",
        "Monitor migration progress",
        "Validate data integrity after migration",
        "Update applications if needed"
      ],
      
      validation: [
        "Test all application functionality",
        "Verify external tool compatibility",
        "Monitor performance changes",
        "Document migration outcomes"
      ]
    }
  },
  
  // Custom SQL table names
  customSQLTableNames: {
    purpose: "Replace default Xano table names with meaningful identifiers",
    defaultFormat: "mvpw<workspaceID>_<tableID> (e.g., mvpw1_3)",
    customFormat: "User-defined names (e.g., users, products, orders)",
    
    benefits: [
      "Improved readability for direct database access",
      "Better compatibility with external tools",
      "Simplified query writing and maintenance",
      "Enhanced developer experience"
    ],
    
    considerations: [
      "Names must be globally unique across workspaces",
      "Use workspace prefixes for uniqueness",
      "Data sources automatically add environment suffixes",
      "Update existing queries when changing names"
    ]
  }
};
```

## Team Collaboration Features

### Workspace Sharing and Access Control

```javascript
// Team collaboration and workspace management
const teamCollaboration = {
  // Access control and permissions
  accessControlManagement: {
    roleTypes: {
      owner: {
        permissions: "Full workspace control and management",
        capabilities: [
          "Modify all workspace settings",
          "Manage team member access",
          "Delete or transfer workspace",
          "Access billing and subscription management"
        ]
      },
      
      admin: {
        permissions: "Administrative access with some restrictions",
        capabilities: [
          "Modify workspace configuration",
          "Manage most team members",
          "Deploy and manage applications",
          "Access advanced features"
        ]
      },
      
      developer: {
        permissions: "Development access with limited administrative rights",
        capabilities: [
          "Create and modify APIs and functions",
          "Access database and data sources",
          "Test and debug applications",
          "View performance metrics"
        ]
      },
      
      viewer: {
        permissions: "Read-only access to workspace",
        capabilities: [
          "View workspace structure and configuration",
          "Access documentation and comments",
          "View performance metrics and logs",
          "Export data and reports"
        ]
      }
    },
    
    accessManagementBestPractices: {
      principleOfLeastPrivilege: "Grant minimum necessary access",
      regularAccessReviews: "Periodic review and cleanup of access",
      roleBasedAccess: "Use roles rather than individual permissions",
      documentationMaintenance: "Keep access documentation current"
    }
  },
  
  // Collaboration workflows
  collaborationWorkflows: {
    developmentWorkflow: {
      branchingStrategy: "Use development branches for feature work",
      codeReview: "Review changes before merging to main branch",
      testing: "Comprehensive testing before production deployment",
      documentation: "Maintain current documentation and comments"
    },
    
    deploymentWorkflow: {
      stagingDeployment: "Deploy to staging for testing first",
      productionDeployment: "Careful production deployment with rollback plan",
      monitoringPostDeployment: "Monitor application after deployment",
      rollbackProcedures: "Quick rollback if issues arise"
    }
  },
  
  // Workspace cloning and export
  workspaceManagement: {
    workspaceCloning: {
      purpose: "Create copies of workspace for different environments",
      includes: [
        "Database table schemas and relationships",
        "API groups and endpoint configurations", 
        "Function stacks and business logic",
        "Add-ons and extensions",
        "Background tasks and triggers"
      ],
      excludes: "Database table records and actual data",
      useCases: [
        "Creating staging environments",
        "Backup workspace configurations",
        "Template creation for similar projects",
        "Development environment setup"
      ]
    },
    
    workspaceExport: {
      purpose: "Export complete workspace for backup or migration",
      exportOptions: {
        configurationOnly: "Schema and configuration without data",
        withData: "Complete export including all data",
        withMedia: "Include file attachments and media"
      },
      considerations: [
        "Export processing time depends on data volume",
        "Large exports may take significant time",
        "Exported data available for 12 hours",
        "Email notification when export completes"
      ]
    }
  }
};
```

## Advanced Workspace Features

### Compliance and Audit Features

```javascript
// Advanced workspace features and compliance
const advancedWorkspaceFeatures = {
  // Compliance center
  complianceCenter: {
    purpose: "Advanced auditing and compliance tracking",
    availability: "Premium feature for enterprise plans",
    
    features: {
      auditTrails: "Complete activity logging and tracking",
      complianceReporting: "Generate compliance reports and documentation",
      accessReviews: "Regular access reviews and certifications",
      dataGovernance: "Data handling and retention policies"
    },
    
    complianceStandards: [
      "SOC 2 compliance tracking",
      "GDPR compliance monitoring",
      "HIPAA compliance auditing", 
      "Custom compliance frameworks"
    ]
  },
  
  // Statement explorer
  statementExplorer: {
    purpose: "Search and analyze function implementations across workspace",
    capabilities: [
      "Find all instances of specific functions",
      "Security audit across all workflows",
      "Impact analysis for changes",
      "Code quality assessment"
    ],
    
    useCases: [
      "Security audits and vulnerability assessment",
      "Refactoring and optimization projects",
      "Compliance verification and documentation",
      "Performance analysis and improvements"
    ]
  },
  
  // Realtime settings
  realtimeSettings: {
    purpose: "Configure workspace-wide realtime functionality",
    configuration: [
      "Channel management and permissions",
      "Message routing and filtering",
      "Connection limits and throttling",
      "Authentication and authorization"
    ]
  },
  
  // Draft management
  draftManagement: {
    resetDrafts: {
      purpose: "Clear all drafts and revert to published versions",
      useCases: [
        "Clean up development environment",
        "Resolve draft-related issues",
        "Prepare for major releases",
        "Emergency rollback scenarios"
      ],
      warning: "Action is irreversible - use with caution"
    }
  }
};
```

## 💡 **Pro Tips**

1. **Plan Your Data Sources**: Set up development, staging, and production data sources early in your project

2. **Configure Request History Strategically**: Balance debugging needs with storage costs

3. **Use Workspace-Level Middleware**: Implement consistent cross-cutting concerns at the workspace level

4. **Document Everything**: Enable internal documentation tools and maintain comprehensive project documentation

5. **Regular Access Reviews**: Periodically review and update team member access permissions

## Try This: Complete Workspace Setup

Configure a production-ready workspace:

```javascript
// Complete workspace configuration checklist
const productionWorkspaceSetup = {
  // 1. Identity and organization
  identitySetup: {
    naming: "Use clear, descriptive workspace names",
    description: "Document project purpose and team information",
    documentation: "Enable internal documentation tools",
    marketplace: "Enable marketplace for development efficiency"
  },
  
  // 2. Data source configuration
  dataSourceSetup: {
    environments: "Set up development, staging, and production data sources",
    migration: "Plan data migration strategies between sources",
    backup: "Implement backup and disaster recovery procedures",
    testing: "Configure testing data sources for validation"
  },
  
  // 3. Development workflow
  developmentWorkflow: {
    middleware: "Configure workspace-level middleware for consistency",
    requestHistory: "Set up appropriate logging for each environment",
    database: "Choose optimal table format for your use case",
    collaboration: "Establish team access and collaboration procedures"
  },
  
  // 4. Monitoring and compliance
  monitoringCompliance: {
    auditLogs: "Enable comprehensive audit logging",
    statementExplorer: "Use for security audits and code analysis",
    compliance: "Configure compliance center if required",
    maintenance: "Establish regular maintenance and review procedures"
  }
};
```

## Common Mistakes to Avoid

❌ **Not planning data source strategy early**
✅ Set up multiple data sources from project start

❌ **Excessive request history logging in production**
✅ Balance logging needs with storage costs

❌ **Inconsistent middleware across environments**
✅ Use workspace-level middleware for consistency

❌ **Poor team access management**
✅ Implement proper role-based access control

❌ **Ignoring database format implications**
✅ Choose table format based on integration requirements

Workspace Settings provide the foundation for organized, scalable Xano development. Use these configurations strategically to create efficient development workflows and maintain high-quality, well-documented projects.