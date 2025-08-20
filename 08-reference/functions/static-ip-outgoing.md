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
- Static IP
- Network
- Security
- Enterprise
- Infrastructure
title: 'Static IP (Outgoing) & Network Security'
---

# Static IP (Outgoing) & Network Security

## 📋 **Quick Summary**
Static IP (Outgoing) provides your Xano instance with a fixed IP address for all outbound requests, enabling secure integrations with enterprise services, banking APIs, and other systems that require IP whitelisting. Essential for production applications requiring strict network security compliance.

## 🎯 **Core Concepts**

### What is Static IP (Outgoing)?
Static IP (Outgoing) ensures all external API requests from your Xano instance originate from a fixed, predictable IP address. This enables integration with services that use IP-based access control and security policies.

### Key Benefits
- **Enterprise Integration**: Connect to corporate systems requiring IP whitelisting
- **Banking & Financial APIs**: Meet strict security requirements for financial services
- **Enhanced Security**: Provide additional layer of network-level security
- **Compliance**: Meet regulatory requirements for network traffic control
- **Reliable Integration**: Maintain consistent network identity across deployments

## 🛠️ **Configuration & Setup**

### Enabling Static IP

```javascript
// Instance configuration for static IP
{
  "instance_settings": {
    "network_configuration": {
      "static_ip_outgoing": {
        "enabled": true,
        "ip_address": "203.0.113.42", // Example IP - actual IP provided by Xano
        "status": "active",
        "region": "us-east-1"
      }
    }
  },
  "configuration_steps": [
    "Navigate to Instance Settings",
    "Select 'Static IP (Outgoing)' option",
    "Enable the feature",
    "Note the assigned IP address",
    "Configure external services with the IP"
  ]
}
```

### IP Address Information

```javascript
// Static IP details and management
{
  "ip_information": {
    "assigned_ip": "Your unique static IP address",
    "type": "IPv4",
    "persistence": "Remains constant across instance restarts",
    "scope": "All outbound HTTP/HTTPS requests",
    "geolocation": "Matches your instance region"
  },
  "management": {
    "viewing_ip": "Available in Instance Settings dashboard",
    "changes": "IP remains constant unless instance region changes",
    "monitoring": "Track usage in Instance Activity logs"
  }
}
```

## 🔐 **Security Implementation**

### Third-Party Service Whitelisting

```javascript
// Common integration scenarios requiring IP whitelisting
{
  "enterprise_apis": {
    "banking_systems": {
      "description": "Banks require IP whitelisting for API access",
      "example_services": ["Plaid", "Stripe Connect", "Banking APIs"],
      "security_requirements": [
        "Static IP address registration",
        "SSL/TLS certificate validation",
        "Request signing with API keys"
      ]
    },
    "corporate_systems": {
      "description": "Enterprise software with network restrictions",
      "example_services": ["Salesforce", "SAP", "Oracle", "Custom corporate APIs"],
      "implementation": "Add Xano static IP to corporate firewall rules"
    },
    "government_apis": {
      "description": "Government services with strict access controls",
      "example_services": ["Tax APIs", "Regulatory reporting", "Compliance systems"],
      "requirements": "IP registration with government IT departments"
    }
  }
}
```

### Firewall Configuration Examples

```javascript
// External service firewall configuration
{
  "firewall_rules": {
    "allow_inbound": {
      "source_ip": "203.0.113.42", // Your Xano static IP
      "protocol": "HTTPS",
      "port": 443,
      "description": "Xano instance API access"
    },
    "service_specific": {
      "banking_api": {
        "allowed_ips": ["203.0.113.42"],
        "allowed_methods": ["GET", "POST"],
        "rate_limits": "1000 requests/hour",
        "authentication": "API key + IP validation"
      },
      "corporate_crm": {
        "ip_whitelist": ["203.0.113.42"],
        "access_control": "IP + OAuth 2.0",
        "audit_logging": "All requests logged with source IP"
      }
    }
  }
}
```

## 🔗 **Integration Examples**

### Banking API Integration

