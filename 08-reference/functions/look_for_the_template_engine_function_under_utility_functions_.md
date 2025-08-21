---
title: "Template Engine & Dynamic Content Generation"
description: "Complete guide to using Xano's Template Engine for dynamic HTML/text generation, email templates, and content automation with practical examples."
category: functions
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-21'
tags:
  - template-engine
  - dynamic-content
  - email-templates
  - content-generation
  - utility-functions
---

# Template Engine & Dynamic Content Generation

## 📋 **Quick Summary**
Complete guide to Xano's Template Engine function for generating dynamic content, HTML templates, email templates, and automated content generation. Perfect for creating personalized emails, dynamic web content, and automated document generation in no-code workflows.

## What You'll Learn
- How to locate and use the Template Engine function
- Dynamic content generation with variables and expressions
- Email template creation and personalization
- HTML/text template patterns for automation
- Integration with n8n, WeWeb, Make.com for content workflows

## 🚀 Finding the Template Engine Function

### Location in Visual Builder
```bash
# Access path in function stack:
Add Function → Utility Functions → Template Engine

# Alternative path:
Functions Panel → Utility → Template Engine
```

### Quick Setup
```javascript
// Template Engine function structure
template_engine({
  template: "your_template_with_{{variables}}",
  data: {
    variable1: "value1",
    variable2: "value2"
  }
})
```

## 🎯 Try This: Basic Template Usage

### Simple Variable Replacement
```javascript
// Basic email template
welcome_email_template = template_engine({
  template: `
    Hello {{user_name}},
    
    Welcome to {{company_name}}!
    Your account has been created successfully.
    
    Best regards,
    {{support_team}}
  `,
  data: {
    user_name: request.data.name,
    company_name: "Your Company",
    support_team: "Support Team"
  }
})
```

