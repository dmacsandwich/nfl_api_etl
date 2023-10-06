from api.nfl_api import NflApi
from api.urls import TEAMS_IDS
from football_team_id import team_ids_df

ATHLETE_IDS = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/12/roster'

athlete_data =  NflApi().get_data_from_url(url = ATHLETE_IDS)

team_rosters = []

# Iterate through team_ids in teams_df
for team_id, team_name in zip(team_ids_df['team_id'], team_ids_df['team_name']):
    # Make API request
    api_url = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team_id}/roster'
    response = requests.get(api_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        roster_data = response.json()
        
        # Store the roster data in the dictionary with team_id as the key
        num_of_athletes = len(roster_data['athletes'][0]['items'])
        
        for i in range(num_of_athletes):
            player_name = roster_data['athletes'][0]['items'][i]['fullName']
            team_rosters.append({'team_name': team_name, 'player_name': player_name})
    else:
        print(f"Failed to fetch data for {team_name} (Team ID: {team_id})")

# Create a DataFrame from the list of dictionaries
team_player_df = pd.DataFrame(team_rosters)