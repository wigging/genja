"""Builders module."""

import json
import markdown
import textwrap

from bs4 import BeautifulSoup
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, Template
from operator import itemgetter
from pathlib import Path


def _build_posts(
    config: dict[str, str], template: Template, md: markdown.Markdown
) -> list[dict[str, str]]:
    """Build HTML for posts."""
    base_url = config["base_url"]
    site_output = config["site_output"]
    posts_output = config["posts_output"]

    # Store meta data dictionary for each post
    posts = []

    for path in Path("posts").glob("**/*.md"):
        # Get category, link, url, and post path
        category = path.parts[-2]

        if category != "posts":
            link = f"{posts_output}/{category}/{path.name}".replace("md", "html")
            url = f"{base_url}/{posts_output}/{category}/{path.name}".replace("md", "html")
            post_path = Path(f"{site_output}/{posts_output}/{category}/{path.name}")
        else:
            link = f"{posts_output}/{path.name}".replace("md", "html")
            url = f"{base_url}/{posts_output}/{path.name}".replace("md", "html")
            post_path = Path(f"{site_output}/{posts_output}/{path.name}")

        # Get HTML string for the JSON feed
        with path.open() as f:
            mdtext = f.read()

        html = md.convert(mdtext)
        soup = BeautifulSoup(html, "html.parser")
        html_str = json.dumps(str(soup.p) + f'<p><a href="{url}">Continue reading...</a></p>')

        # Get meta data from the Markdown file
        meta = md.Meta  # pyright: ignore
        title = meta["title"][0]
        long_date = meta["date"][0]
        iso_date = datetime.strptime(meta["date"][0], "%B %d, %Y").isoformat() + "Z"

        # Store the meta data dictionary for the post
        meta_data = {
            "title": title,
            "date": long_date,
            "category": category,
            "link": link,
            "url": url,
            "iso_date": iso_date,
            "html": html_str,
        }

        posts.append(meta_data)

        # Render the post template then write to HTML file
        post_html = template.render(meta=meta_data, content=html)

        post_path = post_path.with_suffix(".html")
        post_path.parent.mkdir(parents=True, exist_ok=True)

        with post_path.open("w") as f:
            f.write(post_html)

        # Reset the Markdown parser
        md.reset()

    return posts


def _build_pages(config: dict[str, str], template: Template, md: markdown.Markdown):
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

        # Render the page template then write to HTML file
        page_html = template.render(content=html)
        page_path.parent.mkdir(parents=True, exist_ok=True)

        with page_path.open("w") as f:
            f.write(page_html)

        # Reset the Markdown parser
        md.reset()


def _build_templates(
    config: dict[str, str], templates: list[Template], names: list[str], posts: list[dict[str, str]]
):
    """Build HTML for certain templates."""
    site_output = config["site_output"]

    # Render the page templates and write to HTML files
    for template, name in zip(templates, names):
        page_html = template.render(posts=posts)
        page_path = Path(f"{site_output}/{name}")

        with page_path.open("w") as f:
            f.write(page_html)


def _build_feed(config: dict[str, str], posts: list[dict[str, str]]):
    """Build the JSON feed."""
    base_url = config["base_url"]
    site_output = config["site_output"]
    title = config["title"]

    # Sort feed dictionaries using date
    sorted_posts = sorted(posts, key=itemgetter("iso_date"), reverse=True)

    # Templates for building JSON feed
    json_start = textwrap.dedent(f"""\
    {{
        "version": "https://jsonfeed.org/version/1.1",
        "title": "{title}",
        "home_page_url": "{base_url}",
        "feed_url": "{base_url}/feed.json",
        "items": [""")

    json_end = textwrap.dedent("""
        ]
    }""")

    # Build the JSON feed and write to a JSON file
    content = ""

    for post in sorted_posts:
        content += f"""
        {{
            "id": "{post['url']}",
            "url": "{post['url']}",
            "title": "{post['title']}",
            "date_published": "{post['iso_date']}",
            "content_html": {post['html']}
        }},"""

    json_feed = json_start + content[:-1] + json_end
    feed_path = Path(f"{site_output}/feed.json")

    with feed_path.open("w") as f:
        f.write(json_feed)


def build_website(config: dict[str, str]):
    """Build the website."""
    # Setup the Markdown converter
    md = markdown.Markdown(extensions=["meta", "fenced_code"])

    # Setup the jinja template environment
    loader = FileSystemLoader("templates")
    env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

    # Build the posts
    post_template = env.get_template("post.html")
    posts = _build_posts(config, post_template, md)

    # Build the pages if they exist
    if Path("templates/page.html").exists() and Path("pages").exists():
        page_template = env.get_template("page.html")
        _build_pages(config, page_template, md)

    # Build certain templates as pages too
    page_names = []
    page_templates = []

    for f in Path("templates").glob("*.html"):
        if f.name != "post.html" and f.name != "page.html" and f.name != "base.html":
            page_template = env.get_template(f.name)
            page_templates.append(page_template)
            page_names.append(f.name)

    _build_templates(config, page_templates, page_names, posts)

    # Build the JSON feed
    _build_feed(config, posts)

    print(f"\nBuilt website in `{config['site_output']}` directory.")
