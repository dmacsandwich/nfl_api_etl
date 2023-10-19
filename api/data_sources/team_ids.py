from .nfl_api import NflApi
from .urls import TEAMS_IDS

class TeamIds(NflApi):
    def __init__(self):
        self.url = TEAMS_IDS
        super().__init__()
        
    def get_data(self):    
        return super().get_data_from_url(self.url)
    