```javascript
// Secure banking API integration with static IP
{
  "banking_integration": {
    "api_endpoint": "https://secure-bank-api.com/v1/accounts",
    "security_requirements": [
      "Static IP whitelisting",
      "TLS 1.2+ encryption",
      "API key authentication",
      "Request signing"
    ],
    "xano_implementation": {
      "function": "External API Request",
      "url": "https://secure-bank-api.com/v1/accounts/{{account_id}}/balance",
      "method": "GET",
      "headers": {
        "Authorization": "Bearer {{env.BANK_API_KEY}}",
        "X-Client-ID": "{{env.BANK_CLIENT_ID}}",
        "X-Request-Signature": "{{generate_hmac_signature}}",
        "Content-Type": "application/json"
      },
      "timeout": 30000,
      "ssl_verification": true
    },
    "error_handling": {
      "ip_blocked": {
        "status_code": 403,
        "message": "IP not whitelisted",
        "resolution": "Verify static IP configuration"
      },
      "api_limits": {
        "status_code": 429,
        "message": "Rate limit exceeded",
        "resolution": "Implement request queuing"
      }
    }
  }
}
```

### Corporate System Integration

```javascript
// Enterprise ERP system integration
{
  "erp_integration": {
    "system": "Enterprise Resource Planning",
    "connection_requirements": {
      "network_access": "Static IP whitelisting required",
      "authentication": "Active Directory integration",
      "encryption": "End-to-end SSL/TLS",
      "compliance": "SOX, GDPR compliance logging"
    },
    "implementation": [
      {
        "step": "Register Static IP",
        "action": "Submit IP address to IT security team",
        "documentation": "Provide Xano static IP for firewall configuration"
      },
      {
        "step": "Configure Authentication",
        "function": "External API Request",
        "url": "https://erp.company.com/api/auth/token",
        "method": "POST",
        "headers": {
          "Content-Type": "application/json",
          "X-Source-IP": "{{static_ip}}"
        },
        "body": {
          "client_id": "{{env.ERP_CLIENT_ID}}",
          "client_secret": "{{env.ERP_CLIENT_SECRET}}",
          "scope": "read:inventory write:orders"
        }
      },
      {
        "step": "Data Synchronization",
        "function": "Custom Function",
        "custom_function": "sync_erp_data",
        "parameters": {
          "auth_token": "{{access_token}}",
          "sync_type": "bidirectional"
        }
      }
    ]
  }
}
```

### Payment Processor Integration

```javascript
// Payment processor with enhanced security
{
  "payment_integration": {
    "processor": "Enterprise Payment Gateway",
    "security_model": {
      "ip_validation": "Static IP required for API access",
      "pci_compliance": "PCI DSS Level 1 certification required",
      "encryption": "AES-256 encryption for sensitive data"
    },
    "integration_workflow": [
      {
        "step": "Create Payment Session",
        "function": "External API Request",
        "url": "https://secure-payments.com/v2/sessions",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{env.PAYMENT_API_KEY}}",
          "X-Source-IP": "{{static_ip_address}}",
          "Content-Type": "application/json"
        },
        "body": {
          "amount": "{{order_total}}",
          "currency": "USD",
          "source_ip": "{{static_ip_address}}",
          "merchant_id": "{{env.MERCHANT_ID}}"
        },
        "ssl_verify": true,
        "timeout": 15000
      },
      {
        "step": "Process Payment",
        "function": "External API Request",
        "url": "https://secure-payments.com/v2/charges",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{env.PAYMENT_API_KEY}}",
          "Idempotency-Key": "{{payment_session_id}}"
        },
        "body": {
          "session_id": "{{payment_session_id}}",
          "confirm": true
        }
      }
    ]
  }
}
```

## 📊 **Monitoring & Compliance**

### Network Activity Monitoring

```javascript
// Monitoring outbound requests from static IP
{
  "monitoring_setup": {
    "request_logging": {
      "log_destination": "Instance Activity dashboard",
      "logged_data": [
        "Destination IP/domain",
        "Request method and headers", 
        "Response status codes",
        "Request/response sizes",
        "Timestamp and duration"
      ]
    },
    "security_monitoring": {
      "failed_requests": "Track authentication failures",
      "rate_limiting": "Monitor API rate limit hits",
      "ssl_errors": "Log SSL/TLS handshake failures",
      "ip_blocks": "Alert on IP-based access denials"
    },
    "compliance_reporting": {
      "audit_trail": "Complete request history for compliance audits",
      "data_export": "Export logs for security analysis",
      "retention_policy": "Configurable log retention periods"
    }
  }
}
```

