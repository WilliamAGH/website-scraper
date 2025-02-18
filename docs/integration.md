# Frontend-Backend Integration Guide

This guide explains how to effectively coordinate between the TypeScript frontend (/app/) and Python backend (/api/).

## Architecture Overview

```
Frontend (/app/)                 Backend (/api/)
[Port 3000]                     [Port 5000]
+----------------+              +----------------+
|                |              |                |
|  React +       |  HTTP/JSON   |  Flask +      |
|  TypeScript    | <----------> |  SQLAlchemy   |
|                |              |                |
+----------------+              +----------------+
```

## Port Configuration

- Backend API: Port 5000
  - All API routes are prefixed with `/api/`
  - Health check available at `/api/health`
  - Development server: `python main.py`

- Frontend: Port 3000
  - Development server: `pnpm run dev`
  - Production build: `pnpm run build`

## Integration Best Practices

1. **API Communication**
   - All API endpoints are prefixed with `/api/`
   - Use type-safe API clients
   - Handle errors consistently
   - Implement proper loading states

2. **Development Workflow**
   - Start both servers during development
   - Backend changes require server restart
   - Frontend has hot module reloading

3. **Type Safety**
   - Share types between frontend and backend
   - Use Pydantic models for API validation
   - TypeScript interfaces match Pydantic models

4. **Error Handling**
   - Consistent error response format
   - Frontend error boundaries
   - Global error handling

## Common Issues and Solutions

1. **CORS Issues**
   - Backend is configured to allow frontend origin
   - Development servers use different ports
   - Production builds use proper CORS configuration

2. **Port Conflicts**
   - Backend always uses port 5000
   - Frontend always uses port 3000
   - Check for conflicting processes if ports are unavailable

3. **Type Synchronization**
   - Generate TypeScript types from Pydantic models
   - Keep API response types in sync
   - Regular type validation during development

## Development Tips

1. **Local Development**
   - Run both servers simultaneously
   - Watch for changes in both directories
   - Use the development server's hot reload

2. **Testing Integration**
   - Test API endpoints independently
   - Verify frontend-backend communication
   - Use proper error handling

3. **Production Deployment**
   - Build frontend assets
   - Configure proper CORS and security headers
   - Set up proper reverse proxy

## Monitoring and Debugging

1. **Frontend Logs**
   - Browser console for frontend issues
   - Network tab for API requests
   - React DevTools for component debugging

2. **Backend Logs**
   - Flask debug mode enabled
   - Detailed error messages
   - Database query logging

3. **Integration Testing**
   - Test complete user flows
   - Verify data consistency
   - Check error handling
