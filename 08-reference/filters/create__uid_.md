---
title: Security and Cryptographic Filters Reference - Complete Guide for No-Code Development
description: Master Xano's security filters including UUID generation, encryption/decryption, hashing (MD5, SHA), HMAC, JWE tokens, and secure ID encoding for robust data protection in n8n, WeWeb, and Make.com integrations
category: 08-reference
subcategory: filters
difficulty: advanced
last_updated: '2025-01-16'
related_docs:
  - authentication-guide.md
  - security-best-practices.md
  - encryption-overview.md
tags:
  - security-filters
  - cryptography
  - encryption
  - hashing
  - uuid
  - hmac
  - jwe-tokens
  - secure-id
---

## 📋 **Quick Summary**

Master Xano's comprehensive security and cryptographic filter library for robust data protection. This reference covers UUID generation, encryption/decryption, hashing algorithms, HMAC signatures, JWE tokens, and secure ID encoding essential for building secure applications with n8n, WeWeb, and Make.com integrations.

## What You'll Learn

- Complete security filter reference with practical examples
- UUID generation and unique identifier creation
- Encryption and decryption techniques
- Hashing algorithms (MD5, SHA family)
- HMAC authentication and message integrity
- JWE token creation and validation
- Secure ID encoding for database protection
- Security best practices and integration patterns

# Security and Cryptographic Filters Reference

## 🔐 **Unique Identifier Generation**

### create_uid

**Purpose**: Returns a unique 64-bit unsigned integer value seeded from the input value.

**How It Works**: Generates a deterministic unique identifier based on the input seed. The same input will always produce the same UID, making it perfect for creating consistent, reproducible unique identifiers.

**Examples:**

**Basic UID Generation:**
```javascript
// Input
parent_value: "user_john_doe"

// Output
1234567890123456789  // 64-bit unsigned integer

// Same input always produces same UID
parent_value: "user_john_doe"
// Output: 1234567890123456789 (consistent)
```

**Use Cases and Patterns:**

**User ID Generation:**
```javascript
// Create consistent user IDs from email addresses
const userEmail = "john.doe@example.com";
const userId = userEmail.create_uid();
// Result: Unique 64-bit ID that's always the same for this email

// n8n: Generate consistent IDs for external systems
const externalUserId = `${externalSystem}_${userData.email}`.create_uid();
```

**Database Sharding:**
```javascript
// WeWeb: Determine which database shard to use
const userEmail = "user@example.com";
const shardId = userEmail.create_uid() % 8; // Distribute across 8 shards
const targetDatabase = `user_shard_${shardId}`;
```

**Cache Key Generation:**
```javascript
// Make.com: Create consistent cache keys
const cacheKey = `${endpoint}_${params.user_id}_${params.filter}`.create_uid();
const cacheKeyString = `cache_${cacheKey}`;
```

**Session ID Creation:**
```javascript
// Generate session identifiers
const sessionSeed = `${userId}_${timestamp}_${clientIP}`;
const sessionId = sessionSeed.create_uid();
```

## 🛡️ **Encryption and Decryption**

### encrypt

**Purpose**: Encrypts a value and returns the result in binary form.

**Security Note**: This provides symmetric encryption. The same key is used for both encryption and decryption.

**Examples:**

**Basic Encryption:**
```javascript
// Input
parent_value: "sensitive data"
encryption_key: "your-secret-key-here"

// Output
[Binary encrypted data]
```

### decrypt

**Purpose**: Decrypts an encrypted value and returns the original result.

**Examples:**

**Basic Decryption:**
```javascript
// Input
parent_value: [Binary encrypted data]
decryption_key: "your-secret-key-here"

// Output
"sensitive data"
```

**🔗 Real-World Security Patterns:**

**Secure Data Storage:**
```javascript
// n8n: Encrypt sensitive user data before storage
const sensitiveData = {
  ssn: "123-45-6789",
  credit_card: "4111-1111-1111-1111",
  bank_account: "9876543210"
};

const encryptionKey = process.env.ENCRYPTION_KEY;
const encryptedData = JSON.stringify(sensitiveData).encrypt(encryptionKey);

// Store encryptedData in database
// To retrieve: encryptedData.decrypt(encryptionKey).json_decode()
```

