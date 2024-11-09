from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI service!"}

def test_get_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    assert response.json() == [
        "OPPENHEIMER", 
        "KILLERS OF THE FLOWER MOON", 
        "SPIDER-MAN: ACROSS THE SPIDER-VERSE"
    ]

def test_get_jobs_oppenheimer():
    response = client.get("/jobs/OPPENHEIMER")
    assert response.status_code == 200
    assert response.json() == [
        {"jobName": "job_1", "runType": "manual", "runTime": "2024-02-01 12:00:00"},
        {"jobName": "job_1", "runType": "scheduled", "runTime": "2024-02-01 13:00:00"},
    ]

def test_get_jobs_non_existent():
    response = client.get("/jobs/NON_EXISTENT_JOB")
    assert response.status_code == 200
    assert response.json() == []
