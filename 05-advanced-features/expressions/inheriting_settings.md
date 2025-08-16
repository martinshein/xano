---
title: "Workspace Settings and Configuration"
description: "Master Xano workspace settings including request history, middleware, branching, table formats, and inheritance patterns for optimal development workflows"
category: expressions
has_code_examples: true
last_updated: '2025-01-16'
tags:
  - workspace-settings
  - request-history
  - middleware
  - table-formats
  - inheritance
  - configuration
---

# Workspace Settings and Configuration

## 📋 **Quick Summary**

Xano workspace settings provide comprehensive control over your development environment, including request history logging, middleware configuration, table formats, and inheritance patterns. Proper configuration optimizes performance, debugging capabilities, and team collaboration workflows.

## What You'll Learn

- Complete workspace settings configuration
- Request history management and inheritance
- Database table format selection (JSONB vs SQL)
- Custom SQL table naming strategies
- Middleware and branch default configurations
- Best practices for team environments

## Accessing Workspace Settings

Navigate to workspace settings through the main interface:

1. **Open Workspace Dashboard**
   - Go to your target workspace
   - Click the three dots (⋮) icon in the top-right corner

2. **Select Settings**
   - Choose "Settings" from the dropdown menu
   - Access comprehensive configuration options

## General Settings Configuration

### Basic Workspace Information

**Workspace Name** *(Required)*
- Give your workspace a unique, descriptive name
- Use naming conventions for team organization
- Example: "ProductionAPI-v2" or "DevEnvironment-TeamA"

**Description**
- Document workspace purpose and usage
- Include team contact information
- Note any special configurations or restrictions

**Feature Toggles**
- **Internal Documentation Tool**: Enable plain text documentation for function stacks
- **Start Page**: Show beginner guidance (recommended for new team members)
- **Marketplace**: Enable access to Xano snippet marketplace
- **AI Preferences**: Accept terms to use AI-powered features like Database Assistant

## Request History Configuration

Request history provides crucial debugging and monitoring capabilities by logging API calls, function executions, and database operations.

### Understanding Request History Impact

**Storage Consideration**: Request history uses your Database (SSD) storage allocation
**Performance Impact**: Extensive logging can affect performance
**Debugging Value**: Essential for troubleshooting and optimization

### Branch Default Settings

Configure default request history behavior for all workspace objects:

**Available Object Types:**
- Query (API endpoints)
- Function (Custom functions)
- Task (Background tasks)
- Middleware (Request/response processing)
- Trigger (Event-driven workflows)

**Configuration Options for Each Type:**

1. **Enable/Disable**: Turn logging on or off completely
2. **Function Statement Limit**: Choose logging detail level
   - No statements (minimal logging)
   - 100 statements (light logging)
   - 1,000 statements (moderate logging)
   - 10,000 statements (detailed logging)
   - Store all statements (complete logging)

### Try This: Optimal Request History Configuration

```markdown
# Production Environment Settings

## High-Priority APIs (User-facing)
- Enable: Yes
- Statement Limit: 1,000 statements
- Use Case: Balance debugging capability with performance

## Background Tasks
- Enable: Yes  
- Statement Limit: 10,000 statements
- Use Case: Detailed logging for complex operations

## Development Functions
- Enable: Yes
- Statement Limit: Store all statements
- Use Case: Complete debugging information

## Middleware
- Enable: Yes
- Statement Limit: 100 statements
- Use Case: Light logging to avoid overhead
```

### Inheriting Settings

Individual objects can override workspace defaults through inheritance settings:

**Inheritance Options:**
- **Inherit**: Use workspace branch defaults (recommended)
- **Custom**: Override with object-specific settings

**Best Practices:**
- Keep most objects on "inherit" for consistency
- Override only when specific objects need different logging
- Document any custom inheritance decisions

## Database Table Formats

Xano supports two table storage formats with different advantages:

### JSONB Format (Legacy Default)

**Structure:**
- Two columns per table: `id` and `jsonb`
- JSON representation of entire record in `jsonb` column
- Backward compatible with existing workspaces

**Advantages:**
- Flexible schema changes
- Complex data structure support
- Existing workspace compatibility

**Disadvantages:**
- Less efficient for direct database queries
- Limited third-party tool compatibility
- Slower non-indexed queries

### Standard SQL Format (Recommended)

**Structure:**
- Individual column for each field
- Traditional relational database layout
- Better third-party tool integration

**Advantages:**
- Faster performance for non-indexed queries
- Better compatibility with analytics tools
- Faster column additions
- Standard SQL query support

**When to Use Standard SQL:**
- Direct database connections with tools like Tableau or PowerBI
- Frequent addition of new fields
- Complex reporting requirements
- SQL analytics tool integration
- Performance optimization needs

### Converting Table Formats

**⚠️ WARNING**: Table format conversion is permanent and irreversible.

**Conversion Process:**

1. **Enable Standard SQL Setting**
   - Go to workspace settings
   - Scroll to "Database Preferences"
   - Check "Use standard SQL columns for new tables"

2. **Convert Existing Tables**
   - Access migration panel from workspace settings
   - Select tables for conversion
   - Confirm conversion choices
   - Monitor migration progress

3. **Update External Connections**
   - Modify any direct database queries
   - Update third-party tool connections
   - Test all external integrations

