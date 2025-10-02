# Examples

Examples are available in the `genja/examples` directory in the Genja [GitHub](https://github.com/wigging/genja) repository. Use the `genja build` or `genja serve` command to generate the HTML for a particular example. For instance, use the command shown below to build the website and run a local server for the `directory-output` example. The website will automatically reload in the web browser when changes are saved to the Markdown files.

```bash
cd examples/directory-output
genja serve
```

Alternatively, use the build command to build the website without starting a local server.

```bash
cd examples/directory-output
genja build
```

## Code blocks

The `code-blocks` example demonstrates the use of [highlight.js](https://highlightjs.org) to provide syntax coloring of code that is rendered in pages and posts. The CSS and JavaScript for hightlightjs must be defined in the `<head>...</head>` section in the HTML page or post template such as:

```html
<!-- Highlightjs -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
```

Next, code blocks can be defined in the Markdown files as follows:

````markdown
```python
def seyhello():
    s = "hello there"
    print(s)
```
````

## Directory output

The `directory-output` example defines `site_output = "mysite"` in the `genja.toml` file. This tells Genja to output the generated content to the `mysite` directory in the project.

```text
directory-output/
├── _pages/
├── _posts/
├── _templates/
├── mysite/      <-- output from Genja will go in this directory
└── genja.toml
```

## HTML content

The `html-content` example demonstrates putting HTML in the Markdown file. The `about.md` in the example uses the `<figure>` element to display an image with a caption.

```html
<figure>
  <img src="images/homer-simpson.jpg" alt="Homer Simpson" />
  <figcaption>An image of Homer Simpson is in this figure.</figcaption>
</figure>
```

The same is done in the `apple.md` post but notice the path to the image file is adjusted for the post.

```html
<figure>
  <img src="../images/apple.jpg" alt="an apple" />
  <figcaption>This is an image of an apple.</figcaption>
</figure>
```

## Image files

The `image-files` example shows how to embed images in the Markdown file. This is accomplished as shown below but notice the path to the image file may vary for pages and posts.

```markdown
![Homer Simpson](images/homer-simpson.jpg)
```

## Pages and posts

The `pages-and-posts` examples demonstrates creating pages and posts as Markdown files. Pages reside in the `_pages` directory while posts reside in the `_posts` directory.

## Root output

The `root-output` example generates the HTML website content at the root level of the project. This is defined in the `genja.toml` config file by setting the `site_output` to the current working directory as shown below:

```toml
base_url = "https://example.com"
posts_output = "blog"
site_output = "."
title = "My Website"
```

## Sort posts

The `sort-posts` example shows how to sort posts by date, category, or tag. A demonstration of sorting only recent posts is also given. This is accomplished with the Jinja template engine. See the [Template Designer Documentation](https://jinja.palletsprojects.com/en/stable/templates/) for more information about creating Jinja templates.

