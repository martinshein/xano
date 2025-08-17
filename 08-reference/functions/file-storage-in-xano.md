---
title: File Storage Functions Reference
description: Complete guide to implementing file storage in Xano - upload, manage, and serve files for no-code platforms with secure access controls
category: functions
subcategory: 08-reference/functions
tags:
- file-storage
- file-upload
- cloud-storage
- file-management
- security
- access-control
- image-processing
- n8n-integration
- weweb-integration
- make-automation
last_updated: '2025-01-17'
difficulty: intermediate
has_code_examples: true
related_docs:
- 02-core-concepts/function-stack/file-storage.md
- 08-reference/functions/private-file-storage.md
- 08-reference/functions/middleware.md
---

## 📋 **Quick Summary**

Xano provides comprehensive file storage capabilities for uploading, managing, and serving files with built-in security, access controls, and integration options. Files can be stored publicly or privately with advanced processing features.

## What You'll Learn

- How to implement file upload and management
- Public vs private file storage configurations
- File security and access control patterns
- Image processing and transformation features
- File storage integration with no-code platforms
- Best practices for file organization and performance
- Advanced file handling scenarios

## File Storage Overview

### Storage Types

**Public File Storage:**
- Directly accessible via URL
- Suitable for images, documents, media
- Cached and CDN-optimized
- No authentication required

**Private File Storage:**
- Access-controlled downloads
- Secure file serving with permissions
- Time-limited access tokens
- Audit trail capabilities

### File Field Types

```javascript
// Database field configurations
{
  "public_file_field": {
    "type": "file",
    "storage": "public",
    "allowed_extensions": ["jpg", "png", "gif", "pdf"],
    "max_size": "10MB"
  },
  "private_file_field": {
    "type": "file", 
    "storage": "private",
    "allowed_extensions": ["pdf", "doc", "docx"],
    "max_size": "50MB"
  },
  "multiple_files_field": {
    "type": "file",
    "multiple": true,
    "storage": "public",
    "max_files": 5
  }
}
```

## File Upload Implementation

### 1. Basic File Upload API

```javascript
// File upload endpoint
{
  "endpoint": "/api/upload",
  "method": "POST",
  "inputs": [
    {"name": "file", "type": "file"},
    {"name": "title", "type": "text"},
    {"name": "category", "type": "text"}
  ],
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{!file}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 400,
          "body": {"error": "No file provided"}
        }
      ]
    },
    {
      "function": "add_record",
      "table": "files",
      "data": {
        "file": "{{file}}",
        "title": "{{title}}",
        "category": "{{category}}",
        "uploaded_by": "{{auth.user.id}}",
        "uploaded_at": "{{now()}}"
      }
    }
  ]
}
```

### 2. File Validation and Processing

```javascript
// Advanced file upload with validation
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "file_info",
      "value": {
        "name": "{{file.name}}",
        "size": "{{file.size}}",
        "type": "{{file.type}}",
        "extension": "{{file_extension(file.name)}}"
      }
    },
    {
      "function": "conditional",
      "condition": "{{file_info.size > 10485760}}", // 10MB
      "true_stack": [
        {
          "function": "throw_error",
          "message": "File too large. Max size is 10MB",
          "code": "FILE_TOO_LARGE"
        }
      ]
    },
    {
      "function": "conditional",
      "condition": "{{!in_array(file_info.extension, ['jpg', 'png', 'gif', 'pdf'])}}",
      "true_stack": [
        {
          "function": "throw_error",
          "message": "Invalid file type",
          "code": "INVALID_FILE_TYPE"
        }
      ]
    },
    {
      "function": "add_record",
      "table": "uploads",
      "data": {
        "file": "{{file}}",
        "original_name": "{{file_info.name}}",
        "file_size": "{{file_info.size}}",
        "mime_type": "{{file_info.type}}",
        "uploaded_by": "{{auth.user.id}}"
      }
    }
  ]
}
```

### 3. Multiple File Upload

