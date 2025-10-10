"""Shared fixtures for tests."""

from pathlib import Path

import markdown
import pytest


@pytest.fixture
def config(tmp_path: Path):
    """Create a test configuration."""
    return {
        "base_url": "https://example.com",
        "site_output": str(tmp_path / "_site"),
        "posts_output": "posts",
    }


@pytest.fixture(scope="session")
def mdown():
    """Create a Markdown converter with extensions."""
    return markdown.Markdown(extensions=["meta", "fenced_code"])
