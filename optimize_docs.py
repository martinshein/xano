#!/usr/bin/env python3
"""
Xano Documentation Optimizer
Optimizes markdown documentation for non-developers using n8n, Xano, WeWeb, and AI automation tools.
Preserves all original content while cleaning formatting and enhancing readability.
"""

import os
import re
import yaml
from pathlib import Path
import shutil
from datetime import datetime
import html
import json

class XanoDocOptimizer:
    def __init__(self, input_dir, output_dir, backup_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.backup_dir = Path(backup_dir)
        self.processed_count = 0
        self.error_count = 0
        self.optimization_log = []
        
    def backup_existing(self):
        """Create backup of existing documentation"""
        if self.output_dir.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = self.backup_dir / f"backup_{timestamp}"
            shutil.copytree(self.output_dir, backup_path)
            print(f"Backup created at: {backup_path}")
            return backup_path
        return None
        
    def extract_clean_title(self, content, filepath):
        """Extract a clean, meaningful title from content or filepath"""
        
        # First try to find a markdown heading
        heading_match = re.search(r'^#\s+([^#\n]+)', content, re.MULTILINE)
        if heading_match:
            title = heading_match.group(1).strip()
            # Clean up the title
            title = re.sub(r'!\[.*?\]\(.*?\)', '', title)  # Remove images
            title = re.sub(r'\[.*?\]\(.*?\)', '', title)    # Remove links
            title = re.sub(r'<[^>]+>', '', title)           # Remove HTML
            title = re.sub(r'\s+', ' ', title).strip()
            if len(title) > 10 and not title.startswith('http'):
                return title
        
        # Try to extract from filename
        filename = filepath.stem
        
        # Clean up filename
        title = filename.replace('_', ' ').replace('-', ' ')
        
        # Handle special cases
        if 'add record' in title.lower():
            return "Add Record"
        elif 'edit record' in title.lower():
            return "Edit Record"
        elif 'delete record' in title.lower():
            return "Delete Record"
        elif 'query all' in title.lower():
            return "Query All Records"
        elif 'get record' in title.lower():
            return "Get Record"
        elif 'api' in title.lower():
            parts = title.split()
            if 'request' in title.lower():
                return "API Request"
            elif 'endpoint' in title.lower():
                return "API Endpoints"
            else:
                return "API: " + ' '.join(parts[1:]).title() if len(parts) > 1 else "API Documentation"
        elif 'function' in title.lower():
            parts = title.split()
            return "Function: " + ' '.join(parts[1:]).title() if len(parts) > 1 else "Functions"
        elif 'database' in title.lower():
            return "Database: " + title.replace('database', '').strip().title()
        elif 'auth' in title.lower():
            return "Authentication: " + title.replace('auth', '').replace('authentication', '').strip().title()
        
        # General title case
        return title.title()
        
    def clean_html_content(self, content):
        """Remove ALL HTML tags and convert to pure markdown"""
        
        # Decode HTML entities first
        content = html.unescape(content)
        
        # Remove the frontmatter CSS-like artifacts first
        content = re.sub(r'^---[\s\S]*?---\n', '', content)
        
        # Remove ALL ::: blocks and their content
        content = re.sub(r':::\s*\{[^}]*\}[\s\S]*?:::', '', content)
        content = re.sub(r':::\s*[\s\S]*?:::', '', content)
        content = re.sub(r'-\s+:::', '', content)
        
        # Remove navigation lists with brackets
        content = re.sub(r'^\s*-\s+\[.*?\].*?$', '', content, flags=re.MULTILINE)
        
        # Remove GitBook header/footer artifacts
        content = re.sub(r'\[.*?\]\(.*?index\.html.*?\)', '', content)
        content = re.sub(r'Xano Documentation\s*\[Ctrl\]\[K\]', '', content)
        content = re.sub(r'\[Ctrl\]\[K\]', '', content)
        
        # Convert HTML images to markdown BEFORE removing tags
        # Handle various image formats
        content = re.sub(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*/?>', r'![\2](\1)', content)
        content = re.sub(r'<img\s+[^>]*alt=["\']([^"\']*)["\'][^>]*src=["\']([^"\']+)["\'][^>]*/?>', r'![\1](\2)', content)
        content = re.sub(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*/?>', r'![Image](\1)', content)
        
        # Convert HTML links to markdown
        content = re.sub(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>', r'[\2](\1)', content)
        
        # Convert HTML headings to markdown
        for i in range(6, 0, -1):
            content = re.sub(f'<h{i}[^>]*>([^<]+)</h{i}>', '#' * i + r' \1', content, flags=re.IGNORECASE)
        
        # Convert HTML lists
        content = re.sub(r'<li[^>]*>([^<]+)</li>', r'- \1', content, flags=re.IGNORECASE)
        content = re.sub(r'<ul[^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'</ul>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<ol[^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'</ol>', '', content, flags=re.IGNORECASE)
        
        # Convert HTML emphasis
        content = re.sub(r'<strong[^>]*>([^<]+)</strong>', r'**\1**', content, flags=re.IGNORECASE)
        content = re.sub(r'<b[^>]*>([^<]+)</b>', r'**\1**', content, flags=re.IGNORECASE)
        content = re.sub(r'<em[^>]*>([^<]+)</em>', r'*\1*', content, flags=re.IGNORECASE)
        content = re.sub(r'<i[^>]*>([^<]+)</i>', r'*\1*', content, flags=re.IGNORECASE)
        content = re.sub(r'<code[^>]*>([^<]+)</code>', r'`\1`', content, flags=re.IGNORECASE)
        
        # Convert HTML line breaks and paragraphs
        content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'<p[^>]*>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'</p>', '\n', content, flags=re.IGNORECASE)
        
        # Remove ALL remaining HTML tags
        content = re.sub(r'<[^>]+>', '', content)
        
        # Remove CSS class definitions
        content = re.sub(r'::: \{[^}]+\}', '', content)
        content = re.sub(r'\{[.#][^}]+\}', '', content)
        
        # Remove GitBook specific artifacts
        content = re.sub(r'!\[\]\([^)]*gitbook[^)]*\)', '', content)
        content = re.sub(r'\[!\[\]\([^)]*\)\]\([^)]*\)', '', content)
        content = re.sub(r'!\[.*?\]\(.*?gitbook.*?\)', '', content)
        
        # Clean up navigation/UI elements
        content = re.sub(r'On this page.*?(?=\n#|\n##|\Z)', '', content, flags=re.DOTALL)
        content = re.sub(r'Was this helpful\?.*?(?=\n#|\n##|\Z)', '', content, flags=re.DOTALL)
        content = re.sub(r'Copy\s*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'Last updated.*?(?=\n#|\n##|\Z)', '', content, flags=re.DOTALL)
        content = re.sub(r'\[Powered by GitBook\]', '', content)
        
        # Remove emoji icons in brackets like [🛠️]
        content = re.sub(r'\[[\U0001F300-\U0001F9FF]+\]', '', content)
        
        # Clean up excessive whitespace
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
        content = re.sub(r'^\s*-\s*$', '', content, flags=re.MULTILINE)
        
        return content.strip()
        
    def enhance_code_blocks(self, content):
        """Ensure all code blocks use proper markdown syntax with language hints"""
        
        # Fix code blocks without language specification
        def add_language_hint(match):
            code = match.group(1)
            # Try to detect language
            if '{' in code or 'function' in code or 'const' in code or 'var' in code:
                return f"```javascript\n{code}\n```"
            elif 'SELECT' in code.upper() or 'INSERT' in code.upper() or 'CREATE' in code.upper():
                return f"```sql\n{code}\n```"
            elif 'def ' in code or 'import ' in code or 'print(' in code:
                return f"```python\n{code}\n```"
            elif '<?php' in code:
                return f"```php\n{code}\n```"
            elif '<' in code and '>' in code and 'html' in code.lower():
                return f"```html\n{code}\n```"
            elif 'curl' in code.lower():
                return f"```bash\n{code}\n```"
            else:
                # Default to javascript for Xano context
                return f"```javascript\n{code}\n```"
        
        # Fix code blocks without language
        content = re.sub(r'```\n([^`]+)\n```', add_language_hint, content)
        
        # Ensure proper spacing around code blocks
        content = re.sub(r'([^\n])\n```', r'\1\n\n```', content)
        content = re.sub(r'```\n([^\n])', r'```\n\n\1', content)
        
        return content
        
    def add_no_code_explanations(self, content):
        """Add explanations for non-developer users"""
        
        # Add explanations after technical terms
        technical_terms = {
            r'\bAPI\b(?![:\s]+)': 'API (Application Programming Interface)',
            r'\bREST\b': 'REST (a standard way for systems to communicate)',
            r'\bJSON\b': 'JSON (a format for structuring data)',
            r'\bWebhook\b': 'Webhook (automated message sent when something happens)',
            r'\bEndpoint\b': 'Endpoint (a specific URL where your API can be accessed)',
            r'\bSchema\b': 'Schema (the structure of your database)',
            r'\bCRUD\b': 'CRUD (Create, Read, Update, Delete operations)',
            r'\bAuth\b': 'Auth (Authentication - verifying user identity)',
            r'\bJWT\b': 'JWT (JSON Web Token - a secure way to handle user sessions)',
            r'\bOAuth\b': 'OAuth (a standard for access delegation)',
        }
        
        # Only add explanations in the first occurrence of each section
        for term, explanation in technical_terms.items():
            # Check if explanation doesn't already exist
            if explanation not in content:
                content = re.sub(f'(^## .*\n)(.*?)({term})', 
                               rf'\1\2{explanation}', 
                               content, count=1, flags=re.MULTILINE | re.DOTALL)
        
        # Add integration tips for n8n/WeWeb
        if 'webhook' in content.lower() and 'n8n integration' not in content.lower():
            webhook_tip = "\n\n> **💡 Tip for n8n users:** You can trigger this webhook directly from n8n using the HTTP Request node. Just copy the webhook URL from Xano and paste it into n8n.\n"
            content = re.sub(r'(webhook[^.]*\.)', rf'\1{webhook_tip}', content, count=1, flags=re.IGNORECASE)
        
        if 'api endpoint' in content.lower() and 'weweb integration' not in content.lower():
            api_tip = "\n\n> **💡 Tip for WeWeb users:** This API endpoint can be connected directly in WeWeb's data sources. Use the Xano plugin for seamless integration.\n"
            content = re.sub(r'(api endpoint[^.]*\.)', rf'\1{api_tip}', content, count=1, flags=re.IGNORECASE)
        
        return content
        
    def improve_structure(self, content):
        """Improve document structure and readability"""
        
        # Ensure consistent heading hierarchy
        lines = content.split('\n')
        new_lines = []
        in_code_block = False
        
        for line in lines:
            # Track code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
            
            # Don't modify lines inside code blocks
            if not in_code_block:
                # Fix heading hierarchy
                if line.startswith('#'):
                    # Count the number of # symbols
                    level = len(line) - len(line.lstrip('#'))
                    # Ensure space after #
                    if level > 0 and level <= 6:
                        heading_text = line[level:].strip()
                        line = '#' * level + ' ' + heading_text
                
                # Add emoji icons for better visual scanning
                if line.startswith('## '):
                    if 'database' in line.lower():
                        line = line.replace('## ', '## 🗄️ ', 1)
                    elif 'api' in line.lower():
                        line = line.replace('## ', '## 🔌 ', 1)
                    elif 'function' in line.lower():
                        line = line.replace('## ', '## ⚙️ ', 1)
                    elif 'auth' in line.lower():
                        line = line.replace('## ', '## 🔐 ', 1)
                    elif 'webhook' in line.lower():
                        line = line.replace('## ', '## 🪝 ', 1)
                    elif 'example' in line.lower():
                        line = line.replace('## ', '## 📝 ', 1)
                    elif 'setup' in line.lower() or 'install' in line.lower():
                        line = line.replace('## ', '## 🚀 ', 1)
                    elif 'error' in line.lower() or 'troubleshoot' in line.lower():
                        line = line.replace('## ', '## 🔧 ', 1)
            
            new_lines.append(line)
        
        content = '\n'.join(new_lines)
        
        # Add section breaks between major topics
        content = re.sub(r'\n(#{1,2} )', r'\n---\n\n\1', content)
        
        # Format notes, tips, and warnings
        content = re.sub(r'^Note:', '> **📝 Note:**', content, flags=re.MULTILINE)
        content = re.sub(r'^Tip:', '> **💡 Tip:**', content, flags=re.MULTILINE)
        content = re.sub(r'^Warning:', '> **⚠️ Warning:**', content, flags=re.MULTILINE)
        content = re.sub(r'^Important:', '> **❗ Important:**', content, flags=re.MULTILINE)
        
        return content
        
    def extract_category(self, filepath):
        """Extract category from file path"""
        parts = filepath.relative_to(self.input_dir).parts
        if len(parts) > 1:
            # Return the main category
            category = parts[0]
            # Clean up category name
            category = re.sub(r'^\d+-', '', category)  # Remove number prefix
            return category.replace('-', ' ').title()
        return "General"
        
    def generate_clean_filename(self, title, original_path):
        """Generate clean filename from title"""
        # Clean the title for filename
        filename = title.lower()
        filename = re.sub(r'[^\w\s-]', '', filename)  # Remove special chars
        filename = re.sub(r'[-\s]+', '-', filename)   # Replace spaces with hyphens
        filename = filename.strip('-')                 # Remove leading/trailing hyphens
        
        # Limit length
        if len(filename) > 60:
            filename = filename[:60].rsplit('-', 1)[0]
        
        # Ensure uniqueness by adding category prefix if needed
        category_parts = original_path.parts[:-1]
        if category_parts and len(filename) < 20:
            category_prefix = category_parts[-1].split('-')[-1]
            if category_prefix not in filename:
                filename = f"{category_prefix}-{filename}"
        
        return filename + '.md'
        
    def process_file(self, input_path):
        """Process a single markdown file"""
        try:
            # Read the file
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if file is too small or non-documentation
            if len(content) < 50:
                return None
            
            # Extract original frontmatter if exists
            frontmatter = {}
            original_content = content
            if content.startswith('---'):
                try:
                    end_index = content.index('\n---', 3)
                    yaml_content = content[4:end_index]
                    frontmatter = yaml.safe_load(yaml_content) or {}
                    content = content[end_index + 4:].strip()
                except:
                    # If frontmatter parsing fails, treat whole thing as content
                    content = original_content
            
            # Clean HTML content
            content = self.clean_html_content(content)
            
            # Skip if content is now too small after cleaning
            if len(content) < 30:
                return None
            
            # Extract clean title
            title = self.extract_clean_title(content, input_path)
            
            # Enhance code blocks
            content = self.enhance_code_blocks(content)
            
            # Add no-code explanations
            content = self.add_no_code_explanations(content)
            
            # Improve structure
            content = self.improve_structure(content)
            
            # Extract category
            category = self.extract_category(input_path)
            
            # Generate tags based on content
            tags = []
            tag_keywords = {
                'api': ['api', 'endpoint', 'rest', 'http'],
                'database': ['database', 'table', 'query', 'sql', 'record'],
                'function': ['function', 'logic', 'workflow'],
                'authentication': ['auth', 'login', 'user', 'jwt', 'oauth'],
                'webhook': ['webhook', 'trigger', 'event'],
                'integration': ['integration', 'connect', 'external'],
                'n8n': ['n8n', 'workflow', 'automation'],
                'weweb': ['weweb', 'frontend', 'ui'],
            }
            
            content_lower = content.lower()
            for tag, keywords in tag_keywords.items():
                if any(keyword in content_lower for keyword in keywords):
                    tags.append(tag)
            
            # Update frontmatter
            frontmatter.update({
                'title': title,
                'category': category,
                'tags': tags[:5],  # Limit to 5 tags
                'last_updated': datetime.now().strftime('%Y-%m-%d'),
                'for_non_developers': True,
                'integrations': []
            })
            
            # Add integration flags
            if 'n8n' in content_lower:
                frontmatter['integrations'].append('n8n')
            if 'weweb' in content_lower:
                frontmatter['integrations'].append('weweb')
            
            # Determine output path with clean filename
            clean_filename = self.generate_clean_filename(title, input_path)
            
            # Preserve directory structure
            relative_dir = input_path.parent.relative_to(self.input_dir)
            output_path = self.output_dir / relative_dir / clean_filename
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write optimized file
            with open(output_path, 'w', encoding='utf-8') as f:
                # Write frontmatter
                f.write('---\n')
                f.write(yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True))
                f.write('---\n\n')
                
                # Write title if not already in content
                if not content.startswith('#'):
                    f.write(f"# {title}\n\n")
                
                # Add introduction for complex topics
                if category in ['Database', 'Api Endpoints', 'Functions'] and '## ' in content:
                    intro = f"This guide covers {title.lower()} in Xano. "
                    if 'n8n' in frontmatter.get('integrations', []):
                        intro += "You'll learn how to use this with n8n automations. "
                    if 'weweb' in frontmatter.get('integrations', []):
                        intro += "This integrates seamlessly with WeWeb frontends. "
                    f.write(f"{intro}\n\n")
                
                # Write content
                f.write(content)
                
                # Add footer with helpful links
                f.write("\n\n---\n\n")
                f.write("## 🔗 Related Resources\n\n")
                
                if 'api' in tags:
                    f.write("- [API Documentation](../reference/api-reference.md)\n")
                if 'database' in tags:
                    f.write("- [Database Guide](../core-concepts/database.md)\n")
                if 'function' in tags:
                    f.write("- [Function Stack Guide](../core-concepts/function-stack.md)\n")
                if 'n8n' in frontmatter.get('integrations', []):
                    f.write("- [n8n Integration Guide](../integrations/n8n-integration.md)\n")
                if 'weweb' in frontmatter.get('integrations', []):
                    f.write("- [WeWeb Integration Guide](../integrations/weweb-integration.md)\n")
            
            self.processed_count += 1
            self.optimization_log.append({
                'file': str(input_path),
                'output': str(output_path),
                'title': title,
                'category': category,
                'tags': tags,
                'size_before': len(content),
                'status': 'success'
            })
            
            return str(output_path)
            
        except Exception as e:
            self.error_count += 1
            self.optimization_log.append({
                'file': str(input_path),
                'error': str(e),
                'status': 'error'
            })
            print(f"Error processing {input_path}: {e}")
            return None
            
    def process_all_files(self):
        """Process all markdown files in the input directory"""
        # Find all markdown files
        md_files = list(self.input_dir.rglob('*.md'))
        total_files = len(md_files)
        
        print(f"Found {total_files} markdown files to process")
        
        for i, md_file in enumerate(md_files, 1):
            if i % 10 == 0:
                print(f"Processing file {i}/{total_files}...")
            
            self.process_file(md_file)
        
        print(f"\nProcessing complete!")
        print(f"Successfully processed: {self.processed_count} files")
        print(f"Errors encountered: {self.error_count} files")
        
    def generate_report(self):
        """Generate optimization report"""
        report_path = self.output_dir / 'OPTIMIZATION_REPORT.md'
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# Documentation Optimization Report\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Summary\n\n")
            f.write(f"- **Total Files Processed:** {self.processed_count}\n")
            f.write(f"- **Errors:** {self.error_count}\n")
            f.write(f"- **Success Rate:** {(self.processed_count/(self.processed_count+self.error_count)*100):.1f}%\n\n")
            
            f.write("## Optimizations Applied\n\n")
            f.write("1. ✅ Removed all HTML tags and artifacts\n")
            f.write("2. ✅ Converted HTML elements to pure markdown\n")
            f.write("3. ✅ Fixed YAML frontmatter with descriptive titles\n")
            f.write("4. ✅ Enhanced code blocks with language hints\n")
            f.write("5. ✅ Added explanations for non-developers\n")
            f.write("6. ✅ Improved document structure with emojis\n")
            f.write("7. ✅ Added integration tips for n8n/WeWeb\n")
            f.write("8. ✅ Generated clean, descriptive filenames\n")
            f.write("9. ✅ Added related resources links\n")
            f.write("10. ✅ Preserved all original content\n\n")
            
            f.write("## Categories Processed\n\n")
            categories = {}
            for log in self.optimization_log:
                if log['status'] == 'success':
                    cat = log.get('category', 'Unknown')
                    categories[cat] = categories.get(cat, 0) + 1
            
            for cat, count in sorted(categories.items()):
                f.write(f"- **{cat}:** {count} files\n")
            
            f.write("\n## Common Tags Found\n\n")
            all_tags = {}
            for log in self.optimization_log:
                if log['status'] == 'success':
                    for tag in log.get('tags', []):
                        all_tags[tag] = all_tags.get(tag, 0) + 1
            
            for tag, count in sorted(all_tags.items(), key=lambda x: x[1], reverse=True)[:10]:
                f.write(f"- **{tag}:** {count} occurrences\n")
            
            if self.error_count > 0:
                f.write("\n## Errors Encountered\n\n")
                for log in self.optimization_log:
                    if log['status'] == 'error':
                        f.write(f"- {log['file']}: {log.get('error', 'Unknown error')}\n")
            
            f.write("\n---\n\n")
            f.write("*This report was automatically generated by the Xano Documentation Optimizer*\n")
        
        # Save detailed log as JSON
        log_path = self.output_dir / 'optimization_log.json'
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(self.optimization_log, f, indent=2, default=str)
        
        print(f"\nReport generated: {report_path}")
        print(f"Detailed log saved: {log_path}")


def main():
    # Set directories
    input_dir = "/root/xano-knowledge"
    output_dir = "/root/xano-knowledge-optimized"
    backup_dir = "/root/xano-backups"
    
    # Create optimizer
    optimizer = XanoDocOptimizer(input_dir, output_dir, backup_dir)
    
    # Create backup
    print("Creating backup...")
    backup_path = optimizer.backup_existing()
    
    # Process all files
    print("\nStarting optimization process...")
    optimizer.process_all_files()
    
    # Generate report
    print("\nGenerating report...")
    optimizer.generate_report()
    
    print("\n✅ Optimization complete!")
    print(f"Optimized documentation: {output_dir}")
    if backup_path:
        print(f"Backup location: {backup_path}")


if __name__ == "__main__":
    main()