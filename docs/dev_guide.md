# Developer Guide

## Development Rules

### Code Review Process
1. Review existing imports before adding new ones
2. Never modify existing functionality without discussion
3. Double-check all work before submitting
4. Verify type safety compliance

### Code Quality
1. Write clean, simple code
2. Use minimum lines necessary
3. Review code for potential optimizations
4. Follow DRY principles

### Backend Development
1. All backend functionality must be in Python
   - Keep all Python code under /api/
   - Use appropriate error handling
   - Implement proper logging

2. API Design
   - RESTful endpoints under /api/routes/rest/
   - tRPC endpoints under /api/routes/trpc/
   - GraphQL schemas under /api/routes/graphql/

3. Database Operations
   - Use SQLAlchemy for database interactions
   - Implement proper migrations
   - Handle transactions carefully

### Frontend Development
1. UI code only in app/
2. Use proper component composition
3. Implement proper state management
4. Follow accessibility guidelines

### Testing
1. Write unit tests for all new functionality
2. Maintain test coverage
3. Use appropriate mocking

### Documentation
1. Keep documentation up-to-date
2. Document all API changes
3. Include examples in documentation

## Getting Started

1. Clone the repository
2. Install uv package manager
3. Install dependencies: `uv pip install -e .`
4. Start the server: `python main.py`
5. Visit http://localhost:5000/api/health to verify