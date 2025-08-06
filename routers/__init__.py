from fastapi import FastAPI

from . import (
    router_registers,
    router_auth,
    router_deletes,
    router_emails,
    router_modifications,
    router_gets
)

def include_all_routers(app: FastAPI):
    app.include_router(router_registers.router, prefix="/register")
    app.include_router(router_auth.router, prefix="/auth")
    app.include_router(router_deletes.router, prefix="/delete")
    app.include_router(router_emails.router, prefix="/email")
    app.include_router(router_modifications.router, prefix="/modify")
    app.include_router(router_gets.router, prefix="/get")
