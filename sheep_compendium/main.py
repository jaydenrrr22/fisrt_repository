from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep
app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id:int):
    sheep = db.get_sheep(id)
    if not sheep:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep

@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id:int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this ID not found")

    del db.data[id]
    return

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id:int, updatedSheep: Sheep):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this ID not found")

    db.data[id] = updatedSheep
    return updatedSheep
