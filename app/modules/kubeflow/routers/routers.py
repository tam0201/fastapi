from fastapi import APIRouter

from .endpoints import pipeline, run

router = APIRouter()

router.include_router(pipeline.router, prefix="/pipelines", tags=["Pipeline"])
router.include_router(run.router, prefix="/runs", tags=["Run"])
