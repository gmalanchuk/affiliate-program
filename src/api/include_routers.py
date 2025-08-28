from src.api.routers.admin.admin import admin_router
from src.api.routers.admin.create_offer import create_offer_router
from src.api.routers.buyer import buyer_router
from src.api.routers.start import start_router

all_routers = (admin_router, buyer_router, start_router, create_offer_router)
