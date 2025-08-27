from src.database.models.base import TimeStampMixin, Base


class Offer(Base, TimeStampMixin):
    __tablename__ = "offers"

    pass
    # тип (товарка, гемблинг, вакансии)
    # выплата decimal
    # описание
    # ссылка
    # овнер

