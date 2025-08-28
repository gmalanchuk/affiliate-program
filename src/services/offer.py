from src.repositories.offer import OfferRepository


class OfferService:
    def __init__(self):
        self.offer_repository = OfferRepository()

    # async def create_offer(self, **kwargs):
    #     await self.offer_repository.add_one(data={
    #         "telegram_user_id": telegram_user_id
    #     })
