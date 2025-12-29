import requests
import random

BASE_URL = "http://127.0.0.1:8000/teams/"

team_names = [
    "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Theta", "Lambda"
]
universities = [
    "MIT", "Stanford", "Harvard", "Cambridge", "Oxford", "Moscow State"
]
cities = [
    "New York", "London", "Moscow", "Boston", "Cambridge", "San Francisco"
]

NUM_TEAMS = 50

for i in range(NUM_TEAMS):
    data = {
        "name": random.choice(team_names) + f" {i+1}",
        "university": random.choice(universities),
        "city": random.choice(cities)
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print(f"[OK] Добавлена команда: {data['name']}")
    else:
        print(f"[ERROR] Не удалось добавить: {data['name']}, {response.text}")
