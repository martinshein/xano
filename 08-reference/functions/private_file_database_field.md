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
- File Storage
- Security
- Private Files
title: Private File Database Field
---

# Private File Database Field

## 📋 **Quick Summary**
Private file database fields in Xano provide secure file storage with controlled access through signed URLs. Unlike public files, private files require authentication and time-limited URL generation to ensure sensitive content remains protected while still being accessible to authorized users.

## 🎯 **Core Concepts**

### Private File Storage Components
1. **Private File Database Field**: Database field configured for private file storage
2. **Private File: Sign URL Function**: Generates time-limited, authenticated access URLs
3. **TTL (Time To Live)**: Configurable expiration time for file access
4. **Path Storage**: File paths stored in database without direct URL access

### Security Features
- No direct file URLs in database responses
- Time-limited access through signed URLs
- Per-field privacy configuration
- Authentication-based access control

## 🛠️ **Implementation Guide**

### Step 1: Configure Private File Database Field

```javascript
// In Xano database table setup:
// 1. Add file field (image, file, or video)
// 2. Enable "Private File Storage" option
// 3. Lock icon appears indicating private status
// 4. No URL previews in database view (by design)

// Example table structure:
{
  "id": 1,
  "name": "Confidential Document",
  "private_file": "private-files/documents/confidential-doc.pdf", // Path only
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Step 2: Query Private File Records

```javascript
// Function stack to get private file record
// Returns path, not URL for private files

// Database query result:
{
  "id": 1,
  "name": "Confidential Document",
  "private_file": "private-files/documents/confidential-doc.pdf", // No URL provided
  "file_size": 2048576,
  "mime_type": "application/pdf"
}

