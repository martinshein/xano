---
title: "File Storage - Managing Files and Media"
description: "Upload, store, and manage files in your Xano backend"
category: function-stack
subcategory: storage
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- files
- storage
- upload
- media
- images
---

# File Storage - Managing Files and Media



## Quick Summary

> **What it is:** Functions for uploading, storing, and managing files in your backend
> 
> **When to use:** User profile photos, document uploads, CSV processing, or any file handling
> 
> **Key benefit:** Built-in file management with automatic optimization and CDN delivery
> 
> **Perfect for:** Non-developers building apps with file uploads, image galleries, or document management

## What You'll Learn

- File upload basics
- Working with images
- Processing files
- Storage strategies
- CDN and optimization

## File Upload Flow

### Three States of Files

1. **File Resource**
   - Base64 encoded reference
   - Used during function execution
   - Passed between functions

2. **Raw File Data**
   - Actual file contents
   - For processing (CSV, text)
   - Can be manipulated

3. **Metadata**
   - File information
   - Name, size, type, URL
   - Stored in database

## Basic File Upload

### Step 1: Create Upload Endpoint
```javascript
// API Input
file: file (type: file)
user_id: integer

// Function Stack
uploaded_file = Input.file
```

### Step 2: Store File
```javascript
// Create file resource
file_data = Create_File_Resource {
  file: uploaded_file,
  type: "image"
}

// Get metadata
file_url = file_data.url
file_size = file_data.size
file_name = file_data.name
```

### Step 3: Save to Database
```javascript
Add_Record {
  table: "user_files",
  user_id: Input.user_id,
  file_url: file_url,
  file_name: file_name,
  file_size: file_size,
  uploaded_at: timestamp()
}
```

## Integration Examples

### With n8n - Bulk File Processing
```javascript
// n8n sends file URL
file_url = Webhook.file_url

// Download file
file = Download_File(file_url)

// Process file
if (file.type == "csv") {
  csv_data = Parse_CSV(file)
  
  For Each row in csv_data {
    Add_Record {
      table: "imported_data",
      data: row
    }
  }
}
```

### With WeWeb - Profile Photo Upload
```javascript
// WeWeb sends photo
photo = Input.profile_photo

// Resize and optimize
optimized = Image_Manipulation {
  file: photo,
  resize: {
    width: 500,
    height: 500,
    mode: "cover"
  },
  quality: 85
}

// Create thumbnail
thumbnail = Image_Manipulation {
  file: photo,
  resize: {
    width: 150,
    height: 150,
    mode: "cover"
  }
}

// Store both versions
Edit_Record {
  id: Auth.user_id,
  profile_photo: optimized.url,
  profile_thumbnail: thumbnail.url
}
```

## Image Manipulation

### Resize Options
```javascript
Image_Manipulation {
  file: Input.image,
  resize: {
    width: 800,
    height: 600,
    mode: "contain"  // or "cover", "fill"
  }
}
```

### Image Formats
```javascript
// Convert to different format
converted = Image_Manipulation {
  file: Input.image,
  format: "webp",  // or "jpg", "png"
  quality: 90
}
```

### Multiple Sizes
```javascript
// Generate responsive images
sizes = [
  {name: "small", width: 320},
  {name: "medium", width: 768},
  {name: "large", width: 1920}
]

image_urls = {}
For Each size in sizes {
  resized = Image_Manipulation {
    file: Input.image,
    resize: {width: size.width}
  }
  image_urls[size.name] = resized.url
}
```

## File Processing

### CSV Files
```javascript
// Parse CSV
csv_file = Input.csv_file
csv_data = Get_File_Data(csv_file)

// Process rows
rows = Parse_CSV(csv_data)
For Each row in rows {
  // Process each row
  Process_Row(row)
}
```

### Text Files
```javascript
// Read text file
text_file = Input.document
content = Get_File_Data(text_file)

// Process content
lines = content.split("\n")
word_count = content.split(" ").length
```

### JSON Files
```javascript
// Parse JSON file
json_file = Input.data_file
json_string = Get_File_Data(json_file)
data = json_decode(json_string)

// Use parsed data
Process_Data(data)
```

## Storage Strategies

### Public vs Private Files

**Public Files** (default):
```javascript
// Accessible via URL
file_resource = Create_File_Resource {
  file: Input.file,
  private: false
}
// Returns: https://cdn.xano.io/public/file.jpg
```

