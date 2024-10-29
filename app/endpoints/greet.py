# endpoints/greet.py
from fastapi import APIRouter
from models import GreetRequest

router = APIRouter()

TAG = 'Greetings'


@router.get("/api/greet-normal", tags=[TAG])
def greet_normal_get():
    return {"message": "Hello world!"}


@router.post("/api/greet-normal", tags=[TAG])
def greet_normal_post(request: GreetRequest):
    return {"message": f"Hello there, {request.name}!"}


@router.post("/api/greet-pirate", tags=[TAG])
def greet_pirate_post(request: GreetRequest):
    return {"message": f"Ahoy, matey {request.name}!"}
