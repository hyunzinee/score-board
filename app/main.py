from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.db import engine
from app.deps import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tennis Tournament API")


# 1. Tournament
@app.post("/tournaments", response_model=schemas.TournamentResponse)
def create_tournament(data: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db, data.name)


@app.get("/tournaments", response_model=list[schemas.TournamentResponse])
def list_tournaments(db: Session = Depends(get_db)):
    return crud.get_tournaments(db)


# 2. Player
@app.post("/tournaments/{tournament_id}/players", response_model=schemas.PlayerResponse)
def create_player(
    tournament_id: int,
    data: schemas.PlayerCreate,
    db: Session = Depends(get_db),
):
    return crud.create_player(db, tournament_id, data.name, data.birth)


@app.get("/tournaments/{tournament_id}/players", response_model=list[schemas.PlayerResponse])
def list_players(tournament_id: int, db: Session = Depends(get_db)):
    return crud.get_players(db, tournament_id)


# 3. Match
@app.post("/tournaments/{tournament_id}/matches", response_model=schemas.MatchResponse)
def create_match(
    tournament_id: int,
    data: schemas.MatchCreate,
    db: Session = Depends(get_db),
):
    return crud.create_match(db, tournament_id, data)


@app.get("/tournaments/{tournament_id}/matches", response_model=list[schemas.MatchResponse])
def list_matches(tournament_id: int, db: Session = Depends(get_db)):
    return crud.get_matches(db, tournament_id)


# 4. Ranking
@app.get("/tournaments/{tournament_id}/ranking", response_model=list[schemas.RankingItem])
def get_ranking(tournament_id: int, db: Session = Depends(get_db)):
    return crud.calculate_ranking(db, tournament_id)