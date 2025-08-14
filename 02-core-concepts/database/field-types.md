---
title: "Database Field Types - Complete Guide for No-Code Builders"
description: "Master Xano's database field types to build robust applications. Learn when to use each field type with practical examples for n8n, WeWeb, and Make integrations."
category: database
subcategory: core-concepts
tags:
  - Database
  - Field Types
  - Data Modeling
  - Schema Design
  - No-Code
  - Data Types
  - Best Practices
difficulty: beginner
reading_time: 10 minutes
last_updated: '2025-01-23'
prerequisites:
  - Basic understanding of databases
  - Access to Xano workspace
---

# Database Field Types - Complete Guide for No-Code Builders

## 📋 **Quick Summary**

**What it does:** Field types define what kind of data you can store in each column of your database tables - like choosing the right container for different items.

**Why it matters:** Choosing the right field type:
- Ensures data consistency and validation
- Optimizes database performance
- Prevents data entry errors
- Makes integrations with n8n and WeWeb smoother
- Reduces debugging time

**Time to implement:** 2-5 minutes per field when creating tables

---

## What You'll Learn

- All 16 field types available in Xano
- When to use each field type (with real examples)
- Common mistakes to avoid
- Integration tips for n8n and WeWeb
- Best practices for data modeling

## Understanding Field Types

Think of field types like kitchen containers - you wouldn't store soup in a colander or dry pasta in a liquid measuring cup. Each field type is designed for specific kinds of data.

### 💡 **What This Means for You**

- **No more data errors:** The right field type prevents incorrect data from entering your database
- **Better performance:** Proper field types make queries faster
- **Easier integrations:** n8n and WeWeb work better when data types match expectations
- **Less debugging:** Catch errors at data entry, not in production

## Complete Field Type Reference

### 📄 **Text Field**

**What it stores:** Any text data - names, descriptions, addresses, notes

**When to use:**
- User names and addresses
- Product descriptions
- Comments and feedback
- Any free-form text input

**Example values:**
```
"John Smith"
"123 Main Street, Chicago"
"This product is amazing!"
```

**🔧 n8n Tip:** Text fields map directly to String type in n8n workflows

**🌐 WeWeb Integration:** Use text inputs or textareas in WeWeb forms

**Common mistake:** Using text fields for numbers you need to calculate with

---

### 🔢 **Integer Field**

**What it stores:** Whole numbers without decimals

**When to use:**
- Quantities (inventory count)
- Ages
- User IDs
- Rating scores (1-5 stars)

**Example values:**
```
42
1000
-15
0
```

**Try This:** Use integers for anything you count but don't measure

**⚠️ Common Mistake:** Using integers for money (use Decimal instead)

---

### 🔢 **Decimal Field**

**What it stores:** Numbers with decimal points

**When to use:**
- Prices and monetary values
- Measurements (weight, distance)
- Percentages
- GPS coordinates

**Example values:**
```
19.99
3.14159
0.75
-123.45
```

**Best Practice:** Always use Decimal for money to avoid rounding errors

**🔧 n8n Tip:** When working with currency, multiply by 100 to work in cents, then divide for display

---

### ㊙️ **UUID Field**

**What it stores:** Universally Unique Identifiers - random strings that guarantee uniqueness

**When to use:**
- Primary keys for records
- API keys
- Session tokens
- Tracking codes

**Example values:**
```
"105c8b80-fd24-4cf3-bbed-a43e8134c8b0"
"984a0t12-rt12-5ey6-poqw-b12y1923e6l0"
```

**💡 Pro Tip:** Xano can auto-generate UUIDs for new records

---

### 🍱 **Object Field**

**What it stores:** Structured data with multiple properties - like a folder with labeled sections

**When to use:**
- User preferences settings
- Product specifications
- Address with multiple components
- Any grouped related data

**Example value:**
```json
{
  "street": "123 Main St",
  "city": "Chicago",
  "state": "IL",
  "zip": "60601"
}
```

**🌐 WeWeb Integration:** Perfect for form data that has multiple related fields

---

### ❓ **Table Reference Field**

**What it stores:** Links to records in other tables (or the same table)

**When to use:**
- User roles (linking users to roles table)
- Product categories
- Order items (linking to products)
- Parent-child relationships

**How it works:** Like a hyperlink in a document - it points to data stored elsewhere

**Best Practice:** Use references instead of duplicating data across tables

---

### 🤖 **Vector Field**

**What it stores:** Arrays of numbers used for AI/ML applications

**When to use:**
- AI-powered search (semantic search)
- Recommendation systems
- Image similarity matching
- Chatbot memory

**Example value:**
```
[-0.235, 0.458, -0.891, 0.023, 0.444, -0.657, ...]
```

**💡 For AI Builders:** Vectors store embeddings from OpenAI, Anthropic, or other AI models

---

### 🛑 **Enum Field**

**What it stores:** One value from a predefined list of options

**When to use:**
- Status fields (pending, approved, rejected)
- Subscription tiers (free, pro, enterprise)
- Shirt sizes (S, M, L, XL)
- Any field with limited, fixed options

**Example values:**
```
"pending"
"approved"
"rejected"
```

**🌐 WeWeb Tip:** Perfect for dropdown menus and radio buttons

---

### 🕕 **Timestamp Field**

