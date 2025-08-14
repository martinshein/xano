---
title: "File Management with Metadata API - Complete Guide"
description: "Master file uploads, management, and integration with Xano's Metadata API - perfect for building media-rich applications with n8n, WeWeb, and Make"
category: api-endpoints
tags:
  - File Management
  - File Upload
  - Metadata API
  - Media Storage
  - Image Processing
difficulty: intermediate
reading_time: 12 minutes
last_updated: '2025-01-23'
prerequisites:
  - Basic understanding of file handling
  - Xano workspace with Metadata API access
  - Knowledge of multipart form data
---

# File Management with Metadata API

## 📋 **Quick Summary**

**What it does:** The Metadata API's file management capabilities allow you to upload, organize, and manage files programmatically within your Xano workspace.

**Why it matters:** This enables you to:
- Handle file uploads from any frontend or automation tool
- Store and organize media files centrally
- Associate files with database records seamlessly
- Build media-rich applications without custom file endpoints

**Time to implement:** 10-15 minutes for basic file upload, 30+ minutes for advanced workflows

---

## What You'll Learn

- How to upload files via Metadata API
- Different file types and constraints
- Associating files with database records
- File management best practices
- Error handling and validation
- Integration patterns for no-code tools

## Understanding File Management in Xano

Think of Xano's file storage as your centralized media library - like having a cloud storage service built directly into your backend that automatically integrates with your database.

### 🎯 **Perfect For:**
- User profile pictures and avatars
- Product images in e-commerce apps
- Document storage and management
- Media galleries and portfolios
- File-based data imports

## File Upload Fundamentals

### Supported File Types

Xano categorizes files into specific types with different handling:

| Type | Extensions | Max Size | Use Cases |
|------|------------|----------|-----------|
| **image** | jpg, jpeg, png, gif, webp | 10MB | Avatars, products, galleries |
| **video** | mp4, mov, avi, webm | 100MB | Tutorials, demos, content |
| **audio** | mp3, wav, aac, ogg | 50MB | Podcasts, music, sounds |
| **attachment** | pdf, doc, txt, zip, etc. | 25MB | Documents, files, data |

### Basic File Upload

The most straightforward way to upload a file:

```javascript
POST /api:metadata/file
Content-Type: multipart/form-data

{
  "workspace_id": 12345,
  "content": [file binary data],
  "type": "image"  // Optional: image, video, audio, or attachment
}
```

### 📝 **Example Response**

```json
{
  "id": "file_abc123",
  "created_at": 1681349436618,
  "name": "profile-photo.jpg",
  "url": "https://x8d0-doy0-xx99.n0.xano.io/file/abc123",
  "size": 245760,
  "type": "image",
  "mime_type": "image/jpeg",
  "metadata": {
    "width": 800,
    "height": 600,
    "format": "JPEG"
  }
}
```

## File Upload Patterns

### Pattern 1: Direct Upload from Form

Perfect for user-generated content:

```yaml
User Form → File Input → Upload to Metadata API → Store File ID in Database
```

**Implementation:**
```javascript
// Frontend form submission
const formData = new FormData();
formData.append('workspace_id', '12345');
formData.append('content', fileInput.files[0]);
formData.append('type', 'image');

const response = await fetch('/api:metadata/file', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer ' + metadataToken
  },
  body: formData
});
```

### Pattern 2: File + Database Record Creation

Upload file and create associated record in one workflow:

```yaml
1. Upload file via Metadata API
2. Get file metadata from response
3. Create database record with file reference
4. Return success with record and file info
```

**Example Implementation:**
```javascript
// 1. Upload file first
const fileResponse = await uploadFile(file);

// 2. Create database record with file reference
const recordResponse = await metadataAPI.createRecord({
  workspace_id: 12345,
  table_id: 67890,
  fields: {
    title: "Product Image",
    image: fileResponse.metadata, // File metadata object
    created_by: userId
  }
});
```

### Pattern 3: Bulk File Processing

For processing multiple files:

```yaml
Files Array → Process Each → Upload to API → Collect Results → Create Records
```

## File Metadata and Database Integration

### Understanding File Metadata

When you upload a file, Xano returns a metadata object that you store in your database:

```json
{
  "id": "file_abc123",
  "name": "product-image.jpg",
  "url": "https://instance.xano.io/file/abc123",
  "size": 245760,
  "type": "image",
  "mime_type": "image/jpeg",
  "width": 800,
  "height": 600
}
```

