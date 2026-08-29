"""Sidebar — the navigation menu of the main window.

Structure (top to bottom):

    1. App brand (name + subtitle)
    2. One checkable button per section in ``NAV_ITEMS``
    3. Stretch (pushes everything below to the bottom)
    4. Live clock (date + time, refreshes every second)
"""

from __future__ import annotations

import typing as t

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QButtonGroup, QLabel, QPushButton, QVBoxLayout, QWidget

from app.config import APP_VERSION, LANGUAGE, NAV_ITEMS, tr
from app.utils.clock import ClockWidget


class Sidebar(QWidget):
    """Vertical navigation bar shown on the left side of the main window.

    Signals:
        page_selected(str): emitted with the navigation key of the clicked
            menu button (e.g. "sales"). The main window switches the
            QStackedWidget to the matching page.
    """

    page_selected = pyqtSignal(str)

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setObjectName("sidebar")
        self.setFixedWidth(240)

        root = QVBoxLayout(self)
        root.setContentsMargins(12, 20, 12, 16)
        root.setSpacing(6)

        # --- brand -------------------------------------------------------
        self.brand_label = QLabel(tr("app_name"), self)
        self.brand_label.setObjectName("brand")

        self.subtitle_label = QLabel(f"{APP_VERSION} · {tr('subtitle')}", self)
        self.subtitle_label.setObjectName("brandSub")

        root.addWidget(self.brand_label)
        root.addWidget(self.subtitle_label)
        root.addSpacing(14)

        # --- navigation buttons ------------------------------------------
        self._group = QButtonGroup(self)
        self._group.setExclusive(True)  # only one highlighted item at a time

        self._buttons: dict[str, QPushButton] = {}
        for key in NAV_ITEMS:
            button = QPushButton(tr(key), self)
            button.setObjectName("navButton")
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            # `k=key` fixes Python's late-binding closure problem.
            button.clicked.connect(lambda _checked, k=key: self.page_selected.emit(k))
            self._group.addButton(button)
            self._buttons[key] = button
            root.addWidget(button)

        # --- clock at the bottom ------------------------------------------
        root.addStretch(1)

        self.clock = ClockWidget(language=LANGUAGE, parent=self)
        self.clock.setObjectName("clock")
        root.addWidget(self.clock)

    # ------------------------------------------------------------------ API
    def buttons(self) -> dict[str, QPushButton]:
        """Return the menu buttons keyed by navigation key."""
        return self._buttons

    def set_active(self, key: str) -> None:
        """Highlight the menu button matching ``key``.

        The exclusive QButtonGroup keeps the previously active button
        unchecked automatically.
        """
        button = self._buttons.get(key)
        if button is not None:
            button.setChecked(True)

    def stop_clock(self) -> None:
        """Stop the live clock (call from the main window closeEvent)."""
        self.clock.stop()