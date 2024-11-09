from fastapi import FastAPI
from app.routers import jobs

app = FastAPI(
    title="FastAPI Service",
    description="API documentation for the FastAPI service that provides movie and job information.",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI service!"}

app.include_router(jobs.router)
