import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api.routes.rest.health import router as health_router
from api.routes.trpc.router import router as trpc_router
from api.routes.graphql.schema import schema
import strawberry
from strawberry.fastapi import GraphQLRouter

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(title="Mini API V2")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REST routes
app.include_router(health_router, prefix="/api")

# tRPC routes
app.include_router(trpc_router, prefix="/trpc")

# GraphQL routes
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
