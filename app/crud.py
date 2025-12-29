from sqlalchemy.orm import Session
from . import models, schemas

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(
        name=team.name,
        university=team.university,
        city=team.city
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_teams(db: Session):
    return db.query(models.Team).all()

def create_result(db: Session, result: schemas.ResultCreate):
    db_result = models.Result(
        team_id=result.team_id,
        game_id=result.game_id,
        place=result.place,
        points=result.points,
        next_round=result.next_round
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_results(db: Session):
    return db.query(models.Result).all()

def get_results_by_team(db: Session, team_id: int):
    return db.query(models.Result).filter(models.Result.team_id == team_id).all()

def get_results_by_game(db: Session, game_id: int):
    return db.query(models.Result).filter(models.Result.game_id == game_id).all()

def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(
        name=game.name,
        league=game.league,
        date=game.date,
        venue=game.venue
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_games(db: Session):
    return db.query(models.Game).all()


def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def delete_game(db: Session, game_id: int):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if game:
        db.delete(game)
        db.commit()
    return game