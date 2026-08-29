"""Suppliers page — supplier directory and restocking data."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class SuppliersPage(BasePage):
    """Suppliers.

    TODO(next steps):
      - Supplier CRUD (name, phone, address, notes)
      - Purchases from suppliers / restocking
      - What the shop owes each supplier
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="suppliers", parent=parent)