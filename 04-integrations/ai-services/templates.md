---
title: AI Agent Templates - Pre-Built Solutions for Common Use Cases
description: Ready-to-use AI agent templates for customer support, e-commerce, content moderation, and business automation workflows
category: ai-services
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - agents.md
  - ai-tools.md
  - mcp-functions.md
subcategory: 04-integrations/ai-services
tags:
  - templates
  - agent-templates
  - automation
  - customer-support
  - e-commerce
  - no-code
---

## 📋 **Quick Summary**

AI Agent Templates provide pre-built, ready-to-use agent configurations for common business scenarios. These templates include system prompts, tool configurations, and workflow patterns that you can customize for your specific needs. Perfect for quickly implementing AI automation in n8n, WeWeb, and other no-code platforms.

## What You'll Learn

- How to use pre-built agent templates for faster deployment
- Customizing templates for your specific business needs
- Template categories: support, e-commerce, content, and automation
- Best practices for template modification and optimization
- Integration patterns with no-code platforms

# AI Agent Templates

## Overview

Agent templates are pre-configured AI agents designed for specific business use cases. Instead of building agents from scratch, you can start with proven templates and customize them for your needs. Each template includes:

- **System Prompt**: Carefully crafted instructions for optimal performance
- **Tool Configuration**: Pre-selected tools for the specific use case
- **Example Interactions**: Sample conversations and responses
- **Integration Guidelines**: Best practices for implementation
- **Customization Tips**: How to adapt the template to your business

## Template Categories

### 🎧 **Customer Support Templates**

#### Basic Support Agent
**Use Case**: Handle common customer inquiries and escalate complex issues

**Configuration:**
```javascript
{
  "name": "Basic Support Agent",
  "system_prompt": "You are a helpful customer support representative. Always be polite, professional, and solution-oriented. If you cannot resolve an issue, escalate to human support.",
  "tools": [
    "get_customer_info",
    "check_order_status", 
    "update_customer_details",
    "create_support_ticket"
  ],
  "max_steps": 5
}
```

#### Advanced Support Agent with Sentiment Analysis
**Use Case**: Intelligent customer support with emotion detection and personalized responses

**Configuration:**
```javascript
{
  "name": "Advanced Support Agent",
  "system_prompt": "You are an empathetic customer support agent with sentiment analysis capabilities. Adjust your tone based on customer emotions and provide personalized assistance.",
  "tools": [
    "analyze_customer_sentiment",    // MCP tool
    "get_customer_profile",
    "access_knowledge_base",
    "process_refund_request",
    "escalate_to_supervisor"
  ],
  "structured_outputs": true,
  "output_schema": {
    "response": "string",
    "sentiment_detected": "string",
    "escalation_needed": "boolean",
    "follow_up_required": "boolean"
  }
}
```

### 🛒 **E-commerce Templates**

#### Order Management Agent
**Use Case**: Handle order inquiries, modifications, and shipping updates

**Configuration:**
```javascript
{
  "name": "Order Management Agent",
  "system_prompt": "You help customers with order-related inquiries. Always verify order details before making changes. Explain shipping policies clearly.",
  "tools": [
    "lookup_order_details",
    "track_shipment",
    "modify_shipping_address",
    "process_order_cancellation",
    "calculate_return_window"
  ]
}
```

#### Product Recommendation Agent
**Use Case**: Provide personalized product recommendations based on customer preferences

**Configuration:**
```javascript
{
  "name": "Product Recommendation Agent", 
  "system_prompt": "You are a knowledgeable product advisor. Ask clarifying questions to understand customer needs and provide tailored recommendations.",
  "tools": [
    "get_customer_history",
    "search_product_catalog",
    "compare_products",
    "check_inventory",
    "apply_discounts"
  ]
}
```

### 📝 **Content Management Templates**

#### Content Moderation Agent
**Use Case**: Automatically review and moderate user-generated content

**Configuration:**
```javascript
{
  "name": "Content Moderation Agent",
  "system_prompt": "You review content for policy compliance. Flag inappropriate content and provide clear explanations for moderation decisions.",
  "tools": [
    "analyze_text_toxicity",      // MCP tool
    "detect_spam_patterns",       // MCP tool
    "check_content_guidelines",
    "escalate_borderline_content",
    "log_moderation_decision"
  ],
  "structured_outputs": true,
  "output_schema": {
    "approved": "boolean",
    "reason": "string",
    "confidence": "number",
    "requires_human_review": "boolean"
  }
}
```

#### SEO Content Assistant
**Use Case**: Help optimize content for search engines

**Configuration:**
```javascript
{
  "name": "SEO Content Assistant",
  "system_prompt": "You help optimize content for SEO. Analyze content structure, suggest improvements, and recommend keywords while maintaining readability.",
  "tools": [
    "analyze_keyword_density",    // MCP tool
    "check_readability_score",    // MCP tool
    "suggest_meta_descriptions",
    "optimize_headings",
    "generate_schema_markup"
  ]
}
```

### 🔧 **Business Automation Templates**

#### Data Analysis Agent
**Use Case**: Analyze business data and generate insights

**Configuration:**
```javascript
{
  "name": "Business Intelligence Agent",
  "system_prompt": "You analyze business data to provide actionable insights. Present findings clearly with supporting data and recommendations.",
  "tools": [
    "query_sales_database",
    "calculate_growth_metrics",
    "generate_trend_analysis",
    "create_data_visualizations",
    "export_reports"
  ]
}
```

#### Appointment Scheduling Agent
**Use Case**: Manage calendar appointments and scheduling

