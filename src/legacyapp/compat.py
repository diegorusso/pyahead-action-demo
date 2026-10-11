"""A guarded fallback PyAhead recognises: the handler never runs on 3.9+."""

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


def is_mapping(value):
    return isinstance(value, Mapping)
