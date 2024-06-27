from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class User(Base):
    __tablename__ = 'users'

    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