### Associating Files with Records

To link a file with a database record, store the file metadata in a field:

**Database Schema:**
```yaml
products table:
  - id (integer, primary)
  - name (text)
  - image (file) ← Store file metadata here
  - gallery (file, array) ← Multiple files
```

**Creating Record with File:**
```json
POST /api:metadata/content
{
  "workspace_id": 12345,
  "table_id": 67890,
  "fields": {
    "name": "Wireless Headphones",
    "price": 99.99,
    "image": {
      "id": "file_abc123",
      "name": "headphones.jpg",
      "url": "https://instance.xano.io/file/abc123",
      "size": 245760,
      "type": "image",
      "mime_type": "image/jpeg"
    }
  }
}
```

## No-Code Platform Integrations

### 🔗 **n8n File Upload Workflow**

```yaml
1. HTTP Request (Receive file from webhook)
2. Set Node (Prepare file data)
3. HTTP Request (Upload to Metadata API)
4. Set Node (Extract file metadata)
5. HTTP Request (Create database record)
6. Respond to Webhook (Return success)
```

**n8n HTTP Request Configuration:**
```yaml
Method: POST
URL: https://[instance].xano.io/api:metadata/file
Authentication: Header Auth
Header Name: Authorization
Header Value: Bearer [metadata-token]
Body Content Type: multipart-form-data
Fields:
  - workspace_id: 12345
  - content: [file from previous node]
  - type: image
```

### 🌐 **WeWeb File Upload Component**

```javascript
// WeWeb action for file upload
async function uploadToXano(file) {
  const formData = new FormData();
  formData.append('workspace_id', wwLib.envVars.WORKSPACE_ID);
  formData.append('content', file);
  formData.append('type', 'image');
  
  const response = await wwLib.api.post({
    url: wwLib.envVars.XANO_METADATA_API + '/file',
    data: formData,
    headers: {
      'Authorization': 'Bearer ' + wwLib.envVars.METADATA_TOKEN
    }
  });
  
  return response.data;
}
```

### 🔧 **Make File Processing**

```yaml
Scenario Steps:
1. Webhook (Receive file)
2. HTTP Request (Upload to Xano)
3. JSON Parse (Extract metadata)
4. HTTP Request (Update database)
5. Email (Notify completion)
```

## File Validation and Security

### Pre-Upload Validation

Always validate files before uploading:

```javascript
function validateFile(file, options = {}) {
  const errors = [];
  
  // Size validation
  const maxSize = options.maxSize || 10 * 1024 * 1024; // 10MB
  if (file.size > maxSize) {
    errors.push(`File too large. Max size: ${maxSize / 1024 / 1024}MB`);
  }
  
  // Type validation
  const allowedTypes = options.allowedTypes || ['image/jpeg', 'image/png'];
  if (!allowedTypes.includes(file.type)) {
    errors.push(`Invalid file type. Allowed: ${allowedTypes.join(', ')}`);
  }
  
  // Name validation
  if (file.name.length > 100) {
    errors.push('Filename too long. Max 100 characters.');
  }
  
  return errors;
}
```

### Security Best Practices

#### 1. **File Type Enforcement**
```javascript
// Enforce specific file types
const uploadConfig = {
  image: ['image/jpeg', 'image/png', 'image/webp'],
  document: ['application/pdf', 'text/plain'],
  video: ['video/mp4', 'video/webm']
};
```

#### 2. **Size Limits**
```javascript
// Different size limits by type
const sizeLimits = {
  image: 5 * 1024 * 1024,    // 5MB
  video: 50 * 1024 * 1024,   // 50MB
  document: 10 * 1024 * 1024  // 10MB
};
```

#### 3. **Content Scanning**
```javascript
// Basic content validation
function validateImageContent(file) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(true);
    img.onerror = () => reject(new Error('Invalid image file'));
    img.src = URL.createObjectURL(file);
  });
}
```

## Error Handling

### Common Upload Errors

| Error Code | Issue | Solution |
|------------|-------|----------|
| 400 | Invalid file format | Check file type and size |
| 401 | Authentication failed | Verify Metadata API token |
| 413 | File too large | Reduce file size or compress |
| 415 | Unsupported media type | Use allowed file formats |
| 500 | Server error | Retry or contact support |

### Robust Error Handling

