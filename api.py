import json
import csv
import requests
import player
from flask import flash


def process_playerstats(playerstats):
    stats = playerstats["results"]
    curr_season_stats = stats[0]
    player_obj = player.Player(curr_season_stats)
    player_obj.print_basic_stats()
    return player_obj

def call_api(player_name):
    base_api_url = "https://nba-stats-db.herokuapp.com/api/playerdata/name/"
    name = player_name.split()
    api_url = base_api_url

    for i in range(len(name)-1):
        api_url += name[i] + " "
    api_url += name[-1]

    #api_url = base_api_url + name[0] + " " + name[1]  # this is pretty hardcoded, find a better solution?
    try:
        api_response = requests.get(api_url)
        player_stats = json.loads(api_response.text)
        if player_stats["results"]:
            return process_playerstats(player_stats)
        else:
            print("No player")
    except requests.exceptions.RequestException:
        flash("Please enter the player's full name", "error")

stat_name_map = {
    'id': 'Player ID',
    'player_name': 'Player Name',
    'age': 'Age',
    'games': 'Games Played',
    'games_started': 'Games Started',
    'minutes_played': 'Minutes Played',
    'field_goals': 'Field Goals Made',
    'field_attempts': 'Field Goals Attempted',
    'field_percent': 'Field Goal Percentage',
    'three_fg': 'Three-Point Field Goals Made',
    'three_attempts': 'Three-Point Field Goals Attempted',
    'three_percent': 'Three-Point Field Goal Percentage',
    'two_fg': 'Two-Point Field Goals Made',
    'two_attempts': 'Two-Point Field Goals Attempted',
    'two_percent': 'Two-Point Field Goal Percentage',
    'effect_fg_percent': 'Effective Field Goal Percentage',
    'ft': 'Free Throws Made',
    'fta': 'Free Throws Attempted',
    'ft_percent': 'Free Throw Percentage',
    'ORB': 'Offensive Rebounds',
    'DRB': 'Defensive Rebounds',
    'TRB': 'Total Rebounds',
    'AST': 'Assists',
    'STL': 'Steals',
    'BLK': 'Blocks',
    'TOV': 'Turnovers',
    'PF': 'Personal Fouls',
    'PTS': 'Points',
    'team': 'Team',
    'season': 'Season'
}

"""
if __name__ == '__main__':
    print("Enter an NBA player:")
    base_api_url = "https://nba-stats-db.herokuapp.com/api/playerdata/name/"
    input_player_name = input()
    name = input_player_name.split()
    api_url = base_api_url + name[0] + " " + name[1]  # this is pretty hardcoded, find a better solution?

    api_response = requests.get(api_url)
    player_stats = json.loads(api_response.text)
    if player_stats["results"]:
        process_playerstats(player_stats)
    else:
        print("No player")
"""