# This file is used to ensure that all models are imported before
# Base is used by Alembic or for database creation.

from app.db.base_class import Base
from app.models.user import User
from app.models.client import Client
