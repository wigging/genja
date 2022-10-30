# Genger

Genger is a simple command line tool that generates HTML files from markdown files.

## Installation

Clone this project and install with pip.

```bash
# Clone the project
git clone x

# Install with pip
cd genger
pip install .
```

## Usage

Run genger from the command line by providing the input and output directories as arguments. The input directory contains the markdown files. The output directory is where the generated HTML files are written.

```bash
# Run genger where input is `content` directory and output is `website` directory.
# Input directory contains the markdown files.
# Output directory contains the generated HTML files.
genger content website
```

Output from running the help command `genger --help` is shown below.

```
usage: genger [-h] input output

Generate HTML files from markdown files.

positional arguments:
  input       markdown directory
  output      html directory

options:
  -h, --help  show this help message and exit
```

## Contributing

Use the conda environment file to create a Python environment for developing genger. See the commands below for creating and activating the environment.

```bash
# Create the conda environment
conda env create --file environment.yml

# Activate the environment
conda activate genger
```
