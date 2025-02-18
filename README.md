curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install dependencies:
```bash
uv sync
```

3. Run the server:
```bash
python main.py
```

The server will start at http://localhost:5000. Available endpoints:
- `/` - API information
- `/api/health` - Health check endpoint
- `/trpc` - tRPC endpoints (coming soon)
- `/graphql` - GraphQL endpoint (coming soon)

## Documentation

- [API Documentation](docs/api.md) - Detailed API endpoint documentation
- [Application Guidelines](docs/app.md) - Frontend architecture and styling guidelines
- [Repository Rules](docs/repo_rules.md) - Code organization and type safety requirements
- [Developer Guide](docs/dev_guide.md) - Development workflow and best practices

## Project Structure

```
.
├── api/               # Python backend code
│   ├── routes/       # API endpoints (REST, tRPC, GraphQL)
│   ├── models/       # Data models and schemas
│   └── utils/        # Shared utilities
├── app/              # TypeScript frontend (upcoming)
├── docs/             # Documentation
└── main.py          # Application entry point