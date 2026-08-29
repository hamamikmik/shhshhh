"""Reports page — daily/weekly/monthly statistics."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class ReportsPage(BasePage):
    """Reports.

    TODO(next steps):
      - Daily / weekly / monthly sales summary
      - Best-selling products, payment method split
      - Export to CSV / PDF
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="reports", parent=parent)