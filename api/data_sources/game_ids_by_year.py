from .nfl_api import NflApi
from .urls import GAME_IDS

class GameIds(NflApi):
    def __init__(self):
        self.url = GAME_IDS
        super().__init__()
    
    def get_data(self, year:int)-> dict:
        return super().get_data_from_url(self.url.format(year_endpoint=year))
    
    def get_data_by_year(self, years: list)-> list[dict]:
        return [self.get_data(year=year) for year in years]