install-local-package:
	uv pip install -e .

format:
	ruff format

clean:
	rm -rf src/rlist.egg-info

test-cpython:
	uv run python -m unittest -v src/rlist/tests/cpython/test_rlist.py
