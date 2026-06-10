# ui/cover_page.py

import customtkinter as ctk

from auth.session import Session
from sharepoint.accounts import AccountService
from sharepoint.teams import TeamService


class CoverPage(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        sp,
        on_continue
    ):
        super().__init__(parent)

        self.sp = sp
        self.on_continue = on_continue

        self.account_service = AccountService(
            sp
        )

        self.team_service = TeamService(
            sp
        )

        self.build_ui()

    def build_ui(self):

        self.pack(
            fill="both",
            expand=True
        )

        frame = ctk.CTkFrame(
            self,
            width=500,
            height=420,
            corner_radius=20
        )

        frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        user = Session.current_user

        title = ctk.CTkLabel(
            frame,
            text=f"Welcome {user['full_name']}",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(pady=(30, 10))

        role = ctk.CTkLabel(
            frame,
            text=f"Role: {Session.role}",
            font=("Segoe UI", 14)
        )

        role.pack()

        accounts = self.account_service.get_accounts()
        teams = self.team_service.get_teams()

        ctk.CTkLabel(
            frame,
            text="Select Account"
        ).pack(pady=(25, 5))

        self.account_combo = ctk.CTkComboBox(
            frame,
            values=accounts,
            width=280
        )

        self.account_combo.pack()

        ctk.CTkLabel(
            frame,
            text="Select Team"
        ).pack(pady=(25, 5))

        self.team_combo = ctk.CTkComboBox(
            frame,
            values=teams,
            width=280
        )

        self.team_combo.pack()

        btn = ctk.CTkButton(
            frame,
            text="Continue",
            width=220,
            height=48,
            command=self.continue_dashboard
        )

        btn.pack(pady=35)

    def continue_dashboard(self):

        Session.account = (
            self.account_combo.get()
        )

        Session.team = (
            self.team_combo.get()
        )

        self.on_continue()