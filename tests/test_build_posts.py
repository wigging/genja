"""Tests for the _build_posts function in the builder module."""

import json
from pathlib import Path
from textwrap import dedent

import pytest
from jinja2 import Template

from genja.builder import _build_posts


@pytest.fixture
def temp_posts_dir(tmp_path: Path):
    """Create a temporary _posts directory with sample markdown files."""
    posts_dir = tmp_path / "_posts"
    posts_dir.mkdir()

    post1 = posts_dir / "test-post-1.md"

    subdir = posts_dir / "articles"
    subdir.mkdir()
    post2 = subdir / "test-post-2.md"

    content1 = dedent("""\
    ---
    title: Test Post 1
    date: January 1, 2024
    categories: python, testing
    tags: pytest, markdown
    ---

    This is the first test post.

    ## Section 1

    Some content here.""")

    content2 = dedent("""\
    ---
    title: Test Post 2
    date: February 15, 2024
    ---

    This is the second test post in a subdirectory.""")

    post1.write_text(content1)
    post2.write_text(content2)

    return posts_dir


@pytest.fixture
def template():
    """Create a simple Jinja template for testing."""
    template_str = dedent("""\
    <html><head><title>{{ meta.title }}</title></head><body>{{ content }}</body></html>
    """).strip()
    return Template(template_str)


def test_build_posts_html_files(temp_posts_dir, config, template, mdown, monkeypatch):
    """Test that _build_posts creates HTML files for each markdown post."""
    monkeypatch.chdir(temp_posts_dir.parent)

    posts = _build_posts(config, template, mdown)
    assert len(posts) == 2

    output_dir = Path(config["site_output"]) / config["posts_output"]
    assert (output_dir / "test-post-1.html").exists()
    assert (output_dir / "articles" / "test-post-2.html").exists()


def test_build_posts_metadata(temp_posts_dir, config, template, mdown, monkeypatch):
    """Test that _build_posts returns correct metadata for each post."""
    monkeypatch.chdir(temp_posts_dir.parent)

    posts = _build_posts(config, template, mdown)

    post1 = next(p for p in posts if p["title"] == "Test Post 1")
    assert post1["date"] == "January 1, 2024"
    assert post1["categories"] == ["python", "testing"]
    assert post1["tags"] == ["pytest", "markdown"]
    assert post1["link"] == "posts/test-post-1.html"
    assert post1["url"] == "https://example.com/posts/test-post-1.html"
    assert post1["iso_date"] == "2024-01-01T00:00:00Z"

    post2 = next(p for p in posts if p["title"] == "Test Post 2")
    assert post2["date"] == "February 15, 2024"
    assert post2["categories"] == ["none"]
    assert post2["tags"] == ["none"]
    assert post2["link"] == "posts/articles/test-post-2.html"
    assert post2["url"] == "https://example.com/posts/articles/test-post-2.html"


def test_build_posts_html_content(temp_posts_dir, config, template, mdown, monkeypatch):
    """Test that _build_posts generates valid HTML content."""
    monkeypatch.chdir(temp_posts_dir.parent)

    _build_posts(config, template, mdown)

    output_file = Path(config["site_output"]) / config["posts_output"] / "test-post-1.html"
    html_content = output_file.read_text()

    assert "<title>Test Post 1</title>" in html_content
    assert "This is the first test post." in html_content
    assert "<h2>Section 1</h2>" in html_content


def test_build_posts_json_feed(temp_posts_dir, config, template, mdown, monkeypatch):
    """Test that _build_posts creates JSON-compatible HTML strings."""
    monkeypatch.chdir(temp_posts_dir.parent)

    posts = _build_posts(config, template, mdown)

    post1 = next(p for p in posts if p["title"] == "Test Post 1")
    html_str = json.loads(post1["html"])

    assert "This is the first test post." in html_str
    assert 'href="https://example.com/posts/test-post-1.html"' in html_str
    assert "Continue reading..." in html_str


def test_build_posts_subdirs(temp_posts_dir, config, template, mdown, monkeypatch):
    """Test that _build_posts creates necessary subdirectories."""
    monkeypatch.chdir(temp_posts_dir.parent)

    _build_posts(config, template, mdown)

    output_dir = Path(config["site_output"]) / config["posts_output"] / "articles"
    assert output_dir.exists()
    assert output_dir.is_dir()
