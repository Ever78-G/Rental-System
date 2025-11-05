import flet as ft

import flet as ft

class Button:
    def __init__(self, title, color=ft.Colors.BLUE_700, onclick=None, icon=None,width=120,height=50):
        self.button = ft.ElevatedButton(
            text=title,
            icon=icon,
            on_click=onclick,
            height=height,
            width=width,
            style=ft.ButtonStyle(
                icon_size=20,
                text_style=ft.TextStyle(size=20),
                bgcolor=color,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=10),
            )
        )

    def get(self):
        return self.button
