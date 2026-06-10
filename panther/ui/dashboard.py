# ui/dashboard.py

import customtkinter as ctk
from auth.session import Session


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.build_ui()

    def build_ui(self):

        self.pack(
            fill="both",
            expand=True
        )

        sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=0
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        ctk.CTkLabel(
            sidebar,
            text="⚡ PANTHER",
            font=("Segoe UI", 26, "bold")
        ).pack(pady=30)

        menu_items = [
            "Dashboard",
            "Load Excel",
            "Layout Generator",
            "LISP Preview",
            "AutoCAD"
        ]

        if Session.role == "Admin":
            menu_items.append(
                "User Management"
            )

        for item in menu_items:

            ctk.CTkButton(
                sidebar,
                text=item,
                width=180
            ).pack(pady=8)

        self.mode_switch = ctk.CTkSwitch(
            sidebar,
            text="Dark Mode",
            command=self.toggle_mode
        )

        self.mode_switch.select()

        self.mode_switch.pack(
            side="bottom",
            pady=20
        )

        content = ctk.CTkFrame(self)

        content.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        header = ctk.CTkLabel(
            content,
            text=f"{Session.account} | {Session.team}",
            font=("Segoe UI", 24, "bold")
        )

        header.pack(
            anchor="w",
            pady=(10, 0)
        )

        user_info = ctk.CTkLabel(
            content,
            text=f"Logged in as: "
                 f"{Session.current_user['full_name']} "
                 f"({Session.role})",
            font=("Segoe UI", 14)
        )

        user_info.pack(
            anchor="w"
        )

    def toggle_mode(self):

        if self.mode_switch.get():

            ctk.set_appearance_mode(
                "dark"
            )

        else:

            ctk.set_appearance_mode(
                "light"
            )