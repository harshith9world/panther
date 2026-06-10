# main.py

import customtkinter as ctk

from ui.login_screen import LoginScreen
from ui.cover_page import CoverPage
from ui.dashboard import Dashboard

from auth.sso_auth import SSOAuth
from sharepoint.sp_client import SharePointClient


class PantherApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Panther v3")

        self.geometry("1400x850")

        ctk.set_appearance_mode(
            "dark"
        )

        ctk.set_default_color_theme(
            "blue"
        )

        self.show_login()

    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):

        self.clear()

        LoginScreen(
            self,
            self.show_cover
        )

    def show_cover(self):

        self.clear()

        auth = SSOAuth()

        token = auth.login()[
            "access_token"
        ]

        sp = SharePointClient(
            token
        )

        CoverPage(
            self,
            sp,
            self.show_dashboard
        )

    def show_dashboard(self):

        self.clear()

        Dashboard(self)


if __name__ == "__main__":

    app = PantherApp()

    app.mainloop()