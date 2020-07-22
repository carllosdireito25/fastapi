from fastapi import APIRouter
from .hello_world import hello_world_routes

api_router = APIRouter()

api_router.include_router(
    hello_world_routes.router,
    prefix='/hello',
    tags=['hello'],
)
