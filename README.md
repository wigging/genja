# Genja

Genja is a simple static website generator. It is a Python command line tool that generates HTML files and a JSON feed from Markdown content.

Installation
------------

Install uv using the installation steps at https://docs.astral.sh/uv. After installing uv, use the `uv tool` command to install Genja as a command line tool on your computer:

```bash
uv tool install genja
```

Check the installed version from the command line to make sure installation was successful:

```bash
genja --version
```

## Usage

Before running Genja, create a project structure as shown below. Markdown files go into the `_pages` and `_posts` directories. The pages directory is for standalone content that is not dated such as an about page or contact page. The posts directory is for dated content such as blog posts or articles. The `_templates` directory contains [Jinja](https://jinja.palletsprojects.com/) templates that are used to render the HTML pages. The `mysite` directory contains the generated website which can be hosted with GitHub Pages or some other web hosting platform. Lastly, the `genja.toml` file defines the URLs and directories for the project.

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

The items in the `genja.toml` file are shown below. The ``base_url`` is the URL for the homepage of the website. The ``posts_output`` defines the output directory for the generated posts. The HTML files generated from Genja are located in the ``site_output`` directory. Static content such as images and CSS files should go in this directory. The title of the website is defined by the ``title`` key.

```toml
base_url = "https://example.com"
posts_output = "blog"
site_output = "mysite"
title = "My Website"
```

Use the serve command to build the website and start a local server. This will automatically open the default web browser to view the website. The website will automatically reload when changes are saved to the Markdown files.

```bash
genja serve
```

Use the build command to build the website without running a local server.

```bash
genja build
```

## Examples

See the examples directory in this repository for projects that can be built with Genja. For more information about each example, see the Examples section in the [Genja documentation](https://genja.readthedocs.io).

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for information about contributing to this project.

## Support

Support this project by using the **:heart: Sponsor** button at the top of this page. Thank you :smile:.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE.md) document for the license text.
