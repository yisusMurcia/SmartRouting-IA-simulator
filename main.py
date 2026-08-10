from fastapi import FastAPI
from contextlib import asynccontextmanager
from models.trainModel import buildFeatureVector
from routing.routeImportation import getRoutes
from api.routes.routes import router as router
from db.session import init_db, close_db

async def load_data():
    app.state.model = buildFeatureVector()
    app.state.routes = getRoutes()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await load_data()
    init_db()
    yield
    close_db()
app = FastAPI(title="Mi Backend FastAPI", version="1.0.0", lifespan=lifespan)

app.include_router(
    router,
    prefix="/api",
)

@app.get("/")
def home():
    return {"mensaje": "¡Backend funcionando con éxito!"}