"""Timestamps written before datetime.utcnow was deprecated in Python 3.12."""

from datetime import datetime


def now_utc():
    return datetime.utcnow()
