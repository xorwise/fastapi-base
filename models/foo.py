from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base


class SampleItem(Base):
    __tablename__ = "sample_items"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    public = Column(Boolean, default=False)
