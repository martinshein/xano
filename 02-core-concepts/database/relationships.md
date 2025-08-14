---
title: "Database Relationships - Connect Your Data Like Building Blocks"
description: "Master database relationships in Xano to link tables together. Learn one-to-one, one-to-many, and many-to-many relationships with practical examples for n8n and WeWeb."
category: database
subcategory: fundamentals
tags:
  - Relationships
  - Table Reference
  - Foreign Keys
  - Data Modeling
  - One-to-Many
  - Many-to-Many
  - Database Design
difficulty: intermediate
reading_time: 12 minutes
last_updated: '2025-01-23'
prerequisites:
  - Understanding of database tables
  - Basic field types knowledge
  - At least 2 tables created
---

# Database Relationships - Connect Your Data Like Building Blocks

## 📋 **Quick Summary**

**What it does:** Database relationships link information between different tables, like connecting a customer to their orders or a student to their classes, preventing data duplication and enabling powerful queries.

**Why it matters:** Relationships enable you to:
- Store data once, use it everywhere
- Maintain data consistency automatically
- Build complex apps with simple structures
- Create powerful API endpoints for n8n/WeWeb
- Scale without duplicating information

**Time to implement:** 5 minutes per relationship

---

## What You'll Learn

- Understanding the three types of relationships
- Creating relationships with Table Reference fields
- Building relationship-based APIs
- Optimizing for n8n and WeWeb
- Common relationship patterns
- Troubleshooting relationship issues

## Understanding Database Relationships

### 🔗 **What Are Relationships?**

Think of relationships like connecting LEGO blocks:

**Without Relationships (Messy):**
```
Orders Table:
├── Order #1001
│   ├── Customer Name: John Doe
│   ├── Customer Email: john@example.com
│   ├── Customer Phone: 555-0100
│   └── Product: Widget
├── Order #1002
│   ├── Customer Name: John Doe (duplicated!)
│   ├── Customer Email: john@example.com (duplicated!)
│   ├── Customer Phone: 555-0100 (duplicated!)
│   └── Product: Gadget
```

**With Relationships (Clean):**
```
Customers Table:
├── Customer #42
    ├── Name: John Doe
    ├── Email: john@example.com
    └── Phone: 555-0100

Orders Table:
├── Order #1001
│   ├── Customer ID: 42 (links to customer)
│   └── Product: Widget
├── Order #1002
    ├── Customer ID: 42 (same link!)
    └── Product: Gadget
```

### 🔑 **Key Concepts**

**Primary Key:**
- The unique identifier for each record
- Usually the `id` field
- Like a social security number - unique to each record

**Foreign Key:**
- A field that references another table's primary key
- Creates the actual relationship
- Like a shipping label with a customer number

## Types of Relationships

### 1️⃣ **One-to-One (1:1)**

Each record in Table A relates to exactly one record in Table B.

**Real-world examples:**
```yaml
Person ←→ Passport:
- Each person has one passport
- Each passport belongs to one person

User ←→ Profile:
- Each user has one profile
- Each profile belongs to one user

Employee ←→ Desk:
- Each employee has one desk
- Each desk is assigned to one employee
```

**When to use:**
- Separating sensitive data (user credentials vs. profile)
- Optional extended information
- Performance optimization (rarely accessed data)

### 2️⃣ **One-to-Many (1:N)**

One record in Table A relates to multiple records in Table B.

**Real-world examples:**
```yaml
Customer → Orders:
- One customer can have many orders
- Each order belongs to one customer

Author → Books:
- One author can write many books
- Each book has one primary author

Category → Products:
- One category contains many products
- Each product belongs to one category
```

**When to use:**
- Parent-child relationships
- Ownership scenarios
- Hierarchical data structures

### 3️⃣ **Many-to-Many (M:N)**

Multiple records in Table A relate to multiple records in Table B.

