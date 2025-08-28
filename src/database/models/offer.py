from enum import Enum

from sqlalchemy import ForeignKey, Numeric, DECIMAL
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Enum as SqlEnum

from src.database.models.base import TimeStampMixin, Base


class OfferType(Enum):
    UNDEFINED = "не визначено"
    NEWS = "новини"
    VACANCIES = "вакансії"


class OfferStatus(Enum):
    IN_PROGRESS = "в процесі"
    SUSPENDED = "призупинено"
    COMPLETED = "завершено"


class Offer(Base, TimeStampMixin):
    __tablename__ = "offers"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    link: Mapped[str]
    type: Mapped[OfferType] = mapped_column(SqlEnum(OfferType), default=OfferType.UNDEFINED)
    status: Mapped[OfferStatus] = mapped_column(SqlEnum(OfferStatus), default=OfferStatus.SUSPENDED)
    price: Mapped[DECIMAL] = mapped_column(DECIMAL(precision=4, scale=2), default=0.0)
    # описание
    # users m2m потому что много людей могут брать много офферов
