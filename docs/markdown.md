# Markdown content

Genja uses Markdown files to create the content for HTML pages and posts. See the sections below for more information about writing page and post content in Markdown. All of the basic Markdown syntax and features are supported by Genja.

## Page content

The `_pages` directory is for standalone content that is not dated such as an about page or contact page. The content of a Markdown file that represents an about page is shown below. Notice there is no metadata defined at the top of the file.

```markdown
# About

Hi, I’m Homer Simpson. By day, I dive into the world of coding—building
projects, solving problems, and tinkering with new technologies. By weekend,
you’ll probably find me on a hiking trail, enjoying fresh air and the
occasional snack break. This site is my space to share what I’m learning,
making, and exploring, both in front of a screen and out in nature.

![Homer Simpson](images/homer-simpson.jpg)
```

## Post content

The `_posts` directory is for dated content such as blog posts or articles. The content of a Markdown file that represents a blog post is shown below. The metadata for the post is defined at the top of the Markdown file. The allowed keys for the metadata are `title`, `date`, `categories`, and `tags`. Code blocks are also supported in the Markdown content.

````text
---
title: Apple
date: November 19, 2020
---

Apples are crisp, sweet (or tart) fruits that come in a rainbow of varieties,
from bright red to golden yellow and fresh green. They’re enjoyed fresh,
baked into pies, pressed into cider, or even dried for a chewy snack. Packed
with fiber, vitamins, and antioxidants, apples have been a staple in diets
around the world for centuries—proving that sometimes the simplest foods are
the most timeless.

Below is an example of a Python function. Syntax highlighting is supported
in the rendered HTML content.

```python
def sayhello():
    """A function that prints a string."""
    s = 'Hello there'
    print(s)
```
````
