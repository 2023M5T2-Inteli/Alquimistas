from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime

class Report(Base):
    __tablename__ = "Reports"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True))
    project=Column(String)
    client=Column(String)
    sample=Column(String)
    operator=Column(String)
    cycles=Column(Integer)
    liquid_initial_mass=Column(Float)
    solid_initial_mass=Column(Float)
    duration = Column(Float)
    magnetic_field = Column(Float)
    velocity = Column(Float)
    cycle_time=Column(Float)
    magnet_heigth = Column(Float)

    def __repr__(self) -> str:
      return f"Report(id={self.id}, client={self.client}, sample={self.sample}, operator={self.operator}, cycles={self.cycles}, liquid_initial_mass={self.liquid_initial_mass}, solid_initial_mass={self.solid_initial_mass})"
