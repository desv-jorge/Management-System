from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import router_registers
from routers import router_auth
from routers import router_deletes
from routers import router_emails
from routers import router_modifications
from routers import router_gets

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
app.include_router(router_emails.router, prefix="/email")
app.include_router(router_modifications.router, prefix="/modify")
app.include_router(router_gets.router, prefix="/get")