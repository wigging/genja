"""
Generate HTML files from Markdown files.
"""

import argparse
import markdown
import json
import webbrowser
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from importlib.metadata import version
from operator import itemgetter
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler


def run_server(config):
    """
    Run local server for viewing the website.
    """

    server_address = ('localhost', 9000)
    handler = partial(SimpleHTTPRequestHandler, directory=config['output_dir'])
    httpd = HTTPServer(server_address, handler)

    print('Serving at http://localhost:9000')
    webbrowser.open('http://localhost:9000')

    httpd.serve_forever()


def build_index(config, md, template):
    """
    Build the index.html page.
    """

    # Get configuration
    command = config['command']
    repo_name = config['repo_name']
    input_dir = config['input_dir']
    output_dir = config['output_dir']

    # Set base url based on run command
    if command == 'serve':
        base_url = ''
    else:
        base_url = '/' + repo_name

    # Store items for the index.html template
    items = []

    for path in Path(input_dir).glob('**/*.md'):

        with path.open() as f:
            mdtext = f.read()

        _ = md.convert(mdtext)
        meta = md.Meta

        parts = list(path.parts)

        if len(parts) > 2:
            section = parts[1]
            link = f'/{parts[1]}/{parts[2].replace("md", "html")}'
            title = meta['title'][0]
            items.append({'section': section, 'link': link, 'title': title})

    # Sort the items using section and title
    sorted_items = sorted(items, key=itemgetter('section', 'title'))

    # Write index.html to output directory
    index_html = template.render(base_url=base_url, items=sorted_items)
    output_path = Path(f'{output_dir}/index.html')

    with output_path.open('w') as f:
        f.write(index_html)

    md.reset()


def build_pages(config, md, template):
    """
    Parse content of Markdown files and write to HTML files. If needed,
    subfolders are created too.
    """

    # Get configuration
    command = config['command']
    repo_name = config['repo_name']
    input_dir = config['input_dir']
    output_dir = config['output_dir']

    # Set base url based on run command
    if command == 'serve':
        base_url = ''
    else:
        base_url = '/' + repo_name

    # Parse markdown files and build website pages
    for mdfile in Path(input_dir).glob('**/*.md'):

        with mdfile.open() as f:
            mdtext = f.read()

        if command == 'serve':
            html = md.convert(mdtext)
        else:
            html = md.convert(mdtext)
            html = html.replace('/img', base_url + '/img')

        meta = md.Meta
        page = template.render(base_url=base_url, data=meta, content=html)

        parts = list(mdfile.parts)
        parts[0] = output_dir
        pathout = Path(*parts).with_suffix('.html')
        pathout.parent.mkdir(parents=True, exist_ok=True)

        with pathout.open('w') as f:
            f.write(page)

        md.reset()


def main():
    """
    Main driver to run the program.
    """

    parser = argparse.ArgumentParser(description='Generate HTML files from Markdown files.')
    parser.add_argument('command', choices=['build', 'serve'], help='build or serve website')
    parser.add_argument('-v', '--version', action='version', version=version('genja'))
    args = parser.parse_args()

    # Get configuration from JSON file
    with open("config.json") as json_file:
        config = json.load(json_file)

    config['command'] = args.command

    print(f'\n{"Command ":.<30} {config["command"]}')
    print(f'{"Repository name ":.<30} {config["repo_name"]}')
    print(f'{"Input directory ":.<30} {config["input_dir"]}')
    print(f'{"Output directory ":.<30} {config["output_dir"]}')
    print(f'{"Generate HTML files ":.<30} ', end='')

    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
    index_template = env.get_template('index.html')
    page_template = env.get_template('page.html')

    build_index(config, md, index_template)
    build_pages(config, md, page_template)

    print('DONE\n')

    if config['command'] == 'serve':
        run_server(config)
