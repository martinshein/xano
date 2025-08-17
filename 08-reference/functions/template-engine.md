---
title: Template Engine Functions Reference
description: Complete guide to the Xano Template Engine powered by Twig - dynamic text generation, templating, and content manipulation for no-code platforms
category: functions
subcategory: 08-reference/functions
tags:
- template-engine
- twig-templating
- dynamic-content
- text-generation
- ai-prompts
- html-generation
- email-templates
- sql-templates
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-08-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 02-core-concepts/function-stack/text.md
- 08-reference/functions/emails.md
- 08-reference/functions/chatbots.md
---

## 📋 **Quick Summary**

The Template Engine in Xano, powered by Twig, enables dynamic text generation and content manipulation for creating AI prompts, HTML pages, emails, and other large-format content with complex data structures and conditional logic.

## What You'll Learn

- How to use the Template Engine for dynamic content generation
- Twig templating syntax including variables, conditionals, and loops
- Creating templates for AI prompts, HTML, emails, and SQL queries
- Integration patterns for n8n, WeWeb, and Make.com platforms
- Advanced templating features and best practices
- Template security and escaping strategies
- Troubleshooting common templating issues

## Understanding the Template Engine

### Template Engine Overview

**What is the Template Engine:**
- Powerful text replacement and manipulation system
- Powered by Twig templating language
- Designed for complex data structures and large text blocks
- Superior to simple text filters for sophisticated templating needs

**Use Cases:**
- **AI Prompts**: Dynamic prompt generation with context and constraints
- **HTML Generation**: Dynamic web pages and email templates
- **SQL Queries**: Flexible database query construction
- **JSON/XML**: Structured data format generation
- **Markdown**: Documentation and content generation

### When to Use Template Engine vs Text Filters

```javascript
// Decision matrix for templating approach
{
  "use_text_filters": {
    "scenarios": [
      "Simple string replacement (Hello, [name])",
      "Short text manipulations",
      "Single value substitutions",
      "Basic formatting operations"
    ],
    "examples": ["replace", "sprintf", "concat"]
  },
  "use_template_engine": {
    "scenarios": [
      "Complex nested data structures",
      "Conditional content sections",
      "Loop-based content generation",
      "Multi-format output requirements",
      "Templates edited by non-developers",
      "Reusable templates with different data sources"
    ],
    "advantages": [
      "Rich syntax for complex logic",
      "Built-in security features",
      "Extensive filtering capabilities",
      "Template inheritance support"
    ]
  }
}
```

## Basic Template Engine Implementation

### 1. Setting Up Template Engine

```javascript
// Using Template Engine in function stack
{
  "function": "generate_dynamic_content",
  "data_source": "{{input_data}}",
  "function_stack": [
    {
      "function": "query_all_records",
      "table": "products",
      "filter": {"status": "active"}
    },
    {
      "function": "get_record",
      "table": "users",
      "record_id": "{{auth.user.id}}"
    },
    {
      "function": "template_engine",
      "template": "{{product_listing_template}}",
      "variables": {
        "user": "{{users}}",
        "products": "{{products}}",
        "page_title": "Product Catalog",
        "current_date": "{{now()}}"
      }
    }
  ]
}
```

### 2. Basic Variable Usage

```javascript
// Template syntax for variable replacement
{
  "basic_variables": {
    "simple_variable": "Hi, {{ $user.name }}",
    "object_property": "Email: {{ $user.profile.email }}",
    "array_element": "First item: {{ $items[0] }}",
    "nested_object": "Address: {{ $user.address.street }}, {{ $user.address.city }}"
  },
  "variable_examples": {
    "user_data": {
      "name": "John Smith",
      "email": "john@example.com",
      "vip_status": true,
      "orders": [
        {"id": 1, "total": 99.99},
        {"id": 2, "total": 149.50}
      ]
    },
    "template_output": "Welcome {{ $user.name }}! Your last order was ${{ $user.orders[0].total }}"
  }
}
```

### 3. Conditional Logic Implementation

