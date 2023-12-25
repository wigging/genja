"""
Builder class with methods to build the HTML pages and JSON feed.
"""

import json
from datetime import datetime
from pathlib import Path
from operator import itemgetter
from bs4 import BeautifulSoup


class Builder:
    """
    Builder class to create HTML pages and JSON feed.

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
        """
        Initialize with the config dictionary.
        """
        self.base_url = config["base_url"]
        self.input_dir = config["input_dir"]
        self.output_dir = config["output_dir"]

    def build_pages(self, md, template):
        """
        Build root and category HTML pages from Markdown files.

        Parameters
        ----------
        md : x
            Here
        template : x
            Here
        """

        pages = []  # Store page dictionaries for index template
        feeds = []  # Store feed dictionaries for feed template

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
            page_path = Path(*parts).with_suffix(".html")
            page_path.parent.mkdir(parents=True, exist_ok=True)

            # Render the page template then write to HTML file
            catpage = True if len(parts) > 2 else False
            page_html = template.render(meta=meta, content=html, catpage=catpage)

            with page_path.open("w") as f:
                f.write(page_html)

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

            # Reset the Markdown parser
            md.reset()

        return pages, feeds

    def build_index(self, template, pages):
        """
        Build the index HTML page.
        """

        # Sort page dictionaries using category and title
        sorted_pages = sorted(pages, key=itemgetter("category", "title"))

        # Sort page dictionaries by date
        recent_pages = sorted(pages, key=itemgetter("date"), reverse=True)

        # Render the index template then write to HTML file
        index_html = template.render(pages=sorted_pages, recents=recent_pages)
        index_path = Path(f"{self.output_dir}/index.html")

        with index_path.open("w") as f:
            f.write(index_html)

    def build_feed(self, template, feeds):
        """
        Build the JSON feed.
        """

        # Sort feed dictionaries using date
        sorted_feeds = sorted(feeds, key=itemgetter("date"), reverse=True)

        # Render the feed template then write to JSON file
        feed_json = template.render(feeds=sorted_feeds)
        feed_path = Path(f"{self.output_dir}/feed.json")

        with feed_path.open("w") as f:
            f.write(feed_json)
