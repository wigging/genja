# Genja

Genja is a simple command line tool that generates HTML files from Markdown files.

## Installation

Clone this project and install with pip.

```bash
# Clone the project
git clone https://github.com/wigging/genja.git

# Install with pip
cd genja
pip install .
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
usage: genja [-h] input output

Generate HTML files from Markdown files.

positional arguments:
  input       Directory of Markdown files and Jinja template
  output      Directory for generated HTML files

options:
  -h, --help  show this help message and exit
```

## Example

To run the example, go to the example directory in this repository. Use the `mdcontent` as the input directory and the `website` as the output directory. Notice the template file used by genja is located in the `mdcontent` directory. The index file links to the generated HTML pages. The template and index files are created by the user, not by genja.

```bash
# Run the example
cd example
genja mdcontent website
```

## Contributing

Use the conda environment file to create a Python environment for developing genja.

```bash
# Create the conda environment
conda env create --file environment.yml

# Activate the environment
conda activate genja
```

## License

This project is licensed under the terms of the MIT license. See [here](LICENSE.md) for the license text.
