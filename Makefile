.PHONY: build upload

build:
	python setup.py sdist

upload:
	twine upload dist/zhipuai-*.tar.gz
	rm dist/zhipuai-*.tar.gz

