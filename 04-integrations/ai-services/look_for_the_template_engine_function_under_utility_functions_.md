---
title: Template Engine Setup - Dynamic Content Generation with Twig
description: Complete guide to setting up and using Xano's Template Engine powered by Twig for dynamic content generation, AI prompts, HTML templates, and email automation
category: ai-services
difficulty: beginner
last_updated: '2025-01-16'
related_docs:
  - ai-tools.md
  - templates.md
  - mcp-functions.md
subcategory: 04-integrations/ai-services
tags:
  - template-engine
  - twig
  - dynamic-content
  - email-templates
  - ai-prompts
  - content-generation
  - no-code
---

## 📋 **Quick Summary**

The Template Engine in Xano is powered by Twig and enables dynamic content generation for emails, AI prompts, HTML, and other large-format text. Perfect for creating personalized content, complex data transformations, and automated messaging in n8n, WeWeb, and other no-code platforms. Use it when you need conditional logic, loops, and sophisticated formatting beyond simple string replacement.

## What You'll Learn

- How to add and configure the Template Engine function
- Template syntax including variables, conditionals, and loops
- When to use Template Engine vs simple text filters
- Security best practices with escape filters
- Integration patterns for no-code platforms
- Real-world examples for email and AI prompt generation

# Template Engine Setup Guide

## Overview

The Template Engine is a powerful utility function that generates dynamic content using the Twig templating language. Unlike simple text filters that work well for short string replacements, the Template Engine excels at creating complex, conditional content with loops, data formatting, and sophisticated logic.

### When to Use Template Engine

**✅ Use Template Engine for:**
- Templates edited by non-developers
- Complex data structures with nested objects
- Conditional sections and dynamic content
- Consistent data formatting (dates, numbers)
- Templates reused with different data sources
- Long-form content like emails or AI prompts

**❌ Use simple filters for:**
- Short string replacements like "Hello, [first_name] [last_name]"
- Single value substitutions like pricing
- Simple concatenation operations

## 🚀 **Setting Up Template Engine**

### Step 1: Add Template Engine Function

1. **Navigate to Function Stack**: Open your API endpoint or function stack
2. **Find Utility Functions**: Look for the Template Engine function under **Utility Functions**
3. **Add to Stack**: Drag the Template Engine function into your stack

### Step 2: Configure the Editor

1. **Open Editor**: Click the ✏️ button in the Template Engine panel
2. **Choose Method**: 
   - Use the visual editor for building templates manually
   - Use the AI assistant to help write templates automatically
3. **Build Template**: Start creating your template using Twig syntax

### Step 3: Test Your Template

1. **Provide Sample Data**: Add test data to preview your template
2. **Validate Output**: Ensure the generated content meets your needs
3. **Deploy**: Save and use your template in production

## 🔗 **No-Code Platform Integration**

### n8n Email Automation

**Dynamic Email Template with Xano:**

```javascript
// n8n HTTP Request node for email generation
{
  "method": "POST",
  "url": "https://your-xano-instance.com/api/generate-email",
  "headers": {
    "Authorization": "Bearer {{ $json.auth_token }}",
    "Content-Type": "application/json"
  },
  "body": {
    "customer": {
      "name": "{{ $json.customer_name }}",
      "email": "{{ $json.customer_email }}",
      "vip": "{{ $json.is_vip }}"
    },
    "order": {
      "id": "{{ $json.order_id }}",
      "items": "{{ $json.order_items }}",
      "total": "{{ $json.order_total }}"
    },
    "template_type": "order_confirmation"
  }
}
```

### WeWeb Dynamic Content

**Template Engine Integration Component:**

```javascript
// WeWeb component for dynamic content generation
class XanoTemplateEngine {
  constructor(xanoBaseUrl, authToken) {
    this.baseUrl = xanoBaseUrl;
    this.authToken = authToken;
  }
  
  async generateContent(templateData, templateType = 'default') {
    try {
      const response = await fetch(`${this.baseUrl}/api/generate-template`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.authToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          template_type: templateType,
          data: templateData,
          format: 'html'
        })
      });
      
      const result = await response.json();
      return result.generated_content;
    } catch (error) {
      console.error('Template generation failed:', error);
      return 'Content generation unavailable';
    }
  }
  
  async generatePersonalizedEmail(customerData, orderData) {
    const templateData = {
      customer: customerData,
      order: orderData,
      current_date: new Date().toISOString()
    };
    
    const emailContent = await this.generateContent(templateData, 'email_template');
    
    // Update WeWeb variables
    wwLib.wwVariable.updateValue('generated_email', emailContent);
    
    return emailContent;
  }
}

// Usage in WeWeb
const templateEngine = new XanoTemplateEngine(
  wwLib.wwVariable.getValue('xano_base_url'),
  wwLib.wwVariable.getValue('auth_token')
);

async function createPersonalizedMessage() {
  const customer = wwLib.wwVariable.getValue('current_customer');
  const order = wwLib.wwVariable.getValue('current_order');
  
  const personalizedContent = await templateEngine.generatePersonalizedEmail(customer, order);
  
  // Display in UI
  wwLib.wwVariable.updateValue('message_content', personalizedContent);
}
```

