# sharepoint/teams.py

from config import LISTS


class TeamService:

    def __init__(self, sp):
        self.sp = sp

    def get_teams(self):

        rows = self.sp.get_list_items(
            LISTS["teams"]
        )

        return [
            r["TeamName"]
            for r in rows
        ]