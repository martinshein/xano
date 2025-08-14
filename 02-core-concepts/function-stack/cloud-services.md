---
title: "Cloud Storage & Search - Enterprise Services Made Simple"
description: "Connect to AWS, Google Cloud, Azure, and Elasticsearch without code"
category: function-stack
subcategory: cloud-services
difficulty: intermediate
has_code_examples: true
last_updated: '2025-01-23'
tags:
- cloud-storage
- elasticsearch
- aws-s3
- azure
- google-cloud
---

# Cloud Storage & Search - Enterprise Services Made Simple



## Quick Summary

> **What it is:** Pre-built functions to connect with major cloud services for storage and search
> 
> **When to use:** Storing files in the cloud, implementing advanced search, or scaling beyond local storage
> 
> **Key benefit:** Enterprise-grade infrastructure without DevOps complexity
> 
> **Perfect for:** Non-developers building scalable applications with cloud services

## What You'll Learn

- Setting up cloud storage
- Managing files across platforms
- Implementing Elasticsearch
- Using signed URLs
- Best practices for cloud services

## Available Cloud Services

### Storage Services
- **Amazon S3** - AWS file storage
- **Google Cloud Storage** - GCS buckets
- **Azure Blob Storage** - Microsoft cloud
- **Xano Storage** - Built-in option

### Search Services
- **Elasticsearch** - Advanced search
- **OpenSearch** - AWS search service

## Amazon S3 Setup

### Getting Credentials

1. Log into AWS Console
2. Navigate to Security Credentials
3. Create Access Key
4. Save Key ID and Secret
5. Note your bucket name and region

### Common S3 Operations

```javascript
// List files
S3_List_Directory {
  bucket: "my-bucket",
  region: "us-west-2",
  key: env.AWS_KEY,
  secret: env.AWS_SECRET
}

// Upload file
S3_Upload {
  bucket: "my-bucket",
  file: Input.uploaded_file,
  file_key: "uploads/document.pdf"
}

// Generate signed URL (temporary access)
url = S3_Signed_URL {
  bucket: "my-bucket",
  file_key: "private/document.pdf",
  ttl: 3600  // 1 hour access
}
```

## Google Cloud Storage

### Service Account Setup

1. Create Service Account in GCP
2. Add required roles:
   - Storage Admin
   - Storage Object Admin
3. Download JSON key
4. Store as environment variable

### GCS Operations

```javascript
// Upload to GCS
GCS_Upload {
  service_account: env.GCS_KEY,
  bucket: "my-bucket",
  filePath: "images/photo.jpg",
  file: Input.image
}

// List directory
files = GCS_List {
  service_account: env.GCS_KEY,
  bucket: "my-bucket",
  path: "images/"
}
```

## Azure Blob Storage

### Azure Configuration

1. Create Storage Account
2. Create Container
3. Get Access Key
4. Store credentials

### Azure Operations

```javascript
// Upload to Azure
Azure_Upload {
  account_name: "mystorageaccount",
  account_key: env.AZURE_KEY,
  container: "files",
  filePath: "documents/report.pdf",
  file: Input.document
}

// Get file metadata
metadata = Azure_Get_Metadata {
  account_name: "mystorageaccount",
  container: "files",
  filePath: "documents/report.pdf"
}
```

## Elasticsearch Integration

### Setting Up Search

```javascript
// Configure connection
Elasticsearch_Config {
  auth_type: "Basic",
  key_id: "username",
  access_key: "password",
  base_url: "https://search.domain.com",
  index: "products"
}
```

### Search Operations

```javascript
// Query wizard
results = Elasticsearch_Query {
  // Visual query builder
  filters: [
    {field: "category", operator: "equals", value: "electronics"},
    {field: "price", operator: "less_than", value: 100}
  ],
  size: 20,
  from: 0,
  sort: [{field: "price", order: "asc"}]
}

// Add document
Elasticsearch_Document {
  method: "POST",
  document: {
    title: "Product Name",
    category: "electronics",
    price: 49.99,
    description: "Product description"
  }
}
```

