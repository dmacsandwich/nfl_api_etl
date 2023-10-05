import requests
from custom_logging.custom_logger import CustomLogger as logger


class NflApi:
    def __init__(self) -> None:
        self.log = logger('NflApi').get_logger()
        
    def add_url_endpoints(self, url) -> str:
        pass
        
    def get_data_from_url(self, url: str) -> dict:
        """Gets data from specified URL and returns in form of dict
        raises exception otherwise.

        Args:
            url (str): API url to get data

        Returns:
            dict: Returns dict of the data from URL.
        """
        self.log.info(f'Sending request to {url}')
        response = requests.get(url)
        try:
            self.log.info(f'Successfully received data from {url}')
            return response.json()
        except:
            self.log.error(f'Failed to receive data from {url}. Status code: {response.status_code}')