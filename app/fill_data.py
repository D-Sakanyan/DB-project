from app import models, database
from datetime import date

db = database.SessionLocal()

games_data = [
    {"name": "Game 1", "league": "League A", "date": date(2025, 12, 29), "venue": "Stadium 1", "teams": [1, 2]},
    {"name": "Game 2", "league": "League A", "date": date(2025, 12, 30), "venue": "Stadium 2", "teams": [2, 3]},
    {"name": "Game 3", "league": "League B", "date": date(2025, 12, 31), "venue": "Stadium 3", "teams": [1, 3]},
]

for g in games_data:
    game = models.Game(
        name=g["name"],
        league=g["league"],
        date=g["date"],
        venue=g["venue"]
    )
    db.add(game)
    db.commit()
    db.refresh(game)

    for team_id in g["teams"]:
        result = models.Result(
            team_id=team_id,
            game_id=game.id,
            place=0,
            points=0,
            next_round=False
        )
        db.add(result)

    db.commit()
    print(f"Игра '{game.name}' добавлена с результатами команд {g['teams']}")

db.close()