## 📝 **Template Syntax Reference**

### Variables

Variables use `{{ }}` syntax and begin with `$`:

```twig
Hi, {{ $user.name }}!
Your account balance is ${{ $user.balance }}.
```

**Array Access:**
```twig
Welcome {{ $users[0].first_name }}!
Your first item is: {{ $cart.items[0].name }}
```

### Conditionals

Use `{% %}` for logic with support for `else` and `elseif`:

```twig
{% if $user.vip %}
  Welcome back, VIP member {{ $user.name }}!
  You have access to exclusive deals.
{% else %}
  Hi {{ $user.name }}! 
  Upgrade to VIP for exclusive benefits.
{% endif %}
```

**Multiple Conditions:**
```twig
{% if $score >= 90 %}
  Your grade is an A - Excellent work!
{% elseif $score >= 80 %}
  Your grade is a B - Good job!
{% elseif $score >= 70 %}
  Your grade is a C - Keep improving!
{% else %}
  Your grade is an F - Please see your instructor.
{% endif %}
```

### Loops

Perfect for dynamic lists without knowing the item count:

```twig
Your Order Summary:
{% for item in $order_items %}
  - {{ item.quantity }}x {{ item.name }} at ${{ item.price }} each
{% endfor %}

Total: ${{ $order.total }}
```

**Loop with Else (empty state):**
```twig
{% for notification in $notifications %}
  • {{ notification.message }}
{% else %}
  No new notifications.
{% endfor %}
```

### Filters

Transform data using Twig's built-in filters:

| Filter | Description | Example | Result |
|--------|-------------|---------|--------|
| `upper` | Convert to uppercase | `{{ $user.name\|upper }}` | "JOHN SMITH" |
| `lower` | Convert to lowercase | `{{ $user.name\|lower }}` | "john smith" |
| `trim` | Remove whitespace | `{{ $user.input\|trim }}` | "hello" |
| `join` | Join array with delimiter | `{{ $tags\|join(', ') }}` | "php, twig, web" |
| `default` | Fallback value | `{{ $middle_name\|default('N/A') }}` | "N/A" |
| `number_format` | Format numbers | `{{ $price\|number_format }}` | "1,234.56" |
| `date` | Format dates | `{{ $created_at\|date('F j, Y') }}` | "December 25, 2023" |

## 🔐 **Security with Escape Filters**

Always escape user input to prevent security issues:

### HTML Escaping
```twig
{# Safe HTML output #}
<p>{{ $user_comment|e('html') }}</p>

{# Converts: <script>alert("XSS");</script> #}
{# To: &lt;script&gt;alert(&quot;XSS&quot;);&lt;/script&gt; #}
```

### JavaScript Escaping
```twig
<script>
var userName = "{{ $user.name|e('js') }}";
</script>
```

### URL Escaping
```twig
<a href="https://example.com/search?q={{ $search_query|e('url') }}">
  Search Results
</a>
```

### CSS Escaping
```twig
<style>
.user-theme {
  color: {{ $user_color|e('css') }};
}
</style>
```

## 🛠️ **Practical Examples**

### Example 1: Order Confirmation Email

**Template:**
```twig
Subject: Order Confirmation #{{ $order.id }}

Dear {{ $customer.first_name }},

Thank you for your order! Here are the details:

{% if $order.status == 'confirmed' %}
✅ Your order has been confirmed and is being processed.
{% elseif $order.status == 'shipped' %}
📦 Great news! Your order has shipped.
Tracking: {{ $order.tracking_number }}
{% endif %}

Order Items:
{% for item in $order.items %}
• {{ item.quantity }}x {{ item.name }} - ${{ item.price|number_format }}
{% endfor %}

Subtotal: ${{ $order.subtotal|number_format }}
{% if $order.discount > 0 %}
Discount: -${{ $order.discount|number_format }}
{% endif %}
Tax: ${{ $order.tax|number_format }}
Total: ${{ $order.total|number_format }}

{% if $customer.vip %}
🌟 VIP Shipping: FREE 2-day delivery included!
{% else %}
Shipping: ${{ $order.shipping|number_format }}
{% endif %}

Estimated delivery: {{ $order.estimated_delivery|date('F j, Y') }}

Thank you for choosing us!
{{ $store.name }} Team
```

### Example 2: AI Prompt Generation

