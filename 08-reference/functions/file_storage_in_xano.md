---
category: functions
description: Complete file storage guide for Xano with upload handling, transformation, cloud integration, and security best practices
difficulty: intermediate
has_code_examples: true
last_updated: '2025-08-20'
related_docs:
  - file-upload.md
  - cloud-storage.md
  - image-processing.md
  - security.md
subcategory: 08-reference/functions
tags:
  - file-storage
  - uploads
  - cloud-integration
  - security
  - transformations
  - optimization
title: File Storage in Xano
---

# File Storage in Xano

## 📋 **Quick Summary**
Master file storage in Xano with secure upload handling, cloud integration, real-time processing, and optimization strategies for scalable file management systems.

## What You'll Learn
- File upload and validation patterns
- Cloud storage integration (AWS S3, Google Cloud, Azure)
- Image and document processing
- Security and access control
- Performance optimization techniques
- Integration with n8n and WeWeb

## File Storage Architecture

### Storage Options
```javascript
// Xano file storage options
const storageOptions = {
  "xano_storage": {
    "description": "Built-in Xano file storage",
    "best_for": "Small to medium files, development",
    "limitations": "Storage limits based on plan",
    "advantages": ["Easy setup", "Integrated with Xano", "No external dependencies"]
  },
  
  "aws_s3": {
    "description": "Amazon S3 integration",
    "best_for": "Production apps, large files, global CDN",
    "advantages": ["Unlimited storage", "CDN integration", "Advanced features"],
    "use_cases": ["High traffic apps", "Media storage", "Global distribution"]
  },
  
  "google_cloud": {
    "description": "Google Cloud Storage",
    "best_for": "AI/ML processing, analytics",
    "advantages": ["AI integration", "Analytics", "Competitive pricing"],
    "use_cases": ["Image recognition", "Document analysis", "Video processing"]
  },
  
  "azure_blob": {
    "description": "Microsoft Azure Blob Storage", 
    "best_for": "Enterprise applications",
    "advantages": ["Enterprise features", "Security", "Compliance"],
    "use_cases": ["Enterprise apps", "Compliance requirements", "B2B solutions"]
  }
};
```

## File Upload Implementation