**Real-world examples:**
```yaml
Students ←→ Courses:
- Students take multiple courses
- Courses have multiple students
- Requires junction table: Enrollments

Products ←→ Tags:
- Products have multiple tags
- Tags apply to multiple products
- Requires junction table: ProductTags

Users ←→ Roles:
- Users can have multiple roles
- Roles can belong to multiple users
- Requires junction table: UserRoles
```

**When to use:**
- Complex many-sided relationships
- Tagging systems
- Permission systems
- Subscription models

## Creating Relationships in Xano

### 🛠️ **Step 1: Add Table Reference Field**

1. **Open your table** (e.g., Orders)
2. **Click "Add Field"**
3. **Select "Table Reference"**
4. **Configure:**
   ```yaml
   Field Name: customer_id
   Reference Table: customers
   Display Field: email (what shows in UI)
   Required: Yes
   ```

### 🎯 **Step 2: Configure Auto-Complete**

Make referenced data display nicely:

1. **Go to referenced table** (customers)
2. **Click ⋮ → Auto-Complete**
3. **Customize display:**
   ```yaml
   Columns to show:
   - name
   - email
   - status
   Format: "John Doe (john@example.com)"
   ```

### 🔄 **Step 3: Use in API Endpoints**

Access related data in your functions:

```javascript
// Get Order with Customer Details
1. Get Record: order_id
2. Addon: customer_id
   - Type: Single Record
   - Table: customers
   - Output: customer_details

// Result includes:
{
  order_id: 1001,
  product: "Widget",
  customer_details: {
    name: "John Doe",
    email: "john@example.com"
  }
}
```

## Implementing Common Patterns

### 🛒 **E-Commerce Pattern**

```yaml
Tables Structure:
customers (1) → orders (N)
orders (1) → order_items (N)
order_items (N) ← products (1)
products (N) ← categories (1)

Implementation:
1. Customer places order
2. Order contains multiple items
3. Each item references a product
4. Products belong to categories
```

### 👥 **User Management Pattern**

```yaml
Tables Structure:
users (N) ← user_roles (junction) → roles (N)
users (1) → sessions (N)
users (1) → notifications (N)

Implementation:
1. Users assigned multiple roles
2. Roles define permissions
3. Sessions track logins
4. Notifications per user
```

### 📝 **Content Management Pattern**

```yaml
Tables Structure:
authors (1) → posts (N)
posts (N) ← post_tags (junction) → tags (N)
posts (1) → comments (N)
users (1) → comments (N)

Implementation:
1. Authors create posts
2. Posts tagged with multiple tags
3. Users comment on posts
4. Track comment authors
```

## Junction Tables for Many-to-Many

### 🌉 **Creating Junction Tables**

For Students ←→ Courses relationship:

**1. Create Junction Table:**
```yaml
Table: enrollments
Fields:
- id (primary key)
- student_id (table reference → students)
- course_id (table reference → courses)
- enrolled_date (timestamp)
- grade (text, optional)
- status (enum: enrolled, completed, dropped)
```

**2. Query Enrolled Students:**
```javascript
// API: Get all students in a course
1. Query All Records: enrollments
   - Filter: course_id = {input.course_id}
2. Addon Loop: student_id
   - Get full student details

// Returns array of enrolled students
```

**3. Query Student's Courses:**
```javascript
// API: Get all courses for a student
1. Query All Records: enrollments
   - Filter: student_id = {input.student_id}
2. Addon Loop: course_id
   - Get full course details

// Returns array of enrolled courses
```

## Integration Best Practices

### 🔧 **n8n Workflows**

Leverage relationships in automation:

```javascript
// n8n: Process order with customer notification
1. Webhook receives order_id
2. Xano node: Get order with customer addon
3. Email node: Send to customer.email
4. Xano node: Update customer.last_order_date

// Single API call gets all related data!
```

### 🌐 **WeWeb Collections**

Display related data efficiently:

