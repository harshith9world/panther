# auth/sso_auth.py

import msal
import os
import pickle
from config import CLIENT_ID, SCOPES, TOKEN_CACHE_FILE


class SSOAuth:

    def __init__(self):
        self.cache = msal.SerializableTokenCache()

        if os.path.exists(TOKEN_CACHE_FILE):
            self.cache.deserialize(open(TOKEN_CACHE_FILE, "r").read())

        self.app = msal.PublicClientApplication(
            CLIENT_ID,
            token_cache=self.cache
        )

    def save_cache(self):
        if self.cache.has_state_changed:
            with open(TOKEN_CACHE_FILE, "w") as f:
                f.write(self.cache.serialize())

    def login(self):

        accounts = self.app.get_accounts()

        if accounts:
            result = self.app.acquire_token_silent(
                SCOPES,
                account=accounts[0]
            )

            if result and "access_token" in result:
                self.save_cache()
                return result

        flow = self.app.initiate_device_flow(
            scopes=SCOPES
        )

        if "user_code" not in flow:
            raise Exception("Device flow failed.")

        print(flow["message"])

        result = self.app.acquire_token_by_device_flow(flow)

        if "access_token" in result:
            self.save_cache()
            return result

        raise Exception("Microsoft sign-in failed.")