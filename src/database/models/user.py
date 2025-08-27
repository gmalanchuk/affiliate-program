from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import TimeStampMixin, Base


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    telegram_user_id: Mapped[int] = mapped_column(nullable=False, unique=True)
