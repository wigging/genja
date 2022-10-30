"""
HTML page generator from markdown files.
"""

import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

CONTENT_PATH = 'content'
SITE_PATH = 'website'
TEMPLATE_FILE = 'template.html'


def parse_markdown(file, md, template):
    """
    Parse the content of the markdown files and write to HTML.
    """
    if file.suffix != '.md':
        return

    with open(file, 'r') as f:
        text = f.read()

    html = md.convert(text)
    meta = md.Meta

    page = template.render(title=meta['title'][0], content=html)

    with open(f'{SITE_PATH}/{file.stem}.html', 'w') as f:
        f.write(page)

    md.reset()


def main():
    """
    Main driver to run the program.
    """
    print(f'\nContent path: {CONTENT_PATH}')
    print(f'Site path: {SITE_PATH}')
    print(f'Template file: {TEMPLATE_FILE}')
    print('Generate HTML files ... ', end='')

    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    env = Environment(loader=FileSystemLoader(SITE_PATH))
    template = env.get_template(TEMPLATE_FILE)

    path = Path(CONTENT_PATH)
    for file in path.iterdir():
        parse_markdown(file, md, template)

    print('Done')
