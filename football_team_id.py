from api.nfl_api import NflApi

URL = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams'
data = NflApi().get_data_from_url(url=URL)

num_of_teams=len(data['sports'][0]['leagues'][0]['teams'])
for i in range(num_of_teams):
    print(data['sports'][0]['leagues'][0]['teams'][i]['team']['id'] \
    ,data['sports'][0]['leagues'][0]['teams'][i]['team']['displayName'])
#print(data['sports'][0]['leagues'][0]['teams'][0]['team'])