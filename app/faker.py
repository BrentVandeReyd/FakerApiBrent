from fastapi import FastAPI
from pydantic import BaseModel
import json
from faker import Faker
from faker.providers import internet
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "https://brentvandereyd.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

@app.get("/internet")
async def root():
    i=0
    fake = Faker()
    fake.add_provider(internet)
    return {fake.ipv4_private()}

@app.get("/japan")
async def root():
    fake = Faker(['ja_JP'])
    for i in range(10):
        return {fake.name()}

@app.get("/Duits")
async def root():
    fake = Faker(['de_DE'])
    for i in range(10):
        return {fake.name()}

class japan(BaseModel):
    name: str

@app.post("/japan/", response_model=japan)
async def Japan(jap: japan):
    return jap

# uvicorn test:app --reload
