install-local-package:
	uv pip install -e .

format:
	ruff format

clean:
	rm -rf src/rlist.egg-info
