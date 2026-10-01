"""
War40k — текстовая RPG по вселенной Warhammer 40,000.
Точка входа приложения.
"""

import flet as ft

from core.constants import (
    COLOR_BG_DARK,
    COLOR_TEXT_ACCENT,
    COLOR_TEXT_DIM,
    COLOR_TEXT_MAIN,
    GAME_AUTHOR,
    GAME_NAME,
    GAME_VERSION,
    WINDOW_HEIGHT,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_WIDTH,
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
    # ЭКРАН: ГЛАВНОЕ МЕНЮ
    # ============================================================
    def show_main_menu() -> None:
        """Показывает главное меню."""
        page.controls.clear()

        # --- Кнопки ---
        def on_new_game(e):
            """Переход к созданию персонажа."""
            show_character_creation()

        def on_load_game(e):
            print("Загрузка — TODO")

        def on_settings(e):
            print("Настройки — TODO")

        def on_exit(e):
            page.window.close()

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
                    on_click=on_new_game,
                ),
                ft.Container(height=10),
                ft.Button(
                    content="Загрузка",
                    width=300,
                    height=50,
                    bgcolor="#2A2A2A",
                    color=COLOR_TEXT_MAIN,
                    on_click=on_load_game,
                ),
                ft.Container(height=10),
                ft.Button(
                    content="Настройки",
                    width=300,
                    height=50,
                    bgcolor="#2A2A2A",
                    color=COLOR_TEXT_MAIN,
                    on_click=on_settings,
                ),
                ft.Container(height=10),
                ft.Button(
                    content="Выход",
                    width=300,
                    height=50,
                    bgcolor="#2A2A2A",
                    color=COLOR_TEXT_MAIN,
                    on_click=on_exit,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )

        imperium_icon = ft.Icon(icon=ft.Icons.SHIELD, size=120, color=COLOR_TEXT_ACCENT)
        chaos_icon = ft.Icon(icon=ft.Icons.BRIGHTNESS_7, size=120, color=COLOR_TEXT_ACCENT)

        main_row = ft.Row(
            controls=[
                ft.Container(content=imperium_icon, expand=True, alignment=ft.Alignment.CENTER),
                menu_column,
                ft.Container(content=chaos_icon, expand=True, alignment=ft.Alignment.CENTER),
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
        """Экран создания персонажа: имя + происхождение."""
        page.controls.clear()

        name_input = ft.TextField(
            label="Имя персонажа",
            hint_text="Введите имя (русское или английское)",
            width=400,
            bgcolor="#1A1A1A",
            border_color=COLOR_TEXT_ACCENT,
            color=COLOR_TEXT_MAIN,
            label_style=ft.TextStyle(color=COLOR_TEXT_DIM),
        )

        origin_dropdown = ft.Dropdown(
            label="Происхождение",
            width=400,
            bgcolor="#1A1A1A",
            border_color=COLOR_TEXT_ACCENT,
            color=COLOR_TEXT_MAIN,
            label_style=ft.TextStyle(color=COLOR_TEXT_DIM),
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

        status_text = ft.Text("", color=COLOR_TEXT_DIM, size=12)

        def on_start(e):
            """Запуск игры после создания персонажа."""
            name = name_input.value.strip()
            if not name:
                status_text.value = "Введите имя!"
                status_text.color = "#DC143C"
                page.update()
                return
            status_text.value = f"Персонаж: {name} | Происхождение: {origin_dropdown.value}. Начинаем..."
            status_text.color = "#228B22"
            page.update()
            # TODO: переход к прологу
            print(f"Игра начата: {name}, {origin_dropdown.value}")

        def on_back(e):
            show_main_menu()

        content = ft.Column(
            controls=[
                ft.Container(height=40),
                ft.Text(
                    "СОЗДАНИЕ ПЕРСОНАЖА",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=COLOR_TEXT_ACCENT,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=30),
                name_input,
                ft.Container(height=20),
                origin_dropdown,
                ft.Container(height=20),
                ft.Button(
                    content="Начать путь",
                    width=400,
                    height=50,
                    bgcolor=COLOR_TEXT_ACCENT,
                    color=COLOR_BG_DARK,
                    on_click=on_start,
                ),
                ft.Container(height=10),
                ft.Button(
                    content="Назад",
                    width=400,
                    height=40,
                    bgcolor="#2A2A2A",
                    color=COLOR_TEXT_MAIN,
                    on_click=on_back,
                ),
                ft.Container(height=10),
                status_text,
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
