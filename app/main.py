from fastapi import FastAPI
from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    summary=settings.SUMMARY,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)


@app.get("/api/greet")
def greet():
    return {"message": "Ahoy, World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
