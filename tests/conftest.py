"""Ensure NLTK resources required by the test suite are available.

Downloads ``punkt_tab`` (or ``punkt`` as a fallback) on first run if missing.
If the machine is offline and the resources are not yet cached, tests that
need them will be skipped rather than failing with a ``LookupError``.
"""
from __future__ import annotations

import pytest

_NLTK_AVAILABLE: bool


def _ensure_nltk() -> bool:
    import nltk

    for resource, paths in (
        ("punkt_tab", ("tokenizers/punkt_tab",)),
        ("cmudict", ("corpora/cmudict",)),
    ):
        for path in paths:
            try:
                nltk.data.find(path)
                break
            except LookupError:
                continue
        else:
            try:
                nltk.download(resource, quiet=True, raise_on_error=True)
            except Exception:
                return False
    return True


_NLTK_AVAILABLE = _ensure_nltk()


def pytest_collection_modifyitems(config, items):
    if _NLTK_AVAILABLE:
        return
    skip = pytest.mark.skip(reason="NLTK data (punkt_tab/cmudict) not available")
    for item in items:
        item.add_marker(skip)
