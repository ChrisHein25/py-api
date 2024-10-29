# main.py
from fastapi import FastAPI
from config import settings
from endpoints.greet import router as greet_router
from endpoints.goodbye import router as goodbye_router

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    summary=settings.SUMMARY,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

# Include routers with the versioned prefix
app.include_router(greet_router)
app.include_router(goodbye_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