### Performance Analytics

```javascript
// Static IP performance and reliability metrics
{
  "performance_metrics": {
    "network_latency": {
      "measurement": "Response time by destination",
      "analysis": "Identify slow external services",
      "optimization": "Route optimization recommendations"
    },
    "success_rates": {
      "overall_success": "Percentage of successful outbound requests",
      "service_specific": "Success rates by external service",
      "trend_analysis": "Success rate trends over time"
    },
    "usage_patterns": {
      "request_volume": "Number of outbound requests per hour/day",
      "peak_usage": "High-traffic periods identification",
      "cost_analysis": "Static IP cost vs. usage analysis"
    }
  }
}
```

## 🚀 **Advanced Configuration**

### Multi-Region Static IP

```javascript
// Managing static IPs across multiple regions
{
  "multi_region_setup": {
    "regional_ips": {
      "us_east_1": "203.0.113.42",
      "eu_west_1": "198.51.100.23", 
      "ap_southeast_1": "192.0.2.15"
    },
    "routing_strategy": {
      "primary_region": "Route requests from primary instance region",
      "failover": "Automatic failover to backup regions",
      "load_balancing": "Distribute requests across regions"
    },
    "service_configuration": {
      "global_services": "Configure all regional IPs in external services",
      "region_specific": "Use region-specific IPs for local services",
      "compliance": "Meet data residency requirements"
    }
  }
}
```

### Integration Testing

```javascript
// Testing static IP integrations
{
  "testing_framework": {
    "ip_verification": {
      "endpoint": "https://api.ipify.org",
      "method": "GET",
      "purpose": "Verify outbound IP matches static IP",
      "expected_response": "{{configured_static_ip}}"
    },
    "service_connectivity": {
      "test_cases": [
        {
          "name": "Banking API Connection",
          "endpoint": "https://banking-api.com/health",
          "expected_status": 200,
          "validation": "IP whitelisting working"
        },
        {
          "name": "Corporate System Access",
          "endpoint": "https://erp.company.com/api/ping",
          "expected_status": 200,
          "validation": "Firewall rules configured correctly"
        }
      ]
    },
    "security_validation": {
      "ssl_verification": "Test SSL/TLS handshake success",
      "certificate_validation": "Verify certificate chain",
      "encryption_strength": "Confirm encryption standards"
    }
  }
}
```

## 🎯 **Best Practices**

### Security Guidelines

```javascript
// Best practices for static IP security
{
  "security_best_practices": {
    "ip_management": {
      "documentation": "Maintain record of all services using static IP",
      "access_control": "Limit who can view/modify IP configurations",
      "change_management": "Process for IP changes or updates"
    },
    "external_service_coordination": {
      "advance_notice": "Notify external services of any IP changes",
      "fallback_planning": "Maintain backup connectivity options",
      "incident_response": "Plan for IP-related connectivity issues"
    },
    "monitoring_alerting": {
      "connectivity_alerts": "Alert on failed external connections",
      "security_alerts": "Monitor for suspicious outbound activity",
      "performance_alerts": "Track degraded response times"
    }
  }
}
```

### Cost Optimization

```javascript
// Managing static IP costs effectively
{
  "cost_optimization": {
    "usage_analysis": {
      "request_patterns": "Analyze which services require static IP",
      "traffic_volume": "Monitor outbound request volumes",
      "cost_per_request": "Calculate cost efficiency"
    },
    "optimization_strategies": {
      "selective_routing": "Route only required requests through static IP",
      "request_batching": "Combine multiple requests to reduce calls",
      "caching": "Cache responses to minimize external requests"
    },
    "alternatives": {
      "dynamic_ip_services": "Evaluate services that don't require IP whitelisting",
      "api_gateway": "Consider API gateway solutions for cost reduction",
      "regional_optimization": "Optimize for regional service access"
    }
  }
}
```

---

*Static IP (Outgoing) provides the network-level security and consistency required for enterprise integrations, enabling secure connections to banking systems, corporate APIs, and other services that require IP-based access control.*