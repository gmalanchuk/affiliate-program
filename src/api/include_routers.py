from src.api.routers.admin import admin_router
from src.api.routers.buyer import buyer_router
from src.api.routers.start import start_router


all_routers = (admin_router, buyer_router, start_router)
