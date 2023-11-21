from api.data_sources.team_ids import TeamIds
from prefect import flow, task
import pandas as pd

@task(retries=1,retry_delay_seconds=10)
def get_team_ids_from_url()->dict:
    team_ids_data = TeamIds().get_data()
    return team_ids_data

#add cache
@task
def get_team_ids(data: list[dict]) ->list:
    num_of_teams=len(data['sports'][0]['leagues'][0]['teams'])
    
    for i in range(num_of_teams):
        yield (data['sports'][0]['leagues'][0]['teams'][i]['team']['id'],\
              data['sports'][0]['leagues'][0]['teams'][i]['team']['displayName']
        )

#TODO separate logic into etl format. Below should be
@task 
def load_ids_to_parquet(team_ids: list)-> None:
    team_ids_df = pd.DataFrame(team_ids, columns=['team_id', 'team_name'])
    team_ids_df.to_parquet(path=r'./etl/data/raw/team_ids.parquet')

@flow
def team_id_etl()->None:
    team_ids_data = get_team_ids_from_url()
    team_ids = get_team_ids(data=team_ids_data)
    load_ids_to_parquet(team_ids)
    

if __name__ == "__main__":
    # create your first deployment
    team_id_etl.serve(name="Team ID Flow")
    