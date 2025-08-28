from src.database.models import Offer
from src.repositories.base.postgres import PostgresRepository


class OfferRepository(PostgresRepository):
    model = Offer
