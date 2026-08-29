"""Reusable clock helpers.

- ``format_now``  — pure function that formats the current date/time.
- ``ClockWidget`` — a QLabel that refreshes itself every second using a
  QTimer, meant for the sidebar (and reusable anywhere else later).
"""

from __future__ import annotations

import datetime as dt
import typing as t

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QLabel, QWidget

# Python's weekday(): Monday=0 ... Sunday=6
WEEKDAYS_EN: tuple[str, ...] = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday",
)
WEEKDAYS_KU: tuple[str, ...] = (
    "دووشەممە", "سێشەممە", "چوارشەممە", "پێنجشەممە",
    "هەینی", "شەممە", "یەکشەممە",
)

_TIME_FORMAT: str = "%Y-%m-%d  %H:%M:%S"


def format_now(*, language: str = "en", include_weekday: bool = True) -> str:
    """Format the current local time, e.g. ``Monday · 2026-08-30 14:22:31``.

    TODO(later): add a 12h option and invoice/timestamp helpers here so all
    date formatting in the app stays consistent.
    """
    now = dt.datetime.now()
    clock = now.strftime(_TIME_FORMAT)
    if not include_weekday:
        return clock
    weekdays = WEEKDAYS_KU if language == "ku" else WEEKDAYS_EN
    return f"{weekdays[now.weekday()]}  ·  {clock}"


class ClockWidget(QLabel):
    """QLabel that shows the live date/time and updates it every second.

    Usage::

        clock = ClockWidget(language="ku", parent=self)
        clock.setObjectName("clock")   # for styling
    """

    def __init__(
        self,
        language: str = "en",
        include_weekday: bool = True,
        parent: t.Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self._language = language
        self._include_weekday = include_weekday

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(1_000)  # milliseconds

        # TODO(cosmetic): sync the first tick to the exact second boundary
        # instead of starting mid-second.
        self._tick()

    def _tick(self) -> None:  # noqa: D401 - "called by the QTimer"
        self.setText(
            format_now(language=self._language, include_weekday=self._include_weekday)
        )

    def stop(self) -> None:
        """Stop the timer (call from the window's closeEvent)."""
        self._timer.stop()

    def start(self) -> None:
        """(Re)start the timer."""
        self._timer.start(1_000)