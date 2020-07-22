from sqlalchemy import Column, Integer, String, Numeric

from app.core.database import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=False, index=True)

    def __init__(self, **kwargs):
        super(Stock, self).__init__(**kwargs)



