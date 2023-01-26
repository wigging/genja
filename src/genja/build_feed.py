from bs4 import BeautifulSoup
from datetime import datetime
from operator import itemgetter
from pathlib import Path


def build_feed(config, md, template):
    """
    Build the JSON feed.
    """

    # Get configuration
    base_url = config['base_url']
    input_dir = config['input_dir']
    output_dir = config['output_dir']

    # Store feed dictionaries for feed.json template
    feeds = []

    # Parse the Markdown files and get metadata for each page
    for mdfile in Path(input_dir).glob('**/*.md'):

        parts = list(mdfile.parts)

        if len(parts) == 3:

            with mdfile.open() as f:
                mdtext = f.read()

            html = md.convert(mdtext)
            meta = md.Meta

            soup = BeautifulSoup(html, 'html.parser')
            url = f'{base_url}/{parts[1]}/{parts[2].replace("md", "html")}'

            feeds.append({
                'url': url,
                'title': meta['title'][0],
                'html': soup.p,
                'date': datetime.strptime(meta['date'][0], '%B %d, %Y').isoformat() + 'Z'
            })

    # Sort feed dictionaries using date
    sorted_feeds = sorted(feeds, key=itemgetter('date'), reverse=True)

    # Write feed.json to output directory
    feed_json = template.render(feeds=sorted_feeds)
    output_path = Path(f'{output_dir}/feed.json')

    with output_path.open('w') as f:
        f.write(feed_json)

    md.reset()
