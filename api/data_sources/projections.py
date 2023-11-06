from .nfl_api import NflApi
from .urls import MATCH_PREDICTIONS

class Projections(NflApi):
    def __init__(self):
        self.url = MATCH_PREDICTIONS
        super().__init__()
    
    def get_data(self, id:int)-> dict:
        return super().get_data_from_url(self.url.format(event_id=id))
    
    def get_projections_by_id(self, ids: list)-> list[dict]:
        return [self.get_data(id=id) for id in ids]