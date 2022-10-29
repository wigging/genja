import markdown


def parse_markdown(file):

    if file.suffix != '.md':
        return

    md = markdown.Markdown(extensions=['meta'])

    with open(file, 'r') as f:
        text = f.read()
        html = md.convert(text)
        meta = md.Meta

    print('')
    print(file)
    print(meta)
    print(html)