```javascript
// Handle multiple file uploads
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "uploaded_files",
      "value": []
    },
    {
      "function": "for_each_loop",
      "array": "{{files}}",
      "function_stack": [
        {
          "function": "conditional",
          "condition": "{{loop_item.size <= 5242880}}", // 5MB per file
          "true_stack": [
            {
              "function": "add_record",
              "table": "gallery_images",
              "data": {
                "image": "{{loop_item}}",
                "gallery_id": "{{gallery_id}}",
                "order": "{{loop_index}}",
                "uploaded_at": "{{now()}}"
              }
            },
            {
              "function": "update_variable",
              "variable": "uploaded_files",
              "value": "{{append(uploaded_files, gallery_images.id)}}"
            }
          ]
        }
      ]
    }
  ]
}
```

## Private File Storage and Security

### 1. Secure File Access

```javascript
// Private file download with permissions
{
  "endpoint": "/api/files/{file_id}/download",
  "method": "GET",
  "authentication": "required",
  "function_stack": [
    {
      "function": "get_record",
      "table": "private_files",
      "record_id": "{{file_id}}"
    },
    {
      "function": "conditional",
      "condition": "{{private_files.owner_id != auth.user.id && !has_file_permission(auth.user.id, file_id)}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 403,
          "body": {"error": "Access denied"}
        }
      ]
    },
    {
      "function": "add_record",
      "table": "file_access_log",
      "data": {
        "file_id": "{{file_id}}",
        "user_id": "{{auth.user.id}}",
        "accessed_at": "{{now()}}",
        "ip_address": "{{request.ip}}"
      }
    },
    {
      "function": "return_file",
      "file": "{{private_files.file}}",
      "filename": "{{private_files.original_name}}"
    }
  ]
}
```

### 2. Time-Limited Access Tokens

```javascript
// Generate temporary file access token
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "access_token",
      "value": "{{generate_uuid()}}"
    },
    {
      "function": "create_variable",
      "name": "expires_at",
      "value": "{{add_hours(now(), 24)}}"
    },
    {
      "function": "add_record",
      "table": "file_access_tokens",
      "data": {
        "token": "{{access_token}}",
        "file_id": "{{file_id}}",
        "user_id": "{{auth.user.id}}",
        "expires_at": "{{expires_at}}",
        "created_at": "{{now()}}"
      }
    },
    {
      "function": "return_response",
      "body": {
        "download_url": "{{env.APP_URL}}/api/files/download/{{access_token}}",
        "expires_at": "{{expires_at}}"
      }
    }
  ]
}

// Token-based download
{
  "endpoint": "/api/files/download/{token}",
  "function_stack": [
    {
      "function": "get_record",
      "table": "file_access_tokens",
      "filter": {"token": "{{token}}"}
    },
    {
      "function": "conditional",
      "condition": "{{!file_access_tokens || file_access_tokens.expires_at < now()}}",
      "true_stack": [
        {
          "function": "return_response",
          "status": 404,
          "body": {"error": "Invalid or expired token"}
        }
      ]
    },
    {
      "function": "get_record",
      "table": "private_files",
      "record_id": "{{file_access_tokens.file_id}}"
    },
    {
      "function": "return_file",
      "file": "{{private_files.file}}"
    }
  ]
}
```

## Image Processing Features

### 1. Image Transformations

```javascript
// Image resize and optimization
{
  "function_stack": [
    {
      "function": "conditional",
      "condition": "{{is_image(file.type)}}",
      "true_stack": [
        {
          "function": "create_variable",
          "name": "processed_image",
          "value": "{{resize_image(file, {width: 800, height: 600, quality: 80})}}"
        },
        {
          "function": "create_variable",
          "name": "thumbnail",
          "value": "{{resize_image(file, {width: 200, height: 200, crop: 'center'})}}"
        },
        {
          "function": "add_record",
          "table": "images",
          "data": {
            "original": "{{file}}",
            "processed": "{{processed_image}}",
            "thumbnail": "{{thumbnail}}",
            "alt_text": "{{alt_text}}",
            "uploaded_by": "{{auth.user.id}}"
          }
        }
      ]
    }
  ]
}
```