```yaml
Collection Setup:
1. Create "Orders" collection
2. Enable customer addon
3. Display in repeater:
   - Order ID
   - Product Name
   - Customer Name (from addon)
   - Customer Email (from addon)

No separate API calls needed!
```

## Relationship Views

### 📊 **Visualizing Relationships**

Use Xano's relationship viewer:

1. **Database → Show Table Relationships**
2. **Drag tables** to organize
3. **See connections** between tables
4. **Identify missing** relationships

**Visual indicators:**
```
customers ──1──→ orders (one-to-many)
students ←──N──→ courses (many-to-many via junction)
users ──1──→ profiles (one-to-one)
```

## Performance Optimization

### ⚡ **Best Practices**

1. **Index foreign keys:**
   ```yaml
   Always index:
   - customer_id in orders
   - user_id in sessions
   - Any frequently joined field
   ```

2. **Limit addon depth:**
   ```yaml
   Good: Order → Customer
   OK: Order → Customer → Address
   Bad: Order → Customer → Address → City → Country
   ```

3. **Use selective addons:**
   ```javascript
   // Only get what you need
   Addon: customer_id
   Fields: name, email (not entire record)
   ```

## Common Mistakes to Avoid

### ❌ **Mistake 1: Circular References**

```yaml
Wrong:
users → companies → users → companies...

Right:
users → companies (one direction)
companies → owner_id (separate reference)
```

### ❌ **Mistake 2: Missing Junction Tables**

```yaml
Wrong:
products.tags = "electronics,sale,featured"

Right:
product_tags junction table with:
- product_id
- tag_id
```

### ❌ **Mistake 3: Over-Nesting Addons**

```yaml
Wrong:
Order → Customer → Address → City → State → Country

Right:
Order → Customer (with essential fields)
Separate API call for full address when needed
```

## Try This: Build a Blog System

### 📝 **Exercise: Create Blog Relationships**

Build these tables and relationships:

**1. Authors Table:**
```yaml
Fields:
- id
- name
- email
- bio
```

**2. Posts Table:**
```yaml
Fields:
- id
- title
- content
- author_id (reference → authors)
- published_at
```

**3. Categories Table:**
```yaml
Fields:
- id
- name
- slug
```

**4. Post_Categories Junction:**
```yaml
Fields:
- id
- post_id (reference → posts)
- category_id (reference → categories)
```

**5. Test API:**
- Get all posts by author
- Get all posts in category
- Get post with author details

## Troubleshooting

### 🔍 **"Can't create relationship"**
- Check both tables exist
- Verify correct field type (Table Reference)
- Ensure referenced table has records

### 🔍 **"Addon not returning data"**
- Verify relationship field has value
- Check addon configuration
- Test with known good record

### 🔍 **"Slow queries with relationships"**
- Add indexes on foreign keys
- Limit addon fields
- Consider caching strategy

## Best Practices Summary

### ✅ **Do's**

1. **Plan relationships** before creating tables
2. **Use meaningful** foreign key names
3. **Index all** foreign key fields
4. **Create junction tables** for many-to-many
5. **Test relationships** with sample data
6. **Document** your relationship structure

### ❌ **Don'ts**

1. **Don't duplicate** data across tables
2. **Don't use** comma-separated values for relationships
3. **Don't create** circular references
4. **Don't over-nest** addons
5. **Don't forget** to index foreign keys
6. **Don't skip** junction tables for many-to-many

## Next Steps

After mastering relationships:

1. **Design your complete** database schema
2. **Create all necessary** junction tables
3. **Build API endpoints** with addons
4. **Test with n8n** workflows
5. **Display in WeWeb** with collections
6. **Optimize with indexes** for performance

## Related Documentation

- [Field Types](./field-types.md)
- [Database Design](./designing-your-database.md)
- [Indexing](./indexing.md)
- [Query All Records](../function-stack/query-all-records.md)
- [Database Views](./database-views.md)