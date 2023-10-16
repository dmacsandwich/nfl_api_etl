from .nfl_api import NflApi
from .urls import ATHLETE_IDS

class AthleteIds(NflApi):
    def __init__(self):
        self.url = ATHLETE_IDS
        super().__init__()
        
    def get_data(self, year:int, id:int) ->list[dict]:
        return super().get_data_from_url(self.url.format(team_id=id, year=year))
    
    def get_athlete_by_id_and_year(self, years: list, team_ids: list):
        data = []
        
        #TODO add dict comprehension for data
        for year in years:
            for id in team_ids:
                data.append(self.get_athlete_by_id_and_year(id,year))
                
        return data