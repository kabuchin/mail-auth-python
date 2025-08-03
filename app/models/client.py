import uuid
from sqlalchemy import Column, String, Boolean, JSON

from app.db.base_class import Base


class Client(Base):
    __tablename__ = "clients"

    client_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    client_secret_hash = Column(String, nullable=False)
    client_name = Column(String, index=True, nullable=False)
    allowed_ips = Column(JSON, nullable=True)  # Stored as a JSON array of strings
    is_active = Column(Boolean, default=True)
