from typing import Dict, Any
from abc import ABC, abstractmethod


class ApiDAO(ABC):
    """Generic class to interact with an API
    Args : This constructor takes api_config, which contains api base url params, as dictionary input
    """
    def __init__(self, api_config: Dict[str, Any]):
        self.api_config = api_config

    @abstractmethod
    def construct_api_url(self) -> str:
        """An Abstract method for constructing api url with the help of api_config"""
        pass

    @abstractmethod
    def make_api_request(self, url: str) -> Dict[str, Any]:
        """An Abstract method for making an api request with the help of url constructed"""
        pass

    @abstractmethod
    def api_response_handler(self):
        """An Abstract method to handle the api response data and return the processed result"""
        pass
