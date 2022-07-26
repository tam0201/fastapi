from kubeflow.routers import routers as kubeflow_router
from fastapi import FastAPI
import uvicorn
import os

port = os.environ["PORT"]
app=FastAPI()

app.include_router(kubeflow_router.router, prefix="/kubeflow", tags=["kubeflow API"])

@app.get("/")
def index():
    return {"data": "Application ran successfully - FastAPI"}

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=port, reload=False)