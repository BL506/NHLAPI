# NHL team stats

import functions as f

# Get two teams from user (team name, no location) and find their id's
print("Input first team name")
team1 = input()
print("Input second team name")
team2 = input()

id1 = f.get_team_id(team1)
id2 = f.get_team_id(team2)


# Get two goalies from user (last name)
print("Input first team goalie")
goalie1 = input()
print("Input second team goalie")
goalie2 = input()


# Collect team and goalie information
stats1 = {}
stats2 = {}
stats1 = f.get_season_stats(id1)
stats2 = f.get_season_stats(id2)

team_stats1 = f.get_team_stats(stats1)
team_stats2 = f.get_team_stats(stats2)

goalie_stats1 = f.get_goalie_stats(stats1, goalie1)
goalie_stats2 = f.get_goalie_stats(stats2, goalie2)


# Display goalie information
print("\n" + goalie1 + ":\nSave %: " + str(goalie_stats1['save_pct']) 
    + "\tAvg Goals Against: " + str(goalie_stats1['avg_goals_against']))

print("\n" + goalie2 + ":\nSave %: " + str(goalie_stats2['save_pct']) 
    + "\tAvg Goals Against: " + str(goalie_stats2['avg_goals_against']))


# Calculate and display expected values
goals1 = (team_stats1['goals'] + team_stats2['goals_against'])/2
goals2 = (team_stats2['goals'] + team_stats1['goals_against'])/2
shots1 = (team_stats1['shots'] + team_stats2['shots_against'])/2
shots2 = (team_stats2['shots'] + team_stats1['shots_against'])/2
saves1 = goalie_stats1['save_pct'] * shots2
saves2 = goalie_stats2['save_pct'] * shots1
goals_against1 = (shots2 - saves1 + goalie_stats1['avg_goals_against'])/2
goals_against2 = (shots1 - saves2 + goalie_stats2['avg_goals_against'])/2

print("\nExpected totals:")
print("\n" + team1 + ":\nGoals: " + "{:.2f}".format(goals1) + "\tShots: " + "{:.2f}".format(shots1))
print("\n" + team2 + ":\nGoals: " + "{:.2f}".format(goals2) + "\tShots: " + "{:.2f}".format(shots2))
print("\n" + goalie1 + ":\nSaves: " + "{:.2f}".format(saves1) + "\tGoals Against: " + "{:.2f}".format(goals_against1))
print("\n" + goalie2 + ":\nSaves: " + "{:.2f}".format(saves2) + "\tGoals Against: " + "{:.2f}".format(goals_against2))
