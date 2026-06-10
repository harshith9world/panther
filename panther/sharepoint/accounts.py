# sharepoint/accounts.py

from config import LISTS


class AccountService:

    def __init__(self, sp):
        self.sp = sp

    def get_accounts(self):

        rows = self.sp.get_list_items(
            LISTS["accounts"]
        )

        return [
            r["AccountName"]
            for r in rows
        ]