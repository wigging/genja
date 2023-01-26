from pathlib import Path
from operator import itemgetter


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

    # Store page dictionaries for index.html template
    pages = []

    # Parse the Markdown files and get metadata for each page
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
            pages.append({'section': section, 'link': link, 'title': title})

    # Sort page dictionaries using section and title
    sorted_pages = sorted(pages, key=itemgetter('section', 'title'))

    # Write index.html to output directory
    index_html = template.render(base_url=base_url, pages=sorted_pages)
    output_path = Path(f'{output_dir}/index.html')

    with output_path.open('w') as f:
        f.write(index_html)

    md.reset()
