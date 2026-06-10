# sharepoint/users.py

from config import LISTS


class UserService:

    def __init__(self, sp):
        self.sp = sp

    def get_user_by_email(self, email):

        users = self.sp.get_list_items(
            LISTS["users"]
        )

        for user in users:

            sp_email = user.get(
                "Email", ""
            ).lower()

            if sp_email == email.lower():

                return {
                    "username": user.get("Username"),
                    "role": user.get("Role"),
                    "active": user.get("Active"),
                    "full_name": user.get("FullName"),
                    "email": sp_email
                }

        return None