## Custom SQL Table Names

### Default Naming Convention

Xano assigns default SQL names in format: `mvpw<workspaceID>_<tableID>`
- Example: `mvpw1_3` for workspace 1, table 3
- Functional but not intuitive for direct queries

### Custom Naming Benefits

**Improved Readability**: `users` instead of `mvpw1_3`
**Better Tool Integration**: More intuitive for database tools
**Query Simplification**: Easier to write and maintain direct SQL

### Configuration Process

1. **Enable Custom SQL Names**
   - Go to workspace settings
   - Enable "Custom SQL Table Names"

2. **Configure Individual Tables**
   - Navigate to table settings
   - Click "Manage" next to "SQL Table Name"
   - Set custom name or leave blank for default

### Naming Best Practices

```markdown
# SQL Table Naming Strategy

## Workspace Prefixes
- Use workspace-specific prefixes: `projA_users`, `projB_users`
- Ensures uniqueness across workspaces
- Maintains organization clarity

## Environment Suffixes  
- Development: `users_dev`
- Testing: `users_test`  
- Production: `users` (clean)

## Naming Conventions
- Use lowercase with underscores
- Be descriptive but concise
- Include version numbers if needed: `users_v2`
```

## Data Sources and Migration

### Data Source Management

**Purpose**: Maintain separate databases with same schema
**Use Cases**: 
- Production vs. testing data separation
- Environment-specific configurations
- Data isolation for different clients

**Management Options:**
- **Manage**: Browse and add new data sources
- **Migrate**: Transfer data between sources

### Migration Strategies

```markdown
# Data Source Migration Workflow

## Development to Staging
1. Create staging data source
2. Migrate schema structure
3. Populate with test data
4. Validate functionality

## Staging to Production  
1. Create production data source
2. Migrate validated schema
3. Import production data
4. Switch live environment
```

## Team Collaboration Features

### Workspace Cloning

**Purpose**: Create workspace copies for testing or branching
**Includes**: Database schema, APIs, functions, addons, tasks
**Excludes**: Actual database records

**Process:**
1. Access workspace settings
2. Choose "Clone Workspace"
3. Configure new workspace settings
4. Wait for cloning completion

### Workspace Export/Import

**Export Process:**
- Background processing for large workspaces
- Optional media attachment inclusion
- Email notification when ready
- 12-hour download availability

**Import Considerations:**
- Completely replaces destination workspace
- Test in development environment first
- Create backups before importing

## Integration with No-Code Platforms

### WeWeb Project Configuration

Align WeWeb projects with workspace settings:

1. **API Configuration**: Match WeWeb datasource settings with workspace APIs
2. **Authentication**: Coordinate auth patterns with workspace middleware
3. **Error Handling**: Align error responses with request history settings
4. **Performance**: Configure WeWeb caching based on workspace performance

### Make.com Automation

Leverage workspace settings in automation:

1. **Request Monitoring**: Use request history data for automation triggers
2. **Error Handling**: Create scenarios based on workspace error patterns
3. **Performance Optimization**: Adjust scenarios based on workspace metrics
4. **Data Validation**: Use workspace validation rules in scenarios

### n8n Workflow Integration

Coordinate n8n workflows with workspace configuration:

1. **Logging Integration**: Export request history to n8n for analysis
2. **Performance Monitoring**: Create workflows to monitor workspace health
3. **Backup Automation**: Automate workspace exports through n8n
4. **Team Notifications**: Alert teams of workspace configuration changes

## Common Mistakes to Avoid

1. **Over-Logging**: Excessive request history can impact performance and storage
2. **Format Confusion**: Not understanding JSONB vs SQL format implications
3. **Inheritance Chaos**: Too many custom inheritance settings create complexity
4. **Migration Rush**: Converting table formats without proper testing
5. **Documentation Neglect**: Not documenting custom settings and decisions

## Pro Tips

1. **Storage Monitoring**: Regularly review request history storage usage
2. **Performance Testing**: Test different logging levels for optimal performance
3. **Documentation Standards**: Maintain clear documentation of custom configurations
4. **Team Communication**: Notify team members of workspace setting changes
5. **Backup Strategy**: Create backups before major setting changes
6. **Environment Consistency**: Keep similar settings across development environments

## Advanced Configuration Patterns

### Environment-Specific Settings

```markdown
# Multi-Environment Configuration

## Development Workspace
- Request History: Store all statements
- Table Format: Standard SQL  
- Custom Names: Enabled with _dev suffix
- AI Features: Enabled for experimentation

## Production Workspace  
- Request History: 1,000 statements
- Table Format: Standard SQL
- Custom Names: Clean production names
- AI Features: Controlled enablement
```

### Team-Based Inheritance

```markdown
# Team Inheritance Strategy

## Backend Team Functions
- Inherit: No (custom detailed logging)
- Statement Limit: Store all statements
- Reason: Complex debugging requirements

## Frontend Team APIs
- Inherit: Yes (use workspace defaults)
- Reason: Standard logging sufficient

## DevOps Monitoring
- Inherit: No (minimal logging)
- Statement Limit: 100 statements  
- Reason: Performance optimization
```

Proper workspace configuration creates a foundation for efficient development, effective debugging, and seamless team collaboration. By understanding and implementing these settings strategically, you can optimize your Xano environment for both current needs and future scalability.