# Genja

Genja is a simple command line tool that generates HTML files from Markdown files.

## Installation

Install from [PyPI](https://pypi.org) using the following command:

```
pip install genja
```

Check the installed version from the command line:

```
$ genja --version
22.11
```

## Usage

Run genja from the command line by providing the input and output directories as arguments. The input directory contains the Markdown files and must contain a [Jinja](https://jinja.palletsprojects.com/) template file named `template.html`. This template is used to render the generated HTML files. The output directory is where the generated HTML files are written.

```bash
# Run genja where input is `content` directory and output is `website` directory.
# Input directory contains the Markdown files and Jinja template.
# Output directory contains the generated HTML files.
genja content website
```

Output from running the help command `genja --help` is shown below.

```
usage: genja [-h] [-v] input output

Generate HTML files from Markdown files.

positional arguments:
  input          directory of Markdown files and Jinja template
  output         directory for generated HTML files

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

## Example

To run the example, go to the example directory in this repository. Use the `mdcontent` as the input directory and the `website` as the output directory. Notice the template file used by genja is located in the `mdcontent` directory. The index file links to the generated HTML pages. The template and index files are created by the user, not by genja.

```bash
# Run the example
cd example
genja mdcontent website
```

## Contributing

Clone this repository and use the conda environment file to create a Python environment for developing genja. This environment uses [flake8](https://github.com/PyCQA/flake8) for linting and [pytest](https://github.com/pytest-dev/pytest) for running tests. Genja is installed in editable mode within the environment.

```bash
# Clone the project
git clone https://github.com/wigging/genja.git

# Create the conda environment
cd genja
conda env create --file environment.yml

# Activate the conda environment
conda activate genja
```

## License

This project is licensed under the terms of the MIT license. See [here](LICENSE.md) for the license text.
