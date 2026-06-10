# sharepoint/sp_client.py

import requests
from config import SITE_URL


class SharePointClient:

    def __init__(self, token):
        self.token = token

    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json;odata=verbose",
            "Content-Type": "application/json"
        }

    def get_list_items(self, list_name):

        url = (
            f"{SITE_URL}/_api/web/lists"
            f"/getbytitle('{list_name}')/items"
        )

        response = requests.get(
            url,
            headers=self.headers()
        )

        response.raise_for_status()

        return response.json()["d"]["results"]

    def create_item(self, list_name, data):

        url = (
            f"{SITE_URL}/_api/web/lists"
            f"/getbytitle('{list_name}')/items"
        )

        response = requests.post(
            url,
            headers=self.headers(),
            json=data
        )

        response.raise_for_status()

        return response.json()