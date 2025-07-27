install-local-package:
	uv pip install -e .

format:
	ruff format

lint:
	ruff check --exclude src/rlist/tests/cpython

type-check:
	uv run ty check --exclude src/rlist/tests/

test-cpython:
	uv run python -m unittest -v src/rlist/tests/cpython/test_rlist.py

test:
	uv run python -m unittest -v src/rlist/tests/test_rlist.py

start-doc-server:
	uv run python -m mkdocs serve

deploy-documentation:
	uv run python -m mkdocs gh-deploy --config-file mkdocs.yml

build:
	uv build

clean:
	rm -rf dist src/rlist.egg-info

publish:
	uv publish

