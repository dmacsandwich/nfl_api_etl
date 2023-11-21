from api.data_sources.game_ids_by_year import GameIds
from prefect import flow, task
import pandas as pd

year_range = [2019,2020,2021,2022]

@task(retries=1,retry_delay_seconds=10)
def get_game_ids_from_url()->dict:
    game_ids_data = GameIds().get_data_by_year(years=year_range) 
    return game_ids_data

@task
def get_game_ids(data: list[dict])-> list[tuple]:
    
    for year in range(len(year_range)):
        num_events = data[year]['events']
        for events in range(len(num_events)):
            num_competitions = data[year]['events'][events]['competitions']
            for competitions in range(len(num_competitions)):
                yield (data[year]['events'][events]['id'],
                data[year]['events'][events]['name'],
                data[year]['events'][events]['date'],
                data[year]['events'][events]['season']['year'],
                data[year]['events'][events]['season']['slug'],
                data[year]['events'][events]['week']['number'],
                data[year]['events'][events]['competitions'][competitions]['attendance'],
                data[year]['events'][events]['competitions'][competitions]['venue']['id'],
                data[year]['events'][events]['competitions'][competitions]['venue']['fullName'],
                data[year]['events'][events]['competitions'][competitions]['venue']['address']['city'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][0]['leaders'][0]['athlete']['id'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][0]['leaders'][0]['athlete']['team']['id'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][0]['leaders'][0]['value'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][1]['leaders'][0]['athlete']['id'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][1]['leaders'][0]['athlete']['team']['id'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][1]['leaders'][0]['value'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][2]['leaders'][0]['athlete']['id'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][2]['leaders'][0]['athlete']['team']['id'],
                data[year]['events'][events]['competitions'][competitions]['leaders'][2]['leaders'][0]['value'],
                data[year]['events'][events]['competitions'][competitions]['competitors'][0]['id'],
                data[year]['events'][events]['competitions'][competitions]['competitors'][0]['score'],
                data[year]['events'][events]['competitions'][competitions]['competitors'][1]['id'],
                data[year]['events'][events]['competitions'][competitions]['competitors'][1]['score']
                )


@task 
def load_ids_to_parquet(game_ids: list)->None:
    game_ids_df = pd.DataFrame(game_ids,
                            columns=['id', 'name', 'date', 'season_year', 'type_of_season', 'week_number',\
                                        'attendance', 'venue_id', 'venue_name', 'city',\
                                        'passing_leader_id', 'passing_leader_team_id', 'passing_leader_value',\
                                        'rushing_leader_id', 'rushing_leader_team_id', 'rushing_leader_value',\
                                        'receiving_leader_id', 'receiving_leader_team_id', 'receiving_leader_value',\
                                        'home_team_id', 'home_score', 'away_team_id', 'away_score'])
    game_ids_df.to_parquet(path=r'./etl/data/raw/match_ids.parquet')

@flow
def game_id_etl()->None:
    game_ids_data = get_game_ids_from_url()
    game_ids = get_game_ids(data=game_ids_data)
    load_ids_to_parquet(game_ids)


if __name__ == "__main__":
    game_id_etl.serve(name="Game ID Flow")