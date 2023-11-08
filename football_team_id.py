from api.data_sources.team_ids import TeamIds

team_ids_data = TeamIds().get_data()

def get_team_ids(data: list[dict]) ->list:
    num_of_teams=len(data['sports'][0]['leagues'][0]['teams']):
    
    return [[data['sports'][0]['leagues'][0]['teams'][i]['team']['id'] 
             ,data['sports'][0]['leagues'][0]['teams'][i]['team']['displayName']]
            for i in range(num_of_teams)]

team_ids = get_team_ids(data=team_ids_data)

#TODO separate logic into etl format. Below should be
import pandas as pd
team_ids_df = pd.DataFrame(team_ids, columns=['team_id', 'team_name'])

team_ids_df.to_parquet(path=r'./etl/data/raw/team_ids.parquet')
