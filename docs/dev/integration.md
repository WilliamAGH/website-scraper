Frontend (/app/)                 Backend (/api/)
[Port 3000]                     [Port 5000]
+----------------+              +----------------+
|                |              |                |
|  React +       |  HTTP/JSON   |  Flask +      |
|  TypeScript    | <----------> |  SQLAlchemy   |
|                |              |                |
+----------------+              +----------------+
```

## API Endpoints

### REST API (Base: /api/v1)
- `/api/health` - Health check endpoint
- `/api/v1/auth/*` - Authentication endpoints
  - POST `/register` - User registration
  - POST `/login` - User login
  - POST `/logout` - User logout
- `/api/v1/users/*` - User management
  - GET `/` - List users
  - GET `/:id` - Get user details
- `/api/v1/posts/*` - Post management
  - GET `/` - List posts
  - GET `/:id` - Get post details

### GraphQL
- `/graphql` - GraphQL endpoint
  - Supports queries and mutations
  - Interactive playground available in development

### tRPC
- `/trpc/*` - tRPC endpoints
  - Type-safe API calls
  - Automatic type inference

## Development Setup

1. Start the Backend (Port 5000):
```bash
cd api
python main.py
```

2. Start the Frontend (Port 3000):
```bash
cd app
pnpm install
pnpm run dev