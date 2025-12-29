from pydantic import BaseModel
from typing import Optional
from datetime import date


class TeamBase(BaseModel):
    name: str
    university: Optional[str] = None
    city: Optional[str] = None

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int

    class Config:
        from_attributes = True

class ResultCreate(BaseModel):
    team_id: int
    game_id: int
    place: int
    points: int
    next_round: bool

class ResultResponse(ResultCreate):
    id: int

    class Config:
        from_attributes = True

class GameCreate(BaseModel):
    name: Optional[str] = None
    league: Optional[str] = None
    date: date
    venue: Optional[str] = None


class GameResponse(GameCreate):
    id: int

    class Config:
        from_attributes = True