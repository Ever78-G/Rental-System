import flet as ft
from database.db import db_manager,get_db_path
from pages.login import LoginPage
from database.models.user import User


def main(page: ft.Page):

    def route_change(e):
        page.views.clear()
        page.snack_bar = ft.SnackBar(content=ft.Text(""), open=False)

        if page.route == "/login" or page.route == "/":
            page.views.append(LoginPage(page))
        elif page.route == "/home":
            page.views.append(
                ft.View(
                    "/home",
                    controls=[
                        ft.Text("Bienvenido al Home!", size=30, color=ft.colors.WHITE)
                    ],
                    bgcolor=ft.colors.GREEN_700,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)