**API Token Protection:**
```javascript
// WeWeb: Secure API token storage
const apiToken = "sk_live_abcd1234efgh5678";
const userSpecificKey = `${userId}_${appSecret}`;
const encryptedToken = apiToken.encrypt(userSpecificKey);

// Store encryptedToken in user preferences
// Decrypt when needed: encryptedToken.decrypt(userSpecificKey)
```

**Configuration Security:**
```javascript
// Make.com: Encrypt configuration data
const configData = {
  database_url: "postgresql://user:pass@host:5432/db",
  api_keys: {
    stripe: "sk_live_...",
    sendgrid: "SG...."
  }
};

const masterKey = process.env.MASTER_ENCRYPTION_KEY;
const encryptedConfig = JSON.stringify(configData).encrypt(masterKey);
```

## 🔑 **Hashing Algorithms**

### md5

**Purpose**: Returns an MD5 hash representation of the value. Optional salt for additional security.

**Security Warning**: MD5 is cryptographically broken and should not be used for security-critical applications. Use SHA-256 or higher for security purposes.

**Examples:**
```javascript
// Basic MD5 hash
parent_value: "password123"

// Output
"482c811da5d5b4bc6d497ffa98491e38"

// MD5 with salt
parent_value: "password123"
salt: "random_salt_value"

// Output
"different_hash_due_to_salt"
```

### sha1

**Purpose**: Returns a SHA-1 hash representation of the value.

**Security Note**: SHA-1 is deprecated for security applications. Use SHA-256 or higher.

**Examples:**
```javascript
// Basic SHA-1
parent_value: "data to hash"

// Output
"2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"
```

### sha256 / sha384 / sha512

**Purpose**: Returns SHA-256/384/512 hash representation (recommended for security).

**Examples:**

**SHA-256 (Recommended):**
```javascript
// Input
parent_value: "secure data"
salt: "unique_salt_2025"

// Output
"a1b2c3d4e5f6789012345678901234567890abcdef123456789abcdef0123456"
```

**🔗 Secure Hashing Patterns:**

**Password Hashing:**
```javascript
// n8n: Secure password storage
const password = userInput.password;
const salt = generateRandomSalt(); // Generate unique salt per user
const hashedPassword = `${password}${salt}`.sha256();

// Store both hashedPassword and salt
const userRecord = {
  email: userInput.email,
  password_hash: hashedPassword,
  salt: salt
};
```

**Data Integrity Verification:**
```javascript
// WeWeb: Verify data hasn't been tampered with
const originalData = JSON.stringify(userData);
const dataHash = originalData.sha256();

// Store data and hash separately
// Later verification:
const currentHash = JSON.stringify(retrievedData).sha256();
const isDataIntact = currentHash.equals(storedHash);
```

**File Integrity Checking:**
```javascript
// Make.com: Verify uploaded file integrity
const fileContent = uploadedFile.content;
const fileHash = fileContent.sha256();
const expectedHash = metadata.expected_hash;

if (!fileHash.equals(expectedHash)) {
  throw new Error("File integrity check failed");
}
```

## 🔐 **HMAC Authentication**

### hmac_md5 / hmac_sha1 / hmac_sha256 / hmac_sha384 / hmac_sha512

**Purpose**: Returns HMAC signature using shared secret for message authentication and integrity.

**How HMAC Works**: Uses a cryptographic hash function combined with a secret key to provide both data integrity and authentication.

**Examples:**

**HMAC-SHA256 (Recommended):**
```javascript
// Input
parent_value: "message to authenticate"
secret_key: "shared-secret-key"

// Output
"hmac_signature_hash_here"
```

**🔗 HMAC Integration Patterns:**

**API Request Signing:**
```javascript
// n8n: Sign API requests for webhook security
const requestData = JSON.stringify(webhookPayload);
const timestamp = Date.now().toString();
const message = `${timestamp}.${requestData}`;
const signature = message.hmac_sha256(webhookSecret);

const headers = {
  'X-Timestamp': timestamp,
  'X-Signature': `sha256=${signature}`,
  'Content-Type': 'application/json'
};
```

