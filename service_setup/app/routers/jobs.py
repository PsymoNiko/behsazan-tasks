from fastapi import APIRouter
from typing import List, Dict

router = APIRouter()

# Sample data for movies and jobs
movies = ["OPPENHEIMER", "KILLERS OF THE FLOWER MOON", "SPIDER-MAN: ACROSS THE SPIDER-VERSE"]

jobs_data = {
    "OPPENHEIMER": [
        {"jobName": "job_1", "runType": "manual", "runTime": "2024-02-01 12:00:00"},
        {"jobName": "job_1", "runType": "scheduled", "runTime": "2024-02-01 13:00:00"},
    ],
    "KILLERS OF THE FLOWER MOON": [],
    "SPIDER-MAN: ACROSS THE SPIDER-VERSE": [],
}

@router.get("/movies", response_model=List[str])
def get_movies():
    return movies

@router.get("/jobs/{job_name}", response_model=List[Dict[str, str]])
def get_jobs(job_name: str):
    return jobs_data.get(job_name, [])
