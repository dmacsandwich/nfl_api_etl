from api.urls import GAME_IDS
from api.nfl_api import NflApi

data =  NflApi().get_data_from_url(url = GAME_IDS)

#TODO make api use generators for further enhancement, make url dynamic for different values
def get_game_ids(data: list[dict])-> list[tuple]:
    num_events = len(data['events'])
    
    return [(data['events'][i]['id'],
            data['events'][i]['date'], 
            data['events'][i]['name']) 
            for i in range(num_events)]
    
#TODO seperate api call, transformation & load into separate files, 
import pandas as pd

game_ids_df = pd.DataFrame(get_game_ids(data),
                           columns=['id', 'date', 'name'])