**Webhook Verification:**
```javascript
// WeWeb: Verify incoming webhook signatures
const receivedSignature = request.headers['x-signature'];
const payload = request.body;
const expectedSignature = payload.hmac_sha256(webhookSecret);

if (!receivedSignature.equals(`sha256=${expectedSignature}`)) {
  throw new Error("Invalid webhook signature");
}
```

**Session Token Validation:**
```javascript
// Make.com: Create and validate secure session tokens
const sessionData = {
  user_id: userId,
  expires: expirationTime,
  permissions: userPermissions
};

const sessionString = JSON.stringify(sessionData);
const sessionSignature = sessionString.hmac_sha256(sessionSecret);
const sessionToken = `${sessionString.base64_encode()}.${sessionSignature}`;

// Validation
const [encodedData, signature] = sessionToken.split('.');
const expectedSignature = encodedData.base64_decode().hmac_sha256(sessionSecret);
const isValidSession = signature.equals(expectedSignature);
```

## 🎫 **JWE Token Management**

### jwe_encode

**Purpose**: Encodes data as a JWE (JSON Web Encryption) token.

**Parameters:**
- `headers`: Custom headers to include
- `key`: Encryption key
- `key_algorithm`: Key encryption algorithm
- `content_algorithm`: Content encryption algorithm  
- `ttl`: Token expiration time in seconds (0 = no expiration)

**Examples:**
```javascript
// Input
parent_value: {
  "user_id": 12345,
  "role": "admin",
  "permissions": ["read", "write", "delete"]
}

headers: {"typ": "JWT", "alg": "RSA-OAEP"}
key: "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"
key_algorithm: "RSA-OAEP"
content_algorithm: "A256GCM"
ttl: 3600  // 1 hour

// Output
"eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ..."
```

### jwe_decode

**Purpose**: Decodes a JWE token and returns the original payload.

**Examples:**
```javascript
// Input
parent_value: "eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ..."
key: "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"

// Output
{
  "user_id": 12345,
  "role": "admin", 
  "permissions": ["read", "write", "delete"]
}
```

**🔗 JWE Token Patterns:**

**Secure Session Management:**
```javascript
// n8n: Create encrypted user sessions
const sessionData = {
  user_id: userData.id,
  email: userData.email,
  role: userData.role,
  login_time: new Date().toISOString(),
  ip_address: clientIP
};

const sessionToken = sessionData.jwe_encode({
  key: process.env.SESSION_ENCRYPTION_KEY,
  key_algorithm: "dir",
  content_algorithm: "A256GCM",
  ttl: 86400 // 24 hours
});

// Return token to client
response.setHeader('Authorization', `Bearer ${sessionToken}`);
```

**Secure Data Transfer:**
```javascript
// WeWeb: Encrypt sensitive data for client storage
const sensitiveClientData = {
  user_preferences: userPrefs,
  cached_data: expensiveQueryResults,
  temporary_tokens: tempTokens
};

const encryptedData = sensitiveClientData.jwe_encode({
  key: clientSpecificKey,
  key_algorithm: "A256GCMKW",
  content_algorithm: "A256GCM",
  ttl: 1800 // 30 minutes
});

// Store in secure client storage
localStorage.setItem('encrypted_session', encryptedData);
```

**API Communication Security:**
```javascript
// Make.com: Secure API payload transmission
const apiPayload = {
  transaction_data: transactionInfo,
  user_context: userContext,
  sensitive_flags: securityFlags
};

const encryptedPayload = apiPayload.jwe_encode({
  key: apiSharedSecret,
  key_algorithm: "RSA-OAEP-256",
  content_algorithm: "A256GCM",
  ttl: 300 // 5 minutes for API calls
});
```

## 🔒 **Secure ID Encoding**

### secureid_encode

**Purpose**: Returns an encrypted version of an integer ID with optional salt.

**Use Case**: Prevents ID enumeration attacks by obscuring database primary keys.

**Examples:**
```javascript
// Input
parent_value: 12345  // Database ID
salt: "application_secret_salt"

// Output
"a1b2c3d4e5f6g7h8"  // Encoded secure ID
```

### secureid_decode

