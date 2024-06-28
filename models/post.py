from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .review import Review


class Post(Base):
    __tablename__ = 'posts'

    title: Mapped[str] = mapped_column(String(155), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.pk'))
    user: Mapped['User'] = relationship(back_populates='posts')
    reviews: Mapped[list['Review']] = relationship(back_populates='post')

    def __repr__(self):
        return f'<Post(title={self.title!r}, content={self.content!r}, user_id={self.user_id!r})>'
