# Show help, place this first so it runs with just `make`
help:
	@printf "\nCommands:\n"
	@printf "\033[32mcheck\033[0m    run ruff linter and formatter checks\n"
	@printf "\033[32mclean\033[0m    remove cache directories\n"
	@printf "\033[32mdocs\033[0m     build HTML documentation using Sphinx\n"
	@printf "\033[32mpublish\033[0m  build and upload package to PyPI\n"
	@printf "\033[32mtests\033[0m    run unit tests with pytest\n"

check:
	uv run ruff check .
	uv run ruff format --check .

# Remove cache directories generated by ruff and pytest
# Remove Sphinx build output
clean:
	rm -rf .ruff_cache
	rm -rf .pytest_cache
	uv run sphinx-build -M clean docs docs/_build

# Build the HTML documentation using Sphinx
.PHONY: docs
docs:
	uv run sphinx-build -M html docs docs/_build

# Remove old `dist` directory then build and upload package to PyPI
# See the uploading distribution steps at
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
publish:
	rm -rf dist
	uv build
	uv publish

# Run unit tests using pytest
.PHONY: tests
tests:
	uv run pytest
