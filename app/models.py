from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db import Base


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    status = Column(String(20), default="READY")

    players = relationship("Player", back_populates="tournament")
    matches = relationship("Match", back_populates="tournament")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    name = Column(String(50), nullable=False)
    birth = Column(Integer, nullable=False)

    tournament = relationship("Tournament", back_populates="players")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))

    match_order = Column(Integer)

    teama_player1_id = Column(Integer)
    teama_player2_id = Column(Integer)
    teamb_player1_id = Column(Integer)
    teamb_player2_id = Column(Integer)

    scorea = Column(Integer)
    scoreb = Column(Integer)

    is_tiebreak = Column(Boolean, default=False)
    winner_team = Column(String(1))

    tournament = relationship("Tournament", back_populates="matches")