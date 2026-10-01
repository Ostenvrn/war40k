"""
Экран пролога.
Отображает сцены, выборы и последствия в стиле Warhammer.
"""

import flet as ft

from ui import theme


class PrologueScreen:
    """Экран пролога."""

    def __init__(self, page: ft.Page, on_finish=None):
        self.page = page
        self.on_finish = on_finish
        self.origin = "Улей"
        self.name = "Безымянный"
        self.flags = {}

    def set_character(self, name: str, origin: str) -> None:
        self.name = name
        self.origin = origin

    def show(self) -> None:
        from data.prologue import get_scene_1

        scene = get_scene_1(self.origin)
        self._show_scene(scene)

    def _show_scene(self, scene: dict) -> None:
        self.page.controls.clear()

        # --- Имя персонажа ---
        char_info = ft.Text(
            f"{self.name} | {self.origin}",
            size=14,
            italic=True,
            color=theme.TEXT_DIM,
            text_align=ft.TextAlign.CENTER,
        )

        # --- Текст сцены (в рамке-пергаменте) ---
        text_content = ft.Text(
            scene["text"],
            size=15,
            color=theme.TEXT_MAIN,
            text_align=ft.TextAlign.LEFT,
            selectable=True,
            font_family=theme.FONT_BODY,
        )

        text_frame = theme.create_frame(
            content=text_content,
            width=850,
            padding=30,
        )

        # --- Кнопки выбора ---
        choice_buttons = []
        for choice in scene["choices"]:
            btn = ft.Button(
                content=ft.Text(choice["text"], size=14),
                width=850,
                height=50,
                bgcolor=theme.BG_CARD,
                color=theme.TEXT_MAIN,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=2),
                    side=ft.BorderSide(1, theme.TEXT_ACCENT),
                ),
                on_click=lambda e, c=choice: self._on_choice(c),
            )
            choice_buttons.append(btn)

        # --- Сборка ---
        content = ft.Column(
            controls=[
                ft.Container(height=20),
                theme.create_header("ПРОЛОГ", size=32),
                ft.Container(height=5),
                char_info,
                ft.Container(height=20),
                theme.create_divider(),
                ft.Container(height=20),
                text_frame,
                ft.Container(height=30),
                *choice_buttons,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

        self.page.add(content)
        self.page.update()

    def _on_choice(self, choice: dict) -> None:
        tag = choice.get("tag", "")
        consequence = choice.get("consequence", "")

        print(f"[Пролог] Выбор: {choice['text']} | Тег: {tag}")
        print(f"[Пролог] Последствие: {consequence}")

        self.flags[tag] = True

        if self.on_finish:
            self.on_finish()
