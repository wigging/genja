"""
Static site generator for GitHub Pages.
"""

import argparse
import markdown
import json
from importlib.metadata import version
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from .builder import Builder
from .server import run_server


def main():
    """
    Run the genja program.
    """

    # Command line arguments
    parser = argparse.ArgumentParser(description="Genja static site generator for GitHub Pages")
    parser.add_argument("command", choices=["build", "serve", "clean"], help="genja commands")
    parser.add_argument("-v", "--version", action="version", version=version("genja"))
    args = parser.parse_args()

    # Get configuration from JSON file
    with open("config.json") as json_file:
        config = json.load(json_file)

    print(f'\n{"Command ":.<30} {args.command}')
    print(f'{"Base URL ":.<30} {config["base_url"]}')
    print(f'{"Input directory ":.<30} {config["input_dir"]}')
    print(f'{"Output directory ":.<30} {config["output_dir"]}')

    # Setup the Markdown converter
    md = markdown.Markdown(extensions=["meta", "fenced_code"])

    # Setup the jinja template environment
    env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True)
    md_template = env.get_template("page.html")
    html_template = env.get_template("index.html")
    json_template = env.get_template("feed.json")

    # Build the HTML pages and JSON feed
    builder = Builder(config)
    pages, feeds = builder.build_markdown_pages(md, md_template)
    builder.build_html_pages(html_template, pages)
    builder.build_json_feed(json_template, feeds)

    # Run a local server and open web browser
    if args.command == "serve":
        run_server(config)

    # Clean up (remove) all HTML files and the feed.json file in output directory
    if args.command == "clean":
        output_path = Path(config["output_dir"])

        Path(output_path / "feed.json").unlink()

        for html_file in output_path.glob("**/*.html"):
            html_file.unlink()

        print(f"\nRemoved all HTML files and feed.json in {output_path} directory.")
