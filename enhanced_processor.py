#!/usr/bin/env python3
"""
Enhanced Xano Documentation Processor
Performs deeper cleaning and better organization
"""

import os
import re
import json
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class EnhancedXanoProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.glossary = {}
        self.examples = []
        self.faq_items = []
        
    def deep_clean_content(self, content):
        """Perform aggressive cleaning of HTML/CSS artifacts"""
        
        # Remove all image tags with complex URLs
        content = re.sub(r'!\[[^\]]*\]\([^)]*gitbook[^)]*\)', '', content)
        content = re.sub(r'\[[^\]]*\]\([^)]*gitbook[^)]*\)', '', content)
        
        # Remove all remaining CSS-like content
        content = re.sub(r'\{[^{}]*\}', '', content, flags=re.MULTILINE)
        
        # Remove all div-like structures
        content = re.sub(r'^:::.*$', '', content, flags=re.MULTILINE)
        
        # Remove navigation lists
        content = re.sub(r'^-\s+\[.*\].*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'^\s*-\s+[A-Z][^:]+$', '', content, flags=re.MULTILINE)
        
        # Remove style and class attributes
        content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
        
        # Clean up excessive whitespace
        content = re.sub(r'\n{4,}', '\n\n', content)
        content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
        
        # Extract actual content after massive header cleanup
        lines = content.split('\n')
        clean_lines = []
        skip_until_content = True
        
        for line in lines:
            # Skip until we find real content
            if skip_until_content:
                if (len(line) > 20 and 
                    not line.startswith('-') and 
                    not 'gitbook' in line.lower() and
                    not 'navigation' in line.lower() and
                    not '...' in line):
                    skip_until_content = False
                else:
                    continue
                    
            # Keep content lines
            if line.strip():
                clean_lines.append(line)
                
        return '\n'.join(clean_lines).strip()
        
    def extract_real_title(self, file_path, content):
        """Extract meaningful title from file path or content"""
        
        # Try to get from file path
        path_parts = str(file_path).split('/')
        filename = Path(file_path).stem
        
        # Clean up filename
        title = filename.replace('-', ' ').replace('_', ' ').title()
        
        # Special cases
        if 'add-record' in filename:
            return "Add Record"
        elif 'edit-record' in filename:
            return "Edit Record"
        elif 'delete-record' in filename:
            return "Delete Record"
        elif 'query-all' in filename:
            return "Query All Records"
        elif 'get-record' in filename:
            return "Get Record"
        elif 'api' in filename.lower():
            return f"API: {title}"
        elif 'function' in filename.lower():
            return f"Function: {title}"
            
        # Look for markdown heading
        heading_match = re.search(r'^#+\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            return heading_match.group(1).strip()
            
        return title
        
    def categorize_by_content(self, file_path, content):
        """Smart categorization based on file path and content analysis"""
        
        path_str = str(file_path).lower()
        
        # Map based on path structure
        if 'before-you-begin' in path_str or 'getting-started' in path_str:
            return "01-getting-started"
        elif 'database-requests' in path_str:
            return "03-data-operations"
        elif 'ai-tools' in path_str or '/ai/' in path_str:
            return "04-integrations/ai-services"
        elif 'function-stack/functions' in path_str:
            if 'database' in path_str:
                return "03-data-operations"
            elif 'api' in path_str:
                return "02-core-concepts/api-endpoints"
            else:
                return "02-core-concepts/function-stack"
        elif 'the-database' in path_str:
            return "02-core-concepts/database"
        elif 'building-with-visual' in path_str:
            return "05-advanced-features/custom-functions"
        elif 'troubleshoot' in path_str:
            return "07-troubleshooting"
        elif 'xano-features' in path_str:
            return "05-advanced-features/expressions"
        elif 'testing' in path_str:
            return "06-best-practices"
        else:
            # Default based on keywords
            if 'example' in path_str:
                return "08-reference/examples"
            elif 'filter' in path_str:
                return "08-reference/filters"
            else:
                return "08-reference/functions"
                
    def extract_code_blocks(self, content):
        """Extract and format code blocks properly"""
        
        # Find all code blocks
        code_blocks = re.findall(r'```([^`]*)```', content, re.DOTALL)
        
        formatted_blocks = []
        for block in code_blocks:
            # Try to determine language
            lines = block.strip().split('\n')
            if lines:
                first_line = lines[0].strip()
                if first_line in ['javascript', 'js', 'json', 'sql', 'python']:
                    # Has language specifier
                    formatted_blocks.append(f"```{first_line}\n" + '\n'.join(lines[1:]) + "\n```")
                else:
                    # No language, try to guess
                    if '{' in block or 'function' in block:
                        formatted_blocks.append(f"```javascript\n{block}\n```")
                    elif 'SELECT' in block.upper() or 'INSERT' in block.upper():
                        formatted_blocks.append(f"```sql\n{block}\n```")
                    else:
                        formatted_blocks.append(f"```\n{block}\n```")
                        
        return formatted_blocks
        
    def create_glossary_entry(self, term, definition):
        """Add term to glossary"""
        self.glossary[term] = definition
        
    def process_enhanced_file(self, input_path):
        """Process file with enhanced cleaning"""
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                raw_content = f.read()
                
            # Skip non-documentation files
            if any(skip in str(input_path) for skip in ['gitbook', 'fontawesome', 'static', 'cache']):
                return None
                
            # Deep clean
            content = self.deep_clean_content(raw_content)
            
            # Skip if too little content
            if len(content) < 50:
                return None
                
            # Extract title
            title = self.extract_real_title(input_path, content)
            
            # Categorize
            category = self.categorize_by_content(input_path, content)
            
            # Extract code examples
            code_blocks = self.extract_code_blocks(content)
            if code_blocks:
                self.examples.extend([(title, block) for block in code_blocks])
                
            # Generate clean frontmatter
            frontmatter = {
                'title': title,
                'category': category.split('/')[-1],
                'tags': self.extract_simple_tags(content),
                'has_code_examples': len(code_blocks) > 0,
                'last_updated': '2025-01-23'
            }
            
            # Determine output file
            safe_filename = re.sub(r'[^\w\-]', '_', title.lower()) + '.md'
            output_path = self.output_dir / category / safe_filename
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write clean file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write(yaml.dump(frontmatter, default_flow_style=False))
                f.write('---\n\n')
                f.write(f"# {title}\n\n")
                f.write(content)
                
                # Add code examples section if any
                if code_blocks:
                    f.write("\n\n## Code Examples\n\n")
                    for block in code_blocks:
                        f.write(block + "\n\n")
                        
            return str(output_path)
            
        except Exception as e:
            print(f"Error processing {input_path}: {e}")
            return None
            
    def extract_simple_tags(self, content):
        """Extract simple relevant tags"""
        tags = []
        keywords = {
            'api': 'API',
            'database': 'Database',
            'function': 'Functions',
            'query': 'Queries',
            'crud': 'CRUD',
            'auth': 'Authentication',
            'webhook': 'Webhooks',
            'expression': 'Expressions',
            'filter': 'Filters',
            'transaction': 'Transactions'
        }
        
        content_lower = content.lower()
        for key, tag in keywords.items():
            if key in content_lower:
                tags.append(tag)
                
        return tags[:5]  # Limit to 5 tags
        
    def generate_reference_files(self):
        """Generate comprehensive reference files"""
        
        # Quick Reference
        quick_ref = """# Xano Quick Reference

## Common Patterns

### Database Operations

#### Add Record
```javascript
// Add a new record to a table
xano.database.add_record({
  table: 'users',
  data: {
    name: 'John Doe',
    email: 'john@example.com'
  }
})
```

#### Query Records
```javascript
// Query with filters
xano.database.query_all_records({
  table: 'users',
  filters: [
    {field: 'status', operator: '=', value: 'active'}
  ],
  sort: {field: 'created_at', order: 'desc'},
  limit: 10
})
```

#### Update Record
```javascript
// Update existing record
xano.database.edit_record({
  table: 'users',
  id: 123,
  data: {
    status: 'inactive'
  }
})
```

### API Endpoints

#### Create REST Endpoint
```javascript
// Define GET endpoint
xano.api.create({
  method: 'GET',
  path: '/users/{id}',
  function_stack: [
    'validate_input',
    'get_user',
    'format_response'
  ]
})
```

### Functions

#### Custom Function
```javascript
// Define custom function
xano.function.create({
  name: 'calculate_total',
  inputs: ['items', 'tax_rate'],
  logic: function(items, tax_rate) {
    let subtotal = items.reduce((sum, item) => sum + item.price, 0);
    return subtotal * (1 + tax_rate);
  }
})
```

## Expression Syntax

- Variables: `{variable_name}`
- Conditionals: `{if condition then value1 else value2}`
- Math: `{value1 + value2}`, `{value1 * value2}`
- String: `{concat(str1, str2)}`, `{upper(text)}`
- Date: `{now()}`, `{date_add(date, 1, 'days')}`

## Filter Operators

- `=` : Equals
- `!=` : Not equals
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal
- `<=` : Less than or equal
- `contains` : String contains
- `starts_with` : String starts with
- `ends_with` : String ends with
- `in` : Value in array
- `not_in` : Value not in array
- `is_null` : Is null
- `is_not_null` : Is not null

## Authentication

### Basic Auth Setup
```javascript
xano.auth.setup({
  table: 'users',
  username_field: 'email',
  password_field: 'password',
  hash_method: 'bcrypt',
  token_expiry: 3600
})
```

## Webhooks

### Incoming Webhook
```javascript
xano.webhook.create({
  name: 'payment_received',
  method: 'POST',
  authentication: 'bearer_token',
  function_stack: ['validate_webhook', 'process_payment']
})
```

## Background Tasks

### Schedule Task
```javascript
xano.task.schedule({
  name: 'daily_cleanup',
  cron: '0 0 * * *',  // Daily at midnight
  function: 'cleanup_old_records'
})
```
"""
        
        with open(self.output_dir / 'QUICK_REFERENCE.md', 'w') as f:
            f.write(quick_ref)
            
        # Glossary
        glossary_content = """# Xano Glossary

## A

**API Endpoint**: A specific URL path that accepts requests and returns responses.

**Authentication**: Process of verifying user identity.

**Addon**: Additional functionality that can be added to your Xano workspace.

## B

**Background Task**: Functions that run asynchronously in the background.

**Branch**: A separate version of your API for development/testing.

## C

**CRUD**: Create, Read, Update, Delete - basic database operations.

**Custom Function**: User-defined reusable logic blocks.

## D

**Database Table**: Structured storage for your data records.

**Data Type**: The type of data a field can hold (text, integer, boolean, etc.).

## E

**Expression**: Dynamic values calculated at runtime using Xano's expression syntax.

**External API**: Third-party API that Xano can connect to.

## F

**Filter**: Conditions used to narrow down query results.

**Function Stack**: The sequence of operations executed in an API endpoint.

## G

**GraphQL**: Alternative API query language supported by Xano.

## H

**Hash**: One-way encryption used for passwords.

**Hook**: Code that runs at specific points in the execution flow.

## I

**Input**: Data received by a function or API endpoint.

**Instance**: A deployed version of your Xano backend.

## J

**JWT**: JSON Web Token used for authentication.

## L

**Lambda Function**: Serverless function execution.

**Loop**: Iteration over arrays or collections.

## M

**Middleware**: Functions that run before/after main logic.

**Migration**: Moving data between tables or systems.

## O

**Output**: Data returned from a function or API endpoint.

## P

**Pagination**: Breaking large result sets into pages.

**Precondition**: Validation that must pass before execution.

## Q

**Query**: Request for data from the database.

## R

**Redis**: In-memory cache system for performance.

**REST**: Representational State Transfer API architecture.

## S

**Schema**: Structure definition of database tables.

**SQL**: Structured Query Language for database operations.

## T

**Token**: Authentication credential.

**Transaction**: Group of operations that succeed or fail together.

**Trigger**: Event that causes a function to execute.

## V

**Validation**: Checking data meets requirements.

**Variable**: Named storage for values.

## W

**Webhook**: HTTP callback triggered by events.

**Workspace**: Your Xano project environment.
"""
        
        with open(self.output_dir / 'GLOSSARY.md', 'w') as f:
            f.write(glossary_content)
            
    def process_all_enhanced(self):
        """Run enhanced processing"""
        
        # Process all markdown files
        md_files = list(self.input_dir.rglob('*.md'))
        processed = 0
        
        for i, md_file in enumerate(md_files):
            if i % 20 == 0:
                print(f"Processing {i}/{len(md_files)}")
            result = self.process_enhanced_file(md_file)
            if result:
                processed += 1
                
        print(f"Processed {processed} files successfully")
        
        # Generate reference files
        self.generate_reference_files()
        
        # Create examples index
        if self.examples:
            with open(self.output_dir / 'EXAMPLES_INDEX.md', 'w') as f:
                f.write("# Code Examples Index\n\n")
                for title, example in self.examples[:50]:  # Limit to 50
                    f.write(f"## {title}\n\n{example}\n\n---\n\n")
                    
        print("Enhanced processing complete!")
        

if __name__ == "__main__":
    processor = EnhancedXanoProcessor(
        input_dir="/root/docu-download/output/markdown",
        output_dir="/root/xano-knowledge"
    )
    processor.process_all_enhanced()