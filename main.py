import requests
import json
import pandas as pd

#github =https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c

YEAR = 2018

year_url = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates={YEAR}&seasontype=2'

response = requests.get(year_url)

season_scoreboard = response.json()

#the above contains two keys and is type dict, legaues and evets
#leagues contains data such week, week start and end date and seaon information such as
#preseason, season, superbowl
print(season_scoreboard['events'][0]['id'])
print(season_scoreboard['events'][0]['date'])
print(season_scoreboard['events'][0]['season']['type'])
print(season_scoreboard['events'][0]['season']['slug'])
print(season_scoreboard['events'][0]['week']['number'])
print(season_scoreboard['events'][0]['competitions'][0]['attendance'])
print(season_scoreboard['events'][0]['competitions'][0]['type']['id'])
print(season_scoreboard['events'][0]['competitions'][0]['venue']['id'])
print(season_scoreboard['events'][0]['competitions'][0]['venue']['capacity'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][0]['homeAway'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][0]['team']['id'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][0]['score'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][0]['team']['displayName'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][1]['homeAway'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][1]['winner'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][1]['team']['id'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][1]['score'])
print(season_scoreboard['events'][0]['competitions'][0]['competitors'][1]['team']['displayName'])












#events has the following format
# [
# {id:400999175, date:'2018-01-06T21:20Z, 
# 'name': 'Tennessee Titans at Kansas City Chiefs', season:{year:2017, 
# type:3, slug: post-season}, week: {number:1}, 
# competitions:[{attendance:73319,type:{id:14}, venue:{id:3622, 'fullName':GEHA Field At Arrow Stadium, address:{city:, state:}, capacity:, indoor:}
# 'competitors': [{'id': '12',  'homeAway': 'home', 'winner': False, 'team': {'id': '12', 'displayName': 'Kansas City Chiefs','venue': {'id': '3622'}]
# }]
#print(df.head())
#print(df.columns)

"""
First entry in data for events
"""
