from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import include_all_routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

include_all_routers(app)
