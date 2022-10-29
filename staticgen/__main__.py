import markdown
from pathlib import Path

md = markdown.Markdown(extensions=['meta'])

with open('content/example.md', 'r') as file:
    text = file.read()
    html = md.convert(text)
    meta = md.Meta

print(meta)
print(html)

path = Path('content')

for f in path.iterdir():
    print(f)

    with open(f, 'r') as file:
        text = file.read()
        html = md.convert(text)
        meta = md.Meta

    print(meta)
    print(html)