**What it stores:** Exact date and time (stored as Unix epoch in milliseconds)

**When to use:**
- Created/updated dates
- Event scheduling
- Appointment times
- Any time-sensitive data

**Example:**
```
1733762528000 // Represents: Mon, 09 Dec 2024 16:42:08 GMT
```

**Best Practice:** Always use Timestamp over Date unless you specifically don't need time

---

### 📅 **Date Field**

**What it stores:** Calendar dates without time

**When to use:**
- Birthdays
- Anniversaries
- Holiday dates
- Any date where time doesn't matter

**Note:** Less flexible than Timestamp - only use when you definitely don't need time

---

### ✅ **Boolean Field**

**What it stores:** True or false values only

**When to use:**
- Feature flags (enabled/disabled)
- Subscription status (active/inactive)
- Checkboxes (checked/unchecked)
- Any yes/no decision

**Why not just use text?**
- Takes less storage space
- Prevents typos (e.g., "ture" instead of "true")
- Faster queries

---

### 📨 **Email Field**

**What it stores:** Email addresses with automatic validation

**When to use:**
- User registration
- Contact forms
- Newsletter subscriptions

**Benefit:** Automatically validates email format before saving

---

### 🔑 **Password Field**

**What it stores:** Encrypted passwords (never plain text)

**Security features:**
- Automatically encrypted on save
- Never visible in database view
- Cannot be retrieved in plain text
- Only encrypted version shown in queries

**When to use:** Only for user passwords - never for API keys or other secrets

---

### 💻 **JSON Field**

**What it stores:** Complex, nested data structures

**When to use:**
- Dynamic form data
- API responses
- Configuration settings
- Any data with varying structure

**Example:**
```json
{
  "recipe": {
    "name": "Chocolate Chip Cookies",
    "ingredients": ["flour", "sugar", "butter"],
    "steps": ["Mix", "Bake", "Cool"],
    "prepTime": 15
  }
}
```

---

### 🖼️ **Storage Field**

**What it stores:** File metadata (not the file itself)

**When to use:**
- Profile pictures
- Document uploads
- Product images
- Any file attachments

**What gets stored:**
```json
{
  "name": "profile.jpg",
  "size": 123456,
  "mime": "image/jpeg",
  "url": "https://your-domain.io/vault/profile.jpg"
}
```

---

### 🗺️ **Geography Field**

**What it stores:** Location data (points, paths, or polygons)

**Three types:**
1. **Point:** Single location (store, user location)
2. **Path:** Route or line (delivery route)
3. **Polygon:** Area (delivery zone, service area)

**When to use:**
- Store locations
- Delivery zones
- Route planning
- Geofencing

---

## Best Practices for Choosing Field Types

### 🎯 **Decision Guide**

Ask yourself these questions:

1. **Will I need to search or filter by this field?**
   - Yes → Use specific type (Integer, Boolean, Enum)
   - No → Text might be fine

2. **Will I perform calculations with this data?**
   - Yes → Use Integer or Decimal
   - No → Text is okay for display-only numbers

3. **Does this data have a fixed set of options?**
   - Yes → Use Enum
   - No → Use Text

4. **Am I storing money?**
   - Always use Decimal, never Integer or Text

5. **Do I need both date AND time?**
   - Yes → Use Timestamp
   - No → Use Date

### ⚠️ **Common Mistakes to Avoid**

1. **Using Text for everything**
   - Loses data validation
   - Makes queries slower
   - Causes integration issues

2. **Using Integer for money**
   - Loses decimal precision
   - Causes rounding errors

3. **Storing files in the database**
   - Use Storage field for metadata
   - Files go to file storage

4. **Using multiple fields for related data**
   - Use Object field instead
   - Keeps data organized

5. **Not using Table References**
   - Causes data duplication
   - Makes updates difficult

## Integration Examples

### 🔧 **n8n Workflow Example**

When receiving webhook data in n8n:
```javascript
// Map incoming data to correct Xano field types
{
  "name": String($json.name),
  "age": Number($json.age),
  "price": parseFloat($json.price),
  "is_active": Boolean($json.status === "active"),
  "preferences": JSON.parse($json.settings)
}
```

### 🌐 **WeWeb Form Mapping**

Match WeWeb inputs to Xano fields:
- Text Input → Text field
- Number Input → Integer/Decimal field
- Toggle → Boolean field
- Select Dropdown → Enum field
- Date Picker → Date/Timestamp field
- File Upload → Storage field

## Try This: Quick Field Type Exercise

Create a table for an e-commerce product:

1. **name** → Text (product name)
2. **price** → Decimal (selling price)
3. **quantity** → Integer (stock count)
4. **category_id** → Table Reference (to categories table)
5. **is_featured** → Boolean (featured product?)
6. **images** → Storage (product photos)
7. **specifications** → JSON (variable product specs)
8. **created_at** → Timestamp (when added)

## Next Steps

Now that you understand field types:
1. Review your existing tables for optimization opportunities
2. Plan your schema with the right field types from the start
3. Set up proper validation rules
4. Configure your n8n/WeWeb integrations to match

## Related Documentation

- [Database Design Best Practices](./designing-your-database.md)
- [Table Relationships](./relationships.md)
- [Data Import Guide](./csv-import-and-export.md)
- [Storage and Files](./storage.md)