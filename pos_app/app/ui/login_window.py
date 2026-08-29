"""Login window — placeholder authentication for the cashier/seller user."""

from __future__ import annotations

import typing as t

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QDialog,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.config import PLACEHOLDER_PASSWORD, PLACEHOLDER_USERNAME, tr


class LoginWindow(QDialog):
    """Login screen (username + password).

    Signals:
        login_succeeded(str): emitted with the username after a successful
            login. ``main.py`` connects this to opening the main window.

    TODO(next steps): replace the hardcoded ``admin / admin`` check with real
    authentication against the local database (users table, hashed/salted
    passwords, session handling, password change in Settings, ...).
    """

    login_succeeded = pyqtSignal(str)

    def __init__(self, parent: t.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setObjectName("loginRoot")
        self.setWindowTitle(tr("login_title"))
        self.setFixedSize(440, 560)

        # ------------------------------------------------------------------
        # Centered white card over a dark background
        # ------------------------------------------------------------------
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame(self)
        card.setObjectName("loginCard")
        card.setFixedWidth(370)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(32, 36, 32, 30)
        card_layout.setSpacing(12)

        self.title_label = QLabel(tr("login_title"), card)
        self.title_label.setObjectName("loginTitle")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitle_label = QLabel(tr("subtitle"), card)
        self.subtitle_label.setObjectName("loginSub")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_layout.addWidget(self.title_label)
        card_layout.addWidget(self.subtitle_label)
        card_layout.addSpacing(10)

        # --- username -------------------------------------------------
        self.username_caption = QLabel(tr("username"), card)
        self.username_caption.setObjectName("fieldLabel")

        self.username_input = QLineEdit(card)
        self.username_input.setPlaceholderText(tr("username"))
        self.username_input.setClearButtonEnabled(True)

        card_layout.addWidget(self.username_caption)
        card_layout.addWidget(self.username_input)

        # --- password -------------------------------------------------
        self.password_caption = QLabel(tr("password"), card)
        self.password_caption.setObjectName("fieldLabel")

        self.password_input = QLineEdit(card)
        self.password_input.setPlaceholderText(tr("password"))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        # NOTE: no returnPressed handler here on purpose — the login button
        # is the dialog's default button (setDefault below), so Qt already
        # triggers it when the user presses Enter inside this dialog.

        card_layout.addWidget(self.password_caption)
        card_layout.addWidget(self.password_input)

        # --- error / hint area (always visible to avoid layout jumps) --
        self.error_label = QLabel("", card)
        self.error_label.setObjectName("errorLabel")
        self.error_label.setWordWrap(True)
        self.error_label.setMinimumHeight(20)

        self.login_button = QPushButton(tr("login_button"), card)
        self.login_button.setObjectName("primaryButton")
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.setDefault(True)  # activates on Enter
        self.login_button.setMinimumHeight(44)
        self.login_button.clicked.connect(self._on_login_clicked)

        self.hint_label = QLabel(tr("hint_credentials"), card)
        self.hint_label.setObjectName("hintLabel")
        self.hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_layout.addWidget(self.error_label)
        card_layout.addSpacing(4)
        card_layout.addWidget(self.login_button)
        card_layout.addSpacing(8)
        card_layout.addWidget(self.hint_label)

        root.addWidget(card)

        # TODO(next steps): add a tooltip/note mentioning the placeholder
        # credentials, or make them configurable via a first-run setup.

    # ------------------------------------------------------------------ API
    def username(self) -> str:
        """Return the trimmed username entered by the user."""
        return self.username_input.text().strip()

    # ------------------------------------------------------------- actions
    def _on_login_clicked(self) -> None:
        """Validate the input and either emit ``login_succeeded`` or show an
        inline error. This is *placeholder* validation only — no security. """
        username = self.username_input.text().strip()
        password = self.password_input.text()

        if not username or not password:
            self._show_error(tr("error_required"))
            return

        if username == PLACEHOLDER_USERNAME and password == PLACEHOLDER_PASSWORD:
            self._show_error("")
            self.login_succeeded.emit(username)
        else:
            self._show_error(tr("error_invalid"))

    def _show_error(self, message: str) -> None:
        """Display or clear the inline error message."""
        self.error_label.setText(message)