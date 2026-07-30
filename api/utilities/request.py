from fastapi import Request
from models.model import Model

def get_model(request: Request)->Model:
    return request.app.state.model

def get_routes(request: Request)->dict:
    return request.app.state.routes