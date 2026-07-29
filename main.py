from fastapi import FastAPI

# Creamos la instancia principal
app = FastAPI(title="Mi Backend FastAPI", version="1.0.0")

@app.get("/")
def home():
    return {"mensaje": "¡Backend funcionando con éxito!"}