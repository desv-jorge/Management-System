from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import router_registers
from routers import router_auth
from routers import router_deletes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router_registers.router, prefix="/register")
app.include_router(router_auth.router, prefix="/auth")
app.include_router(router_deletes.router, prefix="/delete")