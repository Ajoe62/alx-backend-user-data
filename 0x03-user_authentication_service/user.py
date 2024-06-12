#!/usr/bin/env python3
"""Defines the User model for the application."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """Represents a user in the system.

    Attributes:
        id (int): Unique identifier for the user.
        email (str): Email address of the user, unique per account.
        hashed_password (str): Hashed password for authentication.
        session_id (str): Optional session identifier.
        reset_token (str): Optional token for password reset.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

