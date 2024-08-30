.PHONY: install virtualenv ipython clean test pflake8

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration

test:
	@.venv/bin/pytest -vv -s

watch:
	#@.venv/bin/ptw -- -vv -s
	ls **/*.py | entr pytest

clean:				##Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycahe__' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@find -rf .cache
	@find -rf .pytest_cache
	@find -rf .mypy_cache
	@find -rf build
	@find -rf dist
	@find -rf *.egg-info
	@find -rf htmlcov
	@find -rf .tox/
	@find -rf docs/_build
