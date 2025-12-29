from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    university = Column(String)
    city = Column(String)
    results = relationship("Result", back_populates="team")

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    league = Column(String)
    date = Column(Date)
    venue = Column(String)
    results = relationship("Result", back_populates="game")

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    place = Column(Integer)
    points = Column(Integer)
    next_round = Column(Boolean)
    team = relationship("Team", back_populates="results")
    game = relationship("Game", back_populates="results")
