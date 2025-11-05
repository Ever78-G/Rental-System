import flet as ft
from database.models.user import User
from ui.button_iu import Button


def LoginPage(page: ft.Page):
    # Configurar el snackbar en la página (NO dentro del Column)
    data =page.snack_bar = ft.SnackBar(
        content=ft.Text(""),
        bgcolor=ft.Colors.RED_300,
        open=False,
        duration=3000
    )

    username = ft.TextField(label="Digite tu usuario", color=ft.Colors.BLACK)
    password = ft.TextField(label="Digite tu contraseña", color=ft.Colors.BLACK, password=True)

    def _validate(e):
        user_value = username.value.strip()
        pass_value = password.value.strip()

        try:
            user = User.get(
                (User.username == user_value) &
                (User.password == pass_value)
            )
            print("✅ Login correcto")
            page.snack_bar.open = False
            page.go("/home")

        except User.DoesNotExist:
            print("❌ Usuario o contraseña incorrectos")
            page.snack_bar.content = ft.Text("Credenciales inválidas")
            page.snack_bar.open = True
            page.update()

    btn_login = Button(
        "Iniciar Sesion",
        color=ft.Colors.BLUE_ACCENT_700,
        onclick=_validate,
        height=50,
        width=160,
    ).get()

    return ft.View(
        "/login",
        bgcolor=ft.Colors.BLUE_800,
        controls=[
            data,
            ft.Container(
                width=320,
                height=320,
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                padding=20,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Text("📊 Login", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                        username,
                        password,
                        btn_login,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
