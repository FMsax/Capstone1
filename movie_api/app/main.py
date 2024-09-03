from fastapi import FastAPI
from app.routers import movies, users, comments, ratings
from app.database import engine
from app import models
from uvicorn import run



# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Your routes and logic here

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True)

app.include_router(users.router)
app.include_router(movies.router)
app.include_router(comments.router)
app.include_router(ratings.router)