### 2. Dynamic Image Serving

```javascript
// Dynamic image transformation API
{
  "endpoint": "/api/images/{image_id}",
  "method": "GET",
  "inputs": [
    {"name": "width", "type": "integer", "required": false},
    {"name": "height", "type": "integer", "required": false},
    {"name": "quality", "type": "integer", "required": false},
    {"name": "format", "type": "text", "required": false}
  ],
  "function_stack": [
    {
      "function": "get_record",
      "table": "images",
      "record_id": "{{image_id}}"
    },
    {
      "function": "create_variable",
      "name": "transform_params",
      "value": {
        "width": "{{width || 'auto'}}",
        "height": "{{height || 'auto'}}",
        "quality": "{{quality || 80}}",
        "format": "{{format || 'jpg'}}"
      }
    },
    {
      "function": "return_file",
      "file": "{{images.original}}",
      "transform": "{{transform_params}}"
    }
  ]
}
```

## No-Code Platform Integration

### n8n File Processing
```javascript
// Send file data to n8n for processing
{
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "https://hooks.n8n.cloud/webhook/file-processor",
      "method": "POST",
      "data": {
        "file_url": "{{file.url}}",
        "file_id": "{{file.id}}",
        "file_type": "{{file.mime_type}}",
        "uploaded_by": "{{auth.user.id}}",
        "processing_type": "extract_text"
      }
    }
  ]
}
```

### WeWeb File Components
```javascript
// File upload for WeWeb components
{
  "endpoint": "/api/weweb/upload",
  "function_stack": [
    {
      "function": "add_record",
      "table": "user_uploads",
      "data": {
        "file": "{{file}}",
        "user_id": "{{auth.user.id}}",
        "component_id": "{{component_id}}",
        "uploaded_at": "{{now()}}"
      }
    },
    {
      "function": "return_response",
      "body": {
        "file_id": "{{user_uploads.id}}",
        "file_url": "{{user_uploads.file.url}}",
        "thumbnail_url": "{{user_uploads.file.thumbnail_url}}"
      }
    }
  ]
}
```

### Make.com File Automation
```javascript
// Trigger Make.com scenario on file upload
{
  "function_stack": [
    {
      "function": "external_api_request",
      "url": "https://hook.us1.make.com/file-uploaded",
      "data": {
        "file_id": "{{new_record.id}}",
        "file_url": "{{new_record.file.url}}",
        "file_name": "{{new_record.original_name}}",
        "uploaded_by": "{{new_record.uploaded_by}}",
        "category": "{{new_record.category}}"
      }
    }
  ]
}
```

## Advanced File Management

### 1. File Organization System

```javascript
// Hierarchical file organization
{
  "function_stack": [
    {
      "function": "create_variable",
      "name": "file_path",
      "value": "{{auth.user.id}}/{{category}}/{{format_date(now(), 'Y/m')}}"
    },
    {
      "function": "add_record",
      "table": "organized_files",
      "data": {
        "file": "{{file}}",
        "path": "{{file_path}}",
        "category": "{{category}}",
        "tags": "{{tags}}",
        "metadata": {
          "size": "{{file.size}}",
          "type": "{{file.type}}",
          "uploaded_at": "{{now()}}"
        }
      }
    }
  ]
}
```

### 2. File Cleanup and Archival

```javascript
// Automated file cleanup
{
  "scheduled_function": "cleanup_old_files",
  "schedule": "0 2 * * *", // Daily at 2 AM
  "function_stack": [
    {
      "function": "query_all_records",
      "table": "temporary_files",
      "filter": {
        "created_at": {"$lt": "{{subtract_days(now(), 7)}}"}
      }
    },
    {
      "function": "for_each_loop",
      "array": "{{temporary_files}}",
      "function_stack": [
        {
          "function": "delete_file",
          "file": "{{loop_item.file}}"
        },
        {
          "function": "delete_record",
          "table": "temporary_files",
          "record_id": "{{loop_item.id}}"
        }
      ]
    }
  ]
}
```

