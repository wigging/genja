# Genja

Genja is a simple static site generator for GitHub Pages. It is a command line tool built in Python that generates HTML files and a JSON feed from Markdown content.

## Installation

Download and install Python from [python.org](https://www.python.org) or from [Anaconda](https://www.anaconda.com). Next, install genja from [PyPI](https://pypi.org) using the following command:

```
pip install genja
```

Check the installed version from the command line:

```
genja --version
```

## Usage

Before running genja, create a project structure as shown below. The `content` directory contains Markdown files that are used to generate HTML files. The `templates` directory contains [Jinja](https://jinja.palletsprojects.com/) templates that are used to render the HTML pages. The `docs` directory contains the built website which can be hosted with GitHub Pages. Lastly, the `config.json` defines the URLs and directories for the project.

```
mywebsite/
|- content/
|- templates/
|- docs/
|- config.json
```

The items in the `config.json` are shown below. The `base_url` is the URL for the homepage of the website. Markdown files that are parsed by genja are located in the `input_dir` directory. The HTML files generated from genja are located in the `output_dir` directory. Static content such as images and CSS files should go in the output directory.

```json
{
    "base_url": "https://example.com/mywebsite",
    "input_dir": "content",
    "output_dir": "docs"
}
```

Use the serve command to build the website and start a local server. This will automatically open the default web browser to view the website. The website will automatically reload when changes are saved to the Markdown files.

```
genja serve
```

Use the build command to build the website without running a local server.

```
genja build
```

## Example

To run the example, go to the `example` directory in this repository. The `mdcontent` folder is the input directory containing the Mardkown files. The `website` folder is the output directory containing the built HTML files. Use the commands shown below to build the website and run a local server to view the website in the default web browser. The website will automatically reload in the web browser when changes are saved to the Markdown files.

```
cd example
genja serve
```

Use the commands shown below to build the example website without starting a local server.

```
cd example
genja build
```

## Contributing

Clone this repository and use the conda environment file to create a Python environment for developing genja. This environment uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting along with [pytest](https://docs.pytest.org) for running tests. Genja is installed in editable mode within the environment.

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
