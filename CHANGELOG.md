# Changelog

All notable changes to the genja project are documented in this file. The format of this changelog is based on [Keep a Changelog](https://keepachangelog.com). This project adheres to [Calendar Versioning](https://calver.org) based on `YY.MM.MICRO`.

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
