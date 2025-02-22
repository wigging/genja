# Genja

Genja is a simple static website generator. It is a Python command line tool that generates HTML files and a JSON feed from Markdown content.

Installation
------------

Download and install Python from [python.org](https://www.python.org) or from [Anaconda](https://www.anaconda.com). After installing Python, create and activate a virtual environment as shown below:

```text
python -m venv .venv
source .venv/bin/activate
```

Next, install Genja from [PyPI](https://pypi.org) using the following command:

```text
pip install genja
```

Check the installed version from the command line:

```text
genja --version
```

## Usage

Before running genja, create a project structure as shown below. Markdown files go into the `_pages` and `_posts` directories. The pages directory is for standalone content that is not dated such as an about page or contact page. The posts directory is for dated content such as blog posts or articles. The `_templates` directory contains [Jinja](https://jinja.palletsprojects.com/) templates that are used to render the HTML pages. The `mysite` directory contains the generated website which can be hosted with GitHub Pages or some other web hosting platform. Lastly, the `genja.toml` file defines the URLs and directories for the project.

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

```text
genja serve
```

Use the build command to build the website without running a local server.

```text
genja build
```

## Examples

See the examples directory in this repository for projects that can be built with Genja. For more information about each example, see the Examples section in the [Genja documentation](https://genja.readthedocs.io).

## Contributing

Clone this repository and use the conda environment file to create a Python environment for developing Genja. This environment uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting along with [pytest](https://docs.pytest.org) for running tests. Genja is installed in editable mode within the environment.

```bash
# Clone this project
git clone https://github.com/wigging/genja.git

# Create the conda environment
cd genja
conda env create --file environment.yml

# Activate the conda environment
conda activate genja
```

## Support

Support this project by using the **:heart: Sponsor** button at the top of this page. Thank you :smile:.

## License

This project is licensed under the terms of the MIT license. See [here](LICENSE.md) for the license text.
