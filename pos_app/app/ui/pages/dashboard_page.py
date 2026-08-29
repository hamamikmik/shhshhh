"""Dashboard page — landing page after login."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class DashboardPage(BasePage):
    """Dashboard.

    TODO(next steps):
      - Today's sales total, number of invoices, average basket
      - Low-stock alerts / expiring products
      - Quick actions (new sale, add product, ...)
      - Maybe a simple chart of the last 7/30 days
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="dashboard", parent=parent)