"""Debts page — customer credits/installments tracking."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class DebtsPage(BasePage):
    """Debts (money owed to the shop by customers).

    TODO(next steps):
      - Customers list with total debt per customer
      - Add / settle a debt entry linked to invoices
      - Overdue reminders and simple debt report
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="debts", parent=parent)