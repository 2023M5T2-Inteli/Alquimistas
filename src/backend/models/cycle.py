from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

class Cycle(Base):
    __tablename__ = "Cycles"

    id = Column(Integer, primary_key=True)
    report_id = mapped_column(Integer, ForeignKey('Reports.id'))
    magnetic_field = Column(Float) # in gauss
    speed = Column(Float)  # in mm/s
    cycle_mass = Column(Float) # in grams
    cycle_duration = Column(Integer) # in seconds
    parent = relationship("Report", back_populates="children")

    def __repr__(self) -> str:
      return f"Cycle(id={self.id}, report_id={self.report_id})"