**Private Files**:
```javascript
// Requires authentication
file_resource = Create_File_Resource {
  file: Input.file,
  private: true
}
// Generate signed URL for access
signed_url = Generate_Signed_URL {
  file: file_resource,
  expires_in: 3600  // 1 hour
}
```

### File Organization
```javascript
// Organize by user and date
path = "users/" + user_id + "/" + 
       year + "/" + month + "/" + 
       file_name

file_resource = Create_File_Resource {
  file: Input.file,
  path: path
}
```

## File Validation

### Size Limits
```javascript
// Check file size (10MB limit)
max_size = 10485760  // 10MB in bytes

if (Input.file.size > max_size) {
  return {
    error: "File too large. Maximum 10MB allowed."
  }
}
```

### Type Validation
```javascript
// Allowed file types
allowed_types = ["image/jpeg", "image/png", "image/gif"]

if (!allowed_types.includes(Input.file.type)) {
  return {
    error: "Invalid file type. Only JPEG, PNG, and GIF allowed."
  }
}
```

### Filename Sanitization
```javascript
// Clean filename
original_name = Input.file.name
clean_name = original_name
  .toLowerCase()
  .replace(/[^a-z0-9.-]/g, "_")
  .replace(/__+/g, "_")
```

## CDN and Performance

### Automatic CDN
All files automatically served via CDN:
- Global distribution
- Fast delivery
- Automatic caching
- HTTPS secure

### Image Optimization
```javascript
// Auto-optimize for web
optimized = Image_Manipulation {
  file: Input.image,
  auto_optimize: true,
  format: "auto"  // Best format for browser
}
```

### Lazy Loading Support
```javascript
// Generate blur placeholder
placeholder = Image_Manipulation {
  file: Input.image,
  resize: {width: 20},
  blur: 10
}

return {
  image_url: full_image.url,
  placeholder: placeholder.url
}
```

## Common Patterns

### Avatar Upload
```javascript
// Profile photo with validation
avatar = Input.avatar

// Validate
if (avatar.size > 5242880) {  // 5MB
  return {error: "Image too large"}
}

// Process
square_avatar = Image_Manipulation {
  file: avatar,
  resize: {
    width: 400,
    height: 400,
    mode: "cover"
  },
  format: "webp"
}

// Save
Update_User {
  id: Auth.user_id,
  avatar_url: square_avatar.url
}
```

### Document Management
```javascript
// Upload document with metadata
document = Input.document

// Create record
doc_record = Add_Record {
  table: "documents",
  user_id: Auth.user_id,
  file_url: document.url,
  file_name: document.name,
  file_size: document.size,
  file_type: document.type,
  uploaded_at: timestamp()
}

// Set permissions
Set_Permissions {
  document_id: doc_record.id,
  owner: Auth.user_id,
  shared_with: Input.share_with
}
```

### Bulk Upload
```javascript
// Multiple file upload
files = Input.files  // Array of files

uploaded = []
For Each file in files {
  // Process each file
  processed = Process_File(file)
  
  // Store metadata
  record = Add_Record {
    table: "uploads",
    file_data: processed
  }
  
  uploaded.push(record)
}

return {
  success: true,
  uploaded_count: uploaded.length
}
```

## Try This

Create a file upload system:
1. Add file input to API
2. Validate file type and size
3. Process/optimize if image
4. Store file and metadata
5. Return file URL

## Pro Tips

💡 **Validate Early:** Check size/type before processing

💡 **Optimize Images:** Reduce size for better performance

💡 **Use CDN URLs:** Always return CDN URLs to frontend

💡 **Clean Filenames:** Sanitize user-provided names

💡 **Track Usage:** Monitor storage consumption

## Common Gotchas

### File Size Limits
- API limit: 100MB per file
- Recommended: <10MB for images
- Use chunked upload for large files

### CORS Issues
```javascript
// Enable CORS for file URLs
response.headers = {
  "Access-Control-Allow-Origin": "*"
}
```

### Missing Files
```javascript
// Check file exists
if (!Input.file) {
  return {error: "No file provided"}
}

// Check file not empty
if (Input.file.size == 0) {
  return {error: "Empty file"}
}
```

## Next Steps

1. Set up file upload endpoint
2. Add validation rules
3. Implement image optimization
4. Configure private storage
5. Monitor usage and costs

Remember: Xano handles the infrastructure - you focus on building great file experiences!