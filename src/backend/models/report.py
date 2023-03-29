from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

class Report(Base):
    __tablename__ = "Reports"

    id = Column(Integer, primary_key=True)
    project = Column(String)
    client = Column(String)
    sample = Column(String)
    operator = Column(String)
    cycle_number = Column(Integer)
    liquid_initial_mass = Column(Float)
    solid_initial_mass = Column(Float)
    children = relationship("Cycle", back_populates="parent")

    def __repr__(self) -> str:
      return f"Report(id={self.id}, client={self.client}, sample={self.sample}, operator={self.operator}, cycles={self.cycle_number}, liquid_initial_mass={self.liquid_initial_mass}, solid_initial_mass={self.solid_initial_mass})"
