# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install backend dependencies
uv sync

# Install frontend dependencies
cd app && pnpm install
```

2. Start development servers:
```bash
# Terminal 1: Start backend
python main.py

# Terminal 2: Start frontend
cd app && pnpm run dev