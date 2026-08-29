"""Sales page — the cashier's main working screen."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class SalesPage(BasePage):
    """Sales (new invoice).

    TODO(next steps):
      - Product search box + barcode scanner input
      - Cart table (items, quantity, price, subtotal)
      - Totals (subtotal, discount, tax, net) and payment methods
      - Save invoice to the database and print/export the receipt
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="sales", parent=parent)