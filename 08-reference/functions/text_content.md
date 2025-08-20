---
category: functions
has_code_examples: true
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
- Text Processing
- String Manipulation
- Content Management
- Templates
- n8n
- WeWeb
- Documentation
title: 'Text Content & String Processing'
---

# Text Content & String Processing

## 📋 **Quick Summary**
Master text content processing and string manipulation in Xano for building dynamic content, template systems, and intelligent text processing workflows. Essential for content management, automated communication, and data transformation in your n8n and WeWeb applications.

## 🎯 **Core Concepts**

### Understanding Text Processing in Xano
Text content processing involves manipulating, formatting, and transforming string data to create dynamic content, generate templates, and process user-generated text. This includes everything from simple string concatenation to complex content generation systems.

**Key Applications:**
- **Dynamic Email Templates**: Personalized communications with variable substitution
- **Content Generation**: Automated article creation and content management
- **Data Cleaning**: Text normalization and validation
- **Search & Analysis**: Content indexing and text analytics
- **User Interface**: Dynamic labels and messaging systems

### Text Data Types and Formats
- **Plain Text**: Simple string content without formatting
- **Rich Text**: Formatted content with HTML, Markdown, or custom markup
- **Template Strings**: Text with variable placeholders for dynamic content
- **Structured Text**: JSON, XML, CSV, and other structured formats
- **Multilingual Content**: Text content supporting multiple languages

## 🔤 **Basic String Operations**

### String Manipulation Functions
```javascript
// Core string manipulation operations
{
  "string_operations": {
    "concatenation": {
      "function": "Text Concatenation",
      "example": {
        "inputs": ["Hello", " ", "World"],
        "operation": "concat",
        "result": "Hello World",
        "use_case": "Building dynamic messages"
      }
    },
    
    "case_conversion": {
      "uppercase": {
        "input": "hello world",
        "operation": "upper",
        "result": "HELLO WORLD",
        "use_case": "Standardizing text format"
      },
      "lowercase": {
        "input": "HELLO WORLD",
        "operation": "lower",
        "result": "hello world",
        "use_case": "Email address normalization"
      },
      "title_case": {
        "input": "hello world",
        "operation": "title",
        "result": "Hello World", 
        "use_case": "Display names and titles"
      }
    },
    
    "trimming": {
      "function": "Remove whitespace",
      "input": "  hello world  ",
      "operation": "trim",
      "result": "hello world",
      "use_case": "Cleaning user input"
    }
  }
}
```

### Advanced String Processing
```javascript
// Complex string manipulation for real-world scenarios
{
  "advanced_processing": {
    "substring_extraction": {
      "function": "Extract portions of text",
      "example": {
        "input": "user@domain.com",
        "operation": "Extract domain",
        "method": "Split by '@' and take second part",
        "result": "domain.com",
        "implementation": {
          "function_stack": [
            {
              "function": "Create Variable",
              "name": "email_parts",
              "value": "{{split(input_email, '@')}}"
            },
            {
              "function": "Create Variable", 
              "name": "domain",
              "value": "{{email_parts[1]}}"
            }
          ]
        }
      }
    },
    
    "pattern_replacement": {
      "function": "Replace text patterns",
      "examples": [
        {
          "input": "Phone: (555) 123-4567",
          "pattern": "Remove formatting",
          "result": "5551234567",
          "operation": "Replace non-numeric characters"
        },
        {
          "input": "John_Doe@company.com",
          "pattern": "Format name",
          "result": "John Doe",
          "operation": "Replace underscores with spaces"
        }
      ]
    }
  }
}
```

## 📝 **Template Systems**

### Dynamic Email Templates
```javascript
// Email template system with variable substitution
{
  "email_template_system": {
    "welcome_email": {
      "template": "Hello {{user.name}}, welcome to {{company.name}}! Your account has been created successfully. You can login with your email address {{user.email}}. If you have any questions, please contact our support team at {{company.support_email}}.",
      
      "variables": {
        "user": {
          "name": "John Smith",
          "email": "john@example.com"
        },
        "company": {
          "name": "Acme Corp",
          "support_email": "support@acmecorp.com"
        }
      },
      
      "processed_result": "Hello John Smith, welcome to Acme Corp! Your account has been created successfully. You can login with your email address john@example.com. If you have any questions, please contact our support team at support@acmecorp.com.",
      
      "xano_implementation": {
        "function_stack": [
          {
            "function": "Get Record",
            "table": "users",
            "record_id": "{{input.user_id}}"
          },
          {
            "function": "Get Record",
            "table": "company_settings",
            "record_id": 1
          },
          {
            "function": "Create Variable",
            "name": "email_template",
            "value": "Hello {{users.name}}, welcome to {{company_settings.company_name}}! Your account has been created successfully."
          },
          {
            "function": "Create Variable",
            "name": "processed_email",
            "value": "{{replace(replace(email_template, '{{users.name}}', users.name), '{{company_settings.company_name}}', company_settings.company_name)}}"
          }
        ]
      }
    }
  }
}
```

