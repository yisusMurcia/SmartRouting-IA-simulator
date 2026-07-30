from fastapi import Request
from models.model import Model

def get_model(request: Request)->Model:
    return request.app.state.model