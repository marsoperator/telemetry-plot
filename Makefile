test:
	python -m pytest -q tests

clean:
	rm -rf out *.pyc

.PHONY: test clean
