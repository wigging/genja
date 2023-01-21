"""
Generate HTML files from Markdown files.
"""

import argparse
import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from importlib.metadata import version


def parse_markdown(indir, outdir, md, template):
    """
    Parse content of Markdown files and write to HTML files. If needed,
    subfolders are created too.
    """
    for mdfile in Path(indir).glob('**/*.md'):

        with mdfile.open() as f:
            mdtext = f.read()

        html = md.convert(mdtext)
        meta = md.Meta
        page = template.render(data=meta, content=html)

        parts = list(mdfile.parts)
        parts[0] = outdir
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
    print(f'{"Template file ":.<30} {args.input}/template.html')
    print(f'{"HTML directory ":.<30} {args.output}')
    print(f'{"Generate HTML files ":.<30} ', end='')

    md = markdown.Markdown(extensions=['meta', 'fenced_code'])

    env = Environment(loader=FileSystemLoader('templates'))
    page_template = env.get_template('page.html')

    parse_markdown(args.input, args.output, md, page_template)

    print('DONE')
