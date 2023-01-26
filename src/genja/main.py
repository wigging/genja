"""
Generate HTML files from Markdown files.
"""

import argparse
import markdown
import json
from jinja2 import Environment, FileSystemLoader
from importlib.metadata import version

from .build_index import build_index
from .build_pages import build_pages
from .build_feed import build_feed
from .run_server import run_server


def main():
    """
    Main driver to run the genja program.
    """

    # Command line arguments
    parser = argparse.ArgumentParser(description='Generate HTML files from Markdown files.')
    parser.add_argument('command', choices=['build', 'serve'], help='build or serve website')
    parser.add_argument('-v', '--version', action='version', version=version('genja'))
    args = parser.parse_args()

    # Get configuration from JSON file
    with open("config.json") as json_file:
        config = json.load(json_file)

    config['command'] = args.command

    print(f'\n{"Command ":.<30} {config["command"]}')
    print(f'{"Base URL ":.<30} {config["base_url"]}')
    print(f'{"Repository name ":.<30} {config["repo_name"]}')
    print(f'{"Input directory ":.<30} {config["input_dir"]}')
    print(f'{"Output directory ":.<30} {config["output_dir"]}')

    # Setup the Markdown converter
    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    # Setup the jinja template environment
    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
    index_template = env.get_template('index.html')
    page_template = env.get_template('page.html')
    feed_template = env.get_template('feed.json')

    # Build the HTML index and pages
    build_index(config, md, index_template)
    build_pages(config, md, page_template)
    build_feed(config, md, feed_template)

    # Run a local server and open browser if run command is `serve`
    if config['command'] == 'serve':
        run_server(config['output_dir'])
