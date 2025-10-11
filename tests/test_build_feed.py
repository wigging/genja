"""Tests for the _build_feed function in the builder module."""

import json
from pathlib import Path

import pytest

from genja.builder import _build_feed


@pytest.fixture
def sample_posts():
    """Create sample posts data for testing."""
    return [
        {
            "title": "First Post",
            "date": "January 1, 2024",
            "url": "https://example.com/posts/first-post.html",
            "iso_date": "2024-01-01T00:00:00Z",
            "html": (
                '"<p>First post content.</p>'
                '<p><a href=\\"https://example.com/posts/first-post.html\\">'
                'Continue reading...</a></p>"'
            ),
        },
        {
            "title": "Second Post",
            "date": "February 15, 2024",
            "url": "https://example.com/posts/second-post.html",
            "iso_date": "2024-02-15T00:00:00Z",
            "html": (
                '"<p>Second post content.</p>'
                '<p><a href=\\"https://example.com/posts/second-post.html\\">'
                'Continue reading...</a></p>"'
            ),
        },
        {
            "title": "Third Post",
            "date": "March 10, 2024",
            "url": "https://example.com/posts/third-post.html",
            "iso_date": "2024-03-10T00:00:00Z",
            "html": (
                '"<p>Third post content.</p>'
                '<p><a href=\\"https://example.com/posts/third-post.html\\">'
                'Continue reading...</a></p>"'
            ),
        },
    ]


@pytest.fixture
def feed_config(tmp_path: Path):
    """Create a test configuration for the feed."""
    return {
        "base_url": "https://example.com",
        "site_output": str(tmp_path / "_site"),
        "title": "Test Blog",
    }


def test_build_feed_creates_json_file(feed_config, sample_posts):
    """Test that _build_feed creates a feed.json file."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, sample_posts)

    feed_path = site_output / "feed.json"
    assert feed_path.exists()


def test_build_feed_valid_json(feed_config, sample_posts):
    """Test that _build_feed creates valid JSON."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, sample_posts)

    feed_path = site_output / "feed.json"
    feed_content = feed_path.read_text()

    feed_data = json.loads(feed_content)
    assert isinstance(feed_data, dict)


def test_build_feed_structure(feed_config, sample_posts):
    """Test that _build_feed creates feed with correct structure."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, sample_posts)

    feed_path = site_output / "feed.json"
    feed_data = json.loads(feed_path.read_text())

    assert feed_data["version"] == "https://jsonfeed.org/version/1.1"
    assert feed_data["title"] == "Test Blog"
    assert feed_data["home_page_url"] == "https://example.com"
    assert feed_data["feed_url"] == "https://example.com/feed.json"
    assert "items" in feed_data


def test_build_feed_items_count(feed_config, sample_posts):
    """Test that _build_feed includes all posts."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, sample_posts)

    feed_path = site_output / "feed.json"
    feed_data = json.loads(feed_path.read_text())

    assert len(feed_data["items"]) == 3


def test_build_feed_sorted_by_date(feed_config, sample_posts):
    """Test that _build_feed sorts posts by date in reverse chronological order."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, sample_posts)

    feed_path = site_output / "feed.json"
    feed_data = json.loads(feed_path.read_text())

    items = feed_data["items"]
    assert items[0]["title"] == "Third Post"
    assert items[1]["title"] == "Second Post"
    assert items[2]["title"] == "First Post"


def test_build_feed_item_structure(feed_config, sample_posts):
    """Test that each feed item has the correct structure."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, sample_posts)

    feed_path = site_output / "feed.json"
    feed_data = json.loads(feed_path.read_text())

    item = feed_data["items"][0]
    assert "id" in item
    assert "url" in item
    assert "title" in item
    assert "date_published" in item
    assert "content_html" in item


def test_build_feed_item_content(feed_config, sample_posts):
    """Test that feed items contain correct content."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, sample_posts)

    feed_path = site_output / "feed.json"
    feed_data = json.loads(feed_path.read_text())

    item = feed_data["items"][2]
    assert item["id"] == "https://example.com/posts/first-post.html"
    assert item["url"] == "https://example.com/posts/first-post.html"
    assert item["title"] == "First Post"
    assert item["date_published"] == "2024-01-01T00:00:00Z"
    assert "First post content" in item["content_html"]


def test_build_feed_empty_posts(feed_config):
    """Test that _build_feed handles empty posts list."""
    site_output = Path(feed_config["site_output"])
    site_output.mkdir(parents=True, exist_ok=True)

    _build_feed(feed_config, [])

    feed_path = site_output / "feed.json"
    feed_data = json.loads(feed_path.read_text())

    assert feed_data["items"] == []
