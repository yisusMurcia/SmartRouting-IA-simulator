from fastapi import FastAPI
from contextlib import asynccontextmanager
from models.trainModel import buildFeatureVector
from routing.routeImportation import getRoutes

async def load_data():
    app.state.model = buildFeatureVector()
    app.state.routes = getRoutes()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await load_data()
    yield
# Creamos la instancia principal
app = FastAPI(title="Mi Backend FastAPI", version="1.0.0", lifespan=lifespan)

@app.get("/")
def home():
    return {"mensaje": "¡Backend funcionando con éxito!"}