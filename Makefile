.PHONY: build upload

build:
	python setup.py sdist

upload:
	twine upload dist/tianqiai-*.tar.gz
	rm dist/tianqiai-*.tar.gz

