from fastapi.testclient import TestClient

from main import app
from models.db import db

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    newSheep = {
        "id": 7,
        "name": "TestingName",
        "breed": "TestingBreed",
        "sex": "TestingSex"
    }
    response = client.post("/sheep", json=newSheep)

    assert response.status_code == 201

    assert response.json() == newSheep

    getResponse = client.get("/sheep/7")
    assert response.status_code == 201
    assert getResponse.json() == newSheep

def test_delete_sheep():
    assert 6 in db.data
    response = client.delete("/sheep/6")
    assert response.status_code == 204

    getResponse = client.get("/sheep/6")
    assert getResponse.status_code == 404

def test_update_sheep():
    updatedSheep = {
        "id": 1,
        "name": "TestingUpdateName",
        "breed": "TestingUpdateBreed",
        "sex": "TestingUpdateSex"
    }
    response = client.put("/sheep/1", json=updatedSheep)
    assert response.status_code == 200
    assert response.json() == updatedSheep

    getResponse = client.get("/sheep/1")
    assert response.status_code == 200
    assert getResponse.json() == updatedSheep
