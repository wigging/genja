# Changelog

All notable changes to the genja project are documented in this file. The format of this changelog is based on [Keep a Changelog](https://keepachangelog.com). This project adheres to [Calendar Versioning](https://calver.org) based on `YY.MM.MICRO`.

## Genja v25.2

#### Changed

- Prepend directories used by Genja with an underscore. The directories are `_pages`, `_posts`, and `_templates`.
- Configuration file is now `genja.toml` instead of `config.toml`
- Use uv instead of conda for Python and package management

## Genja v24.11

#### Added

- The `genja new` command creates a new example project
- Contributing guidelines
- Use `base.html` as the base template if it exists
- Templates page in documentation

#### Changed

- Use single Makefile at root of project instead of the Makefile in docs
- Build JSON feed from template strings instead of template file
- Refactor all examples for latest package changes

## Genja v24.10

#### Added

- Require Python version 3.12 or higher
- Improve the `genja clean` command to remove all generated files
- Add `template_dir` in config file
- Put examples into subdirectories

#### Changed

- Use TOML instead of JSON for config file
- Change `input_dir` to `markdown_dir` in config file

## Genja v24.3

#### Added

- A Makefile for running various project command line tools
- Sphinx for generating documentation which is hosted with Read the Docs
- A `genja clean` command to remove all HTML files and feed.json in the output directory

## Genja v24.2

#### Added

- The `meta["url"]` is now available for page templates. This provides the URL for the page which can be used in things like [Open Graph](https://www.opengraph.xyz) meta tags.
- Example includes Open Graph meta tags in head section

## Genja v23.12

#### Added

- A `recents` variable for the index template. This can be used to create a list on the home page for recent articles. See the example for a demonstration.

#### Changed

- Change from flake8 to ruff for linting and formating

## Genja v23.3

Breaking changes are in this release so please upgrade from previous versions.

#### Added

- The `genja serve` command now runs a local server using the livereload package. This will automatically reload the website in the browser when changes to the Markdown files are saved.

#### Changed

- Folders in the input directory are considered categories instead of sections. Consequently, the index template must use the `page.category` variable instead of `page.section`.

## Genja v23.2

#### Fixed

- In the example, use relative paths in Markdown and HTML templates
- Ensure relative paths are used within genja

#### Removed

- Remove the repo_name item from the config.json

## Genja v23.1

Breaking changes in this release. Please upgrade from the previous version.

#### Added

- Configuration file `config.json` that defines the base URL, repository name, input directory, and output directory
- JSON feed to allow people to subscribe to the website
- Server for viewing the website in the default web browser

#### Changed

- Command line arguments are now `build` and `serve`

#### Removed

- Command line arguments `input` and `output`

## Genja v22.11

Initial release of the genja command line tool.
