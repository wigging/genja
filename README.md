# Genja

Genja is a simple static website generator. It is a command line tool built in Python that generates HTML files and a JSON feed from Markdown content.

## Installation

Download and install Python from [python.org](https://www.python.org) or from [Anaconda](https://www.anaconda.com). Next, install Genja from [PyPI](https://pypi.org) using the following command:

```text
pip install genja
```

Check the installed version from the command line:

```text
genja --version
```

## Usage

Before running Genja, create a project structure as shown below. The `content` directory contains Markdown files that are used to generate HTML files. The `templates` directory contains [Jinja2](https://jinja.palletsprojects.com/) templates that are used to render the HTML pages. The `docs` directory contains the generated website which can be hosted with GitHub Pages. Lastly, the `config.toml` defines the base URL and directories for the project.

```text
mywebsite/
|- content/
|- templates/
|- docs/
|- config.toml
```

The items in the `config.toml` are shown below. The `base_url` is the URL for the homepage of the website. Markdown files that are parsed by Genja are located in the `markdown_dir` directory. The Jinja2 templates used by Genja are located in the `template_dir` directory. The HTML files generated from Genja are located in the `output_dir` directory. Static content such as images and CSS files should go in the output directory.

```toml
base_url = "https://example.com/mywebsite"
markdown_dir = "content"
template_dir = "templates"
output_dir = "docs"
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

See the `examples` directory in this repository for two example projects that can be built with Genja. The `directory-website` example uses the `website` directory for the generated output. The `toplevel-output` example uses the top-level of the project for the generated output.

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
