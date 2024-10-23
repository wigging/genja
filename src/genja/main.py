"""Static site generator for GitHub Pages."""

import argparse
import markdown
import json
from importlib.metadata import version
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from .builder import Builder
from .server import run_server


def run_builder(config):
    """Build the website."""

    # Setup the Markdown converter
    md = markdown.Markdown(extensions=["meta", "fenced_code"])

    # Setup the jinja template environment and get the Markdown and JSON templates
    loader = FileSystemLoader(config["template_dir"])
    env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    md_template = env.get_template("markdown.html")
    json_template = env.get_template("feed.json")

    # Get the HTML file names and templates
    html_names = []
    html_templates = []

    for f in Path(config["template_dir"]).glob("*.html"):
        if f.name != "markdown.html":
            html_template = env.get_template(f.name)
            html_templates.append(html_template)
            html_names.append(f.name)

    # Build the Markdown pages, HTML pages, and JSON feed
    builder = Builder(config)
    md_pages, feeds = builder.build_markdown_pages(md_template, md)
    builder.build_html_pages(html_templates, html_names, md_pages)
    builder.build_json_feed(json_template, feeds)

    print(f"\nBuilt website in `{config['output_dir']}` directory.")


def main():
    """Run the genja program."""

    # Command line arguments
    parser = argparse.ArgumentParser(description="Genja static site generator for GitHub Pages")
    parser.add_argument("command", choices=["build", "serve", "clean"], help="genja commands")
    parser.add_argument("-v", "--version", action="version", version=version("genja"))
    args = parser.parse_args()

    # Get configuration from JSON file
    with open("config.json") as json_file:
        config = json.load(json_file)

    print(f'\n{"Genja command ":.<30} {args.command}')
    print(f'{"Base URL ":.<30} {config["base_url"]}')
    print(f'{"Markdown directory ":.<30} {config["markdown_dir"]}')
    print(f'{"Template directory ":.<30} {config["template_dir"]}')
    print(f'{"Output directory ":.<30} {config["output_dir"]}')

    # Build the website
    if args.command == "build":
        run_builder(config)

    # Build the website then run a local server and open web browser
    if args.command == "serve":
        run_builder(config)
        run_server(config)

    # Clean up (remove) all HTML files and the feed.json file in output directory
    if args.command == "clean":
        output_path = Path(config["output_dir"])
        template_path = Path(config["template_dir"])

        Path(output_path / "feed.json").unlink()

        for html_path in output_path.glob("**/*.html"):
            if config["output_dir"] != ".":
                html_path.unlink()
            elif html_path.parent != template_path and html_path.name != "index.html":
                html_path.unlink()

        print(f"\nRemoved all HTML files and feed.json in `{output_path}` directory.")
