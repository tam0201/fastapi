from kubeflow.routers import routers as kubeflow_router
from fastapi import FastAPI
import uvicorn

app=FastAPI()

app.include_router(kubeflow_router.router, prefix="/kubeflow", tags=["kubeflow"])


if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)