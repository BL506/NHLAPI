# Functions for accessing info from sportradar api

import requests
import json

headers = {"accept": "application/json"} # Headers for requests


# Get team id from given team name
def get_team_id(team_name):
  try:
    url = "https://api.sportradar.com/nhl/trial/v7/en/league/teams.json?api_key=<Insert personal API key>"
    response = requests.get(url, headers=headers)
    dict = response.json() # Workable dictionary with response info
    
    # Search for team name
    for team in dict['teams']:
      if (team['name'] == team_name):
        return team['id']

  except Exception as e:
    print("An error occurred: %s" % e)
    return None


# Get team season statistics
def get_season_stats(id):
  try:
    url = "https://api.sportradar.com/nhl/trial/v7/en/seasons/2024/REG/teams/" + id + "/statistics.json?api_key=<Insert personal API key>"
    response = requests.get(url, headers=headers)
    return response.json() # Workable dictionary with response info

  except Exception as e:
    print("An error occurred: %s" % e)
    return None


# Get team statistics
def get_team_stats(dict):
  stats = {}
  try:
    stats['goals'] = dict['own_record']['statistics']['average']['goals']
    stats['shots'] = dict['own_record']['statistics']['average']['shots']
    stats['goals_against'] = dict['opponents']['statistics']['average']['goals']
    stats['shots_against'] = dict['opponents']['statistics']['average']['shots']

    return stats
  
  except Exception as e:
    print("An error occurred: %s" % e)
    return None

# Get goalie statistics
def get_goalie_stats(dict, name):
  stats = {}
  try:
    # Search for goalie name
    for goalie in dict['players']:
      if (goalie['last_name'] == name):
        stats['save_pct'] = goalie['goaltending']['total']['saves_pct']
        stats['avg_goals_against'] = goalie['goaltending']['total']['avg_goals_against']

    return stats

  except Exception as e:
    print("An error occurred: %s" % e)
    return None


