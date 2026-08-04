"""Sanity and baseline package tests for reg-ai-engine."""

import reg_ai_engine


def test_package_import_and_version() -> None:
    """Verify package imports correctly and exposes a valid version string."""
    assert reg_ai_engine.__version__ == "0.1.0"
