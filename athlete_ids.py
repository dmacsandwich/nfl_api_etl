from api.data_sources.athlete_ids_by_year import AthleteIds
from prefect import flow, task
import pandas as pd

team_ids = pd.read_parquet("etl/data/raw/team_ids.parquet")
team_ids = list(team_ids.team_id)
year_range = [2019,2020,2021,2022]

@task(retries=1,retry_delay_seconds=10)
def get_athlete_ids_from_url()->dict:
    athlete_data =  AthleteIds().get_athlete_by_id_and_year(years=year_range, team_ids=team_ids)
    return athlete_data

@task
def get_athlete_ids(data: list[dict])-> list[tuple]:
    for team_id in team_ids:
        for position in [0, 1, 2]:
            num_athletes = len(data[int(team_id)]['athletes'][position]['items'])
            for i in range(num_athletes):
                yield (
                        data[int(team_id)]['athletes'][position]['items'][i]['id'],
                        data[int(team_id)]['athletes'][position]['items'][i]['fullName'],
                        data[int(team_id)]['athletes'][position]['items'][i]['weight'],
                        data[int(team_id)]['athletes'][position]['items'][i]['height'],
                        data[int(team_id)]['athletes'][position]['items'][i]['dateOfBirth']
                )

@task
def load_ids_to_parquet(athlete_ids: list)->None:
    athlete_ids_df = pd.DataFrame(athlete_ids, columns=['id', 'fullName', 'weight', 'height', 'dateOfBirth'])
    # Specify the path to save the Parquet file
    parquet_file_path = "etl/data/raw/athlete_ids.parquet"
    athlete_ids_df.to_parquet(parquet_file_path)

@flow
def athlete_id_etl()->None:
    athlete_ids_data = get_athlete_ids_from_url()
    athlete_ids = get_athlete_ids(data=athlete_ids_data)
    load_ids_to_parquet(athlete_ids)

if __name__ == "__main__":
    athlete_id_etl.serve(name="Athlete ID Flow")