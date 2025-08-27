from src.api.routers.admin.admin import admin_router
from src.api.routers.buyer.buyer import buyer_router
from src.api.routers.start import start_router

all_routers = (admin_router, buyer_router, start_router)
