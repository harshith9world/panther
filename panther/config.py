# config.py

SITE_URL = "https://psixbox.sharepoint.com/sites/test1-Sandbox"

LISTS = {
    "users": "Panther_Users",
    "accounts": "Panther_Accounts",
    "teams": "Panther_Teams",
    "audit": "Panther_AuditLogs"
}

APP_NAME = "Panther v3"

THEME_DEFAULT = "dark"

TOKEN_CACHE_FILE = "token_cache.bin"

# Microsoft public client app
CLIENT_ID = "04f0c124-f2bc-4f9d-8b9a-5a3e9c5f6d34"

SCOPES = [
    "User.Read",
    "Sites.Read.All",
    "Sites.ReadWrite.All"
]