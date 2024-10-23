"""Builder class with methods to build the HTML pages and JSON feed."""

import json
from datetime import datetime
from pathlib import Path
from operator import itemgetter
from bs4 import BeautifulSoup


class Builder:
    """Builder class to create HTML pages and JSON feed.

    Attributes
    ----------
    base_url : str
        Base URL for the GitHub repository.
    input_dir : str
        Path to the Markdown content.
    output_dir : str
        Path where the HTML content is generated.
    """

    def __init__(self, config: dict[str, str]):
        """Initialize with the config dictionary."""
        self.base_url = config["base_url"]
        self.input_dir = config["input_dir"]
        self.output_dir = config["output_dir"]

    def build_markdown_pages(self, template, md):
        """Build the Markdown HTML pages."""

        pages = []  # Store page dictionaries for Markdown and HTML templates
        feeds = []  # Store feed dictionaries for JSON feed template

        # Parse the Markdown files and build HTML pages
        for path in Path(self.input_dir).glob("**/*.md"):
            # Read text content of the Markdown file
            with path.open() as f:
                mdtext = f.read()

            # Convert Markdown content to HTML
            html = md.convert(mdtext)

            # Get metadata from the Markdown file
            meta = md.Meta

            # Get path parts and create the HTML path
            parts = list(path.parts)
            parts[0] = self.output_dir

            # Store dictionaries for category pages
            if len(parts) > 2:
                # Get page dictionary for index template
                category = parts[1]
                link = f'{parts[1]}/{parts[2].replace("md", "html")}'
                title = meta["title"][0]
                date = meta["date"][0]
                iso_date = datetime.strptime(date, "%B %d, %Y").isoformat() + "Z"

                pages.append({"category": category, "link": link, "title": title, "date": iso_date})

                # Get feed dictionary for feed template
                soup = BeautifulSoup(html, "html.parser")
                url = f'{self.base_url}/{parts[1]}/{parts[2].replace("md", "html")}'
                cont_reading = f'<p><a href="{url}">Continue reading...</a></p>'
                html_str = json.dumps(str(soup.p) + cont_reading)

                feeds.append({"url": url, "title": title, "html": html_str, "date": iso_date})
            else:
                url = f'{self.base_url}/{parts[1].replace("md", "html")}'

            # Render the page template then write to HTML file
            catpage = True if len(parts) > 2 else False
            meta["url"] = url
            page_html = template.render(meta=meta, content=html, catpage=catpage)

            page_path = Path(*parts).with_suffix(".html")
            page_path.parent.mkdir(parents=True, exist_ok=True)

            with page_path.open("w") as f:
                f.write(page_html)

            # Reset the Markdown parser
            md.reset()

        return pages, feeds

    def build_html_pages(self, templates, names, pages):
        """Build the other HTML pages.

        Parameters
        ----------
        templates : list of jinja templates
            The templates used to render each HTML file.
        names : list of str
            HTML file names associated with the templates. These file names
            are written to the output directory.
        pages : list of dict
            The dictionaries that describe the Markdown pages.
        """

        # Sort page dictionaries using category and title
        sorted_pages = sorted(pages, key=itemgetter("category", "title"))

        # Sort page dictionaries by date
        recent_pages = sorted(pages, key=itemgetter("date"), reverse=True)

        # Render the index template then write to HTML file
        for template, name in zip(templates, names):
            html_render = template.render(pages=sorted_pages, recents=recent_pages)
            html_path = Path(f"{self.output_dir}/{name}")

            with html_path.open("w") as f:
                f.write(html_render)

    def build_json_feed(self, template, feeds):
        """Build the JSON feed."""

        # Sort feed dictionaries using date
        sorted_feeds = sorted(feeds, key=itemgetter("date"), reverse=True)

        # Render the feed template then write to JSON file
        feed_json = template.render(feeds=sorted_feeds)
        feed_path = Path(f"{self.output_dir}/feed.json")

        with feed_path.open("w") as f:
            f.write(feed_json)
