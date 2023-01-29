"""
Static site generator for GitHub Pages.
"""

import argparse
import markdown
import json
from jinja2 import Environment, FileSystemLoader
from importlib.metadata import version

from .builder import Builder
from .server import run_server


def main():
    """
    Main driver to run the genja program.
    """

    # Command line arguments
    parser = argparse.ArgumentParser(description='Static site generator for GitHub Pages.')
    parser.add_argument('command', choices=['build', 'serve'], help='build or serve website')
    parser.add_argument('-v', '--version', action='version', version=version('genja'))
    args = parser.parse_args()

    # Get configuration from JSON file
    with open("config.json") as json_file:
        config = json.load(json_file)

    print(f'\n{"Command ":.<30} {args.command}')
    print(f'{"Base URL ":.<30} {config["base_url"]}')
    print(f'{"Repository name ":.<30} {config["repo_name"]}')
    print(f'{"Input directory ":.<30} {config["input_dir"]}')
    print(f'{"Output directory ":.<30} {config["output_dir"]}')

    # Setup the Markdown converter
    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    # Setup the jinja template environment
    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
    page_template = env.get_template('page.html')
    index_template = env.get_template('index.html')
    feed_template = env.get_template('feed.json')

    # Build the HTML pages and JSON feed
    builder = Builder(config, args.command)
    pages, feeds = builder.build_pages(md, page_template)
    builder.build_index(index_template, pages)
    builder.build_feed(feed_template, feeds)

    # Run a local server and open browser if run command is `serve`
    if args.command == 'serve':
        run_server(config['output_dir'])