### Content Generation System
```javascript
// Automated content generation with templates
{
  "content_generation": {
    "product_description": {
      "template_structure": {
        "intro": "Introducing the {{product.name}} - {{product.tagline}}",
        "features": "Key features include: {{join(product.features, ', ')}}",
        "benefits": "This product helps you {{product.primary_benefit}}",
        "cta": "Order now for just ${{product.price}} and get {{product.warranty}} warranty!"
      },
      
      "product_data": {
        "name": "Smart Fitness Tracker",
        "tagline": "Your personal health companion",
        "features": ["Heart rate monitoring", "Sleep tracking", "Waterproof design", "7-day battery"],
        "primary_benefit": "stay healthy and motivated",
        "price": 199.99,
        "warranty": "2-year"
      },
      
      "generation_function": {
        "function_stack": [
          {
            "function": "Get Record",
            "table": "products",
            "record_id": "{{input.product_id}}"
          },
          {
            "function": "Create Variable",
            "name": "description_parts",
            "value": [
              "Introducing the {{products.name}} - {{products.tagline}}.",
              "Key features include: {{join(products.features, ', ')}}.",
              "This product helps you {{products.primary_benefit}}.",
              "Order now for just ${{products.price}} and get {{products.warranty}} warranty!"
            ]
          },
          {
            "function": "Create Variable",
            "name": "final_description",
            "value": "{{join(description_parts, ' ')}}"
          },
          {
            "function": "Edit Record",
            "table": "products",
            "record_id": "{{input.product_id}}",
            "data": {
              "generated_description": "{{final_description}}",
              "description_updated_at": "{{now()}}"
            }
          }
        ]
      }
    }
  }
}
```

## 🔍 **Text Processing & Analysis**

### Content Validation and Cleaning
```javascript
// Text validation and cleaning workflows
{
  "text_validation": {
    "user_input_sanitization": {
      "function_name": "sanitize_user_content",
      "function_stack": [
        {
          "step": "Basic Cleaning",
          "function": "Create Variable",
          "name": "cleaned_text",
          "value": "{{trim(input.user_text)}}"
        },
        {
          "step": "Remove HTML Tags",
          "function": "Create Variable",
          "name": "plain_text",
          "value": "{{regex_replace(cleaned_text, '<[^>]*>', '')}}"
        },
        {
          "step": "Profanity Filter",
          "function": "Get Records",
          "table": "banned_words",
          "filter": {"is_active": true}
        },
        {
          "step": "Apply Filters",
          "function": "For Each",
          "array": "{{banned_words}}",
          "inner_functions": [
            {
              "function": "Update Variable",
              "variable": "plain_text",
              "value": "{{regex_replace(plain_text, item.word, '***')}}"
            }
          ]
        },
        {
          "step": "Length Validation",
          "function": "Conditional",
          "condition": "{{length(plain_text) > 1000}}",
          "true_functions": [
            {
              "function": "Create Variable",
              "name": "truncated_text",
              "value": "{{substring(plain_text, 0, 997)}}..."
            }
          ],
          "false_functions": [
            {
              "function": "Create Variable",
              "name": "truncated_text",
              "value": "{{plain_text}}"
            }
          ]
        }
      ]
    }
  }
}
```

