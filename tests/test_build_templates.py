"""Tests for the _build_templates function in the builder module."""

from pathlib import Path
from textwrap import dedent

import pytest
from jinja2 import Template

from genja.builder import _build_templates


@pytest.fixture
def templates():
    """Create sample Jinja templates for testing."""
    template1_str = dedent("""\
    <html>
    <body>
    <h1>Index</h1>
    <ul>
    {% for post in posts %}
    <li><a href="{{ post.link }}">{{ post.title }}</a></li>
    {% endfor %}
    </ul>
    </body>
    </html>
    """).strip()

    template2_str = dedent("""\
    <html>
    <body>
    <h1>Archive</h1>
    {% for post in posts %}
    <p>{{ post.title }} - {{ post.date }}</p>
    {% endfor %}
    </body>
    </html>
    """).strip()

    return [Template(template1_str), Template(template2_str)]


@pytest.fixture
def template_names():
    """Return sample template names."""
    return ["index.html", "archive.html"]


@pytest.fixture
def sample_posts():
    """Create sample post metadata."""
    return [
        {
            "title": "First Post",
            "date": "January 1, 2024",
            "link": "posts/first-post.html",
            "url": "https://example.com/posts/first-post.html",
        },
        {
            "title": "Second Post",
            "date": "January 2, 2024",
            "link": "posts/second-post.html",
            "url": "https://example.com/posts/second-post.html",
        },
    ]


def test_build_templates_html_files(config, templates, template_names, sample_posts):
    """Test that _build_templates creates HTML files."""
    output_dir = Path(config["site_output"])
    output_dir.mkdir(parents=True, exist_ok=True)

    _build_templates(config, templates, template_names, sample_posts)

    assert (output_dir / "index.html").exists()
    assert (output_dir / "archive.html").exists()


def test_build_templates_html_content(config, templates, template_names, sample_posts):
    """Test that _build_templates generates valid HTML content."""
    output_dir = Path(config["site_output"])
    output_dir.mkdir(parents=True, exist_ok=True)

    _build_templates(config, templates, template_names, sample_posts)

    index_file = Path(config["site_output"]) / "index.html"
    html_content = index_file.read_text()

    assert "<h1>Index</h1>" in html_content
    assert "First Post" in html_content
    assert "Second Post" in html_content
    assert "posts/first-post.html" in html_content


def test_build_templates_renders_posts(config, templates, template_names, sample_posts):
    """Test that _build_templates renders posts in templates."""
    output_dir = Path(config["site_output"])
    output_dir.mkdir(parents=True, exist_ok=True)

    _build_templates(config, templates, template_names, sample_posts)

    archive_file = Path(config["site_output"]) / "archive.html"
    html_content = archive_file.read_text()

    assert "First Post - January 1, 2024" in html_content
    assert "Second Post - January 2, 2024" in html_content


def test_build_templates_multiple_files(config, templates, template_names, sample_posts):
    """Test that _build_templates processes all templates."""
    output_dir = Path(config["site_output"])
    output_dir.mkdir(parents=True, exist_ok=True)

    _build_templates(config, templates, template_names, sample_posts)

    html_files = list(output_dir.glob("*.html"))
    assert len(html_files) == 2


def test_build_templates_empty_posts(config, templates, template_names):
    """Test that _build_templates handles empty posts list."""
    output_dir = Path(config["site_output"])
    output_dir.mkdir(parents=True, exist_ok=True)

    _build_templates(config, templates, template_names, [])

    index_file = Path(config["site_output"]) / "index.html"
    assert index_file.exists()

    html_content = index_file.read_text()
    assert "<h1>Index</h1>" in html_content
