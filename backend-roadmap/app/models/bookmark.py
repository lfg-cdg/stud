from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    is_favourite = Column(Boolean, default=False)
