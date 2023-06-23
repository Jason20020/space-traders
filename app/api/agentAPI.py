import requests
import json
from .. import config


class AgentAPI:
    def __init__(self, base_url=None):
        self.base_url = base_url or config.APIURL
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def register(self, faction, symbol, email):
        url = f"{self.base_url}/v2/register"
        data = {
            "faction": faction,
            "symbol": symbol,
            "email": email
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data))

        # Check the response status code and handle errors if needed
        if response.status_code != 200:
            raise Exception(f"Request failed with status {response.status_code}")

        # Parse the response JSON and return it
        return response.json()