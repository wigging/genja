# Getting started

Genja is distributed on [PyPI](https://pypi.org/project/genja/). Instructions for installing and using Genja are given below.

## Installation

Genja can be installed with uv as a Python command-line tool. Install uv using the installation instructions at <https://docs.astral.sh/uv/>. Next, install Genja using the following uv command:

```bash
uv tool install genja
```

Check the installed Genja version to make sure installation was successful:

```bash
genja --version
```

You can also run Genja directly with uv using `uv tool run genja` or `uvx genja`. This will run Genja in a temporary environment that is removed when the uv cache is deleted. This approach is slightly more verbose than installing the tool user-wide but either method is suitable.

## Usage

Before running Genja, create a project structure as shown below. Or create a new example project by using the `genja new` command. Markdown files go into the `_pages` and `_posts` directories. The `_pages` directory is for standalone content that is not dated such as an about page or contact page. The `_posts` directory is for dated content such as blog posts or articles. The `_templates` directory contains [Jinja](https://jinja.palletsprojects.com) templates that are used to render the HTML pages and posts. The `mysite` directory contains the built website which can be hosted with GitHub Pages or some other web hosting platform. Lastly, the `genja.toml` defines the URLs and directories for the project.

```text
myproject/
├── mysite/
│   ├── img/
│   └── styles.css
├── _pages/
│   ├── about.md
│   └── contact.md
├── _posts/
│   ├── apple.md
│   └── orange.md
├── _templates/
│   ├── index.html
│   ├── page.html
│   └── post.html
└── genja.toml
```

The items in the `genja.toml` are shown below. The `base_url` is the URL for the homepage of the website. The `posts_output` defines the output directory for the generated HTML posts. All of the HTML files generated from Genja are located in the `site_output` directory. Static content such as images and CSS files should go in this directory. The title of the website is defined by the `title` key.

```toml
base_url = "https://example.com"
posts_output = "blog"
site_output = "mysite"
title = "My Website"
```

Use the `serve` command to build the website and start a local server. This will automatically open the default web browser to view the website. The website will automatically reload when changes are saved to the Markdown files.

```bash
genja serve
```

Use the `build` command to build the website without running a local server.

```bash
genja build
```

Use the `clean` command to remove all the generated HTML files and the JSON feed file.

```bash
genja clean
```
