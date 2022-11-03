"""
Generate HTML files from Markdown files.
"""

import argparse
import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def parse_markdown(pathin, output, md, template):
    """
    Parse content of Markdown files and write to HTML files. Folders are
    created for categories.
    """
    for mdfile in pathin.glob('*.md'):

        with mdfile.open() as f:
            text = f.read()

        html = md.convert(text)
        meta = md.Meta

        page = template.render(data=meta, content=html)

        if 'category' in meta:
            folder = Path(f'{output}/{meta["category"][0]}')
            folder.mkdir(parents=True, exist_ok=True)

            pathout = folder / f'{mdfile.stem}.html'
            with pathout.open('w') as f:
                f.write(page)
        else:
            pathout = Path(f'{output}/{mdfile.stem}.html')

            with pathout.open('w') as f:
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

    pathin = Path(args.input)
    parse_markdown(pathin, args.output, md, template)

    print('DONE')
