from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_get_task():
    r = client.post("/tasks", json={"title": "apprendre Terraform"})
    assert r.status_code == 201
    task_id = r.json()["id"]

    r = client.get(f"/tasks/{task_id}")
    assert r.status_code == 200
    assert r.json()["title"] == "apprendre Terraform"


def test_get_unknown_task():
    assert client.get("/tasks/99999").status_code == 404
