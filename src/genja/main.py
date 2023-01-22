"""
Generate HTML files from Markdown files.
"""

import argparse
import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from importlib.metadata import version
from operator import itemgetter


def build_index(args, md, template):
    """
    Build the index.html page.
    """

    # Get input and output directories
    input_dir = args.input
    output_dir = args.output

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
    index_html = template.render(items=sorted_items)
    output_path = Path(f'{output_dir}/index.html')

    with output_path.open('w') as f:
        f.write(index_html)

    md.reset()


def build_pages(args, md, template):
    """
    Parse content of Markdown files and write to HTML files. If needed,
    subfolders are created too.
    """

    # Get input and output directories
    input_dir = args.input
    output_dir = args.output

    for mdfile in Path(input_dir).glob('**/*.md'):

        with mdfile.open() as f:
            mdtext = f.read()

        html = md.convert(mdtext)
        meta = md.Meta
        page = template.render(data=meta, content=html)

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
    parser.add_argument('input', help='directory of Markdown files')
    parser.add_argument('output', help='directory for generated HTML files')
    parser.add_argument('-v', '--version', action='version', version=version('genja'))
    args = parser.parse_args()

    print(f'\n{"Markdown directory ":.<30} {args.input}')
    print(f'{"HTML directory ":.<30} {args.output}')
    print(f'{"Generate HTML files ":.<30} ', end='')

    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
    index_template = env.get_template('index.html')
    page_template = env.get_template('page.html')

    build_index(args, md, index_template)
    build_pages(args, md, page_template)

    print('DONE')
