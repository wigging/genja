"""Tests for the _build_pages function in the builder module."""

from pathlib import Path
from textwrap import dedent

import pytest
from jinja2 import Template

from genja.builder import _build_pages


@pytest.fixture
def temp_pages_dir(tmp_path: Path):
    """Create a temporary _pages directory with sample markdown files."""
    pages_dir = tmp_path / "_pages"
    pages_dir.mkdir()

    page1 = pages_dir / "about.md"
    page2 = pages_dir / "contact.md"

    content1 = dedent("""\
    # About

    This is the about page.

    ## More Info

    Additional content here.""")

    content2 = dedent("""\
    # Contact

    Get in touch with us.""")

    page1.write_text(content1)
    page2.write_text(content2)

    return pages_dir


@pytest.fixture
def template():
    """Create a simple Jinja template for testing."""
    template_str = dedent("""\
    <html><body>{{ content }}</body></html>
    """).strip()
    return Template(template_str)


def test_build_pages_html_files(temp_pages_dir, config, template, mdown, monkeypatch):
    """Test that _build_pages creates HTML files for each markdown page."""
    monkeypatch.chdir(temp_pages_dir.parent)

    _build_pages(config, template, mdown)

    output_dir = Path(config["site_output"])
    assert (output_dir / "about.html").exists()
    assert (output_dir / "contact.html").exists()


def test_build_pages_html_content(temp_pages_dir, config, template, mdown, monkeypatch):
    """Test that _build_pages generates valid HTML content."""
    monkeypatch.chdir(temp_pages_dir.parent)

    _build_pages(config, template, mdown)

    about_file = Path(config["site_output"]) / "about.html"
    html_content = about_file.read_text()

    assert "<h1>About</h1>" in html_content
    assert "This is the about page." in html_content
    assert "<h2>More Info</h2>" in html_content


def test_build_pages_output_dir(temp_pages_dir, config, template, mdown, monkeypatch):
    """Test that _build_pages creates the output directory if it doesn't exist."""
    monkeypatch.chdir(temp_pages_dir.parent)

    output_dir = Path(config["site_output"])
    assert not output_dir.exists()

    _build_pages(config, template, mdown)

    assert output_dir.exists()
    assert output_dir.is_dir()


def test_build_pages_multiple_files(temp_pages_dir, config, template, mdown, monkeypatch):
    """Test that _build_pages processes all markdown files in _pages directory."""
    monkeypatch.chdir(temp_pages_dir.parent)

    _build_pages(config, template, mdown)

    output_dir = Path(config["site_output"])
    html_files = list(output_dir.glob("*.html"))
    assert len(html_files) == 2
