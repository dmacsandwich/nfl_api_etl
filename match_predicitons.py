import pandas as pd
from api.data_sources.projections import Projections
from prefect import flow, task


match_ids = pd.read_parquet(r'C:\Users\dylan\OneDrive\Desktop\nfl_api_etl\etl\data\raw\match_ids.parquet')
match_ids = list(match_ids['id'])

projections = Projections()
data = projections.get_projections_by_id(ids=match_ids)

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

home_projections = get_projections(data)