from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text, Integer, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .post import Post


class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = (
        CheckConstraint('rating >= 0 AND rating <= 5', name='rating_range'),
    )

    name: Mapped[str]
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now, server_default=func.now())
    rating: Mapped[int] = mapped_column(Integer)

    post_id: Mapped[int] = mapped_column(ForeignKey('posts.pk'))
    post: Mapped['Post'] = relationship(back_populates='reviews')
