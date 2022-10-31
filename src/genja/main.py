"""
Generate HTML files from Markdown files.
"""

import argparse
import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def parse_markdown(file, md, template, output):
    """
    Parse the content of the markdown files and write to HTML files.
    """
    if file.suffix != '.md':
        return

    with open(file, 'r') as f:
        text = f.read()

    html = md.convert(text)
    meta = md.Meta

    page = template.render(data=meta, content=html)

    with open(f'{output}/{file.stem}.html', 'w') as f:
        f.write(page)

    md.reset()


def main():
    """
    Main driver to run the program.
    """
    parser = argparse.ArgumentParser(description='Generate HTML files from Markdown files.')
    parser.add_argument('input', help='markdown directory')
    parser.add_argument('output', help='html directory')
    args = parser.parse_args()

    print(f'\n{"Markdown directory ":.<30} {args.input}')
    print(f'{"HTML directory ":.<30} {args.output}')
    print(f'{"Template file ":.<30} {args.input}/template.html')
    print(f'{"Generate HTML files ":.<30} ', end='')

    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    env = Environment(loader=FileSystemLoader(args.output))
    template = env.get_template('template.html')

    path = Path(args.input)
    for file in path.iterdir():
        parse_markdown(file, md, template, args.output)

    print('DONE')
