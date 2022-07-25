from kubeflow.routers import routers as kubeflow_router
from fastapi import FastAPI
import uvicorn
import os

port = os.environ["PORT"]
app=FastAPI()

app.include_router(kubeflow_router.router, prefix="/kubeflow", tags=["kubeflow"])


if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=port)