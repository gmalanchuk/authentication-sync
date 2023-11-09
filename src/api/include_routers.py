from src.api.routers.auth import auth_router
from src.api.routers.permission import permission_router


all_routers = (auth_router, permission_router)
