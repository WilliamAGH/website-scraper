# Repository Rules

## Type Safety Requirements

### Python
- Use Pydantic for data validation
- Enable strict MyPy checking
- All functions must have type annotations
- No `Any` types unless absolutely necessary

### TypeScript (Frontend)
- Strict mode enabled
- No `any` types
- Use proper interface definitions

## File Naming Conventions
- Python files (api/): snake_case
- TypeScript files (app/): camelCase
- Test files: `*_test.py` or `*.test.ts`

## Documentation Requirements
- All public functions must have docstrings
- Include type hints in docstrings
- Document complex algorithms
- Keep related code files linked

## Code Organization
- All Python backend code must be in /api/
- All TypeScript frontend code must be in /app/
- Separate concerns between UI and business logic
