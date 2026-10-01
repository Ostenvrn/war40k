"""
War40k — текстовая RPG по вселенной Warhammer 40,000.
Точка входа приложения.
"""

import flet as ft

from core.constants import (
    GAME_AUTHOR,
    GAME_NAME,
    GAME_VERSION,
    WINDOW_HEIGHT,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_WIDTH,
)
from ui import theme


def main(page: ft.Page) -> None:
    """Главная функция приложения."""

    # ============================================================
    # НАСТРОЙКИ ОКНА
    # ============================================================
    page.title = f"{GAME_NAME} v{GAME_VERSION}"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = theme.BG_DARK
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.min_width = WINDOW_MIN_WIDTH
    page.window.min_height = WINDOW_MIN_HEIGHT
    page.padding = 20

    # ============================================================
    # ЭКРАН: ГЛАВНОЕ МЕНЮ
    # ============================================================
    def show_main_menu() -> None:
        page.controls.clear()

        def on_new_game(e):
            show_character_creation()

        def on_load_game(e):
            print("Загрузка — TODO")

        def on_settings(e):
            print("Настройки — TODO")

        def on_exit(e):
            page.window.close()

        title = ft.Text(
            "WAR40K",
            size=72,
            weight=ft.FontWeight.BOLD,
            color=theme.TEXT_ACCENT,
            text_align=ft.TextAlign.CENTER,
        )

        subtitle = ft.Text(
            "В 41-м тысячелетии есть только война.",
            size=16,
            italic=True,
            color=theme.TEXT_DIM,
            text_align=ft.TextAlign.CENTER,
        )

        version = ft.Text(
            f"v{GAME_VERSION} | {GAME_AUTHOR}",
            size=12,
            color=theme.TEXT_DIM,
            text_align=ft.TextAlign.CENTER,
        )

        divider = ft.Container(
            width=400,
            height=2,
            bgcolor=theme.TEXT_ACCENT,
            margin=ft.Margin.symmetric(vertical=20),  # ← ИСПРАВЛЕНО
        )

        btn_new = ft.Button(
            content=ft.Text("НОВАЯ ИГРА", size=16, weight=ft.FontWeight.BOLD),
            **theme.STYLE_BUTTON_PRIMARY,
            on_click=on_new_game,
        )
        btn_load = ft.Button(
            content=ft.Text("ЗАГРУЗКА", size=16),
            **theme.STYLE_BUTTON,
            on_click=on_load_game,
        )
        btn_settings = ft.Button(
            content=ft.Text("НАСТРОЙКИ", size=16),
            **theme.STYLE_BUTTON,
            on_click=on_settings,
        )
        btn_exit = ft.Button(
            content=ft.Text("ВЫХОД", size=16),
            **theme.STYLE_BUTTON,
            on_click=on_exit,
        )

        menu_column = ft.Column(
            controls=[
                title,
                subtitle,
                ft.Container(height=5),
                version,
                divider,
                btn_new,
                ft.Container(height=12),
                btn_load,
                ft.Container(height=12),
                btn_settings,
                ft.Container(height=12),
                btn_exit,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )

        imperium_icon = ft.Icon(
            icon=ft.Icons.SHIELD,
            size=160,
            color=theme.IMPERIUM,
        )
        chaos_icon = ft.Icon(
            icon=ft.Icons.BRIGHTNESS_7,
            size=160,
            color=theme.CHAOS,
        )

        main_row = ft.Row(
            controls=[
                ft.Container(
                    content=imperium_icon,
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                ),
                menu_column,
                ft.Container(
                    content=chaos_icon,
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

        page.add(main_row)
        page.update()

    # ============================================================
    # ЭКРАН: СОЗДАНИЕ ПЕРСОНАЖА
    # ============================================================
    def show_character_creation() -> None:
        page.controls.clear()

        name_input = ft.TextField(
            label="Имя персонажа",
            hint_text="Введите имя",
            **theme.STYLE_TEXT_FIELD,
            label_style=ft.TextStyle(color=theme.TEXT_DIM),
        )

        origin_dropdown = ft.Dropdown(
            label="Происхождение",
            **theme.STYLE_DROPDOWN,
            label_style=ft.TextStyle(color=theme.TEXT_DIM),
            options=[
                ft.dropdown.Option("Улей"),
                ft.dropdown.Option("Корабль торговца"),
                ft.dropdown.Option("Кадия"),
                ft.dropdown.Option("Мир-кузня"),
                ft.dropdown.Option("Фенрис"),
                ft.dropdown.Option("Ноктюрн"),
                ft.dropdown.Option("Ваал"),
            ],
            value="Улей",
        )

        status_text = ft.Text("", color=theme.TEXT_DIM, size=12)

        def on_start(e):
            name = name_input.value.strip()
            if not name:
                status_text.value = "Введите имя!"
                status_text.color = theme.DANGER
                page.update()
                return

            from ui.screens.prologue import PrologueScreen
            prologue = PrologueScreen(
                page,
                on_finish=lambda: print("[Пролог] Завершён"),
            )
            prologue.set_character(name, origin_dropdown.value)
            prologue.show()

        def on_back(e):
            show_main_menu()

        form_frame = theme.create_frame(
            content=ft.Column(
                controls=[
                    name_input,
                    ft.Container(height=15),
                    origin_dropdown,
                    ft.Container(height=25),
                    ft.Button(
                        content=ft.Text("НАЧАТЬ ПУТЬ", size=16, weight=ft.FontWeight.BOLD),
                        **theme.STYLE_BUTTON_PRIMARY,
                        on_click=on_start,
                    ),
                    ft.Container(height=12),
                    ft.Button(
                        content=ft.Text("НАЗАД", size=14),
                        **theme.STYLE_BUTTON,
                        on_click=on_back,
                    ),
                    ft.Container(height=10),
                    status_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            ),
            width=520,
            padding=30,
        )

        content = ft.Column(
            controls=[
                ft.Container(height=30),
                theme.create_header("СОЗДАНИЕ ПЕРСОНАЖА", size=28),
                ft.Container(height=30),
                form_frame,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )

        page.add(content)
        page.update()

    # ============================================================
    # ЗАПУСК
    # ============================================================
    show_main_menu()


if __name__ == "__main__":
    ft.run(main)
