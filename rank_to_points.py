tier_map = {
    "IRON": 0,
    "BRONZE": 400,
    "SILVER": 800,
    "GOLD": 1200,
    "PLATINUM": 1600,
    "DIAMOND": 2000,
    "MASTER": 2400,
    "GRANDMASTER": 2400,
    "CHALLENGER": 2400
}

rank_map = {
    "I": 300,
    "II": 200,
    "III": 100,
    "IV": 0
}

def rank_to_points(tier: str, rank: str, league_points: int) -> int:
    return tier_map[tier] + rank_map[rank] + league_points
