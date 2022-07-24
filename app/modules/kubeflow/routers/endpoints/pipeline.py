from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_pipelines():
    pass

@router.get("/{pipeline_id}")
def get_pipeline():
    pass

@router.get("/{pipeline_name}")
def get_pipeline_by_name():
    pass

