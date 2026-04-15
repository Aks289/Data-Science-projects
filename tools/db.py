import os
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Ensure data folder exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../data/database.db")

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}")

Session = sessionmaker(bind=engine)
Base = declarative_base()


class Shipment(Base):
    __tablename__ = "shipments"

    shipment_id = Column(String, primary_key=True)
    origin = Column(String)
    destination = Column(String)
    cost = Column(Float)
    date = Column(String)


Base.metadata.create_all(engine)