**Purpose**: Returns the original ID from the encoded version.

**Examples:**
```javascript
// Input
parent_value: "a1b2c3d4e5f6g7h8"  // Encoded ID
salt: "application_secret_salt"  // Same salt used for encoding

// Output
12345  // Original database ID
```

**🔗 Secure ID Patterns:**

**URL Security:**
```javascript
// n8n: Generate secure URLs with encoded IDs
const databaseId = record.id;
const secureId = databaseId.secureid_encode(urlSalt);
const publicUrl = `https://app.example.com/user/${secureId}`;

// Later decode for database lookup
const encodedId = urlParams.userId;
const actualId = encodedId.secureid_decode(urlSalt);
const userRecord = database.getUser(actualId);
```

**API Endpoint Protection:**
```javascript
// WeWeb: Secure API endpoint IDs
const internalUserId = 98765;
const publicUserId = internalUserId.secureid_encode(apiSalt);

// Public API response
{
  "user_id": publicUserId,  // "x1y2z3a4b5c6"
  "name": "John Doe",
  "email": "john@example.com"
}

// Internal processing
const receivedId = apiRequest.user_id;
const internalId = receivedId.secureid_decode(apiSalt);
```

**Database Security:**
```javascript
// Make.com: Secure database ID exposure
const orderIds = orders.map(order => ({
  secure_id: order.id.secureid_encode(orderSalt),
  order_details: order.details,
  public_info: order.public_data
}));

// When processing secure ID
const secureOrderId = request.order_id;
const actualOrderId = secureOrderId.secureid_decode(orderSalt);
const orderRecord = database.getOrder(actualOrderId);
```

## 🛡️ **Security Best Practices**

### Key Management

**Environment Variables:**
```javascript
// Store keys securely in environment variables
const encryptionKey = process.env.ENCRYPTION_KEY;
const hmacSecret = process.env.HMAC_SECRET;
const jweKey = process.env.JWE_ENCRYPTION_KEY;

// Never hardcode keys in your code
// ❌ DON'T DO THIS:
// const key = "hardcoded-secret-key";

// ✅ DO THIS:
const key = process.env.SECRET_KEY || (() => {
  throw new Error("SECRET_KEY environment variable required");
})();
```

**Key Rotation Strategy:**
```javascript
// Support multiple keys for rotation
const getCurrentKey = () => {
  return process.env.CURRENT_ENCRYPTION_KEY;
};

const getPreviousKeys = () => {
  return [
    process.env.ENCRYPTION_KEY_V1,
    process.env.ENCRYPTION_KEY_V2,
    process.env.ENCRYPTION_KEY_V3
  ].filter(Boolean);
};

// Encrypt with current key
const encryptData = (data) => {
  return data.encrypt(getCurrentKey());
};

// Decrypt trying multiple keys
const decryptData = (encryptedData) => {
  // Try current key first
  try {
    return encryptedData.decrypt(getCurrentKey());
  } catch (error) {
    // Try previous keys
    const previousKeys = getPreviousKeys();
    for (const key of previousKeys) {
      try {
        return encryptedData.decrypt(key);
      } catch (e) {
        continue;
      }
    }
    throw new Error("Unable to decrypt data with any available key");
  }
};
```

### Salt Generation

**Unique Salt Strategy:**
```javascript
// Generate unique salts per user/record
const generateUserSalt = (userId) => {
  return `${userId}_${process.env.MASTER_SALT}_${Date.now()}`;
};

const generateRecordSalt = (recordType, recordId) => {
  return `${recordType}_${recordId}_${process.env.MASTER_SALT}`;
};

// Usage
const userSalt = generateUserSalt(user.id);
const hashedPassword = `${password}${userSalt}`.sha256();
```

### Timing Attack Prevention

**Constant-Time Comparison:**
```javascript
// Prevent timing attacks in signature verification
const secureCompare = (signature1, signature2) => {
  if (signature1.length !== signature2.length) {
    return false;
  }
  
  let result = 0;
  for (let i = 0; i < signature1.length; i++) {
    result |= signature1.charCodeAt(i) ^ signature2.charCodeAt(i);
  }
  
  return result === 0;
};

