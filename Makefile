install-local-package:
	uv pip install -e .

format:
	ruff format

lint:
	ruff check --exclude src/rlist/tests/cpython

type-check:
	uv run ty check --exclude src/rlist/tests/

clean:
	rm -rf src/rlist.egg-info

test-cpython:
	uv run python -m unittest -v src/rlist/tests/cpython/test_rlist.py
