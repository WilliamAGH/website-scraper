1. Setup local environment variables:
`cp .env.example .env`

2. Install dependencies:
# Backend
`cd api && uv sync`

# Frontend
`cd app && pnpm install`

3. Start the servers:

# Terminal 1: Start backend (default: http://localhost:5000)
`uv run api/main.py`

# Terminal 2: Start frontend (default: http://localhost:3000)
`cd app && pnpm run dev`

## Development Workflow

The project uses a dual-server setup with configurable ports:
- Backend API server (default: port 5000)
- Frontend development server (default: port 3000)
- Frontend automatically proxies API requests to the backend

Port configuration can be customized via environment variables:
- Use `API_PORT` and `APP_PORT` for explicit port overrides
- Alternatively, ports can be extracted from `API_URL` and `APP_URL`

## Available Endpoints

Backend (default: http://localhost:5000):
- `/api/health` - Health check endpoint
- `/api/v1/*` - REST API endpoints
- `/trpc/*` - tRPC endpoints
- `/graphql` - GraphQL endpoint

Frontend (default: http://localhost:3000):
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