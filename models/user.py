from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from .post import Post
    from .review import Review


class User(Base):
    __tablename__ = 'users'

    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)

    posts: Mapped[list['Post']] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f'<User {self.email}>'

