"""
Tests for the Builder class.
"""

from genja.builder import Builder


def test_init():
    """
    Test the Builder init.
    """
    config = {
        "base_url": "https://example.com/testsite",
        "markdown_dir": "mdcontent",
        "template_dir": "templates",
        "output_dir": "website"
    }

    builder = Builder(config)
    assert builder.base_url == "https://example.com/testsite"
    assert builder.markdown_dir == "mdcontent"
    assert builder.output_dir == "website"
