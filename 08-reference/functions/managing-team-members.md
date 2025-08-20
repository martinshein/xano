---
category: functions
description: Complete guide to managing team members in Xano with role-based access control, collaboration workflows, and permission management
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - add_a_team_member.md
  - audit-logs.md
  - workspace-settings.md
  - ci-cd.md
subcategory: 08-reference/functions
tags:
  - team-management
  - rbac
  - permissions
  - collaboration
  - workflow
  - security
title: Managing Team Members
---

# Managing Team Members

## 📋 **Quick Summary**
Master team management in Xano with role-based access control, workflow collaboration, permission systems, and secure development practices for distributed teams and agencies.

## What You'll Learn
- Team member invitation and onboarding
- Role-based access control (RBAC) implementation
- Collaboration workflows and permissions
- Audit logging and activity tracking
- Agency and client management
- Integration with external team tools

## Team Structure and Roles

### Default Role Hierarchy
```javascript
// Xano team roles and permissions
const teamRoles = {
  "owner": {
    "description": "Full system access and billing control",
    "permissions": ["*"], // All permissions
    "limitations": "Cannot be removed, only transferred"
  },
  "admin": {
    "description": "Full development and management access",
    "permissions": [
      "database.*", "api.*", "settings.*", 
      "team.manage", "deploy.production"
    ],
    "limitations": "Cannot modify billing or transfer ownership"
  },
  "developer": {
    "description": "Development access with deployment restrictions",
    "permissions": [
      "database.read", "database.write", "api.*",
      "deploy.staging", "logs.read"
    ],
    "limitations": "No production deployment or team management"
  },
  "viewer": {
    "description": "Read-only access for monitoring and review",
    "permissions": [
      "database.read", "api.read", "logs.read"
    ],
    "limitations": "Cannot modify any resources"
  }
};
```

### Custom Role Creation
```javascript
// Custom role definition
function createCustomRole(roleData) {
  return {
    name: roleData.name,
    description: roleData.description,
    permissions: {
      // Database permissions
      database: {
        read: roleData.permissions.includes('database.read'),
        write: roleData.permissions.includes('database.write'),
        schema: roleData.permissions.includes('database.schema'),
        delete: roleData.permissions.includes('database.delete')
      },
      // API permissions  
      api: {
        read: roleData.permissions.includes('api.read'),
        write: roleData.permissions.includes('api.write'),
        deploy: roleData.permissions.includes('api.deploy'),
        delete: roleData.permissions.includes('api.delete')
      },
      // System permissions
      system: {
        settings: roleData.permissions.includes('system.settings'),
        billing: roleData.permissions.includes('system.billing'),
        team: roleData.permissions.includes('system.team'),
        logs: roleData.permissions.includes('system.logs')
      }
    },
    restrictions: {
      ip_whitelist: roleData.ip_restrictions || [],
      time_restrictions: roleData.time_restrictions || null,
      resource_limits: roleData.resource_limits || {}
    }
  };
}
```

## Team Member Management Functions

### Invitation System
```javascript
// Function stack for team member invitation
[
  {
    "function": "Validate Invitation",
    "logic": `
      // Check if user has permission to invite
      if (!auth.user.permissions.includes('team.manage')) {
        return error(403, "Insufficient permissions to invite team members");
      }
      
      // Validate email format
      if (!inputs.email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
        return error(400, "Invalid email format");
      }
      
      // Check if user is already a team member
      const existingMember = await queryDatabase(
        "SELECT id FROM team_members WHERE email = ? AND workspace_id = ?",
        [inputs.email, auth.workspace.id]
      );
      
      if (existingMember.length > 0) {
        return error(409, "User is already a team member");
      }
    `
  },
  {
    "function": "Create Invitation Record",
    "action": "add_record",
    "table": "team_invitations",
    "data": {
      "workspace_id": "auth.workspace.id",
      "email": "inputs.email",
      "role": "inputs.role", 
      "invited_by": "auth.user.id",
      "invitation_token": "generate_secure_token(32)",
      "expires_at": "date_add(now(), INTERVAL 7 DAY)",
      "status": "pending"
    }
  },
  {
    "function": "Send Invitation Email",
    "email_template": "team-invitation",
    "to": "inputs.email",
    "variables": {
      "inviter_name": "auth.user.name",
      "workspace_name": "auth.workspace.name",
      "role": "inputs.role",
      "invitation_link": "concat(environment.APP_URL, '/invite/', invitation.invitation_token)",
      "expires_at": "invitation.expires_at"
    }
  },
  {
    "function": "Log Activity",
    "action": "add_record",
    "table": "activity_logs",
    "data": {
      "user_id": "auth.user.id",
      "action": "team_member_invited",
      "details": {
        "invited_email": "inputs.email",
        "role": "inputs.role"
      },
      "timestamp": "now()"
    }
  }
]
```

