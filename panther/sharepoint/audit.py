# sharepoint/audit.py

from datetime import datetime
from config import LISTS


class AuditService:

    def __init__(self, sp):
        self.sp = sp

    def log(
        self,
        username,
        action,
        details=""
    ):

        self.sp.create_item(
            LISTS["audit"],
            {
                "Username": username,
                "Action": action,
                "Details": details,
                "Timestamp": datetime.now().isoformat()
            }
        )