"""
Static site generator.
"""

import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def parse_markdown(file, md, template):

    if file.suffix != '.md':
        return

    with open(file, 'r') as f:
        text = f.read()

    html = md.convert(text)
    meta = md.Meta

    page = template.render(title=meta['title'][0], content=html)

    with open(f'htmlcontent/{file.stem}.html', 'w') as f:
        f.write(page)

    md.reset()


def main():
    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    env = Environment(loader=FileSystemLoader('htmlcontent'))
    template = env.get_template('template.html')

    path = Path('mdcontent')
    for file in path.iterdir():
        parse_markdown(file, md, template)


if __name__ == '__main__':
    main()
