#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data

# Function to print section header
print_header() {
    echo "================================================"
    echo "🚀 Generating: $1"
    echo "================================================"
}

# 1. Todo List API Development
print_header "TODO LIST API DEVELOPMENT ALGORITHM"
python generate_prompt.py --template-id dev-algo-v1 --start-prompt "Create a FastAPI-based REST API for a todo list application with:
- CRUD operations for todos
- User authentication with JWT
- SQLite database
- Input validation using Pydantic
- Error handling with proper HTTP status codes
- Unit tests with pytest
- API documentation with Swagger" --output data/TODO_LIST_API_DEV.md

# 2. Authentication Security Review
print_header "AUTH MODULE SECURITY REVIEW"
python generate_prompt.py --template-id code-review-v1 --start-prompt "Perform a security review of the authentication module:
- JWT implementation
- Password hashing with bcrypt
- Session management
- Rate limiting
- OWASP Top 10 compliance
- Security headers
- CSRF protection
- Input sanitization" --output data/AUTH_SECURITY_REVIEW.md

# 3. Database Performance Optimization
print_header "DATABASE PERFORMANCE OPTIMIZATION"
python generate_prompt.py --template-id perf-opt-v1 --start-prompt "Optimize PostgreSQL database performance:
- Current query response time: 3s average
- Target response time: <500ms
- Complex JOIN operations
- Large dataset (10M+ records)
- Heavy concurrent access
- Must maintain data consistency
- Using Django ORM" --output data/DATABASE_PERF_OPT.md

# 4. Legacy Code Refactoring
print_header "MONOLITH TO MICROSERVICES REFACTORING"
python generate_prompt.py --template-id refactor-v1 --start-prompt "Refactor monolithic e-commerce application:
- Current: PHP monolith (Laravel 5.4)
- Target: Microservices architecture
- Split into: Auth, Products, Orders, Payment
- Must maintain API compatibility
- Zero downtime migration
- Gradual transition strategy
- Docker containerization" --output data/MONOLITH_REFACTOR.md

# 5. Payment System Test Suite
print_header "PAYMENT SYSTEM TEST SUITE"
python generate_prompt.py --template-id test-gen-v1 --start-prompt "Create comprehensive test suite for payment processing:
- Stripe integration
- PayPal integration
- Credit card processing
- Refund handling
- Error scenarios
- Transaction rollbacks
- Concurrent transactions
- PCI compliance validation
- 95% code coverage target" --output data/PAYMENT_TEST_SUITE.md

# 6. API Gateway Development
print_header "API GATEWAY DEVELOPMENT"
python generate_prompt.py --template-id dev-algo-v1 --start-prompt "Develop an API Gateway using Node.js:
- Route management
- Authentication/Authorization
- Rate limiting
- Request validation
- Response caching
- Circuit breaking
- Load balancing
- Logging and monitoring
- OpenAPI documentation" --output data/API_GATEWAY_DEV.md

# 7. Cache System Optimization
print_header "CACHE SYSTEM OPTIMIZATION"
python generate_prompt.py --template-id perf-opt-v1 --start-prompt "Optimize Redis caching system:
- Current hit rate: 65%
- Target hit rate: 90%
- Memory usage optimization
- Cache invalidation strategy
- Handle cache stampede
- Implement cache warming
- Monitor cache efficiency" --output data/CACHE_OPTIMIZATION.md

# 8. GraphQL API Development
print_header "GRAPHQL API DEVELOPMENT"
python generate_prompt.py --template-id dev-algo-v1 --start-prompt "Create a GraphQL API using Apollo Server:
- Type definitions
- Query resolvers
- Mutation resolvers
- Subscription support
- DataLoader implementation
- Error handling
- Authentication
- Rate limiting
- Performance monitoring" --output data/GRAPHQL_API_DEV.md

echo ""
echo "✅ All examples generated successfully!"
echo "📁 Output files are in the data/ directory:"
ls -l data/

# Set read permissions for all users
chmod 644 data/*.md

echo ""
echo "🔒 File permissions set to 644 (rw-r--r--)" 