"""Returns page — returned items / refunds."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class ReturnsPage(BasePage):
    """Returns (items returned by customers / refunds).

    TODO(next steps):
      - Search an invoice and mark items as returned
      - Refund handling (cash back or balance to the customer)
      - Returns history list
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="returns", parent=parent)