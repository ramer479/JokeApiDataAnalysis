import requests
from src.dao.api_dao import ApiDAO
from typing import Dict, Any


class APIError(Exception):
    pass


class JokeApi(ApiDAO):
    def __init__(self, api_config):
        super().__init__(api_config=api_config)

    def construct_api_url(self) -> str:
        cfg = self.api_config
        base_url = cfg.get("base_api_url")
        print(base_url)

    def make_api_request(self, url: str) -> Dict[str, Any]:
        try:
            response = requests.get(url=url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # You can handle different request-related exceptions here (e.g., Timeout, ConnectionError)
            raise APIError(f"Error making API request: {e}")
        except ValueError as e:
            # This exception is raised if response.json() cannot decode the JSON data
            raise APIError(f"Error parsing API response JSON: {e}")

    def api_response_handler(self):
        api_url = self.construct_api_url()
        response = self.make_api_request(url=api_url)
        return response
