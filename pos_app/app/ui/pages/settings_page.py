"""Settings page — application configuration."""

from __future__ import annotations

import typing as t

from PyQt6.QtWidgets import QWidget

from app.ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    """Settings.

    TODO(next steps):
      - Shop information (name, address, phone, receipt header)
      - Currency, tax rate, receipt printer options
      - Cashiers/users management (add, disable, change password)
      - Database backup / restore
    """

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(title_key="settings", parent=parent)