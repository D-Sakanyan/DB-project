from pydantic import BaseModel
from typing import Optional
from datetime import date


class TeamBase(BaseModel):
    name: str
    university: Optional[str] = None
    city: Optional[str] = None

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        from_attributes = True


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

class ResultJoin(BaseModel):
    team_name: str
    city: Optional[str]
    game_name: str
    place: int
    points: int

    class Config:
        from_attributes = True

class ResultUpdate(BaseModel):
    place: Optional[int] = None
    points: Optional[int] = None

class GameCreate(BaseModel):
    name: Optional[str] = None
    league: Optional[str] = None
    date: date
    venue: Optional[str] = None


class GameResponse(GameCreate):
    id: int

    class Config:
        from_attributes = True