### HTML Template Generation
```html
<!-- Dynamic HTML content -->
html_template = template_engine({
  template: `
    <div class="user-profile">
      <h1>Welcome, {{user.name}}!</h1>
      <p>Email: {{user.email}}</p>
      <p>Member since: {{user.created_at | date}}</p>
      
      {{#if user.is_premium}}
        <div class="premium-badge">Premium Member</div>
      {{/if}}
      
      <ul class="recent-orders">
        {{#each orders}}
          <li>Order #{{id}} - ${{total}}</li>
        {{/each}}
      </ul>
    </div>
  `,
  data: {
    user: user_data,
    orders: recent_orders
  }
})
```

## 🔗 Integration Examples

### n8n Email Campaign
```javascript
// Generate personalized email content for n8n
email_campaign = template_engine({
  template: `
    <h2>Hi {{customer.first_name}},</h2>
    
    <p>We noticed you left {{cart.item_count}} items in your cart:</p>
    
    {{#each cart.items}}
      <div style="border: 1px solid #ddd; padding: 10px; margin: 5px;">
        <strong>{{name}}</strong><br>
        Price: ${{price}}<br>
        Quantity: {{quantity}}
      </div>
    {{/each}}
    
    <p>Total: ${{cart.total}}</p>
    
    <a href="{{checkout_url}}" style="background: #007cba; color: white; padding: 10px 20px; text-decoration: none;">
      Complete Your Purchase
    </a>
  `,
  data: {
    customer: customer_record,
    cart: abandoned_cart_data,
    checkout_url: process.env.SITE_URL + "/checkout/" + cart.id
  }
})

// Send to n8n for email delivery
trigger_n8n_email = external_api_request({
  url: process.env.N8N_EMAIL_WEBHOOK,
  method: "POST",
  data: {
    to: customer_record.email,
    subject: "Complete your purchase, " + customer_record.first_name,
    html_content: email_campaign
  }
})
```

### WeWeb Dynamic Content
```javascript
// Generate dynamic page content for WeWeb
page_content = template_engine({
  template: `
    {
      "hero_title": "Welcome back, {{user.name}}!",
      "stats": {
        "total_orders": {{user.order_count}},
        "total_spent": "{{user.total_spent | currency}}",
        "membership_level": "{{user.tier}}"
      },
      "recommendations": [
        {{#each recommended_products}}
          {
            "id": {{id}},
            "name": "{{name}}",
            "price": {{price}},
            "image": "{{image_url}}",
            "discount": {{#if on_sale}}"{{discount_percentage}}% off"{{else}}null{{/if}}
          }{{#unless @last}},{{/unless}}
        {{/each}}
      ]
    }
  `,
  data: {
    user: user_profile,
    recommended_products: product_recommendations
  }
})
```

### Make.com Document Generation
```javascript
// Generate invoice/receipt for Make.com
invoice_template = template_engine({
  template: `
    <div class="invoice">
      <header>
        <h1>INVOICE</h1>
        <p>Invoice #{{invoice.number}}</p>
        <p>Date: {{invoice.date | date_format}}</p>
      </header>
      
      <div class="billing-info">
        <div class="bill-to">
          <strong>Bill To:</strong><br>
          {{customer.name}}<br>
          {{customer.address}}<br>
          {{customer.city}}, {{customer.state}} {{customer.zip}}
        </div>
        
        <div class="bill-from">
          <strong>From:</strong><br>
          {{company.name}}<br>
          {{company.address}}<br>
          {{company.phone}}
        </div>
      </div>
      
      <table class="line-items">
        <thead>
          <tr>
            <th>Item</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          {{#each line_items}}
            <tr>
              <td>{{description}}</td>
              <td>{{quantity}}</td>
              <td>${{unit_price}}</td>
              <td>${{total_price}}</td>
            </tr>
          {{/each}}
        </tbody>
        <tfoot>
          <tr>
            <td colspan="3"><strong>Total:</strong></td>
            <td><strong>${{invoice.total}}</strong></td>
          </tr>
        </tfoot>
      </table>
    </div>
  `,
  data: {
    invoice: invoice_data,
    customer: customer_info,
    company: company_details,
    line_items: order_items
  }
})
```

## ⚙️ Advanced Template Patterns

### Conditional Content
```javascript
// Advanced conditional logic
conditional_template = template_engine({
  template: `
    {{#if user.is_vip}}
      <div class="vip-section">
        <h3>VIP Exclusive Offers</h3>
        {{#each vip_offers}}
          <div class="offer">{{title}} - {{discount}}% off</div>
        {{/each}}
      </div>
    {{else if user.is_premium}}
      <div class="premium-section">
        <h3>Premium Member Benefits</h3>
        <ul>
          {{#each premium_benefits}}
            <li>{{this}}</li>
          {{/each}}
        </ul>
      </div>
    {{else}}
      <div class="upgrade-prompt">
        <h3>Upgrade to Premium</h3>
        <p>Get access to exclusive features and offers!</p>
      </div>
    {{/if}}
  `,
  data: {
    user: user_data,
    vip_offers: vip_promotions,
    premium_benefits: ["Free shipping", "Early access", "24/7 support"]
  }
})
```

### Dynamic Lists and Loops
```javascript
// Complex list rendering
dynamic_list = template_engine({
  template: `
    <div class="product-grid">
      {{#each categories}}
        <div class="category">
          <h3>{{name}} ({{products.length}} items)</h3>
          <div class="products">
            {{#each products}}
              <div class="product {{#if featured}}featured{{/if}}">
                <img src="{{image}}" alt="{{name}}">
                <h4>{{name}}</h4>
                <p class="price">
                  {{#if sale_price}}
                    <span class="original">${{price}}</span>
                    <span class="sale">${{sale_price}}</span>
                  {{else}}
                    ${{price}}
                  {{/if}}
                </p>
                {{#if in_stock}}
                  <button class="add-to-cart" data-id="{{id}}">Add to Cart</button>
                {{else}}
                  <button disabled>Out of Stock</button>
                {{/if}}
              </div>
            {{/each}}
          </div>
        </div>
      {{/each}}
    </div>
  `,
  data: {
    categories: product_categories_with_products
  }
})
```

### Filters and Formatters
```javascript
// Using built-in filters
formatted_content = template_engine({
  template: `
    <div class="report">
      <h2>Sales Report for {{date | date_format("MMMM YYYY")}}</h2>
      
      <div class="metrics">
        <div class="metric">
          <label>Total Revenue:</label>
          <span>{{revenue | currency}}</span>
        </div>
        
        <div class="metric">
          <label>Orders:</label>
          <span>{{order_count | number_format}}</span>
        </div>
        
        <div class="metric">
          <label>Average Order:</label>
          <span>{{average_order | currency}}</span>
        </div>
        
        <div class="metric">
          <label>Growth:</label>
          <span class="{{#if growth_positive}}positive{{else}}negative{{/if}}">
            {{growth_percentage | percentage}}
          </span>
        </div>
      </div>
      
      <div class="description">
        {{description | truncate(200)}}
      </div>
    </div>
  `,
  data: {
    date: report_date,
    revenue: total_revenue,
    order_count: total_orders,
    average_order: average_order_value,
    growth_percentage: monthly_growth,
    growth_positive: monthly_growth > 0,
    description: report_description
  }
})
```

## 💡 Pro Tips

- **Template Caching**: Store frequently used templates as environment variables
- **Data Validation**: Always validate template data before processing
- **Error Handling**: Provide fallback values for optional template variables
- **Performance**: Use templates for bulk content generation efficiently
- **Testing**: Test templates with sample data before production use

## 🆘 Common Mistakes to Avoid

- **Missing Variables**: Ensure all template variables have corresponding data
- **HTML Escaping**: Be careful with user-generated content in HTML templates
- **Large Templates**: Break complex templates into smaller, reusable components
- **Data Structure**: Match template structure with your data organization
- **Security**: Never include sensitive data directly in templates

## 📊 Template Use Cases

| Use Case | Template Type | Integration | Complexity |
|----------|---------------|-------------|------------|
| Welcome Emails | HTML/Text | Email Service | Beginner |
| Order Confirmations | HTML | n8n/Make.com | Intermediate |
| PDF Generation | HTML | Document Service | Advanced |
| SMS Messages | Text | SMS API | Beginner |
| Dynamic Web Pages | JSON/HTML | WeWeb/Frontend | Intermediate |

## 🔄 Complete Workflow Example

```javascript
// Complete email automation workflow
email_automation_workflow = function_stack([
  // 1. Get user data
  get_user_data,
  
  // 2. Generate personalized content
  create_variable({
    name: "email_content",
    value: template_engine({
      template: process.env.EMAIL_TEMPLATE_WELCOME,
      data: {
        user: response_data,
        company: {
          name: process.env.COMPANY_NAME,
          website: process.env.COMPANY_WEBSITE,
          support_email: process.env.SUPPORT_EMAIL
        },
        unsubscribe_link: process.env.SITE_URL + "/unsubscribe/" + response_data.id
      }
    })
  }),
  
  // 3. Send via external service
  external_api_request({
    url: process.env.EMAIL_SERVICE_URL,
    method: "POST",
    headers: {
      "Authorization": "Bearer " + process.env.EMAIL_API_KEY
    },
    data: {
      to: response_data.email,
      subject: "Welcome to " + process.env.COMPANY_NAME,
      html: email_content
    }
  }),
  
  // 4. Log the activity
  add_record({
    table: "email_log",
    data: {
      user_id: response_data.id,
      email_type: "welcome",
      sent_at: now(),
      status: "sent"
    }
  })
])
```

The Template Engine is a powerful tool for creating dynamic, personalized content at scale. Use it to enhance user experiences and automate content generation across your no-code workflows!