// Use in signature verification
const isValidSignature = secureCompare(receivedSignature, expectedSignature);
```

## 🚨 **Security Considerations**

### Algorithm Selection

**Recommended Algorithms:**
```javascript
// ✅ RECOMMENDED for new applications
const secureHashing = {
  primary: "sha256",
  fallback: "sha512"
};

const secureHmac = {
  primary: "hmac_sha256",
  fallback: "hmac_sha512"
};

// ⚠️ DEPRECATED - avoid for security-critical applications
const deprecatedHashing = {
  avoid: ["md5", "sha1"],
  reason: "Cryptographically broken"
};
```

### Input Validation

**Secure Input Handling:**
```javascript
// Validate input before cryptographic operations
const validateEncryptionInput = (data) => {
  if (!data || typeof data !== 'string') {
    throw new Error("Invalid encryption input");
  }
  
  if (data.length > 1000000) { // 1MB limit
    throw new Error("Data too large for encryption");
  }
  
  return data;
};

const validateKey = (key) => {
  if (!key || key.length < 32) {
    throw new Error("Encryption key must be at least 32 characters");
  }
  
  return key;
};
```

### Error Handling

**Secure Error Messages:**
```javascript
// Don't leak sensitive information in errors
const secureDecrypt = (encryptedData, key) => {
  try {
    return encryptedData.decrypt(key);
  } catch (error) {
    // Don't expose specific decryption errors
    throw new Error("Decryption failed");
  }
};

const secureVerifySignature = (data, signature, secret) => {
  try {
    const expectedSignature = data.hmac_sha256(secret);
    return signature.equals(expectedSignature);
  } catch (error) {
    // Always return false for any error
    return false;
  }
};
```

## 🔗 **Integration Security Patterns**

### n8n Security Workflow

**Secure Data Processing:**
```javascript
// n8n Code node: Secure webhook processing
const incomingData = $input.all()[0].json;

// Verify HMAC signature
const receivedSignature = $node["Webhook"].json.headers['x-signature'];
const payloadString = JSON.stringify(incomingData);
const expectedSignature = payloadString.hmac_sha256(process.env.WEBHOOK_SECRET);

if (!receivedSignature.equals(`sha256=${expectedSignature}`)) {
  throw new Error("Invalid webhook signature");
}

// Encrypt sensitive data before storage
const sensitiveFields = ['ssn', 'credit_card', 'bank_account'];
const processedData = { ...incomingData };

sensitiveFields.forEach(field => {
  if (processedData[field]) {
    processedData[field] = processedData[field].encrypt(process.env.DATA_ENCRYPTION_KEY);
  }
});

return processedData;
```

### WeWeb Security Integration

**Client-Side Security:**
```javascript
// WeWeb: Secure client data handling
const secureStorage = {
  encrypt: (data) => {
    const key = wwLib.wwVariable.getValue('userEncryptionKey');
    return JSON.stringify(data).encrypt(key);
  },
  
  decrypt: (encryptedData) => {
    const key = wwLib.wwVariable.getValue('userEncryptionKey');
    return encryptedData.decrypt(key).json_decode();
  },
  
  generateSecureId: (id) => {
    const salt = wwLib.wwVariable.getValue('appSalt');
    return id.secureid_encode(salt);
  }
};

// Usage in WeWeb components
const encryptedUserData = secureStorage.encrypt(userData);
localStorage.setItem('secure_user_data', encryptedUserData);
```

### Make.com Security Scenarios

**Secure API Integration:**
```javascript
// Make.com: Secure external API calls
const createSecureApiRequest = (data) => {
  const timestamp = Date.now().toString();
  const nonce = Math.random().toString(36).substring(7);
  
  const signatureData = {
    timestamp: timestamp,
    nonce: nonce,
    data: data
  };
  
  const signatureString = JSON.stringify(signatureData);
  const signature = signatureString.hmac_sha256(process.env.API_SECRET);
  
  return {
    data: data,
    timestamp: timestamp,
    nonce: nonce,
    signature: signature
  };
};
```

---

**Next Steps**: Explore more filter types in [Text Processing Filters](text-filters.md) and [Mathematical Operations](math-filters.md) to complete your data processing toolkit.