### 3. File Versioning

```javascript
// File version management
{
  "function_stack": [
    {
      "function": "get_record",
      "table": "documents",
      "record_id": "{{document_id}}"
    },
    {
      "function": "add_record",
      "table": "document_versions",
      "data": {
        "document_id": "{{document_id}}",
        "version_number": "{{documents.current_version + 1}}",
        "file": "{{new_file}}",
        "changes": "{{changes}}",
        "created_by": "{{auth.user.id}}",
        "created_at": "{{now()}}"
      }
    },
    {
      "function": "edit_record",
      "table": "documents",
      "record_id": "{{document_id}}",
      "data": {
        "current_version": "{{documents.current_version + 1}}",
        "current_file": "{{new_file}}",
        "updated_at": "{{now()}}"
      }
    }
  ]
}
```

## Try This: Complete File Management System

Create a comprehensive file management workflow:

```javascript
// Complete file management implementation
{
  "upload_endpoint": {
    "path": "/api/files/upload",
    "method": "POST",
    "function_stack": [
      {
        "function": "validate_file",
        "max_size": "50MB",
        "allowed_types": ["image/*", "application/pdf", "text/*"]
      },
      {
        "function": "add_record",
        "table": "files",
        "data": {
          "file": "{{file}}",
          "name": "{{name || file.name}}",
          "description": "{{description}}",
          "folder_id": "{{folder_id || null}}",
          "is_public": "{{is_public || false}}",
          "uploaded_by": "{{auth.user.id}}",
          "uploaded_at": "{{now()}}"
        }
      },
      {
        "function": "conditional",
        "condition": "{{is_image(file.type)}}",
        "true_stack": [
          {
            "function": "generate_thumbnails",
            "sizes": [{"width": 150, "height": 150}, {"width": 300, "height": 300}]
          }
        ]
      },
      {
        "function": "add_record",
        "table": "file_activity",
        "data": {
          "file_id": "{{files.id}}",
          "action": "uploaded",
          "user_id": "{{auth.user.id}}",
          "timestamp": "{{now()}}"
        }
      }
    ]
  },
  "download_endpoint": {
    "path": "/api/files/{file_id}/download",
    "method": "GET",
    "function_stack": [
      {
        "function": "check_file_permissions",
        "file_id": "{{file_id}}",
        "user_id": "{{auth.user.id}}"
      },
      {
        "function": "log_file_access",
        "file_id": "{{file_id}}",
        "user_id": "{{auth.user.id}}"
      },
      {
        "function": "serve_file",
        "file_id": "{{file_id}}"
      }
    ]
  }
}
```

## Common File Storage Mistakes to Avoid

### ❌ Poor Practices
- Storing files without validation
- Missing access controls on private files
- Not implementing file cleanup
- Ignoring file size and type restrictions
- Storing sensitive files in public storage

### ✅ Best Practices
- Always validate file uploads
- Implement proper access controls
- Use appropriate storage types (public/private)
- Set up automated cleanup processes
- Monitor storage usage and costs

## Pro Tips

### 💡 **Performance Optimization**
- Use CDN for public file delivery
- Implement lazy loading for images
- Compress images before storage
- Cache frequently accessed files

### 🔒 **Security Best Practices**
- Validate file types and content
- Scan uploads for malware
- Use signed URLs for private files
- Implement rate limiting on uploads

### 📊 **Storage Management**
- Monitor storage usage regularly
- Implement file lifecycle policies
- Use appropriate file formats
- Set up automated backups

### 🔄 **Integration Patterns**
- Use webhooks for file processing
- Implement real-time upload progress
- Create file sharing workflows
- Set up automated file transformations

## Troubleshooting File Storage Issues

### Common Problems
1. **Upload failures**: Check file size limits and network connectivity
2. **Access denied errors**: Verify authentication and permissions
3. **Missing files**: Check file paths and storage configuration
4. **Slow uploads**: Optimize file sizes and use appropriate storage regions

File storage in Xano provides robust capabilities for managing all types of files with security, performance, and integration features essential for modern no-code applications.