```javascript
// Advanced conditional templating
{
  "conditional_templates": {
    "basic_if": `
      {% if $user.vip_status %}
        Welcome to our VIP section, {{ $user.name }}!
      {% else %}
        Welcome {{ $user.name }}! Consider upgrading to VIP.
      {% endif %}
    `,
    "multiple_conditions": `
      {% if $order.total >= 100 %}
        You qualify for free shipping!
      {% elseif $order.total >= 50 %}
        Add ${{ 100 - $order.total }} for free shipping.
      {% else %}
        Minimum order for free shipping is $100.
      {% endif %}
    `,
    "complex_logic": `
      {% if $user.subscription.status == 'active' and $user.subscription.tier == 'premium' %}
        Premium features unlocked!
      {% elseif $user.subscription.status == 'expired' %}
        Your subscription has expired. Renew now!
      {% else %}
        Upgrade to premium for advanced features.
      {% endif %}
    `
  }
}
```

## Advanced Template Features

### 1. Loop Operations and List Generation

```javascript
// Comprehensive loop templating
{
  "loop_templates": {
    "product_listing": `
      <h2>Available Products</h2>
      {% for $product in $products %}
        <div class="product">
          <h3>{{ $product.name }}</h3>
          <p>Price: ${{ $product.price|number_format(2) }}</p>
          {% if $product.in_stock %}
            <button>Add to Cart</button>
          {% else %}
            <span class="out-of-stock">Out of Stock</span>
          {% endif %}
        </div>
      {% else %}
        <p>No products available.</p>
      {% endfor %}
    `,
    "order_summary": `
      Order Summary:
      {% for $item in $order.items %}
        - {{ $item.quantity }}x {{ $item.name }} at ${{ $item.price }} each
          Subtotal: ${{ $item.quantity * $item.price }}
      {% endfor %}
      
      Total: ${{ $order.total }}
    `,
    "conditional_loop": `
      {% for $notification in $notifications %}
        {% if $notification.priority == 'high' %}
          🚨 URGENT: {{ $notification.message }}
        {% elseif $notification.priority == 'medium' %}
          ⚠️ {{ $notification.message }}
        {% else %}
          ℹ️ {{ $notification.message }}
        {% endif %}
      {% endfor %}
    `
  }
}
```

### 2. Template Filters and Data Transformation

```javascript
// Built-in Twig filters for data manipulation
{
  "filter_examples": {
    "text_formatting": {
      "uppercase": "{{ $user.name|upper }}", // "JOHN SMITH"
      "lowercase": "{{ $user.email|lower }}", // "john@example.com"
      "title_case": "{{ $product.name|title }}", // "Blue T-Shirt"
      "trim_whitespace": "{{ $user.input|trim }}" // Remove leading/trailing spaces
    },
    "number_formatting": {
      "currency": "${{ $product.price|number_format(2) }}", // "$19.99"
      "percentage": "{{ $discount|number_format(1) }}%", // "15.0%"
      "thousands": "{{ $revenue|number_format }}" // "1,234,567"
    },
    "array_operations": {
      "join_elements": "{{ $tags|join(', ') }}", // "php, twig, web"
      "array_length": "{{ $items|length }} items",
      "first_element": "{{ $products|first.name }}",
      "last_element": "{{ $orders|last.date }}"
    },
    "date_formatting": {
      "formatted_date": "{{ $order.created_at|date('F j, Y') }}", // "January 15, 2025"
      "time_format": "{{ $timestamp|date('g:i A') }}", // "3:30 PM"
      "iso_date": "{{ $event.date|date('c') }}" // ISO 8601 format
    },
    "default_values": {
      "fallback_text": "{{ $user.middle_name|default('N/A') }}",
      "empty_array": "{{ $items|default([]) }}",
      "null_handling": "{{ $optional_field|default('Not specified') }}"
    }
  }
}
```

### 3. Security and Escaping

```javascript
// Template security and proper escaping
{
  "security_features": {
    "html_escaping": {
      "basic_escape": "{{ $user_input|e('html') }}",
      "prevent_xss": `
        {% set $comment = '<script>alert("XSS")</script>' %}
        {{ $comment|e('html') }}
        // Output: &lt;script&gt;alert(&quot;XSS&quot;);&lt;/script&gt;
      `
    },
    "javascript_escaping": {
      "js_strings": "{{ $js_variable|e('js') }}",
      "json_data": `
        var userData = {{ $user|json_encode|raw }};
      `
    },
    "url_escaping": {
      "query_params": "?search={{ $search_term|e('url') }}",
      "safe_urls": "{{ $redirect_url|e('url') }}"
    },
    "css_escaping": {
      "style_values": "color: {{ $color_value|e('css') }};",
      "prevent_css_injection": "{{ $user_style|e('css') }}"
    }
  }
}
```

