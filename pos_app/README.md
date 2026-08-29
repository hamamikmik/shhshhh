# POS System (Cashier) — Base Skeleton

Local, offline-friendly Point of Sale (POS) skeleton written in **Python 3.11+**
with **PyQt6**. This step delivers only the *base structure*: the **login
window** and the **main window with sidebar navigation + live clock**.
Business logic (sales, inventory, debts, reports, …) will be built section by
section in the next steps.

## What is included (this step)

- **Login window** (cashier/seller): username + password with inline error
  messages. Placeholder credentials: `admin` / `admin`
  (→ see `app/config.py`, TODO: real authentication later).
- **Main window** with a left **sidebar menu** containing:
  Dashboard · Sales · Sales History · Debts · Suppliers · Returns ·
  Reports · Settings.
- **Content area** on the right using a `QStackedWidget` — one page per
  section, each section having **its own dedicated file**.
- **Live clock** (weekday · date · time) at the bottom of the sidebar,
  refreshed every second via `QTimer` (`app/utils/clock.py`).
- Active menu item highlighting + a simple modern stylesheet (dark sidebar,
  light content) defined in `app/config.py`.
- UI language: **Kurdish (Sorani) by default**, English available — switch
  with the `LANGUAGE` constant in `app/config.py`.

## Requirements

- Python 3.11 or newer
- Only dependency: **PyQt6** (see `requirements.txt`)

## Setup & Run

From the `pos_app` project directory:

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

> Login with the placeholder credentials: **admin / admin**.

## Project structure

```
pos_app/
├── main.py                 # entry point (run this)
├── requirements.txt        # PyQt6 only
├── README.md
└── app/
    ├── __init__.py
    ├── config.py           # settings, labels (en/ku), stylesheet
    ├── utils/
    │   ├── __init__.py
    │   └── clock.py        # format_now() + ClockWidget (live QLabel)
    └── ui/
        ├── __init__.py
        ├── login_window.py # LoginWindow (placeholder auth)
        ├── main_window.py  # MainWindow (sidebar + QStackedWidget)
        ├── sidebar.py      # Sidebar (menu buttons + clock at the bottom)
        └── pages/
            ├── __init__.py         # PAGE_CLASSES registry
            ├── base_page.py        # shared page shell (title + placeholder)
            ├── dashboard_page.py
            ├── sales_page.py
            ├── sales_history_page.py
            ├── debts_page.py
            ├── suppliers_page.py
            ├── returns_page.py
            ├── reports_page.py
            └── settings_page.py
```

## How the pieces fit together

| File | Responsibility |
| --- | --- |
| `main.py` | Shows `LoginWindow`; on success opens `MainWindow` and closes login. |
| `app/ui/sidebar.py` | Builds one checkable button per `NAV_ITEMS` entry; emits `page_selected(key)`; shows `ClockWidget` at the bottom. |
| `app/ui/main_window.py` | Creates sidebar + one page per `PAGE_CLASSES` entry inside a `QStackedWidget`; switches pages on sidebar clicks. |
| `app/ui/pages/*.py` | One `QWidget` subclass per sidebar section (currently title + placeholder layout only). |
| `app/utils/clock.py` | Reusable `ClockWidget` (QLabel + QTimer, 1-second refresh) and `format_now()` helper. |
| `app/config.py` | Navigation items, UI strings (`tr()` localization), placeholder credentials, global stylesheet. |

## Roadmap (next steps)

1. **Database layer** — local SQLite (products, users, invoices, sales,
   debts, suppliers, returns) + a `db` package.
2. **Sales page** — product search, cart, totals, payment, receipt print.
3. **Dashboard** — today's totals, low-stock alerts, quick actions.
4. **Sales History / Returns / Debts / Suppliers / Reports / Settings** —
   fill each remaining section using the same patterns.

## Notes

- The app runs **fully locally/offline** — no web framework, no server.
- Every `TODO` comment marks a place to be implemented in a later step;
  search for `TODO(` to find them all.
- All timestamps are formatted through one helper (`app/utils/clock.py`) so
  invoices and reports stay consistent.