from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models
from app import crud, schemas
from app.database import get_db
from app.crud import get_results_count_by_team
from sqlalchemy import desc

router = APIRouter(prefix="/results", tags=["Results"])


@router.get("/join", response_model=List[schemas.ResultJoin])
def read_results_join(db: Session = Depends(get_db)):
    return crud.get_results_with_join(db)

@router.put("/update/{team_id}/{game_id}")
def update_result(team_id: int, game_id: int, result: schemas.ResultUpdate, db: Session = Depends(get_db)):
    db_result = db.query(models.Result).filter(
        models.Result.team_id == team_id,
        models.Result.game_id == game_id
    ).first()

    if not db_result:
        raise HTTPException(status_code=404, detail="Result not found")

    if result.place is not None:
        db_result.place = result.place
    if result.points is not None:
        db_result.points = result.points

    db.commit()
    db.refresh(db_result)
    return db_result

@router.get("/count-by-team")
def results_count(db: Session = Depends(get_db)):
    return get_results_count_by_team(db)

@router.get("/results/sorted", response_model=list[schemas.ResultResponse])
def get_sorted_results(
    db: Session = Depends(get_db),
    sort_by: str = "points",
    descending: bool = False
):
    query = db.query(models.Result)

    if not hasattr(models.Result, sort_by):
        raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}")

    column = getattr(models.Result, sort_by)
    if descending:
        query = query.order_by(desc(column))
    else:
        query = query.order_by(column)

    return query.all()