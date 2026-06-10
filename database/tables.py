from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
Base = declarative_base()

class CatalogProductEntity(Base):
    __tablename__ = os.getenv("CATALOG")

    entity_id = Column(Integer, primary_key=True)
    sku = Column(String)

    