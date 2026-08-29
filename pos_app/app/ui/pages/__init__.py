"""Pages — one QWidget subclass per sidebar section, each in its own file.

The registry below is the single source of truth that the main window uses
to build the stacked content area. Keys MUST match ``NAV_ITEMS`` in
``app/config.py``.

TODO(next steps): fill each page with its real widgets (tables, forms,
charts ...) working on the local SQLite database.
"""

from __future__ import annotations

from PyQt6.QtWidgets import QWidget

from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.debts_page import DebtsPage
from app.ui.pages.reports_page import ReportsPage
from app.ui.pages.returns_page import ReturnsPage
from app.ui.pages.sales_history_page import SalesHistoryPage
from app.ui.pages.sales_page import SalesPage
from app.ui.pages.settings_page import SettingsPage
from app.ui.pages.suppliers_page import SuppliersPage

PAGE_CLASSES: dict[str, type[QWidget]] = {
    "dashboard": DashboardPage,
    "sales": SalesPage,
    "sales_history": SalesHistoryPage,
    "debts": DebtsPage,
    "suppliers": SuppliersPage,
    "returns": ReturnsPage,
    "reports": ReportsPage,
    "settings": SettingsPage,
}

__all__ = ["PAGE_CLASSES"]