### Search and Text Analysis
```javascript
// Text search and analysis capabilities
{
  "text_analysis": {
    "keyword_extraction": {
      "function": "Extract important keywords from text",
      "implementation": {
        "function_stack": [
          {
            "function": "Create Variable",
            "name": "text_words",
            "value": "{{split(lowercase(input.text), ' ')}}"
          },
          {
            "function": "Create Variable",
            "name": "filtered_words",
            "value": "{{filter_array(text_words, 'length > 3')}}"
          },
          {
            "function": "Create Variable",
            "name": "word_frequency",
            "value": "{{count_occurrences(filtered_words)}}"
          },
          {
            "function": "Create Variable",
            "name": "top_keywords",
            "value": "{{top_items(word_frequency, 10)}}"
          }
        ]
      }
    },
    
    "sentiment_analysis": {
      "function": "Analyze text sentiment",
      "positive_words": ["good", "great", "excellent", "amazing", "wonderful", "fantastic"],
      "negative_words": ["bad", "terrible", "awful", "horrible", "disappointing", "worst"],
      "implementation": {
        "function_stack": [
          {
            "function": "Create Variable",
            "name": "text_lower",
            "value": "{{lowercase(input.text)}}"
          },
          {
            "function": "Create Variable",
            "name": "positive_count",
            "value": 0
          },
          {
            "function": "Create Variable",
            "name": "negative_count", 
            "value": 0
          },
          {
            "function": "For Each",
            "array": "{{positive_words}}",
            "inner_functions": [
              {
                "function": "Conditional",
                "condition": "{{contains(text_lower, item)}}",
                "true_functions": [
                  {
                    "function": "Update Variable",
                    "variable": "positive_count",
                    "value": "{{positive_count + 1}}"
                  }
                ]
              }
            ]
          },
          {
            "function": "Create Variable",
            "name": "sentiment_score",
            "value": "{{positive_count - negative_count}}"
          },
          {
            "function": "Create Variable",
            "name": "sentiment",
            "value": "{{sentiment_score > 0 ? 'positive' : sentiment_score < 0 ? 'negative' : 'neutral'}}"
          }
        ]
      }
    }
  }
}
```

## 🔗 **n8n Integration Examples**

### Content Processing Workflows
```javascript
// n8n workflow for content processing
{
  "n8n_content_workflow": {
    "blog_content_processor": {
      "nodes": [
        {
          "node": "Webhook",
          "description": "Receive blog post content"
        },
        {
          "node": "Set Variables",
          "variables": {
            "raw_content": "{{$json.content}}",
            "author": "{{$json.author}}",
            "category": "{{$json.category}}"
          }
        },
        {
          "node": "HTTP Request",
          "method": "POST",
          "url": "{{xano_instance}}/api/content/process",
          "body": {
            "content": "{{$node.Set_Variables.json.raw_content}}",
            "processing_options": {
              "extract_keywords": true,
              "generate_summary": true,
              "check_readability": true
            }
          }
        },
        {
          "node": "Set Variables",
          "variables": {
            "processed_content": "{{$json.processed_text}}",
            "keywords": "{{$json.extracted_keywords}}",
            "summary": "{{$json.generated_summary}}"
          }
        },
        {
          "node": "HTTP Request",
          "method": "POST", 
          "url": "{{xano_instance}}/api/blog/create",
          "body": {
            "title": "{{$node.Webhook.json.title}}",
            "content": "{{$node.Set_Variables1.json.processed_content}}",
            "summary": "{{$node.Set_Variables1.json.summary}}",
            "keywords": "{{$node.Set_Variables1.json.keywords}}",
            "author": "{{$node.Set_Variables.json.author}}",
            "category": "{{$node.Set_Variables.json.category}}",
            "status": "draft"
          }
        }
      ]
    }
  }
}
```

### Multilingual Content Management
```javascript
// Multilingual content processing workflow
{
  "multilingual_content": {
    "translation_workflow": {
      "nodes": [
        {
          "node": "Webhook",
          "description": "Content to translate"
        },
        {
          "node": "HTTP Request",
          "url": "{{xano_instance}}/api/content/detect-language",
          "body": {
            "text": "{{$json.content}}"
          }
        },
        {
          "node": "IF",
          "condition": "{{$json.detected_language !== 'en'}}",
          "true_branch": [
            {
              "node": "HTTP Request",
              "url": "{{translation_service}}/translate",
              "body": {
                "text": "{{$node.Webhook.json.content}}",
                "source": "{{$node.HTTP_Request.json.detected_language}}",
                "target": "en"
              }
            }
          ]
        },
        {
          "node": "HTTP Request",
          "url": "{{xano_instance}}/api/content/store",
          "body": {
            "original_content": "{{$node.Webhook.json.content}}",
            "translated_content": "{{$node.HTTP_Request1.json.translated_text}}",
            "source_language": "{{$node.HTTP_Request.json.detected_language}}",
            "target_language": "en"
          }
        }
      ]
    }
  }
}
```

## 🌐 **WeWeb Integration**