## Real-World Template Examples

### 1. AI Prompt Generation Template

```javascript
// Dynamic AI prompt creation
{
  "ai_prompt_template": `
    You are an AI assistant specialized in {{ $task.domain }}.
    
    Context:
    {% if $context %}
    {{ $context }}
    {% else %}
    *No additional context provided*
    {% endif %}
    
    Instructions:
    {% for $step in $instructions %}
    {{ loop.index }}. {{ $step }}
    {% endfor %}
    
    Constraints:
    {% for $constraint in $constraints %}
    - {{ $constraint }}
    {% endfor %}
    
    Input Data:
    {% if $input_format == 'json' %}
    ```json
    {{ $sample_input|json_encode(constant('JSON_PRETTY_PRINT')) }}
    ```
    {% else %}
    {{ $sample_input }}
    {% endif %}
    
    Expected Output Format:
    {{ $output_format }}
    
    {% if $examples %}
    Examples:
    {% for $example in $examples %}
    Input: {{ $example.input }}
    Output: {{ $example.output }}
    {% endfor %}
    {% endif %}
  `,
  "template_usage": {
    "variables": {
      "task": {"domain": "content generation"},
      "context": "Generate product descriptions for e-commerce",
      "instructions": [
        "Analyze the product features",
        "Write compelling copy",
        "Include SEO keywords"
      ],
      "constraints": [
        "Keep descriptions under 200 words",
        "Use active voice",
        "Include call-to-action"
      ]
    }
  }
}
```

### 2. Dynamic HTML Email Template

