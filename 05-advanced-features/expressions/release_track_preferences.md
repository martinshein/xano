---
title: "Release Track Preferences"
description: "Learn how to configure when and how your Xano instance receives platform updates through release track preferences"
category: expressions
has_code_examples: false
last_updated: '2025-01-16'
tags:
  - release-tracks
  - updates
  - maintenance
  - instance-management
  - deployment
---

# Release Track Preferences
## 📋 **Quick Summary**

Release Track Preferences control when and how your Xano instance receives platform updates. This feature allows you to balance staying current with new features against maintaining stability for production environments.

## What You'll Learn

- How to access and configure release track settings
- Understanding the three release track options
- Setting maintenance windows for controlled updates
- Best practices for different environment types
- Enterprise manual update control

## Understanding Release Tracks

Xano continuously improves its platform with new features, bug fixes, and performance enhancements. Release tracks give you control over when these updates are applied to your instance:

**Why This Matters:**
- **Production Stability**: Avoid unexpected changes during critical business periods
- **Testing Coordination**: Align updates with your testing schedules
- **Team Preparation**: Ensure your team is ready for new features
- **Change Management**: Maintain control over your deployment environment

## Accessing Release Track Settings

1. **Navigate to Instance Settings**
   - Go to your instance selection screen
   - Click the settings icon (⚙️) next to your target instance

2. **Select Release Track**
   - Choose "Release Track" from the settings panel
   - Review current setting and available options

3. **Configure Preferences**
   - Select your preferred track based on plan availability
   - Set maintenance windows if using Flexible track
   - Save configuration changes

## Release Track Options

### Immediate (Default)

**How It Works:**
- Updates deploy automatically as soon as available
- No manual intervention required
- Fastest access to new features and fixes

**Best For:**
- Development environments
- Testing instances
- Teams comfortable with frequent updates
- Instances where downtime is not critical

**Considerations:**
- Updates can happen at any time
- May introduce changes during active development
- Requires team readiness for immediate changes

### Flexible

**How It Works:**
- Updates deploy during specified maintenance windows
- Choose preferred days of the week
- Control timing of update application

**Configuration Options:**

**Maintenance Window:**
- Set specific time ranges for updates
- Typically scheduled during low-traffic periods
- Coordinate with team availability
- Consider user timezone and usage patterns

**Preferred Release Days:**
- Select specific days of the week
- Common choices: Weekends, specific weekdays
- Avoid high-traffic or critical business days
- Align with team maintenance schedules

**Best For:**
- Production environments
- Instances with predictable traffic patterns
- Teams with structured maintenance schedules
- Applications requiring scheduled downtime

### Manual (Enterprise Only)

**How It Works:**
- Complete manual control over update deployment
- Updates held until explicitly approved
- Maximum control over timing and coordination

**Best For:**
- Critical production systems
- Highly regulated environments
- Complex integration dependencies
- Organizations with strict change management

**Requirements:**
- Enterprise plan subscription
- Dedicated change management processes
- Regular review of available updates
- Coordination with Xano support team

## Try This: Multi-Environment Configuration

Set up appropriate release tracks for different environment types:

```markdown
# Release Track Strategy by Environment

## Development Environment
- Track: Immediate
- Reason: Fast access to new features for testing
- Risk: Low (non-production)

## Staging Environment  
- Track: Flexible
- Window: Weekends, early morning
- Reason: Controlled testing before production
- Risk: Medium (testing impact)

## Production Environment
- Track: Flexible or Manual (Enterprise)
- Window: Sunday 2:00-4:00 AM (low traffic)
- Reason: Maximum stability and control
- Risk: High (customer impact)
```

## Setting Optimal Maintenance Windows

### Analyzing Traffic Patterns

Before setting maintenance windows, understand your usage patterns:

**Data to Review:**
- Peak usage hours and days
- Geographic distribution of users
- Critical business processes timing
- Team availability for monitoring

### Recommended Window Strategies

**Global Applications:**
```markdown
# Global Maintenance Window Strategy

## Option 1: Rolling Windows
- Different windows for different regions
- Minimize impact across time zones
- Coordinate with regional teams

## Option 2: Universal Low-Impact
- Identify globally quiet periods
- Typically weekend early morning UTC
- Shorter maintenance windows
```

