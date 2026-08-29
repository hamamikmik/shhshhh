"""BasePage — shared shell for every content page (DRY).

Every concrete page (DashboardPage, SalesPage, ...) inherits from this class,
so the big title label, margins and the placeholder card are defined only
once. Real content will be added below the title, inside the same layout.
"""

from __future__ import annotations

import typing as t

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget

from app.config import tr


class BasePage(QWidget):
    """Common page shell: large title at the top, content area below.

    Subclasses only pass their own ``title_key``; later steps can attach
    real widgets to ``self.content_layout`` (and hide/remove
    ``self.placeholder_label`` when they do).
    """

    def __init__(self, title_key: str, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(parent)

        root = QVBoxLayout(self)
        root.setContentsMargins(28, 28, 28, 28)
        root.setSpacing(16)

        # Big page title (styling via #pageTitle in config.STYLESHEET).
        self.title_label = QLabel(tr(title_key), self)
        self.title_label.setObjectName("pageTitle")
        root.addWidget(self.title_label)

        # Placeholder card — to be replaced/augmented by real content.
        self.placeholder_card = QFrame(self)
        self.placeholder_card.setObjectName("placeholderCard")

        self.content_layout = QVBoxLayout(self.placeholder_card)
        self.content_layout.setContentsMargins(24, 24, 24, 24)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.placeholder_label = QLabel(tr("placeholder_text"), self.placeholder_card)
        self.placeholder_label.setObjectName("placeholderText")
        self.placeholder_label.setWordWrap(True)
        self.placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.content_layout.addWidget(self.placeholder_label)
        root.addWidget(self.placeholder_card, 1)  # card stretches to fill