### Invitation Acceptance
```javascript
// Accept team invitation workflow
function acceptInvitation(invitationToken, userData) {
  const workflow = [
    {
      name: "Validate Token",
      logic: `
        const invitation = await queryDatabase(
          "SELECT * FROM team_invitations WHERE invitation_token = ? AND status = 'pending' AND expires_at > NOW()",
          [invitationToken]
        );
        
        if (!invitation) {
          throw new Error("Invalid or expired invitation");
        }
        
        return invitation;
      `
    },
    {
      name: "Create User Account",
      conditional: "user_exists",
      logic: `
        // Check if user already has an account
        const existingUser = await queryDatabase(
          "SELECT id FROM users WHERE email = ?",
          [invitation.email]
        );
        
        if (!existingUser) {
          const newUser = await addRecord("users", {
            email: invitation.email,
            name: userData.name,
            password: hashPassword(userData.password),
            created_at: new Date()
          });
          return newUser;
        }
        
        return existingUser;
      `
    },
    {
      name: "Add Team Member",
      action: "add_record",
      table: "team_members",
      data: {
        user_id: "user.id",
        workspace_id: "invitation.workspace_id", 
        role: "invitation.role",
        invited_by: "invitation.invited_by",
        joined_at: "now()",
        status: "active"
      }
    },
    {
      name: "Update Invitation Status",
      action: "edit_record",
      table: "team_invitations",
      where: { id: "invitation.id" },
      data: {
        status: "accepted",
        accepted_at: "now()"
      }
    }
  ];
  
  return executeWorkflow(workflow);
}
```

## Permission Management System

