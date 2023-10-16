from api.data_sources.game_ids_by_year import GameIds

year_range = [2019,2020,2021,2022]
data = GameIds().get_data_by_year(years=year_range) 

#TODO make api use generators for further enhancement, make url dynamic for different values
def get_game_ids(data: list[dict])-> list[tuple]:
    
    entries = []
    for datapacks in data:
        for i in range(len(datapacks)):  
            entries.append((datapacks['events'][i]['id'],
            datapacks['events'][i]['date'], 
            datapacks['events'][i]['name']))
    return entries
    
#TODO seperate api call, transformation & load into separate files, 
import pandas as pd

game_ids_df = pd.DataFrame(get_game_ids(data),
                           columns=['id', 'date', 'name'])

game_ids_df.to_parquet(path=r'./etl/data/raw/match_ids.parquet')