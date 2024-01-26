from fastapi import FastAPI
from controllers import router as post_router

app = FastAPI()

app.include_router(post_router)
