from api.term.router import router as term_router
from fastapi import APIRouter

router = APIRouter()
routers_to_include = [term_router]
[router.include_router(router_to_include) for router_to_include in routers_to_include]