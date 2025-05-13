from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Database
from app.models.semaforo import Semaforo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/semaforos")
def listarSemaforos():
    sems = Semaforo.selectAll()
    return [vars(s) for s in sems]