### Dynamic Content Display
```javascript
// WeWeb component with dynamic text processing
{
  "weweb_content_display": {
    "article_component": {
      "data_sources": {
        "article_content": "{{xano_instance}}/api/articles/{{article_id}}",
        "user_preferences": "{{xano_instance}}/api/users/{{user_id}}/preferences"
      },
      
      "computed_properties": {
        "reading_time": `
// Calculate reading time based on word count
computed: {
  readingTime() {
    if (!this.article.content) return '0 min';
    
    const wordsPerMinute = 200;
    const wordCount = this.article.content.split(' ').length;
    const minutes = Math.ceil(wordCount / wordsPerMinute);
    
    return minutes + (minutes === 1 ? ' min' : ' mins');
  }
}`,
        
        "formatted_content": `
// Format content based on user preferences
computed: {
  formattedContent() {
    let content = this.article.content;
    
    // Apply user reading preferences
    if (this.userPreferences.large_text) {
      content = '<div class="large-text">' + content + '</div>';
    }
    
    if (this.userPreferences.highlight_keywords) {
      this.article.keywords.forEach(keyword => {
        const regex = new RegExp(keyword, 'gi');
        content = content.replace(regex, '<mark>' + keyword + '</mark>');
      });
    }
    
    return content;
  }
}`
      }
    }
  }
}
```

### Real-Time Text Editor
```javascript
// WeWeb text editor with live processing
{
  "text_editor_component": {
    "features": [
      "Real-time character count",
      "Automatic text formatting",
      "Spell check integration",
      "Content suggestions"
    ],
    
    "implementation": `
// WeWeb text editor with Xano processing
export default {
  data() {
    return {
      content: '',
      processing: false,
      suggestions: [],
      stats: {
        characters: 0,
        words: 0,
        paragraphs: 0
      }
    };
  },
  
  watch: {
    content: {
      handler(newContent) {
        this.updateStats(newContent);
        this.debounceProcessing(newContent);
      },
      immediate: true
    }
  },
  
  methods: {
    updateStats(content) {
      this.stats.characters = content.length;
      this.stats.words = content.split(/\\s+/).filter(word => word).length;
      this.stats.paragraphs = content.split(/\\n\\s*\\n/).length;
    },
    
    debounceProcessing: _.debounce(function(content) {
      this.processContent(content);
    }, 500),
    
    async processContent(content) {
      if (!content.trim()) return;
      
      this.processing = true;
      
      try {
        const response = await fetch(\`\${this.xanoInstance}/api/text/analyze\`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': \`Bearer \${this.userToken}\`
          },
          body: JSON.stringify({
            content: content,
            analysis_type: ['grammar', 'readability', 'suggestions']
          })
        });
        
        const result = await response.json();
        this.suggestions = result.suggestions;
        
      } catch (error) {
        console.error('Content processing error:', error);
      } finally {
        this.processing = false;
      }
    }
  }
};`
  }
}
```

## 🎯 **Best Practices**

### Text Processing Optimization
```javascript
// Best practices for efficient text processing
{
  "optimization_guidelines": {
    "performance": [
      "Cache frequently processed text content",
      "Use database indexes for text search operations", 
      "Implement pagination for large text datasets",
      "Optimize regex patterns for better performance"
    ],
    
    "memory_management": [
      "Process large texts in chunks",
      "Clean up temporary string variables",
      "Use streams for very large content processing",
      "Implement proper garbage collection for text operations"
    ],
    
    "scalability": [
      "Use background tasks for heavy text processing",
      "Implement caching layers for processed content",
      "Consider external services for complex analysis",
      "Queue text processing jobs for high volume"
    ]
  }
}
```

### Security and Validation
```javascript
// Security considerations for text processing
{
  "security_guidelines": {
    "input_sanitization": [
      "Always validate and sanitize user-generated text",
      "Remove or escape HTML tags from user input",
      "Implement length limits on text fields",
      "Filter out potentially harmful content"
    ],
    
    "content_security": [
      "Validate text encoding and character sets",
      "Prevent script injection in dynamic content",
      "Implement rate limiting for text processing APIs",
      "Log and monitor suspicious text patterns"
    ],
    
    "data_privacy": [
      "Hash or encrypt sensitive text content",
      "Implement proper access controls for text data",
      "Follow GDPR guidelines for text data processing",
      "Provide data deletion capabilities for text content"
    ]
  }
}
```

---

*Text content processing forms the backbone of modern applications, enabling dynamic communication, intelligent content management, and automated text analysis. Master these patterns to build sophisticated content systems that scale with your application needs.*