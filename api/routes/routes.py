from fastapi import APIRouter
from api.routes.assignments import router as assignments_router

router = APIRouter()

router.include_router(assignments_router, prefix="/assignments", tags=["Assignments"])