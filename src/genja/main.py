"""Static site generator for GitHub Pages."""

import argparse
import markdown
import tomllib
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


def remove_files(config):
    """Remove the generated HTML and JSON feed files."""
    markdown_path = Path(config["markdown_dir"])
    template_path = Path(config["template_dir"])
    output_path = Path(config["output_dir"])

    # Get HTML files that were generated from the Markdown files
    p = markdown_path.glob("**/*.md")
    html_files = [x.name.replace("md", "html") for x in p if x.is_file()]

    # Add HTML files that were generated from templates
    p = template_path.glob("**/*.html")
    for x in p:
        if x.name != "markdown.html":
            html_files.append(x.name)

    # Remove the generated JSON feed file in the output directory
    json_path = Path(output_path / "feed.json")

    if json_path.exists():
        json_path.unlink()

    # Remove the generated HTML files in the output directory
    for html_path in output_path.glob("**/*.html"):
        if html_path.name in html_files and html_path.parent != template_path:
            html_path.unlink()

    # Remove empty directories
    for path in output_path.iterdir():
        if path.is_dir() and any(path.iterdir()) is False:
            path.rmdir()

    print(f"\nRemoved generated HTML files and JSON feed file in `{output_path}` directory.")


def main():
    """Run the genja program."""
    # Command line arguments
    parser = argparse.ArgumentParser(description="Genja static site generator for GitHub Pages")
    parser.add_argument("command", choices=["build", "serve", "clean"], help="genja commands")
    parser.add_argument("-v", "--version", action="version", version=version("genja"))
    args = parser.parse_args()

    # Get configuration from TOML file, requires Python 3.11 or higher
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

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

    # Remove generated files in the output directory
    if args.command == "clean":
        remove_files(config)
