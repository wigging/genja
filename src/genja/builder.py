from datetime import datetime
from pathlib import Path
from operator import itemgetter
from bs4 import BeautifulSoup


class Builder:

    def __init__(self, config, command):

        # Set attributes
        self.command = command
        self.base_url = config['base_url']
        self.input_dir = config['input_dir']
        self.output_dir = config['output_dir']

        # Set repo url attribute based on run command
        if command == 'serve':
            self.repo_url = ''
        else:
            self.repo_url = '/' + config['repo_name']

    def build_pages(self, md, template):
        """
        Build root and section HTML pages from Markdown files.
        """

        # Store page dictionaries for index template
        pages = []

        # Store feed dictionaries for feed template
        feeds = []

        # Parse the Markdown files and build HTML pages
        for path in Path(self.input_dir).glob('**/*.md'):

            # Read text content of the Markdown file
            with path.open() as f:
                mdtext = f.read()

            # Convert Markdown content to HTML
            if self.command == 'serve':
                html = md.convert(mdtext)
            else:
                html = md.convert(mdtext)
                html = html.replace('/img', self.repo_url + '/img')

            # Get metadata from the Markdown file
            meta = md.Meta

            # Render the page template then write to HTML file
            page_html = template.render(repo_url=self.repo_url, meta=meta, content=html)

            parts = list(path.parts)
            parts[0] = self.output_dir
            page_path = Path(*parts).with_suffix('.html')
            page_path.parent.mkdir(parents=True, exist_ok=True)

            with page_path.open('w') as f:
                f.write(page_html)

            # Store dictionaries for category pages
            if len(parts) > 2:

                # Get page dictionary for index template
                section = parts[1]
                link = f'/{parts[1]}/{parts[2].replace("md", "html")}'
                title = meta['title'][0]
                pages.append({'section': section, 'link': link, 'title': title})

                # Get feed dictionary for feed template
                soup = BeautifulSoup(html, 'html.parser')
                url = f'{self.base_url}/{parts[1]}/{parts[2].replace("md", "html")}'

                feeds.append({
                    'url': url,
                    'title': meta['title'][0],
                    'html': soup.p,
                    'date': datetime.strptime(meta['date'][0], '%B %d, %Y').isoformat() + 'Z'
                })

            # Reset the Markdown parser
            md.reset()

        return pages, feeds

    def build_index(self, template, pages):
        """
        Build the index.html page.
        """

        # Sort page dictionaries using section and title
        sorted_pages = sorted(pages, key=itemgetter('section', 'title'))

        # Render the index template then write to HTML file
        index_html = template.render(repo_url=self.repo_url, pages=sorted_pages)
        index_path = Path(f'{self.output_dir}/index.html')

        with index_path.open('w') as f:
            f.write(index_html)

    def build_feed(self, template, feeds):
        """
        Build the JSON feed.
        """

        # Sort feed dictionaries using date
        sorted_feeds = sorted(feeds, key=itemgetter('date'), reverse=True)

        # Render the feed template then write to JSON file
        feed_json = template.render(feeds=sorted_feeds)
        feed_path = Path(f'{self.output_dir}/feed.json')

        with feed_path.open('w') as f:
            f.write(feed_json)
