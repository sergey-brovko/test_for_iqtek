from sqlalchemy import Column, Integer, String
from src.database import Base


class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=True)


