from sqlalchemy.orm import Session
from app.models import Tournament, Player, Match


def get_tournaments(db: Session):
    return db.query(Tournament).all()


def get_players(db: Session, tournament_id: int):
    return db.query(Player).filter_by(tournament_id=tournament_id).all()


def get_matches(db: Session, tournament_id: int):
    return db.query(Match).filter_by(tournament_id=tournament_id).order_by(Match.match_order).all()


def create_match(db: Session, tournament_id: int, data):
    winner = None
    if data.score_a is not None and data.score_b is not None:
        winner = "a" if data.score_a > data.score_b else "b"

    match = Match(
        tournament_id=tournament_id,
        match_order=data.match_order,
        team_a_player1_id=data.team_a_player1_id,
        team_a_player2_id=data.team_a_player2_id,
        team_b_player1_id=data.team_b_player1_id,
        team_b_player2_id=data.team_b_player2_id,
        score_a=data.score_a,
        score_b=data.score_b,
        winner_team=winner,
    )

    db.add(match)
    db.commit()
    db.refresh(match)
    return match


def calculate_ranking(db: Session, tournament_id: int):
    players = get_players(db, tournament_id)
    matches = get_matches(db, tournament_id)

    stats = {
        p.id: {
            "player_id": p.id,
            "name": p.name,
            "birth": p.birth,
            "wins": 0,
            "score_diff": 0,
        }
        for p in players
    }

    for m in matches:
        if m.score_a is None or m.score_b is None:
            continue

        team_a = [m.team_a_player1_id, m.team_a_player2_id]
        team_b = [m.team_b_player1_id, m.team_b_player2_id]

        for p in team_a:
            stats[p]["score_diff"] += (m.score_a - m.score_b)
        for p in team_b:
            stats[p]["score_diff"] += (m.score_b - m.score_a)

        if m.winner_team == "a":
            for p in team_a:
                stats[p]["wins"] += 1
        elif m.winner_team == "b":
            for p in team_b:
                stats[p]["wins"] += 1

    ranking = sorted(
        stats.values(),
        key=lambda x: (
            -x["wins"],
            -x["score_diff"],
            x["birth"],
        ),
    )

    return ranking

# from sqlalchemy.orm import Session
# from models import Tournament, Player, Match


def create_tournament(db: Session, name: str):
    t = Tournament(name=name)
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


def create_player(db: Session, tournament_id: int, name: str, birth: int):
    p = Player(
        tournament_id=tournament_id,
        name=name,
        birth=birth
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


def validate_match_players(p_ids: list):
    # 동일 선수 중복 체크
    if len(p_ids) != len(set(p_ids)):
        raise ValueError("한 경기에서 동일 선수가 중복됨")


def determine_winner(score_a, score_b):
    if score_a is None or score_b is None:
        return None
    return "A" if score_a > score_b else "B"


# def create_match(
#     db: Session,
#     tournament_id: int,
#     match_order: int,
#     teamA: tuple,
#     teamB: tuple,
#     scoreA=None,
#     scoreB=None,
# ):
#     all_players = list(teamA) + list(teamB)

#     validate_match_players(all_players)

#     winner = determine_winner(scoreA, scoreB)

#     match = Match(
#         tournament_id=tournament_id,
#         match_order=match_order,
#         teama_player1_id=teamA[0],
#         teama_player2_id=teamA[1],
#         teamb_player1_id=teamB[0],
#         teamb_player2_id=teamB[1],
#         scorea=scoreA,
#         scoreb=scoreB,
#         winner_team=winner,
#     )

#     db.add(match)
#     db.commit()
#     db.refresh(match)
#     return match

# def calculate_ranking(db: Session, tournament_id: int):
#     players = db.query(Player).filter_by(tournament_id=tournament_id).all()
#     matches = db.query(Match).filter_by(tournament_id=tournament_id).all()

#     stats = {
#         p.id: {
#             "name": p.name,
#             "birth": p.birth,
#             "wins": 0,
#             "score_diff": 0,
#         }
#         for p in players
#     }

#     for m in matches:
#         if m.scorea is None or m.scoreb is None:
#             continue

#         teamA = [m.teama_player1_id, m.teama_player2_id]
#         teamB = [m.teamb_player1_id, m.teamb_player2_id]

#         for p in teamA:
#             stats[p]["score_diff"] += (m.scorea - m.scoreb)
#         for p in teamB:
#             stats[p]["score_diff"] += (m.scoreb - m.scorea)

#         if m.winner_team == "A":
#             for p in teamA:
#                 stats[p]["wins"] += 1
#         elif m.winner_team == "B":
#             for p in teamB:
#                 stats[p]["wins"] += 1

#     ranking = sorted(
#         stats.items(),
#         key=lambda x: (
#             -x[1]["wins"],
#             -x[1]["score_diff"],
#             -x[1]["birth"],
#         ),
#     )

#     return ranking
