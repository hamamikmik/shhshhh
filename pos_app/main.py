"""Point of Sale (POS) — base skeleton entry point.

Run from this directory (pos_app/):

    python main.py

Flow: LoginWindow → on success → MainWindow (sidebar + stacked pages).
"""

from __future__ import annotations

import sys
import typing as t

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

from app.config import FONT_FAMILIES, STYLESHEET, tr
from app.ui.login_window import LoginWindow
from app.ui.main_window import MainWindow


def _apply_global_appearance(app: QApplication) -> None:
    """Apply the global stylesheet and a preferred font to the whole app."""
    font = QFont()
    font.setFamilies(list(FONT_FAMILIES))
    font.setPointSize(10)
    app.setFont(font)
    app.setStyleSheet(STYLESHEET)


def main() -> int:
    """Entry point: show the login window; open the main window on success."""
    app = QApplication(sys.argv)
    app.setApplicationName(tr("app_name"))
    _apply_global_appearance(app)

    login = LoginWindow()
    main_window: t.Optional[MainWindow] = None

    def _open_main_window(username: str) -> None:
        """Callback once the login succeeds: open the main window and close
        the login window. The app exits when the last window closes."""
        nonlocal main_window
        main_window = MainWindow(username=username)
        main_window.show()
        login.close()

    login.login_succeeded.connect(_open_main_window)
    login.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())