**Dynamic AI Prompt Template:**
```twig
Generate a {{ $content_type }} about {{ $topic }} with the following requirements:

Tone: {{ $tone|default('professional') }}
Length: {{ $length|default('medium') }}
Audience: {{ $audience|default('general') }}

{% if $keywords %}
Include these keywords:
{% for keyword in $keywords %}
- {{ keyword }}
{% endfor %}
{% endif %}

{% if $examples %}
Reference these examples:
{% for example in $examples %}
• {{ example.title }}: {{ example.description }}
{% endfor %}
{% endif %}

{% if $constraints %}
Additional constraints:
{% for constraint in $constraints %}
- {{ constraint }}
{% endfor %}
{% endif %}

Output format: {{ $output_format|default('markdown') }}
```

### Example 3: Dynamic HTML Report

**Business Report Template:**
```twig
<!DOCTYPE html>
<html>
<head>
  <title>{{ $report.title }} - {{ $report.date|date('F Y') }}</title>
  <style>
    .metric { margin: 20px 0; padding: 15px; border-left: 4px solid #007cba; }
    .positive { color: green; }
    .negative { color: red; }
  </style>
</head>
<body>
  <h1>{{ $report.title }}</h1>
  <p>Generated on {{ $report.generated_at|date('F j, Y g:i A') }}</p>
  
  <h2>Key Metrics</h2>
  {% for metric in $report.metrics %}
  <div class="metric">
    <h3>{{ metric.name }}</h3>
    <p>Current: {{ metric.current|number_format }}</p>
    {% if metric.change %}
    <p class="{{ metric.change > 0 ? 'positive' : 'negative' }}">
      Change: {{ metric.change > 0 ? '+' : '' }}{{ metric.change|number_format }}
      ({{ metric.change_percent|number_format }}%)
    </p>
    {% endif %}
  </div>
  {% endfor %}
  
  {% if $report.insights %}
  <h2>Insights</h2>
  <ul>
    {% for insight in $report.insights %}
    <li>{{ insight|e('html') }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</body>
</html>
```

## 🎯 **Function Stack Implementation**

### Complete Email Generation Function Stack

```javascript
[
  {
    "function": "get_record",
    "table": "customers",
    "id": "{{ request.body.customer_id }}"
  },
  {
    "function": "get_record", 
    "table": "orders",
    "id": "{{ request.body.order_id }}"
  },
  {
    "function": "query_all_records",
    "table": "order_items",
    "filter": {
      "order_id": "{{ order.id }}"
    }
  },
  {
    "function": "template_engine",
    "template": "order_confirmation_email",
    "data": {
      "customer": "{{ customer }}",
      "order": "{{ order }}",
      "items": "{{ order_items }}",
      "store": {
        "name": "{{ env.STORE_NAME }}",
        "support_email": "{{ env.SUPPORT_EMAIL }}"
      }
    },
    "return_as": "email_content"
  },
  {
    "function": "external_api_request",
    "url": "{{ env.EMAIL_SERVICE_URL }}",
    "method": "POST",
    "body": {
      "to": "{{ customer.email }}",
      "subject": "Order Confirmation #{{ order.id }}",
      "html": "{{ email_content }}"
    }
  }
]
```

## 💡 **Pro Tips**

### Performance Optimization
- **Cache Templates**: Store frequently used templates for faster generation
- **Minimize Data**: Only pass necessary data to avoid processing overhead
- **Use Filters Wisely**: Apply filters efficiently to reduce computation

### Best Practices
- **Always Escape**: Use appropriate escape filters for security
- **Test Edge Cases**: Verify templates work with empty or null data
- **Keep It Simple**: Break complex templates into smaller, reusable components
- **Document Templates**: Add comments to explain complex logic

### Common Patterns
```twig
{# Comments for documentation #}
{# This template generates personalized recommendations #}

{# Fallback for missing data #}
{{ $user.name|default('Valued Customer') }}

{# Safe null checking #}
{% if $user.preferences %}
  Your preferences: {{ $user.preferences|join(', ') }}
{% endif %}

{# Number formatting with fallbacks #}
Price: ${{ $product.price|default(0)|number_format }}
```

## 🔧 **Troubleshooting**

### Common Issues

**Problem**: Variables not rendering  
**Solution**: Ensure variables use `$` prefix and correct object notation

**Problem**: Conditionals not working  
**Solution**: Check syntax - use `{% %}` for logic, not `{{ }}`

**Problem**: Loops producing no output  
**Solution**: Verify array data exists and use `{% else %}` for empty states

**Problem**: Formatting issues  
**Solution**: Apply appropriate filters and escape user input

---

**Next Steps**: Ready to create dynamic content? Explore [AI Tools](ai-tools.md) for more template patterns or check out [Templates](templates.md) for pre-built examples