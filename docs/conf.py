"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import importlib.metadata

# Project information
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Genja"
copyright = "2025, Gavin Wiggins"
author = "Gavin Wiggins"
release = importlib.metadata.version("genja")

# General configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Options for HTML output
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

html_title = "Genja"
html_static_path = ["_static"]
html_logo = "_static/logo200.png"

html_theme_options = {
    "source_repository": "https://github.com/wigging/genja",
    "source_branch": "main",
    "source_directory": "docs/",
}

