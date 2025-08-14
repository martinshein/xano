---
title: "Security Functions and UUID Generation in Xano"
description: "Generate unique identifiers, create secure tokens, and implement encryption in your Xano applications"
category: function-stack
subcategory: security
has_code_examples: true
last_updated: '2025-01-23'
tags:
- uuid
- security
- authentication
- encryption
- tokens
---

# Security Functions and UUID Generation in Xano

## Quick Summary

> **What it is:** A comprehensive suite of security functions for generating unique IDs, creating authentication tokens, managing passwords, and encrypting sensitive data
> 
> **When to use:** Whenever you need unique identifiers, secure authentication, password management, or data encryption
> 
> **Key benefit:** Built-in security best practices without needing cryptography expertise
> 
> **Most used:** UUID generation for unique record IDs and authentication token creation

## What You'll Learn

- Generating universally unique identifiers (UUIDs)
- Creating and managing authentication tokens
- Password generation and validation
- Encrypting and decrypting sensitive data
- Understanding JWS vs JWE tokens
- Best practices for n8n and WeWeb integrations

## UUID Generation

### What is a UUID?

A UUID (Universally Unique Identifier) is like a digital fingerprint - a string that's guaranteed to be unique across all systems and time. Xano generates version 4 UUIDs that look like: `9bcc06a9-9782-4859-a69f-778a7f28d666`

### When to Use UUIDs

**Perfect for:**
- Primary keys in distributed systems
- Public-facing record IDs (hide sequential patterns)
- Temporary session identifiers
- File upload references
- API request tracking

**Example Use Cases:**
```javascript
// Order ID visible to customers
order_uuid: "a4f7b2c9-8e3d-4a1b-9c7e-2d8f6e9a3b5c"

// Instead of sequential IDs that reveal business metrics
// Bad: order_id: 12345 (reveals you've had 12,345 orders)
// Good: order_uuid (reveals nothing about your business)
```

## Authentication Token Management

### Create Authentication Token

Generate secure tokens for user sessions with built-in expiration.

**Configuration:**
- **Database Table:** Select your users table (must have auth enabled)
- **User ID:** The user's record ID
- **Extras:** Additional data to store in token (e.g., user role, permissions)
- **Expiration:** Token lifetime in seconds

**Example for n8n/WeWeb:**
```javascript
// Create a 24-hour session token
Table: users
ID: user.id
Extras: {
  role: "admin",
  subscription: "pro",
  workspace_id: 123
}
Expiration: 86400 // 24 hours
```

### Token Best Practices

1. **Short-lived tokens for sensitive operations**
   - Payment processing: 5 minutes (300 seconds)
   - Admin actions: 1 hour (3600 seconds)

2. **Longer tokens for general use**
   - User sessions: 24 hours to 7 days
   - API access: 30-90 days with refresh

3. **Store extras wisely**
   - Include role/permissions for quick access
   - Avoid sensitive data (use IDs, fetch details later)

## Password Management

### Generate Password

Create secure passwords with customizable requirements.

**Configuration Options:**
```javascript
{
  character_count: 16,        // Length
  require_lowercase: true,     // a-z
  require_uppercase: true,     // A-Z
  require_digit: true,        // 0-9
  require_symbol: true,       // !@#$%
  symbol_whitelist: "!@#$"   // Allowed symbols
}
```

### Validate Password

Check if a plain text password matches a hashed version.

**Use case:** User login verification
```javascript
Input: user_entered_password
Hashed: stored_password_hash
Returns: true/false
```

**Pro Tip:** Never store plain text passwords! Always hash them before storage.

## Encryption and Decryption

### Basic Encryption

Protect sensitive data with military-grade encryption.

**Setup:**
```javascript
Data: "sensitive information"
Algorithm: "aes-256-gcm" // Most secure
Key: environment.ENCRYPTION_KEY
IV: environment.ENCRYPTION_IV // 12 chars for GCM
```

**Important:** Store keys and IVs in environment variables, never in code!

### When to Encrypt

**Always encrypt:**
- Social Security Numbers
- Credit card details
- API keys and secrets
- Personal health information
- Private messages

**Don't encrypt:**
- Data you need to search/filter
- Public information
- Already hashed passwords

## JWS vs JWE Tokens

### JWS (JSON Web Signature)
- **Visible but tamper-proof**
- Data can be read but not modified
- Good for: Public claims, user info

### JWE (JSON Web Encryption)
- **Encrypted and tamper-proof**
- Data is completely hidden
- Good for: Sensitive data, private claims

**Example Comparison:**
```javascript
// JWS - Readable at jwt.io
{
  "user_id": 123,
  "role": "admin"
}

// JWE - Completely encrypted
"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0..."
```

## Random Number Generation

Generate cryptographically secure random numbers for:
- OTP codes
- Lottery systems
- Random sampling
- Game mechanics

**Configuration:**
```javascript
Min: 100000  // 6-digit OTP
Max: 999999
```

## Integration Examples

### With n8n

**Secure Webhook Authentication:**
```javascript
1. Generate UUID for webhook ID
2. Create auth token with webhook permissions
3. Validate token on each request
4. Expire after single use for sensitive operations
```

### With WeWeb

**User Session Management:**
```javascript
// Login flow
1. Validate password
2. Create auth token with user extras
3. Store token in WeWeb auth plugin
4. Include token in all API requests
```

## Common Mistakes to Avoid

1. **Using predictable IDs**
   - Always use UUIDs for public-facing IDs
   - Keep sequential IDs internal only

2. **Storing sensitive data in tokens**
   - Tokens are often logged/cached
   - Store IDs, fetch sensitive data separately

3. **Reusing encryption keys**
   - Use different keys for different data types
   - Rotate keys periodically

4. **Long token expiration for sensitive ops**
   - Payment tokens: minutes not days
   - Admin actions: hours not weeks

## Try This

Create a secure document sharing system:
1. Generate UUID for document ID
2. Encrypt document content
3. Create time-limited access token
4. Validate token and decrypt on access
5. Log all access attempts

## Pro Tips

💡 **Environment Variables:** Always store keys, IVs, and secrets in environment variables

💡 **Token Extras:** Include just enough data to avoid database lookups, but not sensitive info

💡 **UUID Format:** Use UUIDs in URLs - they're URL-safe and reveal nothing about your data

💡 **Encryption Algorithm:** Use AES-256-GCM for best security/performance balance

## Security Checklist

✅ Never log passwords or tokens
✅ Use HTTPS for all API calls
✅ Implement rate limiting on auth endpoints
✅ Monitor failed authentication attempts
✅ Rotate encryption keys periodically
✅ Test token expiration handling

Remember: Security is not optional. Use these functions to protect your users' data and maintain trust!