**Configuration:**
```javascript
{
  "name": "Scheduling Assistant",
  "system_prompt": "You help schedule and manage appointments. Always confirm details and send calendar invitations.",
  "tools": [
    "check_calendar_availability",
    "book_appointment",
    "send_confirmation_email",
    "reschedule_meeting",
    "cancel_appointment"
  ]
}
```

## 🔗 **No-Code Platform Integration**

### n8n Template Integration

**Workflow Setup for Customer Support Template:**

```javascript
// n8n workflow configuration
{
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "Webhook",
      "parameters": {
        "path": "customer-support"
      }
    },
    {
      "name": "Call Support Agent",
      "type": "HTTP Request",
      "parameters": {
        "url": "https://your-xano-instance.com/api/support-agent",
        "method": "POST",
        "body": {
          "template": "basic_support_agent",
          "customer_inquiry": "{{ $json.message }}",
          "customer_id": "{{ $json.customer_id }}"
        }
      }
    },
    {
      "name": "Route Response",
      "type": "Switch",
      "parameters": {
        "conditions": [
          {
            "condition": "{{ $json.escalation_needed }}",
            "action": "notify_human_agent"
          },
          {
            "condition": "{{ $json.follow_up_required }}",
            "action": "schedule_follow_up"
          }
        ]
      }
    }
  ]
}
```

### WeWeb Template Integration

**Frontend Component for E-commerce Template:**

```javascript
// WeWeb component for product recommendations
async function getProductRecommendations(customerData) {
  try {
    const response = await fetch(`${wwLib.wwVariable.getValue('xano_base_url')}/api/recommendation-agent`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${wwLib.wwVariable.getValue('auth_token')}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        template: "product_recommendation_agent",
        customer_preferences: customerData.preferences,
        purchase_history: customerData.history,
        current_context: customerData.browsing_context
      })
    });
    
    const recommendations = await response.json();
    
    // Update product display
    wwLib.wwVariable.updateValue('recommended_products', recommendations.products);
    wwLib.wwVariable.updateValue('recommendation_reasoning', recommendations.explanation);
    
    return recommendations;
  } catch (error) {
    console.error('Recommendation agent failed:', error);
    return { products: [], explanation: 'Recommendations unavailable' };
  }
}
```

## Template Customization Guide

### Step 1: Choose Base Template

1. **Identify Your Use Case**: Select the template that best matches your needs
2. **Review Template Components**: Understand the system prompt, tools, and configuration
3. **Check Dependencies**: Ensure required tools and integrations are available

### Step 2: Customize System Prompt

**Example Customization:**
```javascript
// Original template prompt
"You are a helpful customer support representative."

// Customized for your brand
"You are a friendly support agent for TechCorp. Our values are innovation, reliability, and customer success. Always mention our 30-day guarantee when relevant."
```

### Step 3: Modify Tool Configuration

**Add Business-Specific Tools:**
```javascript
{
  "tools": [
    // Standard template tools
    "get_customer_info",
    "check_order_status",
    
    // Your custom tools
    "check_loyalty_points",
    "apply_vip_discount",
    "schedule_tech_support"
  ]
}
```

### Step 4: Configure Output Format

**Structure Outputs for Your Workflow:**
```javascript
{
  "structured_outputs": true,
  "output_schema": {
    "customer_response": "string",
    "internal_notes": "string",
    "priority_level": "number",
    "department_routing": "string",
    "follow_up_date": "string"
  }
}
```

## Template Best Practices

### Performance Optimization

1. **Minimize Tool Count**: Use only necessary tools to reduce response time
2. **Optimize Prompts**: Keep system prompts focused and specific
3. **Set Appropriate Limits**: Configure max_steps based on complexity
4. **Cache Common Responses**: Store frequently used responses

### Quality Assurance

1. **Test with Real Data**: Use actual customer scenarios for testing
2. **Monitor Performance**: Track response quality and user satisfaction
3. **Iterate Based on Feedback**: Continuously improve based on results
4. **Document Changes**: Keep track of customizations and improvements

### Security Considerations

1. **Validate Inputs**: Always sanitize and validate user inputs
2. **Limit Tool Permissions**: Grant minimal necessary permissions
3. **Monitor Usage**: Track agent activity for unusual patterns
4. **Secure Integrations**: Use proper authentication for all connections

## 🎯 **Try This**

**Quick Template Implementation:**

1. **Choose a Template**: Start with the Basic Support Agent template
2. **Customize the Prompt**: Add your brand voice and specific policies
3. **Configure Tools**: Select 3-4 tools relevant to your business
4. **Test Interactions**: Try various customer scenarios
5. **Deploy and Monitor**: Implement in your chosen platform and track performance

## Common Template Modifications

### Adding Multi-Language Support

```javascript
{
  "system_prompt": "You support customers in multiple languages. Always respond in the customer's language. Use translation tools when needed.",
  "tools": [
    "detect_language",        // MCP tool
    "translate_message",      // MCP tool
    "get_localized_responses"
  ]
}
```

### Implementing Escalation Rules

```javascript
{
  "escalation_rules": {
    "high_value_customer": "immediate_human_escalation",
    "complex_technical_issue": "tier_2_support",
    "billing_dispute": "accounting_team",
    "urgent_order_issue": "priority_queue"
  }
}
```

### Adding Integration Hooks

```javascript
{
  "integration_hooks": {
    "before_response": "log_interaction",
    "after_resolution": "update_customer_satisfaction", 
    "on_escalation": "notify_supervisor",
    "on_error": "alert_technical_team"
  }
}
```

---

**Next Steps**: Ready to implement a template? Start with [AI Agents](agents.md) to learn the fundamentals, or explore [AI Tools](ai-tools.md) for advanced customization options
