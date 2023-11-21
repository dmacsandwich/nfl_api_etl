import pandas as pd
from api.data_sources.projections import Projections
from prefect import flow, task


match_ids = pd.read_parquet(r'etl/data/raw/match_ids.parquet')
match_ids = list(match_ids['id'])
projections = Projections()

@task(retries=1,retry_delay_seconds=10)
def get_projections_from_url()->dict:
    data = projections.get_projections_by_id(ids=match_ids)
    return data

@task
def get_projections(data: list[dict], team: str='homeTeam')-> list[tuple]:
    projections_list = [] 
    for event in data:
        projections_list.append(event[team]['statistics'][0]['name'],
        event[team]['statistics'][0]['value'],
        event[team]['statistics'][1]['name'],
        event[team]['statistics'][1]['value'],
        event[team]['statistics'][2]['name'],
        event[team]['statistics'][2]['value'],
        event[team]['statistics'][3]['name'],
        event[team]['statistics'][3]['value'],
        event[team]['statistics'][4]['name'],
        event[team]['statistics'][4]['value'],
        event[team]['statistics'][5]['name'],
        event[team]['statistics'][5]['value'],
        event[team]['statistics'][6]['name'],
        event[team]['statistics'][6]['value'],
        event[team]['statistics'][7]['name'],
        event[team]['statistics'][7]['value'],
        event[team]['statistics'][8]['name'],
        event[team]['statistics'][8]['value'],
        event[team]['statistics'][9]['name'],
        event[team]['statistics'][9]['value'],
        event[team]['statistics'][11]['name'],
        event[team]['statistics'][11]['value'],
        event[team]['statistics'][12]['name'],
        event[team]['statistics'][12]['value'],
        event[team]['statistics'][13]['name'],
        event[team]['statistics'][13]['value'],
        event[team]['statistics'][14]['name'],
        event[team]['statistics'][14]['value'])
    return projections_list

@flow
def projections_etl():
    projections_data = get_projections_from_url()
    home_projections = get_projections(projections_data)


if __name__ == "__main__":
    projections_etl.serve("Projections Flow")