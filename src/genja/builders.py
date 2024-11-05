"""Builders module."""

from operator import itemgetter
from pathlib import Path


def build_posts(config, template, md) -> list[dict]:
    """Build HTML for posts."""
    base_url = config["base_url"]
    site_output = config["site_output"]
    posts_output = config["posts_output"]

    # Store meta data dictionary for each post
    posts = []

    for path in Path("posts").glob("**/*.md"):
        # Read text content of the Markdown file
        with path.open() as f:
            mdtext = f.read()

        # Convert Markdown content to HTML content
        html = md.convert(mdtext)

        # Get metadata from the Markdown file
        meta = md.Meta
        meta_data = {
            "title": meta["title"][0],
            "date": meta["date"][0],
            "category": path.parts[-2],
            "link": f"{posts_output}/{path.name}".replace("md", "html"),
            "url": f"{base_url}/{posts_output}/{path.name}".replace("md", "html"),
        }
        posts.append(meta_data)

        # Create new HTML path for the post
        post_path = Path(f"{site_output}/{posts_output}/{path.name}")
        post_path = post_path.with_suffix(".html")

        # Render the post template then write to HTML file
        post_html = template.render(meta=meta_data, content=html)
        post_path.parent.mkdir(parents=True, exist_ok=True)

        with post_path.open("w") as f:
            f.write(post_html)

        # Reset the Markdown parser
        md.reset()

    return posts


def build_pages(config, template, md):
    """Build HTML for pages."""
    site_output = config["site_output"]

    for path in Path("pages").glob("**/*.md"):
        # Read text content of the Markdown file
        with path.open() as f:
            mdtext = f.read()

        # Convert Markdown content to HTML content
        html = md.convert(mdtext)

        # Create new HTML path for the page
        page_path = Path(f"{site_output}/{path.name}")
        page_path = page_path.with_suffix(".html")

        # Render the post template then write to HTML file
        page_html = template.render(content=html)
        page_path.parent.mkdir(parents=True, exist_ok=True)

        with page_path.open("w") as f:
            f.write(page_html)

        # Reset the Markdown parser
        md.reset()


def build_templates(config, templates, names, posts):
    """Build HTML for certain templates."""
    site_output = config["site_output"]

    # Sort page dictionaries using category and title
    sorted_posts = sorted(posts, key=itemgetter("category", "title"))

    # Render the index template then write to HTML file
    for template, name in zip(templates, names):
        page_html = template.render(posts=sorted_posts)
        page_path = Path(f"{site_output}/{name}")

        with page_path.open("w") as f:
            f.write(page_html)