```javascript
// Email template with personalization
{
  "email_template": `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ $email.subject }}</title>
        <style>
            .header { background-color: {{ $brand.primary_color }}; padding: 20px; }
            .content { padding: 20px; font-family: Arial, sans-serif; }
            .footer { background-color: #f5f5f5; padding: 10px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1 style="color: white;">{{ $brand.name }}</h1>
        </div>
        
        <div class="content">
            <h2>Hi {{ $recipient.first_name }}!</h2>
            
            {% if $email.type == 'welcome' %}
                <p>Welcome to {{ $brand.name }}! We're excited to have you join our community.</p>
                <p>Here's what you can do next:</p>
                <ul>
                {% for $action in $onboarding_actions %}
                    <li>{{ $action.description }}</li>
                {% endfor %}
                </ul>
            {% elseif $email.type == 'order_confirmation' %}
                <p>Thank you for your order #{{ $order.id }}!</p>
                <h3>Order Details:</h3>
                {% for $item in $order.items %}
                <div>
                    {{ $item.quantity }}x {{ $item.name }} - ${{ $item.price|number_format(2) }}
                </div>
                {% endfor %}
                <p><strong>Total: ${{ $order.total|number_format(2) }}</strong></p>
            {% endif %}
            
            {% if $recipient.vip_status %}
            <div style="background-color: gold; padding: 10px; margin: 20px 0;">
                <p><strong>VIP Exclusive:</strong> {{ $vip_offer.description }}</p>
            </div>
            {% endif %}
        </div>
        
        <div class="footer">
            <p>&copy; {{ "now"|date("Y") }} {{ $brand.name }}. All rights reserved.</p>
            <p><a href="{{ $unsubscribe_url }}">Unsubscribe</a></p>
        </div>
    </body>
    </html>
  `
}
```

### 3. Dynamic SQL Query Template

```javascript
// Flexible SQL generation with security
{
  "sql_template": `
    SELECT 
        {{ $base_columns|join(', ') }}
        {% if $additional_columns %}
        , {{ $additional_columns|join(', ') }}
        {% endif %}
    FROM {{ $table_name|sql_alias }}
    WHERE 1=1
        {% if $user.role != 'admin' %}
        AND organization_id = {{ $user.organization_id|sql_esc }}
        {% endif %}
        {% if $filters.status %}
        AND status = '{{ $filters.status|sql_esc }}'
        {% endif %}
        {% if $filters.date_range %}
        AND created_at BETWEEN '{{ $filters.date_range.start|sql_esc }}' 
                           AND '{{ $filters.date_range.end|sql_esc }}'
        {% endif %}
        {% if $search_term %}
        AND (
            name LIKE '%{{ $search_term|sql_esc }}%' 
            OR description LIKE '%{{ $search_term|sql_esc }}%'
        )
        {% endif %}
    {% if $group_by %}
    GROUP BY {{ $group_by|join(', ') }}
    {% endif %}
    ORDER BY 
        {% if $sort_by %}
        {{ $sort_by|sql_alias }} {{ $sort_direction|default('ASC')|sql_esc }}
        {% else %}
        created_at DESC
        {% endif %}
    LIMIT {{ $limit|default(10)|abs }}
    {% if $offset %}
    OFFSET {{ $offset|abs }}
    {% endif %}
  `,
  "security_notes": {
    "sql_injection_prevention": [
      "Always use |sql_esc filter for user input",
      "Use |sql_alias for column/table names",
      "Validate numeric inputs with |abs filter",
      "Never concatenate raw user input"
    ]
  }
}
```

## No-Code Platform Integration

### n8n Template Automation
```javascript
// n8n workflow for template processing
{
  "n8n_template_workflow": {
    "webhook_url": "https://hooks.n8n.cloud/webhook/template-processor",
    "template_events": [
      {
        "event": "generate_report",
        "data": {
          "template_id": "{{template_id}}",
          "data_source": "{{data_source}}",
          "output_format": "{{format}}",
          "variables": "{{template_variables}}"
        }
      },
      {
        "event": "batch_template_processing",
        "data": {
          "templates": "{{template_batch}}",
          "processing_mode": "parallel",
          "error_handling": "continue_on_error"
        }
      }
    ]
  }
}
```

### WeWeb Template Components
```javascript
// WeWeb integration for template management
{
  "weweb_template_system": {
    "component": "template_processor",
    "api_endpoints": {
      "process_template": "/api/template/process",
      "save_template": "/api/template/save",
      "preview_template": "/api/template/preview"
    },
    "features": {
      "live_preview": true,
      "syntax_highlighting": true,
      "variable_autocomplete": true,
      "template_library": true
    },
    "template_editor": {
      "syntax_validation": "real_time",
      "variable_suggestions": "context_aware",
      "error_highlighting": "inline"
    }
  }
}
```

### Make.com Template Scenarios
```javascript
// Make.com automation for template workflows
{
  "make_template_automation": {
    "scenario_url": "https://hook.us1.make.com/template-automation",
    "automation_flows": [
      {
        "trigger": "new_data_available",
        "action": "regenerate_templates",
        "data": {
          "template_ids": "{{affected_templates}}",
          "data_source": "{{updated_data}}",
          "notification_channels": ["email", "slack"]
        }
      },
      {
        "trigger": "template_error",
        "condition": "{{error_count > 3}}",
        "action": "escalate_to_admin",
        "data": {
          "error_details": "{{error_log}}",
          "template_id": "{{failed_template}}",
          "suggested_fixes": "{{ai_suggestions}}"
        }
      }
    ]
  }
}
```

## Advanced Template Patterns

### 1. Template Inheritance and Composition

```javascript
// Advanced template architecture
{
  "template_inheritance": {
    "base_template": `
      <!DOCTYPE html>
      <html>
      <head>
          <title>{% block title %}Default Title{% endblock %}</title>
          {% block head %}{% endblock %}
      </head>
      <body>
          {% block header %}
          <header>{{ $site.name }}</header>
          {% endblock %}
          
          {% block content %}{% endblock %}
          
          {% block footer %}
          <footer>&copy; {{ "now"|date("Y") }}</footer>
          {% endblock %}
      </body>
      </html>
    `,
    "child_template": `
      {% extends "base_template" %}
      
      {% block title %}{{ $page.title }} - {{ parent() }}{% endblock %}
      
      {% block content %}
      <h1>{{ $page.title }}</h1>
      {{ $page.content }}
      {% endblock %}
    `
  }
}
```

### 2. Macro Functions and Reusable Components

```javascript
// Template macros for reusability
{
  "template_macros": {
    "form_field_macro": `
      {% macro input_field(name, type, label, value, required) %}
      <div class="form-field">
          <label for="{{ name }}">
              {{ label }}
              {% if required %}<span class="required">*</span>{% endif %}
          </label>
          <input 
              type="{{ type|default('text') }}" 
              id="{{ name }}" 
              name="{{ name }}" 
              value="{{ value|default('')|e('html') }}"
              {% if required %}required{% endif %}
          />
      </div>
      {% endmacro %}
    `,
    "macro_usage": `
      {% import "form_macros" as forms %}
      
      {{ forms.input_field('email', 'email', 'Email Address', $user.email, true) }}
      {{ forms.input_field('phone', 'tel', 'Phone Number', $user.phone, false) }}
    `
  }
}
```

### 3. Dynamic Template Loading

```javascript
// Runtime template selection and loading
{
  "dynamic_templates": {
    "template_selector": `
      {% set template_name = $user.preferences.email_template|default('default') %}
      {% set template_path = 'emails/' ~ template_name ~ '.twig' %}
      
      {% include template_path ignore missing %}
      {% if not template_exists %}
          {% include 'emails/default.twig' %}
      {% endif %}
    `,
    "conditional_includes": `
      {% if $feature_flags.new_ui %}
          {% include 'components/new_header.twig' %}
      {% else %}
          {% include 'components/legacy_header.twig' %}
      {% endif %}
    `
  }
}
```

## Try This: Complete Template System

Create a comprehensive template management system:

```javascript
// Complete template engine implementation
{
  "template_management_system": {
    "process_template": {
      "endpoint": "/api/template/process",
      "method": "POST",
      "inputs": [
        {"name": "template_id", "type": "text", "required": true},
        {"name": "variables", "type": "object", "required": true},
        {"name": "output_format", "type": "text", "default": "html"},
        {"name": "cache_enabled", "type": "boolean", "default": true}
      ],
      "function_stack": [
        {
          "function": "get_record",
          "table": "templates",
          "record_id": "{{template_id}}"
        },
        {
          "function": "validate_template_variables",
          "template": "{{templates.content}}",
          "provided_variables": "{{variables}}"
        },
        {
          "function": "conditional",
          "condition": "{{cache_enabled}}",
          "true_stack": [
            {
              "function": "get_cache",
              "key": "template:{{template_id}}:{{md5(variables)}}"
            }
          ]
        },
        {
          "function": "conditional",
          "condition": "{{!cache_value}}",
          "true_stack": [
            {
              "function": "template_engine",
              "template": "{{templates.content}}",
              "variables": "{{variables}}"
            },
            {
              "function": "conditional",
              "condition": "{{cache_enabled}}",
              "true_stack": [
                {
                  "function": "set_cache",
                  "key": "template:{{template_id}}:{{md5(variables)}}",
                  "value": "{{template_engine_output}}",
                  "ttl": 3600
                }
              ]
            }
          ]
        },
        {
          "function": "format_output",
          "content": "{{template_engine_output || cache_value}}",
          "format": "{{output_format}}"
        }
      ]
    }
  }
}
```

## Common Template Mistakes to Avoid

### ❌ Poor Practices
- Not escaping user input properly (security risk)
- Using complex logic in templates instead of preprocessing data
- Missing fallback values for optional variables
- Not validating template syntax before deployment
- Hardcoding values that should be variables

### ✅ Best Practices
- Always escape user input with appropriate filters
- Preprocess complex data logic before templating
- Provide sensible default values for all variables
- Test templates with various data scenarios
- Use template inheritance for consistent layouts

## Pro Tips

### 💡 **Performance Optimization**
- Cache frequently used templates and their outputs
- Preprocess complex data transformations outside templates
- Use template inheritance to reduce duplication
- Optimize loop operations for large datasets

### 🔒 **Security Best Practices**
- Always escape output based on context (HTML, JS, CSS, URL)
- Validate and sanitize all input variables
- Use whitelist approaches for dynamic template selection
- Implement template access controls and permissions

### 📊 **Template Management**
- Version control template changes
- Document template variables and expected data structures
- Create template libraries for common patterns
- Implement template testing and validation workflows

### 🔄 **Integration Strategies**
- Design templates for multiple output formats
- Create consistent variable naming conventions
- Implement template composition patterns
- Use conditional logic for platform-specific content

## Troubleshooting Template Issues

### Common Problems
1. **Variable not found errors**: Check variable names and data structure
2. **Escaping issues**: Verify appropriate filter usage for context
3. **Performance problems**: Review loop efficiency and caching strategy
4. **Syntax errors**: Validate Twig syntax and bracket matching

The Template Engine in Xano provides powerful content generation capabilities through Twig templating, enabling sophisticated dynamic content creation with proper security and performance optimization for no-code applications.