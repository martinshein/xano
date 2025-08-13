#!/usr/bin/env python3
"""
Xano Documentation Processing Pipeline
Cleans, organizes, and optimizes Xano documentation for knowledge base use
"""

import os
import re
import json
import yaml
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import hashlib

class XanoDocProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.metadata = {
            "total_files": 0,
            "categories": defaultdict(list),
            "tags": defaultdict(int),
            "difficulty_distribution": defaultdict(int),
            "code_examples_count": 0,
            "cross_references": [],
            "processing_date": datetime.now().isoformat()
        }
        self.file_mapping = {}
        
    def setup_output_structure(self):
        """Create organized directory structure"""
        directories = [
            "01-getting-started",
            "02-core-concepts/function-stack",
            "02-core-concepts/database",
            "02-core-concepts/api-endpoints",
            "02-core-concepts/authentication",
            "03-data-operations",
            "04-integrations/external-apis",
            "04-integrations/ai-services",
            "04-integrations/third-party",
            "05-advanced-features/expressions",
            "05-advanced-features/conditionals",
            "05-advanced-features/custom-functions",
            "06-best-practices",
            "07-troubleshooting",
            "08-reference/functions",
            "08-reference/filters",
            "08-reference/examples"
        ]
        
        for dir_path in directories:
            (self.output_dir / dir_path).mkdir(parents=True, exist_ok=True)
            
    def clean_content(self, content):
        """Remove HTML artifacts and clean markdown content"""
        
        # Remove CSS class definitions and divs
        content = re.sub(r'::: \{[^}]+\}', '', content)
        content = re.sub(r':::(\s|$)', '', content)
        
        # Remove inline CSS classes
        content = re.sub(r'\{[^}]*\.[^}]+\}', '', content)
        
        # Clean up links with classes
        content = re.sub(r'\]\([^)]+\)\{[^}]+\}', ']', content)
        
        # Remove style attributes
        content = re.sub(r'style="[^"]*"', '', content)
        content = re.sub(r'style=\'[^\']*\'', '', content)
        
        # Remove data attributes
        content = re.sub(r'data-[^=]+="[^"]*"', '', content)
        content = re.sub(r'testid="[^"]*"', '', content)
        
        # Remove aria attributes
        content = re.sub(r'aria-[^=]+="[^"]*"', '', content)
        
        # Clean up image tags with excessive attributes
        content = re.sub(r'srcset="[^"]*"', '', content)
        content = re.sub(r'sizes="[^"]*"', '', content)
        content = re.sub(r'width="[^"]*"', '', content)
        content = re.sub(r'height="[^"]*"', '', content)
        
        # Remove font-emoji spans
        content = re.sub(r'\[([^]]+)\]\{\.font-emoji[^}]*\}', r'\1', content)
        
        # Clean up empty lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Remove navigation elements
        navigation_patterns = [
            r'^.*Welcome to Xano!.*$',
            r'^.*Frequently Asked Questions.*$',
            r'^.*Security & Compliance.*$',
            r'^.*Feature Requests.*$',
            r'^.*Known Issues.*$',
            r'^.*Before You Begin.*$',
            r'^.*The Visual Builder.*$',
            r'^\[Ctrl\].*\[K\].*$',
            r'^.*Xano Documentation.*$'
        ]
        
        for pattern in navigation_patterns:
            content = re.sub(pattern, '', content, flags=re.MULTILINE)
            
        # Remove marketing CTAs
        cta_patterns = [
            r'.*Get Started.*Free.*',
            r'.*Sign Up.*',
            r'.*Contact.*Support.*',
            r'.*Ask.*Question.*'
        ]
        
        for pattern in cta_patterns:
            content = re.sub(pattern, '', content, flags=re.MULTILINE | re.IGNORECASE)
            
        return content.strip()
        
    def extract_title(self, content):
        """Extract the main title from content"""
        # Look for h1 heading
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
            
        # Look for first non-empty line
        for line in content.split('\n'):
            line = line.strip()
            if line and not line.startswith('-') and len(line) > 10:
                return line[:100]
                
        return "Untitled"
        
    def categorize_file(self, file_path, content):
        """Determine category based on file path and content"""
        path_str = str(file_path).lower()
        content_lower = content.lower()
        
        # Category mapping rules
        if 'getting-started' in path_str or 'before-you-begin' in path_str:
            return "01-getting-started"
        elif 'function-stack' in path_str:
            return "02-core-concepts/function-stack"
        elif 'database' in path_str or 'table' in path_str:
            return "02-core-concepts/database"
        elif 'api' in path_str or 'endpoint' in path_str:
            return "02-core-concepts/api-endpoints"
        elif 'auth' in path_str or 'security' in path_str:
            return "02-core-concepts/authentication"
        elif 'ai-' in path_str or 'ai_' in path_str or 'artificial' in content_lower:
            return "04-integrations/ai-services"
        elif 'external' in path_str or 'integration' in path_str:
            return "04-integrations/external-apis"
        elif 'expression' in path_str:
            return "05-advanced-features/expressions"
        elif 'conditional' in path_str or 'if' in path_str:
            return "05-advanced-features/conditionals"
        elif 'custom' in path_str or 'function' in path_str:
            return "05-advanced-features/custom-functions"
        elif 'troubleshoot' in path_str or 'error' in path_str:
            return "07-troubleshooting"
        elif 'filter' in path_str:
            return "08-reference/filters"
        elif 'example' in path_str:
            return "08-reference/examples"
        else:
            return "08-reference/functions"
            
    def extract_tags(self, content):
        """Extract relevant tags from content"""
        tags = set()
        
        # Common Xano concepts
        keywords = [
            'api', 'database', 'function', 'expression', 'filter',
            'authentication', 'webhook', 'trigger', 'middleware',
            'background-task', 'custom-function', 'query', 'crud',
            'rest', 'graphql', 'websocket', 'realtime', 'cache',
            'transaction', 'validation', 'transformation', 'integration'
        ]
        
        content_lower = content.lower()
        for keyword in keywords:
            if keyword in content_lower:
                tags.add(keyword)
                
        return list(tags)
        
    def determine_difficulty(self, content):
        """Determine difficulty level based on content complexity"""
        advanced_indicators = [
            'transaction', 'optimization', 'performance', 'scaling',
            'custom function', 'complex', 'advanced', 'enterprise'
        ]
        
        intermediate_indicators = [
            'filter', 'expression', 'webhook', 'api', 'integration',
            'authentication', 'validation', 'transformation'
        ]
        
        content_lower = content.lower()
        
        advanced_count = sum(1 for ind in advanced_indicators if ind in content_lower)
        intermediate_count = sum(1 for ind in intermediate_indicators if ind in content_lower)
        
        if advanced_count >= 2:
            return "advanced"
        elif intermediate_count >= 2:
            return "intermediate"
        else:
            return "beginner"
            
    def count_code_examples(self, content):
        """Count code blocks in content"""
        # Count markdown code blocks
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        inline_code = re.findall(r'`[^`]+`', content)
        
        return len(code_blocks) + (len(inline_code) // 3)  # Approximate
        
    def generate_frontmatter(self, file_path, content, title):
        """Generate YAML frontmatter for file"""
        category = self.categorize_file(file_path, content)
        tags = self.extract_tags(content)
        difficulty = self.determine_difficulty(content)
        
        frontmatter = {
            'title': title,
            'category': category.split('/')[-1],
            'subcategory': category if '/' in category else None,
            'tags': tags,
            'difficulty': difficulty,
            'last_updated': '2025-01-23',
            'related_docs': []  # Will be populated in cross-reference phase
        }
        
        # Update metadata
        self.metadata['categories'][category].append(title)
        self.metadata['difficulty_distribution'][difficulty] += 1
        for tag in tags:
            self.metadata['tags'][tag] += 1
            
        return frontmatter
        
    def process_file(self, input_path):
        """Process a single markdown file"""
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Skip non-docs files
            if 'gitbook' in str(input_path) or 'fontawesome' in str(input_path):
                return None
                
            # Clean content
            cleaned_content = self.clean_content(content)
            
            # Skip if too little content remains
            if len(cleaned_content) < 100:
                return None
                
            # Extract title
            title = self.extract_title(cleaned_content)
            
            # Generate frontmatter
            frontmatter = self.generate_frontmatter(input_path, cleaned_content, title)
            
            # Count code examples
            code_count = self.count_code_examples(cleaned_content)
            self.metadata['code_examples_count'] += code_count
            
            # Determine output path
            category = self.categorize_file(input_path, cleaned_content)
            filename = Path(input_path).stem + '.md'
            output_path = self.output_dir / category / filename
            
            # Store mapping for cross-references
            self.file_mapping[str(input_path)] = str(output_path)
            
            # Write processed file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write(yaml.dump(frontmatter, default_flow_style=False))
                f.write('---\n\n')
                f.write(cleaned_content)
                
            self.metadata['total_files'] += 1
            return output_path
            
        except Exception as e:
            print(f"Error processing {input_path}: {e}")
            return None
            
    def create_cross_references(self):
        """Add cross-references between related documents"""
        # This would analyze content similarity and add related_docs
        # For now, we'll skip this complex step
        pass
        
    def generate_index_files(self):
        """Generate index and reference files"""
        
        # Generate README.md
        readme_content = """# Xano Knowledge Base

## Overview
This is a comprehensive, organized knowledge base extracted from Xano documentation.
All content has been cleaned, categorized, and optimized for easy reference.

## Structure

### 01. Getting Started
Introduction to Xano, account setup, and basic concepts.

### 02. Core Concepts
- **Function Stack**: Core function operations and flow
- **Database**: Database design and management
- **API Endpoints**: REST API creation and management
- **Authentication**: User authentication and security

### 03. Data Operations
CRUD operations, queries, and data manipulation.

### 04. Integrations
- **External APIs**: Connecting to third-party services
- **AI Services**: AI integration and tools
- **Third Party**: Other integration options

### 05. Advanced Features
- **Expressions**: Expression syntax and usage
- **Conditionals**: Conditional logic and branching
- **Custom Functions**: Creating custom functions

### 06. Best Practices
Recommended patterns and practices for Xano development.

### 07. Troubleshooting
Common issues and their solutions.

### 08. Reference
- **Functions**: Complete function reference
- **Filters**: Filter operations reference
- **Examples**: Code examples and patterns

## Quick Start
1. Start with [Getting Started](01-getting-started/)
2. Learn [Core Concepts](02-core-concepts/)
3. Explore [Examples](08-reference/examples/)

## Statistics
- Total Files: {total_files}
- Code Examples: {code_examples}
- Last Updated: {date}
""".format(
            total_files=self.metadata['total_files'],
            code_examples=self.metadata['code_examples_count'],
            date=datetime.now().strftime('%Y-%m-%d')
        )
        
        with open(self.output_dir / 'README.md', 'w') as f:
            f.write(readme_content)
            
        # Save metadata
        with open(self.output_dir / 'metadata.json', 'w') as f:
            json.dump(self.metadata, f, indent=2, default=str)
            
    def process_all(self):
        """Process all markdown files"""
        self.setup_output_structure()
        
        # Find all markdown files
        md_files = list(self.input_dir.rglob('*.md'))
        print(f"Found {len(md_files)} markdown files")
        
        # Process each file
        for i, md_file in enumerate(md_files):
            if i % 10 == 0:
                print(f"Processing file {i+1}/{len(md_files)}")
            self.process_file(md_file)
            
        # Create cross-references
        self.create_cross_references()
        
        # Generate index files
        self.generate_index_files()
        
        print(f"\nProcessing complete!")
        print(f"Total files processed: {self.metadata['total_files']}")
        print(f"Total code examples: {self.metadata['code_examples_count']}")
        print(f"Categories: {len(self.metadata['categories'])}")
        

if __name__ == "__main__":
    processor = XanoDocProcessor(
        input_dir="/root/docu-download/output/markdown",
        output_dir="/root/xano-knowledge"
    )
    processor.process_all()