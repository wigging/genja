from pathlib import Path


def build_pages(config, md, template):
    """
    Build root and section HTML pages from Markdown files.
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

    # Parse the Markdown files and build HTML pages
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
