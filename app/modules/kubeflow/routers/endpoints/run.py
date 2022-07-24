from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_runs():
    pass

@router.get("/{pipeline_id}")
def get_run():
    pass

@router.get("/{pipeline_name}")
def get_run_by_name():
    pass

