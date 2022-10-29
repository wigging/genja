"""
Static site generator.
"""

import markdown
import textwrap
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def parse_markdown(file, md):

    if file.suffix != '.md':
        return

    with open(file, 'r') as f:
        text = f.read()

    html = md.convert(text)
    meta = md.Meta

    print('')
    print(file)
    print(meta)
    print(html)

    env = Environment(loader=FileSystemLoader('htmlcontent'))
    template = env.get_template('template.html')
    page = template.render(title=meta['title'][0], content=html)

    with open(f'htmlcontent/{file.stem}.html', 'w') as f:
        f.write(page)

    md.reset()


def main():
    md = markdown.Markdown(extensions=['meta'])

    path = Path('mdcontent')
    for file in path.iterdir():
        parse_markdown(file, md)


if __name__ == '__main__':
    main()
