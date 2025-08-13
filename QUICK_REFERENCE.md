# Xano Quick Reference

## Common Patterns

### Database Operations

#### Add Record
```javascript
// Add a new record to a table
xano.database.add_record({
  table: 'users',
  data: {
    name: 'John Doe',
    email: 'john@example.com'
  }
})
```

#### Query Records
```javascript
// Query with filters
xano.database.query_all_records({
  table: 'users',
  filters: [
    {field: 'status', operator: '=', value: 'active'}
  ],
  sort: {field: 'created_at', order: 'desc'},
  limit: 10
})
```

#### Update Record
```javascript
// Update existing record
xano.database.edit_record({
  table: 'users',
  id: 123,
  data: {
    status: 'inactive'
  }
})
```

### API Endpoints

#### Create REST Endpoint
```javascript
// Define GET endpoint
xano.api.create({
  method: 'GET',
  path: '/users/{id}',
  function_stack: [
    'validate_input',
    'get_user',
    'format_response'
  ]
})
```

### Functions

#### Custom Function
```javascript
// Define custom function
xano.function.create({
  name: 'calculate_total',
  inputs: ['items', 'tax_rate'],
  logic: function(items, tax_rate) {
    let subtotal = items.reduce((sum, item) => sum + item.price, 0);
    return subtotal * (1 + tax_rate);
  }
})
```

## Expression Syntax

- Variables: `{variable_name}`
- Conditionals: `{if condition then value1 else value2}`
- Math: `{value1 + value2}`, `{value1 * value2}`
- String: `{concat(str1, str2)}`, `{upper(text)}`
- Date: `{now()}`, `{date_add(date, 1, 'days')}`

## Filter Operators

- `=` : Equals
- `!=` : Not equals
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal
- `<=` : Less than or equal
- `contains` : String contains
- `starts_with` : String starts with
- `ends_with` : String ends with
- `in` : Value in array
- `not_in` : Value not in array
- `is_null` : Is null
- `is_not_null` : Is not null

## Authentication

### Basic Auth Setup
```javascript
xano.auth.setup({
  table: 'users',
  username_field: 'email',
  password_field: 'password',
  hash_method: 'bcrypt',
  token_expiry: 3600
})
```

## Webhooks

### Incoming Webhook
```javascript
xano.webhook.create({
  name: 'payment_received',
  method: 'POST',
  authentication: 'bearer_token',
  function_stack: ['validate_webhook', 'process_payment']
})
```

## Background Tasks

### Schedule Task
```javascript
xano.task.schedule({
  name: 'daily_cleanup',
  cron: '0 0 * * *',  // Daily at midnight
  function: 'cleanup_old_records'
})
```
