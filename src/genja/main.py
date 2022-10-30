"""
Generate HTML files from markdown files.
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

    page = template.render(title=meta['title'][0], content=html)

    with open(f'{output}/{file.stem}.html', 'w') as f:
        f.write(page)

    md.reset()


def main():
    """
    Main driver to run the program.
    """
    parser = argparse.ArgumentParser(description='Generate HTML files from markdown files.')
    parser.add_argument('input', help='markdown directory')
    parser.add_argument('output', help='html directory')
    args = parser.parse_args()

    print(f'\nMarkdown directory: {args.input}')
    print(f'HTML directory: {args.output}')
    print(f'Template file: {args.input}/template.html')
    print('Generate HTML files ... ', end='')

    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    env = Environment(loader=FileSystemLoader(args.output))
    template = env.get_template('template.html')

    path = Path(args.input)
    for file in path.iterdir():
        parse_markdown(file, md, template, args.output)

    print('Done')
