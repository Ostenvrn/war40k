"""
War40k — текстовая RPG по вселенной Warhammer 40,000.
Точка входа приложения.
"""

import flet as ft
from core.constants import (
    GAME_NAME, GAME_VERSION, GAME_AUTHOR,
    COLOR_BG_DARK, COLOR_TEXT_MAIN, COLOR_TEXT_DIM, COLOR_TEXT_ACCENT,
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT
)


def main(page: ft.Page) -> None:
    """Главная функция приложения."""

    # ============================================================
    # НАСТРОЙКИ ОКНА
    # ============================================================
    page.title = f"{GAME_NAME} v{GAME_VERSION}"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = COLOR_BG_DARK
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.min_width = WINDOW_MIN_WIDTH
    page.window.min_height = WINDOW_MIN_HEIGHT
    page.padding = 20

    # ============================================================
    # ГЛАВНОЕ МЕНЮ
    # ============================================================
    def show_main_menu() -> None:
        """Показывает главное меню."""
        page.controls.clear()

        # --- Центральный блок с заголовком и кнопками ---
        menu_column = ft.Column(
            controls=[
                ft.Text(
                    GAME_NAME,
                    size=64,
                    weight=ft.FontWeight.BOLD,
                    color=COLOR_TEXT_ACCENT,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "В 41-м тысячелетии есть только война.",
                    size=16,
                    italic=True,
                    color=COLOR_TEXT_DIM,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    f"v{GAME_VERSION} | {GAME_AUTHOR}",
                    size=12,
                    color=COLOR_TEXT_DIM,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=40),
                ft.Button(
                    content="Новая игра",
                    width=300,
                    height=50,
                    bgcolor=COLOR_TEXT_ACCENT,
                    color=COLOR_BG_DARK,
                    on_click=lambda e: print("Новая игра — TODO"),
                ),
                ft.Container(height=10),
                ft.Button(
                    content="Загрузка",
                    width=300,
                    height=50,
                    bgcolor="#2A2A2A",
                    color=COLOR_TEXT_MAIN,
                    on_click=lambda e: print("Загрузка — TODO"),
                ),
                ft.Container(height=10),
                ft.Button(
                    content="Настройки",
                    width=300,
                    height=50,
                    bgcolor="#2A2A2A",
                    color=COLOR_TEXT_MAIN,
                    on_click=lambda e: print("Настройки — TODO"),
                ),
                ft.Container(height=10),
                ft.Button(
                    content="Выход",
                    width=300,
                    height=50,
                    bgcolor="#2A2A2A",
                    color=COLOR_TEXT_MAIN,
                    on_click=lambda e: page.window.close(),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )

        # --- Символы по бокам ---
        # Используем Alignment.CENTER (новый API)
        imperium_icon = ft.Icon(
            icon=ft.Icons.SHIELD,  # Заглушка
            size=120,
            color=COLOR_TEXT_ACCENT,
        )
        chaos_icon = ft.Icon(
            icon=ft.Icons.BRIGHTNESS_7,  # Заглушка
            size=120,
            color=COLOR_TEXT_ACCENT,
        )

        # --- Главный ряд: символ, меню, символ ---
        main_row = ft.Row(
            controls=[
                ft.Container(
                    content=imperium_icon,
                    expand=True,
                    alignment=ft.Alignment.CENTER,  # ← ИСПРАВЛЕНО
                ),
                menu_column,
                ft.Container(
                    content=chaos_icon,
                    expand=True,
                    alignment=ft.Alignment.CENTER,  # ← ИСПРАВЛЕНО
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

        page.add(main_row)
        page.update()

    # ============================================================
    # ЗАПУСК
    # ============================================================
    show_main_menu()


if __name__ == "__main__":
    ft.run(main)
