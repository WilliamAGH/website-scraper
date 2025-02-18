cp .env.example .env
```

2. Configure environment variables in `.env`:
   - `API_URL`: Backend API URL (default: http://localhost:5000)
   - `APP_URL`: Frontend URL (default: http://localhost:3000)
   - `API_PORT`: Optional override for backend port
   - `APP_PORT`: Optional override for frontend port

Note: If `API_PORT` or `APP_PORT` are not set, the system will attempt to parse the port from `API_URL` or `APP_URL` respectively.

## Installation

```bash
# Install backend dependencies
cd api && uv sync

# Install frontend dependencies
cd app && pnpm install
```

## Start development servers:
```bash
# Terminal 1: Start backend
cd api && python main.py

# Terminal 2: Start frontend
cd app && pnpm run dev