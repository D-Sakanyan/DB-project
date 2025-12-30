from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.get("/search", response_model=List[schemas.Team])
def search_teams(
    city: Optional[str] = Query(None),
    university: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Team)

    if city:
        query = query.filter(models.Team.city == city)

    if university:
        query = query.filter(models.Team.university == university)

    return query.all()
