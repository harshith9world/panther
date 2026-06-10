# ui/login_screen.py

import customtkinter as ctk
import threading
from tkinter import messagebox

from auth.sso_auth import SSOAuth
from auth.session import Session

from sharepoint.sp_client import SharePointClient
from sharepoint.users import UserService
from sharepoint.audit import AuditService


class LoginScreen(ctk.CTkFrame):

    def __init__(self, parent, on_success):
        super().__init__(parent)

        self.on_success = on_success

        self.configure(
            fg_color=("gray95", "#171717")
        )

        self.build_ui()

    def build_ui(self):

        self.pack(fill="both", expand=True)

        center = ctk.CTkFrame(
            self,
            corner_radius=20,
            width=500,
            height=420
        )

        center.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        title = ctk.CTkLabel(
            center,
            text="⚡ PANTHER",
            font=("Segoe UI", 34, "bold")
        )
        title.pack(pady=(40, 10))

        subtitle = ctk.CTkLabel(
            center,
            text="AutoCAD Layout Generator v3",
            font=("Segoe UI", 15)
        )
        subtitle.pack()

        self.status_lbl = ctk.CTkLabel(
            center,
            text="Ready to sign in",
            font=("Segoe UI", 14)
        )
        self.status_lbl.pack(pady=20)

        self.login_btn = ctk.CTkButton(
            center,
            text="Sign in with Microsoft",
            height=48,
            width=280,
            command=self.start_login
        )

        self.login_btn.pack(pady=20)

        self.progress = ctk.CTkProgressBar(
            center,
            width=280
        )

        self.progress.set(0)

    def start_login(self):

        self.login_btn.configure(
            state="disabled"
        )

        self.progress.pack(pady=10)

        thread = threading.Thread(
            target=self.login_process
        )

        thread.start()

    def login_process(self):

        try:

            self.update_status(
                "Connecting to Microsoft..."
            )

            auth = SSOAuth()

            result = auth.login()

            token = result["access_token"]

            email = result["id_token_claims"][
                "preferred_username"
            ]

            self.update_status(
                f"Logged in as {email}"
            )

            sp = SharePointClient(token)

            user_service = UserService(sp)

            user = user_service.get_user_by_email(
                email
            )

            if not user:
                self.after(
                    0,
                    lambda:
                    messagebox.showerror(
                        "Access Denied",
                        "You are not registered in Panther."
                    )
                )
                return

            if not user["active"]:
                self.after(
                    0,
                    lambda:
                    messagebox.showerror(
                        "Inactive User",
                        "Your account is inactive."
                    )
                )
                return

            Session.current_user = user
            Session.role = user["role"]

            audit = AuditService(sp)

            audit.log(
                user["username"],
                "LOGIN"
            )

            self.after(
                0,
                self.on_success
            )

        except Exception as e:

            self.after(
                0,
                lambda:
                messagebox.showerror(
                    "Login Error",
                    str(e)
                )
            )

            self.after(
                0,
                lambda:
                self.login_btn.configure(
                    state="normal"
                )
            )

    def update_status(self, text):

        self.after(
            0,
            lambda:
            self.status_lbl.configure(
                text=text
            )
        )