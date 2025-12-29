from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database, schemas, crud
from fastapi import HTTPException

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/teams", response_model=schemas.TeamResponse)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)

@app.get("/teams", response_model=list[schemas.TeamResponse])
def read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)

@app.get("/teams/{team_id}")
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.put("/teams/{team_id}")
def update_team(
    team_id: int,
    team: schemas.TeamCreate,
    db: Session = Depends(get_db)
):
    db_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")

    db_team.name = team.name
    db_team.university = team.university
    db_team.city = team.city

    db.commit()
    db.refresh(db_team)
    return db_team

@app.delete("/teams/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    db.delete(team)
    db.commit()
    return {"detail": "Team deleted"}

@app.post("/results", response_model=schemas.ResultResponse)
def create_result(result: schemas.ResultCreate, db: Session = Depends(get_db)):
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

@app.get("/results", response_model=list[schemas.ResultResponse])
def read_results(db: Session = Depends(get_db)):
    return db.query(models.Result).all()

@app.get("/results/team/{team_id}", response_model=list[schemas.ResultResponse])
def results_by_team(team_id: int, db: Session = Depends(get_db)):
    return db.query(models.Result).filter(models.Result.team_id == team_id).all()

@app.post("/games", response_model=schemas.GameResponse)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db, game)


@app.get("/games", response_model=list[schemas.GameResponse])
def read_games(db: Session = Depends(get_db)):
    return crud.get_games(db)


@app.get("/games/{game_id}", response_model=schemas.GameResponse)
def read_game(game_id: int, db: Session = Depends(get_db)):
    game = crud.get_game(db, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


@app.delete("/games/{game_id}")
def delete_game(game_id: int, db: Session = Depends(get_db)):
    game = crud.delete_game(db, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"detail": "Game deleted"}