---
title: "Data Manipulation Functions"
description: "Transform, filter, and manipulate data within your Xano function stacks using powerful data manipulation tools"
category: function-stack
difficulty: intermediate
tags:
  - data-manipulation
  - transformation
  - filters
  - arrays
  - objects
related_docs:
  - arrays
  - objects
  - loops
  - conditional
last_updated: '2025-01-23'
---

# Data Manipulation Functions

## Quick Summary
Data manipulation functions in Xano allow you to transform, filter, sort, and restructure data as it flows through your function stacks. These tools are essential for preparing data for APIs, processing user inputs, and formatting responses.

## What You'll Learn
- Core data manipulation techniques in Xano
- Working with arrays and objects
- Filtering and sorting data
- Complex data transformations for n8n and WeWeb

## Core Manipulation Functions

### Array Operations
- **Filter** - Remove unwanted items based on conditions
- **Map** - Transform each item in an array
- **Sort** - Order array items by specific criteria
- **Group By** - Organize data into grouped collections
- **Unique** - Remove duplicate items

### Object Operations
- **Pick** - Select specific fields from objects
- **Omit** - Remove specific fields from objects
- **Merge** - Combine multiple objects
- **Transform** - Restructure object properties

## Try This: Basic Data Transformation

Transform user data for API consumption:
1. Filter active users only
2. Select required fields (name, email, role)
3. Sort by registration date
4. Format for frontend display

This gives you clean, structured data perfect for n8n workflows and WeWeb components.

## Integration Patterns

### For n8n
Use manipulation functions to prepare data before sending to n8n webhooks, ensuring the data format matches your automation requirements.

### For WeWeb
Transform database responses into the exact structure your WeWeb components expect, reducing frontend processing overhead.

## Common Use Cases
- **API Response Formatting** - Structure data for consistent API responses
- **Data Cleaning** - Remove invalid or incomplete records
- **Report Generation** - Aggregate and summarize data
- **User Interface Preparation** - Format data for dropdown menus and forms

Data manipulation functions are the foundation of clean, efficient data processing in your Xano backends.