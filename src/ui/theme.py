"""
Тема и стили для War40k.
Цвета, шрифты, градиенты, декоративные элементы.
"""

import flet as ft

# ============================================================
# ЦВЕТА (палитра Warhammer 40,000)
# ============================================================
BG_DARK = "#0A0A0A"
BG_PANEL = "#141414"
BG_CARD = "#1E1E1E"
BG_CARD_HOVER = "#2A2A2A"

TEXT_MAIN = "#D4C5A9"
TEXT_DIM = "#7A6F5F"
TEXT_ACCENT = "#C9A227"
TEXT_DANGER = "#8B0000"

IMPERIUM = "#C9A227"
CHAOS = "#8B0000"
MECHANICUS = "#B22222"
INQUISITION = "#4B0082"
XENOS = "#00FF7F"
NEUTRAL = "#7A7A7A"

SUCCESS = "#228B22"
WARNING = "#FF8C00"
DANGER = "#DC143C"
CORRUPTION = "#800080"

# ============================================================
# ШРИФТЫ
# ============================================================
FONT_HEADER = "Cinzel"
FONT_BODY = "Georgia"
FONT_MONO = "Consolas"

# ============================================================
# СТИЛИ КОМПОНЕНТОВ
# ============================================================
STYLE_BUTTON = {
    "width": 320,
    "height": 55,
    "bgcolor": BG_CARD,
    "color": TEXT_MAIN,
    "style": ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=2),
        side=ft.BorderSide(1, TEXT_ACCENT),
    ),
}

STYLE_BUTTON_PRIMARY = {
    "width": 320,
    "height": 55,
    "bgcolor": TEXT_ACCENT,
    "color": BG_DARK,
    "style": ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=2),
        side=ft.BorderSide(2, "#8B7020"),
    ),
}

STYLE_TEXT_FIELD = {
    "width": 420,
    "bgcolor": BG_CARD,
    "border_color": TEXT_ACCENT,
    "color": TEXT_MAIN,
    "border_radius": 2,
    "filled": True,
}

STYLE_DROPDOWN = {
    "width": 420,
    "bgcolor": BG_CARD,
    "border_color": TEXT_ACCENT,
    "color": TEXT_MAIN,
    "border_radius": 2,
    "filled": True,
}

# ============================================================
# ДЕКОРАТИВНЫЕ ЭЛЕМЕНТЫ
# ============================================================
def create_frame(
    content: ft.Control,
    width: int | None = None,
    padding: int = 20,
) -> ft.Container:
    """Создаёт рамку в стиле Warhammer (пергамент/металл)."""
    return ft.Container(
        content=content,
        width=width,
        padding=padding,
        bgcolor=BG_PANEL,
        border=ft.Border.all(2, TEXT_ACCENT),  # ← ИСПРАВЛЕНО
        border_radius=2,
    )


def create_divider() -> ft.Divider:
    """Декоративный разделитель с золотым оттенком."""
    return ft.Divider(height=2, color=TEXT_ACCENT)


def create_header(text: str, size: int = 32) -> ft.Text:
    """Заголовок в стиле Warhammer."""
    return ft.Text(
        text,
        size=size,
        weight=ft.FontWeight.BOLD,
        color=TEXT_ACCENT,
        text_align=ft.TextAlign.CENTER,
        font_family=FONT_HEADER,
    )


def create_body_text(text: str, size: int = 14) -> ft.Text:
    """Текст в стиле пергамента."""
    return ft.Text(
        text,
        size=size,
        color=TEXT_MAIN,
        text_align=ft.TextAlign.LEFT,
        selectable=True,
        font_family=FONT_BODY,
    )
