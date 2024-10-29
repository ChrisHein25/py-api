"""
Define Pydantic response models
"""

from pydantic import BaseModel


# Define a Pydantic model for request data
class GreetRequest(BaseModel):
    name: str

