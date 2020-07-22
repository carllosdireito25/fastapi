from sqlalchemy import Column, Integer, String

from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    position = Column(String, unique=False, index=True)
    supervisor = Column(String, unique=False, index=True)
    status = Column(String, unique=False, index=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)