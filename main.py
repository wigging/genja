import markdown

md = markdown.Markdown(extensions=['meta'])

with open('example.md', 'r') as file:
    text = file.read()
    html = md.convert(text)
    meta = md.Meta

print(meta)

print(html)