// Compare with public file (includes direct URL):
{
  "id": 2,
  "name": "Public Document",
  "public_file": "https://files.xano.io/public/document.pdf", // Direct URL available
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Step 3: Generate Signed URL

```javascript
// Using Private File: Sign URL function
// Function stack configuration:
{
  "function": "Private File: Sign URL",
  "inputs": {
    "file_path": "{{file_record.private_file}}", // Path from database
    "ttl": 3600, // 1 hour in seconds
    "return_variable": "signed_url"
  }
}

// Generated signed URL result:
{
  "signed_url": "https://files.xano.io/signed/abc123def456...?expires=1705401000",
  "expires_at": "2024-01-15T11:30:00Z"
}
```

## 🔗 **Integration Examples**

### n8n Private File Access Workflow
```javascript
// n8n HTTP Request to get private file record
{
  "method": "GET",
  "url": "https://your-xano.xano.io/api:v1/documents/{{$json.document_id}}",
  "headers": {
    "Authorization": "Bearer {{$node.auth.token}}"
  }
}

// Follow-up request to generate signed URL
{
  "method": "POST",
  "url": "https://your-xano.xano.io/api:v1/generate_file_access",
  "headers": {
    "Authorization": "Bearer {{$node.auth.token}}",
    "Content-Type": "application/json"
  },
  "body": {
    "file_path": "{{$json.private_file}}",
    "ttl": 1800, // 30 minutes
    "user_id": "{{$json.user_id}}"
  }
}
```

### WeWeb Private File Display
```vue
<template>
  <div class="private-file-viewer">
    <!-- Show loading state while generating signed URL -->
    <div v-if="loading" class="loading-spinner">
      Generating secure access...
    </div>
    
    <!-- Display file once signed URL is ready -->
    <div v-else-if="signedUrl" class="file-container">
      <img 
        v-if="isImage" 
        :src="signedUrl" 
        :alt="fileName"
        @error="handleImageError"
      />
      <iframe 
        v-else-if="isPDF" 
        :src="signedUrl" 
        class="pdf-viewer"
      ></iframe>
      <a 
        v-else 
        :href="signedUrl" 
        :download="fileName"
        class="download-link"
      >
        Download {{ fileName }}
      </a>
    </div>
    
    <!-- Error state -->
    <div v-else class="error-message">
      Unable to access file. Please try again.
    </div>
  </div>
</template>

<script>
export default {
  props: {
    fileRecord: Object,
    userId: String
  },
  data() {
    return {
      signedUrl: null,
      loading: false,
      error: null
    }
  },
  computed: {
    fileName() {
      return this.fileRecord.name || 'Unknown File'
    },
    isImage() {
      return this.fileRecord.mime_type?.startsWith('image/')
    },
    isPDF() {
      return this.fileRecord.mime_type === 'application/pdf'
    }
  },
  async mounted() {
    await this.generateSignedUrl()
  },
  methods: {
    async generateSignedUrl() {
      this.loading = true
      try {
        const response = await this.$xano.auth.post('/generate_file_access', {
          file_path: this.fileRecord.private_file,
          ttl: 1800, // 30 minutes
          user_id: this.userId
        })
        this.signedUrl = response.signed_url
      } catch (error) {
        console.error('Error generating signed URL:', error)
        this.error = 'Failed to access file'
      } finally {
        this.loading = false
      }
    },
    handleImageError() {
      this.error = 'Image failed to load'
    }
  }
}
</script>
```

## 🚀 **Advanced Usage Patterns**

### Time-Based Access Control
```javascript
// Different TTL values for different scenarios
const ttlSettings = {
  "preview": 300,      // 5 minutes for quick previews
  "download": 1800,    // 30 minutes for downloads
  "admin": 86400,      // 24 hours for admin access
  "temporary": 60      // 1 minute for one-time access
}

// Dynamic TTL based on user role
function calculateTTL(userRole, accessType) {
  const baseTTL = ttlSettings[accessType] || 300
  
  switch(userRole) {
    case 'admin':
      return baseTTL * 4 // Extended access for admins
    case 'premium':
      return baseTTL * 2 // Extended access for premium users
    default:
      return baseTTL
  }
}
```

### Batch URL Generation
```javascript
// Generate signed URLs for multiple private files
// Function stack for bulk operations
{
  "function": "Loop",
  "input_array": "{{private_files}}",
  "loop_item_variable": "file",
  "steps": [
    {
      "function": "Private File: Sign URL",
      "inputs": {
        "file_path": "{{file.private_file}}",
        "ttl": "{{calculateTTL(user.role, 'download')}}",
        "return_variable": "signed_url"
      }
    },
    {
      "function": "Update Variable",
      "variable": "signed_files",
      "operation": "append",
      "value": {
        "id": "{{file.id}}",
        "name": "{{file.name}}",
        "url": "{{signed_url}}",
        "expires_at": "{{timestamp + ttl}}"
      }
    }
  ]
}
```

### Access Logging
```javascript
// Track private file access for security auditing
{
  "function": "Add Record",
  "table": "file_access_log",
  "data": {
    "file_id": "{{file_record.id}}",
    "user_id": "{{auth_user.id}}",
    "access_type": "signed_url_generated",
    "ip_address": "{{request.ip}}",
    "user_agent": "{{request.user_agent}}",
    "ttl_granted": "{{ttl}}",
    "expires_at": "{{timestamp + ttl}}",
    "accessed_at": "{{timestamp}}"
  }
}
```

## 🎯 **Best Practices**

### 1. Appropriate TTL Selection
```javascript
// Choose TTL based on use case:
const ttlGuidelines = {
  "image_preview": 300,        // 5 minutes - quick viewing
  "document_review": 3600,     // 1 hour - reading time
  "video_streaming": 7200,     // 2 hours - viewing duration
  "bulk_download": 1800,       // 30 minutes - download time
  "api_integration": 600       // 10 minutes - processing time
}
```

### 2. Error Handling
```javascript
// Robust error handling for signed URL generation
try {
  const signedUrl = await generateSignedUrl(filePath, ttl)
  return { success: true, url: signedUrl }
} catch (error) {
  if (error.code === 'FILE_NOT_FOUND') {
    return { success: false, error: 'File no longer exists' }
  } else if (error.code === 'ACCESS_DENIED') {
    return { success: false, error: 'Insufficient permissions' }
  } else {
    return { success: false, error: 'Unable to generate access URL' }
  }
}
```

### 3. URL Refresh Strategy
```javascript
// Automatically refresh signed URLs before expiration
function setupUrlRefresh(signedUrl, expiresAt) {
  const refreshTime = expiresAt - (5 * 60 * 1000) // 5 minutes before expiry
  const now = Date.now()
  
  if (refreshTime > now) {
    setTimeout(() => {
      refreshSignedUrl()
    }, refreshTime - now)
  }
}
```

## 🔧 **Common Use Cases**

### Sensitive Document Management
```javascript
// Legal documents, contracts, financial records
{
  "table": "legal_documents",
  "fields": {
    "document_file": "private_file", // Confidential documents
    "access_level": "restricted",
    "allowed_roles": ["legal", "admin"]
  }
}
```

### User Profile Pictures (Privacy Mode)
```javascript
// Private profile images for dating apps, professional networks
{
  "table": "user_profiles",
  "fields": {
    "private_avatar": "private_file", // Only visible to matched/connected users
    "privacy_setting": "private"
  }
}
```

### Premium Content Access
```javascript
// Subscriber-only content, paid courses, exclusive media
{
  "table": "premium_content",
  "fields": {
    "content_file": "private_file", // Protected premium content
    "subscription_tier": "premium",
    "access_duration": 7200 // 2 hours viewing time
  }
}
```

### Medical Records Storage
```javascript
// HIPAA-compliant file storage with audit trails
{
  "table": "medical_records",
  "fields": {
    "record_file": "private_file", // Protected health information
    "patient_id": "encrypted",
    "access_logged": true
  }
}
```

## 🔍 **Troubleshooting**

### File Access Issues
- **No URL returned**: Verify field is configured for private storage
- **Signed URL expired**: Check TTL settings and refresh mechanism
- **Access denied**: Verify user permissions and authentication
- **File not found**: Confirm file path exists in storage

### Performance Optimization
- Cache signed URLs with appropriate TTL
- Batch generate URLs for multiple files
- Use appropriate TTL values to minimize regeneration
- Implement URL refresh before expiration

---

*Private file storage ensures sensitive content remains secure while providing controlled access through time-limited, authenticated URLs.*