**Regional Applications:**
```markdown
# Regional Maintenance Strategy

## Business Hours Consideration
- Avoid peak business hours
- Schedule during off-hours
- Consider holiday calendars

## Weekend Scheduling
- Saturday/Sunday early morning
- Friday late evening
- Coordinate with support availability
```

## Best Practices by Environment Type

### Development Environments

**Recommended Settings:**
- Release Track: Immediate
- Monitoring: Basic
- Team Preparation: Minimal required

**Benefits:**
- Access to latest features immediately
- Early identification of potential issues
- Faster development cycle capability

### Staging Environments

**Recommended Settings:**
- Release Track: Flexible
- Maintenance Window: Weekends or early mornings
- Team Preparation: Moderate

**Strategy:**
- Test updates before production deployment
- Validate integrations and functionality
- Prepare team for production changes

### Production Environments

**Recommended Settings:**
- Release Track: Flexible (or Manual for Enterprise)
- Maintenance Window: Carefully chosen low-impact periods
- Team Preparation: Full preparation and monitoring

**Critical Considerations:**
- User impact minimization
- Rollback procedures ready
- Team availability during windows
- Customer communication if needed

## Team Coordination Strategies

### Pre-Update Preparation

```markdown
# Update Preparation Checklist

## Technical Preparation
- [ ] Review update notes and changes
- [ ] Backup critical data and configurations
- [ ] Test in staging environment first
- [ ] Prepare rollback procedures

## Team Coordination
- [ ] Notify team of update schedule
- [ ] Assign monitoring responsibilities
- [ ] Plan post-update validation
- [ ] Coordinate with customer support

## Communication
- [ ] Inform stakeholders of maintenance window
- [ ] Prepare customer notifications if needed
- [ ] Document expected changes
- [ ] Set up monitoring and alerting
```

### Post-Update Monitoring

**Immediate Checks:**
- API functionality validation
- Performance monitoring
- Error rate assessment
- User experience verification

**Extended Monitoring:**
- System stability over 24-48 hours
- Integration point validation
- User feedback collection
- Performance trend analysis

## Integration with CI/CD Workflows

### Coordinating with Development Cycles

**Sprint Planning Integration:**
- Schedule updates during sprint breaks
- Avoid updates during feature releases
- Coordinate with testing phases
- Plan for update-related adjustments

**Release Coordination:**
- Align Xano updates with application releases
- Test compatibility before production deployment
- Prepare for potential integration updates
- Document version dependencies

## Common Mistakes to Avoid

1. **Ignoring Traffic Patterns**: Scheduling updates during peak usage
2. **Insufficient Testing**: Not testing updates in staging first
3. **Poor Communication**: Not notifying teams or users appropriately
4. **No Rollback Plan**: Lacking procedures for reverting changes
5. **Inconsistent Strategy**: Different tracks without clear reasoning

## Pro Tips

1. **Environment Alignment**: Use consistent strategies across similar environments
2. **Documentation**: Keep records of update schedules and outcomes
3. **Monitoring Setup**: Establish automated monitoring for post-update validation
4. **Team Training**: Ensure team understands update processes and procedures
5. **Customer Communication**: Prepare templates for user notifications when needed
6. **Performance Baseline**: Establish performance baselines for comparison

## Troubleshooting Update Issues

### Common Problems

**Update Delays:**
- Check maintenance window configuration
- Verify plan includes flexible options
- Contact support for manual track issues

**Unexpected Updates:**
- Review current track setting
- Check for recent configuration changes
- Verify maintenance window settings

**Integration Issues Post-Update:**
- Test API endpoints for changes
- Review update notes for breaking changes
- Check authentication and headers
- Validate data formats and responses

### Getting Support

**When to Contact Xano Support:**
- Enterprise manual track configuration
- Update issues affecting production
- Unexpected behavior post-update
- Complex maintenance window requirements

**Information to Provide:**
- Instance ID and current track setting
- Specific issues or unexpected behavior
- Timeline of when issues started
- Steps already taken to resolve

Release Track Preferences provide essential control over your Xano instance updates, enabling you to balance platform improvements with operational stability. By choosing appropriate tracks and maintenance windows for each environment, you can ensure smooth operations while staying current with Xano's latest capabilities.