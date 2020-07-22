from sqlalchemy import Column, Integer, String, Numeric

from app.core.database import Base


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=False, index=True)

    def __init__(self, **kwargs):
        super(Car, self).__init__(**kwargs)