### Basic Upload Handler
```javascript
// File upload function stack
[
  {
    "function": "Validate File",
    "logic": `
      // Check file size (10MB limit)
      if (inputs.file.size > 10 * 1024 * 1024) {
        return error(400, "File size exceeds 10MB limit");
      }
      
      // Check file type
      const allowedTypes = ['image/jpeg', 'image/png', 'image/webp', 'application/pdf'];
      if (!allowedTypes.includes(inputs.file.type)) {
        return error(400, "Unsupported file type");
      }
      
      // Check file extension
      const allowedExtensions = ['.jpg', '.jpeg', '.png', '.webp', '.pdf'];
      const extension = inputs.file.name.toLowerCase().substring(inputs.file.name.lastIndexOf('.'));
      if (!allowedExtensions.includes(extension)) {
        return error(400, "Invalid file extension");
      }
    `
  },
  {
    "function": "Generate Unique Filename",
    "logic": `
      const timestamp = Date.now();
      const randomString = Math.random().toString(36).substring(2, 8);
      const extension = inputs.file.name.substring(inputs.file.name.lastIndexOf('.'));
      const uniqueFilename = \`\${timestamp}_\${randomString}\${extension}\`;
      
      return {
        original_name: inputs.file.name,
        unique_filename: uniqueFilename,
        file_path: \`uploads/\${new Date().getFullYear()}/\${new Date().getMonth() + 1}/\${uniqueFilename}\`
      };
    `
  },
  {
    "function": "Upload to Storage",
    "action": "upload_file",
    "file": "inputs.file",
    "filename": "filename_data.unique_filename",
    "path": "filename_data.file_path"
  },
  {
    "function": "Save File Record",
    "action": "add_record",
    "table": "files",
    "data": {
      "original_name": "filename_data.original_name",
      "filename": "filename_data.unique_filename", 
      "file_path": "filename_data.file_path",
      "file_size": "inputs.file.size",
      "file_type": "inputs.file.type",
      "uploaded_by": "auth.user.id",
      "uploaded_at": "now()",
      "public_url": "upload_result.url"
    }
  }
]
```

### Advanced Upload with Processing
```javascript
// Advanced file processing pipeline
const advancedUploadPipeline = {
  "image_upload_with_variants": [
    {
      "function": "Validate Image",
      "logic": `
        const imageTypes = ['image/jpeg', 'image/png', 'image/webp'];
        if (!imageTypes.includes(inputs.file.type)) {
          return error(400, "Only image files are allowed");
        }
        
        // Additional image validation
        const maxDimension = 4000; // 4000px max width/height
        if (inputs.file.width > maxDimension || inputs.file.height > maxDimension) {
          return error(400, "Image dimensions too large");
        }
      `
    },
    {
      "function": "Process Image Variants",
      "lambda_function": "image_processor",
      "code": `
        const sharp = require('sharp');
        
        async function processImageVariants(fileBuffer, originalName) {
          const variants = {
            thumbnail: { width: 150, height: 150, fit: 'cover' },
            small: { width: 400, height: 300, fit: 'inside' },
            medium: { width: 800, height: 600, fit: 'inside' },
            large: { width: 1200, height: 900, fit: 'inside' }
          };
          
          const results = {};
          
          for (const [variantName, options] of Object.entries(variants)) {
            const processed = await sharp(fileBuffer)
              .resize(options.width, options.height, { fit: options.fit })
              .jpeg({ quality: 85, progressive: true })
              .toBuffer();
            
            // Generate filename for variant
            const extension = originalName.substring(originalName.lastIndexOf('.'));
            const baseName = originalName.substring(0, originalName.lastIndexOf('.'));
            const variantFilename = \`\${baseName}_\${variantName}\${extension}\`;
            
            results[variantName] = {
              buffer: processed,
              filename: variantFilename,
              size: processed.length
            };
          }
          
          return results;
        }
        
        return await processImageVariants(inputs.file.buffer, inputs.file.name);
      `
    },
    {
      "function": "Upload All Variants",
      "loop": "processed_variants",
      "upload_action": "upload_to_s3",
      "generate_urls": true
    },
    {
      "function": "Save File Metadata",
      "action": "add_record",
      "table": "media_files",
      "data": {
        "original_name": "inputs.file.name",
        "file_type": "inputs.file.type",
        "variants": "upload_results",
        "uploaded_by": "auth.user.id",
        "created_at": "now()",
        "metadata": {
          "dimensions": {
            "width": "inputs.file.width",
            "height": "inputs.file.height"
          },
          "processing_time": "processing_duration"
        }
      }
    }
  ]
};
```

## Cloud Storage Integration

### AWS S3 Integration
```javascript
// S3 upload with advanced features
const s3Integration = {
  // Direct S3 upload with presigned URLs
  generatePresignedUpload: {
    "lambda_function": "s3_presigned_url",
    "code": `
      const AWS = require('aws-sdk');
      const s3 = new AWS.S3({
        accessKeyId: process.env.AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
        region: process.env.AWS_REGION
      });
      
      async function generatePresignedUrl(filename, contentType, userId) {
        const key = \`uploads/\${userId}/\${Date.now()}_\${filename}\`;
        
        const params = {
          Bucket: process.env.S3_BUCKET,
          Key: key,
          Expires: 300, // 5 minutes
          ContentType: contentType,
          Metadata: {
            'uploaded-by': userId.toString(),
            'upload-timestamp': Date.now().toString()
          }
        };
        
        const uploadUrl = await s3.getSignedUrlPromise('putObject', params);
        
        return {
          upload_url: uploadUrl,
          file_key: key,
          expires_in: 300
        };
      }
      
      return await generatePresignedUrl(
        inputs.filename, 
        inputs.content_type, 
        auth.user.id
      );
    `
  },
  
  // S3 webhook for processing completion
  s3ProcessingWebhook: [
    {
      "function": "Verify S3 Signature",
      "logic": `
        // Verify webhook signature from S3
        const signature = request_headers['x-amz-sns-message-signature'];
        const message = JSON.parse(inputs.raw_body);
        
        // Validate SNS message signature
        const isValid = validateSNSSignature(message, signature);
        if (!isValid) {
          return error(401, "Invalid webhook signature");
        }
      `
    },
    {
      "function": "Process S3 Event",
      "logic": `
        const s3Event = JSON.parse(message.Message);
        const record = s3Event.Records[0];
        
        if (record.eventName.startsWith('s3:ObjectCreated:')) {
          const bucket = record.s3.bucket.name;
          const key = record.s3.object.key;
          const size = record.s3.object.size;
          
          // Update file record with S3 metadata
          const fileRecord = await queryDatabase(
            "SELECT id FROM media_files WHERE file_key = ?",
            [key]
          );
          
          if (fileRecord.length > 0) {
            await updateRecord("media_files", fileRecord[0].id, {
              storage_provider: 's3',
              storage_bucket: bucket,
              file_size: size,
              processing_status: 'completed',
              public_url: \`https://\${bucket}.s3.amazonaws.com/\${key}\`
            });
          }
        }
      `
    }
  ]
};
```

### Multi-Cloud Storage Strategy
```javascript
// Multi-cloud storage with failover
const multiCloudStorage = {
  "upload_with_redundancy": {
    "logic": `
      async function uploadWithRedundancy(fileData, filename) {
        const providers = [
          { name: 's3', priority: 1, endpoint: 'aws_s3_upload' },
          { name: 'gcp', priority: 2, endpoint: 'gcp_storage_upload' },
          { name: 'azure', priority: 3, endpoint: 'azure_blob_upload' }
        ];
        
        const results = { primary: null, backups: [], errors: [] };
        
        // Try primary provider first
        try {
          const primaryResult = await uploadToProvider(providers[0], fileData, filename);
          results.primary = {
            provider: providers[0].name,
            url: primaryResult.url,
            success: true
          };
        } catch (error) {
          results.errors.push({ provider: providers[0].name, error: error.message });
        }
        
        // Upload to backup providers
        for (let i = 1; i < providers.length; i++) {
          try {
            const backupResult = await uploadToProvider(providers[i], fileData, filename);
            results.backups.push({
              provider: providers[i].name,
              url: backupResult.url,
              success: true
            });
          } catch (error) {
            results.errors.push({ provider: providers[i].name, error: error.message });
          }
        }
        
        return results;
      }
      
      return await uploadWithRedundancy(inputs.file_data, inputs.filename);
    `
  }
};
```

## Security and Access Control

### Secure File Access
```javascript
// Secure file access patterns
const secureFileAccess = {
  // Generate temporary download URLs
  generateSecureUrl: [
    {
      "function": "Validate Access",
      "logic": `
        // Check if user has permission to access file
        const file = await queryDatabase(
          "SELECT * FROM files WHERE id = ?",
          [inputs.file_id]
        );
        
        if (!file.length) {
          return error(404, "File not found");
        }
        
        const fileRecord = file[0];
        
        // Check ownership or shared access
        if (fileRecord.uploaded_by !== auth.user.id) {
          const sharedAccess = await queryDatabase(
            "SELECT * FROM file_shares WHERE file_id = ? AND user_id = ? AND expires_at > NOW()",
            [inputs.file_id, auth.user.id]
          );
          
          if (!sharedAccess.length) {
            return error(403, "Access denied");
          }
        }
      `
    },
    {
      "function": "Generate Temporary URL",
      "lambda_function": "generate_secure_url",
      "code": `
        const crypto = require('crypto');
        
        function generateSecureDownloadUrl(fileId, userId, expiresIn = 3600) {
          const expires = Date.now() + (expiresIn * 1000);
          const signature = crypto
            .createHmac('sha256', process.env.FILE_ACCESS_SECRET)
            .update(\`\${fileId}:\${userId}:\${expires}\`)
            .digest('hex');
          
          return {
            download_url: \`/api/files/download/\${fileId}?expires=\${expires}&signature=\${signature}\`,
            expires_at: new Date(expires).toISOString(),
            valid_for: expiresIn
          };
        }
        
        return generateSecureDownloadUrl(inputs.file_id, auth.user.id, inputs.expires_in);
      `
    }
  ],
  
  // File download with access validation
  secureDownload: [
    {
      "function": "Validate Download Token",
      "logic": `
        const { expires, signature } = inputs;
        const currentTime = Date.now();
        
        // Check if link has expired
        if (currentTime > parseInt(expires)) {
          return error(410, "Download link has expired");
        }
        
        // Verify signature
        const expectedSignature = crypto
          .createHmac('sha256', environment_variables.FILE_ACCESS_SECRET)
          .update(\`\${inputs.file_id}:\${auth.user.id}:\${expires}\`)
          .digest('hex');
        
        if (signature !== expectedSignature) {
          return error(401, "Invalid download token");
        }
      `
    },
    {
      "function": "Stream File",
      "action": "stream_file",
      "file_path": "file_record.file_path",
      "content_type": "file_record.file_type",
      "download": true
    }
  ]
};
```

## n8n and WeWeb Integration

### n8n File Processing Workflows
```javascript
// n8n workflow: Automated file processing
{
  "name": "File Processing Pipeline",
  "trigger": {
    "type": "xano-webhook",
    "event": "file_uploaded"
  },
  "nodes": [
    {
      "name": "Analyze File Type",
      "type": "switch",
      "conditions": [
        {
          "case": "{{ $json.file_type.startsWith('image/') }}",
          "route": "process-image"
        },
        {
          "case": "{{ $json.file_type === 'application/pdf' }}",
          "route": "process-pdf"
        },
        {
          "case": "{{ $json.file_type.startsWith('video/') }}",
          "route": "process-video"
        }
      ]
    },
    {
      "name": "Process Image",
      "type": "xano-lambda",
      "function": "image-processor",
      "data": {
        "file_url": "{{ $json.public_url }}",
        "operations": ["resize", "optimize", "generate_thumbnails"]
      }
    },
    {
      "name": "Extract PDF Text", 
      "type": "xano-lambda",
      "function": "pdf-text-extractor",
      "data": {
        "file_url": "{{ $json.public_url }}"
      }
    },
    {
      "name": "Generate Video Thumbnails",
      "type": "xano-lambda",
      "function": "video-thumbnail-generator",
      "data": {
        "file_url": "{{ $json.public_url }}",
        "timestamps": [0, 30, 60] // Generate thumbnails at 0s, 30s, 60s
      }
    },
    {
      "name": "Update File Record",
      "type": "xano-api",
      "endpoint": "/files/{{ $json.file_id }}",
      "method": "PUT",
      "data": {
        "processing_status": "completed",
        "processed_data": "{{ $json }}"
      }
    }
  ]
}
```

### WeWeb File Management
```javascript
// WeWeb file management component
const wewebFileManager = {
  data: {
    files: [],
    uploadProgress: {},
    dragOver: false
  },
  
  methods: {
    async handleFileUpload(files) {
      for (const file of files) {
        await this.uploadFile(file);
      }
    },
    
    async uploadFile(file) {
      try {
        // Get presigned upload URL
        const presignedResponse = await wwLib.executeWorkflow('get-presigned-upload', {
          filename: file.name,
          content_type: file.type,
          file_size: file.size
        });
        
        if (!presignedResponse.success) {
          throw new Error('Failed to get upload URL');
        }
        
        // Upload directly to cloud storage
        const uploadResponse = await fetch(presignedResponse.upload_url, {
          method: 'PUT',
          body: file,
          headers: {
            'Content-Type': file.type
          },
          onUploadProgress: (progress) => {
            this.uploadProgress[file.name] = Math.round((progress.loaded / progress.total) * 100);
          }
        });
        
        if (uploadResponse.ok) {
          // Confirm upload with Xano
          await wwLib.executeWorkflow('confirm-file-upload', {
            file_key: presignedResponse.file_key,
            original_name: file.name,
            file_size: file.size
          });
          
          this.loadFiles(); // Refresh file list
        }
        
      } catch (error) {
        this.showError(`Failed to upload ${file.name}: ${error.message}`);
      } finally {
        delete this.uploadProgress[file.name];
      }
    },
    
    async deleteFile(fileId) {
      const confirmed = await this.confirmDelete();
      if (confirmed) {
        const response = await wwLib.executeWorkflow('delete-file', { file_id: fileId });
        if (response.success) {
          this.files = this.files.filter(f => f.id !== fileId);
        }
      }
    }
  }
};
```

## Try This: Build File Management System

1. **Set up Basic Upload**
   - Create file upload endpoint
   - Add validation and security
   - Test with different file types

2. **Add Cloud Storage**
   - Configure S3 or Google Cloud
   - Implement presigned URLs
   - Set up webhook processing

3. **Build Processing Pipeline**
   - Add image resizing
   - Implement text extraction
   - Create automated workflows

4. **Create Frontend Interface**
   - Build WeWeb upload component
   - Add drag-and-drop support
   - Display upload progress

## Common Mistakes to Avoid

- **Missing file validation** - Always validate file types and sizes
- **Insecure file access** - Implement proper access controls
- **Poor error handling** - Handle upload failures gracefully
- **Ignoring file limits** - Set and enforce storage limits
- **Missing cleanup** - Remove orphaned or expired files

## Pro Tips

💡 **Use presigned URLs** - Direct cloud uploads reduce server load

💡 **Implement file versioning** - Track file changes and allow rollbacks

💡 **Add virus scanning** - Scan uploads for malware and threats

💡 **Optimize for performance** - Compress images and use CDN

💡 **Monitor storage costs** - Track usage and implement cleanup policies