"""Sales History page — list and search of past invoices."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class SalesHistoryPage(BasePage):
    """Sales history.

    TODO(next steps):
      - Table of invoices (number, date, cashier, total, payment method)
      - Filters: by date range, cashier, payment method
      - View invoice details / reprint a receipt
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="sales_history", parent=parent)