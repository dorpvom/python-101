.PHONY: default
default: tests

.PHONY: all
all: tests

.PHONY: tests
tests:
	PYTHONPATH=src/ pytest -vv --import-mode=importlib test