## Integration Examples

### With n8n - File Processing

```javascript
// n8n sends file
file_data = Webhook.file

// Process and store
processed = Process_File(file_data)

// Upload to S3
s3_result = S3_Upload {
  bucket: "processed-files",
  file: processed,
  file_key: "output/" + timestamp
}

// Return S3 URL
return s3_result.url
```

### With WeWeb - User Uploads

```javascript
// WeWeb form with file
user_file = Input.profile_photo

// Generate unique name
file_name = user.id + "_" + timestamp

// Upload to cloud
GCS_Upload {
  bucket: "user-profiles",
  filePath: "photos/" + file_name,
  file: user_file
}

// Save URL to database
Update_User {
  photo_url: "photos/" + file_name
}
```

## Signed URLs

Temporary secure access to private files:

```javascript
// Generate temporary link
signed_url = S3_Signed_URL {
  bucket: "private-docs",
  file_key: "contracts/agreement.pdf",
  ttl: 7200  // 2 hours
}

// Send to user
Send_Email {
  to: user.email,
  subject: "Your document",
  body: "Access your file: " + signed_url
}
```

## File Management Patterns

### Multi-Cloud Backup

```javascript
// Upload to multiple clouds
file = Input.important_file

// Primary storage
S3_Upload(file)

// Backup storage
GCS_Upload(file)

// Disaster recovery
Azure_Upload(file)
```

### CDN Distribution

```javascript
// Upload to origin
S3_Upload {
  bucket: "cdn-origin",
  file: image,
  file_key: "images/" + hash
}

// Generate CDN URL
cdn_url = "https://cdn.domain.com/images/" + hash
```

## Search Implementation

### Product Search

```javascript
// User search query
search_term = Input.query

// Elasticsearch query
results = Elasticsearch_Query {
  query: {
    multi_match: {
      query: search_term,
      fields: ["title", "description", "tags"]
    }
  },
  size: 50
}

return results.hits
```

### Faceted Search

```javascript
// Category filters
filters = []
if (Input.category) {
  filters.push({term: {category: Input.category}})
}
if (Input.price_max) {
  filters.push({range: {price: {lte: Input.price_max}}})
}

// Execute search
Elasticsearch_Query {
  query: {bool: {must: filters}},
  aggregations: {
    categories: {terms: {field: "category"}},
    price_ranges: {histogram: {field: "price"}}
  }
}
```

## Best Practices

### Security
- Never expose credentials
- Use environment variables
- Implement access controls
- Rotate keys regularly

### Performance
- Use appropriate regions
- Implement caching
- Batch operations
- Monitor usage

### Cost Management
- Set lifecycle policies
- Delete unused files
- Monitor storage costs
- Use appropriate storage classes

## Try This

Create a file management system:
1. Accept file upload
2. Validate file type/size
3. Upload to cloud storage
4. Generate signed URL
5. Save metadata to database

## Pro Tips

💡 **Use Environment Variables:** Never hardcode credentials

💡 **Regional Storage:** Choose regions close to users

💡 **Lifecycle Rules:** Auto-delete old files to save costs

💡 **Index Strategy:** Plan Elasticsearch mappings carefully

💡 **Backup Important:** Always have redundancy for critical files

## Common Patterns

### Image Processing Pipeline
```javascript
1. Upload original to S3
2. Generate thumbnails
3. Store variants
4. Update database
5. Purge CDN cache
```

### Document Management
```javascript
1. Upload to private bucket
2. Generate signed URLs
3. Track access logs
4. Implement versioning
5. Archive old versions
```

## Next Steps

1. Choose your cloud provider
2. Set up credentials
3. Test basic operations
4. Implement file uploads
5. Add search if needed

Remember: Cloud services give you enterprise infrastructure without the complexity!