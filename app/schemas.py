from pydantic import BaseModel
from typing import Optional, List


class TournamentCreate(BaseModel):
    name: str


class TournamentResponse(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True


class PlayerCreate(BaseModel):
    name: str
    birth: int


class PlayerResponse(BaseModel):
    id: int
    name: str
    birth: int

    class Config:
        from_attributes = True


class MatchCreate(BaseModel):
    match_order: int
    team_a_player1_id: int
    team_a_player2_id: int
    team_b_player1_id: int
    team_b_player2_id: int
    score_a: Optional[int] = None
    score_b: Optional[int] = None


class MatchResponse(BaseModel):
    id: int
    match_order: int
    score_a: Optional[int]
    score_b: Optional[int]
    winner_team: Optional[str]

    class Config:
        from_attributes = True


class RankingItem(BaseModel):
    player_id: int
    name: str
    birth: int
    wins: int
    score_diff: int