```javascript
async function uploadWithRetry(file, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      // Validate file first
      const errors = validateFile(file);
      if (errors.length > 0) {
        throw new Error(`Validation failed: ${errors.join(', ')}`);
      }
      
      // Attempt upload
      const result = await uploadFile(file);
      return result;
      
    } catch (error) {
      console.log(`Upload attempt ${attempt} failed:`, error.message);
      
      if (attempt === maxRetries) {
        throw error;
      }
      
      // Wait before retry (exponential backoff)
      await new Promise(resolve => 
        setTimeout(resolve, 1000 * Math.pow(2, attempt - 1))
      );
    }
  }
}
```

## Advanced File Management

### File Organization Patterns

#### 1. **Folder-like Organization**
```javascript
// Use naming conventions for organization
const fileName = `users/${userId}/profile/${Date.now()}_${originalName}`;
```

#### 2. **Metadata Tagging**
```json
{
  "name": "profile-photo.jpg",
  "tags": ["profile", "user-123", "avatar"],
  "category": "user-content",
  "visibility": "private"
}
```

#### 3. **Version Control**
```javascript
// Keep track of file versions
const versionedName = `${baseFileName}_v${version}.${extension}`;
```

### File Processing Workflows

#### Image Optimization Pipeline

```yaml
1. Upload original image
2. Generate thumbnails (if needed client-side)
3. Create multiple sizes (small, medium, large)
4. Store all versions in database
5. Serve appropriate size based on context
```

#### Document Processing

```yaml
1. Upload document
2. Extract metadata (pages, size, type)
3. Generate preview (if possible)
4. Store in searchable format
5. Create access logs
```

## Performance Optimization

### Client-Side Optimization

```javascript
// Compress images before upload
function compressImage(file, quality = 0.8) {
  return new Promise((resolve) => {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const img = new Image();
    
    img.onload = () => {
      // Calculate new dimensions
      const ratio = Math.min(1920/img.width, 1080/img.height);
      canvas.width = img.width * ratio;
      canvas.height = img.height * ratio;
      
      // Draw and compress
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      canvas.toBlob(resolve, 'image/jpeg', quality);
    };
    
    img.src = URL.createObjectURL(file);
  });
}
```

### Upload Progress Tracking

```javascript
function uploadWithProgress(file, onProgress) {
  return new Promise((resolve, reject) => {
    const formData = new FormData();
    formData.append('workspace_id', workspaceId);
    formData.append('content', file);
    
    const xhr = new XMLHttpRequest();
    
    xhr.upload.addEventListener('progress', (event) => {
      if (event.lengthComputable) {
        const progress = (event.loaded / event.total) * 100;
        onProgress(progress);
      }
    });
    
    xhr.addEventListener('load', () => {
      if (xhr.status === 200) {
        resolve(JSON.parse(xhr.responseText));
      } else {
        reject(new Error(`Upload failed: ${xhr.statusText}`));
      }
    });
    
    xhr.open('POST', '/api:metadata/file');
    xhr.setRequestHeader('Authorization', `Bearer ${token}`);
    xhr.send(formData);
  });
}
```

## 💡 **Try This**

### Beginner Challenge
Create a simple file upload form that:
1. Validates file size and type
2. Shows upload progress
3. Displays the uploaded file
4. Saves file metadata to database

### Intermediate Challenge
Build a photo gallery system that:
1. Accepts multiple image uploads
2. Creates thumbnails
3. Organizes by categories
4. Provides search functionality

### Advanced Challenge
Design a document management system that:
1. Handles various file types
2. Implements access controls
3. Provides version history
4. Generates activity logs

## Common Mistakes to Avoid

1. **Not validating files** - Always validate size, type, and content
2. **Missing error handling** - Upload failures are common
3. **Storing files in database** - Use metadata references, not file content
4. **No progress feedback** - Users need upload progress indication
5. **Ignoring security** - Validate and sanitize all uploaded content

## Next Steps

- Explore [Content Management](content.md) for database integration
- Learn about [Search Operations](search.md) for finding files
- Master [Workspace Management](workspace-import-and-export.md)
- Understand [Token Security](token-scopes-reference.md)

## Need Help?

- 📚 [Xano Community](https://community.xano.com) - File upload discussions
- 🎥 [Video Tutorials](https://university.xano.com) - Step-by-step guides
- 📖 [File Storage Docs](../../file-storage/file-storage-in-xano.md) - Comprehensive reference
- 🔧 [Support](https://xano.com/support) - Technical assistance