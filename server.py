from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import router_registers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router_registers.router, prefix="/register")