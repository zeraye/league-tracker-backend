import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path
from rank_to_points import rank_to_points

load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")
LEAGUE_V4_ENDPOINT = os.getenv("LEAGUE_V4_ENDPOINT")

def update_points() -> None:
    with open(Path(os.path.dirname(os.path.realpath(__file__))) / "database" / "users.json", "r") as file:
        users_data = json.load(file)
    
    with open(Path(os.path.dirname(os.path.realpath(__file__))) / "database" / "points.json", "r") as file:
        points_data = json.load(file)

    require_database_update = False
    users_points = {}

    for user in users_data:
        request_url = f"{LEAGUE_V4_ENDPOINT}{users_data[user]}?api_key={RIOT_API_KEY}"
        response_data = requests.get(request_url).json()

        for queue_data in response_data:
            if queue_data["queueType"] == "RANKED_SOLO_5x5":
                users_points[user] = rank_to_points(
                    queue_data["tier"],
                    queue_data["rank"],
                    queue_data["leaguePoints"]
                )

                if points_data[user][-1] != users_points[user]:
                    require_database_update = True

    if require_database_update:
        for user in users_points:
            points_data[user].append(users_points[user])

        with open(Path(os.path.dirname(os.path.realpath(__file__))) / "database" / "points.json", "w") as file:
            json.dump(points_data, file)

if __name__ == "__main__":
    update_points()
