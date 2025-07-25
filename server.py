from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import router_registers
from routers import router_gets

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router_registers.router)
app.include_router(router_gets.router)