### RBAC Implementation
```javascript
// Role-based access control middleware
function checkPermissions(requiredPermissions) {
  return {
    middleware: "permission_check",
    logic: `
      const userPermissions = await getUserPermissions(auth.user.id, auth.workspace.id);
      
      // Check if user has required permissions
      for (const permission of requiredPermissions) {
        if (!hasPermission(userPermissions, permission)) {
          return error(403, \`Insufficient permissions: \${permission} required\`);
        }
      }
      
      // Log permission check for audit
      await logActivity({
        user_id: auth.user.id,
        action: 'permission_check',
        resource: request.endpoint,
        permissions_checked: requiredPermissions,
        result: 'granted'
      });
    `
  };
}

// Helper function to check permissions
function hasPermission(userPermissions, requiredPermission) {
  // Handle wildcard permissions
  if (userPermissions.includes('*')) {
    return true;
  }
  
  // Direct permission match
  if (userPermissions.includes(requiredPermission)) {
    return true;
  }
  
  // Pattern matching (e.g., 'database.*' includes 'database.read')
  const permissionParts = requiredPermission.split('.');
  for (let i = permissionParts.length; i > 0; i--) {
    const wildcardPermission = permissionParts.slice(0, i).join('.') + '.*';
    if (userPermissions.includes(wildcardPermission)) {
      return true;
    }
  }
  
  return false;
}
```

### Dynamic Permission Assignment
```javascript
// Update team member permissions
function updateMemberPermissions(memberId, newPermissions) {
  return [
    {
      function: "Validate Request",
      logic: `
        // Only admins can modify permissions
        if (!auth.user.permissions.includes('team.manage')) {
          return error(403, "Only administrators can modify permissions");
        }
        
        // Cannot modify owner permissions
        const member = await getMemberDetails(memberId);
        if (member.role === 'owner') {
          return error(403, "Cannot modify owner permissions");
        }
      `
    },
    {
      function: "Update Member Record",
      action: "edit_record", 
      table: "team_members",
      where: { id: memberId },
      data: {
        permissions: newPermissions,
        updated_by: "auth.user.id",
        updated_at: "now()"
      }
    },
    {
      function: "Log Permission Change",
      action: "add_record",
      table: "permission_changes",
      data: {
        member_id: memberId,
        changed_by: "auth.user.id",
        previous_permissions: "member.permissions",
        new_permissions: newPermissions,
        timestamp: "now()"
      }
    },
    {
      function: "Notify Member",
      email_template: "permissions-updated",
      to: "member.email",
      variables: {
        workspace_name: "auth.workspace.name",
        updated_by: "auth.user.name",
        new_permissions: newPermissions
      }
    }
  ];
}
```

## Collaboration Workflows

### Code Review and Approval
```javascript
// Code review workflow
const codeReviewWorkflow = {
  // Submit for review
  submitForReview: [
    {
      function: "Create Review Request",
      action: "add_record",
      table: "code_reviews",
      data: {
        author_id: "auth.user.id",
        branch: "inputs.branch",
        changes_summary: "inputs.summary",
        reviewers: "inputs.reviewers",
        status: "pending",
        created_at: "now()"
      }
    },
    {
      function: "Notify Reviewers",
      loop: "inputs.reviewers",
      email_template: "code-review-request",
      variables: {
        author_name: "auth.user.name",
        branch: "inputs.branch",
        summary: "inputs.summary",
        review_url: "generate_review_url(code_review.id)"
      }
    }
  ],
  
  // Approve changes
  approveReview: [
    {
      function: "Validate Reviewer",
      logic: `
        const review = await getCodeReview(inputs.review_id);
        
        if (!review.reviewers.includes(auth.user.id)) {
          return error(403, "You are not assigned as a reviewer");
        }
        
        if (review.author_id === auth.user.id) {
          return error(403, "Cannot review your own code");
        }
      `
    },
    {
      function: "Record Approval",
      action: "add_record", 
      table: "review_approvals",
      data: {
        review_id: "inputs.review_id",
        reviewer_id: "auth.user.id",
        status: "approved",
        comments: "inputs.comments",
        approved_at: "now()"
      }
    },
    {
      function: "Check All Approvals",
      logic: `
        const approvals = await getReviewApprovals(inputs.review_id);
        const review = await getCodeReview(inputs.review_id);
        
        if (approvals.length >= review.required_approvals) {
          await updateRecord("code_reviews", inputs.review_id, {
            status: "approved",
            approved_at: new Date()
          });
          
          // Auto-deploy if configured
          if (review.auto_deploy) {
            await triggerDeployment(review.branch);
          }
        }
      `
    }
  ]
};
```

### n8n Team Automation
```javascript
// n8n workflow: Team onboarding automation
{
  "name": "New Team Member Onboarding",
  "trigger": {
    "type": "xano-webhook",
    "event": "team_member_joined"
  },
  "nodes": [
    {
      "name": "Create Accounts",
      "type": "parallel",
      "branches": [
        {
          "name": "Slack Account",
          "type": "slack-api",
          "action": "invite_user",
          "email": "{{ $json.member.email }}"
        },
        {
          "name": "GitHub Access",
          "type": "github-api", 
          "action": "add_collaborator",
          "username": "{{ $json.member.github_username }}"
        },
        {
          "name": "Documentation Access",
          "type": "notion-api",
          "action": "share_workspace",
          "email": "{{ $json.member.email }}"
        }
      ]
    },
    {
      "name": "Send Welcome Package",
      "type": "email",
      "template": "team-welcome",
      "attachments": [
        "team-handbook.pdf",
        "development-guidelines.pdf"
      ]
    },
    {
      "name": "Schedule Check-in",
      "type": "calendar-api",
      "action": "create_event",
      "title": "New Member Check-in",
      "attendees": ["{{ $json.member.email }}", "{{ $json.manager.email }}"],
      "date": "{{ $moment().add(1, 'week').format() }}"
    }
  ]
}
```

## WeWeb Team Dashboard

### Team Management Interface
```javascript
// WeWeb team management component
const teamManagement = {
  data: {
    teamMembers: [],
    pendingInvitations: [],
    selectedMember: null,
    rolePermissions: {}
  },
  
  async mounted() {
    await this.loadTeamData();
    this.setupRealTimeUpdates();
  },
  
  methods: {
    async loadTeamData() {
      // Load team members
      this.teamMembers = await wwLib.executeWorkflow('get-team-members', {
        workspace_id: this.currentWorkspace.id
      });
      
      // Load pending invitations
      this.pendingInvitations = await wwLib.executeWorkflow('get-pending-invitations', {
        workspace_id: this.currentWorkspace.id
      });
      
      // Load role permissions
      this.rolePermissions = await wwLib.executeWorkflow('get-role-permissions');
    },
    
    async inviteMember(email, role) {
      try {
        const response = await wwLib.executeWorkflow('invite-team-member', {
          email: email,
          role: role,
          workspace_id: this.currentWorkspace.id
        });
        
        if (response.success) {
          this.showSuccess('Invitation sent successfully');
          await this.loadTeamData(); // Refresh data
        }
      } catch (error) {
        this.showError(error.message);
      }
    },
    
    async updateMemberRole(memberId, newRole) {
      const confirmed = await this.confirmAction(
        `Change member role to ${newRole}?`,
        'This will update their permissions immediately.'
      );
      
      if (confirmed) {
        const response = await wwLib.executeWorkflow('update-member-role', {
          member_id: memberId,
          new_role: newRole
        });
        
        if (response.success) {
          await this.loadTeamData();
          this.showSuccess('Member role updated');
        }
      }
    },
    
    async removeMember(memberId) {
      const confirmed = await this.confirmAction(
        'Remove team member?',
        'This action cannot be undone.'
      );
      
      if (confirmed) {
        await wwLib.executeWorkflow('remove-team-member', {
          member_id: memberId
        });
        
        await this.loadTeamData();
        this.showSuccess('Member removed from team');
      }
    },
    
    setupRealTimeUpdates() {
      // Listen for team changes
      wwLib.realtime.subscribe('team-updates', {
        onMemberJoined: (data) => {
          this.teamMembers.push(data.member);
          this.showNotification(`${data.member.name} joined the team`);
        },
        onMemberLeft: (data) => {
          this.teamMembers = this.teamMembers.filter(m => m.id !== data.member_id);
          this.showNotification(`Team member left`);
        },
        onRoleChanged: (data) => {
          const member = this.teamMembers.find(m => m.id === data.member_id);
          if (member) {
            member.role = data.new_role;
            this.showNotification(`${member.name}'s role updated to ${data.new_role}`);
          }
        }
      });
    }
  }
};
```

## Activity Monitoring and Audit

### Comprehensive Audit Logging
```javascript
// Audit logging system
function logTeamActivity(activityData) {
  return {
    function: "Log Team Activity",
    action: "add_record",
    table: "team_audit_logs",
    data: {
      user_id: activityData.user_id,
      workspace_id: activityData.workspace_id,
      action: activityData.action,
      resource_type: activityData.resource_type,
      resource_id: activityData.resource_id,
      details: JSON.stringify(activityData.details),
      ip_address: activityData.ip_address,
      user_agent: activityData.user_agent,
      timestamp: "now()"
    }
  };
}

// Activity monitoring dashboard data
function getTeamActivitySummary(timeframe = '7d') {
  const query = `
    SELECT 
      u.name as user_name,
      u.email,
      tm.role,
      COUNT(*) as activity_count,
      MAX(tal.timestamp) as last_activity,
      GROUP_CONCAT(DISTINCT tal.action) as actions
    FROM team_audit_logs tal
    JOIN users u ON tal.user_id = u.id  
    JOIN team_members tm ON tal.user_id = tm.user_id
    WHERE tal.timestamp >= DATE_SUB(NOW(), INTERVAL ? DAY)
      AND tal.workspace_id = ?
    GROUP BY tal.user_id
    ORDER BY activity_count DESC
  `;
  
  return executeQuery(query, [parseInt(timeframe), workspace.id]);
}
```

## Try This: Set Up Team Management

1. **Create Team Roles**
   - Define custom roles with specific permissions
   - Set up approval workflows for sensitive operations
   - Test permission boundaries

2. **Build Invitation System**
   - Create invitation email templates
   - Set up token-based acceptance flow
   - Add expiration and security measures

3. **Implement Audit Logging**
   - Track all team activities
   - Create monitoring dashboard in WeWeb
   - Set up alert notifications

4. **Integrate External Tools**
   - Connect Slack for notifications
   - Set up GitHub collaboration
   - Automate onboarding workflows

## Common Mistakes to Avoid

- **Overly complex permission systems** - Start simple and add complexity as needed
- **Missing audit trails** - Always log permission changes and sensitive actions
- **Poor invitation security** - Use secure tokens and expiration dates
- **Inadequate role separation** - Ensure clear boundaries between roles
- **Forgotten offboarding** - Create processes to revoke access when members leave

## Pro Tips

💡 **Use least privilege principle** - Start with minimal permissions and add as needed

💡 **Implement approval workflows** - Require approvals for production deployments

💡 **Monitor team activity** - Set up dashboards to track collaboration patterns

💡 **Automate routine tasks** - Use n8n workflows for onboarding and notifications

💡 **Regular permission audits** - Review and update team permissions quarterly