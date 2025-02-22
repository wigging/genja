# Contributing to Genja

:+1::tada: Thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to the Genja Python package. Submitted code that does not conform to these guidelines will not be merged into the package.

## Development environment

Clone this repository and use the [uv tool](https://docs.astral.sh/uv/) for Python and package management. The environment created by uv uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting along with [pytest](https://docs.pytest.org) for running tests. Genja is installed in editable mode within the environment.

```bash
# Clone this project
git clone https://github.com/wigging/genja.git

# Sync the project environment
uv sync
```

## Code style, linting, and formatting

All Python code in the Genja package should adhere to the [PEP 8](https://peps.python.org/pep-0008/) style guide. All linting and formatting should be implemented with [ruff](https://github.com/astral-sh/ruff). Configuration for ruff is defined in the **pyproject.toml** file.

## Docstrings

All functions, classes, and other Python components should contain docstrings with syntax and best practices outlined by the [NumPy docstring guide](https://numpydoc.readthedocs.io/en/latest/format.html).

## Tests

New code for the Genja package should include associated tests in the **tests** folder. The [pytest](https://github.com/pytest-dev/pytest) framework is used to execute the test files.

## Changelog

Don't forget to edit the changelog based on your contributions. Follow the style on the [Keep a Changelog](https://keepachangelog.com) website.

## Sphinx documentation

New source code along with examples should be documented in the [Sphinx documentation](http://www.sphinx-doc.org/en/stable/) located in the **docs** folder.

## Creating a pull request

Fork this repository and create a new feature branch in the forked repository. Submit a pull request to the **main** branch when your changes and/or fixes are ready for review. Don't forget to use ruff to make sure the code is styled and formatted properly.
