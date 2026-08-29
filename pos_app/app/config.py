"""Central configuration for the POS application.

Everything that is likely to change (navigation items, UI language, the
placeholder login credentials, colors and the global stylesheet) lives here
so the rest of the codebase stays clean and modular.
"""

from __future__ import annotations

import typing as t

# ---------------------------------------------------------------------------
# Application metadata
# ---------------------------------------------------------------------------
APP_NAME: str = "Point of Sale System"      # used for English window titles
APP_VERSION: str = "0.1.0"

# Preferred UI language. Options:
#   "ku"  -> Kurdish (Sorani) labels   (default)
#   "en"  -> English labels
LANGUAGE: str = "ku"

# Font families used by the app (first available one is preferred).
# An Arabic-capable font is needed for Kurdish/Sorani text.
FONT_FAMILIES: t.Sequence[str] = (
    "Segoe UI",
    "Noto Sans Arabic",
    "Noto Sans",
    "Tahoma",
    "DejaVu Sans",
)

# ---------------------------------------------------------------------------
# Placeholder authentication (STEP 1 only)
# ---------------------------------------------------------------------------
# TODO(next steps): replace with real authentication against the local
# database (users table + hashed passwords). These constants only exist so
# the login flow can be tested until then.
PLACEHOLDER_USERNAME: str = "admin"
PLACEHOLDER_PASSWORD: str = "admin"

# ---------------------------------------------------------------------------
# Navigation — keys must match the keys of PAGE_CLASSES in app/ui/pages.
# ---------------------------------------------------------------------------
NAV_ITEMS: t.Sequence[str] = (
    "dashboard",
    "sales",
    "sales_history",
    "debts",
    "suppliers",
    "returns",
    "reports",
    "settings",
)

# ---------------------------------------------------------------------------
# UI strings (simple dictionary-based localization)
# ---------------------------------------------------------------------------
UI_LABELS: dict[str, dict[str, str]] = {
    # Login / generic
    "app_name": {
        "en": "Point of Sale System",
        "ku": "سیستەمی فرۆشتن",
    },
    "subtitle": {
        "en": "Local · offline cashier",
        "ku": "کاشێری ناوخۆیی · بێ ئینتەرنێت",
    },
    "login_title": {
        "en": "Cashier Login",
        "ku": "چوونەژوورەوەی فرۆشیار",
    },
    "username": {
        "en": "Username",
        "ku": "ناوی بەکارهێنەر",
    },
    "password": {
        "en": "Password",
        "ku": "وشەی نهێنی",
    },
    "login_button": {
        "en": "Login",
        "ku": "چوونەژوورەوە",
    },
    "error_required": {
        "en": "Please enter both username and password.",
        "ku": "تکایە ناوی بەکارهێنەر و وشەی نهێنی بنووسە.",
    },
    "error_invalid": {
        "en": "Invalid username or password.",
        "ku": "ناوی بەکارهێنەر یان وشەی نهێنی هەڵەیە.",
    },
    "hint_credentials": {
        "en": "Default: admin / admin",
        "ku": "بە بنەڕەت: admin / admin",
    },
    "auth_todo": {
        "en": "Real authentication (database + hashed passwords) comes in a later step.",
        "ku": "ڕێپێدانی ڕاستەقینە (بنکەی زانیاری و وشەی نهێنی هاشکراو) لە هەنگاوی داهاتوودا دێت.",
    },
    "status_cashier": {
        "en": "Cashier: {name}",
        "ku": "فرۆشیار: {name}",
    },
    # Sidebar navigation
    "dashboard": {"en": "Dashboard", "ku": "داشبۆڕد"},
    "sales": {"en": "Sales", "ku": "فرۆشتن"},
    "sales_history": {"en": "Sales History", "ku": "مێژووی فرۆشتن"},
    "debts": {"en": "Debts", "ku": "قەرزەکان"},
    "suppliers": {"en": "Suppliers", "ku": "دابینکەرەکان"},
    "returns": {"en": "Returns", "ku": "گەڕاوەکان"},
    "reports": {"en": "Reports", "ku": "ڕاپۆرتەکان"},
    "settings": {"en": "Settings", "ku": "ڕێکخستن"},
    # Pages (shared placeholder text)
    "placeholder_text": {
        "en": "This section is a placeholder for now.\nIts content will be built in the next steps.",
        "ku": "ئەم بەشە ئێستا هەڵبەستەیە (placeholder).\nناوەڕۆکەکەی لە هەنگاوە داهاتووەکاندا دروست دەکرێت.",
    },
}


def tr(key: str) -> str:
    """Return the UI string for ``key`` in the configured language.

    Falls back to the English entry, then to the key itself.
    """
    entry = UI_LABELS.get(key)
    if not entry:
        return key
    return entry.get(LANGUAGE) or entry.get("en") or key


# ---------------------------------------------------------------------------
# Global stylesheet (simple modern look: dark sidebar / light content)
# ---------------------------------------------------------------------------
STYLESHEET: str = """
* {
    font-family: "Segoe UI", "Noto Sans Arabic", "Noto Sans", "Tahoma",
                 "DejaVu Sans", sans-serif;
}

/* ---------------------------------------------------------- Login window */
QWidget#loginRoot {
    background-color: #111827;
}
QFrame#loginCard {
    background-color: #ffffff;
    border-radius: 16px;
}
QLabel#loginTitle {
    font-size: 22px;
    font-weight: 700;
    color: #111827;
}
QLabel#loginSub {
    color: #6b7280;
    font-size: 13px;
}
QLabel#fieldLabel {
    color: #374151;
    font-size: 13px;
    font-weight: 600;
}
QPushButton#primaryButton {
    background-color: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 12px;
    font-size: 15px;
    font-weight: 600;
}
QPushButton#primaryButton:hover  { background-color: #1d4ed8; }
QPushButton#primaryButton:pressed { background-color: #1e40af; }
QLabel#errorLabel {
    color: #dc2626;
    font-size: 13px;
}
QLabel#hintLabel {
    color: #9ca3af;
    font-size: 12px;
}

/* -------------------------------------------------------------- Sidebar */
QWidget#sidebar {
    background-color: #1f2937;
}
QLabel#brand {
    color: #ffffff;
    font-size: 17px;
    font-weight: 700;
}
QLabel#brandSub {
    color: #9ca3af;
    font-size: 12px;
}
QPushButton#navButton {
    background-color: transparent;
    color: #d1d5db;
    border: none;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 14px;
    text-align: left;
}
QPushButton#navButton:hover {
    background-color: #374151;
    color: #ffffff;
}
QPushButton#navButton:checked {
    background-color: #2563eb;
    color: #ffffff;
    font-weight: 600;
}
QLabel#clock {
    color: #e5e7eb;
    background-color: #111827;
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 13px;
}

/* ------------------------------------------------------- Content area */
QWidget#content {
    background-color: #f3f4f6;
}
QLabel#pageTitle {
    font-size: 26px;
    font-weight: 700;
    color: #111827;
}
QFrame#placeholderCard {
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
}
QLabel#placeholderText {
    color: #6b7280;
    font-size: 15px;
}

/* ---------------------------------------------------------- Inputs */
QLineEdit {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 14px;
    color: #111827;
}
QLineEdit:focus {
    border: 1px solid #2563eb;
}

/* -------------------------------------------------------- Status bar */
QStatusBar {
    background-color: #ffffff;
    color: #4b5563;
    border-top: 1px solid #e5e7eb;
}
"""