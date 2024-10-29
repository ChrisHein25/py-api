# endpoints/goodbye.py
from fastapi import APIRouter
from models import GreetRequest

router = APIRouter()

TAG = 'Goodbyes'


@router.post("/api/goodbye-normal", tags=[TAG])
def goodbye_normal_post(request: GreetRequest):
    return {"message": f"Goodbye, {request.name}!"}


@router.post("/api/goodbye-sad", tags=[TAG])
def goodbye_sad_post(request: GreetRequest):
    return {"message": f"Alas, so long my lovely mate {request.name}!"}
