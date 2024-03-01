clean:
	rm -rf .ruff_cache

# Check for formatter errors using ruff
format:
	ruff format --check .

# Check for linter errors using ruff
lint:
	ruff check .

# Build and publish package to PyPI
publish:
	python -m build
	twine upload dist/*
