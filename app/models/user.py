import uuid
from sqlalchemy import Column, String, Boolean, Enum as SAEnum, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(SAEnum("admin", "client", name="user_role_enum"), nullable=False)
    client_id = Column(String, ForeignKey("clients.client_id"), nullable=True)
    is_active = Column(Boolean, default=True)

    client = relationship("Client")
