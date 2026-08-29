"""Main window — sidebar navigation + stacked content area."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QStackedWidget, QWidget

from app.config import NAV_ITEMS, tr
from app.ui.pages import PAGE_CLASSES
from app.ui.sidebar import Sidebar


class MainWindow(QMainWindow):
    """Main application window shown after a successful login.

    Layout:

        ┌────────────┬──────────────────────────────────┐
        │  Sidebar   │   QStackedWidget (content area)  │
        │  (menu +   │   one page per section           │
        │   clock)   │                                  │
        └────────────┴──────────────────────────────────┘

    TODO(next steps): sales flow, database and per-section business logic;
    the stacked pages will be filled section by section.
    """

    def __init__(self, username: str, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._username = username

        # Safety check: every sidebar item must have a page class.
        leftover = set(NAV_ITEMS) - set(PAGE_CLASSES)
        if leftover:
            raise RuntimeError(f"Missing page class(es) for: {sorted(leftover)}")

        self.setWindowTitle(f"{tr('app_name')} — {username}")
        self.resize(1200, 760)
        self.setMinimumSize(960, 620)

        # ----------------------------------------------------------------
        # Central widget: sidebar | stacked pages
        # ----------------------------------------------------------------
        central = QWidget(self)
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar(central)

        self.stack = QStackedWidget(central)
        self.stack.setObjectName("content")

        # One page instance per navigation key (order == NAV_ITEMS order
        # is guaranteed by the dict definition in app.ui.pages).
        self.pages: dict[str, QWidget] = {}
        for key, page_class in PAGE_CLASSES.items():
            page = page_class(self.stack)
            self.pages[key] = page
            self.stack.addWidget(page)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack, 1)
        self.setCentralWidget(central)

        # ----------------------------------------------------------------
        # Wire navigation
        # ----------------------------------------------------------------
        self.sidebar.page_selected.connect(self.show_page)
        self.go_to("dashboard")  # landing page after login

        self.statusBar().showMessage(tr("status_cashier").format(name=username))

    # ------------------------------------------------------------------ API
    def show_page(self, key: str) -> None:
        """Switch the stacked content area to the page for ``key``.

        ``key`` is one of the strings in ``NAV_ITEMS`` (e.g. "sales").
        """
        page = self.pages.get(key)
        if page is not None:
            self.stack.setCurrentWidget(page)

    def go_to(self, key: str) -> None:
        """Select the sidebar button for ``key`` and show its page.

        Used both at startup and by any future code that needs to navigate
        programmatically (e.g. after finishing a sale, jump to Sales History).
        """
        self.sidebar.set_active(key)
        self.show_page(key)

    # ------------------------------------------------------------- events
    def closeEvent(self, event) -> None:  # noqa: N802 - Qt naming
        """Clean shutdown: stop the live clock before closing."""
        self.sidebar.stop_clock()
        super().closeEvent(event)