# Backend dependencies
uv sync

# Frontend dependencies
cd app && pnpm install
```

2. Start the servers:
```bash
# Terminal 1: Start backend
cd api && python main.py  # Runs on http://localhost:5000

# Terminal 2: Start frontend
cd app && pnpm run dev  # Runs on http://localhost:3000
```

## Development Workflow

The project uses a dual-server setup:
- Backend API server runs on port 5000
- Frontend development server runs on port 3000
- Frontend automatically proxies API requests to the backend

## Available Endpoints

Backend (http://localhost:5000):
- `/api/health` - Health check endpoint
- `/api/v1/*` - REST API endpoints
- `/trpc/*` - tRPC endpoints
- `/graphql` - GraphQL endpoint

Frontend (http://localhost:3000):
- Main application interface
- Dark/light mode toggle
- Responsive design

## Documentation

- [API Documentation](docs/api.md) - Backend API endpoints and usage
- [Frontend Guide](docs/frontend.md) - Frontend architecture and components
- [Integration Guide](docs/integration.md) - Frontend-Backend integration guide
- [Development Guide](docs/dev_guide.md) - Development workflow and best practices
- [Repository Rules](docs/repo_rules.md) - Code organization and type safety

## Project Structure

```
.
├── api/                    # Python backend code
│   ├── routes/            # API endpoints
│   │   ├── rest/         # REST API endpoints
│   │   ├── graphql/      # GraphQL schema and resolvers
│   │   └── trpc/         # tRPC procedures
│   ├── models/           # Data models and schemas
│   ├── utils/            # Shared utilities
│   └── main.py           # Application entry point
├── app/                   # TypeScript frontend
│   ├── src/              # Frontend source code
│   └── ...               # Frontend configuration files
└── docs/                 # Documentation