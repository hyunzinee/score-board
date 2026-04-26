from app.db import SessionLocal
from app.crud import create_tournament, create_player, create_match, calculate_ranking

db = SessionLocal()

# 1. 시합 생성
t = create_tournament(db, "테스트 시합")

# 2. 참가자 생성
players = []
players.append(create_player(db, t.id, "A", 1996))
players.append(create_player(db, t.id, "B", 2001))
players.append(create_player(db, t.id, "C", 1986))
players.append(create_player(db, t.id, "D", 1991))

# 3. 경기 생성
create_match(
    db,
    t.id,
    1,
    (players[0].id, players[1].id),
    (players[2].id, players[3].id),
    scoreA=6,
    scoreB=4,
)

create_match(
    db,
    t.id,
    2,
    (players[0].id, players[2].id),
    (players[1].id, players[3].id),
    scoreA=3,
    scoreB=6,
)

# 4. 랭킹 계산
ranking = calculate_ranking(db, t.id)

print("=== Ranking ===")
for rank, (pid, stat) in enumerate(ranking, start=1):
    print(rank, stat)