#!/usr/bin/env python3
"""Main application file."""

from typing import List
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Base = declarative_base()

class User(db.Model):
    """User model."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        return f"<User {self.email}>"

@app.route('/')
def home():
    """Return a list of users."""
    users = [user.email for user in User.query.all()]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

